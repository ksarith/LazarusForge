# Cha_Scope_Map.md — Challenges/

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Adm_Scope_Map.md](../Admin/Adm_Scope_Map.md) | [Architecture/Arc_Scope_Map.md](../Architecture/Arc_Scope_Map.md) | [Operations/Ops_Scope_Map.md](../Operations/Ops_Scope_Map.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is a cross-reference index, not a specification     |
| Open Unknowns    | 0 (surfaces existing unknowns from owning files; creates none)      |
| Owning Domain    | Challenges/                                                          |
| Last Reviewed    | 2026-08-08                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md` if present. |

---

## Purpose

Fourth folder in the Scope_Map rollout, following Admin/ (2026-08-07), Architecture/ and Operations/ (both 2026-08-08). Same method: every entry extracted directly from source, not memory. This folder is structurally different from the first three — it holds two distinct subtypes (Problem-Statement and Solution-Track) with genuinely different File State fields, not a formatting inconsistency. Noted per-file below rather than treated as drift.

---

## Scope Entries

### `Challenges/Biofouling.md`
**Subtype:** Problem-Statement · Status: Active · Version v0.3
**Challenge Class:** External — the pressure exists independent of the Forge.
**Owns:** Crisis framing for marine biological colonization/hull degradation/MIC; engineering requirements for ecosystem-safe fouling management; current architectural responses; long-term accommodation objective.
**Does not own (arrow):** Sacrificial shell design (`Tests/Support_Raft.md`) · anode material selection (`Architecture/Geck_forge_seed.md` GK-002) · hydrodynamic drag/boundary layer (`Architecture/Friction_Dynamics.md` §5.1-5.2) · abrasive wear (`Friction_Dynamics.md` §7.2) · galvanic corrosion (`Support_Raft.md` SR-001) · metal fraction recovery (`Gate_04...`, `Gate_05...`) · polymer texture fabrication (`Plastics.md`) · fouling-as-network-signal (`Tests/Leviathan_testing.md`).

### `Challenges/Closed_Loop_Feedstock.md`
**Subtype:** Solution-Track · Status: Exploration · 0/6 · 10 Open Unknowns (CLF-001-010) · Risk: silent contamination cascades / toolhead destruction (CLF-003/CLF-006)
**Owns:** Persistence Yield ($Y_p$) telemetry model; cross-gate salvage-to-feedstock coordination heuristics; recursive improvement doctrine; §2a Embedded Value Preservation principle (ratified 2026-07-17).
**Does not own (arrow):** Mechanical sorting (`Gate_04...`, `Gate_05...`) · thermal/chemical parameters (`Architecture/Thermal_Systems.md`, `Architecture/Chemistry.md`) · toolpath/fabrication (`Gate_06_Fabrication.md`) · toxic/hazardous handling (`Admin/Ethical_Constraints.md`, `Gate_03_Reduction.md` GR-003).
Note: this file's own Scope Boundary is `## 2. Scope Boundary` — a numbered heading, unlike the unnumbered `## Scope Boundary` convention every Admin/Architecture/Operations file uses. Extraction initially missed it entirely on first pass because of this; corrected before this entry was written. Not itself an error worth fixing — Challenges/ files consistently use numbered section headings throughout (§1 Crisis, §2 Scope, §3 Dependencies, etc.), it's a real structural convention for this folder, not drift. Worth remembering for any future automated tooling that greps for Scope Boundary headings, though: an unqualified `## Scope Boundary` search will silently miss every Challenges/ file that numbers its headings.

### `Challenges/Critical_Minerals.md`
**Subtype:** Problem-Statement · Status: Active
**Challenge Class:** External — geopolitical/geological chokepoints exist independent of the Forge.
**Owns:** Crisis framing for supply chain concentration/geopolitical weaponization/extraction-dependent manufacturing; engineering requirements for urban mining/critical mineral recovery; current architectural responses; technological sovereignty objective.
**Does not own (arrow):** Centrifugal separation/RPM (`Gate_04...`) · selective induction melting (`Gate_05...`) · triage logic (`Gate_02_Triage.md`) · component characterization (`Architecture/Components.md`) · material assay (`Architecture/Chemistry.md`) · fabrication from recovered alloy (`Gate_06_Fabrication.md`) · network contribution (`Architecture/Forge_Net.md`) · valuation economics (`Admin/Economics.md`).

### `Challenges/Emergence.md`
**Subtype:** Problem-Statement · Status: Exploration
**Challenge Class:** Reflexive — unlike every other file in this folder, this pressure is created by the Forge's own capability (autonomous agent deployment), not by an external condition. Explicitly self-distinguished in its own text from the six External-class files.
**Owns:** Crisis framing for emergent intelligence in distributed autonomous systems; alignment-by-environment engineering requirements; current architectural responses; human-AI co-existence objective.
**Does not own (arrow):** Hardware watchdog specs (`Architecture/Cognitive_Frameworks.md` CF-001) · correlated AI failure modes (`Cognitive_Frameworks.md` CF-002) · firmware trust/Logic-Zero (`Operations/Electronics.md`) · multi-agent consensus gates (`Admin/Verification_Gates_LF.md`) · closed-loop behavioral feedback (`Gate_07_Utilization.md`) · Tier 1 corrigibility (Q-3, `Admin/Governance_Charter.md`).

### `Challenges/Energy_Scarcity.md`
**Subtype:** Problem-Statement · Status: Active
**Challenge Class:** External — energy poverty/grid fragility/fossil dependency exist independent of the Forge.
**Owns:** Crisis framing for the structural gap between energy-as-precondition and its uneven/fragile/absent delivery; energy-access engineering requirements; current architectural responses; community energy sovereignty objective.
**Does not own (arrow):** Forge's own operational energy strategy (`Operations/Energy.md` EV-001/002/003) · deep-environment battery physics/Leviathan power envelope (`Tests/Leviathan_testing.md` LT-001/002) · superconductivity horizons (`Energy.md` §Superconductivity Horizons) · heat pump/moisture yield/thermal recovery (`Architecture/Thermal_Systems.md` TH-001/003) · cost baseline (`Admin/Economics.md` EC-002) · waste heat (`Waste.md`).
**Explicit self-distinction (worth preserving verbatim, not just summarizing):** *"`Operations/Energy.md` answers 'how does the Forge power itself.' This file answers a different, prior question — 'why does energy access matter enough that the Forge should treat it as a purpose, not just a utility bill.'"* Same relationship as Water.md has to Living Waters.

### `Challenges/Planned_Obsolescence.md`
**Subtype:** Problem-Statement · Status: Active
**Challenge Class:** External — designed unrepairability exists as industrial practice independent of the Forge.
**Owns:** Crisis framing for designed unrepairability/firmware lock/repair-economy elimination; non-destructive recovery engineering requirements; current architectural responses; objective of making obsolescence structurally untenable.
**Does not own (arrow):** Thermal desoldering/integrity verification, Logic-Zero re-baselining, counterfeit detection (all `Operations/Electronics.md`, EL-008 for the last) · thermal delamination (`Gate_02_Triage.md` Station 1) · polymer enclosure upcycling (`Plastics.md`) · provenance/identity doctrine (`Admin/Ship_of_Theseus.md`) · toxic stream handling (`Air_Scrubber.md`, `Electronics.md`).

### `Challenges/Return_To_Eden.md`
**Subtype:** Solution-Track · Status: Exploration · Gates: None cleared (G1-G2 conditional, G4-G6 cleared per 2026-06-30 audit) · 5 Open Unknowns (RE-UNK-001-005) · Risk: RE-UNK-001 (Eden Index variables formally specified but not operationally measurable; RE-UNK-005 directly dependent)
**Owns (In-Scope):** Eden Index ($I_E$) as cross-system evaluation heuristic; four Technical Challenge Tiers; Primary Challenge Metrics as index-level pass/fail criteria; the systemic "toward or away from Eden" heuristic question applied at architecture level.
**Does not own (arrow):** Hardware/mechanical implementation (`Air_Scrubber.md`, `Plastics.md`, `Woodworking.md`) · governance mechanics (`Admin/Governance_Charter.md`, `Admin/Auditor_Protocols.md`) · chemical/analytical assay (`Architecture/Chemistry.md`) · water-quality remediation (`Tests/Living_Waters.md`) · measurement instrument spec (`Experiments.md`, pending RE-UNK-001/005).
**Explicitly states its own limit:** "This file sets the objective function; it does not prescribe how any individual module hits it."

### `Challenges/Waste.md`
**Subtype:** Problem-Statement · Status: Active
**Challenge Class:** External — waste as structural condition exists independent of the Forge.
**Owns:** Crisis framing for discretionary waste/repair-capacity loss/repair-economy dismantling; salvage-first recovery engineering requirements; current architectural responses; community material sovereignty objective.
**Does not own (arrow):** Gate routing logic (`Architecture/Forge_flow.md`) · triage sequence (`Gate_02_Triage.md`) · mechanical/thermal separation (`Gate_04...`, `Gate_05...`) · fume/off-gas containment (`Air_Scrubber.md`) · polymer pyrolysis (`Plastics.md`) · utilization feedback (`Gate_07_Utilization.md`) · network federation (`Architecture/Forge_Net.md`).

### `Challenges/Water.md`
**Subtype:** Problem-Statement · Status: Active
**Challenge Class:** External — water scarcity/contamination exist independent of the Forge.
**Owns:** Crisis framing for the gap between recognized water rights and lived reality; remediation-approach engineering requirements; current responses under the Living Waters initiative; community water sovereignty objective.
**Does not own (arrow):** Heat pump sizing (`Architecture/Thermal_Systems.md` TH-001) · atmospheric moisture yield (`Thermal_Systems.md` TH-003 — **explicitly flagged Blocking for Living Waters deployment**, the only cross-reference in this entire folder carrying that designation) · Peltier characterization (`Thermal_Systems.md` TH-004) · venturi scrubbing/airflow (`Architecture/Friction_Dynamics.md` §4) · Spin Chamber applications (`Gate_04...`, `Gate_05...`) · biochar production (`Plastics.md`).

---

## Gaps Exposed By Building This

1. **No missing Scope Boundary content anywhere in this folder** — every one of the 9 files has real, substantive scope text. `Closed_Loop_Feedstock.md` briefly looked like a repeat of Admin/'s missing-section pattern during extraction, but was a false alarm caused by this folder's own numbered-heading convention (`## 2. Scope Boundary` vs. the unnumbered `## Scope Boundary` every other folder uses) — worth documenting as a real structural difference between folders, and as a note for any future tooling: an unqualified heading search will silently miss every file in this folder.

2. **This folder has a genuinely different two-subtype structure**, confirmed rather than assumed: 7 Problem-Statement files (no Spec Gates/Highest Risk by design — External or Reflexive pressures the Forge responds to, not specifications it fulfills) and 2 Solution-Track files (`Closed_Loop_Feedstock.md`, `Return_To_Eden.md` — these do carry Spec Gates and Open Unknowns, same as an Admin/Architecture/Operations file would). Both subtypes use "This file owns / does not own" phrasing rather than "DOES/DOES NOT define" — a consistent folder-wide convention distinct from the other three folders' template.

3. **One Blocking cross-reference found, worth surfacing on its own:** `Water.md`'s dependency on `Thermal_Systems.md` TH-003 (atmospheric moisture yield) is explicitly marked Blocking for Living Waters deployment — the only Blocking-flagged cross-reference anywhere in this folder's nine files. Not a documentation error, just worth naming directly since it's the one place in Challenges/ where a downstream dependency actually gates real deployment rather than just describing division of doctrine ownership.

4. **6 of 7 Problem-Statement files share nearly identical framing language** ("Challenge Class," "Negative-space principle," the exact sentence "The Forge's architecture is the fossil record of the pressures that shaped it...") — `Emergence.md` is the sole Reflexive-class file and explicitly contrasts itself against the other six's External classification in its own text. This is a healthy, deliberate template consistency, not drift — flagged here only because, like the peer-group and hub findings in the prior two folders, it's a pattern only visible once every file is read together.

No corrections were needed in this folder — no stale cross-references, no missing sections, no look-alike false positives requiring a check. Unlike Operations/, this pass found nothing to fix.

---

## Resolution Log

- 2026-08-08: **File created — fourth folder in the Scope_Map rollout**,
  following Admin/ (2026-08-07), Architecture/ and Operations/ (both
  2026-08-08). All 9 Challenges/ files' subtype, Status, and full scope
  content extracted directly from source. One extraction false-positive
  (`Closed_Loop_Feedstock.md` appeared to have no Scope Boundary section
  on first pass, due to this folder's numbered-heading convention) caught
  and corrected before being stated as a finding — documented as a real
  structural note rather than silently fixed and forgotten, since it's a
  genuine trap for any future automated tooling. No stale cross-references
  or corrections needed this pass, unlike Operations/. Confirmed the
  Problem-Statement/Solution-Track subtype split is real and consistent,
  not folder-level drift. Human-directed.
