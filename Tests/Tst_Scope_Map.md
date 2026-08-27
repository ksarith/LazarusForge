# Tst_Scope_Map.md — Tests/

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Adm_Scope_Map.md](../Admin/Adm_Scope_Map.md) | [Architecture/Arc_Scope_Map.md](../Architecture/Arc_Scope_Map.md) | [Operations/Ops_Scope_Map.md](../Operations/Ops_Scope_Map.md) | [Challenges/Cha_Scope_Map.md](../Challenges/Cha_Scope_Map.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is a cross-reference index, not a specification     |
| Open Unknowns    | 0 (surfaces existing unknowns from owning files; creates none)      |
| Owning Domain    | Tests/                                                               |
| Last Reviewed    | 2026-08-08                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Purpose

Fifth folder in the Scope_Map rollout, following Admin/ (2026-08-07), Architecture/, Operations/, and Challenges/ (all 2026-08-08). Same method throughout: every entry extracted directly from source. This is the first folder where the entries were mostly written by this repository's own AI contributors framed as exploratory test/simulation architectures rather than operational doctrine — reflected below in generally lower Spec Gates (0/6 across the board except `Cognitive_Salvage_Layer.md` at 1/6) and higher proportional Open Unknowns counts.

---

## Scope Entries

### `Tests/Chaos_Dynamics.md`
**Status:** Exploration · 0/6 · 0 Open Unknowns · Risk: Medium — gatekeeps the evidentiary pipeline feeding EN-001/EN-001a; misuse risk if sandbox output is cited past its Level <=4 ceiling
**Does:** Exploration/R&D processes; promotion/demotion gates; EN-005 resolution vehicle; feeder to EN-001a.
**Does not:** Cognition doctrine, entropy philosophy, or derating data.
Note: shortest, most compressed entry in this folder — a gatekeeping/process file rather than a domain-content file. Its Risk framing (misuse past Level 4 ceiling) is worth reading literally: this file's real function is bounding how much confidence downstream files may borrow from sandboxed results.

### `Tests/Cognitive_Salvage_Layer.md`
**Status:** Exploration · 1/6 · 13 Open Unknowns · Risk: High
**Does:** Cognitive Salvage Layer as a distinct architectural module; heuristic failure class motivating human-in-the-loop integration; feedback loop architecture (scan to autonomous execution); Auditor Decision Tree (Stages 1-4); six-status grading matrix including CANDIDATE_NOVEL; Heuristic Object telemetry schema; GH-series unknowns.
**Does not (arrow):** Game/puzzle/interface design · robotic arm kinematics/IK solvers · FEA methodology · Forge_Net federated knowledge base (`Architecture/Forge_Net.md`) · auditor operational behavior (`Admin/Auditor_Protocols.md`) · canonical terminology (`Admin/Canonical_Terms.md`) · weld qualification (`Operations/Gate_06_Fabrication.md`).
Note: points to `Operations/Leviathan.md` as "planned" — confirmed that file genuinely does not exist anywhere in the repository yet. Not stale; the file's own label already says planned, not built. Flagged only so a future session doesn't need to re-check this.

### `Tests/Field_Logs.md`
**Status:** Active — Intake · N/A (log, not specification) · 0 Open Unknowns · Risk: N/A
**Does:** Submission format for real-world test runs (physical fabrication, cross-agent sessions, hardware-diversity trials); append-only intake log, same discipline as `Archive/`.
**Does not:** Resolve any Unknown or advance Status/Spec Gate/Body Stability on its own — a logged entry is raw evidence, folding it into doctrine is a separate deliberate step. Require a fork, PR, or GitHub account.
Note: created 2026-08-06, this session. As of this Scope_Map build, its own Log Entries section is still empty — no physical or cross-agent runs have been submitted yet. Worth remembering this file exists and is waiting, not just that it was built.

### `Tests/Hydrologic_Resource_Cascade.md`
**Status:** Exploration · 0/6 · 2 Formal / 6 Unregistered (HR-003-HR-010 pending sidecar registration) · Risk: High
**Does:** Multi-benefit flood resource recovery system; sequential zones (intake/heavy mineral/aggregate/fine sediment/wetland polishing/recreation); episodic flood-driven operation with continuous base-flow; hydraulic modes across drought/normal/seasonal/flood/recovery/containment; HR-001-010 research unknowns; flood resilience + recreation + resource recovery co-benefit framing.
**Does not (arrow):** Detailed engineering drawings/site hydrology models/permitting doctrine · power systems (`Operations/Energy.md`) · material processing gate detail (`Operations/Gate_05_Separation_Thermal.md`) · Leviathan/Support Raft extensions · economic valuation (`Admin/Economics.md`) · contaminant remediation detail · water rights/diversion permitting law · human-machinery co-incident risk.
Note: "2 Formal / 6 Unregistered" Open Unknowns is a distinct pattern from every other file in this folder — worth a decision at some point on whether HR-003 through HR-010 should be formally registered in `Unknowns.md` or whether this file's own sidecar is the intended permanent home. Not flagged as an error, just the one file in this folder whose unknown-tracking status doesn't match the others' pattern.

### `Tests/Leviathan_testing.md`
**Status:** Exploration · 0/6 · 7 Open Unknowns · Risk: High
**Does:** Leviathan test framework purpose/philosophy; deep ocean as chosen test environment; test philosophy/success criteria; power/endurance constraints; failure/recovery requirements; autonomy/control objectives; sensor/environmental doctrine; ethical/environmental constraints; correlated AI failure test criteria (poisoned telemetry injection, CF-002 resolution path); Extensions Framework A/B; knowledge classification tiers; anti-pattern safeguards.
**Does not (arrow):** Hardware designs/materials · power system engineering (`Operations/Energy.md`) · Air Scrubber marine variants (`Air_Scrubber.md` Variant 4) · Support Raft architecture (`Support_Raft.md`) · network protocol implementation (`Architecture/Forge_Net.md`) · autonomy architecture paradigm (LT-003, open) · trust model/peer scoring (LT-004, open, trajectory-scope).

### `Tests/Living_Waters.md`
**Status:** Exploration · 0/6 · 9 Open Unknowns · Risk: Critical — LW-UNK-001 (volatile co-distillation) and LW-UNK-003 (lumen implosion) both carry immediate safety consequences if bypassed
**Does:** Four separation mechanisms (thermal/pressure/phase change/chemical-biological) and ten experimental pathways (LW-001-010); Water Hierarchy tiering purification effort to intended use; site-conditioned pathway selection; sequencing doctrine (purify before atmospheric harvest); partial-advancement promotion criteria.
**Does not (arrow):** Power sourcing specs (`Energy.md`) · PPE/handling doctrine (`Admin/Safety_Protocols.md`) · marine deployment ethics/brine disposal (`Admin/Ethical_Constraints.md`) · recovered salt/mineral valuation (`Admin/Economics.md`) · formal Site Characterization to Pathway Selection framework — declared future work, not yet written (LW-UNK-008, confirmed against `Unknowns.md`: "formal framework not yet written," matches this file's own description exactly).
Note: the only file in this folder carrying a Critical risk rating with an explicit "immediate safety consequences if bypassed" justification, not just a severity label.

### `Tests/Pyrolysis_Cascade.md`
**Status:** Draft — Exploration · 0/6 (not yet audited) · 8 Open Unknowns (PYC-001-008) · Risk: High (thermal processing of mixed salvage; halogen/hazardous-fraction exposure)
**Does:** Staged thermal cascade architecture (primary pyrolysis to secondary high-temp reduction with heat integration); candidate material-separation pathways; explicit dependency surface on upstream triage/reduction/hazard/site/energy/scrubber doctrine; test concepts and measurement priorities.
**Does not (arrow):** Halogenated-polymer triage/field ID (`Operations/Plastics.md` PL-001, `Architecture/Chemistry.md` CE-003) · reduction method selection (`Gate_03_Reduction.md` GR-002) · air scrubbing (`Air_Scrubber.md`) · chemical/biological waste disposal (GR-003, WA-004) · site/emergency/structural safety (FA-001, SP-006, EN-001) · cost baseline/power demand/profitability (ECN-002, EV-001, TR-001).
**Hard preconditions (explicit, non-negotiable, worth preserving verbatim):** no hot pyrolysis of mixed urban salvage may be proposed, piloted, or claimed until PL-001/CE-003 resolve or feedstock is validated halogen-free; no structural/refractory claims until EN-001 closes for the relevant materials; no site-dependent operational claims until FA-001 closes.

### `Tests/Solar_Descent.md`
**Status:** Exploration · 0/6 · 8 Open Unknowns · Risk: High
**Does:** Solar Descent organizing principle, diverge/reconverge architecture; SD-001 optical downlink (molten tin termination concept); SD-002 thermal/fluid downlink; shared underground chamber reconvergence; geodesic/spherical chamber geometry, modular panel expansion; power conversion cascade; safety governance for both pathways; Astroid-miner companion-system technology transfer paths.
**Does not (arrow):** General energy storage (`Operations/Energy.md`) · high-temp thermal processing (`Gate_05_Separation_Thermal.md`) · pyrolysis doctrine (`Plastics.md`) · waste-heat water distillation (`Living_Waters.md` LW-001/008) · geotechnical excavation specs (out of scope at current interval) · site-specific geology (site-conditioned, no universal answer) · grid-scale generation (out of scope for v0).

### `Tests/Support_Raft.md`
**Status:** Exploration · 0/6 · 13 Open Unknowns · Risk: High — SR-001 (galvanic corrosion) Open/High and required before v1.0; a hull corroding faster than modeled threatens the whole anchor-node concept
**Does:** Stationary regional anchor infrastructure doctrine; five anchor roles (Energy/Truth/Recovery/Material/Communication); SWATH hull implementation and Sacrificial Shell System; failure philosophy/succession doctrine; SR-001-013 sidecar unknowns.
**Does not (arrow):** Leviathan unit architecture/autonomy (`Leviathan_testing.md`) · galvanic corrosion chemistry (`Architecture/Chemistry.md` CE-001) · biofouling framing (`Challenges/Biofouling.md`) · firmware trust/cache integrity (`Operations/Electronics.md`) · repository integrity/cache governance (`Admin/Repository_Integrity_Protocol.md`) · energy philosophy (`Operations/Energy.md`) · marine G.E.C.K. variant (`Architecture/Geck_forge_seed.md`) · storm-survival/multi-Raft coordination (`Admin/Trajectories.md`) · identity continuity (`Admin/Ship_of_Theseus.md`) · material separation ops (`Gate_05_Separation_Thermal.md`).
**Explicit self-distinction (worth preserving verbatim):** *"The Support Raft is an anchor node, not headquarters. It does not direct Leviathan unit behavior... The distinction between anchor and director must be preserved as the system scales."*

### `Tests/Trophic_Forge.md`
**Status:** Exploration · 0/6 · 10 Open Unknowns · Risk: High
**Does:** Trophic Forge concept/organizing principle; base loop architecture and node properties; bootstrap sequence for salvage-first deployment; per-node test parameters; naming rationale/prior art questions.
**Does not (arrow):** LED array electrical specs (`Operations/Energy.md`, `Operations/Electronics.md`) · pond/condensate water purification (`Living_Waters.md`) · fish species selection — proposed only, pending site context · crop selection/agronomic practice — out of scope at current interval · atmospheric-scale moisture-extraction effects — explicitly out of scope · any tornado/severe-weather-mitigation claim — out of scope at all intervals.

---

## Gaps Exposed By Building This

1. **No missing or non-conforming Scope Boundary sections** — all 10 files have complete, conforming content (mix of "DOES/DOES NOT" and "owns/does not own" phrasing, both already-established patterns from prior folders, not a new inconsistency).

2. **One confirmed-accurate forward reference:** `Cognitive_Salvage_Layer.md` points to `Operations/Leviathan.md` as "planned" — checked, that file genuinely doesn't exist yet anywhere in the repository. Not stale, since the source file's own label already says planned rather than claiming the file exists. Surfaced here so a future session doesn't need to re-verify it from scratch.

3. **One real inconsistency in how unknowns are tracked, not in scope content:** `Hydrologic_Resource_Cascade.md` uses "2 Formal / 6 Unregistered" for its Open Unknowns count — the only file in this folder (or any folder scoped so far) with unregistered unknowns sitting in its own sidecar rather than fully mirrored to `Unknowns.md`. Not flagged as an error — every other Tests/ file's sidecar unknowns are fully registered — but worth a decision at some point on whether HR-003 through HR-010 should be formally registered.

4. **`Field_Logs.md`'s actual state is worth restating plainly:** built 2026-08-06, cross-referenced from `CONTRIBUTING.md`, and — as of this build — still empty. The infrastructure exists; nothing has been submitted to it yet. This isn't a gap in the file itself, just a fact worth keeping visible rather than letting "we built the intake system" quietly stand in for "the intake system has been used."

5. **No hub pattern as concentrated as Admin/'s Governance_Charter.md or Architecture/'s Facilities.md** — this folder's cross-references spread fairly evenly across `Operations/Energy.md`, `Architecture/Forge_Net.md`, and each other (`Leviathan_testing.md` <-> `Support_Raft.md` is the closest thing to a genuine pair, and both sides' entries already describe the relationship consistently with each other, checked).

No corrections were needed in this folder, same as Challenges/ — no stale cross-references, no missing sections, nothing requiring a fix. Two folders now clean in a row after Operations/'s three corrections.

---

## Resolution Log

- 2026-08-08: **File created — fifth folder in the Scope_Map rollout**,
  following Admin/ (2026-08-07), Architecture/, Operations/, and
  Challenges/ (all 2026-08-08). All 10 Tests/ files' Status/Spec
  Gates/Open Unknowns/Risk and full Scope Boundary content extracted
  directly from source. Confirmed one forward reference
  (`Cognitive_Salvage_Layer.md` to `Operations/Leviathan.md`) as
  accurately-labeled-planned rather than stale, by checking the target
  file genuinely doesn't exist. Found one real tracking inconsistency
  (`Hydrologic_Resource_Cascade.md`'s partially-unregistered unknowns)
  worth a future decision but not itself an error to fix now. No
  corrections applied this pass. Human-directed.
