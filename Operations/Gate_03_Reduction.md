# Gate_03_Reduction

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Gate_03_Reduction is the only fully irreversible step
> in the Lazarus Forge operational flow. Once an item
> enters Reduction, it cannot be recovered as a discrete
> object. Three conditions are hard prerequisites before
> Reduction begins: the Air Scrubber must be operational
> and verified, a human operator must be present, and no
> energetic materials may remain in the item. Contamination
> discovered during Reduction triggers immediate shutdown —
> there is no safe way to continue. When in doubt, stop.
> The cost of a stopped run is always recoverable. The
> cost of a misrouted item is not.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-15; revised 2026-06-08                                      |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Highest Risk reflects current unresolved upstream gaps —
FL-001 gate logic determinism, GI-002 energetic discharge,
and GI-003 augmented detection are all unresolved at v0.
This label should be reviewed after first operational cycle
and Gate_01 augmented detection is validated. See Drift
Indicators.*

---

## Scope Boundary

**This file DOES define:**
- Reduction doctrine — when Reduction is permitted
  and what prerequisites must be met
- Output envelope — what reduced material looks like
  and what constraints apply to downstream processing
- Prohibited inputs — what must be caught upstream
  before reaching Reduction
- Method selection doctrine — shredding, cutting,
  milling, and their appropriate use cases
- Contamination discovery protocol — what happens
  when hazardous material is found during Reduction
- Dust, fines, and particulate handling doctrine
- Emergency shutdown doctrine and safe states
- Handoff to Gate_04_Separation_Mechanical.md
  as primary downstream recipient
- Integration with Operations/Air_Scrubber.md
  for particulate and exhaust handling

**This file DOES NOT define:**
- Gate logic that routes items to Reduction
  (Architecture/Forge_flow.md Gates A through D)
- Upstream hazard screening and energetic discharge
  (Operations/Gate_01_Intake.md — GI-002)
- Specific machine selection, manufacturer, or
  procurement (not yet assigned — GR-002)
- Dust collection hardware specification
  (Operations/Air_Scrubber.md)
- Purification processing of Reduction output
  (Operations/Gate_04_Separation_Mechanical.md,
  Operations/Gate_05_Separation_Thermal.md)
- Energy accounting for Reduction operation
  (Operations/Energy.md)
- Facility siting, clearance, and noise requirements
  (`Architecture/Facilities.md` — FA-001)
- Biological or chemical waste disposal beyond
  containment doctrine (not yet assigned — GR-003)

---

## File Purpose

Gate_03_Reduction is the only fully irreversible step
in the Lazarus Forge operational flow. It receives
items that have failed all recovery gates — functional
use, repair, repurpose, and material recovery through
purification — and reduces them to feedstock through
shredding, cutting, or milling. Once an item enters
Reduction, it cannot be recovered as a discrete object.
This irreversibility is the defining characteristic of
this gate and governs every design decision within it.

Reduction is not a failure state. It is the correct
outcome for items that have genuinely exhausted all
recovery paths. Premature Reduction — routing items
here before gates A through D are properly applied —
is the failure. The gate itself is neutral. The
doctrine governing when it is invoked is not.

The primary outputs of Reduction are sized feedstock
for Gate_04_Separation_Mechanical.md and ultimately
Gate_05_Separation_Thermal.md. The output envelope —
particle size, mass range, prohibited geometries,
moisture and contamination state — directly determines
what Gate_04 can do with the material. A poorly
specified Reduction output is a poorly specified
Gate_04 input.

At v0, Reduction is under-specified by design.
The doctrine of what Reduction must not do is clearer
than what it should do — do not assume feedstock
homogeneity, do not assume automation reliability,
do not proceed when contamination is discovered, do
not operate without Air Scrubber verification. These
constraints are binding now. The positive specification
— method selection, machine parameters, output
envelope — follows operational experience.

If this file disappeared, the repository would have
no governing doctrine for its only irreversible step.
Items routed to Reduction would be processed without
safety prerequisites, without contamination protocols,
and without a defined output envelope for downstream
modules to rely on.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Items reaching Reduction have genuinely failed all prior gates — gate logic is sufficiently deterministic to be trusted at the point of irreversibility | Forge_flow.md gate sequence; FL-001 In Progress | Low | FL-001 resolved — gate logic determinism validated across all boundary cases |
| ASM-002 | Upstream hazard screening at Gate_01_Intake caught all energetic and chemical hazards before items reach Reduction | GI-002 and GI-003 prerequisite doctrine; Intake screening effectiveness | Low | GI-002 and GI-003 resolved and validated — augmented detection confirmed reliable |
| ASM-003 | The Air Scrubber is operational and verified before Reduction begins — particulate and exhaust are contained | Air_Scrubber.md doctrine — "if the scrubber cannot verify safe operation, the Forge does not run" | Medium | Air Scrubber verification integrated into Reduction startup sequence |
| ASM-004 | Reduced output particle size and geometry are controllable enough to remain within Gate_04_Separation_Mechanical.md provisional input envelope | Output envelope dependency — method not yet selected, control not yet validated | Low | Reduction method selected and output envelope validated against Gate_04 inputs |
| ASM-005 | Dust and fines generated during Reduction are capturable by available containment infrastructure — particulate does not escape the processing environment | Particulate handling doctrine; Air Scrubber integration | Low | First operational run characterizes actual particulate generation rate and containment effectiveness |
| ASM-006 | Human operator is present during all Reduction operations at v0 — automated shutdown cannot substitute for human judgment at the point of no return | v0 human-judgment primary doctrine | Medium | Automated Reduction with validated safety interlocks demonstrated and approved per GR-005 |
| ASM-007 | Contamination discovered during Reduction is recognizable as contamination — operators can identify when to stop processing | Contamination discovery protocol; assumes detectable indicators exist | Low | First operational cycle characterizes what contamination discovery actually looks like in practice |

*ASM-001 and ASM-002 are the most consequential —
gate logic determinism and upstream hazard screening
are both unresolved at v0. Together they represent
the risk that a misrouted or inadequately screened
item reaches the only irreversible step in the system.
Both resolve through FL-001 and GI-002/GI-003
respectively. Until they do, human presence (ASM-006)
and Air Scrubber verification (ASM-003) are the
primary compensating controls. Highest Risk label
should be reviewed after first operational cycle
and Gate_01 augmented detection is validated —
see Drift Indicators.*

---

## 1. Reduction Doctrine

Reduction is permitted only when all of the following
are true:

1. The item has passed through Gates A, B, C, and D
   in sequence and failed all four — or has been
   explicitly routed by the Human/AI Oversight Gate
2. The Air Scrubber is operational and has verified
   safe operating conditions — see ASM-003
3. A human operator is present — see ASM-006
4. No energetic materials remain in the item —
   discharged or removed at Gate_01_Intake per GI-002
5. No active contamination discovery is in progress —
   see Section 5

If any condition is not met, Reduction does not begin.
A hold is not a failure. A hold is the correct response
to an unmet prerequisite.

**Reduction is never:**
- A throughput management tool — backlogs do not
  justify routing items to Reduction prematurely
- A default for items that are difficult to classify —
  difficulty routes to Human/AI Oversight Gate,
  not Reduction
- A response to storage constraints — full Component
  Library or holding areas route to Oversight Gate,
  not Reduction
- Reversible — once begun, the item cannot be
  recovered as a discrete object

*The gate is neutral. The doctrine governing when
it is invoked is not.*

---

## 2. Prohibited Inputs

The following must be removed, discharged, or resolved
before any item enters Reduction. Discovery of a
prohibited input during Reduction triggers immediate
shutdown per Section 5.

| Prohibited Input | Risk | Resolution Path |
|---|---|---|
| Undischarged energetic materials — batteries, capacitors, compressed gas | Fire, explosion, projectile | Discharge at Gate_01_Intake per GI-002 before item enters gate flow |
| Active chemical contamination — leaking solvents, fuming materials | Operator health, equipment fouling, exhaust contamination | Isolate and hold at Gate_01_Intake. Route to specialist handling per GR-003 |
| Radiological materials | Operator health, long-term contamination | Isolate immediately. Do not attempt Reduction. Route to specialist handling |
| Biological contamination beyond surface soiling | Operator health, equipment contamination | Isolate and hold. Route to specialist handling per GR-003 |
| Items with unknown contamination status | Any of the above | Do not route to Reduction. Return to Gate_01_Intake for screening |
| Pressurized vessels — even apparently empty | Residual pressure, projectile | Verify depressurization before Reduction. When in doubt, do not reduce |

*This list reflects known prohibited categories at v0.
New categories discovered during operation are logged
and added. The open learning system doctrine from
Architecture/Forge_flow.md applies here — unknown
contamination routes to hold, not to Reduction.*

---

## 3. Method Selection

Reduction method is not yet specified — see GR-002.
The following doctrine governs method selection when
a method is chosen:

**Method categories and appropriate use:**

| Method | Best For | Avoid When |
|---|---|---|
| Cutting — saw, shear, guillotine | Large structural sections, predictable geometry, controlled sizing | Unknown internal structure, pressurized items, brittle materials that shatter unpredictably |
| Shredding — rotary shredder | Mixed small items, bulk volume reduction, irregular geometry | Items with long flexible elements (wire, cable, fabric) that tangle rotors, undischarged energetics |
| Milling — ball mill, hammer mill | Brittle materials, further size reduction of pre-cut stock | Ductile metals that deform rather than fracture, items with unknown composition |

**Method selection doctrine:**
- Match method to material class — do not apply
  a single method to all feedstock regardless of
  composition
- Conservative over aggressive — if uncertain,
  choose the method that produces less catastrophic
  failure modes
- Operator override — operator may refuse to apply
  a method to a specific item without justification
  required. Safety judgment is always valid.
- Method selection feeds back to output envelope —
  different methods produce different particle
  distributions. See Section 4.
- Standardized tooling preferred — select cutting
  and shredding equipment from standard commercial
  stock where possible to support inter-forge
  parts sharing doctrine.

*(Placeholder — specific method selected during
first operational cycle based on available equipment
and feedstock characterization. See GR-002)*

---

## 4. Output Envelope

The Reduction output envelope defines what
Gate_04_Separation_Mechanical.md receives as input.
Until Reduction method is selected and validated,
the output envelope is defined by Gate_04's
provisional input constraints — working backward
from what downstream can accept.

**Provisional v0 output constraints
(Placeholder — cross-reference Gate_04 inputs):**

| Parameter | Provisional Constraint | Basis |
|---|---|---|
| Max particle dimension | ~50mm | Gate_04 provisional input — drum geometry dependent |
| Max particle mass | ~500g | Gate_04 provisional input — rotor balance dependent |
| Prohibited output geometries | Long thin rods >200mm, wire coils, flexible sheet >200mm | Gate_04 entanglement and jam risk |
| Moisture state | Dry or surface-damp only | Gate_04 sensor and bearing risk |
| Contamination state | No free liquid, no active fuming | Gate_04 sensor fouling risk |

**Output envelope doctrine:**
- Reduction is not complete until output is within
  the provisional envelope — oversized or prohibited
  geometry output requires secondary processing
  before handoff to Gate_04
- Output that cannot be brought within envelope
  routes to Unknown Bulk hold, not to Gate_04
- Output envelope must be cross-validated with
  Gate_04_Separation_Mechanical.md when Reduction
  method is selected — provisional constraints
  are placeholders, not guarantees
- Cross-reference: Operations/
  Gate_04_Separation_Mechanical.md Inputs section,
  GR-001

---

## 5. Contamination Discovery Protocol

Contamination discovered during Reduction triggers
an immediate stop. There is no safe way to continue
Reduction of a contaminated item — the contamination
will be distributed through the output, the equipment,
and the exhaust stream.

**Contamination discovery sequence:**
1. Stop Reduction immediately — power off, allow
   moving parts to coast to stop
2. Do not open enclosure until rotation and movement
   have fully stopped
3. Isolate the item and any output already produced
   — treat all output as potentially contaminated
   until assessed
4. Ventilate if chemical contamination suspected —
   Air Scrubber must remain operational during
   ventilation
5. Log the discovery — what was found, at what
   point in processing, what the item was
6. Escalate to Human/AI Oversight Gate — do not
   make disposal decisions without human review
7. Equipment inspection before restart — confirm
   no contamination remains in the processing
   chamber, blades, or exhaust path
8. Do not restart until inspection confirms clean
   equipment and replacement item is confirmed
   free of contamination

**Contamination log minimum content:**
- Item identifier from Gate_01_Intake record
- Contamination type if identifiable
- Point of discovery in processing sequence
- Output produced before discovery — quantity
  and disposition
- Equipment inspection outcome
- Resolution path taken

*Every contamination discovery is a network
contribution — log and contribute to
Architecture/Forge_Net.md reference database.
The next forge to encounter the same item
benefits from this forge's experience.*

---

## 6. Dust, Fines, and Particulate

Reduction generates dust, fines, and particulate
as an inherent byproduct. These are not waste —
they are a hazard, a potential feedstock, and a
diagnostic signal.

**Hazard:**
- Conductive metal dust creates electrical
  shorting risk for sensors and electronics
- Fine particulate is a respiratory hazard —
  operator PPE required during and after Reduction
- Combustible metal dusts (aluminum, magnesium)
  create explosion risk at sufficient concentration
- Particulate that escapes the processing
  environment contaminates downstream equipment

**Doctrine:**
- Air Scrubber must be operational before
  Reduction begins — particulate capture is
  not optional. Cross-reference:
  Operations/Air_Scrubber.md
- Processing enclosure must be sealed during
  Reduction — no open-air Reduction at v0
- Operator PPE: respiratory protection, eye
  protection minimum during and immediately
  after Reduction
- Accumulated fines are collected and classified:
  - Metal fines → potential feedstock for
    Gate_05_Separation_Thermal.md
  - Mixed or contaminated fines → Unknown Bulk,
    route to triage
  - Combustible metal fines → handle per
    specialist protocol, do not accumulate

**Particulate generation rate as diagnostic:**
Unusual dust volume or composition is a signal —
it may indicate unexpected material in the
feedstock, equipment wear, or incomplete upstream
screening. Log and investigate before continuing.
*(Placeholder — baseline particulate generation
rate established during first operational cycle.
See GR-004)*

---

## 7. Emergency Shutdown

Emergency shutdown stops Reduction immediately
regardless of processing state. The material is
left in whatever condition it is in — there is
no safe intermediate state to target.

**Emergency shutdown triggers:**

| Trigger | Response |
|---|---|
| Contamination discovery | Stop immediately — see Section 5 |
| Unusual sound, vibration, or smell | Stop immediately — do not investigate while running |
| Equipment distress — smoke, sparks, unusual heat | Stop immediately, evacuate area, do not re-enter until safe |
| Operator calls stop | Stop immediately — no justification required |
| Air Scrubber fault or shutdown | Stop Reduction — do not continue without scrubber |
| Power loss | Equipment coasts to stop — do not attempt restart until cause identified |

**Post-shutdown doctrine:**
- Do not open enclosure until all movement has
  fully stopped
- Do not re-enter processing area until air quality
  is confirmed safe — Air Scrubber verification
  or sufficient ventilation time
- Log the shutdown — trigger, time, processing
  state at shutdown, operator present
- Equipment inspection required before restart —
  confirm no damage, contamination, or blockage
- Human authorization required to restart after
  any emergency shutdown — operator judgment
  is not sufficient alone at v0

**Safe state after shutdown:**
Power isolated, enclosure closed, Air Scrubber
running for exhaust clearance, item and output
isolated pending assessment. This is the only
defined safe state. Any other configuration
requires explicit human authorization.

---

## 8. Integration Hooks

- `Architecture/Forge_flow.md` — governing gate
  sequence; Reduction is Gate D outcome path
- `Operations/Gate_01_Intake.md` — upstream
  safety screening; GI-002 and GI-003 are
  prerequisites for safe Reduction operation
- `Operations/Gate_02_Triage.md` — upstream
  gate logic; items routed here have failed
  Gate_02 triage
- `Operations/Gate_04_Separation_Mechanical.md`
  — primary downstream recipient of Reduction
  output; output envelope must cross-validate
  against Gate_04 inputs
- `Operations/Air_Scrubber.md` — required
  operational for all Reduction runs; particulate
  and exhaust handling
- `Operations/Energy.md` — energy cost of
  Reduction not yet characterized
- `Architecture/Forge_Net.md` — contamination
  discovery logs and output characterization
  data contributed to network reference database
- `Unknowns.md` — GR-001 through GR-005
  indexed once logged
- `Admin/Trajectories.md` — method selection
  and automation targets by version; melt-and-draw
  wire production fast path noted as future
  consideration for clean single-class feedstock

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Reduction conceived as a simple mechanical process requiring minimal doctrine | Scope expanded during drafting — contamination discovery protocol, prohibited inputs, output envelope, dust handling, and emergency shutdown all surfaced as load-bearing doctrine before a single method was specified | Reduction's irreversibility means doctrine must precede specification. What Reduction must not do is clearer and more urgent than what it should do. Constraints first, positive specification second | Analogous | No — constraints-first approach is correct |
| 2026-05-15 | Audit Review | Output envelope defined from Reduction side — what the method produces | Gate_04_Separation_Mechanical.md provisional inputs are the binding constraint, not method capability | Output envelope must be defined backward from downstream requirements, not forward from method capability. A Reduction output that Gate_04 cannot process is not a valid output regardless of how efficiently it was produced | Analogous | Yes — cross-validate when Reduction method is selected |
| 2026-05-15 | Audit Review | Contamination discovery treated as an exceptional edge case | Contamination discovery during Reduction is a credible operational condition given upstream screening limitations at v0 — GI-002 and GI-003 unresolved | Contamination discovery protocol elevated to a primary body section, not an appendix. Every contamination event is a network contribution — log and share. The protocol exists because upstream screening is imperfect, not because contamination is rare | Analogous | Yes — validate against first operational cycle |
| 2026-05-15 | Audit Review | Dust and fines treated as waste stream only | Metal fines are potential feedstock for Gate_05_Separation_Thermal.md. Combustible metal fines are a distinct hazard requiring specialist protocol | Fines are a hazard, a potential feedstock, and a diagnostic signal simultaneously. Unusual fines volume or composition indicates unexpected feedstock content or equipment wear. Fines handling requires classification, not uniform disposal | Analogous | Yes — baseline fines generation rate established during first operational cycle |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

*No interpretation conflicts currently active. Several
design tensions exist (method selection for mixed vs.
single-class feedstock, automation introduction timing,
output envelope tolerance vs. Gate_04 sensitivity) but
all are deferred pending first operational data and
method selection. Tracked as unknowns in sidecar, not
disputes. Revisit after first operational Reduction
cycle produces method characterization data.*

---

## Auditor Notes & Unknowns

### GR-001 — Output envelope not validated against
Gate_04 inputs

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The Reduction output envelope is
currently defined backward from Gate_04's provisional
input constraints. Neither set of constraints has been
validated against actual Reduction output from a
selected method.

**Why It Matters:** Gate_04 cannot reliably classify
material that arrives outside its design envelope.
Oversized particles jam the rotor. Prohibited geometries
cause entanglement. Wet or contaminated material fouls
sensors. An unvalidated output envelope means Gate_04
receives undefined input — its performance claims
cannot be evaluated.

**Resolution Path:**
- Select Reduction method (GR-002 prerequisite).
- Characterize actual output distribution for
  selected method against representative feedstock
  samples — particle size distribution, mass range,
  geometry profile.
- Cross-validate against Gate_04 provisional inputs
  — does actual output fall within Gate_04 envelope?
- If not: adjust Reduction method parameters or
  revise Gate_04 provisional inputs.
- Payment via Specification — once output envelope
  is characterized and cross-validated, move to
  Section 4 as Measured.
- Cross-reference: Operations/
  Gate_04_Separation_Mechanical.md Inputs section,
  MG-001, UNK-007.

---

### GR-002 — Reduction method not selected

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** No Reduction method has been selected
for v0. Method selection determines output envelope,
equipment requirements, dust generation profile,
operator safety requirements, and energy consumption.

**Why It Matters:** Every positive specification in
this file depends on method selection. A file that
cannot specify its method cannot specify most of its
operational parameters.

**Resolution Path:**
- Evaluate available equipment at v0 bootstrap —
  purchase-what-cannot-be-produced doctrine applies.
- Evaluate feedstock profile — method must suit
  most common feedstock, not ideal feedstock.
- Candidate methods for v0 bootstrap:
  - Angle grinder or cutting wheel — low cost,
    human-operated, controllable, slow. *(Analogous)*
  - Hydraulic shear — higher throughput, larger
    sections, controllable geometry. *(Analogous)*
  - Rotary shredder — highest throughput, mixed
    feedstock, less geometry control. *(Analogous)*
  - Manual cutting — lowest cost, highest control,
    lowest throughput. Valid bootstrap option.
    *(Analogous)*
- Method selection feeds GR-001, GR-004, and
  Energy.md accounting directly.
- Payment via Specification — once method is
  selected and first operational run characterizes
  output, move to Section 3 as Analogous promoting
  toward Measured.

---

### GR-003 — Biological and chemical waste disposal
doctrine not assigned

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety / Governance                  |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Material that cannot be processed
through normal Reduction due to biological or chemical
contamination has no defined disposal path in the
repository. What happens after isolation — controlled
disposal, specialist handling, hazmat routing — has
no owner.

**Why It Matters:** Contaminated material that cannot
be processed cannot be held indefinitely. Without a
disposal doctrine it accumulates in isolation until
an improvised decision is made under pressure.
Improvised hazmat decisions are a primary source of
environmental and safety incidents.

**Resolution Path:**
- Define minimum disposal categories:
  - Chemical contamination — solvent, heavy metal,
    flux residue disposal paths
  - Biological contamination — organic matter,
    fluid disposal paths
  - Radiological — specialist handling required
- Define holding doctrine — maximum hold duration,
  container requirements, labeling
- Define escalation path — when does disposal
  require specialist involvement?
- Jurisdiction-dependent regulatory requirements
  must be researched for each deployment context
- Consider creating `Operations/Waste_Handling.md`
  to own this doctrine across all modules
- Payment via Specification — once disposal
  categories and paths are defined, move to
  Section 2 prohibited inputs as Analogous.
- Cross-reference: Operations/Gate_01_Intake.md
  GI-005, Admin/Ethical_Constraints.md.

---

### GR-004 — Particulate generation rate and
composition not characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The volume, size distribution, and
composition of dust and fines generated during
Reduction have not been characterized for any
candidate method or feedstock class.

**Why It Matters:** Air Scrubber sizing, filter
selection, operator PPE specification, and combustible
dust explosion risk assessment all depend on
particulate characterization. An undersized scrubber
that cannot handle actual particulate load is a safety
failure that won't be visible until the first
operational run.

**Resolution Path:**
- Depends on GR-002 method selection — different
  methods produce different particulate profiles.
- Characterize particulate generation rate and
  size distribution for representative feedstock.
- Cross-reference Operations/Air_Scrubber.md —
  particulate characterization feeds scrubber
  specification and filter selection directly.
- Check for combustible dust risk — aluminum and
  magnesium fines are combustible at sufficient
  concentration and particle size.
- Payment via Specification — once particulate
  profile is characterized, move to Section 6
  as Measured.
- Cross-reference: Operations/Air_Scrubber.md,
  ASM-005.

---

### GR-005 — Automation introduction criteria
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Governance                           |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The criteria that must be met before
automated Reduction without continuous human presence
is permitted have not been defined.

**Why It Matters:** Reduction's irreversibility makes
automation introduction the highest-stakes capability
transition in the Forge system. Introducing automation
prematurely removes the primary compensating control
for unresolved upstream screening and gate logic gaps.

**Resolution Path:**
- Define minimum prerequisites for automation:
  - FL-001 resolved — gate logic determinism
    validated
  - GI-002 resolved — energetic discharge
    validated and operational
  - GI-003 resolved — augmented detection
    validated and operational
  - GR-001 resolved — output envelope validated
  - GR-004 resolved — particulate profile
    characterized and scrubber sized
  - Safety interlock specification — automated
    shutdown triggers defined and tested
  - Human authorization — explicit sign-off
    required before first unattended run
- Automation introduction is a Specification-level
  decision — cannot be made at Exploration stage
- Cross-reference: ASM-006, ASM-001, ASM-002,
  Admin/Ethical_Constraints.md.

---

### GR-006 — Mechanical jam clearing doctrine
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-07-28                                       |
| Last Reviewed | 2026-07-28                                       |

**Description:** No procedure exists for safely clearing a
mechanical jam in Reduction equipment. This entry existed in
`Unknowns.md`'s active index with no matching sidecar block here —
registered now to close that gap; the underlying concern is not new.

**Why It Matters:** A jam-clearing attempt on energized or
partially-energized reduction equipment is a plausible injury
mechanism. Without a defined procedure, operators default to ad hoc
judgment under time pressure — exactly the condition this
repository's safety doctrine generally tries to design out.

**Resolution Path:** Define a mandatory de-energization and
lockout sequence before any jam-clearing attempt, cross-referenced
against `Admin/Safety_Protocols.md`. Identify jam-prone mechanisms
specifically (which Reduction method(s) this applies to depends on
GR-002's method selection, still Open) before finalizing procedure
detail.

---

### GR-007 — Contaminated equipment retirement threshold
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Safety / Governance                              |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-07-28                                       |
| Last Reviewed | 2026-07-28                                       |

**Description:** No threshold exists for when Reduction equipment
exposed to contaminated feedstock (hazardous residue, cross-material
contamination) must be retired rather than cleaned and returned to
service. This entry existed in `Unknowns.md`'s active index with no
matching sidecar block here — registered now to close that gap; the
underlying concern is not new.

**Why It Matters:** Without a retirement threshold, contaminated
equipment either stays in service indefinitely (accumulating risk
silently) or gets retired inconsistently on operator judgment alone.
Cross-references `Challenges/Waste.md` WA-002 (hazardous fraction
identification) and `Admin/Ethical_Constraints.md` §Toxic and
Hazardous Material Handling — this is a genuine safety gap, not a
process nicety, hence Critical priority.

**Resolution Path:** Define contamination categories requiring
retirement vs. decontamination-and-return, cross-referenced against
WA-002's hazardous fraction identification (itself still Open — this
entry is partially downstream of that one). Until both resolve,
treat any equipment with confirmed hazardous contamination as
retired by default rather than attempting an undefined
decontamination procedure.

---

### GR-008 — Operator decision support minimum standard
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Major                                            |
| Type          | Technical / Human Factors                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_03_Reduction.md                  |
| First Logged  | 2026-07-28                                       |
| Last Reviewed | 2026-07-28                                       |

**Description:** No minimum standard exists for what decision
support (guidance, checklists, real-time feedback) an operator
running Reduction must have available. This entry existed in
`Unknowns.md`'s active index with no matching sidecar block here —
registered now to close that gap; the underlying concern is not new.

**Why It Matters:** Reduction is irreversible and safety-relevant
(see GR-005 above); an operator working from memory alone, with no
structured decision support, is a weaker safety posture than one
working from a defined checklist or interlock system — lower
severity than GR-006/GR-007, hence Major rather than Critical.

**Resolution Path:** Define minimum decision-support content
(pre-run checklist, in-run status indicators, stop conditions) once
GR-001 (output envelope) and GR-002 (method selection) resolve —
decision support content depends on knowing what the operator is
actually deciding between.

---

### Resolution Log

- 2026-07-28: GR-006, GR-007, GR-008 given formal sidecar entries —
  previously present in `Unknowns.md`'s active index only, with no
  matching blocks here, surfaced by a Grok-run repo-wide desync audit
  and verified against source (zero prior mentions of any of the
  three anywhere in this file) before registering. Descriptions built
  from the index's own existing text rather than invented. Open
  Unknowns count: 5 → 8. Verified and registered by Claude —
  Synthesizer/Auditor, human-directed.
- 2026-06-08: Navigation Anchors block added. Verification Ref
  corrected from `Admin/Forge_Audit_Kit.md` to
  `Admin/Verification_Gates.md` (PC-001). Scope Boundary
  facility siting reference updated from `UNK-006 — no file
  exists yet` to `Architecture/Facilities.md — FA-001` (PC-002).

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Direct melt-and-draw wire production as a Reduction method — using induction coils to melt feedstock and draw wire directly from the melt | Mixed feedstock produces mixed alloy wire of unknown tensile strength, conductivity, and welding behavior. Contamination in the melt goes directly into the wire with no separation stage. Bypasses Spin Chamber gradient formation entirely — the ranked material stream that justifies Gate_05 complexity is lost. Wire drawn from an uncontrolled melt is brittle and inconsistent without tight draw speed, temperature, and nozzle control | Reconsider for known clean single-class feedstock where wire quality requirements are low and speed matters more than consistency — bootstrap structural welding wire from known aluminum scrap is a candidate. Route to Admin/Trajectories.md and SC-004 for tracked development |
| 2026-05-15 | Single universal Reduction method for all feedstock classes | Different material classes have fundamentally different Reduction behaviors — ductile metals deform rather than fracture under milling, brittle materials shatter unpredictably under cutting, flexible materials tangle rotors under shredding. A single method produces poor output quality and creates safety risks for the classes it handles badly | Reconsider only if operational data shows one method handles v0 feedstock distribution adequately — requires characterization data from first operational cycle |
| 2026-05-15 | Reduction as default routing for difficult-to-classify items | Difficulty in classification is a gate logic problem, not a Reduction trigger. Routing ambiguous items to Reduction resolves the classification problem by destroying the item — this is the wrong resolution. Ambiguous items route to Human/AI Oversight Gate | No — Oversight Gate routing for ambiguous items is permanent doctrine |
| 2026-05-15 | Open-air Reduction without enclosure | Particulate escape risk, operator respiratory exposure, and exhaust contamination of the surrounding environment are all unacceptable. Enclosure is not optional — it is a prerequisite for Air Scrubber integration to function | No — enclosed Reduction is permanent doctrine |
| 2026-05-15 | Automated Reduction at v0 without resolved upstream prerequisites | FL-001 gate logic determinism, GI-002 energetic discharge, and GI-003 augmented detection are all unresolved at v0. Human presence compensates for these gaps. Removing human presence before the gaps are resolved eliminates the primary safety compensating control at the only irreversible step in the system | Reconsider only when FL-001, GI-002, GI-003, GR-001, and GR-004 are all resolved and safety interlocks are validated — see GR-005 |
| 2026-05-15 | Reduction output routed directly to Gate_05_Separation_Thermal without Gate_04 mechanical separation | Skipping Gate_04 sends unclassified mixed material directly to the Spin Chamber, increasing contamination risk, reducing segregation effectiveness, and defeating the purpose of the mechanical separation stage. Gate_04 exists to protect Gate_05 from exactly this scenario | No — sequential gate routing is permanent doctrine |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to Gate_03_Reduction:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Reduction begins without Air Scrubber verification | Air Scrubber operational status is a hard prerequisite — no exceptions. If scrubber cannot verify, Reduction does not start |
| Reduction begins without human operator present before GR-005 resolution | Human presence is the primary compensating control for unresolved upstream gaps — removing it before GR-005 criteria are met eliminates the only irreversible-step safety backstop |
| Contamination discovery protocol bypassed under throughput pressure | Contamination discovered during Reduction must trigger immediate stop — throughput pressure is never a valid override at the only irreversible step |
| Prohibited input list revised without GR-003 review | Waste disposal doctrine and prohibited input list must stay synchronized — a new prohibited category without a disposal path creates an unresolvable hold condition |
| Output envelope revised without GR-001 cross-validation against Gate_04 inputs | Output envelope changes propagate directly to Gate_04 performance — unilateral revision without cross-validation creates hidden downstream incompatibility |
| Reduction method changed without GR-002 update and GR-004 particulate re-characterization | Method change invalidates particulate profile and output envelope — Air Scrubber sizing and Gate_04 input assumptions both require revalidation |
| Open-air Reduction introduced without enclosure | Permanently abandoned path — reverting requires explicit human authorization, documented justification, and Air Scrubber integration review |
| Ambiguous or difficult-to-classify items routed to Reduction without Oversight Gate review | Permanently abandoned path — classification difficulty routes to Oversight Gate, never directly to Reduction |
| Melt-and-draw wire production introduced without clean single-class feedstock confirmation | Abandoned path with conditional reconsider — introduction requires confirmed feedstock purity, wire quality characterization, and explicit route through Admin/Trajectories.md and SC-004 |
| Highest Risk label downgraded without first operational cycle data and GI-002 and GI-003 resolution | High risk reflects current unresolved upstream gaps — downgrade requires operational evidence that those gaps are closed, not assumption |

### Canonical Drift Triggers

*All mandatory re-audit conditions from Admin/File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*
