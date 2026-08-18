# Lazarus Forge — v0 Operational Flow

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> This document governs decision logic that leads to irreversible
> actions. Reduction is the only fully irreversible step in the
> Forge flow — once an item is shredded or milled, it cannot be
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
| Last Audit       | 2026-08-08 (Scope Boundary corrections — UNK-008 stale reference, vocabulary asymmetry); prior: 2026-06-11 |
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
  immediate Human/AI Oversight Gate escalation

*This list is not exhaustive. Unforeseen contamination
categories are expected over operational lifetime. When
a new contamination type is encountered that does not fit
existing categories, it routes to the Human/AI Oversight
Gate and a new category is logged. The system is designed
to learn from what it cannot yet classify.*

**Inert waste** — Material with no remaining functional,
structural, or material recovery value, sorted for
conventional disposal.

**Want vs. Need (policy term)** — A want becomes a need when
its absence limits a higher-priority function. This distinction
governs the Human/AI Oversight Gate and Fabrication priority
order.

---

## Gate Correspondence

Triage station outcomes map to these gates. See
`Operations/Gate_02_Triage.md` for the full mapping table.

| Gate | Test | Routes to |
|---|---|---|
| A | Original function in original context? | Component Library |
| B | Repairable within current tooling? | Repair & Learn |
| C | Useful in reduced/different application? | Repurpose |
| D | Material recovery value remaining? | Reduction |
| Oversight | Any credible active need? | Hold or Reduction |

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
**Test:** Failure is localized, accessible, and within current
tooling capability — see ASM-003
**If YES →** Repair & Learn
**If NO →** Gate C

### Gate C — Graceful Downgrade Possible?
**Test:** Can the item serve a useful function in a different
or reduced application?
**If YES →** Repurpose as Lower-Precision Component
**If NO →** Gate D

*Note: Gate C tests functional downgrade potential. Gate D
tests material integrity. These are distinct tests.
Assemblies that cannot function as a whole may be disassembled
here — each component re-enters at Gate A independently.*

### Gate D — Truly Exhausted?
**Test:** Structural, chemical, or thermal damage prevents
any functional use AND material is not recoverable through
Purification
**If YES →** Reduction
**If NO →** Human/AI Oversight Gate

### Human/AI Oversight Gate
Review items that failed Gates A–D but where reduction feels
premature. Evaluate against active needs only — not
hypothetical future uses. Apply the want/need policy
(see Defined Terms).

- If a genuine need exists: assign with a defined review date
- If no genuine need exists: Reduction proceeds

This gate prevents both hoarding and premature destruction.

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
- *Reversibility: components remain individually recoverable*

### Repair & Learn
- Attempt repair
- Log failure mode and fix
- Update heuristics
- Outputs to Component Library or Repurpose
- *Reversibility: disassembly may affect calibration or
  tolerances — log pre-repair state*

### Repurpose (Lower Precision)
- Assign to reduced-spec use cases
- Examples: jigs, fixtures, structural members
- Feeds Fabrication

### Reduction
**Irreversible step — point of no return for the item as
a discrete object**
- Shredding, cutting, or milling
- Size reduction only (no melting yet)
- Reduction module specification owned by
  Operations/Gate_03_Reduction.md — see FL-002, UNK-007
- *This is the only fully irreversible step in the flow*

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
sensor issue before resuming normal operation. Mirrors
`Operations/Gate_04_Separation_Mechanical.md` degraded
mode doctrine.

**Contamination discovery mid-process** — Contamination
identified after gate routing has begun. Resolution:
stop processing, escalate to Human/AI Oversight Gate,
log new contamination category if not previously defined.
Do not continue routing contaminated material downstream.

**Tooling inventory stale** — Gate B evaluations become
unreliable if tooling inventory is not maintained.
Resolution: Gate B defaults to NO (routes to Gate C)
when tooling inventory is uncertain. Conservative
routing under uncertainty. See ASM-003.

**Operator unavailable** — Human/AI Oversight Gate
requires human presence. Resolution: hold items pending
Oversight Gate review. Do not route to Reduction in
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
| Last Reviewed | 2026-05-16                                       |

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
- Remaining: Adversarial scenarios cover five cases —
  real-world operation will surface new boundary conditions
  that must be logged and resolved.
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

**Why It Matters:** Reduction is the only fully irreversible
step in the Forge flow. It is also the upstream dependency
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
