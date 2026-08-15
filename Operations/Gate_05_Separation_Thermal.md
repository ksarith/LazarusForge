# Gate_05_Separation_Thermal

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> The Spin Chamber operates with molten metal under rotation. Breach, splash,
> and projectile hazards are credible failure modes during all hot and rotating
> states. Physical separation from living organisms and sensitive components is
> required during operation. Siting and clearance requirements are not yet
> governed by a facility or area-of-operation document — see SC-006.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-08 (Scope Boundary DOES-NOT wording corrected to match Lessons Learned); prior: 2026-07-31 (SC-009 registered; SC-004 expanded with Driving Mechanism Options) |
| Auditor          | Claude — Retrofit/Auditor; Claude — Synthesizer, human-directed (SC-009, SC-004 expansion), 2026-07-31 |
| Open Unknowns    | 9                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Operating principle and design intent of the Spin Chamber
- Physical geometry and scale envelope (v0)
- Materials selection for crucible and outer shell
- Rotation system parameters and drive philosophy
- Heating strategy and thermal operating bands
- Electromagnetic field approach and limitations
- Atmosphere control approach
- Extraction interfaces and output categories, including
  wire extrusion as a planned interface for welding wire production
- Instrumentation and control philosophy
- Failure philosophy and acceptable/unacceptable failure modes
- The Spin Chamber's role as a material contributor to
  self-replication (not the self-replication architecture itself)

**This file DOES NOT define:**
- Upstream feedstock preparation
  (`Operations/Gate_03_Reduction.md`)
- Mechanical separation decisions
  (`Operations/Gate_04_Separation_Mechanical.md`)
- Wire extrusion nozzle design
  (deferred — `Admin/Trajectories.md`)
- Welding wire specification or qualification
  (`Architecture/Geck_forge_seed.md`, UNK-008 — ownership
  reassigned 2026-07-19, already correctly cited in this
  file's own Lessons Learned table)
- Self-replication architecture or loop closure logic
  (`Architecture/Forge_flow.md`,
  `Architecture/Geck_forge_seed.md`)
- Facility siting, clearance, and area-of-operation
  requirements (`Architecture/Facilities.md` — FA-001)
- MHD auxiliary coil detailed specification
  (deferred — `Admin/Trajectories.md`)
- Drive system detailed geometry
  (SC-005 — prerequisite for dynamic analysis)
- Energy accounting and kWh/kg metrics
  (`Operations/Energy.md`)

---

## File Purpose

The Spin Chamber is the primary thermal processing module of the Lazarus Forge.
It receives metallic feedstock from the Material Separation Gate and converts it
into ranked material streams through the combined application of induction heating,
slow rotation, and electromagnetic field stabilization. Its outputs feed structural
fabrication, component upgrades, and — through a planned wire extrusion interface —
welding wire production as a pathway toward self-replication.

The chamber is designed for long operational life, predictable behavior, and
modular repair. It prioritizes survivability and consistency over throughput or
purity. It is not the only path to thermal processing within the Forge, but it
is the most elegant one — combining multiple physical biases into a single
patient system rather than requiring separate stages. If this file disappeared,
thermal processing would require more complex, less integrated alternatives.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Grid or equivalent power (5–15kW) is available at bootstrap | v0 site context | Medium | Off-grid or power-constrained deployment confirmed |
| ASM-002 | Feedstock is whatever salvage stock is available; single-stock runs preferred to minimize cross-contamination; aluminum expected as easiest starting material | Metallurgical practice, v0 scope | Medium | Multi-stock processing validated or intentionally adopted |
| ASM-003 | v0 operating environment is terrestrial | No marine or vacuum provisions in v0 spec | Medium | Leviathan or off-world deployment enters scope |
| ASM-004 | Manual operator presence during operation | Control philosophy assumes human response to threshold alerts | Medium | Automated shutdown and monitoring validated |
| ASM-005 | Graphite crucible stock is obtainable through salvage, commercial supply, or inter-forge trade at bootstrap | Purchase-what-cannot-be-produced doctrine; forge ecology context | Low | Local fabrication of crucibles demonstrated |
| ASM-006 | Induction coils can be sourced, purchased, or obtained through inter-forge trade at v0 bootstrap | Purchase-what-cannot-be-produced doctrine; not all forges produce everything | Low | Coil self-fabrication demonstrated |

*Low confidence assumptions reflect resolution paths that vary by forge
instance and deployment context, not critical failure points.
Purchase-what-cannot-be-produced doctrine and inter-forge trade
are valid resolution paths. See README.md and
`Admin/Trajectories.md` for forge ecology context.*

---

## 1. Purpose

The Spin Chamber is the keystone module of Lazarus Forge. It converts mixed metallic
scrap into **ranked material streams** using overlapping physical biases (heat, rotation,
and electromagnetic fields). The goal is *progressive enrichment* and *capability
replication*, not single-pass purity.

This v0 design prioritizes:

- Long operational life
- Predictable behavior
- Modular repair
- Bootstrap compatibility (built from salvage, improves itself over generations)

---

## 2. Operating Principle

1. **Induction melting** homogenizes incoming scrap
2. **Slow rotation** biases the melt radially by density
3. **Magnetohydrodynamic (MHD) damping** stabilizes flow and suppresses turbulence
4. **Time under bias** allows impurities to migrate and segregate
5. **Selective extraction** (tapping / extrusion) routes material by role

The chamber does not aim to produce "pure metal." It produces **useful gradients**.

---

## 3. System Overview

**Stationary outer shell**
- Structural containment
- Thermal insulation
- Houses coils and sensors

**Rotating inner crucible**
- Contains molten metal
- Provides centrifugal bias

**External induction coils**
- Heat source
- Optional MHD field shaping

**Drive module**
- Low RPM rotation
- High tolerance to imbalance

**Extraction interfaces**
- Slag skim
- Radial taps (optional)
- Centerline wire extrusion (future-ready)

---

## 4. Scale & Geometry (v0 Envelope)

- **Internal diameter:** 200–250 mm *(Analogous — derived from small induction furnace commercial offerings)*
- **Internal height:** 200–300 mm *(Analogous)*
- **Melt volume:** 5–10 L *(Analogous)*
- **Batch mass:** ~10–25 kg Al class *(Analogous)*

**Crucible geometry:**
- Rounded conical or shallow paraboloid bottom
- No flat surfaces
- Generous radii to avoid dead zones

**Wall thickness:**
- Graphite: 10–15 mm *(Analogous)*
- Ceramic: 15–25 mm *(Analogous)*

---

## 5. Materials

**Crucible (v0):**
- Graphite (preferred; sacrificial, forgiving)
- Alumina / mullite ceramics (acceptable)

**Outer shell:**
- Refractory liner
- Insulation layer
- Structural steel jacket

**Design note:** Wear is acceptable. Sudden failure is not.

---

## 6. Rotation System

- **Operating RPM:** 50–300 *(Placeholder — bounds derived from first principles, not tested)*
- **Nominal RPM:** 100–150 *(Placeholder)*
- **Never exceed (v0):** 400 *(Simulated — centrifugal pressure and hoop stress
  calculated 2026-05-15; safety factor ~32× at worst-case inputs. Binding constraint
  is dynamic imbalance, not wall integrity. See SC-005 and Lessons Learned 2026-05-15)*

**Drive philosophy:**
- External motor
- Belt or chain drive
- Slip or clutch preferred
- Alignment by geometry, not precision machining
- Component standardization required — bearing sizes, shaft diameters, and fastener
  standards must be drawn from a minimal shared set to support inter-forge
  interchangeability and repair. See SC-005.

---

## 7. Heating & Thermal Strategy

**Heating:**
- External induction coils
- Single zone acceptable for v0
- Power range: 5–15 kW *(Analogous — small induction furnace data)*

**Temperature bands (Al class):**
- Hot idle: 500–550 °C *(Analogous)*
- Processing: 650–720 °C *(Analogous)*

**Thermal doctrine:**
- Maintain near-constant elevated temperature
- Avoid full thermal cycling
- Stop rotation before cooling

This dramatically extends crucible and coil life.

---

## 8. Electromagnetic Fields (v0)

- No electrodes in melt
- No electrochemical assumptions
- Induction fields provide heating and incidental MHD effects
- Optional auxiliary coils for millitesla-scale flow damping *(Placeholder —
  effectiveness at v0 scale and power budget unverified. See SC-003)*

Purpose is **stability**, not forceful separation.

---

## 9. Atmosphere Control

- Passive reducing environment preferred
- Charcoal bed or inert purge if available
- Oxygen ingress minimized, not eliminated

Precision gas chemistry is out of scope for v0.

---

## 10. Extraction & Outputs

**Primary outputs:**
- Slag / oxide layer (skimmed)
- Bulk structural alloy
- Composition-biased inner fraction

**Wire extrusion (planned path):**
- Centerline bottom tap
- Heated, replaceable nozzle
- Diameter controlled by draw speed
- Purpose: welding wire production as a direct pathway toward self-replication
- Nozzle design deferred to v1 scope — see SC-004

Wire is the preferred first product for self-replication.

**CLF-011 acknowledgment (2026-08-14):** this gate is required to
emit the `fir_class` batch field (per
`Challenges/Closed_Loop_Feedstock.md` §4a Integration Hooks / §4b)
on outbound batches. **Not implemented** — no emit logic exists in
this file. This note is acknowledgment of the obligation only;
CLF-011 remains Open until Path A (real batch evidence) or Path B
(human contract-acceptance) is taken per §4b.

---

## 11. Instrumentation & Control

**Required sensing:**
- Temperature (2–3 points)
- Motor current
- Induction power draw
- Vibration (coarse accelerometer acceptable)

**Control philosophy:**
- Thresholds and states
- Slow ramps
- Long dwell times

Example rule:
> If vibration increases for 10 minutes, reduce RPM.

---

## 12. Operating Mode

- Batch operation
- Long holds (hours, not minutes)
- Hot idle between runs

Speed is never a success metric.

---

## 13. Expected Outcomes (v0)

**Expect:**
- Predictable segregation trends
- Improved consistency over time
- Learnable wear patterns

**Do not expect:**
- High purity
- High throughput
- Cosmetic perfection

If behavior is stable and repeatable, the chamber is successful.

---

## 14. Failure Philosophy

Acceptable:
- Crucible wear
- Slag buildup
- Gradual vibration drift

Unacceptable:
- Runaway RPM
- Melt breach
- Explosive failure

Design to fail **slowly and visibly**.

---

## 15. Role in Self-Replicating Foundry Logic

The Spin Chamber is a **material contributor** to the self-replicating foundry loop.
Its outputs feed:
- Structural fabrication
- Coil and motor upgrades
- Thermal and refractory improvements
- Welding wire production via planned extrusion interface

Each generation improves the next. Older chambers remain useful. Self-replication
architecture and loop closure logic are governed by `Architecture/Forge_flow.md` and
`Architecture/Geck_forge_seed.md` — not this file.

---

## 16. Summary

The Spin Chamber is not a purifier. It is a patient system that nudges matter
toward order using time, gravity, and fields.

> **Slow spin. Hot idle. Long life.**

This is the tortoise.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Modeling | Back-of-envelope centrifugal pressure and hoop stress calculation for 400 RPM never-exceed at worst-case v0 geometry | Nothing failed — calculation ran cleanly | At 400 RPM, worst-case centrifugal pressure on the crucible wall is ~0.037 MPa, producing ~0.463 MPa hoop stress against a 15 MPa graphite allowable. Safety factor ~32×. The never-exceed is not the binding constraint — thermal shock and dynamic imbalance are. See SC-001, SC-005 | Simulated | Yes — cold water analog test before first hot run |

### Reference Equations — Centrifugal Pressure and Hoop Stress

For future RPM limit evaluation, the governing equations are:

**Centrifugal pressure from rotating melt:**
P = ½ × ρ × ω² × r²

**Hoop stress in crucible wall:**
σ_hoop = P × r / t

**Angular velocity conversion:**
ω (rad/s) = RPM × (2π / 60)

**Variables:**
- ρ = melt density (kg/m³) — Al class: 2,700 kg/m³
- ω = angular velocity (rad/s)
- r = internal radius (m)
- t = wall thickness (m)
- P = pressure at wall (Pa)
- σ_hoop = hoop stress (Pa)

**v0 worst-case inputs:**
- r = 0.125m, t = 0.010m, ρ = 2,700 kg/m³, RPM = 400
- Result: Safety factor ~32× against weakest graphite grade (15 MPa)

If pushing beyond 400 RPM in future versions, re-run with updated
geometry, confirmed graphite grade tensile strength, and dynamic
imbalance analysis (SC-005) before revising the never-exceed value.
*Cross-reference: SC-001, SC-005*

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts are currently active. Several design tensions
exist (MHD damping scope, crucible material selection, RPM operating band)
but all are deferred pending operational data rather than representing
genuine disagreements between positions. These are tracked as unknowns
in the sidecar, not disputes. Revisit after first operational run.*

---

## Auditor Notes & Unknowns

### SC-001 — RPM envelope validation

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Whether the 50–400 RPM operating envelope is safe and
effective for the specified geometry and melt mass.

**Why It Matters:** An unvalidated never-exceed value provides false
confidence. Exceeding safe RPM with molten contents risks melt breach —
an unacceptable failure mode per the failure philosophy.

**Resolution Path:**
- Static centrifugal pressure and hoop stress calculated 2026-05-15.
  Safety factor ~32× at worst-case inputs. Never-exceed of 400 RPM is
  not the binding constraint on wall integrity. See Lessons Learned
  entry 2026-05-15 for equations and inputs.
- Binding constraints identified as thermal shock and dynamic imbalance
  — dynamic analysis deferred to SC-005 pending drive system specification.
- Cold water analog test remains required before first hot run. Purpose
  is now specifically to validate balance and vibration behavior, not
  wall integrity.
- Payment via Specification — once analog test completes and drive system
  is specified, move validated envelope to Body.

**Claude review 2026-08-14:** Path adequate. Static analysis is real
work already done (not asserted, calculated), and the file correctly
narrows what's still open (thermal shock, dynamic imbalance) rather
than treating the whole envelope as unvalidated. **Approved (path
adequate).** Correctly In Progress, not Open — some resolution exists,
cold-water analog test still required before hot run.

---

### SC-002 — Segregation effectiveness at v0 scale unverified

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Critical                       |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Whether meaningful density-based segregation is
achievable at 5–10L melt volume and 100–150 RPM nominal operating
band in a v0 geometry crucible.

**Why It Matters:** Segregation effectiveness is the core claim of
the Spin Chamber. If meaningful gradients do not form at v0 scale
and RPM, the chamber's primary value proposition is undemonstrated.
The Forge can still process material thermally, but the ranked
material stream output becomes bulk melt — a significant capability
reduction.

**Resolution Path:**
- Literature search for small-scale centrifugal casting and rotary
  furnace analog data at similar volumes and RPM bands. If analog
  data exists, upgrade confidence label from Placeholder to Analogous.
- If no analog data found, flag as Placeholder until first operational
  run produces gradient measurement data.
- Cold water analog test (see SC-001) can provide early qualitative
  evidence of radial stratification behavior before first hot run.
- Payment via Specification — once operational gradient data exists
  and is consistent across multiple runs, move validated segregation
  parameters to Body as Measured.
- This is the highest priority validation for the chamber's core claim
  and should be treated as the primary success metric for Gen-0
  operational testing.

**Claude review 2026-08-14:** Path adequate. Correctly named as the
file's core unresolved claim (Critical, matches the chamber's actual
value proposition) rather than buried among lower-stakes items.
**Approved (path adequate).** Remains Open — this is exactly the kind
of claim that needs first-operational-run data, not agent-closable.

---

### SC-003 — MHD damping effectiveness at v0 power levels

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Whether millitesla-scale auxiliary fields provide
meaningful flow damping at v0 scale and power budget, or negligible
effect.

**Why It Matters:** If MHD damping provides no measurable benefit at
v0 scale, retaining it in the specification adds complexity without
return. Removing it simplifies the v0 build and defers the capability
honestly to a higher-power future version.

**Resolution Path:**
- MHD damping is correctly marked optional in the body. No action
  required before first operational run.
- During Gen-0 testing, run comparative holds with and without
  auxiliary coil activation. Look for measurable difference in
  vibration signature, segregation consistency, or melt stability.
- If no measurable benefit observed at v0 scale: discharge via
  Trajectory — route full MHD specification to `Admin/Trajectories.md`
  for higher-power future versions. Remove optional language from
  v0 body to reduce complexity.
- If measurable benefit observed: Payment via Specification —
  document effective field strength and coil configuration in Body
  as Measured.

**Claude review 2026-08-14:** Path adequate. Honestly bidirectional —
specifies what happens whether the test finds benefit or doesn't,
rather than assuming the outcome. Correctly Minor/Low risk since MHD
is already optional. **Approved (path adequate).** Remains Open —
needs the comparative Gen-0 hold-test data either way.

---

### SC-004 — Wire extrusion nozzle design not specified

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Nozzle material, geometry, replacement interval,
and draw speed control method for the centerline wire extrusion
path are not yet specified.

**Why It Matters:** Wire extrusion is the planned first product
for welding wire production and a direct pathway toward
self-replication. Without a nozzle specification, the extrusion
interface remains a placeholder and the self-replication pathway
it enables cannot be validated or built toward deliberately.

**Driving Mechanism Options (added 2026-07-31):** The interface
above specifies *what* the wire path looks like (centerline tap,
heated replaceable nozzle, draw-speed diameter control) but not
*what force* drives melt through it. Five candidate mechanisms,
ranked by near-term fit:

| Mechanism | Fit | CLF-003 (die/nozzle wear) relevance |
|---|---|---|
| Centrifugal / spin-driven | Strongest v0–v1 fit — uses existing rotation, no new pump; pressure scales with RPM² within the existing 50–400 RPM envelope (SC-001) | Nozzle still under continuous centrifugal + thermal load |
| Gas-pressure (inert-gas head) | Simple, modulable; adds a consumable-gas dependency | Same die-wear exposure as centrifugal |
| Electromagnetic / MHD pumping | Contactless; synergizes with existing induction coils and optional MHD damping; needed for reactive metals in vacuum | Removes mechanical die contact — CLF-003 exposure drops sharply |
| Mechanical piston/ram or screw | High pressure, mature tech, handles particulate/semi-solid feed | Highest CLF-003 exposure — moving parts in molten-metal contact |
| Hybrid continuous-cast + downstream draw (including **dieless drawing**) | Separates the hard molten-nozzle problem from final sizing; dieless drawing (induction-zone softening + velocity-ratio-controlled reduction) is demonstrated on titanium at 30–54% area reduction per pass and eliminates die contact for the sizing stage entirely | Removes the die-wear problem at its root for the sizing stage, not just tolerates it |

Recommended sequencing: centrifugal (+ optional gas assist) for v0
aluminum-class wire; centrifugal + MHD assist as wire maturity
increases; MHD/EM-levitation-driven once reactive metals require
vacuum-compatible, containerless processing (see SC-009). Dieless
drawing is the strongest CLF-003 mitigation for the metal-wire path
specifically — CLF-003's own text describes dieless drawing as
removing die contact from the metal-wire path entirely, rather than
merely tolerating wear on it. This does not touch CLF-003's
polymer-extrusion half, which has no equivalent dieless option.
A minimal experimental dieless-drawing configuration is parked at
`Admin/Trajectories.md` TR-MET-003 (v1 scope, not v0). Astroid-miner's
`Propulsion_Economy_isru/zero_g_fabrication.md` independently lists
"Spun Conical Ceramic Extrusion" (centrifugal) as its stated primary
wire source — consistent with the same centrifugal-first sequencing
recommended here for terrestrial v0.

**Resolution Path:**
- Wire extrusion is correctly marked future-ready in the body
  for v0. No action required before first operational run.
- Nozzle design is a v1 specification task, triggered when:
  1. Spin Chamber Gen-0 operational run demonstrates stable
     melt output
  2. Welding wire specification and qualification requirements
     are defined (currently unowned — see cross-module gap
     noted in Scope Boundary)
  3. Draw speed control method is selected and integrated
     with instrumentation spec
- Discharge via Trajectory — route full nozzle specification
  and driving-mechanism selection to `Admin/Trajectories.md` v1
  scope (see TR-MET-003 for the dieless-drawing experimental plan
  specifically).
- Payment via Specification — once nozzle design is validated
  and draw speed control demonstrated, move to Body as Measured.

**Claude review 2026-08-14:** Path adequate. One correction made
this pass: the Driving Mechanism Options section attributed a direct
quote to CLF-003 ("applies most strongly to any mechanical or
high-pressure contact die...") that does not exist verbatim anywhere
in CLF-003 or the repository — the substance was accurate (dieless
drawing does remove die contact per CLF-003's own text) but it was
presented as a quotation rather than paraphrase. Reworded to remove
the false quote attribution; no other change to the underlying claim.
TR-MET-002/003 cross-references in this section independently
verified against `Admin/Trajectories.md` — both real, phrasing
accurately reflects source. **Approved (path adequate) with
correction applied.** Remains Open — v1 task, correctly not v0
blocking.

---

### SC-005 — Drive system geometry not specified; dynamic imbalance analysis blocked

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-05-15                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Drive shaft geometry, bearing selection, mounting
stiffness, and critical speed are not specified. Dynamic imbalance
analysis cannot be completed without these inputs.

**Why It Matters:** Static analysis (SC-001, Lessons Learned
2026-05-15) confirms 32× wall integrity margin at 400 RPM. Dynamic
imbalance from asymmetric melt loading cycles at rotation frequency
and can excite resonance — at 20kg melt mass with 5mm eccentricity,
~175N cyclical force at 400 RPM. Acceptability depends on bearing
load rating and shaft stiffness, neither currently specified. An
undersized or non-standard component could produce progressive
failure that monitoring catches too late.

**Resolution Path:**
- When specifying drive system, select from a minimal set of
  standardized bearing sizes, shaft diameters, and fastener
  standards. Interchangeability across forge instances is a
  design requirement, not a preference. A bearing that can be
  sourced, replaced, or traded between forges is worth more
  than an optimal but bespoke one. Standardization is how the
  forge ecology scales.
- Calculate critical speed once shaft geometry is selected.
  Confirm operating RPM band sits below first critical frequency
  with adequate margin.
- Reference imbalance force equation: F = m × e × ω²
  where m = melt mass, e = eccentricity, ω = angular velocity.
  Run for worst-case eccentricity once crucible mounting is defined.
- Cold water analog test (SC-001) provides empirical imbalance
  data before full specification — treat results as design input,
  not just validation.
- Payment via Specification — once drive system is specified to
  standard components, critical speed calculated, and analog test
  data reviewed, move validated dynamic envelope to Body alongside
  RPM never-exceed.

**Claude review 2026-08-14:** Path adequate. The 175N cyclical-force
figure is shown as a worked calculation with stated inputs (mass,
eccentricity, RPM), not an asserted number — consistent with the
project's confidence-labeling discipline. Standardization-as-design-
requirement framing correctly ties this unknown to the forge
ecology's interchangeability goals, not just this one build.
**Approved (path adequate).** Remains Open — blocked on drive system
selection, same dependency SC-001 and MG-007 already carry.

---

### SC-006 — Operational siting and area-of-operation requirements not defined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical / Ethical            |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md (seed entry) |
| First Logged  | 2026-05-15                     |
| Last Reviewed | 2026-08-14                     |

**Description:** No facility, siting, or area-of-operation document
exists to govern physical separation requirements, clearance zones,
or operator safety protocols during hot and rotating states.

**Why It Matters:** The Spin Chamber operates with molten metal under
rotation. Breach, splash, and projectile hazards are credible failure
modes. The operational safety advisory at the top of this file states
the requirement for physical separation from living organisms and
sensitive components — but no governing document currently defines
what that separation looks like in practice, at what distances, or
under what conditions.

**Resolution Path:**
- `Architecture/Facilities.md` was created 2026-06-06 and now
  owns siting and clearance doctrine for all hot and rotating
  modules. This entry discharges by reference to FA-001 once
  the safety advisory is updated to cross-reference
  `Architecture/Facilities.md` and the Spin Chamber-specific
  siting requirements are documented there.
- Siting requirements vary by deployment context —
  terrestrial, marine (`Tests/Support_Raft.md`), and future
  off-world contexts each carry different constraints.
- UNK-006 resolved — `Unknowns.md` cross-module entry now
  routes to `Architecture/Facilities.md` as the governing
  siting document.
- Discharge via Trajectory for off-world and marine variants.
  Payment via Specification for terrestrial v0 baseline
  once `Architecture/Facilities.md` FA-001 is resolved.

**Claude review 2026-08-14:** Path adequate. Cross-reference to
`Architecture/Facilities.md` and its FA-001 confirmed real (matches
the same verification done on Gate_04's MG-006, same underlying
file). Discharge-by-reference framing is correct — this file
shouldn't duplicate siting doctrine another file owns. **Approved
(path adequate).** Remains Open — this file's separation-doctrine
gap is real regardless of where the ultimate fix lives.

---

### SC-007 — Extraction process may disrupt segregation gradients

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-07-28                     |
| Last Reviewed | 2026-08-14                     |

**Description:** The physical act of extracting separated material
from the Spin Chamber may itself disturb the density-based
segregation gradient the separation process relies on, degrading
output purity at the extraction step even when segregation itself
worked correctly. This entry existed in `Unknowns.md`'s active index
with no matching sidecar block here — registered now to close that
gap; the underlying concern is not new.

**Why It Matters:** If extraction disrupts gradients, segregation
effectiveness (SC-002, already Open) cannot be fully evaluated by
looking at input/output composition alone — degradation could be
happening at either stage, and the two would need to be
distinguished before either could be resolved.

**Resolution Path:** Define an extraction method and sequence that
preserves gradient integrity (e.g., layer-by-layer removal vs. bulk
draw), and test whether output purity varies by extraction method at
otherwise-identical segregation conditions. Depends on SC-002
reaching at least Provisional Spec first — no point isolating
extraction-stage loss before segregation-stage effectiveness itself
is characterized.

**Claude review 2026-08-14:** Path adequate. Correctly sequences
after SC-002 rather than trying to isolate two confounded unknowns
at once — that dependency ordering is the substance of a good path
here, not a formality. **Approved (path adequate).** Remains Open.

---

### SC-008 — Graphite crucible carbon pickup in alloy

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical / Materials           |
| Blocking      | No                             |
| Owner         | Operations/Gate_05_Separation_Thermal.md |
| First Logged  | 2026-07-28                     |
| Last Reviewed | 2026-08-14                     |

**Description:** Graphite crucibles, a plausible salvage-sourced
containment material for molten metal, are known in conventional
metallurgy to transfer carbon into the melt (carbon pickup),
altering alloy composition. Whether this is significant at Forge
scale and with salvaged material streams is uncharacterized. This
entry existed in `Unknowns.md`'s active index with no matching
sidecar block here — registered now to close that gap; the
underlying concern is not new.

**Why It Matters:** Uncontrolled carbon pickup changes output alloy
properties in ways that could silently invalidate downstream
material claims (e.g., `Architecture/Engineering.md` EN-003's alloy
identification depends on knowing what alloy is actually present,
not just what was fed in).

**Resolution Path:** Characterize carbon pickup rate for graphite
crucibles at Forge-relevant melt temperatures and residence times;
compare against alternative crucible materials salvage streams are
likely to provide (ceramic, steel-shell) as a lower-pickup
alternative if the rate proves significant.

**Claude review 2026-08-14:** Path adequate. EN-003 cross-reference
matches a real known concern (alloy ID depends on what's actually
present) — flags a legitimate silent-failure interaction between two
files rather than treating this as isolated. **Approved (path
adequate).** Remains Open — needs characterization data, not
agent-closable.

---

### SC-009 — Titanium / reactive-metal atmosphere requirements undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | High                           |
| Priority      | Critical (if titanium/reactive metals enter material set); Non-blocking otherwise |
| Type          | Technical / Physical Plausibility (G2) |
| Blocking      | Yes — any titanium (or Zr/Hf/Nb/Ta) melt, weld, or wire-extrusion path |
| Owner         | Operations/Gate_05_Separation_Thermal.md (primary); Architecture/Chemistry.md (oxidation/nitride chemistry) |
| First Logged  | 2026-07-31 |
| Last Reviewed | 2026-08-14 |

**Description:** §9 Atmosphere Control above (passive reducing environment preferred; charcoal bed or inert purge if available; oxygen ingress minimized, not eliminated; precision gas chemistry out of scope for v0) is adequate for the aluminum-class melts this file currently scopes around, but not for titanium or other reactive/refractory metals. These metals react readily with both oxygen and nitrogen when hot or molten — nitrogen contamination in particular causes severe embrittlement, which is why a simple nitrogen purge (fine for many steels or aluminum) is actively harmful here. Real titanium welding or wire-arc additive manufacturing requires either full high-purity argon shielding (residual O₂ typically <50–300 ppm, entire cooling surface protected until <~400°C) or true vacuum (~10⁻²–10⁻³ Pa or better for aerospace-grade work). Titanium currently appears nowhere in this repository as a feedstock, salvage target, or fabrication material — its only existing mention is `Architecture/Chemistry.md`'s galvanic series table (most noble/cathodic metal, high-end marine hardware reference). Raised 2026-07-31 in response to a claim that titanium welding capability would make CLF-003 (nozzle/die wear) moot; verified against source that no such capability or material pathway currently exists.

**Why It Matters:** If titanium (or an equivalent reactive metal) is ever admitted as a salvage stream or fabrication material, this file's existing atmosphere doctrine cannot be silently inherited — doing so would produce embrittled, non-load-bearing product while appearing to have succeeded. It also would not resolve CLF-003 (`Challenges/Closed_Loop_Feedstock.md`): any titanium wire still has to be drawn through a die (harder problem, not easier), and any titanium part welded from near-net shape still needs cutting/trimming, where titanium's low thermal conductivity and rapid work-hardening make tool wear worse than for steel or aluminum, not moot.

**Resolution Path:** (1) G2 Physical Plausibility gate first — confirm whether reactive-metal processing is in scope for any near-term version; if not, this stays parked. (2) If pursued, define minimum atmosphere spec (residual O₂/N₂ limits, shielding vs. blanket, monitoring), explicitly exclude nitrogen as a purge gas, and identify the hardware delta from the current charcoal-bed baseline (full argon shielding vs. vacuum pumping train). (3) Register any external argon/vacuum-hardware dependency against `Challenges/Closed_Loop_Feedstock.md`'s closed-loop premise. (4) `Admin/Trajectories.md` TR-MET-002 records that Astroid-miner's `Propulsion_Economy_isru/zero_g_fabrication.md` independently specifies Induction Heating + EM Levitation (crucible-free, vacuum-native, high-purity) as a fabrication technique well-suited to this exact problem — but per UNK-003 (Cross-repo assumption contracts, Deferred pending Leviathan milestone) that is supporting detail for a v3+ off-world capability, not a resolution path for this terrestrial v0–v2 unknown.

**Cross-references:** §9 (this file, current atmosphere doctrine); SC-004 (wire extrusion nozzle — any titanium wire path inherits this unknown); `Challenges/Closed_Loop_Feedstock.md` CLF-003 (die/nozzle wear — titanium would add a harder second front, not remove the first); `Architecture/Chemistry.md` (galvanic series, sole existing titanium mention); `Admin/Trajectories.md` TR-MET-002 (Astroid-miner cross-repo note, parked).

**Claude review 2026-08-14:** Path adequate; this is the most claim-
dense unknown in the file and each embedded claim was checked
individually rather than accepted as a set. Confirmed real: TR-MET-002
and TR-MET-003 in `Admin/Trajectories.md` (phrasing matches source);
`Architecture/Chemistry.md`'s galvanic series as titanium's sole
existing mention; the CLF-003 cross-reference substance (dieless
drawing removes die contact). One correction made this pass, in
SC-004 above, not here: a quote attributed to CLF-003 in the Driving
Mechanism Options table did not exist verbatim in source — reworded.
The Critical/Blocking-conditional framing (Blocking only if titanium
enters the material set, which it currently has not) is the correct
way to flag a real risk without inflating the file's present state.
**Approved (path adequate).** Remains Open, correctly parked pending
G2 scope decision.

---

### Resolution Log
- 2026-08-14: **Claude resolution-path review (Round 5 — Operations
  sequence, continuing from Rounds 1-4).** All nine SC unknowns
  reviewed against source. One real error found and corrected: SC-004's
  Driving Mechanism Options table attributed a direct quote to
  `Challenges/Closed_Loop_Feedstock.md` CLF-003 ("applies most strongly
  to any mechanical or high-pressure contact die and least strongly to
  pure MHD or dieless paths") that does not exist verbatim anywhere in
  CLF-003 or the repository — a misattributed quote, not a paraphrase.
  The underlying substance was accurate (CLF-003's own text does
  describe dieless drawing as removing die contact from the metal-wire
  path); reworded to state it as description rather than quotation, in
  both SC-004 and SC-009's cross-reference note. All other embedded
  cross-reference claims checked individually and confirmed real:
  TR-MET-002/003 in `Admin/Trajectories.md`, EN-003 in
  `Architecture/Engineering.md`, `Architecture/Facilities.md`'s FA-001/
  UNK-006 ownership, and the Chemistry.md galvanic-series titanium
  mention. Every Resolution Path judged adequate. **No SC-* closed.**
  Open Unknowns remain 9. Blocking status unchanged (SC-009 stays the
  file's sole conditional-Blocking entry). Last Reviewed → 2026-08-14
  on all nine. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **9** = SC-001–009, matches local
  sidecar and `Unknowns.md`. (2) SC-009 correctly nuanced Blocking Yes for
  titanium/reactive-metal path. (3) **F-SC-003 clarified (same-day follow-up):**
  apparent Unknowns.md ↔ local Blocking desync on SC-001/SC-002 is vocabulary
  distinction, not data error — `Unknowns.md` Priority (Promo) column ≠
  file-local operational Blocking field. Definition added to
  `Admin/Canonical_Terms.md`. Local Blocking left No. (4) No SC-* closed.
  Human-directed.

- 2026-08-08: **Scope Boundary DOES-NOT wording corrected** — "Welding
  wire specification or qualification (downstream — not yet assigned)"
  was inconsistent with this file's own Lessons Learned table (line
  888), which already correctly cites UNK-008's 2026-07-19 ownership
  reassignment to `Architecture/Geck_forge_seed.md`. Surfaced by
  `Operations/Ops_Scope_Map.md`'s 2026-08-08 build. Corrected to match
  what this file already knew elsewhere in its own text. Human-directed.

- 2026-07-31: SC-004 expanded — added Driving Mechanism Options
  subsection (five candidate mechanisms for the wire-extrusion
  driving force: centrifugal, gas-pressure, MHD/EM, mechanical
  piston/screw, hybrid continuous-cast + dieless drawing), verified
  against source (existing interface bullets, SC-001's 50–400 RPM
  envelope, Astroid-miner's confirmed "Spun Conical Ceramic
  Extrusion" primary wire source) and cross-linked to CLF-003
  (dieless/MHD paths mitigate die-wear exposure most; centrifugal/
  gas/piston paths least). Status, Priority, Risk, and Blocking
  unchanged (Open/Minor/Low/No) — this remains correctly deferred to
  v1 per the file's own sequencing; no urgency escalation intended.
  Minimal dieless-drawing experimental configuration parked at
  `Admin/Trajectories.md` TR-MET-003. Verified and added by Claude —
  Synthesizer, human-directed.
- 2026-07-31: SC-009 registered — titanium/reactive-metal atmosphere
  requirements. Raised in response to a claim that titanium welding
  would make CLF-003 moot; verified against source that titanium has
  no existing pathway in this repository and that this file's §9
  atmosphere doctrine cannot support it without a dedicated Critical
  unknown. Cross-linked to CLF-003 (Closed_Loop_Feedstock.md) and
  TR-MET-002 (Trajectories.md, Astroid-miner EM-levitation/vacuum
  note, recorded as supporting detail only per UNK-003's
  Leviathan-milestone gate). Open Unknowns: 8 → 9. Verified and
  registered by Claude — Synthesizer/Auditor, human-directed.
- 2026-07-28: SC-007 and SC-008 given formal sidecar entries —
  previously present in `Unknowns.md`'s active index only, with no
  matching blocks here, surfaced by a Grok-run repo-wide desync audit
  and verified against source (zero prior mentions of either anywhere
  in this file) before registering. Descriptions built from the
  index's own existing text rather than invented. Same audit also
  confirmed a separate, pre-existing File State undercount — all six
  of SC-001 through SC-006 checked individually and confirmed
  Open/In Progress, against a declared count of 5. Open Unknowns
  count corrected: 5 → 8 (6 pre-existing + 2 new), not 5 → 7.
  Verified and registered by Claude — Synthesizer/Auditor,
  human-directed.
- 2026-05-15: SC-001 — Status updated from Open to In Progress.
  Static centrifugal pressure and hoop stress calculated. Safety
  factor ~32× at worst-case v0 inputs. Never-exceed of 400 RPM
  confirmed not the binding constraint on wall integrity. Binding
  constraints identified as thermal shock and dynamic imbalance.
  Dynamic analysis deferred to SC-005. Cold water analog test
  remains required — purpose reframed from wall integrity
  validation to balance and vibration characterization.
- 2026-06-08: Navigation Anchors block added. Title corrected
  from `Spin Chamber (v0)` to `Gate_05_Separation_Thermal`.
  Verification Ref corrected from `Verification_Gates.md`
  to `Admin/Verification_Gates.md` (PC-001). Facilities.md
  upstream reference added to Scope Boundary (PC-002). All
  stale filenames corrected throughout: Material_Separation_Gate_v0.md
  → Gate_04_Separation_Mechanical.md, Lazarus_forge_v0_flow.md
  → Forge_flow.md, geck_forge_seed.md → Geck_forge_seed.md,
  Trajectories_LF.md → Trajectories.md, energy_v0.md →
  Energy.md, Support_Raft_v0.md → Support_Raft.md,
  LF_File_Template.md → File_Template.md. Sidecar Owner
  fields corrected from Spin_Chamber_v0.md to
  Operations/Gate_05_Separation_Thermal.md. SC-006 resolution
  path updated — Architecture/Facilities.md now exists and
  owns siting doctrine; UNK-006 resolved.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Single-pass purity as primary output goal | Purity-first design requires significantly more complex separation chemistry, higher energy input, and precision equipment incompatible with v0 bootstrap constraints. Gradient production with progressive enrichment over generations is more honest to v0 capability and more aligned with forge ecology doctrine | No |
| 2026-05-15 | High throughput as a success metric | Speed optimization conflicts directly with the thermal doctrine of long holds, hot idle, and crucible longevity. A fast chamber is a worn chamber. Throughput is a v2+ consideration after stability and repeatability are demonstrated | No |
| 2026-05-15 | Electrochemical separation via in-melt electrodes | Requires precision gas chemistry, electrode materials, and process control beyond v0 bootstrap scope. Adds failure modes without validated benefit at this scale. Section 8 explicitly excludes electrochemical assumptions | No |
| 2026-05-15 | Precision machining for drive alignment | Alignment by geometry preferred over precision machining — reduces fabrication dependency, supports bootstrap compatibility, and is consistent with standardization doctrine. Precision machining is a capability to grow into, not a v0 requirement | Reconsider at v2 when metrology capability matures |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of this file.
All canonical drift indicators from `Admin/File_Template.md` apply.
The following are additional local triggers specific to the
Spin Chamber:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| SC-002 remains unreviewed after first operational run | Segregation effectiveness is the core claim — operational data must feed back immediately |
| RPM never-exceed revised without SC-005 resolution | Dynamic analysis is a prerequisite for any RPM limit change |
| Drive system specified with non-standard components without documented justification | Standardization doctrine applies — bespoke components require explicit override |
| Safety Advisory conditions change without SC-006 update | Siting requirements and the advisory must stay synchronized |
| Wire extrusion interface advanced without welding wire specification owner identified | SC-004 must resolve alongside `Architecture/Geck_forge_seed.md` UNK-008 (ownership reassigned there 2026-07-19; the design principle is defined, the full specification is not) |
| Melt material class expands beyond Al-class without assumptions review | ASM-002 expiry trigger — temperature bands, density values, and crucible material selection all change with material class |
| Hot idle doctrine abandoned in favor of full thermal cycling | Core thermal doctrine — crucible and coil life assumptions depend on it |

### Canonical Drift Triggers

*All mandatory re-audit conditions from `Admin/File_Template.md`
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*
