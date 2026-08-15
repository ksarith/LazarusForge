# Gate_04_Separation_Mechanical

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> The Material Separation Gate operates a high-RPM rotating drum
> with mixed, unknown-geometry feedstock. Fragment ejection,
> rotor imbalance, and bearing failure are credible failure modes
> at operating speeds of 1,000–5,000 RPM. The drum enclosure is
> designed as a closed system — the operating area must remain
> clear of personnel and sensitive components during all rotating
> states. Enclosure integrity is a design requirement, not an
> optional feature. Siting and clearance requirements are not yet
> governed by a facility or area-of-operation document — tracked
> under sidecar unknown MG-006.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-15; revised 2026-06-08                                      |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Design intent and operating philosophy of the Material
  Separation Gate
- Physical subsystem descriptions for v0 (rotor, sensors,
  collection zones, fail-to-bin protocol)
- RPM exploration band and stratification behavior at v0 scale
- Sensor cross-check architecture and confidence scoring logic
- Fail-to-bin protocol and Unknown Bulk handling
- Output classification system (Class A, B, C, Unknown Bulk, Fail)
- Falsifiable performance metrics (Material Diversion Rate,
  Unknown Bulk Rate)
- Scaling strategy and replication doctrine
- Bootstrap Proxy Mode for early Forge implementations
- Lifecycle, failure modes, and degraded operation behavior
- Integration hooks to downstream and upstream modules
- Contamination risk statement and refusal-first design rationale

**This file DOES NOT define:**
- Upstream feedstock reduction or shredding
  (`Operations/Gate_03_Reduction.md`)
- Thermal processing of Class C output
  (`Operations/Gate_05_Separation_Thermal.md`)
- Component triage and human review of Unknown Bulk
  (`Operations/Gate_02_Triage.md`)
- Air handling and exhaust management from high-RPM operation
  (`Operations/Air_Scrubber.md`)
- Energy accounting and kWh/kg metrics
  (`Operations/Energy.md`)
- Marine thermal sink integration beyond integration hook
  (`Tests/Support_Raft.md`)
- Aquatic biofouling impact on rotor and bearing performance
  (`Tests/Leviathan_testing.md`)
- Electromagnetic field bias for future versions
  (deferred — `Admin/Trajectories.md`)
- Facility siting, clearance, and area-of-operation requirements
  (`Architecture/Facilities.md` — FA-001)
- Detailed sensor specifications or spectroscopy hardware
  (not yet assigned)
- Powder feedstock handling
  (explicit non-goal — out of scope for all versions until
  stated otherwise)

---

## File Purpose

The Material Separation Gate is the upstream mechanical decision
point within the Purification stage of the Lazarus Forge
operational flow. Operating after feedstock reduction and before
thermal processing, it uses mechanical separation to divert
usable material away from the energy-intensive Spin Chamber
where possible. Its primary value is avoided processing — every
kilogram diverted here is a kilogram that does not consume Spin
Chamber energy and time.

The gate is designed around a refusal-first philosophy: when
material cannot be classified with sufficient confidence, it is
held for review rather than passed downstream. Incorrect
classification at this stage contaminates thermal systems,
degrades alloy consistency, and increases energy cost across
the entire Forge. The gate protects everything downstream from
decisions made under uncertainty.

The gate is not a purifier, a smelter, or a guarantee of
separation quality. It is a decision amplifier — its value
grows as upstream reduction and downstream logic improve. If
this file disappeared, the Forge would lose its primary
mechanical diversion stage and route all feedstock directly
to thermal processing, significantly increasing energy
consumption and contamination risk.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Reduced feedstock arrives with a known upstream envelope — particle size and mass range are characterized before reaching the gate | Inputs section — stated but not defined | Medium | Upstream reduction module defines and tracks output envelope |
| ASM-002 | Dual-channel sensor cross-check technology (density measurement and spectroscopy) is available at bootstrap through purchase, salvage, or inter-forge trade | Sensor section; purchase-what-cannot-be-produced doctrine | Low | Sensor procurement confirmed or bootstrap proxy validated |
| ASM-003 | 90% confidence threshold is the correct refusal criterion for routing decisions | Fail-to-bin protocol — stated as rule, not yet validated | Low | Controlled classification trials against known feedstock confirm or revise threshold |
| ASM-004 | v0 operating environment is terrestrial | No marine provisions in v0 spec; Leviathan deferred | Medium | Marine or off-world deployment enters scope |
| ASM-005 | Manual operator or Component Triage System capacity exists to process Unknown Bulk output without backlog | Fail-to-bin routes to review — assumes review capacity | Medium | Unknown Bulk accumulation rate exceeds review capacity — scaling trigger activates |
| ASM-006 | Replication is preferable to enlargement for scaling — multiple small gates are assumed to behave better than a single large one at v0 scale | Scaling doctrine; failure mode distribution logic | Medium | Replication produces coordination problems, resource contention, or interference between units that enlargement would not — or replication pressure forces component evolution that changes the preferred architecture |
| ASM-007 | Mechanical separation is energy-positive relative to thermal processing for the same diverted material — the gate saves more energy than it consumes | Energy Position section; directional improvement assumed | Low | Quantitative energy baseline established against `Operations/Energy.md` — directional assumption confirmed or revised |

*Low confidence assumptions reflect unvalidated operational parameters
and sensor procurement uncertainty. ASM-003 and ASM-007 are the most
load-bearing — the confidence threshold governs every routing decision
and the energy-positive claim is the gate's core economic justification.
Both require experimental validation before the gate can be promoted
beyond Exploration. Purchase-what-cannot-be-produced doctrine applies
to ASM-002. See README.md and `Admin/Trajectories.md` for forge ecology context.*

---

## Purpose

The Material Separation Gate is a **pre-purification decision module**
within the Lazarus Forge. Its goal is to **divert material away from
energy-intensive melting and refinement** by recovering usable fractions
earlier in the process.

It is not a smelter, refinery, or guarantee of purity.

Success is defined by *avoided processing*, not perfect separation.

---

## Position in System Flow

The Material Separation Gate operates **after Reduction** and **before
Purification** within the Lazarus Forge operational flow
(`Architecture/Forge_flow.md`). It is the upstream mechanical decision
point — material that passes here avoids the energy cost of the Spin
Chamber entirely.

---

## Design Philosophy

- Preserve function before destroying structure
- Prefer classification over purification
- Allow explicit "unknown" and "fail" outputs — the system must
  always be able to say no
- Optimize for learning and tunability, not peak throughput
- Replicate gates to scale, do not over-enlarge
- Refusal of ambiguous material is a success condition, not a failure

---

## Inputs

- Reduced metallic feedstock (non-powdered)
- Mixed alloys, fasteners, coatings, or contamination allowed
- Known upstream envelope (particle size, mass range) — see ASM-001

**Provisional v0 feedstock envelope (Placeholder):**
The gate's RPM band, classification stability, geometry assumptions,
and sensor calibration all depend on upstream reduction output
being within a known envelope. Until the Reduction module is
specified, the following provisional constraints apply:

| Parameter | Provisional v0 Constraint | Basis |
|---|---|---|
| Max fragment dimension | ~50mm | *(Placeholder — drum geometry dependent)* |
| Max fragment mass | ~500g | *(Placeholder — rotor balance dependent)* |
| Prohibited geometries | Long thin rods, wire coils, flexible sheet >200mm | *(Placeholder — entanglement/jam risk)* |
| Moisture tolerance | Dry or surface-damp only — no free liquid | *(Placeholder — sensor and bearing risk)* |
| Tangling threshold | No flexible or fibrous material >100mm | *(Placeholder — rotor seizure risk)* |

These constraints are not validated. They exist to reduce hidden
dependency fragility until the Reduction module is assigned and
its output envelope is formally defined. When the Reduction module
specification exists, these placeholders must be cross-validated
and either confirmed or revised. Cross-reference: ASM-001, MG-007.

---

## Core Subsystems (v0)

### 1. Rotational Drum / Rotor

- Variable-speed rotor operating across tunable RPM bands
- v0 exploration band: **~1,000–5,000 RPM** *(Analogous — derived
  from centrifugal separator and rotary classifier equipment at
  similar scale; requires empirical mapping per feedstock profile.
  System behavior depends heavily on fragment geometry, ductility,
  size distribution, and contamination. Do not treat as validated
  operating parameters.)*
- Stepped-diameter drum geometry encourages stratification by
  density and inertia

**Stratification Logic:**
- **Outer Rim** — High-density metallic fragments (iron, nickel,
  dense alloys)
- **Mid-Tier** — Silicates, mixed oxides, intermediate-density
  materials
- **Inner Core** — Low-density polymers, organics, light composites

Band position assignments are *(Analogous — inferred from
centrifugal separation literature and density differential
principles. Empirical validation required per feedstock class
before treating as reliable routing heuristics.)*

*Note: Separation is influenced not only by density, but also by
geometry, surface area, ductility, and aerodynamic drag.
Stratification bands represent emergent behavior, not strict
material classes. All band assignments are treated as probabilistic
heuristics, not deterministic rules. Thin steel vs. thick aluminum
can invert expected radial positions — do not treat band assignments
as guarantees.*

---

### 2. Friction & Thermal Management

- Preferred: Passive magnetic or low-contact bearings to reduce wear
- v0 Proxy: Conventional bearings with monitored wear and vibration
  tracking
- Air and fluid drag at operating RPM generates measurable heat —
  not ignored
- Heat generated is routed via heat pipe to the Support Raft's
  thermal sink where available, or dissipated locally in terrestrial
  configurations
- Bearing wear rate is a primary maintenance metric and scaling
  trigger
- Component standardization required — bearing sizes, shaft
  diameters, and fastener standards must be drawn from a minimal
  shared set to support inter-forge interchangeability and repair.
  A bearing that can be sourced, replaced, or traded between forges
  is worth more than an optimal but bespoke one.

---

### 3. Sensor Cross-Check

- Onboard density measurement and spectroscopy provide dual-channel
  material identification
- Cross-check reduces false classification from single-sensor error
- Confidence scoring is required before any fraction is routed to
  a downstream path
- Sensors must cross-reference inertia with optical geometry to
  ensure light-but-dense materials are not prematurely diverted to
  the polymer stream. Example: aluminum foil can exhibit drag
  behavior similar to low-density polymer — geometry correction
  *(Placeholder — correction algorithm not yet specified; see MG-004)*
  prevents silent misclassification into the wrong recovery stream

**Degraded Mode:**
If one sensing channel fails or drifts out of calibration, the
chamber may operate in single-sensor mode with elevated confidence
thresholds and increased routing to Unknown Bulk. Degraded mode
does not suspend operation — it tightens refusal criteria.

**Sensor Fouling and Particulate Doctrine:**
Mixed scrap at 1,000–5,000 RPM generates conductive dust, abrasive
fines, and particulate that can coat optical sensors and silently
degrade confidence scoring — inflating Unknown Bulk rate without
revealing the cause:

- Sensor fouling presents as gradual Unknown Bulk rate increase
  without corresponding change in feedstock composition —
  distinguish from MG-003 calibration drift by cleaning sensors
  and observing whether Unknown Bulk rate recovers
- Sensor cleaning interval: *(Placeholder — to be established
  during Gen-0 testing; start with post-run cleaning and adjust
  based on observed fouling rate)*
- Enclosure cleaning doctrine: particulate accumulation inside
  enclosure affects rotor balance and bearing performance —
  enclosure cleaning is a maintenance task, not an optional one
- Conductive dust creates electrical shorting risk for sensor
  electronics — sensor housing must be sealed against
  particulate ingress
- Cross-link to `Operations/Air_Scrubber.md`: particulate burden from
  high-RPM operation must be explicitly included in scrubber
  intake specification, not only exhaust gas handling
- Rising Unknown Bulk rate is the primary sensor fouling
  indicator — see MG-008

---

### 4. Fail-to-Bin Protocol

In accordance with the refusal-first ethos of the Forge and
Auditor_Protocols.md:

- If sensor cross-check confidence is **< 90%** *(Placeholder —
  threshold not yet validated against known feedstock samples;
  see MG-003)*, material is ejected to the **Unknown Bulk** bin
- Unknown Bulk is not discarded — it is logged, held, and routed
  to `Operations/Gate_02_Triage.md` or Synthesizer review at next
  available cycle
- Unknown Bulk that remains unresolved after triage may be
  reprocessed through reduction with adjusted parameters, or
  routed to Class C for controlled thermal processing
- Attempting to process unknown material risks furnace
  contamination and downstream cascade failures
- Refusal is a first-class output, not a system fault

---

### 5. Optional Field Bias (Deferred)

- Magnetic or electromagnetic biasing may be added in later versions
- Not required for v0 validation
- Must never force separation beyond observable stability
- Deferred to `Admin/Trajectories.md`

---

### 6. Collection Zones

- Radial or axial bins aligned to stratification bands
- Capture fractions that stabilize under rotation
- Geometry favors repeatable, low-chaos trajectories

---

## Outputs

- **Class A:** Usable components or near-components — prioritize
  fasteners, simple shapes, and identifiable geometry before bulk
  metal recovery. Preserve function before destroying structure
- **Class B:** Downgraded material (repurpose / lower-precision use)
- **Class C:** Mixed bulk → Spin Chamber for thermal processing
- **Unknown Bulk:** Ambiguous or low-confidence material →
  `Operations/Gate_02_Triage.md` review → reduction retry or Class C routing
- **Fail:** Unclassifiable after review → Reduction or discard

---

## Contamination Risk

Incorrect classification at this stage can introduce contaminants
into thermal systems downstream, resulting in alloy degradation,
slag instability, equipment fouling, and increased energy cost.
The gate is therefore biased toward refusal over misclassification.
The <90% confidence threshold exists to protect the Spin Chamber
and everything downstream from decisions made under uncertainty.

---

## Energy Position

The primary energy value of this gate is derived from **avoided
thermal processing**. Sorted metal recovery via mechanical
separation is energy-positive relative to processing the same
material through the Spin Chamber *(Placeholder — directional
improvement expected but not yet quantified against
`Operations/Energy.md` baseline)*. Polymer diversion is currently
energy-neutral *(Placeholder — lifecycle justification is
contamination prevention, not energy recovery)*.

Quantitative energy reduction is expected but not required for
v0 validation. Directional improvement is sufficient. Specific
reduction estimates are deferred to experimental baseline against
`Operations/Energy.md` kWh/kg metric.

---

## Bootstrap Proxy Mode

The Material Separation Gate may be approximated in early Forge
implementations using:

- Inclined vibrating tables or gravity sorting rigs
- Magnetic separation for ferrous bias
- Manual classification assisted by simple jigs

These proxies do not replicate full centrifugal behavior but allow
early-stage material diversion and learning. The goal is not
equivalence, but preservation of the decision loop. An imperfect
gate that runs is more valuable than a perfect one that doesn't
exist yet.

---

## Scaling Strategy

- Multiple small gates are preferred over single large units
- Scaling occurs by replication, not enlargement — see ASM-006
- Gates may be tuned for specific material classes

Scaling triggers include:
- Input backlog exceeding dwell capacity
- Wear rate exceeding maintenance window
- Declining classification confidence
- Unknown Bulk accumulation rate exceeding review capacity

---

## Falsifiable Performance Metric (Primary)

**Material Diversion Rate**

Target for v0 exploration (not a guarantee):
- ≥ 30% diversion indicates viability *(Placeholder — target
  derived from design intent, not operational data)*
- < 10% indicates redesign or removal *(Placeholder)*

**Secondary metric:**
- **Unknown Bulk Rate** — proportion of intake routed to Unknown
  Bulk bin. High rates indicate sensor calibration issues or
  upstream reduction inconsistency, not gate failure. Rising
  Unknown Bulk rate is diagnostic signal, not system fault.

**Tertiary metric:**
- **Net Diversion Efficiency** — proportion of Unknown Bulk
  that is eventually routed to Class C thermal processing
  anyway, after triage and retry. *(Placeholder — metric
  not yet instrumented)*

  If Unknown Bulk retry loops consistently result in Class C
  routing, the gate is acting as a preprocessing tax rather
  than a diversion benefit. A high Net Diversion Efficiency
  loss indicates sensor calibration failure, upstream reduction
  inconsistency, or feedstock outside the gate's classification
  envelope. This metric makes the retry loop cost visible and
  falsifiable. Cross-reference: MG-003, `Operations/Energy.md`.

---

## Lifecycle & Failure Modes

**Degraded Operation** — At reduced RPM or single-sensor operation,
classification confidence thresholds tighten automatically. Gate
continues at lower throughput rather than passing ambiguous material
downstream.

**Jam and Entanglement Doctrine:**
Unknown-geometry feedstock makes rotor jam and entanglement
credible operational conditions, not edge cases:

- Jam detection trigger: sustained motor current increase without
  corresponding RPM — indicates rotor resistance *(Placeholder —
  threshold not yet defined)*
- Automatic shutdown condition: motor current exceeds jam threshold
  for more than 30 seconds *(Placeholder)* — stop rotor, isolate
  power, do not attempt restart until cleared
- Manual clearing protocol: lockout power before any physical
  access to drum interior. No manual clearing during rotation
  under any circumstances.
- Post-jam inspection required before restart: check rotor
  balance, bearing condition, and enclosure integrity
- Feedstock geometries most likely to jam: wire coils, flexible
  sheet, long thin rods — see provisional feedstock envelope
  in Inputs section
- Jam rate is a diagnostic signal for upstream reduction
  consistency — rising jam rate indicates reduction output
  is outside the gate's design envelope

**Failure Modes & Detection** — Bearing wear presents as vibration
signature changes before catastrophic failure. Spectroscopy drift
presents as rising Unknown Bulk rate. Both are detectable before
failure if monitored.

**Enclosure Fail-Stop and Containment:**
- Enclosure is the primary fragment containment barrier —
  integrity must be verified before each operational run
- Enclosure retention expectation: contain fragments from
  rotor failure at maximum operating RPM *(Placeholder —
  containment specification not yet defined; see MG-006)*
- Automatic RPM collapse condition: any vibration signature
  exceeding defined threshold triggers immediate RPM reduction
  to zero — do not attempt to hold speed through imbalance event
- Post-failure safe state: rotor stopped, power isolated,
  enclosure intact, operator notified before any access
- Containment failure is an unacceptable failure mode —
  design enclosure with sacrificial energy-absorbing elements
  rather than rigid containment alone

**Maintenance Access** — Bearing replacement and collection zone
clearing are primary service tasks. Modular drum design allows
hot-swap in swarm configurations.

**End-of-Life / Recycling Path** — Gate components are themselves
candidates for Forge intake. Magnetic bearing assemblies are
Class A salvage priority.

---

## Explicit Non-Goals (v0)

- Achieving high-purity metal output
- Replacing smelting or electrorefining
- Handling powdered feedstock
- Solving all alloy separation problems

---

## Integration Hooks

- `Architecture/Forge_flow.md` — governing operational flow; gate
  operates within Purification stage
- `Operations/Gate_05_Separation_Thermal.md` — receives Class C
  bulk output; this gate reduces its thermal load
- `Operations/Gate_02_Triage.md` — receives Unknown Bulk for
  human or assisted review
- `Operations/Air_Scrubber.md` — receives exhaust from high-RPM
  operation
- `Operations/Energy.md` — energy reduction claims require
  cross-validation
- `Tests/Leviathan_testing.md` — aquatic deployment unknowns
  routed here
- `Tests/Support_Raft.md` — thermal sink for heat pipe output
  in marine configurations
- `Architecture/Facilities.md` — siting and clearance requirements
  (FA-001)

**CLF-011 acknowledgment (2026-08-14):** this gate is required to
emit the `fir_class` batch field (per
`Challenges/Closed_Loop_Feedstock.md` §4a Integration Hooks / §4b)
on outbound batches, orthogonal to this gate's own sorting
Class A/B/C/Unknown Bulk/Fail. **Not implemented** — no emit logic
exists in this file. This note is acknowledgment of the obligation
only; CLF-011 remains Open until Path A (real batch evidence) or
Path B (human contract-acceptance) is taken per §4b.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | File operated under name Stratification_Chamber_v0.md | Name implied a specific physical method (stratification) rather than the function being performed (mechanical separation decision) | Renamed to Material_Separation_Gate_v0.md. Name change reflects function over method — the gate separates material by mechanical means regardless of specific implementation. Stale references to Stratification_Chamber_v0.md in other files should be updated; see cross-reference list at bottom of original document | Analogous | No — rename is complete; cross-references require sweep |
| 2026-05-15 | Audit Review | RPM range framed as defined operating band | Implied false precision — actual behavior depends heavily on feedstock geometry, ductility, and contamination | RPM range reframed as exploration band. Stratification noted as emergent behavior, not deterministic output. Band assignments treated as probabilistic heuristics | Analogous | Yes — empirical RPM sweep during v0 testing |
| 2026-05-15 | Audit Review | Unknown Bulk treated as failure output | Created pressure to minimize Unknown Bulk routing, risking downstream contamination | Unknown Bulk loop closure added — unresolved Unknown Bulk routes to Component_Triage_System.md or reduction retry. Unknown Bulk accumulation is diagnostic signal, not system fault | Analogous | No |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | "Purification stage" terminology may cause semantic overlap with `Operations/Gate_05_Separation_Thermal.md` | Position A: Gate sits within Purification stage per `Architecture/Forge_flow.md` definition ("any mechanism achieving comparable separation output"). Position B: Gate does not purify in metallurgical terms — should be called "Mechanical Diversion Stage" or "Pre-Thermal Classification Stage" to avoid confusion | Low | Open | `Architecture/Forge_flow.md` |

*DS-001 is a cross-module terminology question. Resolution belongs
in `Architecture/Forge_flow.md` — if the flow document's Purification
definition is revised to exclude mechanical diversion, this file's
position statement must be updated to match. No unilateral change
made here. Logged following ChatGPT audit 2026-05-15.*

---

## Auditor Notes & Unknowns

### MG-001 — Quantitative energy reduction estimate not established

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-08-14                                       |

**Description:** Quantitative energy reduction from mechanical
separation vs. thermal processing has not been established.
Directional improvement is assumed but not measured.

**Why It Matters:** The gate's core economic justification is
avoided thermal processing. Without a quantitative baseline,
the energy-positive claim cannot be verified or falsified.

**Resolution Path:**
- Deferred to experimental baseline against `Operations/Energy.md`
  kWh/kg metric.
- Resolution requires Leviathan test cycle data or terrestrial
  pilot run with instrumented energy measurement.
- Payment via Specification — once baseline established, move
  quantified claim to Body as Measured.

**Claude review 2026-08-14:** Path adequate. Correctly identifies
this as the gate's core economic claim and correctly refuses to
assert it as measured. **Approved (path adequate).** Remains Open
— needs Leviathan/pilot instrumented data; not agent-closable.

---

### MG-002 — Optimal RPM exploration bands not characterized per feedstock

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-08-14                                       |

**Description:** Optimal RPM bands for mixed municipal vs.
industrial scrap profiles have not been characterized. The
1,000–5,000 RPM exploration band is Analogous, not validated.

**Why It Matters:** RPM band selection directly governs
stratification behavior. An incorrect band produces poor
separation and elevated Unknown Bulk rates without revealing
the cause. Feedstock variation means a single RPM band may
not be optimal across all input classes.

**Resolution Path:**
- Incremental RPM sweep during v0 testing against known
  feedstock samples.
- Map separation quality vs. RPM for at least three distinct
  feedstock classes (ferrous, aluminum-class, mixed).
- Payment via Specification — once optimal bands per feedstock
  class are characterized, move to Body as Measured.

**Claude review 2026-08-14:** Path adequate. Three-class sweep is
a concrete, testable minimum; correctly flags the current band as
Analogous rather than asserting it as validated. **Approved (path
adequate).** Remains Open — needs v0 sweep data.

---

### MG-003 — Confidence threshold calibration not empirically validated

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-08-14                                       |

**Description:** The 90% confidence threshold for Unknown Bulk
routing has not been validated against known feedstock samples.
The threshold is a design intent value, not an empirically
derived one.

**Why It Matters:** The confidence threshold governs every
routing decision the gate makes. A threshold set too high
floods Unknown Bulk with recoverable material. A threshold
set too low passes ambiguous material downstream, risking
contamination. This is the most operationally sensitive
parameter in the gate.

**Resolution Path:**
- Controlled classification trials against known feedstock
  samples with ground-truth composition data.
- Sweep threshold from 70% to 95% and measure false
  positive and false negative rates at each level.
- Select threshold that minimizes downstream contamination
  risk while maintaining acceptable Unknown Bulk rate.
- Payment via Specification — once empirically validated,
  move confirmed threshold to Body as Measured.

**Claude review 2026-08-14:** Path adequate. Correctly identifies
this as the most operationally sensitive parameter in the gate and
resists just picking a defensible-sounding number — a false
positive/negative sweep against ground-truth samples is the right
method. **Approved (path adequate).** Remains Open — this is exactly
the kind of numeric threshold that must not be set on prose alone.

---

### MG-004 — Geometry correction algorithm not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-08-14                                       |

**Description:** The inertia/optical cross-reference algorithm
for geometry correction — preventing misclassification of
light-but-dense or heavy-but-thin materials — is not yet
specified. The need is identified but the implementation
is undefined.

**Why It Matters:** Without geometry correction, materials
like aluminum foil can be silently routed to the polymer
stream. This is a known failure mode that the sensor
cross-check is supposed to prevent — but cannot prevent
without a specified algorithm.

**Resolution Path:**
- Analog centrifuge separation literature review to identify
  existing correction approaches.
- Prototype sensor calibration trials with known edge-case
  materials (aluminum foil, thin steel sheet, dense polymer).
- Algorithm specification is a prerequisite for sensor
  cross-check to function as designed.
- Payment via Specification — once algorithm is specified
  and validated, move to Body as Measured.

**Claude review 2026-08-14:** Path adequate. Correctly sequences
literature review before prototype trials, and correctly names this
as a hard prerequisite for the sensor cross-check rather than a nice-
to-have. Named edge cases (foil, thin steel, dense polymer) are the
right adversarial test set. **Approved (path adequate).** Remains
Open — algorithm still needs to be specified and validated.

---

### MG-005 — Long-term aquatic biofouling impact on rotor balance

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-08-14                                       |

**Description:** Long-term aquatic biofouling impact on rotor
balance and bearing performance in Leviathan deployments has
not been characterized.

**Why It Matters:** Biofouling creates asymmetric mass
accumulation on rotating components — a direct imbalance
source at operating RPM. In marine deployments this could
progressively degrade separation quality and accelerate
bearing failure without obvious external symptoms.

**Resolution Path:**
- Discharge via Trajectory — route to `Tests/Leviathan_testing.md`
  for marine deployment test framework.
- Not relevant to terrestrial v0 validation.

**Claude review 2026-08-14:** Path adequate. `Tests/Leviathan_testing.md`
confirmed to exist — discharge target is real, not invented. Correctly
scoped out of terrestrial v0. **Approved (path adequate).** Remains
Open — this file does not own marine-deployment resolution.

---

### MG-006 — Operational siting and area-of-operation requirements not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Ethical                              |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md (seed entry)      |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** No facility, siting, or area-of-operation
document exists to govern physical separation requirements,
clearance zones, or operator safety protocols during
high-RPM rotating states.

**Why It Matters:** The gate operates at 1,000–5,000 RPM
with unknown-geometry feedstock. Fragment ejection and
rotor failure are credible hazards. The safety advisory
states the enclosure requirement but no governing document
defines clearance distances, enclosure specifications, or
operator protocols.

**Resolution Path:**
- Seed entry for future master safety registry — mirrors
  SC-006 in `Operations/Gate_05_Separation_Thermal.md`.
- Not blocking v0 specification work but must be resolved
  before any operational run.
- Recommend cross-module tracking alongside SC-006 in
  `Unknowns.md` — siting requirements affect all rotating
  and thermal modules in the Forge. UNK-006 resolved —
  `Architecture/Facilities.md` now owns siting doctrine.
- Discharge via Trajectory for marine and off-world variants.
- Payment via Specification for terrestrial v0 baseline
  once siting document exists.

**Claude review 2026-08-14:** Path adequate. `Architecture/Facilities.md`
confirmed to exist and confirmed to explicitly claim ownership of
UNK-006 (its own text: "resolve UNK-006 — the facility siting unknown
referenced by seven [files]"). Cross-reference is real, not invented.
**Approved (path adequate).** Remains Open — correctly Blocking-No
for spec work, but this file's own text is right that it must be
resolved before any operational run; that gate belongs to
Facilities.md, not here.

---

### MG-007 — Rotor jam and entanglement recovery behavior undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** Rotor jam detection thresholds, automatic shutdown
conditions, and manual clearing protocols are not yet defined.
Unknown-geometry feedstock makes jam and entanglement credible
operational conditions.

**Why It Matters:** A jammed rotor without a defined response
protocol risks operator injury during manual clearing, bearing
damage from prolonged stall current, and enclosure integrity
failure if the rotor seizes under load. The feedstock envelope
provisional constraints (Inputs section) identify high-risk
geometries but do not substitute for a clearing doctrine.

**Resolution Path:**
- Define motor current jam threshold based on drive system
  specification — requires drive system to be specified first.
- Establish automatic shutdown trigger: sustained current
  above threshold for defined duration.
- Document manual clearing protocol with explicit lockout
  requirement before any physical access.
- Provisional feedstock envelope constraints (Inputs section)
  reduce jam frequency — treat as complementary, not substitute.
- Payment via Specification — once jam thresholds, shutdown
  triggers, and clearing protocol are defined and tested,
  move to Lifecycle section as Measured.

**Claude review 2026-08-14:** Path adequate and correctly ordered
— jam threshold honestly depends on drive system spec existing
first, not treated as independently definable. Lockout-before-
access requirement is the correct safety-critical default.
**Approved (path adequate).** Remains Open — blocked on drive
system specification; do not write a jam threshold number ahead
of that.

---

### MG-008 — Sensor fouling from conductive or abrasive fines

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_04_Separation_Mechanical.md                   |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** Mixed scrap at high RPM generates conductive dust
and abrasive fines that can coat optical sensors and silently
degrade confidence scoring, inflating Unknown Bulk rate without
revealing the cause.

**Why It Matters:** Sensor fouling is a silent failure mode —
it degrades classification quality gradually rather than
producing a clear fault signal. If fouling is mistaken for
feedstock ambiguity, the response (tightening thresholds,
increasing Unknown Bulk routing) treats the symptom rather
than the cause. Over time this could make the gate appear
increasingly unreliable when the actual problem is maintenance.

**Resolution Path:**
- Establish sensor cleaning interval during Gen-0 testing —
  start with post-run cleaning and adjust based on observed
  fouling rate.
- Sensor housing design must include particulate ingress
  protection — specify before first operational run.
- Rising Unknown Bulk rate is the primary detection signal —
  distinguish fouling from calibration drift (MG-003) by
  cleaning sensors and observing recovery.
- Cross-reference `Operations/Air_Scrubber.md` — particulate burden
  must be included in scrubber intake specification.
- Payment via Specification — once fouling rate is
  characterized and cleaning interval established, move
  to Sensor Cross-Check section as Measured.

**Claude review 2026-08-14:** Path adequate. Explicitly distinguishing
this from MG-003 (calibration drift) rather than letting the two
silent-failure modes get conflated is the right move — same symptom
(rising Unknown Bulk), different cause, different fix. Cross-reference
to Air_Scrubber.md is sound. **Approved (path adequate).** Remains
Open — cleaning interval and housing spec still need Gen-0 data.

---

### Resolution Log

- 2026-08-14: **Claude resolution-path review (Round 4 — Operations,
  continuing the sequence from Grok's Rounds 1-3).** All eight MG
  unknowns reviewed against source. Every Resolution Path judged
  adequate; two embedded cross-reference claims (MG-005 →
  `Tests/Leviathan_testing.md`, MG-006 → `Architecture/Facilities.md`
  UNK-006 ownership) checked against the actual files, not accepted
  on the sidecar's word — both confirmed real. Markers added under
  each path; Last Reviewed → 2026-08-14 on all eight. **No MG-*
  closed.** Open Unknowns remain 8. Blocking status unchanged (all
  No). Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **8** = MG-001–008, matches local +
  `Unknowns.md`. (2) No Blocking understatement of operational-safety type.
  (3) MG-006 siting gap mirrors SC-006 (noted, not escalated this pass).
  (4) No MG-* closed. Human-directed.

- 2026-05-15: MG-001 through MG-005 — Migrated from prose
  Unknowns Registry to structured sidecar format. Content
  preserved; format updated to template standard.
- 2026-05-15: MG-006 — New entry. Siting and safety
  requirements gap identified during retrofit audit.
  Mirrors SC-006 in Spin_Chamber_v0.md. Recommend
  cross-module UNK escalation alongside SC-006.
- 2026-05-15: MG-007 — New entry. Rotor jam and entanglement
  recovery behavior undefined. Logged following Grok and
  ChatGPT independent audit convergence.
- 2026-05-15: MG-008 — New entry. Sensor fouling from
  conductive and abrasive fines. Silent failure mode
  identified by ChatGPT audit. Sensor fouling doctrine
  added to Sensor Cross-Check section.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | File named Stratification_Chamber_v0.md | Name implied a specific physical method rather than the function being performed. Caused semantic confusion about what the module owned and how it related to the Spin Chamber | No — rename to Material_Separation_Gate_v0.md is permanent |
| 2026-05-15 | Electromagnetic field bias in v0 spec | Adds complexity without validated benefit at v0 scale and power budget. Correctly deferred — must never force separation beyond observable stability | Reconsider at v1+ when power budget and field geometry can be specified |
| 2026-05-15 | Single large gate as scaling strategy | Enlargement creates single point of failure, increases maintenance burden, and reduces tunability per feedstock class. Replication preserves modularity and forces component standardization | Reconsider if replication produces coordination or interference problems at swarm scale — see ASM-006 |
| 2026-05-15 | Powder feedstock handling | Requires fundamentally different separation physics — aerodynamic and electrostatic rather than centrifugal and inertial. Out of scope for all v0 rotating drum implementations | Reconsider only as a distinct module, never as an extension of this gate |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of this file.
All canonical drift indicators from File_Template.md apply.
The following are additional local triggers specific to the
Material Separation Gate:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| MG-003 remains unreviewed after first operational run | Confidence threshold governs every routing decision — operational data must feed back immediately |
| RPM band revised without MG-002 resolution | Empirical RPM mapping is prerequisite for any band change |
| Bearing or rotor specified with non-standard components without documented justification | Standardization doctrine applies — bespoke components require explicit override |
| Safety Advisory conditions change without MG-006 update | Enclosure requirements and advisory must stay synchronized |
| Unknown Bulk rate rises without sensor calibration review | Rising Unknown Bulk is diagnostic signal — must trigger MG-003 and MG-004 review before operational changes |
| Feedstock class expands beyond non-powdered reduced metallic without assumptions review | ASM-001 expiry trigger — particle envelope, RPM bands, and sensor calibration all change with feedstock class |
| Replication scaling abandoned in favor of enlargement without ASM-006 review | Core scaling doctrine — override requires explicit audit and documented justification |
| Geometry correction algorithm advanced without MG-004 resolution | Sensor cross-check cannot function as designed without specified algorithm |
| `Architecture/Forge_flow.md` revises Purification stage definition without DS-001 review | Gate's position in system flow depends on flow document definition — any change must propagate here |

### Canonical Drift Triggers

*All mandatory re-audit conditions from `Admin/File_Template.md`
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*

---

### Resolution Log

- 2026-05-15: MG-001 through MG-005 — Migrated from prose
  Unknowns Registry to structured sidecar format. Content
  preserved; format updated to template standard.
- 2026-05-15: MG-006 — New entry. Siting and safety
  requirements gap identified during retrofit audit.
  Mirrors SC-006 in Gate_05_Separation_Thermal.md. Cross-module
  UNK escalation recommended alongside SC-006.
- 2026-05-15: MG-007 — New entry. Rotor jam and entanglement
  recovery behavior undefined. Logged following Grok and
  ChatGPT independent audit convergence.
- 2026-05-15: MG-008 — New entry. Sensor fouling from
  conductive and abrasive fines. Silent failure mode
  identified by ChatGPT audit. Sensor fouling doctrine
  added to Sensor Cross-Check section.
- 2026-06-08: Navigation Anchors block added. Title corrected
  from `Material Separation Gate (v0)` to
  `Gate_04_Separation_Mechanical`. Verification Ref corrected
  from `Forge_Audit_Kit.md` to `Admin/Verification_Gates.md`
  (PC-001). Facilities.md upstream reference added to Scope
  Boundary and Integration Hooks (PC-002). All stale filenames
  corrected throughout: Spin_Chamber_v0.md →
  Gate_05_Separation_Thermal.md, Component_Triage_System.md →
  Gate_02_Triage.md, Air_Scrubber_v0.md → Air_Scrubber.md,
  energy_v0.md → Energy.md, Support_Raft_v0.md →
  Support_Raft.md, leviathan_testing.md →
  Leviathan_testing.md, Trajectories_LF.md → Trajectories.md,
  Lazarus_forge_v0_flow.md → Forge_flow.md. Sidecar Owner
  fields corrected from Material_Separation_Gate_v0.md to
  Operations/Gate_04_Separation_Mechanical.md. MG-006
  resolution path updated — UNK-006 resolved by
  Architecture/Facilities.md.
