# Lazarus Forge — v0 Operational Flow

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> This document governs decision logic that leads to irreversible
> actions. Reduction sits at R4 — the flow's highest-consequence
> boundary — once an item is shredded or milled, it cannot be
> recovered as a discrete object. Gate logic errors at any stage
> can accelerate material toward reduction prematurely.
>
> Approach gate decisions thoughtfully. When uncertain, the
> system is designed to hold — not to proceed. Refusal and
> deferral are first-class outputs at every gate. Human
> judgment overrides automation at any point. The cost of
> a missed recovery is permanent.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-09-08 (Flow State/Transition Model added, Gate D reframed, FL-001 sidecar/Resolution Log desync corrected); prior: 2026-08-08 |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 2                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Minimal viable operational logic of the Lazarus Forge v0
- Reference standard for shared vocabulary across the repository —
  terms defined here carry their meaning into all other documents
  unless explicitly noted otherwise. `Admin/Canonical_Terms.md`
  covers a separate, broader vocabulary layer; where the two
  overlap, this file is authoritative for operational routing
  semantics, and `Canonical_Terms.md` itself defers to this file
  on that point.
- v0 scope, inputs, and explicit non-goals
- Defined Terms for all shared operational vocabulary
- Eight sequential decision gates (Intake through Utilization)
- Gate Correspondence table mapping triage outcomes to gates
- Outcome paths and reversibility notes for each path
- Fabrication priority order and want/need policy
- Feedback and learning doctrine for v0
- Primary KPI definition (value recovered per kWh consumed)
- Termination conditions for items exiting the system
- Human/AI Oversight Gate logic and want/need policy
- Purification stage definition — governs DS-001 terminology dispute
- Self-replication architecture or loop closure logic, as pointed
  to from `Operations/Gate_05_Separation_Thermal.md` (pending —
  see FL-003)

**This file DOES NOT define:**
- Detailed hardware specifications for any module
  (→ `Operations/Gate_04_Separation_Mechanical.md`,
  `Operations/Gate_05_Separation_Thermal.md`, etc.)
- Reduction module specification
  (→ `Operations/Gate_03_Reduction.md` — FL-002)
- Component triage station workflow detail
  (→ `Operations/Gate_02_Triage.md`)
- Energy accounting and power demand
  (→ `Operations/Energy.md`)
- Autonomous operation logic or AI trust architecture
  (→ `Architecture/Cognitive_Frameworks.md`,
  `Admin/Ethical_Constraints.md`)
- Version roadmap and exit conditions
  (→ `Admin/Trajectories.md`)
- Cross-module unknowns global index
  (→ `Unknowns.md`)
- Facility siting or area-of-operation requirements
  (→ `Architecture/Facilities.md`)
- Fabrication output specifications or wire qualification
  (→ `Architecture/Geck_forge_seed.md`, UNK-008 — ownership reassigned 2026-07-19)

---

## File Purpose

This document defines the minimal viable operational logic of the
Lazarus Forge and serves as the reference standard for shared
vocabulary across the entire repository. Terms defined or used
here carry their meaning into all other documents unless
explicitly noted otherwise. It is the intended governing document
for operational decisions and the authoritative source for
gate logic, outcome paths, and the want/need policy that
prevents both hoarding and premature destruction — but these
claims are aspirational at Exploration stage. Promotion to
Specification requires FL-001 resolution and full gate clearance
before the governing role is binding rather than directional.

The flow is intentionally conservative. Irreversibility is
delayed as long as possible. Human judgment is explicit at
every gate. Automation is optional, not assumed. The system
is designed to hold when uncertain — not to proceed.

This document is not a claim of full automation or a promise
of specific recovery rates. It is a falsifiable flow that
can be executed manually, semi-automatically, or automated
later. If this file disappeared, the repository would lose
its shared vocabulary standard and governing decision logic —
every module would be making gate decisions against different
definitions of the same terms.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Items entering the system have been safety-screened before gate logic applies — hazards, pressure, and charge assessed at Intake | Intake section — screening listed but prerequisites not defined | Medium | Intake safety screening formally specified |
| ASM-002 | Human operator is available and capable of overriding gate decisions at any point in the flow | Human/AI Oversight Gate — override assumed available | Medium | Autonomous operation validated and human override formally optional |
| ASM-003 | The Forge's current tooling inventory is known, maintained, and available as a live reference for Gate B evaluation | Gate B — "within current tooling capability" requires known tooling state | Medium | Tooling inventory specification and maintenance doctrine assigned to an owning file |
| ASM-004 | A Component Library exists and is maintained to receive and track Gate A outputs | Outcome Paths — Component Library assumed to exist as a functional system | Medium | Component Library specification assigned to an owning file |
| ASM-005 | Feedback from operational runs reaches classification rules in a timely enough cycle to improve gate decisions | Section 7 — learning assumed to close the loop | Low | Learning cycle time defined and validated against operational cadence |
| ASM-006 | Value in the primary KPI is eventually definable in measurable units — directional validity assumed until then | KPI section — explicitly Placeholder | Low | KPI definition resolved per Operations/Energy.md and operational baseline |
| ASM-007 | Gate logic applies to discrete items, not fixed assemblies. Assemblies may be disassembled — each resulting component re-enters the gate sequence independently at Gate A. Disassembly is itself a Gate C or Gate D decision on the assembly, not a bypass of sequential order | Gate logic architecture; fan/motor worked example | Medium | Parallel or non-sequential gate processing validated as superior at scale |

*ASM-005 and ASM-006 are Low confidence — both depend on operational
data that does not yet exist. ASM-003 and ASM-004 identify ownerless
dependencies that should be assigned before first operational run.
ASM-007 clarifies the scope of sequential gate logic and partially
informs FL-001 resolution.*

---

## v0 Scope and Assumptions

**Input (v0):**
- Small appliances
- Tools
- Mechanical/electromechanical assemblies
- Mixed metals with attached components

**Explicit Non-Goals (v0):**
- Fully autonomous operation
- Zero external inputs
- Net-positive energy claims without measurement
- Perfect material purity

---

## Defined Terms

**Functional** — Performs a useful role in a specific application
context. An item is functional at Gate A if it works in its
original application. An item is functional at Gate C if it
can work in a reduced application.

**Equivalent function (Gate A)** — Performing the same task as
the original in the same application context. If function is
only achievable in a different or reduced application, the item
does not pass Gate A — it routes to Gate C.

**Within tooling capability (Gate B)** — Evaluated against the
Forge's current tooling inventory, not projected future
capability. Requires a known, maintained tooling inventory —
see ASM-003.

**Contamination level** — Type and degree of contamination
sufficient to affect downstream processing or operator safety.
Relevant categories at v0:

- Chemical — heavy metals (lead, cadmium, mercury), solvents,
  coatings, flux residues. Present in consumer products often
  without visible indication. Cross-reference `Operations/Air_Scrubber.md`.
- Biological/organic — oils, fluids, biological matter,
  organic coatings that off-gas under heat or rotation
- Embedded materials — fasteners, inserts, or components
  requiring separation before reduction or purification
- Energetic — batteries, capacitors, compressed gas vessels.
  Must be identified and discharged at Intake before any
  gate logic applies
- Physical/radiological — radiation-emitting materials.
  Rare but unacceptable in any processing stream. Triggers
  immediate Human/AI Oversight Gate escalation (Oversight
  exit: **Escalate**)

*This list is not exhaustive. Unforeseen contamination
categories are expected over operational lifetime. When
a new contamination type is encountered that does not fit
existing categories, it routes to the Human/AI Oversight
Gate and a new category is logged (Oversight exit:
**Reclassify**). The system is designed
to learn from what it cannot yet classify.*

**Inert waste** — Material with no remaining functional,
structural, or material recovery value, sorted for
conventional disposal.

**Want vs. Need (policy term)** — A want becomes a need when
its absence limits a higher-priority function. This distinction
governs the Human/AI Oversight Gate and Fabrication priority
order.

**Irreversibility Levels** — Added 2026-09-08 to replace a flat
irreversible/not-irreversible split with graded consequence.
This taxonomy governs Forge_flow.md's own reversibility notes
below. It is *not yet* extended to Operations/Gate_03_Reduction.md
or any other file — that remains held (HP-001 residual scope).

| Level | Meaning |
|---|---|
| R0 | Fully reversible — no material consequence |
| R1 | Reversible with labor or reassembly |
| R2 | Recoverable but altered (e.g. calibration/tolerance drift) |
| R3 | Discrete-object identity lost (disassembly into components) |
| R4 | Material transformation — Reduction and beyond |

*R4 remains the flow's highest-consequence boundary and the*
*point past which Oversight cannot recover a discrete item —*
*that governing role is unchanged by this taxonomy, only made*
*gradable below it.*

---

## Gate Correspondence

Triage station outcomes map to these gates. See
`Operations/Gate_02_Triage.md` for the full mapping table.

| Gate | Test | Routes to |
|---|---|---|
| A | Original function in original context? | Component Library |
| B | Repairable within current tooling? | Repair & Learn |
| C | Useful in reduced/different application? | Repurpose |
| D | Is Reduction the correct residual path? | Reduction |
| Oversight | Any credible active need? | Hold or Reduction |

---

## Flow State / Transition Model

*Added 2026-09-08. This section is a structural consolidation, not new*
*doctrine — every state and transition below is already established*
*elsewhere in this document (Gate Correspondence, ASM-007, the Outcome*
*Paths, and the Human/AI Oversight Gate section). It exists so the flow*
*can be read as a state-transition system, not only as a linear*
*checklist.*

**States:** Intake → Classification → Gate A → Gate B → Gate C →
Gate D → Human/AI Oversight Gate → {Component Library, Repair & Learn,
Repurpose, Reduction, Purification} → Fabrication → Utilization →
Feedback

**Primary sequence:** Intake → Classification → Gate A → Gate B →
Gate C → Gate D → Oversight (on Gate D failure) → an Outcome Path →
Fabrication → Utilization → Feedback

**Re-entry transitions (per ASM-007):**
- Disassembly at Gate C or Gate D spawns independent components, each
  of which re-enters at **Gate A** — not a bypass of gate order, a
  restart of it per component.

**Exception transitions (per Degraded Operation & Failure Modes):**
- Jammed triage → Unknown Bulk hold (not Reduction)
- Sensor drift → tightened thresholds / increased Unknown Bulk routing
- Mid-process contamination discovery → stop, escalate to Oversight
- Stale tooling inventory → Gate B defaults to NO (routes to Gate C)
- Operator unavailable → hold pending Oversight review
- Component Library full/unmaintained → treated as Gate C items

**Oversight Gate exits (formalized 2026-09-08, HP-002 — see the*
*Human/AI Oversight Gate section for the full mapping):**
- Return to Flow — exception resolved, re-enters normal routing
- Hold — deferred with a defined review point
- Reclassify — new category logged, re-enters via that classification
- Escalate — exceeds this flow's own decision authority
- Terminate — no genuine need confirmed, Reduction proceeds

**Feedback loop:** Utilization → Feedback targets Classification
rules, repair heuristics, tolerance thresholds, and tooling
priorities — i.e., feedback alters future routing at Classification
and Gate B, not a literal re-entry of the same item.

**Terminal states:** active use, stored stock, inert waste (post-
Reduction, all prior gates failed).

---

## 1.1 Flow Invariants
<!-- STATUS: Candidate doctrine — consolidates existing scattered
principles into testable statements; not a new mechanism layer.
Pattern matches Architecture/Forge_Net.md §1.1 Network Invariants. -->

These invariants are **constraints on any future mechanism**, not
a second copy of the sections that already state them. A proposed
gate-logic change or new outcome path that violates an invariant is
out of scope for this architecture unless the invariant is amended
through ordinary review. Each statement points at the existing home
of the rule; do not invent parallel rules here.

| ID | Invariant | Mechanism home |
|----|-----------|-----------------|
| **FI-1** | **The KPI does not govern.** The KPI measures what the system does; the gates govern what the system should do. Irreversibility doctrine overrides efficiency optimization at all times. | v0 Key Performance Indicator — KPI subordination note |
| **FI-2** | **Uncertainty defaults to hold, never to irreversible action.** The system is designed to absorb uncertainty, not resolve it through Reduction or any other R4 action. | Degraded Operation & Failure Modes — standing rule |
| **FI-3** | **Gate logic applies to discrete items only.** No fixed assembly is gated as a permanent unit; disassembly is itself a Gate C or Gate D decision, and every resulting component re-enters at Gate A independently. | ASM-007; Flow State/Transition Model re-entry transitions |
| **FI-4** | **Reduction is the residual path, not the default path.** R4 is the flow's highest-consequence boundary — reached only when every higher-value path (Gates A-C) has failed. | Operational Safety Advisory; Reduction outcome path |

HP-003 (Held Proposals) proposed elevating the KPI sentence alone;
adopted 2026-09-08 as FI-1 within this broader four-invariant table
rather than in isolation, following Forge_Net.md's own precedent of
consolidating several existing scattered principles at once rather
than naming just one.

---

## 1. Intake

**Purpose:** Introduce salvage items into the system with
minimal preprocessing.

**Actions:**
- Visual inspection
- Basic safety screening (hazards, pressure, charge)
- Energetic materials — batteries, capacitors, compressed
  gas — must be identified and discharged before proceeding
- Tagging (manual or digital)

**Outputs:** Item enters Classification

---

## 2. Classification & Triage

**Purpose:** Determine the highest-value path before
irreversible action.

**Classification Attributes (v0):**
- Mechanical integrity
- Electrical continuity
- Contamination level (see Defined Terms)
- Known failure modes

Classification may be **overridden by human operator**.

---

## 3. Decision Gates (Ordered, Mandatory)

*Gate logic applies to discrete items, not fixed assemblies.
Assemblies may be disassembled at Gate C or Gate D — each
resulting component re-enters the gate sequence independently
at Gate A. Disassembly is a Gate C decision on the assembly
as a whole, not a bypass of sequential gate order. See ASM-007.*

### Gate A — Still Functional?
**Test:** Performs original function, or equivalent function
in the same application context
**If YES →** Component Library
**If NO →** Gate B

### Gate B — Repairable?

> ⚠️ **Provisional — Exploration-grade, unvalidated against real
> operation.** Unlike this file's other 2026-09-08 changes, this one
> is *new logic*, not a rename or consolidation of existing
> behavior. Before this addition, any item passing the three
> conditions below went to Repair & Learn — full stop. Now, some of
> those same items will route to Gate C instead. That is a genuine
> behavior change, and it has not been tested against a single real
> item. Treat every Secondary Test outcome as suspect until the
> first operational cycle either confirms or contradicts it.

**Primary Test (all three required):**
- Failure is localized
- Failure is accessible
- Repair is within current tooling capability (see ASM-003 and the
  live Tooling Inventory — FL-004, not yet populated)

**If any primary condition fails →** Gate C

**Secondary Test (only if primary passes):**
Is the estimated repair effort justified by at least one of:
- Recovered functional value (item returns to Component Library or
  active use)
- Learning value (failure mode is novel or high-frequency and the
  repair will improve future heuristics)
- Scarcity or strategic value (measured, not assumed)

**If YES →** Repair & Learn
**If NO →** Gate C (technically possible but not justified)

*At Exploration stage the secondary test is qualitative and
operator-judged — there is no scoring formula, no effort threshold
in minutes or hours, and no calibration data. Every secondary-test
decision must be logged with the operator's rationale, both to
build the missing data and so a future audit can catch systematic
bias (e.g. one operator's threshold differing sharply from
another's). Before Specification the secondary test must become
testable (effort bands, measured scarcity thresholds, or an
equivalent simple score) — until it is, FL-001 cannot claim Gate B
determinism regardless of how clean this wording reads. The
secondary test never routes an item directly to Reduction; Gate C
remains the next sequential step, so the irreversibility doctrine is
unaffected even if this heuristic proves wrong in practice. See also
Queue Economics in Operations/Gate_02_Triage.md for prioritization
inside the Repair & Learn queue.*

### Gate C — Graceful Downgrade Possible?
**Test:** Can the item serve a useful function in a different
or reduced application?
**If YES →** Repurpose as Lower-Precision Component
**If NO →** Gate D

*Note: Gate C tests functional downgrade potential. Gate D
tests material integrity. These are distinct tests.
Assemblies that cannot function as a whole may be disassembled
here — each component re-enters at Gate A independently.*

### Gate D — Material Recovery Viability
**Test:** Is Reduction the correct residual path for material recovery
under current Forge capability?
(i.e., all functional, repair, and repurpose paths have been exhausted,
and the only remaining viable recovery route is size-reduction followed
by Separation / Purification.)
**If YES →** Reduction
**If NO (a non-Reduction recovery path may still exist, or recovery is
genuinely impossible / prohibited) →** Human/AI Oversight Gate

*Rewritten 2026-09-08 to resolve the polarity ambiguity flagged in
HP-004. The prior compound test mixed functional exhaustion with a
negative claim about Purification recoverability, creating a circular
reading (Reduction both "no pathway remains" and the necessary first
step of the primary pathway). The new positive framing matches actual
doctrine: Reduction is the residual R4 path that feeds Separation /
Purification. Oversight remains the correct exit for true edge cases.
Renamed from "Truly Exhausted?" to "Material Recovery Viability"
earlier the same day for testability — that rename is unaffected.*

### Human/AI Oversight Gate — Exception-Resolution State

*Reframed 2026-09-08 (HP-002). This section formalizes exit states*
*that were already scattered across this document's contamination,*
*degraded-operation, and Gate D logic — no routing behavior below*
*is new. Each exit cites where its behavior already existed prior*
*to this reframe.*

The Oversight Gate is entered from multiple triggers, not only
Gate D failure: contamination discovered mid-process, radiological
or other unforeseen hazard categories, operator unavailability,
and Gate D's want/need evaluation. It resolves to one of five
named exits:

- **Return to Flow** — the exception is resolved and the item
  re-enters normal gate routing (e.g. sensor drift corrected and
  classification resumes; see Degraded Operation)
- **Hold** — deferred pending a future condition, with a defined
  review point (genuine need confirmed at Gate D; operator
  unavailable pending return; contamination pending
  characterization — see Degraded Operation)
- **Reclassify** — a new category is logged and the item re-enters
  via that classification (unforeseen contamination category — see
  Contamination Categories)
- **Escalate** — the decision exceeds this flow's own authority
  (radiological or other hazard requiring external protocol — see
  Contamination Categories)
- **Terminate** — no genuine need confirmed; Reduction proceeds
  (Gate D want/need evaluation, below)

This gate prevents both hoarding and premature destruction.

**Gate D want/need evaluation (Hold vs. Terminate exits):**
Review items that failed Gates A–D but where reduction feels
premature. Evaluate against active needs only — not
hypothetical future uses. Apply the want/need policy
(see Defined Terms).

- If a genuine need exists: **Hold** — assign with a defined review date
- If no genuine need exists: **Terminate** — Reduction proceeds

**Minimum criteria for "genuine need" (Exploration-level
heuristics — must become testable before Specification):**

A need is credible if at least one of the following applies:
- Linked to an active fabrication queue item
- Addresses a current tooling deficiency with no available
  substitute
- Replacement lead-time exceeds operational tolerance
- Component scarcity is measured, not assumed
- Failure-rate evidence suggests imminent need
- Dependency chain importance is documented

A want is not a need if:
- The justification is speculative future use
- No active queue item depends on it
- A functional substitute already exists
- The retention decision is driven by emotional value
  rather than operational necessity

*These criteria are heuristic at Exploration stage.
Operator judgment remains valid. The purpose is to make
the judgment auditable, not to remove it.*

---

## 4. Outcome Paths

### Component Library
- Catalog reusable parts
- Track provenance and test results
- Feeds Fabrication directly
- Requires maintained Component Library — see ASM-004
- *Reversibility: R0 — components remain individually recoverable*

### Repair & Learn
- Attempt repair
- Log failure mode and fix
- Update heuristics
- Outputs to Component Library or Repurpose
- *Reversibility: R2 — disassembly may affect calibration or
  tolerances — log pre-repair state*

### Repurpose (Lower Precision)
- Assign to reduced-spec use cases
- Examples: jigs, fixtures, structural members
- Feeds Fabrication

### Reduction
**R4 — point of no return for the item as a discrete object**
- Shredding, cutting, or milling
- Size reduction only (no melting yet)
- Reduction module specification owned by
  Operations/Gate_03_Reduction.md — see FL-002, UNK-007
- *Reversibility: R4 — the flow's highest-consequence boundary.*
  *Operations/Gate_03_Reduction.md still describes this step as*
  *"the only irreversible step" in its own safety doctrine (GR-005,*
  *ASM-001) — that language is intentionally untouched pending*
  *separate review; see HP-001 in Held Proposals.*

**Operations/Gate_03_Reduction.md exists and carries constraints-first
doctrine (contamination shutdown, prohibited inputs, output envelope,
dust handling, emergency shutdown).** Its output envelope has not yet
been cross-validated against the provisional feedstock envelope in
Operations/Gate_04_Separation_Mechanical.md Inputs section — that
cross-validation is FL-002's remaining scope. Until it closes:
- Do not assume feedstock homogeneity after reduction
- Do not assume automated reliability of any reduction method
- Do not assume dust, fines, or contamination are handled
  without explicit doctrine
- Contamination discovered during reduction triggers
  immediate stop and Human/AI Oversight Gate escalation
- Emergency shutdown leaves material in whatever state
  it is in — no assumption of safe intermediate states
- The provisional feedstock envelope in
  Operations/Gate_04_Separation_Mechanical.md Inputs section remains
  the best available downstream constraint until
  Operations/Gate_03_Reduction.md's output envelope is cross-validated
  against it

### Purification
- Spin Chamber or any mechanism achieving comparable
  separation output — including the Material Separation
  Gate as upstream mechanical diversion
- Pass / fail logic
- Fallback to powder or bulk stock if needed
- *Stage definition governs DS-001 terminology dispute —
  see Active Disputes and Auditor Notes*
- *Equivalence criteria defined in
  `Operations/Gate_05_Separation_Thermal.md`*

---

## 5. Fabrication / Assembly

**Inputs:** Salvaged components, purified stock,
repurposed parts

**Outputs:** Tools, fixtures, replacement components,
infrastructure for future Forge growth

Fabrication is **not terminal**.

Priority order:
1. Tools or components the Forge currently lacks
2. Infrastructure that expands Forge capability
3. Output for external use or exchange

Priority is evaluated using the want/need policy
(see Defined Terms).

---

## 6. Utilization

**Purpose:** Test real-world performance.

**Metrics Captured:** Runtime, failure modes, load
tolerance, maintenance frequency

---

## 7. Feedback & Learning

**Feedback Targets:** Classification rules, repair
heuristics, tolerance thresholds, tooling priorities

**Learning Mode (v0):** Human-readable logs, simple
rule updates, no ML required

---

## v0 Key Performance Indicator (KPI)

**Primary KPI:** Value recovered per kWh consumed

If this metric is not competitive at small scale,
scaling is invalid.

*KPI definition is Placeholder pending: (a) definition
of "value" in measurable units; (b) accounting method
for different recovery paths; (c) demand baseline from
`Operations/Energy.md`. See ASM-006.*

**KPI subordination note:**
The KPI is a efficiency metric, not a governing principle.
It is subordinate to irreversibility doctrine at all times.
A system optimizing only this metric may prematurely reduce
difficult repairs, reject rare low-energy components, or
destroy high-complexity salvage to preserve throughput
efficiency. These outcomes violate the core recovery
philosophy even if they improve the KPI score.

Irreversibility doctrine overrides efficiency optimization.
Long-tail scarcity and strategic component value may justify
low immediate energy efficiency. The KPI measures what the
system does — the gates govern what the system should do.

---

## Termination Conditions

An item exits the system only when:
- It is in active use
- It is stored as stock
- It is reduced to inert waste after all prior gates
  fail (see Defined Terms)

---

## Degraded Operation & Failure Modes

The gate system does not assume ideal conditions.
The following failure modes are expected over operational
lifetime and must not cause silent routing errors:

**Jammed triage** — Input backlog exceeds classification
capacity. Resolution: route excess to Unknown Bulk hold,
not to Reduction. Throughput pressure must never override
gate logic. Log backlog rate as diagnostic signal.

**Sensor drift** — Classification confidence degrades
without obvious cause. Resolution: tighten thresholds,
increase Unknown Bulk routing, identify and correct
sensor issue before resuming normal operation (Oversight
exit: **Return to Flow**). Mirrors
`Operations/Gate_04_Separation_Mechanical.md` degraded
mode doctrine.

**Contamination discovery mid-process** — Contamination
identified after gate routing has begun. Resolution:
stop processing, escalate to Human/AI Oversight Gate,
log new contamination category if not previously defined
(Oversight exit: **Hold**, or **Reclassify** if a new
category is logged).
Do not continue routing contaminated material downstream.

**Tooling inventory stale** — Gate B evaluations become
unreliable if tooling inventory is not maintained.
Resolution: Gate B defaults to NO (routes to Gate C)
when tooling inventory is uncertain. Conservative
routing under uncertainty. See ASM-003.

**Operator unavailable** — Human/AI Oversight Gate
requires human presence. Resolution: hold items pending
Oversight Gate review (Oversight exit: **Hold**). Do not route to Reduction in
operator absence unless automated shutdown doctrine
explicitly permits it.

**Component Library full or unmaintained** — Gate A
outputs have no reliable destination. Resolution:
treat as Gate C items until library capacity is restored.
Do not route to Reduction because the library is full.

*Degraded operation doctrine: when in doubt, hold.
The system is designed to absorb uncertainty, not
to resolve it through irreversible action.*

---

## Notes

This flow is intentionally conservative. Irreversibility
is delayed. Human judgment is explicit. Automation is
optional, not assumed.

The Defined Terms section is the most stable element
of this document — treat changes to it with extra care.
Any term redefinition propagates across every file that
inherits the definition.

**Unknown ID naming convention:**
This document uses two identifier systems — they are not
interchangeable:
- **Local sidecar IDs** (FL-001, FL-002) — module-level
  unknowns with full detail in this file's sidecar
- **Cross-module UNK-*** (UNK-007, UNK-008) — repository-level
  navigation only, indexed in `Unknowns.md`

When referencing an unknown, use the local sidecar ID as
primary. Use UNK-* only when the unknown has been formally
escalated to cross-module status in Unknowns.md.
Legacy UNK-* identifiers are preserved as aliases only.

---

## Boundary-Case Worked Examples

These examples exist to resolve FL-001 — gate logic must
produce deterministic routing, not operator-dependent
outcomes. Each example shows the correct route and why.

**Example 1 — Functional motor in non-functional assembly**
Item: Cordless drill. Housing cracked, battery unsafe,
chuck worn, but motor functional and copper windings intact.
- Gate A: Drill as a whole — fails. Cannot perform original
  function safely.
- Gate C: Drill as a whole — disassembly warranted. Motor
  is useful in reduced application. Housing and battery
  route to Gate D.
- Gate D: Housing — structural damage, no functional use,
  material recoverable. Routes to Reduction.
- Gate D: Battery — unsafe, not recoverable through
  standard purification. Routes to contamination handling.
- Gate A (re-entry): Motor — functional as a component.
  Routes to Component Library.
- Gate A (re-entry): Copper windings — functional as
  material stock. Routes to Component Library or Repurpose.
*Key principle: assemblies disassemble at Gate C.
Components re-enter independently at Gate A.*

**Example 2 — No function but recoverable material (Gate C/D boundary)**
Item: Shattered cast iron pan. No functional use in any
application. Material is cast iron — recoverable through
Purification.
- Gate A: Fails — no original function possible.
- Gate B: Fails — not repairable.
- Gate C: Fails — no useful function in reduced application.
  A shattered pan cannot serve as a jig, fixture, or
  structural member.
- Gate D: Passes — material recovery value remains.
  Cast iron routes to Reduction then Purification.
*Key principle: Gate C tests function, Gate D tests
material. An item can fail Gate C and pass Gate D.*

**Example 3 — Ambiguous Oversight Gate (want vs. need)**
Item: Vintage oscilloscope. Functional but obsolete.
No active fabrication queue item requires it. A newer
digital equivalent exists in the Component Library.
- Gates A through D: All pass technically — item is
  functional, repairable, repurposable, and material
  is recoverable.
- Human/AI Oversight Gate: Is there a genuine need?
  Apply minimum criteria — no active queue dependency,
  substitute exists, no measured scarcity, no failure
  rate evidence. Retention is a want, not a need.
- Route: Repurpose or Reduction depending on Component
  Library capacity.
*Key principle: Oversight Gate evaluates need against
active operational requirements, not hypothetical value.*

---

**Example 4 — Repairable but not worth it**
Item: Bench grinder. Motor still spins, one grinding
wheel is missing, the second is cracked, switch
intermittent. Replacement wheels and switch are
available in the Component Library; total repair
labor is estimated at 45 minutes.
- Gate A: Fails as a complete unit — original function
  is compromised (missing/cracked wheels, unreliable
  switch).
- Gate B Primary Test: Passes — the failures are
  localized, accessible, and repair is within current
  tooling capability.
- Gate B Secondary Test: Repair effort (45 min, common
  parts) is justified by recovered functional value —
  the grinder returns to active use. Passes.
- Route: Repair & Learn. The intermittent switch and
  cracked wheel become documented repair cases.
- If an operator instead judges the Secondary Test as
  NO (e.g. no active need for a grinder and no learning
  value — this failure mode is already well documented):
  routes to Gate C instead, with the operator's rationale
  logged per Gate B's Secondary Test doctrine.
*Key principle: Gate B's Primary Test is purely
technical; its Secondary Test makes the "not worth it"
judgment an explicit, logged gate decision rather than
an unlogged queue-priority opinion. This example predates
the Secondary Test's 2026-09-08 addition — updated the
same day to match; see the Provisional notice on Gate B
itself.*

---

**Example 5 — Repurpose vs. material recovery tension**
Item: Aluminum extrusion, 1.2 m long, one end crushed,
rest undamaged. Could serve as structural stock or jig
material (Gate C), or be reduced to clean aluminum
feedstock (Gate D → Reduction → Purification).
- Gate A: Fails — original function is gone.
- Gate B: Fails — crush damage is not repairable to
  original geometry within current tooling.
- Gate C: Passes — the undamaged length is immediately
  useful as lower-precision stock or fixture material.
- Route: Repurpose. The crushed end may be cut and sent
  to Reduction; the good length enters the Component
  Library as usable stock.
- If no current fabrication need exists for aluminum
  stock of that section: still route to Repurpose, or
  Oversight Hold with a defined review date — not
  immediate Reduction. Functional stock outranks pure
  material recovery while it exists.
*Key principle: Gate C functional value outranks
material recovery when both are viable. Reduction is
the residual path (see Gate D), not the preferred one.*

---

**Example 6 — Unknown or incompletely identified material**
Item: Mixed plastic-metal assembly. Housing material is
unmarked, no datasheet, no clear polymer identification;
metal inserts of unknown alloy.
- Gates A–C: Indeterminate — original function and
  reduced-application potential cannot be assessed
  without material identity.
- Gate D: Also indeterminate — an unidentified polymer
  or alloy could contaminate downstream Purification, so
  whether Reduction is the correct residual path cannot
  be answered yet.
- Route: Unknown Bulk hold (or Human/AI Oversight Gate,
  exit: Hold). Do not guess. Log the identification gap.
  Item stays held until material characterization is
  performed or, if provenance allows, returned to source.
- Only after positive identification: re-enter the full
  gate sequence from Gate A.
*Key principle: Incomplete evidence produces a hold,
never a forced gate decision. Determinism requires known
inputs, not assumed ones.*

---

**Example 7 — Incomplete evidence / conflicting operator assessments**
Item: Hydraulic pump. One operator reports the seals as
failed and the unit as scrap; a second reports the seals
serviceable and recommends Repair. No pressure test has
been performed — visual inspection only.
- Gate B: Cannot be evaluated deterministically — the
  failure state itself is disputed and unmeasured.
- Response: Escalate to Human/AI Oversight Gate (exit:
  Hold), or Unknown Bulk hold. Perform the minimal
  diagnostic (pressure test or controlled seal
  inspection) before any gate decision.
- After diagnostic: re-enter at the appropriate gate
  with the measured state.
- If diagnostic capacity does not exist: hold. Do not
  default to Reduction under uncertainty.
*Key principle: Conflicting assessments or missing
measurements produce a hold plus a diagnostic action —
never a majority vote or a forced gate outcome.*

---

## Adversarial Routing Scenarios

These scenarios test gate logic under pressure conditions.
A gate system that only works under cooperative conditions
is not a gate system — it is a suggestion.

**Scenario 1 — Throughput pressure**
Situation: Input backlog is high. Operator is tempted to
route ambiguous items directly to Reduction to clear the
queue faster.
Correct response: Route to Unknown Bulk hold. Log backlog
rate. Throughput pressure is not a gate condition.
Reduction requires gate failure, not queue management.

**Scenario 2 — Emotionally valuable item**
Situation: A family heirloom tool arrives in salvage.
Functional but outside the Forge's current needs.
Operator wants to retain it indefinitely.
Correct response: Apply want/need criteria. If no active
need exists, assign a defined review date. If review date
passes without a need emerging, route to Reduction or
return to owner if provenance allows. Emotional value
does not override gate logic — but it is a legitimate
signal to escalate to the Oversight Gate rather than
auto-routing.

**Scenario 3 — Contaminated high-value material**
Situation: A large copper component arrives with suspected
lead contamination (visible surface oxidation, unknown
provenance). High material value tempts bypass of
contamination screening.
Correct response: Route to contamination assessment before
any gate logic applies. If contamination is confirmed,
route to `Operations/Air_Scrubber.md` protocol and controlled
processing. High value does not override contamination
doctrine. The Air Scrubber exists precisely for this case.

**Scenario 4 — Partially functional assembly under scarcity**
Situation: A rare motor controller arrives. One channel
is failed, two are functional. No substitute exists in
the Component Library. Scarcity is real and measured.
Correct response: Gate C — disassemble. Functional
channels route to Component Library. Failed channel
routes to Gate D. Scarcity justifies careful disassembly
over bulk Reduction. Document scarcity evidence in
the Component Library entry.

**Scenario 5 — Operator disputes gate outcome**
Situation: Two operators disagree about whether an item
passes Gate C. One argues it has reduced-application
value; the other argues it does not.
Correct response: Escalate to Human/AI Oversight Gate.
Log the disagreement and the resolution rationale.
If the dispute reveals a genuine boundary ambiguity,
log a new boundary-case worked example. Gate disputes
are data — they feed FL-001 resolution.

---

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review | Gate A "equivalent function" left undefined | Created overlap with Gate C — same item could route to either | Gate A requires function in original application context; Gate C handles all reduced or different applications. Definitions must be mutually exclusive at every boundary | Analogous | No — definition is stable |
| May 2026 | Audit Review | Gate C and Gate D described with near-identical language | Boundary between them was ambiguous — items could satisfy both or neither | Gate C = functional downgrade test; Gate D = material integrity test. Explicitly distinct. Gate C asks can it do something useful; Gate D asks is the material itself recoverable | Analogous | No — distinction is stable |
| 2026-05-15 | Audit Review | Gate logic assumed to apply to assemblies as fixed units | Created ambiguity about disassembly — pulling a motor from a fan before reduction felt like a gate bypass | Gate logic applies to discrete items not fixed assemblies. Disassembly is a Gate C decision on the assembly — each resulting component re-enters at Gate A independently. Sequential order is preserved at the component level. See ASM-007 | Analogous | Yes — worked examples needed for complex multi-component assemblies |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | "Purification stage" terminology may cause semantic overlap with Spin_Chamber_v0.md and misrepresent the Material Separation Gate's function | Position A: Purification is correctly defined broadly — "Spin chamber or any mechanism achieving comparable separation output" — the Gate fits this definition and no rename is needed. Position B: The Gate does not purify in metallurgical terms; calling its stage Purification creates confusion about what the module does and risks semantic drift across the repository | Low | Open | Architecture/Forge_flow.md |

*DS-001 originates from ChatGPT audit of Operations/Gate_04_Separation_Mechanical.md
(2026-05-15) and is logged there as a cross-reference. Resolution
belongs here — if the Purification stage definition is revised,
Operations/Gate_04_Separation_Mechanical.md File Purpose and position statement
must be updated to match, and Unknowns.md notified.
Position A is the current standing definition. Position B requires
a terminology change with repository-wide propagation.
Recommended trigger for revisit: when a second mechanical separation
module enters scope.*

---

## Auditor Notes & Unknowns

### FL-001 — Gate logic determinism unverified at boundary cases

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | Yes — blocks promotion to Specification          |
| Owner         | Architecture/Forge_flow.md                         |
| First Logged  | May 2026                                         |
| Last Reviewed | 2026-09-08                                       |

**Description:** Whether gate logic (A→B→C→D) produces
deterministic routing for all item types at boundary cases
has not been verified.

**Why It Matters:** Non-deterministic gate logic means
identical items could route differently depending on
operator interpretation. This undermines the flow
document's role as a reliable decision standard and
creates inconsistency across forge instances.

**Resolution Path:**
- Gate Correspondence table added — partial resolution.
- Motor worked example added to Operations/Gate_02_Triage.md
  (65% torque → Gate A fail, Gate C pass) — partial
  resolution.
- Assembly disassembly clarification added 2026-05-15 —
  Gate C decision on assembly spawns independent Gate A
  evaluations per component. See ASM-007 and Lessons
  Learned entry 2026-05-15.
- Five boundary-case worked examples added 2026-05-16 —
  functional motor in broken assembly, shattered cast iron
  (Gate C/D boundary), ambiguous Oversight Gate want/need,
  adversarial throughput pressure, operator dispute
  escalation. See Boundary-Case Worked Examples section.
- Five adversarial routing scenarios added 2026-05-16 —
  throughput pressure, emotional value, contaminated
  high-value material, scarcity under partial function,
  operator dispute. See Adversarial Routing Scenarios section.
- "Genuine need" minimum criteria added to Oversight Gate
  2026-05-16 — linked fabrication queue, tooling deficiency,
  lead-time, scarcity evidence, failure-rate, dependency chain.
- Remaining: Gate C/D boundary worked example covers
  shattered cast iron — additional complex assembly examples
  may be needed before full determinism is claimed.
- 2026-09-08: Examples 4-7 added (repairable-not-worth-it,
  repurpose-vs-recovery tension, unknown material,
  incomplete/conflicting evidence) — closes four of the
  gap cells identified under HP-005. Complex
  multi-component assemblies beyond Example 1's drill case
  remain the one uncovered cell — see HP-005.
- Remaining: Adversarial scenarios cover five cases —
  real-world operation will surface new boundary conditions
  that must be logged and resolved.
- Gate D renamed "Material Recovery Viability" 2026-09-08 for
  testability, then rewritten same day (HP-004, Option A) to a
  single positive test — the compound-test polarity ambiguity
  is resolved. Routing outcomes unchanged throughout.
- Last Reviewed field corrected 2026-09-08 — had drifted stale
  against this file's own Resolution Log, which recorded
  substantive audits (2026-08-08, 2026-08-10) after the field's
  prior 2026-05-16 value.
- Payment via Specification — once all boundary cases
  have worked examples producing deterministic outcomes
  across multiple operators, move validated gate logic
  to Body as Measured.
- Cross-module reference: UNK-012 in Unknowns.md

---

### FL-002 — Reduction output envelope cross-validation pending

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Architecture/Forge_flow.md                         |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-17                                       |

**Description:** Operations/Gate_03_Reduction.md now exists and
specifies constraints-first Reduction doctrine (contamination
shutdown, prohibited inputs, output envelope, dust handling,
emergency shutdown). Its output envelope has not yet been
cross-validated against Operations/Gate_04_Separation_Mechanical.md's
provisional feedstock envelope (Inputs section).

**Why It Matters:** Reduction sits at R4, the flow's highest-
consequence boundary. It is also the upstream dependency
for the Material Separation Gate — the Gate's provisional
feedstock envelope, RPM bands, sensor calibration, and jam
risk all depend on knowing what Reduction actually produces.
An uncross-validated envelope means the Gate is still operating
against an unconfirmed input.

**Resolution Path:**
- Cross-validate Operations/Gate_03_Reduction.md's output envelope
  (max dimension, max mass, prohibited geometries, moisture and
  contamination handling) against Operations/Gate_04_Separation_Mechanical.md
  Inputs section once a Reduction method is selected.
- Until cross-validated, Operations/Gate_04_Separation_Mechanical.md's
  provisional feedstock envelope (Inputs section) stands as the
  best available constraint.
- Cross-module reference: UNK-007 in Unknowns.md,
  MG-007 in Operations/Gate_04_Separation_Mechanical.md.
- Payment via Specification — once the output envelope is
  cross-validated against Operations/Gate_04_Separation_Mechanical.md
  Inputs section.

---

### FL-003 — Self-replication architecture ownership undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                              |
| Risk          | Low                                               |
| Priority      | Minor                                             |
| Type          | Architectural / Cross-Module                      |
| Blocking      | No                                                |
| Owner         | Architecture/Forge_flow.md                          |
| First Logged  | 2026-09-08                                        |
| Last Reviewed | 2026-09-08                                        |

**Description:** `Operations/Gate_05_Separation_Thermal.md`'s Scope
Boundary points self-replication architecture and loop closure
logic to this file (jointly with Geck_forge_seed.md), but this
file's own Scope Boundary never claims that ownership and contains
no self-replication content. Found during HP-006 cross-layer
reconciliation.

**Why It Matters:** Self-replication is referenced as a downstream
goal from at least one operational file, but nothing in the
architecture layer currently owns defining what that architecture
actually is — an orphaned handoff.

---

### FL-004 — Tooling inventory (ASM-003) has no owning file

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                              |
| Risk          | Medium                                            |
| Priority      | Major                                             |
| Type          | Operational / Cross-Module                        |
| Blocking      | No (but blocks full FL-001 / Gate B determinism)  |
| Owner         | Architecture/Forge_flow.md                          |
| First Logged  | 2026-09-08                                        |
| Last Reviewed | 2026-09-08                                        |

**Description:** ASM-003's Expiry Trigger requires tooling inventory
specification and maintenance doctrine to be "assigned to an owning
file." Checked `Architecture/Components.md` as the candidate — it is
a system-component taxonomy (Critical/Useful/Bootstrap), not a live
tool list, contains no tooling-inventory content, and doesn't claim
this ownership. No file currently does. Found while reviewing a
proposal to draft `Operations/Tooling_Inventory.md` for this purpose
(see Held Proposals HP-007). **Update 2026-09-08 (second entry):**
`Operations/Tooling_Inventory.md` created (Grok-drafted from the
HP-007 skeleton, Claude-reviewed and template-corrected). Ownership
question is now answered; inventory tables remain unpopulated (see
that file's TI-001) — this entry stays Open until first population.

**Why It Matters:** Gate B's "within current tooling capability" test
cannot be fully deterministic without a real, owned, maintained
inventory to evaluate against — this is a live gap in FL-001's own
determinism claim, not just a documentation nicety.

**Resolution Path:**
- ~~Decide ownership~~ Done 2026-09-08 —
  `Operations/Tooling_Inventory.md` created.
- Once the inventory is first populated, close this entry and update
  ASM-003's Expiry Trigger.

---

### FL-005 — Gate B Secondary Test unvalidated against real operation

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                              |
| Risk          | Medium                                            |
| Priority      | Major                                             |
| Type          | Gate Logic                                        |
| Blocking      | Yes — blocks FL-001 Gate B determinism claim      |
| Owner         | Architecture/Forge_flow.md                          |
| First Logged  | 2026-09-08                                        |
| Last Reviewed | 2026-09-08                                        |

**Description:** Gate B's Secondary Test (justified-effort
evaluation, added 2026-09-08) is new gate logic, not a
documentation consolidation like this file's other 2026-09-08
changes. It has not been exercised against a single real item.
The judgment criteria (recovered value / learning value / scarcity)
are qualitative and operator-judged, with no scoring formula or
threshold yet — see the Provisional notice on Gate B itself.

**Why It Matters:** Two operators could reasonably reach different
Secondary Test outcomes for the same item, which is exactly the
non-determinism FL-001 exists to close. Adding the test closes one
documentation gap (Example 4 previously claimed no such test
existed) but opens a new determinism question that did not exist
before this pass.

**Resolution Path:**
- Log every Secondary Test decision with operator rationale from
  first use (per Gate B's own instruction).
- After a meaningful sample of real decisions, check for
  operator-to-operator divergence.
- Before Specification: convert to a testable threshold (effort
  bands, measured scarcity cutoffs, or equivalent) per Gate B's own
  provisional note.
- Cross-module reference: HP-005 in Held Proposals.
- Once an owning file exists and is first populated, update ASM-003's
  Expiry Trigger and this entry.

---

### DS-001 — Purification stage terminology (cross-reference)

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural                                    |
| Blocking      | No                                               |
| Owner         | Architecture/Forge_flow.md                         |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Whether "Purification stage" terminology
accurately represents the Material Separation Gate's
position in the flow, given that the Gate does not purify
in metallurgical terms.

**Why It Matters:** If the stage label causes semantic
drift or confusion as more mechanical separation modules
are added, repository-wide terminology propagation becomes
costly. Current standing definition is deliberately broad
and covers the Gate correctly — but the question is
deferred, not closed.

**Resolution Path:**
- Full dispute entry lives in Operations/Gate_04_Separation_Mechanical.md
  Active Disputes section.
- Resolution belongs here — if Purification stage
  definition is revised, Operations/Gate_04_Separation_Mechanical.md
  File Purpose and position statement must be updated
  to match.
- Recommended trigger for revisit: when a second
  mechanical separation module enters scope, at which
  point the stage label question becomes practically
  important.
- Discharge via Specification — once definition is
  confirmed stable or revised with repository-wide
  propagation.

---

### Resolution Log

- 2026-09-08 (eleventh pass): **HP-003 adopted as a 4-invariant Flow Invariants section.** Checked File_Template.md for an existing "Invariant" convention — none exists in the template itself — but found real precedent in `Architecture/Forge_Net.md`'s §1.1 Network Invariants (NI-1 through NI-8, Grok-drafted, consolidation-only, Candidate-doctrine status marker), so this doesn't introduce an unprecedented category. Given the choice between the original narrow scope (just the KPI sentence) and matching Forge_Net's multi-invariant consolidation, human chose the latter. Added §1.1 Flow Invariants after the Flow State/Transition Model section: FI-1 (KPI subordination, the original HP-003 target), FI-2 (uncertainty defaults to hold — from Degraded Operation's standing rule), FI-3 (discrete items only — ASM-007), FI-4 (Reduction as residual path — Operational Safety Advisory). Each points at its existing mechanism home rather than restating the rule, matching Forge_Net's own discipline. Human-directed.

- 2026-09-08 (ninth pass): **Gate B Secondary Test adopted, flagged more heavily provisional than the source proposal (Grok's Option 1).** Unlike this file's other same-day changes, this is genuine new gate logic — items that previously passed Gate B unconditionally can now route to Gate C instead, based on a qualitative "justified effort" judgment. Applied Grok's exact Option 1 wording as the base, then added a stronger Provisional/unvalidated notice per explicit human direction ("apply, but flag it more heavily as Exploration-grade/provisional"). Updated Example 4, which had asserted Gate B does NOT test cost/effort — now stale given the new Secondary Test, rewritten to walk through Primary Test then Secondary Test explicitly. Registered FL-005 (Blocking) for the test's unvalidated status, both here and Unknowns.md v5.04. HP-005 updated to note the Gate B threshold moved from "unadopted" to "adopted but provisional." Human-directed; explicitly chose the more-cautious framing over applying the source draft as-is.

- 2026-09-08 (eighth pass): **HP-005 partially complete — Examples 4-7 added.** Grok drafted the case content (bench grinder/repairable-not-worth-it, aluminum extrusion/repurpose-vs-recovery, mixed plastic-metal/unknown material, hydraulic pump/incomplete-conflicting evidence), verified and adapted before insertion: fixed an internal inconsistency in the repair-cost example (its own Key Principle said cost/effort is a secondary signal, not a Gate B test, but the body draft had briefly implied otherwise — corrected to match); added HP-002's Oversight exit tags (Hold) where relevant for consistency with the formalized exit model. Inserted as Examples 4-7 after Example 3. FL-001 Resolution Path and HP-005 updated — remaining gap is complex multi-component assemblies beyond Example 1, and an optional (unadopted) Gate B cost/effort threshold. Human-directed.

- 2026-09-08 (seventh pass): **FL-004 and HP-007 logged (not actioned).** Verified Grok's ASM-003-vs-Components.md gap finding against source: Components.md is a system-component taxonomy (Critical/Useful/Bootstrap), contains no tooling-inventory content, and doesn't claim ASM-003's ownership. Registered the gap as FL-004 (Open) here and in Unknowns.md v5.03. Logged the drafted `Operations/Tooling_Inventory.md` skeleton as HP-007 in Held Proposals — file not created. Per James: "let's get it logged, for now" — deliberately a logging-only pass. Human-directed.

- 2026-09-08 (sixth pass): **HP-004 resolved (Grok-drafted Option A, Claude-verified before applying).** Rewrote Gate D from a double-negated compound test to a single positive question: "Is Reduction the correct residual path for material recovery under current Forge capability?" Routing outcomes unchanged. Checked both side effects Grok's own writeup flagged: Gate Correspondence table row updated to match ("Is Reduction the correct residual path?"); worked Examples 1 and 2 checked against the new framing and found already consistent — neither needed edits, since both already routed material to Reduction on the basis of "material recovery value remains," not the old inverted clause. FL-001 Resolution Path updated to reflect the rewrite. Human-directed.

- 2026-09-08 (fifth pass): **HP-002 adopted.** Reviewed the Oversight Gate section against every place it's actually invoked in the document (Gate D failure, contamination mid-process, radiological hazard, operator unavailable, unforeseen contamination category) and found the five proposed exits already existed as scattered, unnamed case-specific behavior — this was a naming/consolidation pass, not new gate logic, so it did not trigger the "gate logic modified without FL-001 resolution" concern originally flagged when this was held. Formalized as Return to Flow / Hold / Reclassify / Escalate / Terminate; tagged all five scattered instances with their exit name; the two previously-binary Gate D outcomes (assign-with-review-date, Reduction) are now explicitly Hold and Terminate respectively, with identical underlying logic. No routing rule changed. Flow State/Transition Model section updated to match. Human-directed.

- 2026-09-08 (fourth pass): **HP-006 first pass complete.** Cross-checked every "DOES NOT define → see X" pointer across Forge_flow.md, Gate_02/03/04/05, Energy.md, and Forge_Net.md against the receiving file's actual DOES-define claims and body text (not just Scope Boundary summaries). Most reconciled cleanly. Found four orphaned handoffs — a term used/pointed-to on one side with zero acknowledgment on the receiving side: "Unknown Bulk" (Gate_04→Gate_02), "Class C" (Gate_04→Gate_05), battery chemistry sorting (Energy.md→Gate_02), self-replication architecture (Gate_05→Forge_flow.md, this file). Registered as TS-009, TS-010, SC-010, FL-003 in each owning file's sidecar and in Unknowns.md v5.02; added one-line stub acknowledgments to each receiving file's Scope Boundary. Did not require HP-005 first — the dependency noted when HP-006 was logged applies to gate-determinism validation, not ownership cross-checking, which turned out to be a tractable independent pass since every file already had self-declared Scope Boundary sections. Human-directed.

- 2026-09-08 (third pass): **HP-001 closed.** Grok proposed the R4-aligned rewording for Gate_03_Reduction.md's GR-005/ASM-001 safety-doctrine language. Claude verified all 8 cited passages against the live file before applying (exact matches) and found one additional un-graded occurrence, ASM-006, not in Grok's original diff — same category, included. Applied to Gate_03_Reduction.md; see that file's own 2026-09-08 Resolution Log entry for the full list. No safety intent changed. HP-001 row updated to Closed.

- 2026-09-08 (second pass): **HP-001 partially adopted.** Added
  Irreversibility Levels taxonomy (R0-R4) to Defined Terms.
  Applied to Forge_flow.md only: tagged Component Library (R0)
  and Repair & Learn (R2) reversibility notes; reworded three
  descriptive "only fully irreversible step" occurrences (Safety
  Advisory, Reduction outcome path, FL-002 Why It Matters) to R4
  framing. Deliberately did NOT touch Operations/Gate_03_Reduction.md
  — GR-005 and ASM-001 there anchor human-presence safety
  requirements to the un-graded phrase, and that's a safety-doctrine
  edit requiring separate explicit review, not a vocabulary
  extension. HP-001 row updated to reflect partial status.

- 2026-09-08: **Refinement pass on ChatGPT proposal (Claude-verified
  subset only).** Added Flow State/Transition Model section —
  pure consolidation of existing states/transitions, no new logic.
  Gate D renamed "Truly Exhausted?" → "Material Recovery Viability"
  for testability; original routing polarity preserved exactly;
  a latent test-polarity ambiguity was noticed and logged (not
  fixed) as HP-004. FL-001 sidecar Last Reviewed corrected from
  stale 2026-05-16 to 2026-09-08 to match actual Resolution Log
  activity. Six other ChatGPT-proposed items (irreversibility
  levels R0-R4, Oversight multi-exit reframe, KPI-as-Flow-Invariant,
  Gate D polarity fix, FL-001 boundary matrix, cross-layer
  reconciliation pass) logged in new Held Proposals section below —
  not adopted, not started. Human-directed; ChatGPT's claims
  independently checked against source before any action (one
  overreach found: "contamination-handling actions could presumably
  alter material condition" was unsupported speculation, excluded
  from rationale).

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **2** = FL-001, FL-002, matches local +
  `Unknowns.md`. (2) FL-001 correctly **Blocking Yes** (blocks promotion to
  Specification — Epistemic/Promo style, field already accurate). (3) FL-002
  Open/Major, Blocking No — Reduction module ownership is Gate_03, not a
  start-interlock here. (4) No FL-* closed. Human-directed.

- 2026-08-08: **Two Scope Boundary corrections, both surfaced by
  `Architecture/Arc_Scope_Map.md` (2026-08-08 folder-scope-map build):**
  (1) the UNK-008 fabrication/wire-qualification reference still said
  "no owner assigned" — stale since 2026-07-19, when ownership moved to
  `Architecture/Geck_forge_seed.md`; this session's own 2026-08-06
  Feedstock Self-Sufficiency patch had already built doctrine on that
  ownership. Corrected to point at the real owner. (2) the shared-
  vocabulary DOES bullet claimed sole reference-standard status without
  acknowledging `Admin/Canonical_Terms.md` exists — `Canonical_Terms.md`
  already correctly deferred to this file from its own side, so nothing
  was actually in conflict, just asymmetrically documented. Added a
  one-sentence reciprocal acknowledgment. Neither correction changes this
  file's actual authority or scope — both are documentation catching up
  to a state that was already true. One of the oldest files in the
  repository (RS-002 dates to 2026-06-11); worth noting that age alone
  is exactly why a stale cross-reference like the UNK-008 one can sit
  unnoticed this long — the file predates the ownership reassignment it
  was still describing. Human-directed.

- 2026-06-11: RS-002 resolved — `Forge_Flow.md` casing outlier corrected to
  `Forge_flow.md` in Archive/Rename_Registry.md. Canonical filename confirmed
  as `Forge_flow.md` throughout repository.
- 2026-06-06: Reference corrections pass — Navigation Anchors block added;
  Verification Ref corrected to Admin/Verification_Gates.md; all stale
  filenames updated per Rename Registry (Spin_Chamber_v0.md,
  Material_Separation_Gate_v0.md, Component_Triage_System.md, energy_v0.md,
  Trajectories_LF.md, Unknowns_LF.md, Air_Scrubber_v0.md, geck_forge_seed.md,
  Reduction_v0.md, Lazarus_forge_v0_flow.md); UNK-006 facility siting reference
  updated to Architecture/Facilities.md. Content unchanged.
  requires original application context. Gate C/D boundary
  clarified — functional vs. material integrity tests.
  Defined Terms section added. Reversibility notes added
  per outcome path. KPI labeled Placeholder. Gate
  Correspondence table added.
- May 2026: FL-001 — Motor worked example added to
  Operations/Gate_02_Triage.md (65% torque → Gate A fail,
  Gate C pass). Partial resolution — boundary cases remain.
- 2026-05-15: FL-001 — Assembly disassembly clarification
  added. Gate logic applies to discrete items not fixed
  assemblies. Disassembly is a Gate C decision on the
  assembly — components re-enter at Gate A independently.
  Sequential order preserved at component level. See
  ASM-007 and Lessons Learned entry 2026-05-15. Status
  remains In Progress — Gate C/D boundary worked example
  and Oversight Gate edge cases still needed.
- 2026-05-15: FL-001 — Reformatted from prose to structured
  sidecar table format. Content preserved, provenance
  dates maintained.
- 2026-05-15: FL-002 — New entry. Reduction module
  unassigned. Upstream dependency for Material Separation
  Gate identified and indexed. Cross-referenced UNK-007
  in Unknowns.md.
- 2026-05-15: DS-001 — New reference entry. Purification
  stage terminology dispute logged. Full entry in
  Operations/Gate_04_Separation_Mechanical.md Active Disputes. Owner
  confirmed as this file. Resolution deferred until second
  mechanical separation module enters scope.
- 2026-05-16: FL-001 — Five boundary-case worked examples
  added. Five adversarial routing scenarios added. Genuine
  need minimum criteria added to Oversight Gate. KPI
  subordination note added. Degraded operation subsection
  added. Reduction under-specification explicitly stated.
  Governing language softened in File Purpose. Unknown ID
  naming convention documented. Status remains In Progress —
  additional boundary cases expected from operational runs.
  Last Reviewed updated to 2026-05-16.

---

## Held Proposals (Not Committed)

*Ideas worth preserving but not yet scoped or started — distinct*
*from Auditor Notes & Unknowns (active, blocking or trackable gaps)*
*and from Abandoned Paths (considered and rejected). A Held entry is*
*neither. Promote to a numbered Unknown (FL-*) when someone commits*
*to scoping it; move to Abandoned Paths if reconsidered and rejected.*

| ID | Proposal | Why Held | Logged |
|----|----------|----------|--------|
| HP-001 | ~~Irreversibility Levels taxonomy (R0-R4)~~ **Fully adopted 2026-09-08.** Taxonomy in Defined Terms; applied throughout Forge_flow.md (Component Library R0, Repair & Learn R2, three descriptive occurrences reworded to R4). Gate_03_Reduction.md's GR-005/ASM-001 safety-doctrine language also aligned to R4 (Grok-proposed, Claude-verified against source before applying; one additional occurrence, ASM-006, found and included). No safety intent changed — see Gate_03_Reduction.md Resolution Log 2026-09-08 entry | Closed | 2026-09-08 |
| HP-002 | ~~Reframe Human/AI Oversight Gate as a formal multi-exit exception-state~~ **Adopted 2026-09-08.** Found the five exits weren't new — they were already scattered as specific-case behavior (sensor drift, contamination mid-process, radiological escalation, operator unavailable, Gate D want/need) with no common naming. Formalized as Return to Flow / Hold / Reclassify / Escalate / Terminate; each scattered instance tagged with its exit name; no routing rule changed | Was a genuine consolidation, not new logic — did not require the caution originally flagged | 2026-09-08 |
| HP-003 | ~~Elevate the KPI-subordination sentence to a named "Flow Invariant" category~~ **Adopted 2026-09-08 as part of a 4-invariant Flow Invariants section (§1.1)**, matching real repo precedent found in Architecture/Forge_Net.md's Network Invariants (NI-1-8) — same consolidation-only pattern, same Candidate-doctrine status marker. Scope expanded from the single KPI sentence to include three other candidate rules already stated elsewhere (uncertainty-defaults-to-hold, discrete-items-only, Reduction-as-residual-path), per explicit human direction to match Forge_Net's multi-invariant pattern rather than adopt just one | Was flagged as needing a File_Template.md convention check before use — checked: no "Invariant" concept exists in the template itself, but real precedent exists elsewhere in the repo (Forge_Net.md), so this doesn't introduce an unprecedented category | 2026-09-08 |
| HP-004 | ~~Gate D's compound test reads ambiguous~~ **Resolved 2026-09-08 (Option A rewrite).** Rewrote as a single positive question ("Is Reduction the correct residual path?") instead of the double-negated compound test. Routing outcomes unchanged — same items still route the same places — only the test's phrasing changed. Gate Correspondence table row aligned to match; worked Examples 1 and 2 checked and already consistent with the new framing, no edit needed there | Was flagged as needing FL-001 treatment since it's a logic-adjacent change — treated with that care: verified against Gate Correspondence table and both existing worked examples before closing, not a silent edit | 2026-09-08 |
| HP-005 | ~~FL-001 boundary-determinism matrix~~ **Partially complete 2026-09-08.** Examples 4-7 added, closing repairable-not-worth-it, repurpose-vs-recovery, unknown material, and incomplete/conflicting evidence. Remaining gap: complex multi-component assemblies beyond Example 1's drill case — flagged in Lessons Learned as still needed. **Update, same day:** the Gate B cost/effort threshold noted here as "optional/unadopted" was adopted a few passes later as a Secondary Test — see Gate B section's Provisional notice and the tenth-pass Resolution Log entry. Example 4 updated to match | Residual scope is now narrower still — complex assemblies is the one clearly-open item; Gate B's new Secondary Test is adopted but explicitly flagged Provisional/unvalidated, not closed | 2026-09-08 |
| HP-006 | ~~Cross-layer reconciliation pass~~ **First pass complete 2026-09-08.** Cross-checked every Scope Boundary pointer across Forge_flow.md, Gate_02/03/04/05, Energy.md, Forge_Net.md — reconciled cleanly overall (including good triangulation on shared owners like Energy.md/Facilities.md). Found four orphaned handoffs, spun off as new Unknowns: TS-009, TS-010, SC-010, FL-003 (see Unknowns.md v5.02). Did not require HP-005/FL-001 closure first — ownership cross-checking was independent of gate-determinism validation | Closed as a pass; residual work now lives in the four spun-off Unknowns, not here | 2026-09-08 |
| HP-007 | ~~Create `Operations/Tooling_Inventory.md`~~ **Done 2026-09-08.** Grok created the file from the drafted skeleton; Claude reviewed it (clean diff against the rest of the repo — only this one new file), found and fixed two File_Template.md gaps (missing Lessons Learned and Active Disputes sections, both required even when empty), added the Components.md cross-reference stub the original draft had prepared but not applied, updated FL-004 to reflect the file's existence, and mirrored TI-001 into Unknowns.md. Inventory tables remain unpopulated — see TI-001 in that file, which stays open until first physical count | Closed as a pass; residual work (first physical inventory, owner assignment) lives in TI-001, not here | 2026-09-08 |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| May 2026 | Gate A and Gate C defined with overlapping language | Identical items could route to either gate depending on interpretation — non-deterministic routing at the most common boundary case. Resolved by requiring Gate A to test original application context exclusively; Gate C handles all reduced or different applications | No — boundary is stable |
| May 2026 | Gate C and Gate D described with near-identical language | Boundary ambiguity between functional downgrade and material integrity tests. Items could satisfy both or neither. Resolved by making the tests explicitly distinct — Gate C asks can it do something useful; Gate D asks is the material itself recoverable | No — distinction is stable |
| May 2026 | Fully autonomous operation as a v0 goal | Automation is valid but not assumed at v0. Human judgment is explicit at every gate. Removing the autonomy assumption makes the flow executable manually from day one — a stronger bootstrap position | Reconsider at v3 when autonomous operation enters scope per Admin/Trajectories.md |
| May 2026 | Net-positive energy claims without measurement | Claiming net-positive economics before measurement is a Magic Energy fallacy. All energy claims labeled Placeholder until Operations/Energy.md baseline is established | No — measurement requirement is permanent doctrine |
| 2026-05-15 | Contamination defined as a closed fixed list | A fixed list creates a false sense of completeness — unforeseen contamination types proceed through gate logic without a defined response. Replaced with an open learning system: unknown contamination routes to Human/AI Oversight Gate and a new category is logged | No — open learning system is the correct architecture |
| 2026-05-15 | Gate logic applied to assemblies as fixed units | Created ambiguity about disassembly before reduction. Resolved by clarifying that gate logic applies to discrete items — assemblies may be disassembled at Gate C or D, with components re-entering at Gate A independently | No — component-level gate logic is stable |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of this file.
All canonical drift indicators from File_Template.md apply.
The following are additional local triggers specific to the
Lazarus Forge operational flow document:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Any module redefines a term from the Defined Terms section without updating this file | This document is the repository vocabulary standard — unauthorized redefinition causes silent semantic drift across all files that inherit the term |
| Purification stage definition revised without DS-001 resolution and repository-wide propagation | DS-001 is the active terminology dispute — any change here must update Operations/Gate_04_Separation_Mechanical.md, Unknowns.md, and any other file referencing the stage |
| Gate logic modified without FL-001 resolution | FL-001 is In Progress — gate changes before boundary cases are resolved risk introducing new non-determinism |
| Reduction module specified without FL-002 closure and cross-validation against Operations/Gate_04_Separation_Mechanical.md Inputs section | FL-002 and UNK-007 must resolve together — a Reduction spec that doesn't match the Gate's provisional feedstock envelope creates a hidden dependency failure |
| Human/AI Oversight Gate removed or made optional | The Oversight Gate is the system's primary safeguard against premature irreversible action — removal requires explicit human authorization and full audit cycle |
| Contamination category list revised without open learning system clause preserved | The open learning system clause is the doctrine that handles unforeseen contamination — removing it closes the list and creates blind spots |
| Want/need policy definition changed without downstream file review | Want/need policy governs Fabrication priority and Oversight Gate decisions — changes propagate to Operations/Gate_02_Triage.md and Architecture/Geck_forge_seed.md at minimum |
| KPI definition promoted from Placeholder without Operations/Energy.md baseline established | KPI is explicitly Placeholder pending measurable value definition and energy accounting — premature promotion is a confidence without basis violation |
| ASM-007 assembly disassembly clarification removed from body without Lessons Learned update | The clarification resolves a real ambiguity — silent removal would reopen the gate logic overlap that was deliberately closed |
| Gate sequence made non-sequential or parallel without full audit cycle | Sequential gate order is the core architectural assumption — parallel processing changes the entire decision logic and must be treated as a major version change |

### Canonical Drift Triggers

*All mandatory re-audit conditions from File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*
