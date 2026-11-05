# DEC-001 — Disposition of the Silicate Pathway

**Status: RESOLVED — option (b) chosen, 2026-08-12**
**Affects:** `experiments/deprecated/replication_constraint_graph_v4_silicate.py` (MDL-GRA-04), `experiments/monte_carlo/dynamic_monte_carlo_optimized.py` (MDL-MC-02), `experiments/monte_carlo/monte_carlo_asteroid_comparison.py` (MDL-MC-03)
**Raised:** Phase 3.1 audit (V0.03.1)

## The situation

Three files that together represent the "silicate byproduct" pathway (SiC ceramics, glass fibers, sintered regolith, basalt-fiber metal substitution) are currently non-functional:

- **MDL-GRA-04** imports cleanly but `solve_cycle()` raises `NameError` on execution — `processed_raw_kg`, `raw_metals`, and `fab_capacity` are referenced but never defined, and the return dict contains a literal `...` placeholder instead of a value. It was rated `AUTHORITATIVE-MODEL | EXEC-FULL` from Phase 1 through Phase 3 because nobody had actually called it before the Phase 3.1 audit — only imported it.
- **MDL-MC-02 / MDL-MC-03** both depend on `Subsystem` and (MC-02 only) `SilicateSubsystem` classes that don't exist in MDL-GRA-04 or anywhere else in the repository in working form.

No amount of import repair fixes this. The pathway's actual physics — the silicate-processing yield curve, the SiC wear-reduction relationship, the basalt-fiber substitution logic — was sketched in comments and partial code but never completed into a runnable model.

## What is NOT in question

The conceptual material this pathway is based on (`feedstock-characterization.md`, the "Silicate Pathway" narrative embedded in MDL-GRA-04's comments) is untouched and still present. This decision is only about the **executable model layer**, not the underlying idea.

## Options

**(a) Commission real implementation.**
Write a `SilicateSubsystem` class and complete `solve_cycle()`'s silicate branch with actual logic — define `processed_raw_kg`, `raw_metals`, `fab_capacity` in terms of the existing swarm-mass/asteroid-composition inputs, replace the `...` placeholder, and reconcile with `MDL-SWR-03`'s existing `ConstraintSolver` interface (or keep it as a deliberately separate solver). This is new model-authorship work, not a bugfix — it should go through the same "no numbers without provenance" discipline as the rest of Phase 2 (i.e. any new constants get logged in `parameters/` with a `provenance_state`, not hardcoded silently).

*Cost:* real engineering/physics-design effort. *Benefit:* the silicate byproduct pathway becomes a genuine, testable part of the model suite instead of a claim.

**(b) Formally deprecate the pathway until (a) happens.**
Mark MDL-GRA-04, MDL-MC-02, and MDL-MC-03 as `DEPRECATED` (not merely `EXPLORATORY`) in the registry, add a top-of-file docstring notice in each stating they are non-functional and awaiting implementation, and stop referencing them as available capability in any README/Discovery-level summaries. Files are kept in place for provenance either way — this is a status change, not a deletion.

*Cost:* the repository's public-facing narrative can no longer claim a working silicate pathway. *Benefit:* zero further epistemic debt — the registry stops carrying three files whose true status is closer to "aspirational" than "model."

**Either way:** the files stay in the repository. This decision does not touch deletion.

## Recommendation from the audit process

No recommendation is made here — this is an engineering-priority call for the repository owner, not something the audit trail should decide unilaterally. Both options are legitimate; they differ in whether silicate processing is worth the implementation cost right now versus later.

## Resolution

- **Decision:** Option (b) — formally deprecate MDL-GRA-04, MDL-MC-02, and MDL-MC-03 rather than commission implementation now.
- **Rationale:** No other part of the repository currently depends on silicate-pathway output (nothing in the swarm model, optimizer, or parameter layer calls into it), so there is no demand signal to design the physics against yet. Designing a `SilicateSubsystem` and its yield/wear/substitution logic now would mean inventing physics in a vacuum, with real risk of redoing it once the swarm/fabrication model matures and the actual required interface becomes clear. The cost of waiting is low: files are retained for provenance, concept docs are untouched, and the registry + a pinning test already make the true status honest rather than misleading. Formal deprecation is cheap and reversible — it costs a docstring and a status flag, and nothing about it forecloses implementing option (a) later if capabilities or requirements shift.
- **Date:** 2026-08-12
- **Follow-up actions:**
  - `MODELS.md` / `REGISTRY.md` status for all three files raised from `EXPLORATORY` to `DEPRECATED`.
  - Top-of-file deprecation docstrings added to all three files, each pointing back to this record.
  - No README/Discovery-level narrative changes were needed — neither document claimed the silicate pathway as working capability.
  - This decision can be reopened if the swarm/optimizer/parameter layer later develops an actual need for silicate-processing output — revisit option (a) at that point rather than treating this resolution as permanent.

## Follow-up — package path cleanup (August 2026)

MDL-GRA-04 was moved from `src/astroid_miner/models/` to `experiments/deprecated/` so it is no longer importable as part of the production package. The known-broken contract test was updated to load the module from its new location. MC-02/MC-03 remain under `experiments/monte_carlo/`. This does not change the substance of option (b); it only hardens the boundary between working package code and retained provenance sketches.
