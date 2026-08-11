# Safety_Protocols.md — LazarusForgeV0

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> This file governs physical operator safety during Forge operations. Unlike other
> Admin/ governance files, its failure mode is not document drift — it is injury or
> death. Forge operations combine arc flash, molten metal, toxic dust, rotating
> machinery, halogenated polymer off-gas, and sustained high-heat environments. No
> process-level precaution compensates for absent PPE, impaired operator judgment,
> or undefined escalation paths. Open unknown SP-001 (acceptable risk threshold)
> means the boundary between operator-managed risk and mandatory hold has not yet
> been formally defined. Until SP-001 is resolved, the working rule is: when a
> hazard involves irreversible physical harm, escalate to human review before
> proceeding. The cost of a hold is always lower than the cost of a miss.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-06-05                                                          |
| Auditor          | Claude — Architect/Auditor                                          |
| Open Unknowns    | 6                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Acceptable risk threshold doctrine — the line between operator-managed risk and
  mandatory escalation (resolves EP-005)
- PPE requirements by hazard class and operation type
- Hearing conservation doctrine (referenced by `Operations/Air_Scrubber.md`)
- Heat stress doctrine — Arkansas summer operating conditions (referenced by
  `Architecture/Facilities.md` FA-004)
- Operator impairment recognition and response protocol
- Hazard class definitions for physical operator risk
- Pre-operation safety checks — minimum conditions before hot operations begin
- Incident reporting doctrine — what gets logged, where, and by whom

**This file DOES NOT define:**
- Facility physical constraints or zone separation (→ `Architecture/Facilities.md`)
- Air Scrubber hardware specifications (→ `Operations/Air_Scrubber.md`)
- Hazard escalation routing for engineering proposals
  (→ `Admin/Engineer_Protocols.md` §Hazard Escalation Doctrine)
- Anti-Weaponization or Life Preservation hard-floor doctrine
  (→ `Admin/Ethical_Constraints.md` — those are governance constraints, not
  operational safety protocols)
- Legal compliance or regulatory requirements (→ SP-005 — human decision,
  jurisdiction-specific)
- Equipment-specific operating procedures (→ owning gate files)
- Emergency response procedures beyond operator scope (→ SP-006 — not yet defined)

---

## File Purpose

This file is the physical operator safety layer for the Lazarus Forge. It is the
only file in Admin/ whose primary failure mode is not document drift or governance
erosion — it is harm to a person. The other Admin/ protocol files (Auditor_Protocols,
Engineer_Protocols, Security_Protocols, Repository_Integrity_Protocol) govern how
contributors think, verify, trust, and protect documents. This file governs what
operators do to protect themselves while the Forge operates.

Without this file, three specific gaps persist: (1) the acceptable risk threshold
referenced in `Admin/Engineer_Protocols.md` EP-005 has no definition — engineers
cannot determine when a hazard triggers mandatory escalation; (2) hearing conservation
referenced in `Operations/Air_Scrubber.md` has no owning document; (3) heat stress
doctrine referenced in `Architecture/Facilities.md` FA-004 has no owning document.
If this file disappeared, physical operator safety would revert to implicit assumptions
distributed across module files with no governing standard.

**Note on placement in Admin/:** Safety_Protocols.md sits in Admin/ because it sets
repository-wide standards that all Operations/ files reference. It is not an
operational procedure file — it is a doctrine file that operational procedures
implement. The doctrine lives here; the application lives in the owning gate file.

---

## Assumptions

| ID      | Assumption                                                                          | Basis                                        | Confidence | Expiry Trigger                                               |
|---------|-------------------------------------------------------------------------------------|----------------------------------------------|------------|--------------------------------------------------------------|
| ASM-001 | Human operator is physically present during all hot operations at v0                | Bootstrap Doctrine — Components.md ASM-002   | High       | Autonomous operation validated and approved                  |
| ASM-002 | Operator is a capable adult with no undisclosed health conditions affecting heat or noise tolerance | v0 bootstrap context          | Medium     | Operator health screening or expanded workforce confirmed    |
| ASM-003 | PPE is available at the site before hot operations begin                            | Prerequisite — not a during-operation check  | Medium     | Site survey confirms PPE unavailability                      |
| ASM-004 | Arkansas summer heat index regularly exceeds 100°F during operating months          | Geographic and climate baseline              | High       | Site relocated outside Arkansas climate zone                 |
| ASM-005 | Noise levels from Air Scrubber, reduction equipment, and arc welding exceed 85 dB   | Engineering estimate — analogous operations  | Medium     | Site noise survey with calibrated meter contradicts estimate |
| ASM-006 | No formal occupational health program exists at v0 — doctrine is the substitute     | v0 bootstrap realism                         | High       | Formal safety program established with trained personnel     |

---

## I. Acceptable Risk Threshold (EP-005 Resolution)

This section resolves `Admin/Engineer_Protocols.md` EP-005 — the undefined threshold
between operator-managed risk and mandatory escalation.

### Risk Consequence Categories

| Category      | Definition                                                      | Decision Authority        |
|---------------|-----------------------------------------------------------------|---------------------------|
| Minor         | Reversible injury, no lasting impairment — cuts, bruises, minor burns | Operator judgment    |
| Major         | Injury requiring medical attention — deep burns, hearing damage, chemical exposure | Human review before proceeding |
| Catastrophic  | Life-threatening injury or permanent impairment                 | Full Stop — halt all operations |
| Irreversible  | Death, permanent disability, or environmental harm that cannot be undone | Full Stop — halt all operations |

### Escalation Rules

**Operator-managed:** Minor consequence class with known mitigation in place. Operator
may proceed with documented PPE and precautions. Log if novel.

**Mandatory hold — human review required:** Major consequence class, OR any consequence
class where the mitigation is undefined or unvalidated. Do not proceed until a human
operator has reviewed and approved.

**Full Stop:** Catastrophic or Irreversible consequence class, regardless of mitigation
status. Operations halt. No autonomous agent may authorize resumption. Human operator
physically present authorizes restart only after documented review.

### Hard Floor

The Life Preservation heuristics in `Admin/Ethical_Constraints.md` are the absolute
floor beneath this framework. No risk threshold defined here permits actions that
violate those heuristics. The acceptable risk threshold governs operational decisions
within the permitted space — it does not expand that space.

### Cross-Reference

This threshold definition feeds directly into:
- `Admin/Engineer_Protocols.md` §Assumption Challenge Triggers (EP-005 resolution)
- `Admin/Engineer_Protocols.md` §Hazard Escalation Doctrine (escalation routing)
- EP-004 (engineering authority boundary) — authority to accept risk requires a
  defined risk threshold; this provides that definition

---

## II. PPE Requirements by Hazard Class

PPE is not optional at the hazard classes below. Absence of listed PPE is a Full Stop
condition for the associated operation.

### Arc Welding (Hot Zone — Gate_06)

| PPE Item | Minimum Specification | Notes |
|---|---|---|
| Welding helmet | Auto-darkening, shade 10–13 | Fixed shade acceptable at v0 |
| Welding gloves | Heavy leather, gauntlet style | No synthetic substitutes near arc |
| Flame-resistant clothing | Cotton or FR-rated — no synthetics | Synthetics melt to skin |
| Leather boots | Steel-toe preferred | No open-toe footwear in Hot Zone |
| Hearing protection | See Section III | Simultaneous with ventilation noise |

### Induction Heating / Thermal Processing (Hot Zone — Gate_05)

| PPE Item | Minimum Specification | Notes |
|---|---|---|
| Face shield | Full-face, heat-rated | In addition to safety glasses |
| Heat-resistant gloves | Rated to operating temperature | Not welding gloves — different hazard |
| Flame-resistant clothing | As above | |
| Leather boots | As above | |
| Hearing protection | See Section III | |

### Reduction / Milling (Hot Zone — Gate_03)

| PPE Item | Minimum Specification | Notes |
|---|---|---|
| Safety glasses | ANSI Z87.1 minimum | Fragment ejection hazard |
| Face shield | Full-face | Over glasses, not instead of |
| Hearing protection | See Section III — priority hazard | Reduction equipment is loudest operation |
| Dust respirator | N95 minimum; P100 for known toxic materials | See Plastics.md PL-001 for halogenated polymer protocol |
| Leather boots | As above | |

### Electronics Harvesting / Soldering (Warm Zone — Electronics.md)

| PPE Item | Minimum Specification | Notes |
|---|---|---|
| Safety glasses | ANSI Z87.1 minimum | Flux spatter, component ejection |
| Nitrile gloves | Chemical-resistant | Flux, solvents, acid cleaning agents |
| Dust respirator | N95 minimum during desoldering | BFR off-gas — see Electronics.md |
| Ventilation | Forced local exhaust | Not PPE — facility prerequisite |

### Chemical Handling (Warm Zone — Air_Scrubber, Chemistry)

| PPE Item | Minimum Specification | Notes |
|---|---|---|
| Chemical splash goggles | Indirect vent | Not safety glasses |
| Chemical-resistant gloves | Neoprene or nitrile per chemical class | Check compatibility before use |
| Chemical-resistant apron | Over clothing | |
| Face shield | Over goggles for pour operations | |

---

## III. Hearing Conservation Doctrine

Referenced by `Operations/Air_Scrubber.md` as a planned file dependency.

### Exposure Baseline

Sustained noise exposure above 85 dB(A) causes cumulative hearing damage. The Forge
at operating state combines multiple noise sources: reduction equipment, Air Scrubber
fans and blowers, arc welding, and compressors. Combined levels at the operator
position are assumed to exceed 85 dB until a site noise survey confirms otherwise
(ASM-005).

**Bootstrap posture:** Treat all Hot Zone and reduction operations as exceeding 85 dB.
Use hearing protection as a standing requirement, not a situational one.

### Hearing Protection Requirements

| Noise Source | Minimum Protection | Notes |
|---|---|---|
| Reduction equipment (shredder, mill) | 25 NRR earplugs or earmuffs | Loudest single source — priority |
| Air Scrubber at full operation | 25 NRR earplugs or earmuffs | Fan array at load is sustained |
| Arc welding (arc plus ventilation) | 25 NRR earplugs or earmuffs | |
| Combined Hot Zone operation | Double protection (plugs + muffs) | When unsure of combined level |

### Duration Limits (Bootstrap Guidance)

Without a formal audiometric program (ASM-006), use NIOSH time-weighted average
guidelines as the bootstrap proxy:
- 85 dB: 8 hours maximum unprotected
- 91 dB: 2 hours maximum unprotected
- 100 dB: 15 minutes maximum unprotected
- Above 100 dB: protection mandatory, duration minimized

At v0, assume Forge operations fall in the 91–100 dB range until measured otherwise.
Limit unprotected exposure accordingly. Hearing damage is irreversible — this is a
Catastrophic consequence class under Section I.

---

## IV. Heat Stress Doctrine

Referenced by `Architecture/Facilities.md` FA-004 as a planned dependency.

### Arkansas Summer Baseline

Arkansas summer operating conditions (June–September):
- Ambient temperatures: 90–105°F common
- Heat index with humidity: regularly exceeds 105°F, occasionally 115°F+
- Indoor enclosed spaces with hot processes: add 10–20°F above ambient
- Effective operator working environment during summer Hot Zone operations:
  potentially 110–125°F equivalent heat index

This is not a worst-case scenario — it is the expected operating condition for
approximately four months per year.

### Heat Stress Consequence Classes

| Condition | Symptoms | Response |
|---|---|---|
| Heat fatigue | Mild discomfort, reduced concentration | Mandatory rest break, hydration |
| Heat exhaustion | Heavy sweating, weakness, nausea, pale skin | Stop operations, move to cool area, hydrate, monitor |
| Heat stroke | Confusion, hot dry skin, loss of consciousness | Full Stop — medical emergency, call for help immediately |

Heat stroke is Catastrophic consequence class under Section I. Any sign of confusion
or altered mental state in an operator is an automatic Full Stop. An impaired operator
is not a reliable Human Override Interface (Components.md Critical item 8).

### Mitigation Requirements

**Before hot operations in summer months:**
- Water available at the workstation — not across the room
- Minimum one rest break per 45–60 minutes of sustained Hot Zone work
- Second person aware of operator location and expected check-in time
- Operations start time preference: early morning before heat index peaks

**Scheduling doctrine:** When ambient conditions exceed 95°F heat index, schedule
hot operations for early morning or defer. This is not a hard prohibition — it is
a risk mitigation that reduces consequence class from Major toward Minor.

**Acclimatization:** First exposure to Arkansas summer heat should be gradual.
An operator unacclimatized to high heat and humidity will reach heat exhaustion
threshold significantly faster than the typical figures suggest.

---

## V. Operator Impairment Recognition

An impaired operator is a failed Human Override Interface. This section defines
what impairment looks like and what the response is.

### Impairment Indicators

Any of the following in an active operator warrants immediate process hold:
- Confusion, disorientation, or inability to answer simple questions correctly
- Slurred speech or loss of coordination
- Signs of heat exhaustion or heat stroke (Section IV)
- Sustained fatigue causing delayed response to equipment state changes
- Emotional distress sufficient to affect judgment

### Response

1. Halt active processes to safe state (not emergency stop unless required)
2. Remove operator from Hot Zone
3. Assess for heat stress, injury, or other cause
4. Do not resume operations until a capable operator is physically present
5. Log the hold and cause in the operating record

An autonomous agent observing impairment indicators must halt operations and
escalate to human review. This is a non-negotiable constraint — not a suggestion.

---

## VI. Pre-Operation Safety Checklist

Minimum checks before beginning any hot operation session. This is not a
comprehensive procedure — it is the floor below which operations do not start.

- [ ] PPE for the operation type is present and inspected (Section II)
- [ ] Hearing protection available at the workstation (Section III)
- [ ] Water at the workstation (Section IV)
- [ ] Nonburnable flooring confirmed in operating zone (Facilities.md Section I)
- [ ] Egress corridors clear (Facilities.md Section VI)
- [ ] Air Scrubber operational or operation is within Air_Scrubber.md scope
- [ ] No known impairment condition for the operator (Section V)
- [ ] FA-003 (zoning/permitting) status confirmed if this is a first-time site use

If any item cannot be checked: hold. Do not begin hot operations.

---

## VII. Incident Reporting Doctrine

### What Gets Logged

Any of the following requires a log entry:
- Injury or near-miss of any severity
- PPE failure during operation
- Heat stress event (any level)
- Unplanned process hold due to safety condition
- First occurrence of any new hazard not previously documented

### Where It Goes

- Minor incidents and near-misses: Lessons Learned entry in the owning gate file
- Incidents involving novel hazards not covered by existing files: new unknown in
  the most relevant owning file, cross-referenced to this file
- Incidents with Catastrophic or Irreversible consequence class: cross-module entry
  in `Unknowns.md` and mandatory human review before operations resume
- Incidents indicating a gap in this file's doctrine: Active Dispute or new unknown
  here in Safety_Protocols.md

### What Incident Records Must Contain

Minimum content for any incident log entry:
1. Date and operation type
2. Hazard class (Section I consequence category)
3. What occurred
4. Immediate response taken
5. Whether operations were halted and for how long
6. Resolution or follow-up required

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### SP-001 — Acceptable risk threshold: cross-reference confirmation with Engineer_Protocols.md

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | Medium                  |
| Priority      | Major                   |
| Type          | Governance              |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** Section I defines the acceptable risk threshold intended to resolve
EP-005 in Engineer_Protocols.md. This resolution requires confirmation that the
consequence categories and escalation rules here are compatible with the Assumption
Challenge Triggers and Hazard Escalation Doctrine in Engineer_Protocols.md. They
were drafted in parallel, not sequentially.

**Why It Matters:** If the two files define escalation triggers inconsistently,
engineers following Engineer_Protocols.md may reach different hold/proceed decisions
than operators following this file. The threshold must be a single coherent standard.

**Resolution Path:** Cross-file review pass — compare Section I here against
Engineer_Protocols.md §Assumption Challenge Triggers and §Hazard Escalation Doctrine.
Align language and update EP-005 status in Engineer_Protocols.md sidecar.
Also cross-reference EC-001 (sufficient confidence threshold in Ethical_Constraints.md)
as the governance floor.

---

### SP-002 — PPE specifications not sourced to standards

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | Medium                  |
| Priority      | Major                   |
| Type          | Technical               |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** PPE specifications in Section II reference common-sense minimums
(ANSI Z87.1, shade ratings, NRR values) but are not formally sourced to OSHA
standards, NFPA 70E (arc flash), or NIOSH guidance. They may be adequate for
bootstrap but are not validated against regulatory requirements.

**Why It Matters:** An operator following this file in good faith may be under-protected
for the actual arc flash or toxic exposure levels present at a real Forge operation.

**Resolution Path:** Human review pass — cross-reference OSHA 1910 Subpart I (PPE),
NFPA 70E (electrical arc flash), and NIOSH noise exposure guidelines against Section II
and III. Update specifications to reference sourced standards. Assign to human operator
with safety knowledge before first hot operation.

---

### SP-003 — Noise levels at actual Forge site not measured

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | Medium                  |
| Priority      | Major                   |
| Type          | Technical               |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** Section III assumes Forge operations exceed 85 dB based on analogous
equipment estimates (ASM-005). No site noise survey has been conducted.

**Why It Matters:** Hearing protection requirements are calibrated to actual exposure
levels. Underestimating noise levels means inadequate protection. Overestimating means
unnecessary burden that may reduce operator compliance.

**Resolution Path:** Site noise survey with calibrated sound level meter at first
operational run. Update Section III with measured values. Resolve ASM-005 expiry trigger.

---

### SP-004 — Heat stress doctrine not validated against operator experience

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | Medium                  |
| Priority      | Minor                   |
| Type          | Technical               |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** Section IV heat stress doctrine uses published NIOSH and general
climate guidelines. It has not been calibrated to the specific operator, site,
or operational profile of the Forge.

**Why It Matters:** Individual heat tolerance varies significantly. The doctrine
provides a baseline but may need adjustment based on actual operator experience
and site conditions.

**Resolution Path:** Operational calibration — update Section IV after first summer
operating season with observed heat stress incidents or near-misses. This is a
Lessons Learned target, not a blocking issue.

---

### SP-005 — Regulatory compliance and permitting not assessed

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | Medium                  |
| Priority      | Major                   |
| Type          | Governance              |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** This file defines safety doctrine but does not assess whether
Forge operations at a given site require OSHA compliance, fire marshal inspection,
or other regulatory oversight. Aligned with FA-003 in Facilities.md — both are
jurisdiction-specific human decisions.

**Why It Matters:** Operating without required safety permits is a legal risk.
Some jurisdictions require formal safety programs for operations involving arc
welding, chemical handling, or pyrolysis regardless of scale.

**Resolution Path:** Human decision. Cannot be resolved by AI audit. Assign to
human operator at site selection. Cross-reference FA-003 in Facilities.md — resolve
both together.

---

### SP-006 — Emergency response procedures not defined

| Field         | Value                   |
|---------------|-------------------------|
| Status        | Open                    |
| Risk          | High                    |
| Priority      | Major                   |
| Type          | Operational             |
| Blocking      | No                      |
| Owner         | Admin/Safety_Protocols.md |
| First Logged  | 2026-06-05              |
| Last Reviewed | 2026-06-05              |

**Description:** This file defines hazard classification and operator impairment
response but does not define emergency response procedures beyond operator scope —
fire suppression, chemical spill containment, medical emergency escalation, or
site evacuation procedures.

**Why It Matters:** Without defined emergency procedures, operator response to a
serious incident defaults to improvisation under stress. A Catastrophic event with
no procedure is worse than a Major event with one.

**Resolution Path:** Payment via Specification — define minimum emergency response
procedures for: (1) fire in Hot Zone; (2) chemical spill or toxic exposure;
(3) medical emergency (heat stroke, arc flash injury, chemical burn);
(4) site evacuation trigger and assembly point. Requires site-specific information —
defer until FA-001 (site confirmed) is resolved. Cross-reference FA-001.

---

### Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **6** = SP-001–006, matches local +
  `Unknowns.md`. (2) SP-006 High Risk emergency response correctly deferred
  pending FA-001 (site confirmed) — Blocking No appropriate. (3) SP-003 site
  noise measurement cross-links AS-004 (now Blocking Yes for Protocol 1.4
  calibration). (4) No SP-* closed; no PPE/claim advancement. Human-directed.

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-06-05 | Placing Safety_Protocols.md in Operations/ alongside gate files | Safety doctrine is a repository-wide standard referenced by multiple Operations/ files. It belongs in Admin/ for the same reason Auditor_Protocols.md is in Admin/ — it sets standards others implement, not the other way around. | No |
| 2026-06-05 | Combining safety doctrine with Engineer_Protocols.md | Engineer_Protocols.md governs cognitive problem-solving behavior. Safety_Protocols.md governs physical operator protection. Merging them creates scope confusion between how contributors think and how operators stay alive. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional triggers
specific to this file:*

- PPE requirements are amended without a sourced standard reference added
- Section I acceptable risk threshold is altered without cross-reference update
  to Engineer_Protocols.md EP-005
- Heat stress or hearing conservation sections are weakened without operational
  evidence justifying the change
- SP-006 (emergency response) remains unresolved after FA-001 (site confirmed) closes
- Incident reports accumulate in gate files without a corresponding review pass here
