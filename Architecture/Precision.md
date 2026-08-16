# Precision.md — LazarusForge

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

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
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Precision as a capability ceiling — declaration, tracking,
  and revision doctrine
- Tolerance classification tier system — repository-wide
  standard that gate files reference
- Metrology doctrine — how the Forge measures what it makes
  at v0 with salvaged equipment (resolves CO-002)
- Measurement uncertainty doctrine — honest accounting of
  what salvaged instruments can and cannot resolve
- Salvage equipment dimensional derating — applying
  Engineering.md derating principles to positional accuracy
  and surface finish
- The fabrication-precision feedback loop — how Gate_07
  utilization data revises the Gate_06 precision ceiling
- Precision floor doctrine — minimum measurable threshold
  below which Forge output cannot be claimed to spec
- Arkansas climate dimensional effects — thermal expansion
  and humidity effects on dimensional stability

**This file DOES NOT define:**
- Foundational engineering principles or safety factors
  (→ `Architecture/Engineering.md`)
- Kinematic interlock thresholds or gantry rigidity criteria
  (→ `Architecture/Mechanical_Structures.md`)
- G-code, toolpath generation, or CAM workflows
  (→ `Operations/Gate_06_Fabrication.md` and future)
- Arc welding qualification criteria
  (→ `Operations/Gate_06_Fabrication.md`)
- Specific instrument specifications or brands
- Metrology for chemical or thermal measurement
  (→ `Architecture/Chemistry.md`,
  `Architecture/Thermal_Systems.md`)
- Quality certification or standards compliance
  (→ GU-003 — not yet assigned)

---

## File Purpose

Precision is referenced throughout the LazarusForge repository
as a capability threshold, a ceiling, a constraint, and a goal —
but no file owns what precision means in the Forge context, how
it is measured, or how the ceiling is declared and tracked.
This file closes that gap.

The Forge at v0 is a salvage-first system operating salvaged
equipment in a high-humidity, high-temperature environment.
Its precision capability is real but bounded — and the bounds
matter. A Forge that claims tolerances it cannot hold produces
parts that fail silently in service. A Forge that honestly
declares its precision ceiling and tracks it as capability
grows is a system that learns.

GK-005 in `Architecture/Geck_forge_seed.md` identified precision
as a capability threshold with no owning file. CO-002 in
`Architecture/Components.md` deferred metrology precision
thresholds to first fabrication trials — this file provides
the doctrine those trials will feed into. ME-001 in
`Architecture/Mechanical_Structures.md` marks kinematic
interlock thresholds as provisional — this file provides
the measurement standard that makes them falsifiable.

Without this file, gate files define their own implicit
precision standards, the fabrication-precision feedback
loop has no doctrine to close against, and the Forge cannot
make honest claims about what it can build to spec.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|----|------------|-------|------------|----------------|
| ASM-001 | v0 fabrication equipment is salvaged and operates below nameplate precision specifications | Salvage-first doctrine; no new precision equipment assumed at bootstrap | High | New precision equipment acquired and characterized |
| ASM-002 | Measurement instruments at v0 are also salvaged or consumer-grade — not calibrated laboratory instruments | Bootstrap realism | High | Calibrated instruments acquired or third-party metrology service engaged |
| ASM-003 | Arkansas summer thermal expansion materially affects dimensional stability of ferrous parts above 300mm | Climate baseline; steel CTE ~12 µm/m·°C; 30°C seasonal swing | Medium | Site temperature-controlled to ±2°C |
| ASM-004 | The operator performing measurement is the same operator who fabricated the part — no independent inspection at v0 | Single-contributor bootstrap | High | Independent inspection capability established |
| ASM-005 | Precision capability improves monotonically as the Forge matures — early ceiling declarations will be revised upward | Expected operational trajectory | Medium | Capability degrades due to equipment wear — ceiling must be revised downward |

---

## I. Precision as a Capability Ceiling

### What the Ceiling Is

The precision ceiling is the tightest tolerance the Forge can
reliably hold across a production run under normal operating
conditions. It is not the tightest tolerance ever achieved on
a single part under ideal conditions — it is the repeatable
bound.

**Reliable** means: achievable on at least 80% of attempts
without exceptional operator intervention or setup time.
A tolerance achieved once under perfect conditions is not
the ceiling — it is an outlier.

**Normal operating conditions** means: ambient temperature
within the Arkansas seasonal range, equipment in standard
maintenance state, no extraordinary fixturing beyond what
the Forge routinely deploys.

### Declaring the Ceiling

The precision ceiling is declared by the operator at each
of the following trigger points:

1. **At v0 commissioning** — baseline declaration from first
   measured fabrication trials. May be coarse. Must be honest.

2. **After any significant equipment change** — new salvaged
   machine, major repair, gantry reconfiguration, spindle
   replacement. Equipment changes invalidate prior ceiling
   declarations for affected axes.

3. **After Gate_07 feedback triggers revision** — when
   utilization data shows systematic dimensional error
   in deployed parts, the ceiling is revised to reflect
   actual observed capability, not intended capability.

4. **At each version advancement** — the precision ceiling
   at v0 exit must be documented as part of the v0→v1
   transition record.

### Ceiling Components

The precision ceiling has three components that must each
be declared:

| Component | Definition | Example Declaration |
|---|---|---|
| Positional accuracy | How close to target position a cut or weld lands | ±1.5mm positional |
| Dimensional repeatability | Variation between identical features across a run | ±0.8mm repeat |
| Surface finish | Achievable surface roughness on machined faces | Ra 6.3 µm (N9) |

At v0 with salvaged equipment, these figures will be coarse.
That is correct. The ceiling is not a target — it is an honest
bound. Aspirational ceilings that exceed demonstrated capability
are a governance failure equivalent to false precision in an
audit finding.

### Ceiling Revision Doctrine

The ceiling may be revised upward when: new equipment is
characterized, process improvement is demonstrated across
multiple cycles, or measurement capability improves and
reveals the prior ceiling was conservative.

The ceiling must be revised downward when: Gate_07 utilization
data shows systematic out-of-spec failures, equipment
degradation is detected, or environmental conditions change
such that prior measurements no longer apply.

**Downward revision is not failure** — it is honest accounting.
A Forge that revises its ceiling downward in response to
evidence is a Forge that learns. A Forge that holds an
aspirational ceiling in the face of contrary evidence is
producing parts it cannot actually make to spec.

---

## II. Tolerance Classification Tier System

Repository-wide standard. Gate files, specification documents,
and part records reference these tiers rather than defining
their own tolerance scales.

### Tier Definitions

| Tier | Name | Positional Tolerance | Typical Application | v0 Achievable |
|---|---|---|---|---|
| T0 | Structural | ±5mm or coarser | Non-load-bearing frames, rough fixtures, enclosures | Yes |
| T1 | Mechanical | ±1–2mm | Load-bearing structural members, bolt patterns, mounting surfaces | Yes — with care |
| T2 | Functional | ±0.5mm | Moving parts, clearance fits, mating surfaces | Marginal — equipment-dependent |
| T3 | Precision | ±0.1mm | Bearing seats, close fits, gauging surfaces | No at v0 — requires dedicated precision equipment |
| T4 | High Precision | ±0.025mm or finer | Spindle interfaces, optical mounts, instrument components | Not in v0 scope |

**v0 operating range:** T0 and T1 are the reliable working
tiers. T2 is achievable on well-maintained salvaged equipment
with careful setup but should not be assumed. T3 and T4
require precision equipment the v0 Forge does not have.

### Tier Assignment in Part Records

When a part is fabricated and logged in Gate_07, its tolerance
tier is recorded alongside the fabrication output tag from
Gate_06. This tier assignment:
- Sets the inspection interval (lower tiers tolerate longer
  intervals; T2 parts are inspected more frequently)
- Determines whether the part is eligible for safety-critical
  or load-bearing service (T0 parts are not)
- Feeds the precision ceiling feedback loop — a T1 part
  that consistently measures within T2 bounds is evidence
  that the ceiling can be revised upward for that process

### Tier and Safety Class

Tier assignment interacts with the safety consequence classes
in `Admin/Safety_Protocols.md`:

| Safety Class | Minimum Tier Required |
|---|---|
| Non-structural (enclosures, guards) | T0 |
| Load-bearing structural | T1 minimum — T2 preferred |
| Moving mechanical interface | T2 minimum |
| Safety-critical (brakes, interlocks, containment) | T2 minimum — T3 required if available |

A safety-critical part fabricated to T0 is a known
under-specification. It must be logged as such, flagged in
Gate_07, and reviewed at the next audit cycle. It is not
automatically prohibited — bootstrap realism applies — but
it is not invisible either.

---

## III. Metrology Doctrine

### What Metrology Means at v0

Metrology is the science of measurement. At v0 with salvaged
or consumer-grade instruments, Forge metrology means:
making dimensional measurements honestly, understanding the
limits of the instruments used, and recording both the
measurement and the instrument's known uncertainty.

CO-002 in `Architecture/Components.md` deferred metrology
precision thresholds to first fabrication trials. This file
provides the doctrine those trials produce measurements against.

### Instrument Classes at v0

| Instrument | Typical Resolution | Typical Accuracy | Forge Use |
|---|---|---|---|
| Steel rule | 0.5mm | ±1mm | T0 rough layout only |
| Vernier caliper (salvaged) | 0.05mm | ±0.1–0.3mm | T1 measurement; T2 marginal |
| Digital caliper (consumer) | 0.01mm | ±0.03–0.1mm | T1 reliable; T2 with care |
| Micrometer (salvaged) | 0.01mm | ±0.02–0.05mm | T1–T2 reliable |
| Dial indicator on surface plate | 0.01mm | ±0.02mm | T2 with good surface plate |
| Angle gauge / protractor | 0.5° | ±1° | Angular layout |

**Salvage derating:** A salvaged instrument's stated accuracy
applies only if: it has been cleaned, the measuring faces are
undamaged, the mechanism moves freely without play, and it
has been checked against a known reference. A salvaged
caliper that has not been verified against a reference standard
should be treated as one accuracy class lower than its
nominal specification.

### Measurement Uncertainty Doctrine

Every measurement has uncertainty. The Forge acknowledges this
explicitly rather than treating measurements as exact.

**At v0, the working rule is:**

> Record the measured value and the instrument used.
> The measurement uncertainty is at minimum the instrument's
> stated accuracy class — and may be higher for salvaged
> instruments not verified against a reference.

When recording a dimension, the format is:
`[measured value] ±[uncertainty] ([instrument])`

Example: `47.3mm ±0.3mm (salvaged vernier caliper, unverified)`

This is not bureaucratic overhead — it is the difference
between a part record that can be acted on and one that
creates false confidence. A part recorded as "47.3mm" implies
precision the measurement may not have. A part recorded as
"47.3mm ±0.3mm" tells the next operator exactly what they
are working with.

### Reference Standard Doctrine

Measurement uncertainty can only be bounded if instruments
are checked against a reference. At v0 bootstrap, the
minimum reference standard is:

- A known-good gauge block set, or
- A precision ground reference bar, or
- A third-party dimensional check of a representative part
  by an external metrology service

A Forge with no reference standard cannot make traceable
dimensional claims. It can still fabricate — but its
part records must reflect that measurements are instrument-
relative, not reference-traceable. This is acceptable at
v0 Exploration stage. It is not acceptable at Specification
stage (PR-003).

---

## IV. Salvage Equipment Dimensional Derating

`Architecture/Engineering.md` owns the general derating
principle for salvaged equipment under Arkansas climate
conditions. This section applies that principle specifically
to dimensional accuracy and positional repeatability.

### Sources of Dimensional Error in Salvaged Equipment

**Mechanical wear:**
Worn leadscrews, backlash in gantry drives, and bearing
play all introduce positional error. A salvaged mill with
0.3mm of leadscrew backlash cannot hold T2 tolerance on
a bidirectional cut regardless of operator skill. The
backlash must be measured and either compensated or
reflected in the ceiling declaration.

**Thermal expansion:**
Steel expands approximately 12 µm per meter per °C.
A 500mm steel workpiece in an Arkansas summer shop that
swings 20°C between morning and afternoon expands 0.12mm
— comparable to T2 tolerance. Parts measured at 7am and
cut at 2pm in an uncontrolled shop are not the same
temperature. This is not a trivial error at T1–T2.

**Arkansas specific derating factors:**

| Condition | Effect | Derating Rule |
|---|---|---|
| Summer ambient swing (≥20°C daily) | Thermal expansion error ≥0.1mm/500mm | Measure and cut within same thermal window; or add thermal expansion allowance |
| High humidity (>80% RH) | Moisture absorption in wood fixtures; surface oxidation on reference faces | Use metal fixturing; clean reference faces before measurement |
| Dust from reduction operations | Instrument contamination; caliper jaw fouling | Segregate metrology from reduction zone; clean instruments before use |

**Structural compliance:**
A salvaged gantry with insufficient rigidity deflects under
cutting load. The deflection is a dimensional error that
does not appear in leadscrew or backlash measurements.
`Architecture/Mechanical_Structures.md` owns the gantry
rigidity doctrine — this file notes that compliance-induced
dimensional error must be included in ceiling declarations
for milling operations.

### Derating Declaration Format

When declaring the precision ceiling after equipment
characterization, the operator records:

1. Measured backlash per axis (if applicable)
2. Thermal expansion allowance applied
3. Estimated compliance deflection under typical cutting load
4. Net declared ceiling after applying all derating factors

The declared ceiling is the sum of these error sources —
not any single source in isolation.

---

## V. The Fabrication-Precision Feedback Loop

### Structure of the Loop

Gate_06 fabricates to a declared precision ceiling.
Gate_07 measures deployed parts and records dimensional
performance in service. That data returns to Gate_06
as evidence for ceiling revision.

This file owns the doctrine for how that loop closes:

**Gate_06 → part record:** Every fabricated part record
includes the tolerance tier claimed at fabrication and
the measurement taken at completion (format per Section III).

**Gate_07 → performance record:** When a part is inspected
in service, dimensional drift, fit degradation, or
out-of-spec findings are recorded against the original
part record. If a T1 part consistently drifts to T0
dimensions in service, that is data about the fabrication
process, not just that part.

**Performance record → ceiling revision:** When three or
more parts from the same process show consistent dimensional
performance above or below the declared ceiling, the
operator reviews the ceiling declaration. Three data points
is not a statistical sample — it is the minimum signal
threshold at v0 bootstrap. More data is better.

**Ceiling revision → Gate_06:** The revised ceiling is
the new operating standard for that process. Parts
fabricated after a ceiling revision are held to the
new standard. Prior parts are not retroactively
re-classified — their original tier stands in the record.

### Loop Failure Modes

| Failure Mode | Signal | Response |
|---|---|---|
| Parts fabricated without tier declaration | Gate_07 has no baseline to compare against | Mandate tier declaration at Gate_06 before part enters service |
| Gate_07 records dimensional findings without routing to ceiling review | Loop is open — data accumulates but doesn't improve the process | Explicit routing tag required in Gate_07 records for dimensional findings |
| Ceiling revised upward without supporting data | Aspirational ceiling inflation — produces systematic out-of-spec parts | Ceiling revision requires three-point evidence minimum |
| Ceiling revised downward but Gate_06 continues to claim prior tier | Prior tier claims become false precision | Ceiling revision propagates immediately to active fabrication standard |

---

## VI. Precision Floor Doctrine

The precision floor is the lower bound — the minimum
dimensional capability below which the Forge cannot
make any meaningful precision claim at all.

At v0, the precision floor is defined by the worst
instrument in routine use and the most significant
uncontrolled error source. If the best instrument
available is a salvaged unverified vernier caliper
with ±0.3mm accuracy, and the shop has uncontrolled
thermal swing, the precision floor is approximately
±0.5mm under typical conditions.

**Below the floor:** Parts fabricated below the precision
floor are T0 structural parts only. They may be fabricated
and used — but they cannot carry a dimensional specification
in their part record, only a nominal dimension with a
"below precision floor" flag.

**Significance:** The precision floor prevents the tolerance
tier system from being applied to parts the Forge genuinely
cannot measure. A T1 claim on a part fabricated and measured
below the precision floor is false precision — the same
governance failure as an unsubstantiated audit claim.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### PR-001 — Precision ceiling not yet declared

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | High                           |
| Priority      | Critical                       |
| Type          | Operational                    |
| Blocking      | Yes — blocks T1/T2 part claims |
| Owner         | Architecture/Precision.md      |
| First Logged  | 2026-06-05                     |
| Last Reviewed | 2026-06-05                     |

**Description:** No precision ceiling has been declared for
any Forge fabrication process. All tolerance tier claims
in fabricated parts are provisional until the ceiling is
established from first fabrication trials.

**Why It Matters:** Without a declared ceiling, Gate_06
fabrication claims, Mechanical_Structures.md interlock
thresholds, and any part record that references a tolerance
tier are all ungrounded. ME-001 explicitly marks kinematic
interlock thresholds as provisional for this reason.

**Resolution Path:** Operator declares ceiling from first
fabrication trials per Section I. Record in Resolution Log
with date, equipment characterized, and derating factors
applied. Closes CO-002 in Components.md and partially
resolves ME-001 in Mechanical_Structures.md.

---

### PR-002 — Reference standard not yet established

| Field         | Value                     |
|---------------|---------------------------|
| Status        | Open                      |
| Risk          | Medium                    |
| Priority      | Major                     |
| Type          | Technical                 |
| Blocking      | No                        |
| Owner         | Architecture/Precision.md |
| First Logged  | 2026-06-05                |
| Last Reviewed | 2026-06-05                |

**Description:** No reference standard exists for instrument
verification at v0. All measurements are instrument-relative,
not reference-traceable. Section III defines the minimum
reference standard required for traceable claims.

**Why It Matters:** Instrument-relative measurements can only
be compared within the same measurement session with the same
instrument. Cross-session, cross-instrument, or cross-forge
dimensional comparison requires a shared reference standard.

**Resolution Path:** Acquire minimum reference standard
(gauge block set, precision ground bar, or third-party
metrology check) before Specification promotion. At
Exploration and Draft stage, instrument-relative measurements
with explicit uncertainty declarations are acceptable.

---

### PR-003 — Traceable dimensional claims required at Specification

| Field         | Value                     |
|---------------|---------------------------|
| Status        | Open                      |
| Risk          | Medium                    |
| Priority      | Major                     |
| Type          | Governance                |
| Blocking      | No — blocks Specification |
| Owner         | Architecture/Precision.md |
| First Logged  | 2026-06-05                |
| Last Reviewed | 2026-06-05                |

**Description:** Section III states that instrument-relative
measurements without reference traceability are not acceptable
at Specification stage. PR-002 (reference standard) must be
resolved before this file or any file making dimensional
claims can be promoted to Specification.

**Why It Matters:** A Specification-level document making
dimensional claims that cannot be externally verified is
not a specification — it is an aspiration with formatting.

**Resolution Path:** Dependent on PR-002. When reference
standard is established, update measurement records to
reference-traceable format. PR-003 closes when PR-002 closes.

---

### PR-004 — Backlash and compliance characterization not yet performed

| Field         | Value                     |
|---------------|---------------------------|
| Status        | Open                      |
| Risk          | High                      |
| Priority      | Major                     |
| Type          | Technical                 |
| Blocking      | No                        |
| Owner         | Architecture/Precision.md |
| First Logged  | 2026-06-05                |
| Last Reviewed | 2026-06-05                |

**Description:** Leadscrew backlash, bearing play, and
compliance deflection under load have not been measured
for any v0 fabrication equipment. Section IV derating
declaration format requires these measurements. The
precision ceiling declared at PR-001 resolution will be
incomplete without them.

**Why It Matters:** A ceiling declared without backlash
and compliance measurements will overstate positional
accuracy. Parts fabricated against an overstated ceiling
will be systematically out of spec in one direction
(the direction where backlash and compliance add rather
than cancel).

**Resolution Path:** Measure backlash per axis and estimate
compliance deflection under typical cutting load at
first equipment characterization. Record per Section IV
derating declaration format. Feed into PR-001 ceiling
declaration.

---

### PR-005 — GK-005 resolution confirmation pending

| Field         | Value                     |
|---------------|---------------------------|
| Status        | Open                      |
| Risk          | Low                       |
| Priority      | Minor                     |
| Type          | Governance                |
| Blocking      | No                        |
| Owner         | Architecture/Precision.md |
| First Logged  | 2026-06-05                |
| Last Reviewed | 2026-06-05                |

**Description:** This file is the intended resolution target
for GK-005 in `Architecture/Geck_forge_seed.md`. GK-005
status should be updated to In Progress or Resolved on
next audit pass of that file.

**Resolution Path:** On next audit pass of
Geck_forge_seed.md, update GK-005 status and
cross-reference this file. Same pattern as GMP-001
for Governance_Migration_Protocol.md.

---

### Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **5** = PR-001–005, matches local +
  `Unknowns.md`. (2) PR-001 correctly **Blocking Yes** (blocks T1/T2 part
  claims). (3) PR-003 “No — blocks Specification” is Epistemic-style nuance,
  consistent with Canonical_Terms Priority (Promo) / Epistemic Blocking.
  (4) No PR-* closed; no ceiling declaration advanced. Human-directed.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-05 | Defining specific tolerance figures for each gate operation | Gate-specific tolerances belong in gate files, not here. This file owns the tier system and ceiling doctrine that gate files reference — not the specific application of those tiers to each module. | No |
| 2026-06-05 | Aspirational precision targets for future versions | Precision capability at v1+ is unknown until v0 operational data exists. Future precision targets stated without basis are false precision — the same failure mode this file exists to prevent. | Reconsider at v1 when operational data exists |
| 2026-06-05 | Filename Precision_LF.md per original GK-005 reference | Repository_Structure.md no-scope-suffix rule adopted. Precision.md is the correct name. GK-005 reference to Precision_LF.md is a stale name — correct on next audit pass of Geck_forge_seed.md. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply.
Additional triggers specific to this file:*

- Precision ceiling declared without fabrication trial data
  (aspirational ceiling — false precision)
- Tolerance tier T3 or T4 claimed in any v0 part record
  without documented exception and evidence
- Gate_07 dimensional findings not routed back to ceiling
  review (feedback loop open)
- Ceiling revised upward without three-point evidence minimum
- Measurements recorded without uncertainty declaration
  after this file reaches Draft status
- PR-002 (reference standard) unresolved when any file
  attempts Specification promotion with dimensional claims
- Backlash and compliance characterization (PR-004) omitted
  from precision ceiling declaration
