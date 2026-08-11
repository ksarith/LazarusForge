# Mechanical_Structures.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Structural deflection, unmodeled thermal expansion, and particulate bearing ingress
> present critical failure vectors capable of destroying irreplaceable salvaged kinematic
> components. Mechanical over-torque during the processing of unrefined feedstocks can
> trigger violent tool-head fracturing or motor burnout. Sacrificial mechanical shear
> couplings and contamination exclusion systems are mandatory across all primary drive
> assemblies — positive-pressure pneumatic purge is the current v0 implementation;
> equivalent alternatives (labyrinth seals, grease barriers, oil mist systems) may be
> substituted when validated against ME-002. Never adjust axis rails or spindle positions
> while the drive bus is energized. **If an axis binds or exhibits harmonic chatter
> exceeding safety thresholds, drop the motor enable lines immediately.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-06-11                                                          |
| Auditor          | Gemini (2026-05-31); ChatGPT (2026-06-11); Claude — Retrofit        |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Structural frame rigidity standards and damp-filling criteria for salvaged members
- Thermal expansion mitigation and coordinate delta compensation rules
- Kinematic protection loops, shunt current monitoring, and torsional alignment interlocks
- Hard-coded mechanical protection protocols (sacrificial shear pins, positive-pressure
  purges)
- Falsifiable mechanical performance metrics and structural drift indicators
- Contamination and bearing protection doctrine for abrasive Forge environments

**This file DOES NOT define:**
- Foundational engineering principles, safety factor doctrine, or materials behavior
  overview (→ `Architecture/Engineering.md`); this file extends that doctrine into
  fabrication machinery specifically
- Specific tool-path G-code files or part-specific geometries
- Component specifications for explicit brands of stepper/servo motors
- Electrical circuit schematics for motor driver boards
  (→ `Operations/Electronics.md`)
- Chemistry profiles for chemical tool-head processing
  (→ `Operations/Air_Scrubber.md`)
- Compressed air system capacity or Air Scrubber back-pressure specifications
  (→ `Operations/Air_Scrubber.md`; see ME-002)
- Precision ceiling doctrine, tolerance tiers, or metrology methodology
  (→ `Architecture/Precision.md`)

---

## File Purpose

This file establishes the structural, mechanical, and kinematic engineering doctrine for
the Lazarus Forge ecosystem. Because the Forge relies entirely on salvaged structural
steel, mismatched linear guides, and unrefined local feedstocks, it cannot operate using
pristine machine shop assumptions.

This document defines the physical safety boundaries, material constraints, and sensor
interlocks required to prevent structural resonance, geometric drift, and catastrophic
mechanical breakdown during autonomous or semi-autonomous fabrication cycles.

**Relationship to `Architecture/Engineering.md`:** That file governs foundational
engineering principles — first principles thinking, safety factor doctrine, materials
behavior, and FMEA discipline. This file applies those principles specifically to
fabrication machinery built from salvaged components. Where the two files address the
same topic, `Architecture/Engineering.md` provides the doctrine and this file provides
the salvage-specific implementation. Conflicts escalate to `Architecture/Engineering.md`
as the upstream authority.

---

## Assumptions

| ID      | Assumption                                                                    | Basis                              | Confidence | Expiry Trigger                                              |
|---------|-------------------------------------------------------------------------------|------------------------------------|------------|-------------------------------------------------------------|
| ASM-001 | Salvaged structural iron/steel frames require dampening to mill carbon steel  | Resonance and flexure profiles     | High       | First physical tool-chatter analysis on unfilled frame      |
| ASM-002 | Mechanical components must endure ambient thermal deltas up to 25°C          | Heat radiation from Gate 05 units  | Medium     | Measured enclosure temperature curves exceed bounds         |
| ASM-003 | Commercial rubber wipers are insufficient against abrasive local slag dust    | Rapid seal abrasion literature     | High       | Bearing failure due to dust ingress inside 50 hours         |
| ASM-004 | Low-cost MEMS accelerometers can reliably capture spindle harmonic chatter   | Analogous industrial telemetry     | Medium     | Software loop fails to filter ambient motor noise           |

---

## Design Philosophy

- **Rigidity Through Mass, Not Sourcing:** Pristine cast-iron machine beds are
  unavailable. Structural rigidity must be achieved by reinforcing salvaged hollow
  profiles with local composite matrices.
- **Expect Distortion, Compensate Logically:** Every physical assembly will warp under
  thermal load or tool resistance. Deflection must be actively monitored at the sensor
  layer and mitigated via hardware interlocks.
- **Sacrificial Mechanical Weak Points:** Electrical fuses protect electronics;
  mechanical fuses must protect gears and motor shafts. Always design cheap, easily
  swappable failure points into high-torque paths.
- **Isolate Moving Surfaces:** Abrasive particulates are an operational certainty.
  Kinematic surfaces must be kept under constant positive pressure or dense physical
  oil barriers to reject contaminants.

---

## Structural Frame & Rigidity Doctrine

### 1. The Elastic Deformation Limit (Gantry Rigidity)

When utilizing salvaged structural sections (such as heavy-wall steel square tubing or
aluminum profiles) for a multi-axis CNC gantry or processing bed, deflection under
cutting forces is the primary vector for dimensional instability and tool breakage.
For a 1000 mm unsupported structural span under a 500 N lateral tool force, standard
unfilled structures introduce unacceptable flexure.

```
[Toolhead Lateral Force: 500 N] ──►
    ┌────────────────────────────────────────┐
    │ Unfilled Aluminum Profile (1000mm)     │ ──► Deflection: ~1.25 mm (Blinds Endmills)
    └────────────────────────────────────────┘
    ┌────────────────────────────────────────┐
    │ Sand/Epoxy Composite Filled Steel Tube │ ──► Deflection: <0.08 mm (Precision Maintained)
    └────────────────────────────────────────┘
```

**Mandatory Stabilization:** To maintain structural rigidity without custom manufacturing
infrastructure, hollow structural steel frames **must** be damp-filled using a dense
composite matrix. The RDC starting mixture is clean, dry quartz sand and epoxy resin
(80:20 mass ratio) — this is a validated starting point, not a frozen specification.
Alternative fills (polymer concrete, fly ash composites, iron shot) may prove superior
and should be evaluated as operational experience accumulates; see ME-004. This fill
can reduce resonance amplitude by up to fourfold while increasing damping ratios and
preserving structural rigidity.

### 2. Thermal Expansion Disconnect

Salvaged linear guideways bolted directly to unmachined steel frames will bind or
introduce severe backlash as ambient temperatures fluctuate during high-energy Forge
operations. Structural carbon steel and salvaged aluminum tool-carriages possess
divergent thermal expansion coefficients:

- Structural Carbon Steel: α ≈ 12 × 10⁻⁶ /°C
- Aluminum 6061-T6: α ≈ 23 × 10⁻⁶ /°C

A temperature swing of 25°C across a 1000 mm axis creates a 0.27 mm differential
expansion delta. To combat this, all multi-axis gantry assemblies must utilize engineered
mechanical slip-planes on secondary anchoring points, or run software-mapped coordinate
thermal compensation arrays bound to local frame thermistors.

---

## Contamination & Bearing Protection Doctrine

Standard commercial rubber linear rail seals fail rapidly when exposed to abrasive,
jagged micro-particulates generated by slag crushing, wood processing, and metal milling.
Once fine silicate dust or metallic swarf bypasses the primary wiper, it mixes with
internal bearing grease to form an aggressive lapping compound, accelerating ball-bearing
wear by over 800%.

All critical mechanical bearing blocks operating inside the primary processing containment
envelope **must** feature:

1. Secondary, field-fabricated positive-pressure felt wipers.
2. Constant saturation via high-viscosity way oil (ISO VG 68 or equivalent) to physically
   flush incoming particulate matter away from the internal bearing tracks.

---

## Kinematic & Mechanical Interlock Matrix

*[Ref: ME-001 — resonance mapping on mismatched salvaged rails; thresholds below are
provisional pending physical characterization. See sidecar.]*

To prevent logic-loop crashes from tool-head binding, axis crashes, or structural
harmonic destruction, all mechanical translation layers must interface directly with
this physical safety grid.

| Targeted Failure Vector         | Primary Detection Method                                              | Actionable System Threshold                                            | Automated Interlock Trigger                                                                               |
|---------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Axis Binding / Rail Ingress** | Shunt-resistor current monitoring on stepper/servo drivers (I_drive)  | I_drive ≥ 135% of nominal tuning baseline for >150 ms                 | **Kinematic Fault 01:** Drop motor enable lines; pause G-code execution buffer; lock z-axis brake.        |
| **Structural Resonance / Chatter** | 3-axis MEMS accelerometer on tool-spindle housing                  | Vibration amplitude >2.2 g within 150 Hz–600 Hz bands                 | **Resonance Mitigation Alert:** Step down spindle speed 15%; decrease axis feed rate 20% to find stable harmonic window. |
| **Spindle Stall / Over-Torque** | Rotary encoder pulse tracking vs. commanded VFD frequency index       | RPM slip delta Δω ≥ 8% for more than 300 ms                           | **E-Stop Lockout:** Cut VFD output bridge; freeze all linear stepper axes to prevent tool plowing.        |
| **Gantry Torsional Misalignment** | Dual homing limit switches per parallel-driven axis (X₁ vs. X₂)   | Squareness offset ΔX ≥ 0.12 mm during homing or runtime cycle         | **Alignment Fault:** Force immediate system halt; initiate automated axis squareness recalibration.       |

---

## Hard-Coded Mechanical Protection Protocols

### 1. Sacrificial Shear Coupling Mandate

To safeguard irreplaceable salvaged motor-generators, custom pulleys, and precision
gearboxes from catastrophic torque spikes during unrefined feedstock processing, direct
rigid coupling between drive units and processing shafts is strictly prohibited.

All primary mechanical drives (rotary crushers, heavy milling spindles, shredder arrays)
**must** utilize a dedicated, easily replaceable sacrificial brass shear pin or a
slip-clutch mechanism calibrated to yield at exactly 125% of the maximum nominal
operating torque ceiling.

### 2. Positive-Pressure Spindle Purge

*[Ref: ME-002 — purge volume vs. Air Scrubber capacity unbalanced; see sidecar.]*

To prevent toxic, corrosive outgassing from migrating down the spindle shaft and
destroying internal spindle motor windings or packing grease, the spindle nose housing
must integrate a continuous pneumatic positive-pressure purge channel. A regulated air
bleed tap (0.5 bar minimum delivery pressure) must feed directly into the upper bearing
sleeve, ensuring a constant outward velocity of clean air to deflect airborne moisture,
acids, and abrasive micro-dust.

---

## Metrics (Falsifiable)

**Primary metric:** Mean Time Between Mechanical Failures (MTBMF) ≥ 250 operational
hours under continuous nominal processing loads. *(Analogous — derived from comparable
industrial salvage machinery baselines; to be upgraded to Measured after first
operational cycle.)*

**Secondary indicators:**
- Axis positional drift — measured delta between homing cycles over 12 hours of runtime
- Bearing block temperature stability — anomalous spikes flag internal particulate ingress
- Structural vibration dampening efficiency over time

---

## Explicit Non-Goals (v0)

- Achieving sub-micron aerospace machining tolerances using unmachined salvaged frames
- Continuous high-speed processing of superalloys or hardened tool steels
- Elimination of manual lubrication and maintenance schedules

---

## Lessons Learned

| Date       | Evidence Type   | What Was Tried                        | What Failed                                                  | What Was Learned                                                                    | Confidence | Revalidation Needed |
|------------|-----------------|---------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-31 | Modeling / Audit | Modeled raw unsealed guideway execution under abrasive particulate load | Predicted rubber seal failure within ~50 hours based on abrasion literature and analogous industrial cases — not yet confirmed by operational observation | Secondary way-oil-saturated felt wipers are mandatory for abrasive particle isolation; validate on first physical run | High | Yes — validate against first physical bearing teardown |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet | —      |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Shunt-resistor current overrides implemented via software that exceed the 135% safety
  threshold
- Removal of the dense damping matrix fill requirement for hollow structural spans
  over 500 mm (the fill is mandatory; the specific mixture ratio is an implementation
  detail that may evolve — see ME-004)
- Softening of the 125% mechanical torque shear-pin cutoff rule into variable software
  limits
- Removal of the spindle pneumatic positive-pressure purge requirement
- Substitution of the falsifiable MTBMF metric with qualitative performance goals
- Scope boundary revised to absorb foundational engineering principles from
  `Architecture/Engineering.md`
- Verification Ref changed away from `Admin/Verification_Gates.md`

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous
audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### ME-001 — Vibration resonance mapping on mismatched salvaged rails uncharacterized

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Architecture/Mechanical_Structures.md |
| First Logged  | 2026-05-31                     |
| Last Reviewed | 2026-05-31                     |

**Description:** The harmonic interplay between different linear rail sizes salvaged from
separate industrial lines is unmeasured. True resonant frequencies could cause tool
chatter below the 2.2 g detection threshold, meaning the interlock matrix may not trigger
on real-world chatter events from this rail combination.

**Why It Matters:** Interlock thresholds in the Kinematic Matrix are provisional until
physical resonance characterization is complete. A threshold set above the actual
problem frequency provides no protection.

**Resolution Path:** Mount the 3-axis MEMS accelerometer to the tool-head spindle and
run air-cutting speed sweeps from 100 to 5000 RPM, mapping peak vibration nodes across
the salvaged rail combination. Update the 2.2 g / 150–600 Hz interlock parameters from
Analogous to Measured once sweep data exists.

---

### ME-002 — Pneumatic purge volume requirements vs. Air Scrubber capacity unbalanced

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Architecture/Mechanical_Structures.md |
| First Logged  | 2026-05-31                     |
| Last Reviewed | 2026-05-31                     |

**Description:** The 0.5 bar minimum spindle air purge tap volume draw has not been
balanced against the system's total compressed air availability or Air Scrubber
back-pressure metrics. A purge tap that starves downstream pneumatic interlocks defeats
its own protective purpose.

**Why It Matters:** If compressed air demand from the purge tap reduces available
pressure below the threshold required by other pneumatic interlocks, the protection
hierarchy inverts — the spindle purge disables the safety systems it is meant to
supplement.

**Resolution Path:** Measure total system compressed air consumption during a simulated
Nominal Mode run. Verify the 0.5 bar bleed tap does not reduce system pressure below
downstream interlock minimums. Cross-reference `Operations/Air_Scrubber.md` for
back-pressure specifications and AS-003 (scrubber waste stream and saturation
calibration — open unknown).

---

---

### ME-003 — Structural creep and damp-fill aging not characterized

| Field         | Value                                |
|---------------|--------------------------------------|
| Status        | Open                                 |
| Risk          | Medium                               |
| Priority      | Major                                |
| Type          | Technical                            |
| Blocking      | No                                   |
| Owner         | `Architecture/Mechanical_Structures.md` |
| First Logged  | 2026-06-11                           |
| Last Reviewed | 2026-06-11                           |

**Description:** Epoxy/sand fills and salvaged weldments may change mechanical
properties over years of operation due to vibration fatigue, moisture ingress,
thermal cycling, shrinkage, and differential expansion between fill and frame.
The damping characteristics of the filled structure may drift gradually without
any single obvious component failure. No monitoring or revalidation doctrine
currently exists for this.

**Why It Matters:** A machine that slowly loses stiffness through fill aging
or weld creep can drift outside its safe operating envelope invisibly. Interlock
thresholds calibrated to a freshly built machine may become insufficient for a
machine that has been operating for two years. This is a silent failure mode —
the process continues but dimensional accuracy and structural safety margins
both degrade.

**Resolution Path:** Establish resonance fingerprinting as a periodic
maintenance procedure. At defined intervals (initially every 250 hours of
operation matching MTBMF), sweep spindle RPM from 100–5000 RPM and measure
accelerometer spectrum. Compare to baseline taken at commissioning. If resonance
signatures shift outside a defined tolerance band, inspect fill integrity,
weld condition, and bearing preload before resuming full operation. Regrouting
or structural reinforcement protocol to be defined when first resonance shift
is observed.

---

### ME-004 — Calibration values not separated from doctrine sections

| Field         | Value                                |
|---------------|--------------------------------------|
| Status        | Open                                 |
| Risk          | Low                                  |
| Priority      | Minor                                |
| Type          | Structural                           |
| Blocking      | No                                   |
| Owner         | `Architecture/Mechanical_Structures.md` |
| First Logged  | 2026-06-11                           |
| Last Reviewed | 2026-06-11                           |

**Description:** Provisional numerical thresholds (2.2 g, 150–600 Hz, 135%,
150 ms, 8%, 300 ms, 0.12 mm, 125%, 0.5 bar) are embedded directly inside
doctrine sections. These values are acknowledged as Analogous/provisional but
their confidence level and promotion path are not tracked per-value. When a
measured value replaces an analogous one, a doctrine section must be rewritten
rather than a parameter table updated.

**Why It Matters:** As operational data accumulates, individual thresholds
will be promoted from Analogous to Measured at different times. The current
structure requires rewriting prose doctrine sections to make those updates,
which creates drift risk and makes confidence levels invisible to future auditors.

**Resolution Path:** Create a Calibration Values appendix table with columns:
Parameter | Current Value | Confidence | Owner Section | Promotion Trigger.
Each numerical threshold in the Kinematic Matrix and Hard-Coded Protocols
gets a row. Doctrine sections reference the table rather than embedding the
number directly. This separates "abnormal current shall trigger motor shutdown"
(doctrine, stable) from "135% for 150ms" (calibration, provisional). Defer
to next major file revision — non-blocking.

---

### Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits as Engineering/Waste pass).**
  Findings only; Spec Gates left locked at 2/6. (1) Open Unknowns **4** =
  ME-001–004, matches local sidecar and `Unknowns.md` (count already corrected
  2026-07-28). (2) All four Blocking No; ME-001 (vibration) and ME-003 (creep)
  carry silent-failure language but do not rise to the operational-interlock
  understatement pattern of TS-002/EL-005. (3) No ME-* closed; no physical
  test claims advanced. Human-directed.

- 2026-07-28: Open Unknowns count corrected 3 → 4. All four of
  ME-001 through ME-004 checked individually and confirmed genuinely
  Open — surfaced by a Grok-run repo-wide desync audit, verified
  against source before correcting. Claude — Synthesizer/Auditor,
  human-directed.
- 2026-06-11: ChatGPT informal audit integrated. Five findings actioned:
  (1) Spec Gate advanced 1→2 — Gate 1 (scope boundary) and Gate 2 (falsifiable
  metrics) both satisfied. (2) "Dampens resonant frequencies by up to 400%"
  corrected to physically accurate amplitude reduction framing. (3) 80:20 ratio
  demoted from frozen specification to RDC starting value — dense fill doctrine
  protected; Drift Indicator updated accordingly. (4) Safety Advisory updated —
  contamination exclusion is the mandatory doctrine; pneumatic purge is the v0
  implementation. (5) Lessons Learned evidence type corrected — wording now
  accurately reflects modeled/predicted failure, not operational observation.
  ME-003 added (structural creep and damp-fill aging). ME-004 added (calibration
  values not separated from doctrine). Open Unknowns updated 2→3 (ME-004 is
  Minor/non-blocking; ME-003 is the substantive new gap). Last Audit updated.
- 2026-06-08: Navigation Anchors block added. Scope Boundary updated.
  mechanical, and kinematic engineering doctrine for salvaged-component fabrication
  machinery. Scope explicitly scoped as downstream extension of
  `Architecture/Engineering.md`, not a replacement. Codified gantry damp-filling
  constraints, thermal expansion compensation rules, felt wiper bearing protections,
  kinematic interlock matrix, sacrificial shear pin mandate, and positive-pressure
  spindle purge parameters. Verification Ref corrected to
  `Admin/Verification_Gates.md`. Open Unknowns count set to 2 (ME-001, ME-002).
  Spec Gate 1 assessed as passing.
- 2026-06-08: Navigation Anchors block added. Scope Boundary updated —
  `Operations/Electronics.md` [PLANNED] tag removed (file now exists);
  `Architecture/Precision.md` added as precision ceiling doctrine owner (PC-003).
  ME-002 resolution path updated — `Operations/Air_Scrubber.md` now exists;
  cross-reference to AS-003 added.
