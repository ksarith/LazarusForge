# Ops_Scope_Map.md — Operations/

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Adm_Scope_Map.md](../Admin/Adm_Scope_Map.md) | [Architecture/Arc_Scope_Map.md](../Architecture/Arc_Scope_Map.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is a cross-reference index, not a specification     |
| Open Unknowns    | 0 (surfaces existing unknowns from owning files; creates none)      |
| Owning Domain    | Operations/                                                          |
| Last Reviewed    | 2026-08-15                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Purpose

Third folder in the Scope_Map rollout, following `Admin/Adm_Scope_Map.md` (2026-08-07) and `Architecture/Arc_Scope_Map.md` (2026-08-08). Same method throughout: every entry extracted directly from its file's own File State and Scope Boundary sections, not reconstructed from memory. Per instruction from the human governing authority, errors found during this build were fixed in the same pass rather than only cataloged — see Gaps Exposed below for what was found and fixed.

---

## Scope Entries

### `Operations/Air_Scrubber.md`
**Status:** Draft · 3/6 · 4 Open Unknowns · Risk: High
**Does:** Five-stage functional architecture (A-E) plus fractional condensation/chemisorption; wet capture variants (0-4); Saturation/Particulate Blinding/Thermal Fault monitoring; E-Stop interlocks; negative pressure/flashback doctrine; Gate 4 Cold Verification Harness.
**Does not (arrow):** Spin Chamber exhaust heat load (`Gate_05_Separation_Thermal.md`) · Forge power budget (`Energy.md`) · deep-sea compression (`Admin/Trajectories.md`) · contamination routing (`Gate_02_Triage.md`) · noise/PPE standards (`Admin/Safety_Protocols.md` SP-003) · facility siting (`Architecture/Facilities.md` FA-001).

### `Operations/Electronics.md`
**Status:** Exploration · 0/6 · 9 Open Unknowns · Risk: High
**Does:** Non-destructive salvage harvesting protocols; firmware trust doctrine (Logic-Zero wipe); PCB fabrication methods; TMR hardware implementation; hardware watchdog doctrine (CF-001); dual-use annotation; counterfeit/remarked component detection.
**Does not (arrow):** TMR as philosophy/framework (`Architecture/Cognitive_Frameworks.md` Framework D) · dual-use ethical escalation (`Admin/Ethical_Constraints.md`) · Air Scrubber specs (`Air_Scrubber.md`) · component taxonomy (`Architecture/Components.md`) · crypto/root-of-trust (unassigned, EL-006) · Forge-Net implementation (`Architecture/Forge_Net.md`).

### `Operations/Energy.md`
**Status:** Draft · 1/6 · 5 Open Unknowns · Risk: High
**Does:** Incremental energy integration philosophy v0-v1; generation interlocks (syngas/biomass); power mode envelopes; battery protection parameters; Energy Governance Layer (EGL — Demand/Generation/Arbitration/Thermal models, proposed 2026-08-01, audited 2026-08-02, not yet ratified); Storage Model & Battery Governance; Energy Capability Trajectory.
**Does not (arrow):** Deep-environment battery physics (`Tests/Leviathan_testing.md` LT-002) · Leviathan power envelope (`Tests/Leviathan_testing.md` LT-001) · unknown-cell chemistry sorting (`Gate_02_Triage.md`) · crypto/root-of-trust (`Electronics.md` EL-006) · Spec Gate definitions (`Admin/Verification_Gates.md`).

### `Operations/Gate_01_Intake.md`
**Status:** Exploration · 0/6 · 7 Open Unknowns · Risk: Medium
**Does:** Entry protocol for all items; safety screening (hazard/energetic/biological/chemical/radiological); physical document handling; digital reference lookup doctrine; item tagging/provenance; unknown-item hold-and-inspect; fastener/small-component recovery; handoff to Triage.
**Does not (arrow):** Triage workflow detail (`Gate_02_Triage.md`) · reference database schema (`Architecture/Forge_Net.md` GI-001) · cognitive save state (`Architecture/Forge_Net.md` FN-005) · energetic material disposal (unassigned, GI-002) · provenance tracking system (`Admin/Ship_of_Theseus.md` grain system) · facility siting (`Architecture/Facilities.md` FA-001).

### `Operations/Gate_02_Triage.md`
**Status:** Draft · 2/6 · 7 Open Unknowns · Risk: High
**Does:** Core triage principles; false-positive tolerance/bootstrap asymmetry; Strategic Recoverability tiers; Gate correspondence table; queue economics; five triage stations; §XII intelligence/arbitration/capability/maturity extension (proposed, unaudited, explicitly not load-bearing).
**Does not (arrow):** Master gate logic/vocabulary (`Architecture/Forge_flow.md`) · decontamination/air handling (`Air_Scrubber.md` AS-003) · electrical harvesting (`Electronics.md`) · reduction methods (`Gate_03_Reduction.md`) · Anti-Weaponization pattern-matching (`Admin/Ethical_Constraints.md` EC-002) · component taxonomy (`Architecture/Components.md`) · FRT accounting (`Gate_07_Utilization.md`, `Admin/Trajectories.md`) · §XII's constitutional bindingness (explicitly deferred to `Admin/CIR_Gov.md`'s own Binding Status, itself Proposed-Not-Ratified pending GOV-008 — this file cannot promote §XII above that).

### `Operations/Gate_03_Reduction.md`
**Status:** Exploration · 0/6 · 7 Open Unknowns (corrected 2026-08-25 from a stale "8" — GR-003 Resolved 2026-08-24) · Risk: High
**Does:** Reduction permission doctrine and prerequisites; output envelope; prohibited-input catch list; method selection (shredding/cutting/milling); contamination-discovery protocol; dust/fines/particulate handling; emergency shutdown; handoff to Gate_04; bio/chemical waste disposal doctrine (GR-003, Resolved 2026-08-24 — five categories, concrete hold-duration/container values).
**Does not (arrow):** Routing logic into Reduction (`Architecture/Forge_flow.md` Gates A-D) · upstream hazard screening (`Gate_01_Intake.md` GI-002) · machine procurement (unassigned, GR-002) · dust collection hardware (`Air_Scrubber.md`) · energy accounting (`Energy.md`) · facility siting (`Architecture/Facilities.md` FA-001). *(Correction 2026-08-25: this line previously listed "bio/chemical waste disposal (unassigned, GR-003)" as something this file does not own — that was a pre-existing self-reference error, since GR-003 has always been this same file's own unknown, not another file's. Moved to the Does line above, where it belongs, and updated to reflect its 2026-08-24 closure.)*

### `Operations/Gate_04_Separation_Mechanical.md`
**Status:** Exploration · 0/6 · 8 Open Unknowns · Risk: Medium
**Does:** Material Separation Gate design intent; v0 physical subsystems (rotor/sensors/collection zones/fail-to-bin); RPM band/stratification; sensor cross-check confidence scoring; output classification (A/B/C/Unknown Bulk/Fail); scaling/replication doctrine; Bootstrap Proxy Mode.
**Does not (arrow):** Upstream reduction (`Gate_03_Reduction.md`) · thermal processing of Class C (`Gate_05_Separation_Thermal.md`) · triage/human review (`Gate_02_Triage.md`) · air handling (`Air_Scrubber.md`) · energy accounting (`Energy.md`) · marine thermal sink (`Tests/Support_Raft.md`) · biofouling impact (`Tests/Leviathan_testing.md`) · powder feedstock (explicit non-goal, all versions until stated otherwise).

### `Operations/Gate_05_Separation_Thermal.md`
**Status:** Exploration · 0/6 · 9 Open Unknowns · Risk: Medium
**Does:** Spin Chamber operating principle/design intent; v0 geometry/scale; crucible/shell materials; rotation drive philosophy; heating strategy; EM field approach; atmosphere control; extraction interfaces including wire extrusion as a planned interface; failure philosophy.
**Does not (arrow):** Feedstock prep (`Gate_03_Reduction.md`) · mechanical separation (`Gate_04_Separation_Mechanical.md`) · wire extrusion nozzle design (deferred, `Admin/Trajectories.md`) · welding wire specification/qualification (`Architecture/Geck_forge_seed.md`, UNK-008 — corrected 2026-08-08, was inconsistent with this file's own already-correct Lessons Learned citation) · self-replication architecture (`Architecture/Forge_flow.md`, `Architecture/Geck_forge_seed.md`) · facility siting (FA-001) · drive geometry (SC-005).

### `Operations/Gate_06_Fabrication.md`
**Status:** Exploration · 0/6 · 7 Open Unknowns · Risk: Medium
**Does:** Fabrication doctrine/priority order; arc welding as v0 gatekeeper capability; add-to-excess/mill-to-spec philosophy; welding wire feedstock requirements; precision ceiling doctrine; operator safety (PPE/shielding/ventilation); method introduction/qualification criteria; feedback to Component Library.
**Does not (arrow):** Wire extrusion nozzle/draw speed (`Gate_05_Separation_Thermal.md` SC-004) · welding wire chemical qualification (`Architecture/Geck_forge_seed.md`, UNK-008 — corrected 2026-08-08, was stale since 2026-07-19) · laser/powder welding, casting/pressing/forging (deferred, `Admin/Trajectories.md`) · machining hardware selection (this file's own GF-003, genuinely open — a pending design decision, not an ownership gap) · Component Library spec (`Architecture/Components.md`) · precision ceiling ownership (`Architecture/Precision.md`).

### `Operations/Gate_07_Utilization.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns · Risk: Low
**Does:** After-action review doctrine; performance logging minimums; failure mode capture/routing; maintenance frequency tracking; feedback to Fabrication and Forge-Net; retirement handoff doctrine; FRT per-cycle logging (measurement/reinvestment against `Admin/Trajectories.md`'s floor); part lifecycle termination.
**Does not (arrow):** Retirement routing decisions (`Gate_02_Triage.md`) · fabrication methods/precision ceiling (`Gate_06_Fabrication.md`) · component taxonomy (`Architecture/Components.md`) · network trust weighting (`Architecture/Forge_Net.md`) · gate logic (`Architecture/Forge_flow.md`) · energy accounting (`Energy.md`) · FRT floor declaration/v1 baseline (`Admin/Economics.md`).

### `Operations/Plastics.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns · Risk: High
**Does:** Salvaged polymer triage routing; low-pressure oxygen-free pyrolysis conceptual framework; batch-fed reaction chamber/condenser array design requirements; off-gas containment boundaries; char/residue handling.
**Does not (arrow):** Per-polymer temperature profiles · custom extrusion/filament-drawing mechanical blueprints · fractional distillation specs · Air Scrubber hardware (`Air_Scrubber.md`) · intake hazard screening (`Gate_01_Intake.md`) · contamination routing (`Gate_02_Triage.md`) · energy accounting (`Energy.md`) · facility siting (FA-001) · operator PPE (`Admin/Safety_Protocols.md`).

### `Operations/Woodworking.md`
**Status:** Draft · 0/6 · 5 Open Unknowns · Risk: High
**Does:** Timber sourcing hierarchy; felling/chainsaw safety; green wood handling/anisotropic behavior/drying; structural woodgrain deployment; power/hand tool milling for irregular stock; CNC/router fixturing; heat treatment/surface modification; joinery/adhesive/finishing doctrine; waste valorization through papermaking.
**Does not (arrow):** CNC toolpath/G-code/CAM · full shop dust extraction system design (`Air_Scrubber.md`) · structural load-bearing calculations · commercial lumber grading/industrial forestry · facility siting (FA-001) · hearing conservation/PPE sourcing (`Admin/Safety_Protocols.md`).

---

## Gaps Exposed By Building This

1. **Same UNK-008 staleness pattern found in two more files, both fixed same-day.** `Gate_06_Fabrication.md`'s Scope Boundary said welding-wire chemical qualification was "not yet assigned — UNK-008" — wrong since 2026-07-19, when ownership moved to `Geck_forge_seed.md`; the file's own body text (lines 682, 879) already cited UNK-008 correctly elsewhere, only the summary line had drifted. `Gate_05_Separation_Thermal.md`'s Scope Boundary said the same thing more vaguely ("downstream — not yet assigned") — also inconsistent with that file's own Lessons Learned table, which already correctly cited the 2026-07-19 reassignment. Both fixed. Combined with `Forge_flow.md`'s identical error found and fixed yesterday, this makes **three separate files** that had drifted on the exact same fact after the same 2026-07-19 ownership change — worth noting as a pattern: a single ownership reassignment can leave stale pointers scattered across a surprising number of files, none of which cross-check each other.

2. **One "not yet assigned" checked and confirmed genuinely correct, not fixed:** `Gate_06_Fabrication.md`'s GF-003 (machining/milling hardware) really is this file's own open unknown — "not yet assigned" means the hardware choice is pending, not that ownership is unclear. Checked against `Unknowns.md` before assuming it was another instance of the same pattern; it isn't.

3. **No missing or non-conforming Scope Boundary sections in this folder** — all 12 files have complete, conforming content, same as Architecture/ and unlike Admin/'s two structural gaps.

4. **No new hub pattern found distinct from what's already known** — `Architecture/Forge_flow.md` (gate logic/vocabulary) and `Architecture/Facilities.md` (siting, FA-001) are the two most frequently cross-referenced files from this folder, consistent with their already-established roles from the Architecture/ pass, not a new finding.

Three corrections applied this pass (`Gate_05_Separation_Thermal.md`, `Gate_06_Fabrication.md`), consistent with instruction from the human governing authority to fix errors found along the way rather than only catalog them. No new unknowns registered — all three were stale pointers to an already-existing, already-correct ownership record, not open questions.

---

## Resolution Log

- 2026-08-15: **Re-checked against a full day of Operations edits (Gate_02,
  Gate_03, Gate_06, Air_Scrubber) — one small drift found and fixed.**
  Applying `Admin/Resolution_Methodology.md` Pattern 5 for real (a prior
  citation of it in that file's Applied Case sections had mislabeled a
  different step — corrected there too). `Gate_02_Triage.md`'s Scope
  Boundary claimed Air_Scrubber owned "decontamination protocols" outright
  — in tension with TS-002's own disposition-workflow content now living
  in that file. Corrected to distinguish mechanism (Air_Scrubber) from
  workflow (Gate_02). `Gate_03_Reduction.md`'s Scope Boundary checked
  clean — already correctly claimed contamination-discovery doctrine
  before GR-003's new content existed. Smaller-scale instance of the same
  class of finding as the 2026-08-08 UNK-008 catches below, not a new
  failure mode. Human-directed.

- 2026-08-08: **File created — third folder in the Scope_Map rollout**,
  following `Admin/Adm_Scope_Map.md` (2026-08-07) and
  `Architecture/Arc_Scope_Map.md` (2026-08-08). All 12 Operations/ files'
  Status/Spec Gates/Open Unknowns/Risk and full Scope Boundary content
  extracted directly from source, same method as both prior folders. Two
  more instances of the exact UNK-008 staleness pattern found in
  `Architecture/Forge_flow.md` yesterday were found here
  (`Gate_05_Separation_Thermal.md`, `Gate_06_Fabrication.md`) and fixed
  in the same pass, per direct instruction. One look-alike
  ("not yet assigned" on GF-003) was checked against `Unknowns.md` and
  confirmed genuinely correct, not fixed. No missing Scope Boundary
  sections in this folder, unlike Admin/. No new unknowns registered.
  Human-directed.
