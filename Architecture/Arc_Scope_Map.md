# Arc_Scope_Map.md — Architecture/

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Adm_Scope_Map.md](../Admin/Adm_Scope_Map.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is a cross-reference index, not a specification     |
| Open Unknowns    | 0 (surfaces existing unknowns from owning files; creates none)      |
| Owning Domain    | Architecture/                                                       |
| Last Reviewed    | 2026-08-08                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md` if present. |

---

## Purpose

Second folder in the Scope_Map rollout, following `Admin/Adm_Scope_Map.md` (2026-08-07, confirmed pushed to main and renamed with the folder-abbreviation-prefix convention this file now follows: `Arc_` for Architecture/). Same method: every entry below extracted directly from its file's own File State and Scope Boundary sections, not reconstructed from memory. Where this summary and a file's own Scope Boundary conflict, the file wins — same rule the Admin/ version and `Discovery.md` both already state.

---

## Scope Entries

### `Architecture/Chemistry.md`
**Status:** Draft · 1/6 · 8 Open Unknowns · Risk: High
**Does:** Electrochemical corrosion doctrine; acid-base and redox fundamentals; contamination identification chemistry; polymer degradation chemistry; surface chemistry; battery/electrochemical cell chemistry; Chemical Operator Minimum Competency appendix.
**Does not (arrow):** Engineering fundamentals (`Engineering.md` — peer) · heat transfer/thermal runaway (`Thermal_Systems.md` — peer) · fluid flow (`Friction_Dynamics.md` — peer) · Air Scrubber hardware (`Operations/Air_Scrubber.md`) · pyrolysis reactor design (`Operations/Plastics.md`) · battery thermal containment (`Operations/Energy.md` EV-003).
**Peer group:** explicitly declares itself a peer to Engineering.md/Thermal_Systems.md/Friction_Dynamics.md — same authority level, intersections require both, neither overrides, conflicts escalate to human.

### `Architecture/Cognitive_Frameworks.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns · Risk: High
**Does:** Cognitive reliability architectures; distributed trust/redundancy; Framework taxonomy A-G; confidence collapse states; split-brain handling; algorithm architecture (Section IX); Epistemic Load Regulation / Triage Posture.
**Does not (arrow):** PCB/MCU wiring, hardware watchdog circuit (`Operations/Electronics.md`, CF-001) · mechanical actuators (`Mechanical_Structures.md`) · ethical policy (`Admin/Ethical_Constraints.md`) · Leviathan mission logic (`Tests/Leviathan_testing.md`) · networking (`Forge_Net.md`) · crypto (`Admin/Security_Protocols.md`) · autonomous governance law (`Admin/Governance_Charter.md`) · debt measurement implementation (CF-004).
Note: gained an `## Authority & Tier Classification` preface 2026-08-07 (verified against source before applying) explicitly stating it does not alter Tier-1 Axioms or override the Charter/Auditor_Protocols/Ethical_Constraints — the clearest explicit non-claim statement of any file in this folder.

### `Architecture/Components.md`
**Status:** Exploration · 0/6 · 2 Open Unknowns · Risk: Low
**Does:** Component taxonomy v0-v3; Critical/Useful/Bootstrap classification; Bootstrap Doctrine and Graduation Rule; dual-use annotation standard.
**Does not (arrow):** Electronics/software/biological/optical fabrication systems · individual component engineering specs · G.E.C.K. manifest (`Geck_forge_seed.md`) · precision/tolerance doctrine (`Precision.md`) · cross-module governance.

### `Architecture/Engineering.md`
**Status:** Draft · 3/6 · 7 Open Unknowns · Risk: High
**Does:** Foundational engineering principles and decision frameworks; materials behavior overview; Reference Deployment Context (RDC) baseline; hierarchy of engineering evidence.
**Does not (arrow):** CNC/gantry structural specifics (`Mechanical_Structures.md` — peer) · heat transfer/thermodynamics (`Thermal_Systems.md` — peer) · fluid mechanics/tribology (`Friction_Dynamics.md` — peer) · chemistry/corrosion (`Chemistry.md` — peer) · domain fabrication techniques (`Operations/`).
**Peer group:** same four-file peer declaration as Chemistry.md above, from the reciprocal side — this file owns broad principles, the other four own their named domains.

### `Architecture/Facilities.md`
**Status:** Exploration · 0/6 · 4 Open Unknowns · Risk: High
**Does:** Minimum physical environment constraints; nonburnable flooring prerequisite; airflow topology; triangle workstation layout; **Reference Deployment Context (RDC)** — the declared climate/site baseline other files substitute their own parameters against; Site Initialization Checklist (§VII).
**Does not (arrow):** Air Scrubber specs (`Operations/Air_Scrubber.md`) · safety/PPE (`Admin/Safety_Protocols.md`) · energy infrastructure (`Operations/Energy.md`) · legal zoning (FA-003, human decision) · marine/off-site environments (`Tests/Support_Raft.md`, `Tests/Leviathan_testing.md`).
**Hub role:** the RDC baseline defined here (§VII) is explicitly referenced as the substitution point by four other files in this folder — Engineering.md, Friction_Dynamics.md, Thermal_Systems.md, and this file's own definition. Not visible from any single one of those files alone; only visible juxtaposed.

### `Architecture/Forge_Net.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns · Risk: Medium
**Does:** Decentralized forge networking philosophy; data layer architecture; shared knowledge base/contribution doctrine; cognitive save state architecture; cluster formation/governance emergence; trust weighting; node loss doctrine; network security threat model.
**Does not (arrow):** Physical networking hardware (unassigned) · database implementation (unassigned) · cluster voting mechanisms (emergent, cannot specify before observed) · delay-tolerant networking (`Tests/Leviathan_testing.md`) · rogue node containment (`Cognitive_Frameworks.md`) · network energy cost (`Operations/Energy.md`) · data privacy/access control implementation (unassigned — FN-005).

### `Architecture/Forge_flow.md`
**Status:** Exploration · 0/6 · 2 Open Unknowns · Risk: Medium
**Does:** Minimal viable v0 operational logic; **reference standard for shared vocabulary across the entire repository** — terms defined here carry into all other documents unless noted, now explicitly acknowledging `Admin/Canonical_Terms.md`'s adjacent role (fixed 2026-08-08); eight sequential decision gates; Gate Correspondence table; primary KPI definition.
**Does not (arrow):** Module hardware specs (`Operations/Gate_04...`, `Gate_05...`) · reduction module spec (`Operations/Gate_03_Reduction.md`) · triage workflow (`Operations/Gate_02_Triage.md`) · energy accounting (`Operations/Energy.md`) · autonomous/AI trust architecture (`Cognitive_Frameworks.md`, `Admin/Ethical_Constraints.md`) · version roadmap (`Admin/Trajectories.md`) · facility siting (`Facilities.md`) · fabrication output/wire qualification (`Geck_forge_seed.md`, UNK-008 — reference corrected 2026-08-08).

✅ **Both findings below fixed 2026-08-08, same day they were surfaced — kept here as a record, not a live warning:**
- **Stale cross-reference (was real, concrete, now corrected):** this file's Does-Not list said fabrication/wire qualification was "→ UNK-008 — no owner assigned." Checked directly against `Unknowns.md`: UNK-008's ownership was reassigned to `Architecture/Geck_forge_seed.md` on 2026-07-19, three weeks before this finding surfaced. Fixed in `Forge_flow.md` directly.
- **Asymmetric cross-reference (was softer, now acknowledged):** this file claimed sole "reference standard for shared vocabulary" without mentioning `Admin/Canonical_Terms.md`, which already correctly deferred to this file from its own side. Added a one-sentence reciprocal acknowledgment in `Forge_flow.md`.

### `Architecture/Friction_Dynamics.md`
**Status:** Draft · 2/6 · 4 Open Unknowns · Risk: Medium
**Does:** Fluid mechanics doctrine (pressure, flow regimes, Bernoulli, pipe flow); aerodynamics (drag, lift, boundary layers, Reynolds number); tribology (friction, wear, lubrication); Reynolds number as universal flow-regime classifier; Reference Deployment Context baseline.
**Does not (arrow):** Engineering fundamentals (`Engineering.md` — peer) · heat transfer in flow systems (`Thermal_Systems.md` — peer) · Air Scrubber specs (`Operations/Air_Scrubber.md`) · Gate_04/05 rotor/crucible parameters (`Operations/Gate_04...`, `Gate_05...`) · Support Raft hull design (`Tests/Support_Raft.md`) · Leviathan mission logic (`Tests/Leviathan_testing.md`) · bearing dimensional specs (`Components.md`).

### `Architecture/Geck_forge_seed.md`
**Status:** Exploration · 0/6 · 3 Open Unknowns · Risk: Medium
**Does:** Minimum viable seed to instantiate a new Forge; core G.E.C.K. module list and criticality rationale; procurement doctrine; precision-as-capability-threshold (introductory); marine variant module list (exploratory); success criteria and v1 scaling pathway. **Owns UNK-008** (welding wire spec/qualification, reassigned here 2026-07-19) — see Forge_flow.md's stale cross-reference above.
**Does not (arrow):** Detailed G.E.C.K. module engineering specs · full precision doctrine (`Precision.md`) · Leviathan/deep-marine systems (`Admin/Trajectories.md`) · energy infrastructure beyond portable minimum (`Operations/Energy.md`) · component taxonomy (`Components.md`).

### `Architecture/Mechanical_Structures.md`
**Status:** Draft · 2/6 · 4 Open Unknowns · Risk: High
**Does:** Structural frame rigidity/damp-filling standards; thermal expansion mitigation and coordinate delta compensation; kinematic protection loops, shunt current monitoring, torsional alignment interlocks; sacrificial shear pins; falsifiable mechanical performance metrics; contamination/bearing protection doctrine.
**Does not (arrow):** Engineering fundamentals (`Engineering.md` — extends into fabrication machinery specifically, not a peer split) · tool-path G-code/part geometries · motor driver circuits (`Operations/Electronics.md`) · compressed air/back-pressure specs (`Operations/Air_Scrubber.md`, ME-002) · precision/tolerance doctrine (`Precision.md`).
**Reciprocal link confirmed:** `Thermal_Systems.md` explicitly names this file as owning "structural response" to the temperature inputs it generates (§Thermal Expansion Disconnect) — checked, this file's own text doesn't restate that link from its side, but doesn't contradict it either; a minor one-directional documentation gap, not a conflict.

### `Architecture/Precision.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns · Risk: High
**Does:** Precision as capability ceiling (declaration/tracking/revision); tolerance classification tier system (repository-wide standard); metrology doctrine for salvaged equipment (resolves CO-002); measurement uncertainty doctrine; fabrication-precision feedback loop (Gate_07 revises Gate_06 ceiling); precision floor doctrine; Arkansas climate dimensional effects.
**Does not (arrow):** Engineering fundamentals (`Engineering.md`) · kinematic interlock thresholds (`Mechanical_Structures.md`) · G-code/CAM workflows, arc welding qualification (`Operations/Gate_06_Fabrication.md`) · chemical/thermal metrology (`Chemistry.md`, `Thermal_Systems.md`) · quality certification (GU-003, unassigned).

### `Architecture/Thermal_Systems.md`
**Status:** Draft · 1/6 · 6 Open Unknowns · Risk: High
**Does:** Laws of thermodynamics as operational doctrine; heat transfer modes; thermal impedance/resistance; insulation doctrine; heat pump/Peltier/TEG doctrine; Reference Deployment Context thermal baseline; cross-module thermal integration hooks; explicit "thermal expansion bridge" to Mechanical_Structures.md.
**Does not (arrow):** Engineering fundamentals (`Engineering.md` — peer) · Gate_05 operating parameters (`Operations/Gate_05_Separation_Thermal.md`) · Air Scrubber thermal fault monitoring (`Operations/Air_Scrubber.md`) · battery thermal containment (`Operations/Energy.md` EV-003) · structural response to thermal expansion (`Mechanical_Structures.md` §Thermal Expansion Disconnect — this file generates the inputs, that file owns the response) · pyrolysis thermal profiles (`Operations/Plastics.md`).

---

## Gaps Exposed By Building This

1. **`Forge_flow.md`'s UNK-008 cross-reference was stale — a real, concrete, verified error, fixed same-day.** Ownership moved to `Geck_forge_seed.md` on 2026-07-19; this file's text still said "no owner assigned" until corrected 2026-08-08.

2. **`Forge_flow.md` and `Admin/Canonical_Terms.md` had an asymmetric vocabulary-authority relationship — also fixed same-day.** Was already resolved in practice (Canonical_Terms.md deferred correctly); now documented from both sides.

3. **Unlike Admin/, every file in this folder has a genuine, conforming Scope Boundary section.** No missing-section findings here — Architecture/ is structurally cleaner than Admin/ was.

4. **Two real hub patterns, visible only in aggregate:** the five-file Engineering/Mechanical_Structures/Thermal_Systems/Friction_Dynamics/Chemistry peer group (explicitly self-declared, consistent from every member's side, checked), and Facilities.md's Reference Deployment Context baseline (referenced by name from three other files' own Scope Boundary text: Engineering.md, Friction_Dynamics.md, Thermal_Systems.md). Both are healthy patterns, not gaps — flagged here only because, same as `Governance_Charter.md`'s hub role in Admin/, this concentration isn't visible from reading any single file in isolation.

5. **One asymmetric-but-resolved cross-reference confirmed clean:** `Mechanical_Structures.md` doesn't restate its Thermal_Systems.md-declared "owns structural response" role from its own side, but doesn't contradict it either. Checked, not flagged as an error — noted for completeness.

No new unknowns registered. Finding 1 is a one-line factual correction candidate in `Forge_flow.md`, not filed as a new tracked unknown — it's a stale pointer, not an open question.

---

## Resolution Log

- 2026-08-08: **Both findings from this file's initial build (stale UNK-008
  reference, asymmetric vocabulary acknowledgment) fixed same-day in
  `Architecture/Forge_flow.md` directly** — James specifically asked for
  errors to be corrected as this rollout continues, not just cataloged.
  Entries above and in Gaps Exposed updated to reflect closure rather than
  rewritten as if the findings never existed, matching this repository's
  general preference for showing what was found and then what was done
  about it. Human-directed.

- 2026-08-08: **File created — second folder in the Scope_Map rollout**,
  following `Admin/Adm_Scope_Map.md` (2026-08-07, confirmed pushed to main
  and renamed with the `Adm_` prefix convention this file now follows as
  `Arc_`). All 12 Architecture/ files' Status/Spec Gates/Open Unknowns/Risk
  and full Scope Boundary content extracted directly from source
  (Python-assisted, spot-verified), same method as the Admin/ pilot. One
  concrete stale cross-reference found and verified against `Unknowns.md`
  directly (`Forge_flow.md`'s UNK-008 claim, wrong since 2026-07-19) and
  one softer asymmetric-documentation gap (Forge_flow.md/Canonical_Terms.md
  vocabulary authority, already resolved in practice, undocumented from one
  side). Unlike Admin/, no files in this folder lack a Scope Boundary
  section — noted as a genuine structural difference between folders, not
  assumed. No new unknowns registered. Human-directed.
