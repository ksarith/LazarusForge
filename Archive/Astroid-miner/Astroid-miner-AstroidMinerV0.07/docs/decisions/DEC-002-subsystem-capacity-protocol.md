# DEC-002 — Canonical Subsystem `capacity()` Protocol

**Status: RESOLVED — option (a) chosen and implemented, 2026-08-12**
**Affects:** `src/astroid_miner/models/power_subsystem.py` (MDL-PWR-01), `src/astroid_miner/models/zero_g_subsystem_swarm_v3.py` (MDL-SWR-03, `ConstraintSolver`)
**Raised:** Phase 3.1 audit (V0.03.1); analyzed for resolution here (V0.06)

## The situation

Every subsystem the authoritative `ConstraintSolver` (MDL-SWR-03) actually calls implements:

```python
def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
```

`global_state` is a dict built up incrementally during `solve_cycle()`: Power's capacity is computed
first and written into it, then Anchor reads `global_state['cohesion_force']`, Mining/Refining/
Fabrication chain off upstream values the same way. It's a single-cycle, cross-subsystem
accumulator — not a history or a counter.

`power_subsystem.py`'s standalone `PowerSubsystem` (MDL-PWR-01) instead implements:

```python
def capacity(self, swarm_mass: float, params: Dict, cycle: int = 0) -> float:
```

Here `cycle` is used for exactly one thing — an exponential degradation factor:
`(1 - power_degradation_per_cycle) ** cycle`. It is a scalar elapsed-cycle counter, not a
cross-subsystem state dict. Passing `ConstraintSolver`'s `global_state` dict into this parameter
as-is would silently break (`dict ** int` type error, or worse, silently wrong if coerced).

## Analysis

The two signatures aren't solving genuinely different problems — `cycle` is strictly narrower than
`global_state`. Every other authoritative subsystem's `capacity()` only needs *this-cycle*
cross-subsystem values; `PowerSubsystem` additionally wants a *cycle-count* for aging. Nothing
about the swarm model's existing five subsystems is incompatible with also carrying a cycle count
through `global_state` — none of them currently use one, and adding an unused key does not affect
their behavior.

## Options

**(a) Generalize the solver: `capacity(swarm_mass, params, global_state)` becomes the sole
canonical protocol.** `solve_cycle()` gains a `cycle` parameter (already present as an unused
parameter on `Optimizer.py`'s caller, currently ignored — see note below) and writes it into
`global_state['cycle']` before calling any subsystem. `PowerSubsystem.capacity()` is rewritten to
read `cycle = global_state.get('cycle', 0)` instead of taking it positionally. This makes
`PowerSubsystem` a drop-in replacement for `ConstraintSolver`'s own internal `PowerSubsystem` class
— genuinely useful, since the standalone file has richer physics (HTS penalty, transmission
efficiency, degradation) that the solver's built-in `PowerSubsystem` currently lacks entirely.

**(b) Keep `PowerSubsystem` as a deliberately separate, non-integrated model.** Leave both
signatures as they are, document permanently (not just provisionally) that MDL-PWR-01 is a
standalone power-budget calculator and not a `ConstraintSolver` subsystem, and stop treating the
signature mismatch as an open defect — reclassify it as an intentional scope boundary instead.

**(c) Do nothing yet; leave DEC-002 open.** Same posture as DEC-001 before resolution — no cost to
waiting, but the defect stays flagged as unresolved rather than being either fixed or reclassified.

## Recommendation

**Option (a).** Unlike DEC-001, this isn't a resource-priority tradeoff — it's a small, mechanical,
low-risk change with a concrete payoff: the swarm model's built-in `PowerSubsystem` class (inside
`zero_g_subsystem_swarm_v3.py`) is currently a much simpler model than the standalone one (no HTS
penalty, no transmission efficiency, no degradation curve). Reconciling the signatures lets the
richer standalone model actually replace the solver's built-in one, which is a genuine capability
gain, not just a cleanup.

**Estimated blast radius if (a) is chosen:**
- `zero_g_subsystem_swarm_v3.py`: `solve_cycle()` gains a `cycle: int = 0` parameter, sets
  `global_state['cycle'] = cycle` before the first `capacity()` call. Non-breaking — existing
  callers that don't pass `cycle` get `0`, identical to current behavior.
- `power_subsystem.py`: `capacity()` signature changes to `(swarm_mass, params, global_state)`,
  body changes one line (`cycle = global_state.get('cycle', 0)`).
- `tests/test_optimizer_interface.py`: `test_power_subsystem_standalone` needs updating to call
  with a `global_state` dict instead of `cycle=1`.
- No changes needed to `Optimizer.py`, `parameters/swarm_v3.yaml`, or any other model.

This was not applied automatically. Per the same discipline as DEC-001, a decision with observable
downstream effects (even a small one) gets recorded and confirmed before code changes, not applied
silently under the banner of "obviously correct."

## Resolution

- **Decision:** Option (a) — generalize the solver's cycle handling; `PowerSubsystem.capacity()`
  now takes `(swarm_mass, params, global_state)` matching every other authoritative subsystem.
- **Rationale:** confirmed by reading the code that `cycle` was strictly narrower than
  `global_state` (used only for one degradation exponent), and that the standalone `PowerSubsystem`
  is a strictly richer model (HTS penalty, transmission efficiency, degradation curve) than
  `ConstraintSolver`'s built-in one — reconciling the signatures was a genuine capability gain, not
  just cleanup.
- **Date:** 2026-08-12
- **Implementation:**
  - `zero_g_subsystem_swarm_v3.py`: `solve_cycle()` gained `cycle: int = 0`, sets
    `global_state['cycle'] = cycle` before any subsystem is called. Confirmed non-breaking: default
    `cycle=0` reproduces prior behavior exactly for all existing callers.
  - `power_subsystem.py`: `capacity()` signature changed to `(swarm_mass, params, global_state)`;
    reads `cycle = global_state.get('cycle', 0)` internally.
  - Verified as a genuine drop-in replacement, not just a type-compatible stub: wired the richer
    `PowerSubsystem` directly into a live `ConstraintSolver` and confirmed `power_available` drops
    from 68.9 → 60.7 across 5 cycles due to the degradation curve actually taking effect.
  - Added `test_power_subsystem_wired_into_solver` to `tests/test_optimizer_interface.py`, which
    asserts this degradation behavior directly (not just "doesn't crash"). Full suite: 11/11 passing.
- **Follow-up actions:**
  - `MODELS.md` / `REGISTRY.md` status for MDL-PWR-01 updated to reflect full solver integration.
  - `ConstraintSolver`'s own simpler built-in `PowerSubsystem` class (inside
    `zero_g_subsystem_swarm_v3.py`) was left as-is — this decision made the standalone model
    *usable* as a replacement, it did not force the swap. Whether to actually substitute it as the
    default in `solve_cycle()`'s example/self-test usage is a separate, smaller follow-up, not
    bundled into this decision.

## Follow-up — CapacityResult hard interface (V0.08)

Implemented in `src/astroid_miner/models/contracts.py`:

- `CapacityResult` dataclass: `capacity`, `subsystem_id`, `units`, `limiting_factor`, `provenance`, optional `meta`
- `SubsystemProtocol` structural contract
- `coerce_capacity()` helper for numeric extraction

All production subsystems under `src/astroid_miner/models/` that participate in the constraint graph now return `CapacityResult` from `capacity(swarm_mass, params, global_state)`. `ConstraintSolver.solve_cycle()` stores numeric values in `global_state` for downstream math and exposes the structured results under `capacity_results`.

Contract tests: `tests/test_subsystem_contract.py`.
