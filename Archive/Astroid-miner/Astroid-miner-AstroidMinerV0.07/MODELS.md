# Computational Model Diagnostic & Dependency Audit
## V0.03 (Phase 3 — post-restructuring)

| Model ID     | Module File (current path)                                  | Status Class                  | Authority          | Executability  | Lineage / Relationship                  |
|--------------|---------------------------------------------------------------|--------------------------------|---------------------|----------------|------------------------------------------|
| MDL-OPT-01   | `src/astroid_miner/optimization/optimizer.py`                | Interface-Repaired Sketch     | Exploratory        | EXEC-PARTIAL   | Phase 2 interface alignment; Phase 3 import path updated |
| MDL-PWR-01   | `src/astroid_miner/models/power_subsystem.py`                | Fully Integrated (DEC-002)    | Authoritative-Model | EXEC-FULL     | **DEC-002, 2026-08-12**: `capacity()` reconciled to `(swarm_mass, params, global_state)`; verified as a real drop-in replacement for the solver's own simpler PowerSubsystem via a degradation-behavior test |
| MDL-REP-01   | `src/astroid_miner/models/replication_model.py`               | Base Replication Model        | Authoritative-Model| EXEC-FULL      | Base exponential expansion loop         |
| MDL-SIM-01   | `src/astroid_miner/models/zero_g_simulator.py`                | Physics Engine                | Authoritative-Model| EXEC-FULL      | Zero-G collision & thruster physics     |
| MDL-SWR-01   | `experiments/deprecated/zero_g_subsystem_swarm_v1.py`         | Swarm Constraint Model v1     | Deprecated          | EXEC-FULL      | Superseded by MDL-SWR-03                |
| MDL-SWR-03   | `src/astroid_miner/models/zero_g_subsystem_swarm_v3.py`       | Swarm Constraint Model v3     | Authoritative-Model| EXEC-FULL      | Primary swarm bottleneck solver; verified via `solve_cycle()` smoke test |
| MDL-MC-01    | `experiments/deprecated/dynamic_optimizer_monte_carlo_v1.py`  | Monte Carlo Engine v1         | Deprecated          | EXEC-FULL      | Superseded by MDL-MC-02                 |
| MDL-MC-02    | `experiments/monte_carlo/dynamic_monte_carlo_optimized.py`    | Deprecated per DEC-001        | Deprecated          | INERT-SKETCH   | **DEC-001 (b), 2026-08-12**: formally deprecated rather than repaired — see decision record |
| MDL-MC-03    | `experiments/monte_carlo/monte_carlo_asteroid_comparison.py`  | Deprecated per DEC-001        | Deprecated          | INERT-SKETCH   | **DEC-001 (b), 2026-08-12**: same disposition as MDL-MC-02 |
| MDL-GRA-04   | `experiments/deprecated/replication_constraint_graph_v4_silicate.py` | Deprecated per DEC-001 | Deprecated | INERT-SKETCH   | **DEC-001 (b), 2026-08-12**: formally deprecated; see `docs/decisions/DEC-001-silicate-pathway.md` |

---

## DEC-001 Resolution (2026-08-12)

MDL-GRA-04, MDL-MC-02, and MDL-MC-03 are now formally **DEPRECATED** per `docs/decisions/DEC-001-silicate-pathway.md`, option (b). This is a status upgrade from the Phase 3.1 `EXPLORATORY` classification — deprecation is stronger and signals "do not build on this, and don't expect it to be repaired soon" rather than merely "unvalidated." Each file now carries a top-of-file docstring notice pointing back to the decision record. No code logic was changed as part of this resolution — files were retained for provenance. In August 2026 MDL-GRA-04 was relocated from `src/astroid_miner/models/` to `experiments/deprecated/` so it is no longer on the importable package path. The decision can be reopened later if something in the swarm/optimizer/parameter layer develops an actual dependency on silicate-pathway output.

## Phase 3.1 Findings — MDL-GRA-04 downgrade and MC-02/03 disposition

**MDL-GRA-04 was misclassified `AUTHORITATIVE-MODEL | EXEC-FULL` on the basis of a successful `import`, not a successful `solve_cycle()` call.** Direct execution against a real `Asteroid` and `ConstraintSolver({"base_fab_yield": 0.65})` raises `NameError: name 'processed_raw_kg' is not defined` immediately. The method body also contains `'active_bottleneck': ...` — a literal ellipsis placeholder, not executable logic. This is now downgraded to `EXPLORATORY | INERT-SKETCH` and covered by a test (`test_replication_constraint_graph_v4_silicate_is_known_broken`) that asserts the exact failure so it can't silently regress or silently start "passing" without someone deliberately completing the model.

**MDL-MC-02 and MDL-MC-03 cannot be mechanically repaired by redirecting their import.** Both need `Subsystem` and (MC-02 additionally) `SilicateSubsystem` from their target module. `replication_constraint_graph_v4_silicate.py` defines neither — only `Asteroid` and the broken `ConstraintSolver` above. No file anywhere in this repository defines a working `ConstraintSolver` + `Subsystem` + `SilicateSubsystem` combination; the only working `ConstraintSolver`/`Subsystem` pair (in `zero_g_subsystem_swarm_v3.py`) has no silicate pathway at all. Actually repairing MC-02/03 would require writing new model code — a `SilicateSubsystem` class and a completed `solve_cycle()` — which is original model authorship, not interface repair, and was not done here to avoid quietly inventing physics under the banner of a "fix." Both remain in `experiments/monte_carlo/` as `INERT-SKETCH`.

## DEC-002 Resolution (2026-08-12)

MDL-PWR-01 is now fully integrated with the authoritative `ConstraintSolver` per
`docs/decisions/DEC-002-subsystem-capacity-protocol.md`, option (a). `capacity()` was changed from
`(swarm_mass, params, cycle=0)` to `(swarm_mass, params, global_state)`, reading
`global_state.get('cycle', 0)` internally. `solve_cycle()` gained a `cycle: int = 0` parameter
threaded into `global_state['cycle']` — non-breaking for all existing callers. This was verified as
a genuine drop-in replacement, not a type-compatible stub: the richer standalone model (HTS penalty,
transmission efficiency, degradation curve) was wired directly into a live solver, and its
degradation curve was confirmed to actually reduce `power_available` across cycles
(`test_power_subsystem_wired_into_solver`). Status raised from `EXPLORATORY | EXEC-PARTIAL` to
`AUTHORITATIVE-MODEL | EXEC-FULL`. The solver's own simpler built-in `PowerSubsystem` class was left
unchanged — this decision made the richer model *usable*, it did not force the substitution.

**MDL-PWR-01 was partially repaired.** Missing imports (`Subsystem` from `zero_g_subsystem_swarm_v3`, `typing.Dict`) are fixed and verified — the class now imports and its `capacity()` method runs correctly in isolation (`tests/test_optimizer_interface.py::test_power_subsystem_standalone`).

---

## Phase 3 Findings (this release)

### MDL-PWR-01 — Downgraded
`power_subsystem.py` references a `Subsystem` base class that is never defined or imported in the file. It was never actually verified as a standalone import in any prior phase — its EXEC-FULL rating rested on visual inspection only. Verified against the original V0.01 file directly: the defect is pre-existing, not caused by the Phase 3 move.

### MDL-MC-02 / MDL-MC-03 — Downgraded
Both files contain `from replication_constraint_graph_v3 import ConstraintSolver, Subsystem, Asteroid[, SilicateSubsystem]`. No file named `replication_constraint_graph_v3.py` (or any variant) exists anywhere in the repository — only `replication_constraint_graph_v4_silicate.py` (MDL-GRA-04) does. These two models were carried forward as `AUTHORITATIVE-MODEL | EXEC-FULL` through Phase 1, 1.1, and 2 without anyone actually running `import`. Kept in `experiments/monte_carlo/` rather than `src/` until repaired.

**Not repaired in this pass** — Phase 3 is a structural move, not an interface-repair phase. Repairing these (likely: point the import at `replication_constraint_graph_v4_silicate` and verify the imported names still match) is flagged as the next natural Phase 2-style task.

---

## Phase 2 Changes (this release)

### MDL-OPT-01 (Optimizer.py) — Interface Repair
**Defects fixed:**
1. Missing imports (`typing.Dict`, `Asteroid`).
2. Fatal `KeyError`: original code expected `baseline['net_growth']` which the authoritative solver never returned.

**Alignment performed:**
- Growth metric now defaults to `fabricated` (the actual net new mass key returned by `ConstraintSolver.solve_cycle()`).
- Explicit `growth_key` parameter added so the metric can be changed without further surgery.
- Self-test under `if __name__ == "__main__"` confirms the function runs without `NameError` or `KeyError`, and produces gradients against the live solver.

**Still exploratory:** No claim is made that finite-difference gradients on `fabricated` constitute an optimal allocation policy. Validation remains UNVALIDATED.

### MDL-SWR-03 Parameter Provenance
All hardcoded values from the original `params` dict have been extracted into:

```
parameters/swarm_v3.yaml
```

Every record carries `parameter_id`, `symbol`, `value`/`unit`, `provenance_state` (currently `exploratory_placeholder` or `assumption`), `confidence_score` (≤ 0.40), and a source note pointing back to the V0.01 hardcoded location.

No numerical values were altered. The Python module still contains `DEFAULT_PARAMS` (same values as before) for backward compatibility; loading from YAML is optional via `load_params()`.

### Unit Test (V0.02.1)
- Added `tests/test_optimizer_interface.py` — 5 contract tests: return type, key set, fraction restoration, missing-key raise, default growth key.
- All 5 pass against the repaired Optimizer + live ConstraintSolver (verified by direct execution).

### YAML Parameter Loading (V0.02.1)
- `ZeroGSubsystemSwarm_v3.py` now exposes `load_params(yaml_path=None)`.
- Tries `../parameters/swarm_v3.yaml` by default; falls back silently to `DEFAULT_PARAMS` if the file or PyYAML is unavailable.
- Example usage moved under `if __name__ == "__main__"` (no import side-effects).
- Numerical results unchanged when YAML values match the original hardcodes.

## Interface Findings (carried forward)

### `ZeroGSubsystemSwarm_v3.py`
Hardcoded parameters are now provenance-tracked in `parameters/swarm_v3.yaml`, but every entry is still `exploratory_placeholder` or `assumption` grade — none are `PROVENANCED`. Highest-leverage candidates for real citation work:
- `panel_specific_power_kw_per_kg = 0.08` (solar specific power)
- `anchoring_force_n_per_kg = 15.0`
- `dig_rate_kg_per_kg = 15.0`
- `refining_rate = 12.0`
- `base_fab_yield = 0.65`
