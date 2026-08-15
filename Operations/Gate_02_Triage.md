# Gate_02_Triage.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Triage handles items of unknown provenance, unknown contamination status,
> and unknown energetic content. A component that passes visual inspection
> may still carry chemical contamination, residual charge, or embedded
> hazardous material not visible at Station 0. Contamination bypass —
> a contaminated component passing to electrical or mechanical stations —
> is the highest-risk triage failure mode. Station 0 contamination check
> is mandatory before escalation; it cannot be skipped under throughput
> pressure. Dual-use and weaponization flags must be assessed before any
> component enters the Component Library. **When in doubt, hold at Station 0.
> The cost of a missed hazard is always higher than the cost of a hold.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-09 — Grok pseudo-audit (Skeptic read + minimal fixes); prior: body 2026-07-17; §XII drafted 2026-08-02 still not Gate-1 audited |
| Auditor          | ChatGPT — Synthesizer; Claude — Engineer; Claude — Embedded Value Preservation cross-reference added (human-directed), 2026-07-17; Copilot — drafted TIL/TAL/TCM/TMV + CIR-Triage extension (human-directed), 2026-08-02; Claude — verified against source and `Admin/Verification_Gates.md`, corrective merge (human-directed), 2026-08-02; Grok pseudo-audit 2026-08-09 — no Spec Gate promotion |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Core triage principles and philosophy
- False-positive tolerance doctrine and bootstrap asymmetry
- Strategic Recoverability tier classification
- Gate correspondence table linking triage outcomes to Forge_flow.md gates
- Queue economics doctrine — queues as active allocations
- Five modular triage stations (Station 0 through Station 4)
- Triage Terminal and Human/AI Oversight Gate behavior
- Failure modes and mitigations specific to triage
- Data and learning loop requirements
- Minimum viable triage configuration for Gen-1 Forge
- Guiding axioms
- Interface map to upstream and downstream modules
- §XII: a proposed, unaudited intelligence/arbitration/capability/maturity
  extension to the above (TIL, TAL, TCM, TMV) — candidate doctrine only,
  not yet load-bearing

**This file DOES NOT define:**
- Master gate logic and shared vocabulary
  (→ `Architecture/Forge_flow.md`)
- Decontamination protocols and air handling
  (→ `Operations/Air_Scrubber.md`, AS-003)
- Electrical component harvesting protocols
  (→ `Operations/Electronics.md`)
- Material Recovery and Reduction methods
  (→ `Operations/Gate_03_Reduction.md`)
- Anti-Weaponization pattern-matching mechanism
  (→ `Admin/Ethical_Constraints.md`, EC-002)
- Component taxonomy and graduation rules
  (→ `Architecture/Components.md`)
- Retirement routing decisions for parts returning from service
  (→ this file receives them from `Operations/Gate_07_Utilization.md`;
  routing decisions made here)
- FRT reinvestment accounting
  (→ `Operations/Gate_07_Utilization.md`, `Admin/Trajectories.md`)
- Whether any predicate in §XII is constitutionally binding
  (→ `Admin/CIR_Gov.md`'s own Binding Status section, which is authoritative;
  CIR_Gov.md is itself Proposed — Not Ratified and structurally depends on
  GOV-008 — nothing in this file can promote §XII above that status)
- The definition of Spec Gates 1–6
  (→ `Admin/Verification_Gates.md` — this file does not define its own
  gate categories)

---

## File Purpose

Gate_02_Triage is the decision gateway between reuse and destruction. It
exists to answer one question with speed, honesty, and minimal energy:
can this component or subassembly still function — or be restored to
function — at lower total cost than fabricating a new one?

The Forge is preserving machine work, precision, process history, and
infrastructure inheritance — not just metal. Everything that passes triage
is preserved as embodied complexity. Everything that fails triage enters
material recovery. Triage always occurs before any material enters
destructive processing.

Without this file, the repository lacks the doctrine required to operate
the decision gateway that determines whether material is saved or destroyed.
Premature destruction is irreversible; this file is the primary defense
against it.

---

## Assumptions

| ID      | Assumption                                                                              | Basis                              | Confidence | Expiry Trigger                                              |
|---------|-----------------------------------------------------------------------------------------|------------------------------------|------------|-------------------------------------------------------------|
| ASM-001 | Human operator judgment is the primary triage authority at v0                          | Current automation capability      | High       | Automated classification demonstrated reliable at v0 scale  |
| ASM-002 | Station 0 contamination check reliably identifies visible contamination                | Standard industrial practice       | Medium     | Invisible contamination (chemical, radiological) confirmed present in intake stream |
| ASM-003 | Components entering triage have passed basic safety screening at Gate_01_Intake        | Sequential gate doctrine           | High       | Gate_01 bypassed or abbreviated                             |
| ASM-004 | Queue saturation is detectable before it causes resource deadlock                      | Queue economics doctrine           | Medium     | First operational queue saturation event observed           |
| ASM-005 | Numeric thresholds (70% performance, 5–15 min runtime) are reasonable starting points | Analogous — industrial triage practice | Low     | N≥50 consistent decisions per component class reached       |
| ASM-006 | Dual-use and weaponization patterns are recognizable by a trained operator at Station 0, applying the Pattern Recognition Annex categories | `Admin/Ethical_Constraints.md` EC-002 Pattern Recognition Annex (closed 2026-08-11) | Medium | Station 0 false-positive/false-negative rate diverges materially from Annex expectation once field data exists |

---

## I. Core Principles

**1. Non-Destructive First**
Never destroy or disassemble a component if a non-invasive test can establish viability.

**2. Progressive Depth**
Begin with the fastest, lowest-energy test. Escalate only when value is plausible.

**3. Human–Machine Hybrid**
Human judgment informs classification — it does not bypass the Gate A–D routing sequence defined in `Architecture/Forge_flow.md`.

**4. Energy & Time Accounting**
Each test has a known energy/time cost. A component must justify deeper testing.

**5. Traceability**
Every triaged item receives a physical provenance tag at final disposition recording: component type, source, triage date, station outcomes, final routing decision, and any prior service or repair history.

**6. Ethical Flag at Entry**
Components matching known dual-use or weaponization patterns must be flagged at Station 0 for Oversight review per `Ethical_Constraints.md` before entering the Component Library.

**7. Queues Are Active Allocations, Not Passive Storage**
Triage queues are prioritized operational allocations competing for finite Forge resources: time, energy, tooling, storage volume, and operator attention. Queue priority should favor actions most likely to improve closure of the current Forge operational loop. Inactive queue items eventually consume more Forge resources than material recovery would reclaim.

**8. Strategic Recoverability Is a Triage Axis**
Triage operates on two axes simultaneously:
- *Operational utility* — does this component help now?
- *Strategic recoverability* — could this become impossible or extremely expensive to recreate later?

Components requiring rare materials, specialized tooling, high precision manufacturing, or fragile supply chains should require higher confidence before irreversible material recovery is authorized.

**9. Embedded Value Preservation (added 2026-07-17, ratified — `Challenges/Closed_Loop_Feedstock.md` §2a)**
This principle governs a step Principle 8 doesn't reach: what happens to a component that *fails* triage as a whole. Before a Gate D item proceeds to full material reduction, check whether it contains sub-components that already embody significant manufacturing effort — precision bearings, laminated motor cores, magnet wire, shafts, threaded fasteners — and are separable at lower cost than the value they represent. Extract and preserve those intact; reduce only what's left. Reduction remains the default for the unit as a whole once it has failed triage — this principle narrows what gets reduced, it doesn't reopen the pass/fail decision itself. See §IV Routing table below for where this check occurs.

---

## II. Triage Philosophy

**What the Forge is optimizing for:**
Preservation of recoverable industrial capability under constrained conditions — not salvage quantity, not efficiency alone.

**False-positive doctrine:**
The Forge preferentially tolerates false-positive retention (preserving a bad component) over false-negative destruction (destroying a recoverable one) during bootstrap phases. As the Forge matures, destruction confidence thresholds tighten.

| Forge Stage | Preferred Error |
|---|---|
| Bootstrap | False-positive retention |
| Transitional | Balanced |
| Mature Industrial | False-negative rejection tolerance increases |

Irreversible destruction should require higher confidence than temporary retention. This is not a hoarding doctrine — it is a calibrated asymmetry that acknowledges the cost of irreversibility during early-stage operations.

**Forge-duty sufficiency:**
A component is sufficient for Forge duty if it materially contributes to closure of the current operational loop, not whether it meets original manufacturer specifications. *(See TS-001)*

**Embedded industrial capability:**
The more advanced the artifact, the more condensed civilization may be inside it. A precision harmonic drive, a failed semiconductor component, or a rare alloy casting may be operationally useless today but strategically irreplaceable later. The operator is not merely evaluating component condition — they are evaluating embedded industrial capability.

---

## III. Strategic Recoverability Tiers

| Tier | Meaning | Triage Implication |
|---|---|---|
| Common | Easily reproduced locally | Standard gate routing |
| Constrained | Reproducible with moderate infrastructure | Elevated retention tolerance |
| Strategic | Requires advanced tooling or supply chains | High confidence required before material recovery |
| Critical | Currently irreproducible within Forge capability | Preservation strongly preferred; escalate to Human/AI Oversight Gate |

These tiers influence queue priority, destruction authorization, provenance retention depth, and repurpose restrictions — without making the system bureaucratic.

---

## IV. Gate Correspondence

Triage stations map to the gate logic in `Architecture/Forge_flow.md`:

| Triage Outcome | Flow Gate | Routing |
|---|---|---|
| Station pass — original function confirmed | Gate A pass | Component Library |
| Station pass — function only in reduced/different application | Gate C pass | Repurpose |
| Station partial — failure localized, within current tooling | Gate B pass | Repair & Learn queue |
| Station partial — failure exceeds current tooling capability | Gate B fail → Gate C | Assess for downgrade or Triage Terminal |
| Station fail — no function, material recovery value present | Gate D | Material Recovery (Reduction path) |
| Station fail — no function, no material recovery value | Gate D + Oversight | Triage Terminal |

*Gate D routing to Material Recovery includes an Embedded Value Preservation check (Principle 9) before full reduction — separable high-value sub-components (bearings, cores, magnet wire, shafts, fasteners) are extracted and preserved intact first; only the remainder proceeds to `Operations/Gate_03_Reduction.md`.*

*Worked example:* A pump motor rated 500W runs at 320W under standard pump load — Gate A fail. The same motor drives a ventilation fan at 40% duty — Gate C pass (repurpose to ventilation duty).

---

## V. Queue Economics

Triage queues are not passive storage. They are dynamic resource-allocation decisions under constrained energy, time, and tooling conditions.

**Queue entry requirements:**
Every component entering a repair or repurpose queue must carry:
- Entry date
- Estimated recovery value (qualitative at v0: Low / Medium / High / Strategic)
- Reassessment interval
- Downgrade criteria (conditions under which the item drops to a lower queue or proceeds to material recovery)

**Queue saturation behavior:**
If a queue reaches capacity, the lowest-value items are reassessed before new items are admitted. Queue saturation is a signal that the Forge's repair or repurpose throughput is insufficient — log it as a Forge health indicator.

**Queue decay:**
Items that exceed their reassessment interval without action are automatically flagged for Human/AI Oversight Gate review. The default downgrade path is: repair queue → repurpose queue → material recovery. Human judgment required to hold above the default path.

**Provenance granularity:**
Provenance chains should preserve enough history to identify recurring failure patterns without imposing unsustainable logging burden. Minimum at v0: original source, triage date, station outcomes, any repair events. Richer provenance for Strategic and Critical tier components.

---

## VI. Modular Triage Stations

### Station 0 — Visual & Basic Mechanical

**Purpose:** Rapid rejection of obvious failures. Strategic tier assessment. Contamination check. Dual-use flag.

- Visual inspection for cracks, burns, deformation, corrosion
- Initial strategic recoverability assessment — assign preliminary tier
- Contamination check: chemical or biological contamination routes to decontamination hold before further triage *(see TS-002)*
- Dual-use flag: components matching known high-risk patterns route to Oversight review

Bins: Good / Maybe / Scrap / Contaminated / Flag / Strategic Hold

*"Scrap" means Material Recovery — Reduction path. Not disposal.*

Decision time: < 2 minutes per item

---

### Station 1 — Electrical & Electronic Components

Priority items: motors, transformers, batteries, inverters, PCBs, solenoids

*Cross-reference: `Operations/Electronics.md` for detailed harvesting, desoldering, and integrity check protocols.*

**Pass Guidance:**
≥ ~70% of expected performance or "sufficient for forge duty" *(Placeholder — see TS-001)*

Gate A vs Gate C distinction: performance in original application = Gate A. Performance only in reduced application = Gate C.

Strategic tier override: a motor at 40% performance that requires rare-earth magnets may warrant Strategic Hold regardless of functional gate outcome.

---

### Station 2 — Mechanical Components

Priority items: bearings, gears, linear rails, pumps, structural members

Acoustic assessment requires separation from active Reduction zones — ambient noise produces false failure readings.

Ultrasonic thickness gauges non-trivial to source at Gen-1 — load testing jigs are acceptable substitute.

---

### Station 3 — Functional Subassembly Test

Runtime: 5–15 minutes *(Placeholder)*

| Result | Condition | Routing |
|---|---|---|
| Pass | Performs original or equivalent function | Component Library (Gate A) |
| Partial | Failure localized, within current tooling | Repair & Learn (Gate B) |
| Partial | Failure exceeds current tooling | Assess for downgrade (Gate C) |
| Fail | No function, material has recovery value | Material Recovery — Reduction (Gate D) |
| Fail | No function, no recovery value | Triage Terminal |
| Any | Strategic or Critical tier | Escalate to Human/AI Oversight Gate regardless of functional result |

---

### Station 4 — Assisted Borderline Evaluation (Later-Stage Forge)

Refines borderline calls. Does not override clear Pass or clear Fail from Stations 0–3.

**Anti-overfitting protection:** Assisted evaluation systems may recommend classifications but must preserve auditable reasoning paths and periodic human validation sampling. Historical bias reinforcement — bad historical classifications confirmed by pattern-matching — is a known failure mode. Require human review samples at defined intervals.

---

## VII. Triage Terminal

Every item reaching Material Recovery disposition must pass a structured hold review before irreversible processing begins. This is the Human/AI Oversight Gate from `Architecture/Forge_flow.md` at the triage exit.

- If a credible, active use case exists: assign with defined review date
- If Strategic or Critical tier: require explicit human authorization before material recovery proceeds
- If no genuine need exists: Material Recovery proceeds

*Re-triage:* Components that fail in Forge service re-enter triage at Station 0 with provenance tag indicating prior service history. Recurring failures on same component type trigger pattern logging.

---

## VIII. Failure Modes

| Failure Mode | Description | Mitigation |
|---|---|---|
| Contamination bypass | Contaminated component passes to electrical/mechanical stations | Station 0 contamination check mandatory before escalation |
| Misclassified fatigue damage | Visually acceptable component fails under load | Station 3 runtime testing; provenance history review |
| Queue saturation | Backlog exceeds Forge capacity to process | Queue decay protocol; reassessment triggers |
| False functional validation | Component passes test but fails in service | Re-triage protocol; provenance pattern logging |
| Unsafe repurpose routing | Component repurposed beyond safe degradation threshold | Strategic tier override at Triage Terminal |
| Provenance loss | Component history lost between triage events | Mandatory tag system; re-triage if tag absent |

---

## IX. Data & Learning Loop

Each triage event records: component type, source, strategic tier, tests performed, energy/time spent, decision outcome, eventual fate.

Numeric thresholds (70% performance, 5–15 min runtime) are Placeholder — revise after N≥50 consistent decisions on similar component classes.

Recurring failure patterns on specific component types are flagged for classification rule updates.

---

## X. Minimum Viable Triage (Gen-1 Forge)

- One skilled human operator
- Multimeter
- 12V / 48V battery bank
- Salvaged loads for testing
- Handwritten performance board for known-good components
- Strategic tier log (even a notebook column) for components assessed as Constrained or above

---

## XI. Guiding Axioms

- Test cheap. Destroy expensive.
- A marginal component today beats a perfect ingot tomorrow.
- Doubt means test deeper. Certainty means move fast.
- Scrap means material recovery, not disposal.
- Triage serves the gate logic — it does not replace it.
- The rarer the capability embedded, the higher the confidence required to destroy it.
- Queues are not storage. They are decisions deferred under resource constraint.

> Triage is not about hoarding. It is about respecting embodied work already paid for by the universe.

---

## XII. Proposed Triage Intelligence & Governance Extension (Not Audited)

**Status: Candidate architecture. Drafted 2026-08-02 (Copilot, human-directed).
Has not passed Gate 1 (Fallacy Check) or any other canonical Verification
Gate. Nothing in this section changes Stations 0–4, the Gate A–D routing
table in §IV, or Principle 9 — it proposes an additional layer that would,
if validated, sit alongside them. Payment via Specification only: presence
of this section is not evidence of operational capability.**

The original draft of this material described itself as already
constitutional and cited a "Spec Gate: Constitutional" category. Neither
claim survives contact with the source files: `Admin/Verification_Gates.md`
defines exactly six gates (Fallacy Check, Physical Plausibility, Adversarial
Challenge, Scope Alignment, Cross-Reference Integrity, Conflict Check) with
no seventh "constitutional" tier, and `Admin/CIR_Gov.md` — the file this
draft proposed to bind itself into — is filed Proposed — Not Ratified, 0/6
gates, and states explicitly that nothing should issue a CIR-VERIFIED
transition until GOV-008 is ratified. This section is written below with
that corrected: every predicate is a *candidate*, not a binding rule.

### XII.1 Triage Intelligence Layer (TIL) — proposed

Converts triage events into structured knowledge that could, once
validated, improve pass/fail decisions and threshold calibration.

- **Would record per event:** component class, station path, tests
  performed, outcome (Gate A/B/C/D), later in-service failures/re-triage.
- **Would derive:** failure-mode distributions per class, repair-success
  likelihoods, repurpose-suitability bands, contamination incidence per
  source stream, strategic-scarcity trends.
- **Proposed governance hook:** numeric thresholds (the 70% performance
  figure in TS-001, the 5–15 min runtime figure) would only be eligible for
  revision once TIL shows a stable pattern at N≥50 consistent events per
  class — this is the same bar ASM-005 already sets; TIL would be the
  mechanism for actually clearing it, not a new bar.
- **v0 minimal form:** a structured log (even a spreadsheet) of component
  class, station path, outcome, and later service fate, reviewed manually.
  No tooling exists for this today.

### XII.1a TIL v0 Log Specification — proposed

*Drafted by Grok 2026-08-02, human-directed; verified against source. This
is a concrete implementation of §XII.1's "v0 minimal form," not a new
layer — it formalizes the physical provenance tag Principle 5 already
requires into a loggable record. Same candidate/not-audited status as the
rest of §XII: it does not make TIL operative, it makes TIL *startable*.*

**Fields (single flat table — spreadsheet or paper log, transcribed
weekly):** Event_ID, Triage_Date, Component_Class, Source_Stream,
Strategic_Tier, Station_Path, Tests_Performed, Measured_Performance,
Outcome (Gate A/B/C/D/Hold/Terminal), Embedded_Value_Actions (if Gate D),
Operator, Energy_Time_Cost (optional), Later_Fate, Notes. Most fields are
free-text at v0; only Event_ID, Triage_Date, Strategic_Tier, Station_Path,
Outcome, and Operator are required.

**`Component_Class` is explicitly provisional, not a settled taxonomy.**
This file's own TS-004 records that the Component Library Schema
(`Admin/Canonical_Terms.md` CT-002) is a genuinely open unknown that
*blocks this file's own Specification promotion*. TIL's log should not be
read as quietly resolving CT-002 by starting to use class labels
informally — log free-text component descriptions now, and reconcile
against a controlled vocabulary once CT-002 actually closes. Do not treat
early TIL groupings by class as validated categories.

**Event_ID format:** `YYYY-MM-DD-NNN` (date of final disposition + a
three-digit daily sequence resetting each day, e.g. `2026-08-02-017`).
Assigned by the operator at final disposition, written on the physical
provenance tag and as the log row's first field in the same action. A
re-triage event always mints a *new* Event_ID and links back via
Later_Fate — the original record is never overwritten.

**Closed-loop fate tracking** is what makes the log more than a decision
record: `Later_Fate` (and `Fate_Date`) get written back against the
original Event_ID when a component fails in service, gets repaired, or is
finally retired — via a re-triage event, a periodic (weekly) fate-review
pass over items still in service, or final-disposition notes at material
recovery. Without this, TIL can only describe what was *decided*, not
what turned out to be *correct* — see §XII.1's threshold-revision hook,
which depends on fate data, not just initial-decision counts.

**Deferred: multi-Forge ID extension (`YYYY-MM-DD-Fxx-NNNN`).** A version
of this format that adds a two-digit Forge-site code was also drafted.
It is deliberately *not* adopted now: `Admin/Trajectories.md` TR-GOV-001
and GOV-008's own sidecar are explicit that no second physical host
exists anywhere in this repository yet, and writing a site code onto
every tag today would add friction for a scenario that isn't real —
directly against this same spec's own "start below the tooling
threshold" principle. This is a deferral, not a rejection: the extension
is specified below so it's ready to adopt without a redesign the day it's
actually needed, rather than being invented under time pressure once a
second Forge exists.

*Expansion criteria — adopt `YYYY-MM-DD-Fxx-NNNN` when any of the
following becomes true, not before:*
- *A second physical Forge host is confirmed to exist (the exact
  condition GOV-008 and TR-GOV-001 are already tracking) — this is the
  primary trigger.*
- *Component or provenance data needs to move between two active Forges
  and plain `YYYY-MM-DD-NNN` IDs from each site would collide.*
- *`Admin/Governance_Migration_Protocol.md`'s hardware diversity ladder
  reaches a stage where multi-site coordination doctrine is being
  actively drafted (see TR-GOV-001) — at that point the ID scheme should
  be adopted alongside it, not as an afterthought.*

*Migration path when triggered:* existing `YYYY-MM-DD-NNN` IDs remain
valid as-is; assign the current site `F01` and mint `Fxx` only for new
Forges going forward — no renumbering of historical records required.
This is why the plain format was chosen as primary: it's a strict prefix
of the extended one, so the deferral costs nothing to reverse later.

*Full extended-format specification, held for that trigger:* `Fxx` = `F`
+ 2-digit zero-padded site code (`F01`–`F99`), assigned once from a
central registry when a site comes online. Sequence extends to 4 digits
(`NNNN`, resets daily per Forge) to comfortably exceed any plausible
single-site daily volume. A parallel daily-total field (`Daily_Header:
2026-08-02-F01 | Triage: 23 | Fabrications: 17 | Total: 40`) covers
quantity reporting rather than embedding a running count inside every
individual ID, which was considered and rejected as unnecessary length
and update overhead for Gen-1-scale volumes. Fabrication-artifact IDs
were considered under this same scheme but are out of scope for this
file — if a unified triage+fabrication ID scheme is wanted later, it
belongs in `Admin/Canonical_Terms.md`, which already owns the Component
Library Schema question, not in this file's TIL note.

### XII.2 Triage Arbitration Layer (TAL) — proposed

A candidate resource-allocation scheme for triage under constraint, modeled
on the Energy Arbitration Layer in `Operations/Energy.md` §IV — which is
itself proposed and unaudited as of 2026-08-02. TAL should be read as
depending on that unvalidated layer, not on a proven one.

- **Priority classes:** T₁ safety-critical (contamination check, dual-use
  flag, Oversight escalation) > T₂ strategic preservation (tiering,
  Principle 9 extraction) > T₃ operational utility (Station 1–3 testing,
  Repair & Learn routing) > T₄ opportunistic (extended characterization).
- **Proposed rule:** if T₁ capacity cannot be maintained, hold everything
  at Station 0 — no escalation, no Gate D routing. This is consistent with
  the existing Safety Advisory at the top of this file ("when in doubt,
  hold at Station 0") rather than a new invention.
- **Not yet defined:** what "triage capacity" is measured in, or how it
  would be sensed. No hardware or telemetry for this exists.

### XII.3 Triage Capability Model (TCM) — proposed

A candidate way of stating, explicitly, what the Forge can currently test,
repair, repurpose, decontaminate, and extract — so triage routing reflects
actual capability rather than operator optimism.

- **Domains:** testing, repair, repurpose, decontamination, embedded-value
  extraction — each with a v0/v1/v2+ maturity ladder.
- **Proposed governance hook:** Gate B (Repair & Learn) is only meaningful
  if repair capability is above the minimum rung; Gate D destruction of a
  component with extractable embedded value (Principle 9) is inappropriate
  if extraction capability can't actually reach it yet. This formalizes
  something Principle 9 and the Gate Correspondence table already imply
  qualitatively — it does not change either.

### XII.4 Triage Maturity Vector (TMV) — proposed

A candidate quantitative maturity score across five dimensions — evidence
quality, repair feasibility, contamination confidence, provenance
completeness, strategic recoverability — each 0–3, averaged to a 0–1 score.

- **Proposed rule:** Gate D destruction of a Strategic or Critical tier
  item would require evidence quality ≥1, repair feasibility ≥1, and
  strategic recoverability ≥1. This is a candidate quantification of the
  Human/AI Oversight Gate requirement §IV and §VIII already impose for
  Strategic/Critical tier items — it is not a new authority, and it does
  not lower the existing bar.
- **Not yet defined:** who scores these dimensions, how often, or with
  what evidence. No scoring mechanism exists.

### XII.5 What this section explicitly does not do

- It does not bind CIR. `Admin/CIR_Gov.md` remains the sole owner of any
  claim about constitutional/predicate-gated enforcement, and that file's
  own Binding Status section governs, not this one.
- It does not raise this file's Spec Gates count. Spec Gates remains 2/6
  until an actual Gate 3+ pass occurs on the existing body — drafting §XII
  is not that pass.
- It does not change Stations 0–4, the Gate Correspondence table, or any
  Core Principle. If a future revision wants TIL/TAL/TCM/TMV to actually
  govern routing, that requires editing §IV–§VI directly, with its own
  audit trail — not treating this section as already authoritative.
- It does not stand alone: TAL depends on Energy.md's unaudited EGL, so
  this entire section inherits that dependency's unvalidated status. If
  EGL is later corrected or reworked, this section needs re-review.
- It does not resolve CT-002 (Component Library Schema, tracked at
  TS-004). §XII.1a's TIL log uses free-text component descriptions
  precisely because CT-002 remains open — starting to log is not the
  same as having settled the taxonomy.
- It does not adopt the multi-Forge Event_ID extension. §XII.1a specifies
  it and states the trigger conditions for adopting it, but the format in
  active use today is the single-Forge `YYYY-MM-DD-NNN` form.

See TS-005 through TS-008 below for tracked unknowns against this section.

---

## Interfaces

| Interface | Direction | What crosses |
|---|---|---|
| Intake | → Triage | Raw salvage items with basic safety screening |
| Material Recovery | Triage → | Failed items routed to Reduction path |
| Component Library | Triage → | Passed items cataloged for Fabrication |
| Repair & Learn queue | Triage ↔ | Partially functional items; outcomes feed back |
| Ethical Constraints | Triage → | Dual-use flags escalate here |
| Forge Flow | Reference | Gate logic and terminology standard |
| Operations/Electronics.md | Reference | Electrical component harvesting protocols |
| Air Scrubber | → Triage | Contamination handling; chemical waste from decontamination |
| Architecture/Precision.md | Reference | Tolerance tier standard for Station 1/3 threshold calibration (T0–T4) |
| Architecture/Facilities.md | Reference | Zone separation doctrine — acoustic isolation for Station 2 |
| Operations/Energy.md §IV (proposed, unaudited) | Reference | §XII.2 TAL priority-class model borrows the EAL pattern; inherits its unaudited status |
| Admin/CIR_Gov.md | Reference | §XII explicitly does not bind to this file; see CIR_Gov.md's own Binding Status |
| Admin/Canonical_Terms.md | Reference | Owns CT-002 (Component Library Schema); §XII.1a's TIL log uses free-text `Component_Class` pending that resolution |
| Admin/Trajectories.md | Reference | TR-GOV-001 tracks hardware diversity / second-host status; §XII.1a's multi-Forge Event_ID extension is deferred until that trigger fires |

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                       | What Failed                                                              | What Was Learned                                                                                           | Confidence | Revalidation Needed |
|----------|---------------|------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | "Scrap" used as terminal bin label                   | Operators may interpret as disposal rather than material recovery        | Replaced with "Material Recovery"; vocabulary note added                                                   | Replicated | No                  |
| May 2026 | Audit Review  | Station 3 routed Fail directly to disassembly        | Missing Human/AI Oversight Gate — irreversible action without hold       | Triage Terminal added as mandatory hold before any material recovery proceeds                              | Replicated | No                  |
| May 2026 | Audit Review  | Queues treated as passive storage                    | Risk of latent hoarding, decision fatigue, dead inventory accumulation   | Queues are active allocations with decay, saturation behavior, and reassessment triggers                   | Replicated | No                  |
| May 2026 | Audit Review  | Single triage axis (operational utility only)        | Strategically irreplaceable components destroyed at same confidence threshold as common components | Strategic Recoverability added as second triage axis; four-tier classification system | Analogous  | Yes                 |
| 2026-08-02 | Cross-agent draft review | Copilot drafted TIL/TAL/TCM/TMV as an already-binding constitutional extension | Wrote candidate architecture as though it were ratified: invented a "Spec Gate: Constitutional" category not present in `Admin/Verification_Gates.md`, and bound it into `Admin/CIR_Gov.md` despite that file's own Binding Status explicitly forbidding this | Cross-agent architectural drafts are useful but default to overclaiming operative status; every such draft needs to be checked against the actual gate/ratification state of every file it claims to extend, not just against plausibility | Analogous | Yes — recheck if §XII is ever promoted toward actual gate passage |

---

## Active Disputes

| ID     | Summary                                                                                   | Positions in Conflict                                                        | Risk   | Status | Owner                    |
|--------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|--------|--------------------------|
| DS-001 | Whether retirement handoff from Gate_07_Utilization should trigger automatic re-triage or require operator decision | Automatic re-entry at Station 0 vs. operator-initiated re-triage only | Medium | Open   | Operations/Gate_02_Triage.md |

---

## Auditor Notes & Unknowns

### TS-001 — "Sufficient for forge duty" threshold undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | Yes                            |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | May 2026                       |
| Last Reviewed | 2026-08-14                     |

**Description:** Quantitative or contextual definition of acceptable degraded
performance for forge-duty components remains incompletely defined.

**Why It Matters:** Without a calibrated threshold, triage decisions at the
Gate A/C boundary rely entirely on operator judgment — reproducibility and
cross-operator consistency cannot be verified.

**Resolution Path:** Working definition added: "A component is sufficient if
it materially contributes to closure of the current operational loop." Populate
Baseline Performance Table after N≥50 observations per component class.
Cross-reference `Architecture/Forge_flow.md` FL-001 (gate logic determinism).

**Grok review 2026-08-14:** Path adequate. Working definition is usable; N≥50 bar is correctly retained as the calibration gate. **Grok approved (path adequate).** Remains In Progress — Baseline Performance Table still needs real observations; do not promote on definition alone.

---

### TS-002 — Contamination routing protocol incomplete

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | Yes — contamination bypass is highest-risk triage failure mode (operator harm) |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | May 2026                       |
| Last Reviewed | 2026-08-14                     |

**Description:** Full decontamination criteria, routing for components that
cannot be decontaminated, and provenance tag requirements for contamination
status remain undefined.

**Why It Matters:** Contamination bypass is the highest-risk triage failure
mode — a contaminated component reaching electrical or mechanical stations
creates secondary contamination and potential operator harm.

**Resolution Path:** Station 0 contamination check and Contaminated bin added.
Full decontamination protocol still needed. Cross-reference
`Operations/Air_Scrubber.md` AS-003 (scrubber waste stream and saturation).

**Grok review 2026-08-14:** Partial path adequate — Station 0 + Contaminated bin are real progress. Residual gap (full decontamination criteria, non-decontaminable routing, provenance tag for contamination status) is correctly named. Blocking Yes remains correct. **Grok approved (partial path adequate).** Remains Open — full decontamination protocol still required before treating contamination routing as closed.

---

### TS-003 — Gate logic determinism at boundary cases

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | Yes                            |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | May 2026                       |
| Last Reviewed | 2026-08-14                     |

**Description:** Deterministic routing for all item types at Gate A/C and
Gate C/D boundaries remains incomplete. Strategic tier override creates
additional boundary cases requiring worked examples.

**Why It Matters:** Non-deterministic boundary cases produce inconsistent
triage outcomes across operators and audit cycles — institutional memory
cannot accumulate reliable patterns.

**Resolution Path:** Gate Correspondence table added. Motor worked example
added. Additional worked examples needed for Strategic tier override paths.
Cross-reference `Architecture/Forge_flow.md` FL-001.

**Grok review 2026-08-14:** Path adequate. Table + motor example are real progress; residual need for Strategic-tier override examples is correctly named. **Grok approved (path adequate).** Remains In Progress — additional worked examples still required.

---

### TS-004 — Component Library Schema (discharged — see Admin/Canonical_Terms.md CT-002)

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Resolved — Discharge via Consolidation |
| Risk          | High                           |
| Priority      | Critical                       |
| Type          | Technical / Architectural      |
| Blocking      | Yes — blocks Specification     |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | 2026-06-06                     |
| Last Reviewed | 2026-07-21                     |

**Description:** Originally logged here as "CT-002" — a naming collision with `Admin/Canonical_Terms.md`'s own CT-002, which is the same unknown (Component Library Schema undefined) independently logged eleven days earlier, 2026-05-26. Two sidecars tracked one real question, each with its own Owner field pointing at the *other* file rather than itself.

**Resolution:** Discharged 2026-07-21 (human-directed, surfaced by `Automation/integrity_check.py`'s Unknown Pass). `Admin/Canonical_Terms.md`'s CT-002 is the canonical entry going forward — `Unknowns.md`'s global index already attributed it there before this discharge, making it the de facto owner in practice even though neither file's own Owner field said so. This entry stays here per the Resolved Unknown Discharge Procedure's non-deletion principle (`Admin/Forge_Audit_Kit.md`) — permanent search anchor, ID renamed from the colliding `CT-002` to this file's own local `TS-` convention so it no longer claims a prefix `Admin/Canonical_Terms.md` owns. The underlying question — Component Library Schema — remains genuinely open; only the duplicate tracking is resolved. Still blocks this file's Specification promotion via `Admin/Canonical_Terms.md` CT-002.

**Lessons Learned:** an ID prefix collision between two files (`CT-` used both by its rightful owner and, coincidentally or by copy, by a second file) went undetected for 46 days because nothing checked for it — the same class of gap `Admin/Auditor_Protocols.md`'s AP-025/AP-026 named for version strings and duplicated definitions, now confirmed to apply to sidecar IDs too. `Automation/integrity_check.py`'s Unknown Pass (built specifically to catch this class of bug) found it on its first run against the repository.

---

### TS-005 — Triage Intelligence Layer (TIL) has no implementation

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No — §XII is not load-bearing  |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | 2026-08-02                     |
| Last Reviewed | 2026-08-14                     |

**Description:** §XII.1 proposes converting triage events into structured
knowledge (failure-mode distributions, repair-likelihood curves, etc.). No
log, database, or manual-review process for this currently exists.

**Why It Matters:** TS-001's threshold-revision bar (N≥50 consistent
observations) already exists independently of TIL; TIL would be the
mechanism for actually reaching it, so its absence keeps TS-001 open too.

**Resolution Path:** Stand up the v0 minimal form described in §XII.1 (a
structured log, manually reviewed) as a real, low-effort first step, before
any more elaborate TIL tooling is drafted.

**Grok review 2026-08-14:** Path adequate and correctly minimal. Non-Blocking status is correct while §XII remains proposed/unaudited. **Grok approved (path adequate).** Remains Open — v0 structured log still needs to be stood up.

---

### TS-006 — Triage Arbitration Layer (TAL) depends on an unaudited Energy Governance Layer

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical / Governance         |
| Blocking      | No — §XII is not load-bearing  |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | 2026-08-02                     |
| Last Reviewed | 2026-08-14                     |

**Description:** §XII.2's priority-class model is patterned on
`Operations/Energy.md` §IV's Energy Arbitration Layer, which is itself
proposed and unaudited (Spec Gates 1/6 as of 2026-08-01/02). "Triage
capacity" as a sensed quantity is undefined.

**Why It Matters:** A doctrine layer built on top of another unvalidated
doctrine layer compounds risk — if Energy.md's EGL is revised, TAL needs
re-review, and neither should be treated as operative until its own
foundation clears Gate 1.

**Resolution Path:** Re-review TAL once Energy.md's EGL passes Gate 1.
Do not implement TAL ahead of that.

**Grok review 2026-08-14:** Path adequate and correctly dependency-aware. Non-Blocking status is correct. **Grok approved (path adequate).** Remains Open — blocked on Energy.md EGL Gate 1; do not implement ahead of that.

---

### TS-007 — Triage Capability Model (TCM) capability ladder is undefined against real tooling

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No — §XII is not load-bearing  |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | 2026-08-02                     |
| Last Reviewed | 2026-08-14                     |

**Description:** §XII.3's v0/v1/v2+ maturity ladder across testing, repair,
repurpose, decontamination, and embedded-value extraction has not been
checked against what tooling actually exists at the Forge's current stage.

**Why It Matters:** An overstated capability rung could make Gate B/C/D
routing look more justified than the Forge can actually deliver on.

**Resolution Path:** Populate the v0 rung of each domain against
`Operations/Electronics.md`, `Operations/Air_Scrubber.md`, and
`Architecture/Precision.md`'s actual current tooling before treating any
rung above v0 as real.

**Grok review 2026-08-14:** Path adequate. Correctly requires real tooling check before treating higher rungs as real. **Grok approved (path adequate).** Remains Open — v0 rung population still required.

---

### TS-008 — Triage Maturity Vector (TMV) has no scoring mechanism

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical / Governance         |
| Blocking      | No — §XII is not load-bearing  |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | 2026-08-02                     |
| Last Reviewed | 2026-08-14                     |

**Description:** §XII.4 proposes a five-dimension 0–3 maturity score. No
one is designated to assign these scores, at what cadence, or against what
evidence standard.

**Why It Matters:** An unscored or self-scored maturity vector attached to
a destruction-authorization rule (Gate D for Strategic/Critical tier) would
be worse than no vector at all — it would look quantitative without being
verifiable.

**Resolution Path:** Do not cite TMV scores in any actual Gate D decision
until a scoring owner and cadence are assigned and logged here.

**Grok review 2026-08-14:** Path adequate and correctly conservative — an unscored maturity vector on a destruction-authorization rule would be worse than none. **Grok approved (path adequate).** Remains Open — scoring owner + cadence still required before any Gate D citation.

---

### Resolution Log

- 2026-08-14: **Grok resolution-path review (Round 2 — Operations).** All open/in-progress TS unknowns (TS-001,002,003,005,006,007,008) reviewed against source. TS-004 left untouched (already Resolved — Discharge). Every live Resolution Path judged adequate; residual evidence/implementation needs correctly retained. Markers added; Last Reviewed → 2026-08-14 on all seven live entries. **No TS-* closed.** Open Unknowns remain 7. Blocking status unchanged. Human-directed.

- 2026-08-11: **ASM-006 updated — EC-002 Pattern Recognition Annex closed.**
  `Admin/Ethical_Constraints.md` added the Pattern Recognition Annex EC-002
  had been pending (six intent/complicity-based pattern categories,
  detection method, false-positive handling, escalation path — hooked
  explicitly to this file's Station 0). ASM-006's Expiry Trigger ("EC-002
  pattern-matching mechanism defined") has fired: Basis updated from
  "Current EC-002 status — Placeholder" to the Annex itself, Confidence
  raised Low → Medium (a defined mechanism exists; it has not yet
  accumulated field data), and Expiry Trigger reworded to what would
  actually falsify it going forward — a material false-positive/
  false-negative divergence once Station 0 has real throughput. Not
  raised to High: the Annex is new and unvalidated against live triage
  volume. Core Principle 6's cross-reference to `Ethical_Constraints.md`
  is unchanged and now has a concrete mechanism behind it. No Spec Gate
  change; no TS-* count change. Human-directed.

- 2026-08-09: **Pseudo-audit (Grok — Skeptic/Auditor read + minimal Synthesizer fixes; human-directed).** Correction: TS-002 Blocking No → Yes — file's own "Why It Matters" calls contamination bypass the highest-risk triage failure mode with operator-harm potential; Unknowns.md already indexed Priority Blocking; local Blocking field understated the substance. **Findings (not closed):** F-G2-001 — Open Unknowns 7 = TS-001,002,003,005,006,007,008 (TS-004 Resolved discharge retained); count matches. F-G2-002 — Spec Gates 2/6 left unchanged; §XII explicitly does not raise gate count; no independent Gate evidence package re-verified this pass. F-G2-003 — DS-001 (retirement handoff auto vs operator re-triage) remains Open Active Dispute. F-G2-004 — TS-005–008 correctly non-blocking while §XII proposed/unaudited. Spec Gates **unchanged** 2/6. Status **unchanged** Draft.

- 2026-08-02: **§XII.1a TIL v0 Log Specification added (Event_ID format,
  closed-loop fate tracking, multi-Forge deferral note), human-directed.**
  Grok drafted three implementation docs (TIL v0 log data model,
  closed-loop fate tracking mechanism, and two Event_ID format proposals
  — single-Forge `YYYY-MM-DD-NNN` and multi-Forge `YYYY-MM-DD-Fxx-NNNN`)
  as a follow-on to reviewing the 2026-08-02 §XII corrective merge (that
  review was independently verified and found accurate — a useful
  second-agent confirmation that the corrective merge held up). Verified
  the implementation docs against source before integrating. Merged in:
  the log data model and closed-loop fate mechanism as §XII.1a, an
  implementation of §XII.1's existing "v0 minimal form," not a new layer;
  the single-Forge `YYYY-MM-DD-NNN` Event_ID as the format in active use.
  Flagged rather than silently accepted: `Component_Class` is explicitly
  noted as provisional/free-text pending CT-002 (Component Library
  Schema), which this file's own TS-004 already records as open and
  blocking — the draft had listed it as an ordinary field needing "a
  short controlled list," which undersold that it's a currently-tracked
  blocking unknown, not a small design choice. Deferred rather than
  adopted: the multi-Forge `Fxx` extension — `Admin/Trajectories.md`
  TR-GOV-001 and GOV-008 are explicit that no second physical host exists
  yet, so embedding a site code in every tag today adds friction for a
  scenario that isn't real. Per human direction, the deferral is written
  as an explicit trigger-conditioned expansion note (three named trigger
  conditions, tied to TR-GOV-001) with the full extended-format spec held
  in reserve, rather than dropped — chosen so the extension needs no
  redesign if a second Forge does materialize, since the single-Forge
  format is a strict prefix of the extended one. Fabrication-artifact IDs
  (also proposed under the same scheme) were left out as outside this
  file's Scope Boundary — noted as `Admin/Canonical_Terms.md`'s territory
  if wanted later. No new Open Unknowns — this elaborates TS-005, and the
  CT-002 dependency is already tracked at TS-004.
- 2026-08-02: **§XII Proposed Triage Intelligence & Governance Extension added, corrective merge, human-directed.** Copilot drafted a four-layer extension (Triage Intelligence Layer, Triage Arbitration Layer, Triage Capability Model, Triage Maturity Vector) plus a "CIR-Triage" constitutional-integration block. Verified against source before integrating. Merged in: the TIL/TAL/TCM/TMV architecture itself, as a clearly-marked proposed/unaudited §XII, with governance hooks reframed as candidate rules that formalize existing doctrine (Principle 9, the Oversight Gate requirement, ASM-005's N≥50 bar) rather than new authority. Cut: (1) the "CIR-Triage" section binding these predicates into `Admin/CIR_Gov.md` as constitutional law — CIR_Gov.md is Proposed — Not Ratified, 0/6 gates, and its own Binding Status section states nothing should issue a CIR-VERIFIED transition until GOV-008 is ratified; (2) the invented "Spec Gate: Constitutional" category, which does not exist in `Admin/Verification_Gates.md`'s six canonical gates; (3) all framing that implied Gate D routing, threshold revision, or Oversight Gate decisions are already governed by these predicates — none are, until §XII passes its own Gate 1. Registered TS-005 through TS-008 to track the four sub-layers' lack of implementation, rather than leaving them unregistered. Open Unknowns 3 → 7. Spec Gates unchanged at 2/6 — drafting §XII is not a gate pass.
- 2026-07-21: **CT-002 → TS-004 (Resolved — Discharge via Consolidation), human-directed, surfaced by `Automation/integrity_check.py`.** The sidecar entry previously logged here as "CT-002" collided with `Admin/Canonical_Terms.md`'s own CT-002 — the same Component Library Schema unknown, independently logged there 11 days earlier (2026-05-26). Renamed to this file's own `TS-` convention and marked discharged to `Admin/Canonical_Terms.md`'s CT-002, which `Unknowns.md`'s global index already treated as canonical. Entry retained per the non-deletion principle, not removed. Open Unknowns 4 → 3.
- 2026-07-17: **Embedded Value Preservation cross-reference added (human-directed).** New Core Principle 9, sourced from `Challenges/Closed_Loop_Feedstock.md` §2a's ratification the same day. Governs a step Principle 8 (Strategic Recoverability) doesn't reach: separable high-value sub-components in a triage-failed unit are extracted and preserved before what remains proceeds to full reduction. Routing table (§IV) annotated at the Gate D / Material Recovery row. Does not change the pass/fail triage decision itself — only what happens to material already routed to Reduction.
- May 2026: Gate Correspondence table added.
- May 2026: Motor worked example added to Station 1.
- May 2026: Triage Terminal added — Human/AI Oversight Gate now present.
- May 2026: "Scrap" replaced with "Material Recovery" throughout.
- May 2026: Contamination check added to Station 0.
- May 2026: Ethical Flag added as Principle 6.
- May 2026: Re-triage path for in-service failures added.
- May 2026: Queue Economics section added — queues as active allocations.
- May 2026: Strategic Recoverability axis added — dual triage axes, tier classification.
- May 2026: False-positive doctrine added — bootstrap asymmetry.
- May 2026: Failure Modes section added.
- May 2026: Interfaces section added.
- May 2026: Station 4 anti-overfitting protection added.
- 2026-05-23: Retrofitted to File_Template.md structure. Safety Advisory, File State table, Scope Boundary, File Purpose, Assumptions table, Abandoned Paths, Drift Indicators added. DS-001 (retirement handoff dispute) added to Active Disputes. Stale flat filenames corrected to canonical folder-prefixed paths throughout. Lessons Learned reformatted to full table with Evidence Type and Confidence columns. Sidecar unknowns reformatted to structured table format.
- 2026-06-06: Navigation Anchors block added. Verification Ref corrected to Admin/Verification_Gates.md. Electronics.md cross-reference corrected to Operations/Electronics.md. Duplicate separator removed. Interfaces table updated — Precision.md and Facilities.md added as upstream references. CT-002 cross-reference entry added to sidecar. Open Unknowns updated 3 → 4.
- 2026-07-12: Reordered Abandoned Paths and Drift Indicators to after Auditor Notes & Unknowns, per template order — they previously sat between Active Disputes and Auditor Notes & Unknowns. No other content changed. Same fix applied same day to `Operations/Air_Scrubber.md` and `Operations/Energy.md`.

---

## Abandoned Paths

| Date     | Path                                                                  | Why Abandoned                                                                                           | Reconsider? |
|----------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------|
| May 2026 | Direct Reduction routing for Station 3 Fail without Triage Terminal  | Irreversible action without Human/AI Oversight Gate — permanently abandoned; Triage Terminal is mandatory | No          |
| May 2026 | Single operational utility axis for triage decisions                  | Strategic recoverability is a distinct dimension — optimizing only for current utility destroys future capability | No |
| May 2026 | Queues as passive storage without decay or saturation doctrine        | Passive queues become dead inventory under resource pressure — active allocation doctrine is permanent   | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Station 0 contamination check made optional or skippable under throughput pressure
- Triage Terminal removed or bypassed for any item class
- Dual-use flag assessment removed from Station 0
- Strategic Recoverability tier classification removed or collapsed to single axis
- Queue decay protocol removed or decay interval extended without operational basis
- False-positive doctrine reversed — destruction confidence lowered below retention confidence during bootstrap
- Gate Correspondence table diverges from `Architecture/Forge_flow.md` gate definitions
- Stale flat filenames present in cross-references
- Human/AI Oversight Gate requirement removed for Strategic or Critical tier components
- DS-001 resolved without explicit audit cycle and cross-validation with Gate_07_Utilization.md
- Ethical Anchor field absent, altered, or does not match canonical string
- §XII (TIL/TAL/TCM/TMV) cited as binding, constitutional, or CIR-integrated without GOV-008 existing and CIR_Gov.md being ratified
- §XII treated as having raised this file's Spec Gates count without an actual gate pass on record
- TMV scores or TCM capability rungs cited in an actual Gate D decision without a scoring owner assigned (TS-008) or a v0-tooling check performed (TS-007)

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.
