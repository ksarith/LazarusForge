# Astroid Miner Master Epistemic Registry (V0.07 — Machine-Readable Registry)

**Status**: Full artifact inventory (69 entries). Phase 2, Phase 3, Phase 3.1 complete; DEC-001 and DEC-002 resolved. Cross-repo link to Lazarus Forge verified (V0.05). This build adds `registry.yaml` (machine-readable source of truth) and `tools/validate_registry.py`, which checks it against actual repository state — file coverage, duplicate IDs, EXEC-FULL/EXEC-PARTIAL claims backed by a real passing test, and no production code depending on deprecated models. All six validator checks were smoke-tested against deliberately broken repository copies before being trusted against the real one. 11/11 tests passing; validator reports 0 problems. Package version in `pyproject.toml` and `astroid_miner.__version__` aligned to **0.7.0** (matching the V0.07 release label).

**Build note**: `mechanical-structures.md` is included but classified honestly as generated/exploratory material with no verified lineage from the original V0.01 archive.

## Taxonomy Multi-Vector Standard

Every artifact is indexed against five orthogonal dimensions:

| Vector              | Allowed Values                                                                 |
|---------------------|--------------------------------------------------------------------------------|
| **Type**            | `CONCEPT` · `MODEL` · `ENGINEERING` · `GOVERNANCE` · `HISTORICAL_RAW` · `BUILD` |
| **Authority**       | `AUTHORITATIVE-DRAFT` · `AUTHORITATIVE-MODEL` · `EXPLORATORY` · `DEPRECATED` · `LEGACY-LINEAGE` |
| **Validation**      | `UNVALIDATED` · `PARTIALLY-VALIDATED` · `BENCHMARKED` · `PEER-REVIEWED`       |
| **Executability**   | `EXEC-FULL` · `EXEC-PARTIAL` · `INERT-SKETCH` · `N/A`                          |
| **Parameter Status**| `PROVENANCED` · `PARTIALLY-PROVENANCED` · `UNPROVENANCED` · `N/A`              |

Notation: `Type | Authority | Validation | Executability | Parameter Status`

---

## 100% Artifact Inventory

### Governance Decisions (`decisions/`)
* `docs/decisions/DEC-001-silicate-pathway.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
  *(RESOLVED 2026-08-12 — option (b), formal deprecation. See file for rationale.)*
* `docs/decisions/DEC-002-subsystem-capacity-protocol.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
  *(RESOLVED 2026-08-12 — option (a) implemented. `PowerSubsystem.capacity()` reconciled to `(swarm_mass, params, global_state)`; verified as a real drop-in replacement via a degradation-behavior integration test, not merely a signature match.)*

### Root Meta & Horizon Documents
* `README.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `CONTRIBUTING.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `Discovery.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **N/A**
* `LONG_HORIZON.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `REGISTRY.md` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `MODELS.md` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**

### High-Level Architecture (`docs/architecture/`)
* `concepts.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `fault-tolerant-power-control.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `mechanical-structures.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
  *(Generated content injected during V0.02 assembly. No verified provenance from original V0.01 baseline. Treat as draft only — not "carved out" of any prior source file.)*
* `roles-doctrine.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `swarm-vs-monolith-vs-hybrid.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `system-architecture-overview.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `uranus-ejector-module.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `zero-spheres-stability.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**

### Propulsion & ISRU (`docs/isru/`)
* `feedstock-characterization.md` — **ENGINEERING** | **AUTHORITATIVE-DRAFT** | **PARTIALLY-VALIDATED** | **N/A** | **PARTIALLY-PROVENANCED**
* `magnetic-drive.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `low-value-acquisitions-strategy.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `module-getm.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `zero-g-collection-anchoring.md` — **ENGINEERING** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **PARTIALLY-PROVENANCED**
* `zero-g-fabrication.md` — **ENGINEERING** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **PARTIALLY-PROVENANCED**

### Solar & Power Backbone (`docs/power/`)
* `1.5-au-solar-farm-concept.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `energy-scaling.md` — **ENGINEERING** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **PARTIALLY-PROVENANCED**
* `superconductor-interconnect-proposal.md` — **ENGINEERING** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `solar-concentrator-mirror-arrays.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
  *(New, V0.04. Technology-transfer candidate summarizing secondhand analysis from an external collaborating model, not independently verified against primary literature by this repository. Flagged in the source material as connected to a companion terrestrial project ("Solar Descent") that is out of scope for and unverified by this repository.)*
* `liquid-metal-rotating-mirrors.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
  *(New, V0.04. Same provenance caveat as above — secondhand technical summary, not independently sourced. Explicitly notes space/off-zenith applications are research-stage with no flight heritage reported.)*

### Terraforming Core (`docs/terraforming/`)
* `martian-atmosphere.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `ceres-planet-building.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `ceres-metabolic-nucleus.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `mars-atmosphere-bootstrapping.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `mars-core-jumpstart-sketch.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**
* `planetary-orbital-conditioning.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **UNPROVENANCED**

### Vision & Governance (`docs/vision/`)
* `cross-repo-lazarus-forge-link.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **PARTIALLY-VALIDATED** | **N/A** | **N/A**
  *(New, V0.05. Verified directly against the uploaded `LazarusForgeV0-1Alpha12.zip` archive — `Tests/Solar_Descent.md` and `Discovery.md` read and quoted directly, not taken secondhand. Confirms the cross-repo relationship is real but explicitly dormant: "planned; activates when Leviathan deployment is underway." Marked PARTIALLY-VALIDATED because the *existence and wording* of the claim is now verified against source, even though the underlying Solar Descent content itself remains Exploration-status/unvalidated in its own repository.)*
* `interstellar-seeding.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **N/A**
* `oceanic-tests.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **N/A**
* `rogue-unit-management.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `safety-lights.md` — **CONCEPT** | **EXPLORATORY** | **UNVALIDATED** | **N/A** | **N/A**
* `Vision` — **CONCEPT** | **LEGACY-LINEAGE** | **UNVALIDATED** | **N/A** | **N/A**
* `ethical-ai-frameworks.md` — **GOVERNANCE** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
  *(v1.1 consolidated, August 2026 — merges original base with role separation, Tested Framework First, runaway/rogue hardening, location agnosticism, auditability, and non-goals.)*
* `ethical-ai-frameworks-v1.1.md` — **GOVERNANCE** | **DEPRECATED** | **UNVALIDATED** | **N/A** | **N/A**
  *(Historical delta only; content merged into `ethical-ai-frameworks.md`. Retained for provenance.)*
* `self-evolving-ai.md` — **CONCEPT** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**

### Computational Models (`src/astroid_miner/`) — Phase 3 relocation
Files below were moved out of the flat `notebooks/` directory (removed in V0.03) into a proper Python package, grouped by validated importability, not merely by narrative status.

* `src/astroid_miner/models/contracts.py` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **EXEC-FULL** | **N/A**
  *(V0.08 DEC-002 CapacityResult + SubsystemProtocol.)*
* `src/astroid_miner/models/power_subsystem.py` (was `PowerSubsystem.py`) — **MODEL** | **AUTHORITATIVE-MODEL** | **UNVALIDATED** | **EXEC-FULL** | **UNPROVENANCED**
  *(DEC-002, 2026-08-12: fully integrated with the authoritative `ConstraintSolver` — `capacity(swarm_mass, params, global_state)` now matches every other subsystem's calling convention. Verified as a genuine drop-in replacement (not merely signature-compatible) by wiring it into a live solver and confirming its degradation curve actually reduces `power_available` across cycles. Raised from EXPLORATORY/EXEC-PARTIAL to AUTHORITATIVE-MODEL/EXEC-FULL — it is now a richer, verified alternative to the solver's own simpler built-in PowerSubsystem class, which was left unchanged.)*
* `src/astroid_miner/models/replication_model.py` (was `Replication_Model.Py`) — **MODEL** | **AUTHORITATIVE-MODEL** | **UNVALIDATED** | **EXEC-FULL** | **UNPROVENANCED**
  *(Note: runs example/demo code at import time as a side effect — candidate for an `if __name__ == "__main__"` guard in a future pass, not done here.)*
* `src/astroid_miner/models/zero_g_simulator.py` (was `Zero-GSimulator.py`) — **MODEL** | **AUTHORITATIVE-MODEL** | **UNVALIDATED** | **EXEC-FULL** | **UNPROVENANCED**
* `src/astroid_miner/models/zero_g_subsystem_swarm_v3.py` (was `ZeroGSubsystemSwarm_v3.py`) — **MODEL** | **AUTHORITATIVE-MODEL** | **UNVALIDATED** | **EXEC-FULL** | **PARTIALLY-PROVENANCED**
  *(`load_params()` default path updated for new depth under `src/astroid_miner/models/`; verified against `parameters/swarm_v3.yaml`.)*
* `experiments/deprecated/replication_constraint_graph_v4_silicate.py` — **MODEL** | **DEPRECATED** | **UNVALIDATED** | **INERT-SKETCH** | **UNPROVENANCED**
  *(DEC-001 (b), 2026-08-12: formally deprecated. Relocated August 2026 from `src/astroid_miner/models/` to `experiments/deprecated/` so it is no longer on the importable package path. `solve_cycle()` raises `NameError` — `processed_raw_kg`, `raw_metals`, `fab_capacity` are never defined, and the return dict contains a literal `...` placeholder. See `docs/decisions/DEC-001-silicate-pathway.md`.)*
* `src/astroid_miner/optimization/optimizer.py` (was `Optimizer.py`) — **MODEL** | **EXPLORATORY** | **UNVALIDATED** | **EXEC-PARTIAL** | **UNPROVENANCED**
  *(Interface repaired in Phase 2; import path updated in Phase 3 to `astroid_miner.models.zero_g_subsystem_swarm_v3`. Verified via `tests/test_optimizer_interface.py`, 5/5 passing.)*

### Experimental / Broken-Interface Models (`experiments/`)
Not placed under `src/` because they are either superseded or not currently importable.

* `experiments/deprecated/zero_g_subsystem_swarm_v1.py` (was `ZeroGSubsystemSwarm.py`) — **MODEL** | **DEPRECATED** | **UNVALIDATED** | **EXEC-FULL** | **UNPROVENANCED**
* `experiments/deprecated/dynamic_optimizer_monte_carlo_v1.py` (was `dynamic_optimizer_monte_carlo.py`) — **MODEL** | **DEPRECATED** | **UNVALIDATED** | **EXEC-FULL** | **UNPROVENANCED**
* `experiments/monte_carlo/dynamic_monte_carlo_optimized.py` — **MODEL** | **DEPRECATED** | **UNVALIDATED** | **INERT-SKETCH** | **UNPROVENANCED**
  *(DEC-001 (b), 2026-08-12: formally deprecated rather than repaired. Needs `Subsystem`/`SilicateSubsystem` from `replication_constraint_graph_v4_silicate.py`, which defines neither and is itself deprecated. Deprecation docstring added; retained for provenance.)*
* `experiments/monte_carlo/monte_carlo_asteroid_comparison.py` — **MODEL** | **DEPRECATED** | **UNVALIDATED** | **INERT-SKETCH** | **UNPROVENANCED**
  *(DEC-001 (b), 2026-08-12: same disposition as MDL-MC-02.)*

### Historical Raw Material (`archive/raw-development/`)
* `astroid-mining.txt` — **HISTORICAL_RAW** | **LEGACY-LINEAGE** | **UNVALIDATED** | **N/A** | **N/A**
* `astroid-mining-2.txt` — **HISTORICAL_RAW** | **LEGACY-LINEAGE** | **UNVALIDATED** | **N/A** | **N/A**
* `astroid-mining-3.txt` — **HISTORICAL_RAW** | **LEGACY-LINEAGE** | **UNVALIDATED** | **N/A** | **N/A**
* `power-allocation-optimizer.md` — **MODEL** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **INERT-SKETCH** | **UNPROVENANCED**

### Parameters & Build Tooling
* `parameters/schema.yaml` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**
* `parameters/swarm_v3.yaml` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**  *(Phase 2 — provenance records for MDL-SWR-03)*
* `tools/update_archive.py` — **BUILD** | **EXPLORATORY** | **UNVALIDATED** | **EXEC-PARTIAL** | **N/A**
* `tools/verify_manifest.py` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **EXEC-FULL** | **N/A**  *(new, Phase 3 — re-hashes the tree and diffs against a build manifest)*
* `tests/test_optimizer_interface.py` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **EXEC-FULL** | **N/A**  *(Phase 2 — 5 contract tests; import paths updated in Phase 3 for the `src/` layout, all still passing; expanded to 11 tests through Phase 3.1/DEC-002)*
* `pyproject.toml` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**  *(new, Phase 3 — minimal packaging config for the `src/astroid_miner` layout)*
* `registry.yaml` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **N/A** | **N/A**  *(new, V0.07 — machine-readable source of truth behind this document; see below)*
* `tools/validate_registry.py` — **BUILD** | **AUTHORITATIVE-DRAFT** | **UNVALIDATED** | **EXEC-FULL** | **N/A**  *(new, V0.07 — checks registry.yaml against actual repository state; see below)*

---

## Explicit Notes on mechanical-structures.md

This file was not present in the original V0.01 baseline. It was supplied during the V0.02 assembly process.
Until independent provenance or validation is established it remains:

```
ENGINEERING | EXPLORATORY | UNVALIDATED | N/A | UNPROVENANCED
```

No claim is made that it was "carved out" of a prior Engineering.md or any other historical source.

---

## Phase 2 Changes (this build)

- `notebooks/Optimizer.py` interface repaired (missing imports fixed; growth-key alignment to `fabricated`, the key the solver actually returns instead of the nonexistent `net_growth`). Status now EXEC-PARTIAL.
- `parameters/swarm_v3.yaml` added — full provenance records for every hardcoded value previously inside `ZeroGSubsystemSwarm_v3.py`. All remain `exploratory_placeholder` / `assumption` with confidence ≤ 0.40.
- Optional YAML loading added to `ZeroGSubsystemSwarm_v3.py` via `load_params()`; falls back silently to the original hardcoded values (`DEFAULT_PARAMS`) if the YAML or PyYAML is unavailable. No numerical values were changed.
- Unit tests added in `tests/test_optimizer_interface.py` (5 contract tests, all passing against the live solver).
- No model physics altered. No directory restructuring performed.

## Phase 3 Changes (this build)

**Restructuring performed:**
- `notebooks/` (flat directory of scripts) removed; contents relocated by validated status, not narrative status:
  - Importable, authoritative models → `src/astroid_miner/models/`
  - Interface-repaired but still exploratory → `src/astroid_miner/optimization/`
  - Deprecated/superseded models → `experiments/deprecated/`
  - Models with unresolved broken imports → `experiments/monte_carlo/` (kept out of `src/` deliberately — see downgrades below)
  - Raw historical `.txt` transcripts and the inert sketch doc → `archive/raw-development/`
- All internal cross-imports (`Optimizer.py`, `ZeroGSubsystemSwarm_v3.py`'s `load_params()` default path) updated for new file depth and verified by direct execution.
- `tests/test_optimizer_interface.py` updated to import from `src/astroid_miner` instead of the old flat-directory `sys.path` hack. Re-ran: 5/5 passing.
- Added `pyproject.toml` (setuptools, `src/` layout) so the package is properly installable/importable rather than relying on manual `sys.path` insertion long-term.
- Conceptual/governance document trees (`docs/architecture/`, `docs/vision/`, `docs/terraforming/`, `docs/power/`, `docs/isru/`) were left untouched — they were already reasonably organized and moving them wasn't justified by anything in the registry.

**New defects discovered during Phase 3 (pre-existing, not introduced by the move):**
1. `PowerSubsystem.py` → `src/astroid_miner/models/power_subsystem.py`: fails standalone import (`NameError: Subsystem`). Was previously classified `AUTHORITATIVE-MODEL | EXEC-FULL` on the basis of visual inspection, not an actual standalone import test. Confirmed by running the *original* V0.01 file in isolation — the defect predates all prior Phase 1/1.1/2 work. Downgraded to `EXPLORATORY | INERT-SKETCH`.
2. `dynamic_monte_carlo_optimized.py` and `monte_carlo_asteroid_comparison.py` both import `from replication_constraint_graph_v3 import ...` — this module does not exist anywhere in the repository (only `_v4_silicate` does). Both were previously classified `AUTHORITATIVE-MODEL | EXEC-FULL` without a standalone import check. Downgraded to `EXPLORATORY | INERT-SKETCH` and kept in `experiments/` rather than `src/`.

**Deliberately not done in Phase 3:**
- No repair of the three newly-found broken imports above — that's Phase 2-style interface repair work, out of scope for a pure restructuring pass, and doing it silently here would repeat the exact problem this registry exists to prevent.
- No numerical/physics changes to any model.
- No changes to conceptual or governance documents.

## Phase 3.1 Changes (this build)

Attempted a follow-up repair pass on the three defects Phase 3 surfaced. Result: partially achievable, partially not — logged honestly rather than forced to completion.

**Actually repaired and verified:**
- `power_subsystem.py`: missing imports fixed (`Subsystem` from the authoritative swarm module, `typing.Dict`). Standalone `capacity()` call verified working by direct execution and a new test. Status raised from `INERT-SKETCH` to `EXEC-PARTIAL`.
- Added `TestModelImportSmoke` to `tests/test_optimizer_interface.py` — 5 new tests that actually import/instantiate every file under `src/astroid_miner/models/`, including one that asserts MDL-GRA-04's exact failure mode so it can't silently regress or silently start "passing." Full suite: 10/10 passing.

**Investigated and found genuinely unrepairable without new model authorship:**
- `replication_constraint_graph_v4_silicate.py` (MDL-GRA-04) — the file MDL-MC-02/03 were assumed to need redirecting to is itself an inert sketch. Direct execution of `solve_cycle()` raises `NameError: name 'processed_raw_kg' is not defined`; `raw_metals` and `fab_capacity` are likewise never assigned, and the return dict contains a literal `...` placeholder. This was previously misclassified `AUTHORITATIVE-MODEL | EXEC-FULL` because nobody had called it, only imported it — import succeeds fine. Downgraded to `EXPLORATORY | INERT-SKETCH`.
- `dynamic_monte_carlo_optimized.py` / `monte_carlo_asteroid_comparison.py` (MDL-MC-02/03) — cannot be fixed by pointing their import at MDL-GRA-04, because MDL-GRA-04 doesn't define the `Subsystem`/`SilicateSubsystem` classes they need, and is broken anyway. No combination of existing files in this repository satisfies their dependencies. Completing them would require writing a new `SilicateSubsystem` class and a working `solve_cycle()` — original model logic, not an interface fix — which was deliberately not fabricated here.
- `power_subsystem.py`'s integration into the authoritative `ConstraintSolver` remains unresolved: the solver calls `capacity(swarm_mass, params, global_state)` on every subsystem, but this class's `capacity()` expects `(swarm_mass, params, cycle=0)`. Reconciling this is a modeling decision (which calling convention should win, and whether the HTS/degradation physics in this file belongs in the authoritative swarm model) that belongs to the repository owner, not something to silently resolve as a side effect of an import fix.

## Phase 4 — Contract & Provenance Hardening: Machine-Readable Registry (V0.07)

**V0.08 extension:** `tools/validate_registry.py` now enforces taxonomy enums, required fields, production path constraints (`src/astroid_miner/` only), no `src/` imports from `experiments/` or `archive/`, no production imports of DEPRECATED models, and EXEC-FULL/PARTIAL ↔ passing `test_ref` for MODEL and BUILD entries. Repository contract tests: `test_registry.py`, `test_import_boundaries.py`, `test_subsystem_contract.py`, `test_release_integrity.py`.

Following ChatGPT's Phase 4 proposal (reviewed and partially adopted — see conversation record).
Added `registry.yaml` as the machine-readable source of truth behind this document, and
`tools/validate_registry.py` to check it against actual repository state.

**What the validator checks, concretely:**
1. Every file under a tracked content directory has a `registry.yaml` entry (catches silent additions).
2. Every `registry.yaml` entry's path actually exists on disk (catches stale/renamed entries).
3. No duplicate `model_id` values across entries.
4. No duplicate `parameter_id` values in `parameters/swarm_v3.yaml`.
5. Any non-deprecated `MODEL` entry claiming `EXEC-FULL` or `EXEC-PARTIAL` must cite a `test_ref`,
   and that test is actually run (not just checked for existence) — a cited test that fails makes
   the registry entry itself fail validation. This directly targets the failure mode that let
   MDL-GRA-04 sit misclassified `EXEC-FULL` for three phases: a status claim with no test behind it,
   or with a test that doesn't actually pass, is now a hard validator failure, not something that
   depends on the next audit happening to check by hand.
6. No file under `src/` (production code) imports a module whose registry entry is `DEPRECATED`.

**Deliberately scoped narrower than the original proposal:** a five-way sub-taxonomy (importability
/ executability / contract compliance / numerical verification / physical validation) was not
adopted as five new registry columns — that risked making entries too expensive to fill in
accurately, which is the same failure mode that let the old registry drift from reality. Instead,
"does EXEC-FULL actually have a passing test" is enforced as a validator rule against the
*existing* Executability field, not a new column. Similarly, a proposed `tests/test_models/`
subdirectory split was not done — premature for an 11-test suite; revisit if the suite grows enough
that a flat file becomes hard to navigate.

**Verified, not just written:** all six checks were smoke-tested against deliberately broken copies
of the repository (orphaned entry, unregistered file, duplicate model_id, missing test_ref, a
test_ref pointing at a test that fails, and a deprecated import from `src/`) and confirmed to fail
correctly in each case, before being run clean against the real repository. Current state: 64
registry entries, 0 problems, 11/11 tests passing.

## Baseline Freeze Statement

This is a **surgical Phase 2 update**, not a full validation pass:

- Interface bugs fixed; physics/parameter *values* unchanged.
- Parameter provenance extracted but not yet independently sourced — everything is still placeholder/assumption grade.
- No directory restructuring or renaming of source modules has occurred.

Next steps: attach real literature/engineering citations to the highest-leverage parameters (starting with solar specific power), then re-run the Monte Carlo models against provenanced inputs.
