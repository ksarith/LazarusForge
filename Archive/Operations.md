Compilation of Operations folder.

# Air_Scrubber.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> The Air Scrubber handles toxic, corrosive, and
> carcinogenic airborne byproducts generated during
> Forge operation. Saturated scrubbing liquid passes
> contaminants directly to exhaust — a Saturation Fault
> while reporting "Airflow OK" is the most dangerous
> failure mode. Continuous fan and compressor operation
> produces sustained noise levels capable of causing
> permanent hearing damage and masking fault signals;
> hearing protection is required during all operation
> and maintenance. The scrubber operates under negative
> pressure — loss of airflow draws hazardous air outward.
> Saturation thresholds are bound to the differential
> sensor matrix; apply the most conservative
> interpretation until calibrated. See AS-003.
> **When in doubt, shut down. The Forge does not run
> if the scrubber cannot verify safe operation.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-31                                                          |
| Auditor          | Gemini                                                              |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Open Unknowns updated from 3 to 4 — AS-004 now
correctly cross-references `Admin/Safety_Protocols.md`
as partial resolution path (noise exposure limits
are addressed there), but the formal hearing
conservation program for Air Scrubber operations
and site-specific SPL measurements remain open.
Gate 4 Cold Verification Harness integrated as
its own body section — Spec Gates remain at 3/6 until
physical verification protocols are executed and
logged.*

---

## Scope Boundary

**This file DOES define:**
- Air Scrubber design philosophy and doctrine
- Five-stage functional architecture (Stages A
  through E) augmented with fractional condensation
  and chemisorption layers
- Wet capture variants (Variant 0 through Variant 4)
  including positive pressure protection variant
- Saturation Fault, Particulate Blinding, and
  Thermal Fault monitoring matrices
- Automated interlock and E-Stop triggers for
  safety boundaries
- Negative pressure safety boundary doctrine and
  flashback mitigation
- Noise hazard acknowledgment and hearing protection
  requirements
- Energy awareness and power budget estimates
- Waste as a managed output
- Gate 4 Cold Verification Harness — physical
  testing protocol for sensor matrix validation
  before hot operation is permitted
- Integration hooks to upstream and downstream
  modules

**This file DOES NOT define:**
- Spin Chamber exhaust heat load
  (`Operations/Gate_05_Separation_Thermal.md`)
- Forge power budget and demand baseline
  (`Operations/Energy.md`)
- Deep-sea compression modules
  (`Admin/Trajectories.md` v2/v3)
- Contamination routing and waste stream final
  disposition (`Operations/Gate_02_Triage.md`)
- Scrubber bootstrap minimum for remote deployment
  (`Architecture/Geck_forge_seed.md`)
- Noise exposure limits, formal hearing conservation
  program, and PPE standards
  (`Admin/Safety_Protocols.md` SP-003)
- Facility siting and ventilation topology
  (`Architecture/Facilities.md` FA-001)

---

## File Purpose

This file defines the design doctrine, functional
architecture, and operational requirements for the
Air Scrubber subsystem of the Lazarus Forge. The
scrubber is an enabling system — without it, the
Forge does not operate. Its purpose is to prevent
release, accumulation, or uncontrolled transformation
of hazardous airborne byproducts generated during
Forge operation.

The Air Scrubber is not a filter appended after the
fact. It is a continuation of the production path.
Every Forge process assumes byproduct generation.
The scrubber is designed around that assumption —
it captures hazards before they escape, converts
mobile hazardous forms into manageable ones, and
provides the sensor matrix that tells the Forge
whether safe operation is occurring. If the scrubber
cannot verify safe operation, the Forge shuts down.

The Gate 4 Cold Verification Harness below
defines the physical testing protocol that must be
executed before hot operations begin. It treats
the sensor matrix as an adversarial system — failure
modes are simulated under cold conditions using
non-hazardous surrogates so that automated interlocks
can be proven before they are needed.

If this file disappeared, operators would lack the
doctrine required to design, operate, and maintain
the safety boundary that makes all other Forge
operations permissible.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Surface and shallow-water variants operate within 500W total system draw | Analogous — industrial scrubbers | Medium | First measured power draw from operational prototype |
| ASM-002 | Variant 4 marine scope is limited to less than 5 atm / 50m depth at v0 power class | Compression work calculation | High | Dedicated high-output compression module available |
| ASM-003 | Negative pressure operation is achievable with salvaged fan/compressor hardware | Analogous — industrial practice | Medium | First prototype demonstrates achievable differential |
| ASM-004 | Thermal sink can be sized to Spin Chamber exhaust load at v0 | Placeholder — exhaust load unknown | Low | `Operations/Gate_05_Separation_Thermal.md` exhaust characterization |
| ASM-005 | Noise from continuous fan/compressor operation exceeds safe exposure limits without PPE | Analogous — industrial fan noise levels | High | Measured SPL confirms otherwise |

---

## Design Philosophy

**1. Capture Is Part of Production**
All Forge processes assume byproduct generation. The
Air Scrubber is a continuation of the production
path, not a cleanup step. Every mode assumes
containment.

**2. Interaction Is Forced, Not Hoped For**
Airflow is deliberately manipulated to increase
residence time and convert mobile hazards into
capturable forms.

**3. Condense, Charge, Cool, Then Capture**
Drop heavy fractions via fractional condensation
loops to protect downstream media → impart a charge
to airborne species to encourage agglomeration →
cool the gas stream to reduce volatility → capture
into liquid or solid phases.

**4. Negative Pressure as a Safety Boundary**
The scrubber operates under slight negative pressure
relative to surroundings. Leaks draw air inward.
Loss of airflow is a critical fault. The Forge
defaults to shutdown rather than uncontrolled
exhaust.

**5. Defeat the Bypass (True Saturation Monitoring)**
A scrubbing system that has reached saturation while
reporting "Airflow OK" is not a scrubber — it is a
bypass. The system must monitor scrubbing liquid
quality alongside differential gas-phase analysis
(Pre- vs. Post-filter) to trigger automated
interlocks before chemical bypass occurs.

**6. Noise Is a Hazard, Not a Side Effect**
Continuous fan and compressor operation produces
sustained noise levels capable of causing permanent
hearing damage and masking critical fault signals.
Hearing protection is required during all scrubber
operation and maintenance. Fault signal audibility
must be verified against ambient noise floor.

---

## Functional Architecture

```
[Incoming Gas Stream]
        │
        ▼
 ┌───────────────┐
 │    Stage A    │ ──► Sacrificial Mechanical Intercept (Coarse Particulates / Cyclones)
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage B    │ ──► Ionization / Electrostatic Conditioning
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage C    │ ──► Thermal Quench / Fractional Condensation Loop
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage D    │ ──► Wet Scrubbing / Water Column (Requires explicit Thermal Sink Interface)
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage E    │ ──► Polishing / Chemisorption Media (Activated GAC + KMnO₄ Bed)
 └───────────────┘
        │
        ▼
 [Safe Exhaust]
```

### Stage A — Sacrificial Mechanical Intercept
Captures coarse particulates and debris. Protects
downstream stages. Designed for frequent replacement
and treated as expendable. Includes mechanical
cyclone separation when dealing with high particulate
loads.

### Stage B — Ionization / Electrostatic Conditioning
Imparts charge to particulates, aerosols, and vapors
to encourage agglomeration and surface attachment.
Ionization energy is moderated. Ozone or unintended
reactive species are monitored as fault conditions.

### Stage C — Thermal Quench / Fractional Condensation Zone
Rapidly lowers gas temperature to encourage
condensation of semi-volatile compounds.

> 🧪 **Hardware Precedent — The Condensation Prerequisite**
> Hardware deployment data indicates that direct-to-carbon
> routing of pyrolysis outgassing causes instantaneous tar
> blinding of the filter media. A multi-stage fractional
> condensation loop (cyclone separator or chilled fluid
> condenser) **must** precede the chemical scrubbing phase
> to drop out heavy oil fractions, paraffins, and waxes.

### Stage D — Wet Scrubbing / Water Column
Absorbs soluble gases and captures charged/agglomerated
particulates. Water is operated in a recirculating
loop with continuous chemical monitoring.

> 🧪 **Cross-Reference, 2026-07-19 — Chlorine-Specific Caustic Dosing:**
> For processes generating chlorine gas (e.g. the chlor-alkali
> acid-sourcing candidate pathway in `Challenges/Closed_Loop_Feedstock.md`
> CLF-004), Stage D is the correct capture mechanism — a caustic (NaOH)
> reagent dose in this recirculating column absorbs Cl₂ via the standard
> industrial reaction (Cl₂ + 2NaOH → NaCl + NaOCl + H₂O). **Stage E's
> KMnO₄ chemisorption bed does not perform this function** — it is an
> oxidizing chemisorbent for reducing-species VOCs, and Cl₂ is itself
> already an oxidizer with no oxidation pathway for KMnO₄ to act through.
> See `Architecture/Chemistry.md` CE-006/CE-007 for the full mechanism
> correction and sourcing.

- **Thermal Sink Requirement:** Hot exhaust from
  the Spin Chamber transfers heat to scrubbing water.
  Stage D requires an explicit, ruggedized thermal
  sink interface (heat exchanger, radiator, or passive
  cooling surface) sized to the expected exhaust heat
  load.
- **Corrosion Isolation:** Wet venturi or water-bubbler
  stages handling exhaust from halogenated materials
  must utilize heavy-walled HDPE or 316L stainless
  steel hulls to resist accelerated hydrochloric acid
  pitting.

### Stage E — Polishing / Last-Chance Chemisorption Bed
Captures residual contaminants that escape primary
stages.

> 🧪 **Hardware Precedent — Chemisorption Overrides**
> Standard granular activated carbon (GAC) exhibits
> poor retention for light-fraction toxic syngas
> components (e.g., carbon monoxide, formaldehydes,
> methane). Where high-temperature reduction or
> synthetic polymer processing is active, the final
> stage dry-bed **must** integrate an active
> chemisorbent media, such as alumina impregnated with
> potassium permanganate (KMnO₄), to permanently
> chemically neutralize low-molecular-weight VOCs.
>
> **Scope note, 2026-07-19:** this media targets reducing-species
> VOCs and does not capture chlorine gas — see the Stage D
> cross-reference above and `Architecture/Chemistry.md` CE-006/CE-007
> for chlorine-generating processes.

---

## Mechanical & Physical Safety

- **Anti-Flashback Assemblies:** All lines routing
  non-condensable syngas or pyrolysis outgassing back
  into process furnaces or flares must feature a
  verified dual-mesh inline explosion-proof flashback
  arrestor to prevent flame propagation back into the
  air scrubber assembly.
- **Containment Enclosure:** All high-pressure
  fittings and liquid sumps must reside inside a
  co-contained workspace pan to capture liquid
  overflow or secondary gas leakages.

---

## Wet Capture Variants

### Variant 0 — Positive Pressure Enclosure Protection (Simplest)
The pressure-differential principle works in both
directions. Where primary scrubbing uses negative
pressure to contain hazards inside a process box,
positive pressure protects a clean operator or
instrument space by pushing air outward through
every structural gap — dust and contaminants must
fight the outward velocity to enter.

- **Applications:** Operator cab or control room
  in a dusty Forge environment; critical electronics
  enclosures.
- **Implementation:** A blower draws ambient air
  through a multi-stage filter (coarse pre-filter
  protecting a finer main filter) and pressurizes
  the protected space. Controlled exits (door seals,
  pressure relief vents) maintain differential without
  over-pressurizing.

### Variant 1 — Aerated Pond-Style Bubbler (Baseline)
Simple tank with a submerged porous diffuser. Gas is
forced through water via fine bubbles. Prioritizes
simplicity, robustness, and ease of inspection.
**Primary v0 baseline.**

### Variant 2 — Packed Column with Recirculation (Intermediate)
Vertical column with random packing or salvaged scrub
media. Counter-current gas–liquid contact provides
higher efficiency with a modest increase in system
pressure drop.

### Variant 3 — Conditioned Intake + Wet Polish (Future)
Upstream ionization stage feeds a wet stage used
primarily for capture and quench. Reserved for
high-energy or highly variable feeds.

### Variant 4 — Shallow-Depth Marine Bubble-Column (Near-Term Marine)
Scoped strictly to shallow water (less than 5 atm /
~50m depth) for v0. Deep-sea variants route directly
to `Admin/Trajectories.md` target milestones.

- Inject compressed air through pressure-rated
  submerged diffusers.
- Aerate low-dissolved-oxygen (DO) water and capture
  volatiles (H₂S, CO₂) at the surface.
- Onboard sensors track real-time pH, DO, turbidity,
  and gas composition.
- Target bubble sizes: 80–500 μm.
- Column depth: 1–3 m.
- **Quantitative Targets:** 10–30% DO saturation
  increase in less than 2 mg/L hypoxic water; energy
  draw less than 100 W per 1–2 m³ plume.

---

## Energy Awareness

Conceptual ballpark ranges (non-binding, Earth surface
standard conditions):

- Fan/compressor draw: 50–150 W
- Ionization stage: 10–30 W
- Wet-stage recirculation: 20–80 W
- Thermal sink (heat exchanger / radiator): Sized
  dynamically to Spin Chamber exhaust heat load.

**Goal:** Maintain less than 500 W total system draw
for surface and shallow-water variants. Deep-sea
variants are a separate power class.

---

## Sensor Layout & Automated Failure Interlocks

The scrubber uses a multi-point differential diagnostic
grid. If the scrubber cannot verify safe operation via
this matrix, the Forge core triggers an automated
shutdown sequence.

| Diagnostic Metric | Detection Method | Actionable System Threshold | Automated Interlock Trigger |
|---|---|---|---|
| **Media Saturation** | Dual VOC PID Sensors (Pre- vs. Post-Filter Differential) | Efficiency drop to less than 85% capture | Trigger **System Fault 04**; Halt downstream heating elements; Force auxiliary air bypass. |
| **Particulate Blinding** | Differential Pressure (ΔP) Transducers across HEPA/Carbon pack | ΔP ≥ 450 Pa over clean baseline | Trigger **Filter Restriction Alert**; Initiate automated mechanical shaker or lock out milling spindle. |
| **Acidic Ingress (HCl/HF)** | Post-scrubber electrochemical gas sensor / pH probe in wet sumps | Sump pH less than 5.5 or Exhaust greater than 5 ppm | Instantaneous **E-Stop Lockout** of Pyrolysis Reactor core. |
| **Thermal Saturation** | Thermocouples in Stage D liquid core | Temperature exceeds rated fluid threshold | Trigger **Thermal Fault**; Divert feedstocks away from primary thermal reduction units. |
| **Noise Fault Masking** | Ambient microphone calibration check | Alarm audio margin less than 10 dB above operating noise floor | Flash high-intensity visual strobes; Flag system failure to supervisory network layer. |

---

## Waste as a Managed Output

Captured materials are not disposable nuisances.

- Liquids, sludges, and solids are routed into
  controlled handling paths.
- Sump chemical composition is monitored as a
  primary diagnostic signal.
- **Disposition:** (1) test for reuse potential;
  (2) if hazardous, immobilize per applicable
  regulations; (3) if inert, route to bulk
  material recovery.

> 🧪 **Worked Example, 2026-07-19 — Sodium Hypochlorite:**
> Stage D caustic dosing for chlorine-generating processes (see
> Stage D cross-reference above) produces sodium hypochlorite
> (NaOCl) liquor as its natural reaction product — a case where
> "test for reuse potential" applies directly rather than defaulting
> to hazardous immobilization. NaOCl has direct salvage value as a
> disinfectant/sanitizer. See `Architecture/Chemistry.md` CE-007 for
> the storage, stability, and reuse doctrine this requires before
> disposition can move past "test for reuse potential" to actual reuse.

---

## Compatibility With Autonomous Operation

The Air Scrubber is designed to operate continuously
without manual tuning, provide clear health signals
to supervisory systems, and fail into containment
rather than release. Human oversight is optional;
stewardship is not.

---

## Integration Hooks

- `Operations/Gate_05_Separation_Thermal.md` — Primary
  exhaust source; thermal load on Stage D sized to
  Spin Chamber output.
- `Operations/Gate_04_Separation_Mechanical.md` —
  Pre-purification separation exhaust source.
- `Tests/Leviathan_testing.md` — Testbed for
  shallow-water marine variants.
- `Operations/Gate_02_Triage.md` — Scrubber chemistry
  feedback refines classification heuristics;
  contamination handling cross-reference.
- `Operations/Energy.md` — Aggregate data refines
  draw estimates; thermal sink power inclusion.
- `Architecture/Geck_forge_seed.md` — Bootstrap
  minimal scrubber for remote deployment.
- `Admin/Ship_of_Theseus.md` — Scrubber as
  preservation enabler during artifact recovery.
- `Admin/Safety_Protocols.md` — Noise exposure limits,
  hearing conservation program, and PPE standards
  for scrubber operations.

---

## Summary Doctrine

The Air Scrubber is not a filter. It is a boundary
system that forces hazardous matter into managed forms,
prevents accidental chemistry, and makes responsible
operation possible at scale.

A Forge that cannot clean up after itself is incomplete
by definition. And a scrubber that does not know when
it is full is a liability.

---

## Gate 4 Cold Verification Harness

This protocol governs the physical and logical
verification of the differential diagnostic grid
defined above. Testing must be performed in sequence,
using non-hazardous surrogates, with the primary Forge
heating elements and feedstock intake mechanically
and electrically isolated.

Successful execution of all four protocols is the
physical evidence required to advance Spec Gates
from 3/6 to 4/6. Results are logged in the Test
Execution Matrix below and contributed to
`Admin/Verification_Gates_LF.md`.

### Pre-Test Safety & Harness Setup

Before executing any sensor verification loop:

1. **Isolate Power Hooks:** Physically disconnect
   the main power lines to the Pyrolysis Reactor
   core heaters and the milling spindle. Verify air
   scrubber fan/compressor power is routed through
   the secondary safety relay loop.
2. **PPE Baseline:** Full face shield and nitrile
   gloves are mandatory during wet sump adjustments.
3. **Log Initialization:** Initialize
   `Automation/AUDIT_HARNESS.py` in listen-only mode to
   capture real-time state transitions on the local
   bus.

### Protocol 1.1 — Media Saturation Interlock (VOC PID)

Verifies dual photoionization detector (PID)
differential capture logic without generating toxic
outgassing.

- [ ] **Step 1 (Baseline Verification):** Power on
  the primary air scrubber fan. Verify that
  Sensor_VOC_Pre and Sensor_VOC_Post settle within
  ±2% of each other in ambient air. Check that the
  control layer reads System Status: Nominal.
- [ ] **Step 2 (Surrogate Injection):** Introduce a
  controlled hydrocarbon surrogate (e.g., exposing
  an open container of isopropyl alcohol near Stage
  A's intake manifold).
- [ ] **Step 3 (Differential Calibration):** Monitor
  the live bus telemetry. Confirm that Sensor_VOC_Pre
  spikes immediately while Sensor_VOC_Post remains
  flat, proving the downstream polishing media is
  active.
- [ ] **Step 4 (Fault Simulation):** Artificially
  force a saturation bypass state. Place a secondary
  surrogate source directly at the Stage E exhaust
  sensor to simulate breakthrough efficiency dropping
  below 85%.
- [ ] **Step 5 (Interlock Check):** Verify that the
  system registers **System Fault 04** within
  < 500 ms. Confirm that the control loop opens the
  primary safety relay, immediately cutting simulation
  power to downstream heating elements.

### Protocol 1.2 — Particulate Blinding Interlock (ΔP)

Verifies differential pressure transducers accurately
flag filter restriction before an over-pressure event
occurs.

- [ ] **Step 1 (Baseline):** Read static pressure
  across HEPA/Carbon pack with fan at max RPM.
  Record ΔP_clean.
- [ ] **Step 2 (Restriction Simulation):** Restrict
  airflow to Stage E by gradually blocking the filter
  chamber face with an inert, non-porous template
  plate.
- [ ] **Step 3 (Alert Threshold):** Monitor pressure
  transducer output. Verify that when ΔP increases
  to ≥ 450 Pa over ΔP_clean, a **Filter Restriction
  Alert** fires on the local operator display.
- [ ] **Step 4 (Actuator Loopback):** Confirm that
  the system automatically sends a pulse train to
  the automated mechanical shaker assembly (if
  equipped) or flags an immediate lockout command
  to the milling spindle bus.
- [ ] **Step 5 (Reset Check):** Remove the restriction
  template. Verify differential pressure drops back
  to baseline and the alert state auto-clears within
  3 seconds.

### Protocol 1.3 — Acidic Ingress Interlock (Sump pH & Gas Phase)

Verifies the system can protect its structural hull
from chemical degradation caused by halogenated
polymer exhaust.

- [ ] **Step 1 (Sump Calibration):** Calibrate the
  Stage D wet sump pH probe using standard buffer
  solutions (pH 4.0 and pH 7.0). Re-insert probe
  into recirculating fluid loop.
- [ ] **Step 2 (Acid Injection):** Using a precision
  pipette, slowly introduce 0.1M HCl solution
  directly into the Stage D sampling well to simulate
  acidic bypass.
- [ ] **Step 3 (E-Stop Trigger):** Observe the
  telemetry bus. The moment the reading dips below
  pH 5.5, the system must execute an instantaneous
  **E-Stop Lockout**.
- [ ] **Step 4 (Line Isolation):** Verify via
  multimeter that the Pyrolysis Reactor core main
  power contactor has dropped open. The contactor
  must open physically and latch into a locked state;
  software-only overrides are a failure.
- [ ] **Step 5 (Neutralization Test):** Add sodium
  carbonate to return the sump to pH 7.0. Verify
  that the system *prohibits* a clear-fault command
  until a manual operator attestation code is
  entered.

### Protocol 1.4 — Noise Fault Masking Interlock

Ensures acoustic alarms remain audible above ambient
fan and compressor noise.

- [ ] **Step 1 (Noise Floor Measurement):** Fire up
  all fan, pump, and compressor modules to maximum
  operating velocity. Place a calibrated sound level
  meter at the primary operator station. Record
  baseline dBA level.
- [ ] **Step 2 (Acoustic Injection):** Use an
  integrated test function to fire the audible
  emergency alarm horn.
- [ ] **Step 3 (Audibility Check):** Measure the
  combined acoustic output. The alarm signal must
  maintain a minimum margin of ≥ 10 dBA above the
  operating noise floor recorded in Step 1.
- [ ] **Step 4 (Optical Redundancy):** While the
  alarm is firing, verify that high-intensity visual
  strobes activate across all facility quadrants
  simultaneously.
- [ ] **Step 5 (Supervisor Attestation):** Unplug
  the primary horn to simulate acoustic alarm failure.
  Verify that the local microphone detects the
  missing signal and instantly flags a network
  supervisor warning.

### Test Execution Matrix

Use this table to record physical verification cycles
before updating File State Spec Gates to 4/6.

| Test ID | Targeted Interlock | Expected Software State | Hardware Action Verified? | Response Latency | Pass / Fail |
|---|---|---|---|---|---|
| **V4-AS-01** | VOC Breakthrough (<85%) | System Fault 04 | Heating Relay Drops Open | ________ ms | [ ] P  [ ] F |
| **V4-AS-02** | Pressure Blinding (≥450 Pa) | Filter Restriction Alert | Spindle Lockout Active | ________ ms | [ ] P  [ ] F |
| **V4-AS-03** | Sump Acid Ingress (pH < 5.5) | Core E-Stop Lockout | Contactors Mechanically Tripped | ________ ms | [ ] P  [ ] F |
| **V4-AS-04** | Alarm Audibility Margin (<10 dB) | Acoustic Masking Warning | Visual Strobes Triggered | ________ ms | [ ] P  [ ] F |

### Post-Verification Action

If all four protocols achieve Pass status:

1. Append verified checklist data to the
   `Admin/Verification_Gates_LF.md` log tracking
   repository.
2. Update the Spec Gates field in File State from
   3/6 to 4/6.
3. Shift Body Stability from Transitional to Stable
   for sections covered by Gate 4 verification.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Modeling | Variant 4 marine claimed 10–100 atm range with 20–50% power uplift | Physically untenable — isothermal compression to 100 atm requires massive work; 150W compressor cannot overcome hydrostatic pressure | Deep-sea compression is a separate power class. v0 marine variants cap at less than 5 atm | Analogous | Yes |
| May 2026 | Audit Review | Stage D described without thermal sink | Hot exhaust heats scrubbing liquid until it cannot quench — hidden failure mode | Thermal sink is not optional; must be explicitly sized to exhaust heat load | Analogous | Yes |
| May 2026 | Anecdotal | Positive pressure insight from dusty-environment cab filtration | Cabin filters fail rapidly under high dust load without pre-filter | Sacrificial pre-filter protecting main filter dramatically extends service life; positive pressure enclosure protection is Variant 0 | Analogous | Yes |
| 2026-05-23 | Audit Review | Noise hazard absent from prior versions | Continuous fan/compressor noise omitted from safety doctrine despite known industrial hearing damage risk | Noise added to Safety Advisory, Design Philosophy, and Monitoring sections. Fault alarm audibility verification added | Analogous | Yes |
| 2026-05-31 | Field Data / Audit | Raw direct-to-carbon routing of pyrolysis outgassing | Instantaneous tar blinding of activated carbon media from heavy oil fractions, paraffins, and waxes | A multi-stage fractional condensation loop must precede chemical scrubbing to knock down heavy fractions | Empirical | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### AS-001 — 500W power budget not validated against Forge demand baseline

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-31                                       |

**Description:** Whether 500W worst-case scrubber
draw (surface/shallow variants) is compatible with
Forge power budget at bootstrap and nominal modes.
Thermal sink power is not yet validated in this loop.

**Why It Matters:** If scrubber + thermal sink exceeds
20% of bootstrap power budget, the Forge cannot operate
the scrubber at full capacity during bootstrap mode —
which means hot operations cannot proceed. The scrubber
is a prerequisite, not an optional load.

**Resolution Path:** Cross-reference against
`Operations/Energy.md` Power Demand stub. Flag if
scrubber + thermal sink exceeds 20% of bootstrap
budget. Payment via Specification — once first
operational power draw is measured, move energy
estimates to Measured.

---

### AS-002 — Marine bubble-column deep-sea variant deferred

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-31                                       |

**Description:** Detailed specification for deep-sea
Variant 4+ (greater than 50m / 5 atm) remains
undefined.

**Why It Matters:** Deep-sea operation is a
`Tests/Leviathan_testing.md` deployment requirement.
Without a specification, Leviathan cannot operate
the scrubber at depth.

**Resolution Path:** Deep-sea variant routes to
`Admin/Trajectories.md` v2/v3 as a separate
power-class problem requiring a dedicated compression
module. Discharge via Trajectory — not in v0 scope.

---

### AS-003 — Scrubber waste stream and sensor thresholds not yet calibrated

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | Yes — blocks Chemistry validation per `Unknowns.md` |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-31                                       |

**Description:** Saturation thresholds have been
bound to a multi-point differential diagnostic grid
(PID VOC, ΔP, and Sump pH). Real-world chemical
baseline data is now required to clamp the
operational float margins.

**Why It Matters:** Without calibrated thresholds,
the interlock system operates on estimated values.
An incorrectly set threshold fires too early (false
positives halt operations) or too late (real
saturation passes undetected). AS-003 blocks
chemistry validation per `Unknowns.md`.

**Resolution Path:** Run automated calibration
sweeps during first hot-pyrolysis validation testing
to map clean baseline deltas. The Gate 4 Cold
Verification Harness must execute
first — it validates interlock logic before hot
calibration begins. Payment via Specification once
first hot-pyrolysis run produces calibration data.

---

### AS-004 — Noise exposure limits and hearing conservation program undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-05-23                                       |
| Last Reviewed | 2026-06-08                                       |

**Description:** Continuous fan and compressor noise
levels during Air Scrubber operation have not been
empirically characterized. `Admin/Safety_Protocols.md`
addresses general hearing conservation doctrine and
PPE requirements, but no site-specific SPL survey
or formal hearing conservation program for Air
Scrubber operations exists.

**Why It Matters:** If actual SPL during scrubber
operation exceeds safe exposure limits, current PPE
specification may be insufficient. The Protocol 1.4
noise fault masking interlock in the Gate 4 Cold Verification Harness section requires
a measured noise floor baseline — this unknown blocks
that calibration step.

**Resolution Path:**
- Measure SPL at all operator positions during
  scrubber operation — fan, pump, and compressor at
  max operating velocity.
- Cross-reference against `Admin/Safety_Protocols.md`
  consequence categories and hearing conservation
  doctrine.
- Verify fault alarm audibility against measured
  noise floor per Protocol 1.4.
- Payment via Specification — once SPL is measured
  and alarm audibility confirmed, move Protocol 1.4
  requirement to Measured and close cross-reference
  with SP-003.

---

### Resolution Log

- 2026-07-19: **Stage D/E cross-reference correction (Grok flag, cross-checked
  against source, human-directed).** `Architecture/Chemistry.md` CE-006 had
  directed chlorine off-gas from a candidate acid-sourcing pathway
  (`Challenges/Closed_Loop_Feedstock.md` CLF-004) toward this file's Stage E
  KMnO₄ chemisorption bed — verified against a primary manufacturer's product
  catalog that this bed does not target Cl₂ (it's an oxidizing chemisorbent
  for reducing-species VOCs; Cl₂ is already an oxidizer). Added a cross-reference
  note to Stage D directing chlorine-generating processes there instead, with
  caustic (NaOH) dosing — Stage D's existing recirculating wet-column architecture
  is already the correct mechanism, no new stage required. Scoped Stage E's
  hardware precedent note to clarify it does not cover chlorine. Added a worked
  example to Waste as a Managed Output noting the resulting sodium hypochlorite
  liquor as a reuse-potential case, cross-referenced to new CE-007. No change to
  Stage D or Stage E's existing operational doctrine for other gas streams.

- 2026-05-04: `Stratification_Chamber_v0.md`
  reference removed. `Material_Separation_Gate_v0.md`
  substituted.
- 2026-05-06: Variant 4 depth scope corrected from
  10–100 atm to less than 5 atm for v0. Deep-sea
  variants routed to `Admin/Trajectories.md`. Thermal
  sink requirement added to Stage D. Saturation Fault
  monitoring requirement added. Variant 0 added.
- 2026-05-23: Retrofit to `Admin/File_Template.md`
  structure. File State, Scope Boundary, Assumptions,
  Abandoned Paths, Drift Indicators sections added.
  Noise hazard added to Safety Advisory, Design
  Philosophy, Monitoring, and AS-004. Integration
  hook references updated to canonical folder-prefixed
  paths.
- 2026-05-31: Integrated Amendment and Field Note
  addenda into core body. Stage C updated with
  fractional condensation prerequisite. Stage E
  updated with KMnO₄ chemisorption mandate. AS-003
  bound to automated interlock sensor matrix.
  Flashback arrestors and corrosion isolation material
  updates added. Promoted Spec Gates to 3/6.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from `Verification_Gates_LF.md`
  to `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary updated — `Admin/Safety_Protocols.md`
  now exists and owns noise exposure limits / hearing
  conservation program (was listed as "planned").
  Integration Hooks updated to include
  `Admin/Safety_Protocols.md`. Gate 4 Cold
  Verification Harness integrated as Section IX —
  moved from raw append to formal body section with
  proper heading hierarchy and formatting. Sidecar
  entries expanded to full field table format. AS-004
  Last Reviewed updated; now cross-references
  `Admin/Safety_Protocols.md`. Open Unknowns updated
  to 4 (AS-004 remains open; site SPL not yet
  measured).
- 2026-07-12: Stray "Section IX" roman-numeral prefix removed from the
  Gate 4 Cold Verification Harness heading and its four live in-body
  references (this Resolution Log entry above is left unchanged as an
  accurate historical record of what the section was called on
  2026-06-08). No other body section in this file uses roman-numeral
  headings, so the "IX" was a leftover artifact from the raw-append
  integration described above, not an intentional numbering scheme.
  Reordered Abandoned Paths and Drift Indicators to after Auditor Notes
  & Unknowns, per template order — they previously sat between Active
  Disputes and Auditor Notes & Unknowns. No other content changed.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| May 2026 | Variant 4 deep-sea scope at v0 power class | Compression work to 100 atm is physically untenable at 100–150W; separate power class required | Yes — at v2/v3 |
| May 2026 | Stage D without explicit thermal sink specification | Hidden failure mode — water heats to ineffectiveness without thermal rejection path | No |
| May 2026 | Direct-to-carbon routing of pyrolysis outgassing | Instantaneous tar blinding of filter media confirmed by hardware data — fractional condensation prerequisite is permanent doctrine | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Saturation Fault monitoring requirement removed,
  bypassed, or decoupled from the differential PID
  sensor matrix
- Negative pressure safety boundary doctrine
  weakened or removed
- Flashback arrestor requirements omitted from
  combustible outgassing lines
- Thermal sink requirement removed from Stage D
- Noise hazard removed from Safety Advisory, Design
  Philosophy, or Monitoring sections
- 500W power budget claimed as validated without
  active power measurement data
- Variant 4 depth scope expanded beyond less than
  5 atm without an autonomous power class
  reallocation
- Gate 4 Cold Verification Harness removed or
  results amended without physical re-test
- Spec Gates advanced to 4/6 without all four
  protocols achieving Pass status in Test
  Execution Matrix

**Compound Drift Rule:** If multiple indicators
activate simultaneously, halt autonomous audit
progression and escalate for human review.

# Electronics.md — Salvaged Electronics & Logic Integration

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Electronics.md governs the trust boundary for all
> autonomous forge systems. A salvaged component that
> passes electrical testing may still carry compromised
> firmware, backdoored logic, or covert surveillance
> capability. Hardware supply chain compromise is a
> documented real-world threat — not a theoretical one.
> No salvaged MCU, controller, or programmable device
> enters forge systems without a Logic-Zero wipe and
> firmware provenance log. See EL-006.
>
> CNC milling of old PCBs produces fiberglass
> microdust, copper particulate, BFR (Brominated Flame
> Retardant) dust, and resin decomposition products.
> Respiratory protection and Air Scrubber operation
> are required during all PCB milling operations.
> See EL-005 and `Operations/Air_Scrubber.md`.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-09 (multi-agent), actioned 2026-05-19; revised 2026-06-08  |
| Auditor          | Claude — Retrofit/Auditor; Gemini — Synthesizer (CF-001 parameters) |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*High risk reflects hardware supply chain compromise
as a documented threat, not a theoretical one. Salvage
electronics from unknown provenance — including consumer
electronics, discarded industrial equipment, and imported
hardware with unknown firmware — are credible attack
vectors for embedded malicious logic, backdoored
controllers, and covert surveillance capability. A
compromised salvaged MCU integrated into forge systems
propagates to every autonomous decision, ethical
constraint, and watchdog behavior the forge depends on.
Electronics.md is the trust-anchor document for the
entire governance substrate.*

---

## Scope Boundary

**This file DOES define:**
- Non-destructive harvesting protocols for salvaged
  electronic components — desoldering standards,
  integrity checks, component identification
- Firmware trust doctrine — reflashing requirements,
  provenance logging, Logic-Zero wipe protocols
  before integration into forge systems
- PCB fabrication methods at v0 — CNC milling,
  laser etching, toner transfer, dead-bug wiring
- Soldering standards for both salvaged component
  integration and new fabrication
- Forge-Standard interface adapter layer — common
  interface enabling salvaged components to
  integrate across forge generations
- TMR hardware implementation — wiring, voter
  circuit, component selection, architectural
  diversity requirement
- Hardware watchdog doctrine — minimum behaviors,
  heartbeat enforcement, neutral-state enforcement
- Dual-use awareness for electronic components —
  annotation standard and escalation paths
- Fault response and Support Raft integration
- Toxic dust and BFR emission profile doctrine
- Counterfeit and remarked component detection
  doctrine

**This file DOES NOT define:**
- TMR as architectural philosophy or framework
  taxonomy (`Architecture/Cognitive_Frameworks.md`
  Framework D)
- Ethical policy governing dual-use escalation
  (`Admin/Ethical_Constraints.md`)
- Confidence collapse states and split-brain
  doctrine (`Architecture/Cognitive_Frameworks.md`)
- Air scrubber hardware specification or waste
  stream chemistry (`Operations/Air_Scrubber.md`)
- Component taxonomy and graduation rules
  (`Architecture/Components.md`)
- Leviathan mission logic or autonomy architecture
  (`Tests/Leviathan_testing.md`)
- Cryptographic key management or root-of-trust
  infrastructure (not yet assigned — EL-006)
- Full autonomous governance law
  (`Admin/Ethical_Constraints.md`)
- Forge-Net network implementation
  (`Architecture/Forge_Net.md`)
- Facility siting for electronics work areas
  (`Architecture/Facilities.md` — FA-001)

---

## File Purpose

Electronics.md governs the recovery, validation,
fabrication, and integration of electronic
components within the Lazarus Forge. It is the
trust-anchor document for the forge's governance
substrate — ethics enforcement, hardware watchdogs,
TMR voting, sensor truth, and AI containment all
depend on the integrity of the electronic systems
this file governs.

The document treats salvaged electronics not as
convenient parts but as potential threat vectors.
A salvaged integrated circuit that passes electrical
testing may still carry compromised firmware,
backdoored logic, or covert surveillance capability
embedded during manufacture. Hardware supply chain
compromise is a documented real-world threat, not
a theoretical one. The forge processes electronics
from unknown provenance — discarded industrial
equipment, imported consumer hardware, and mixed
e-waste — and must treat all of it as potentially
hostile until validated.

At v0, Electronics.md establishes three foundational
capabilities: non-destructive harvesting of salvaged
components with integrity verification, in-house PCB
fabrication when commercial boards are unavailable,
and a TMR architecture with hardware watchdog
enforcement that constrains autonomous behavior even
during total cognitive collapse. Firmware trust
doctrine — requiring Logic-Zero wipes and provenance
logging before any salvaged MCU enters forge systems
— is the primary security boundary between recovered
hardware and trusted infrastructure.

The forge also acknowledges that electronic component
production is a future capability trajectory. As
forges grow and specialize, some will develop
electronics manufacturing capability. The high
specificity of that work means individual forge
instances will naturally diverge in capability based
on local environment and community needs. This file
governs the current recovery and integration scope.
Manufacturing capability is a trajectory item for
later versions.

If this file disappeared, the forge would have no
doctrine for validating salvaged electronics before
integration, no hardware watchdog standard, no TMR
implementation guidance, and no firmware trust
boundary. Every autonomous system the forge builds
would rest on unvalidated hardware of unknown
provenance.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Electrical and functional testing detects component damage and degradation — not firmware compromise or embedded malicious logic | Component triage doctrine; electrical testing standard practice | Low | Firmware trust doctrine (EL-006) fully defined and validated — electrical testing acknowledged as insufficient alone |
| ASM-002 | Salvaged microcontrollers from different donor boards are sufficiently architecturally diverse for TMR independence — shared silicon errata or thermal history does not invalidate independence | TMR doctrine; diversity requirement stated but not yet validated | Low | First TMR prototype characterizes actual independence — correlated failure testing required per EL-007 |
| ASM-003 | AI agents using different models provide sufficient diversity for multi-agent consensus — training data overlap does not produce systematic correlated errors on forge-relevant engineering questions | Multi-agent consensus doctrine; model diversity assumed | Low | Correlated AI failure mode study completed per CF-002 — actual overlap in engineering reasoning characterized |
| ASM-004 | Salvaged components entered the waste stream through legitimate use rather than targeted placement — the salvage stream is not actively seeded with compromised hardware | Threat model; salvage assumed passive not targeted | Low | High-value forge operations attract targeted hardware supply chain attacks — threat model must be reassessed |
| ASM-005 | The hardware watchdog timer is itself uncompromised — a discrete hardware implementation is assumed architecturally simple enough to resist firmware attack | Watchdog doctrine; hardware implementation assumed trustworthy | Medium | Watchdog compromise detected or design found to include programmable elements vulnerable to firmware attack |
| ASM-006 | Chemical etch waste, BFR dust, and solder fumes can be safely managed with available Air Scrubber and containment capability | PCB fabrication doctrine; cross-reference `Operations/Air_Scrubber.md` | Medium | EL-005 toxic dust profile characterized — containment capability confirmed or found insufficient |
| ASM-007 | Desoldering yield rates justify the harvesting overhead — sufficient components survive non-destructive harvest to make the process economically viable | Harvesting doctrine; yield rates unknown at v0 | Low | First operational harvesting cycle characterizes actual yield rate per component class |
| ASM-008 | Forge-Standard interface voltage levels and protocols are achievable with available salvaged components | Forge-Standard doctrine; interface compatibility assumed | Low | First Leviathan hardware iteration characterizes actual salvage compatibility with Forge-Standard spec |

*ASM-001 and ASM-004 are the most dangerous hidden
assumptions in this file. Electrical testing does not
detect firmware compromise — a perfectly functional
component with backdoored logic passes every electrical
test. Targeted hardware supply chain attacks plant
compromised components in expected salvage pathways.
ASM-002 and ASM-003 reflect the correlated failure
risk identified in CF-002 — diversity must be
demonstrated, not assumed. ASM-005 highlights the
recursive trust problem: a watchdog used to detect
compromise must itself be uncompromised. Discrete
hardware implementation with no programmable firmware
is the primary mitigation.*

---

> If the Leviathan units are the muscle, salvaged
> electronics are the nervous system — and the nervous
> system must be trusted before it is connected.

---

## I. Position in System Architecture

Electronics recovery sits between Component Triage
and Fabrication in the Forge flow:

- `Operations/Gate_02_Triage.md` — determines
  whether a board or component has recovery value
- **This document** — governs how recovered
  electronics are harvested, validated, fabricated
  into, and integrated
- `Architecture/Forge_flow.md` — gate logic applies;
  electronic components follow the same A→B→C→D
  routing as mechanical components

Electronic components are not exempt from the gate
sequence. A salvaged IC that cannot perform its
original function routes to Gate C (repurpose to
simpler task) or Gate D (material recovery — copper,
rare earth elements) just like any other component.

**Electronics as trust-anchor:**
Electronics.md governs more than salvage logistics.
The integrity of every autonomous decision, ethical
constraint enforcement, watchdog behavior, and TMR
vote depends on the hardware this file governs.
Compromise here propagates everywhere.

---

## II. Phase I — Non-Destructive Harvesting

### Component Triage & Identification

**The problem:** Mixed e-waste bins are high-entropy
environments. Part markings are worn, boards are
unlabeled, and AI vision systems can hallucinate
pinouts from ambiguous silk screen text.

**Visual fingerprinting:**
- Use AI vision agents to scan donor boards and
  match SMD markings against verified parts ledgers
- Cross-reference identified part numbers against
  confirmed datasheets before any assumption about
  pinout or function
- A hallucinated pinout kills the downstream
  component and potentially the board it is
  installed on — treat unverified pinouts as
  Placeholder until confirmed

**Integrity checks per component class:**

*ICs and microcontrollers:*
- Verify package type and pin count before
  desoldering
- Power-on test at rated voltage before removal
  where board can be safely energized
- Logic gate stress test after removal — if a
  salvaged MOSFET cannot maintain rated R_DS(on),
  relegate to non-critical auxiliary systems
- **Electrical testing detects damage, not
  compromise.** A component that passes all
  electrical tests may still carry malicious
  firmware or backdoored logic. See firmware
  trust doctrine below.

*Capacitors:*
- ESR measurement — high ESR indicates electrolyte
  degradation
- Capacitance check against rated value
- Visual inspection for bulging, leakage, or
  discoloration

*Transformers and inductors:*
- Winding resistance measurement
- Insulation resistance between primary and
  secondary
- Core inspection for cracks or saturation damage

**Counterfeit and remarked component detection:**
Salvage streams include counterfeit components —
recycled parts relabeled as higher-spec versions,
cloned chips with altered ROM behavior, and
fraudulent components with falsified datasheets.
Electrical testing alone does not detect counterfeits.

- Inspect date codes and lot markings for
  consistency — mismatched markings indicate
  remarking
- Cross-reference package markings against known
  manufacturer formatting — font, spacing, and
  logo details differ between genuine and
  counterfeit
- Test performance at rated limits — a counterfeit
  MOSFET labeled for higher current will fail
  at the genuine part's rated operating point
- Treat components from high-counterfeit-risk
  sources (certain market sectors, certain
  geographic origins) with elevated scrutiny
- See EL-008 for unresolved counterfeit detection
  doctrine

### Firmware Trust Doctrine

**Physical recovery of a chip does not guarantee
the integrity of its embedded logic.**

This is the primary security boundary for salvaged
electronics. A salvaged MCU, controller, or
programmable device that passes every electrical
test may still execute malicious firmware, contain
backdoored bootloaders, or perform covert
surveillance. Hardware supply chain compromise
has been documented in industrial controllers,
networking equipment, and consumer electronics
from multiple origins.

**Logic-Zero wipe protocol:**
Before any salvaged programmable device enters
forge systems:
1. Identify device as programmable — any MCU,
   FPGA, DSP, or controller with embedded firmware
2. Attempt full flash erase — confirm erase
   completes successfully
3. Reflash with known-good forge firmware from
   verified source
4. Verify flash contents match expected firmware
   hash before integration
5. Log provenance — device identifier, donor board
   source, wipe date, firmware version installed,
   operator

**Devices that cannot be wiped:**
Some devices have locked bootloaders, write-protected
flash, or hardware-enforced firmware. These cannot
be trusted for forge system integration.

- Locked bootloader devices route to material
  recovery (copper, rare earths) not component
  library
- Document locked device encounter — feed to
  EL-006 resolution path
- Do not attempt to bypass locked bootloaders
  in forge context — the risk of introducing
  exploit tools into the forge environment
  exceeds the component value

**Signed firmware (future — EL-006):**
Full cryptographic firmware signing and root-of-trust
verification is a future capability. At v0, hash
verification of known-good firmware images is the
minimum acceptable practice. Cryptographic
infrastructure is a trajectory item. See EL-006.

### Desoldering Protocols — Non-Destructive Harvesting

Controlled heat is the difference between a
recovered component and a destroyed one.

**Lead-free solder (most post-2006 boards):**
- Reflow temperature: 220–250°C *(Analogous —
  standard lead-free reflow profiles)*
- Use PID-controlled hot air or iron — salvaged
  PID controllers are acceptable if calibrated
- Dwell time at temperature: minimize; silicon
  dies delaminate under sustained heat

**Leaded solder (pre-2006 and some industrial
boards):**
- Reflow temperature: 183–200°C *(Analogous)*
- Lower thermal stress — preferred for sensitive
  components

**Desoldering sequence:**
1. Identify component orientation and any polarized
   pins before heat application
2. Apply heat evenly — avoid thermal gradient
   across package
3. Remove component cleanly — no rocking or
   twisting under heat
4. Inspect pads on donor board — pad lift indicates
   excessive heat or mechanical stress
5. Clean component leads with isopropyl alcohol
   before testing

**Mechanical desoldering (bulk recovery):**
- For boards with no individual component value,
  bulk solder recovery via controlled furnace
  reflow is acceptable
- Components survive this process inconsistently
  — treat bulk-recovered components as
  unknown-state until tested
- Bulk recovery feeds material stream, not
  component library
- **Toxic emissions warning:** Bulk furnace
  reflow of old PCBs produces BFR outgassing,
  lead fumes, and resin decomposition products.
  Air Scrubber must be operational. Operator
  respiratory protection required. See EL-005.

---

## III. Phase II — Substrate Recovery & PCB Fabrication

### Copper Recovery & Substrate Preparation

- Salvaged copper-clad laminates (FR4, CEM-1,
  or equivalent) from donor boards or raw stock
- Clean substrate: remove existing traces via
  chemical strip or mechanical abrasion
- Inspect for delamination, moisture damage, or
  warping before use
- Copper purity adequate for PCB use does not
  require high-grade source material — recovered
  copper sheet or clad is acceptable

### PCB Fabrication Methods (v0 Scope)

**CNC milling (primary v0 method):**
- Mill trace isolation channels directly into
  copper-clad substrate
- No chemical etch required — suitable for salvage
  environment with limited chemical handling
- Trace width limited by end mill diameter —
  typically 0.3–0.8mm for v0 tooling *(Placeholder
  — depends on available mill bits)*
- G-code generated from EDA files or hand-routed
  for simple circuits
- Suitable for: motor controllers, sensor
  interfaces, power distribution, logic boards
- **Toxic dust warning:** CNC milling of old PCBs
  produces fiberglass microdust, copper particulate
  aerosol, BFR dust, and resin decomposition
  products. Respiratory protection and Air Scrubber
  operation required during all milling operations.
  Cross-reference: `Operations/Air_Scrubber.md`,
  EL-005.

**Laser etching:**
- CO2 or diode laser removes copper selectively
- Faster than CNC for fine features; requires
  laser with sufficient power for copper ablation
- Produces finer traces than CNC milling — useful
  for SMD component footprints
- Salvaged laser cutters are candidate tools
- **Fume warning:** Laser ablation of PCB material
  produces similar toxic byproducts to CNC milling.
  Air Scrubber operation required.

**Toner transfer / chemical etch (fallback):**
- Laser-printed mask transferred to copper-clad,
  etched with ferric chloride or similar
- Lowest equipment requirement — achievable with
  minimal tooling
- Chemical waste stream must be managed per
  `Operations/Air_Scrubber.md` contamination handling
- Ferric chloride neutralization: sodium carbonate
  (washing soda) produces iron hydroxide sludge
  — non-hazardous. Define neutralization protocol
  before first use. See EL-004.

**Dead-bug wiring (immediate integration):**
- Salvaged components wired point-to-point without
  a substrate
- Component bodies face upward, leads bent and
  soldered directly
- Valid for prototyping and single-purpose circuits
- Not suitable for high-vibration environments
  without mechanical stabilization

**Hybrid approach:**
- Reuse portions of original industrial boards —
  retain functional power stages or analog sections
- Wire new logic controllers directly onto existing
  infrastructure
- Reduces fabrication burden; leverages proven
  circuit sections

### Soldering Standards

Hand soldering is a core Forge skill. Quality
directly affects system reliability in salvaged
electronics.

**Joint quality criteria:**
- Shiny, smooth fillet — dull or grainy indicates
  cold joint (insufficient heat or movement during
  cooling)
- Full wetting of pad and component lead
- No bridging between adjacent pads
- No excess solder creating shorts or mechanical
  stress

**Flux management:**
- Flux residue is conductive in humid environments
  — clean with isopropyl alcohol after soldering
- No-clean flux acceptable for sealed enclosures;
  clean flux required for exposed boards

**SMD soldering (salvaged SMD components):**
- Solder paste + hot air preferred for small packages
- Fine-pitch ICs (< 0.5mm pitch) require
  magnification and steady technique
- Rework is expected — budget time for inspection
  and correction

**Through-hole soldering:**
- Standard for power components and connectors
- Lead clinch (bent lead after insertion) improves
  mechanical strength before soldering
- Wave soldering acceptable for production runs;
  hand soldering adequate for v0

---

## IV. Phase III — Modular Logic Bricks & Standardization

### Forge-Standard Footprint

Salvaged components have inconsistent form factors.
The Forge Standard defines an adapter layer — a
common interface that allows a salvaged 2024
controller to plug into a 2026 Leviathan chassis
without board redesign.

**v0 Forge-Standard interface (Placeholder — to
be defined with first Leviathan hardware iteration):**
- Power rail: 12V and 5V, common ground *(Placeholder
  — voltage levels pending Leviathan power spec;
  see EL-001)*
- Communication: I2C or UART as primary; SPI for
  high-bandwidth sensors
- Mechanical: standardized mounting hole pattern;
  connector gender defined per function

This standard does not require perfect components
— it requires predictable interfaces. A degraded
but functional controller that speaks I2C at 3.3V
can be adapted to any Forge-Standard slot.

### Hardware TMR Implementation

TMR implementation in hardware is this file's
domain. TMR as architectural philosophy and
framework taxonomy belongs to
`Architecture/Cognitive_Frameworks.md` Framework D.

**Architecture:**
- Three independent logic blocks wired to
  cross-check each other
- A voter circuit compares the three outputs
- If two of three agree, the majority output
  is executed
- If all three disagree (split-brain), the system
  enters Fail-Safe State

**Architectural diversity requirement:**
True TMR requires that the three systems fail
independently. Three identical damaged systems
are not true redundancy — they share failure
modes.

Diversity mechanisms:
- **Silicon diversity** — different MCU families
  (ARM vs AVR vs PIC) have different silicon
  errata and failure modes
- **Firmware diversity** — different firmware
  implementations of the same logic reduce
  shared code vulnerability
- **Power-path diversity** — independent power
  supplies prevent common-mode power failure
- **Thermal diversity** — different physical
  locations reduce shared thermal stress
- **Procurement diversity** — components from
  different donor boards reduce shared batch
  defects and firmware lineage

**Correlated failure risk:**
Salvage-derived TMR systems are especially
vulnerable to hidden common-mode failures:
- Same production batch → same silicon errata
- Same donor equipment → same thermal history
- Same firmware source → same vulnerability
- Same geographic origin → same supply chain
  compromise risk

The false independence claim — that three systems
from different boards are automatically independent
— has been removed. Independence must be
demonstrated through adversarial testing, not
assumed from physical separation. See EL-007.

**Voter implementation:**
- Hardware voter (discrete logic gates) — more
  reliable, harder to compromise, less flexible
- Software voter (hardened script on separate MCU)
  — more flexible, lower component count, vulnerable
  to MCU compromise
- v0 recommendation: software voter on a separate
  dedicated MCU that has undergone Logic-Zero wipe
  and firmware verification per EL-006
- Hardware voter is the v1+ target for
  safety-critical applications

### Hardware Watchdog Doctrine

*CF-001 minimum standard defined 2026-06-08
following Gemini Synthesizer analysis. Confidence:
Analogous — parameters require validation against
first hardware prototype. Closes CF-001 resolution
path from Architecture/Cognitive_Frameworks.md.*

The hardware watchdog is the final backstop when
all software and firmware fails. It must be
independently trustworthy — see ASM-005.

**Layer 1 Minimum Standard (CF-001):**

Layer 1 must enforce an un-bypassable hardware
**windowed watchdog timer (WDT)**. The following
parameters define the minimum acceptable
implementation:

| Parameter | Requirement | Confidence |
|-----------|-------------|------------|
| Heartbeat window | τ = 50 ms — valid heartbeat must be received within this window | Analogous |
| Heartbeat type | Cryptographic — not a simple pulse. Layer 2 must present a valid token that Layer 1 can verify without trusting Layer 2 firmware | Analogous |
| Timeout action | Physically cut power to all primary H-bridge gate drivers — no software-mediated shutdown | Analogous |
| Mechanical result | All actuators forced to passive spring-return neutral state — no uncommanded movement possible | Analogous |
| Bypass | None permitted — watchdog cannot be disabled, paused, or extended by any software layer | Permanent |
| Implementation | Discrete hardware — RC timer, comparator, relay. No programmable firmware. No microcontroller | Permanent |
| Observability | Watchdog state physically observable — LED indicator or mechanical flag visible without powering any logic | Permanent |

**Why cryptographic heartbeat:**
A simple pulse can be spoofed by a compromised
Layer 2 — the logic board sends the pulse even
when its decision-making is corrupted, providing
false assurance. A cryptographic heartbeat requires
Layer 2 to produce a valid token, which it cannot
do if its firmware integrity has been compromised
beyond the token-generation function. This is a
meaningful additional barrier, not a guarantee.
See EL-006 for firmware trust limits.

**Why 50ms:**
The 50ms window is derived from analog deep-sea
AUV watchdog implementations. It is short enough
to catch a locked logic board before it can
complete a damaging actuation cycle, and long
enough that normal control loop latency does not
produce false trips. *(Analogous — validate against
first hardware prototype; adjust if control loop
latency characterization requires a wider window.)*

**Why H-bridge gate drivers:**
Cutting power to H-bridge gate drivers removes
drive capability from all motors and actuators
simultaneously. It does not rely on any actuator's
own brake or hold circuit — those are Layer 2
constructs. The gate driver cutoff is the last
hardware boundary before Layer 0 spring-return.

**Discrete hardware implementation:**
A watchdog implemented as a simple RC timer,
comparator, and relay circuit has no firmware
to compromise. If no valid heartbeat token resets
the timer within τ = 50ms, the relay opens,
cutting H-bridge gate power, and all actuators
return to spring-loaded neutral under passive
mechanical force. This is the physical enforcement
of Layer 0 in `Architecture/Cognitive_Frameworks.md`.

*A compromised watchdog that appears functional
is worse than no watchdog — it provides false
assurance while removing the last safety backstop.
Discrete implementation with no programmable
elements is the primary mitigation against the
recursive trust problem documented in ASM-005.*

Cross-reference: `Architecture/Cognitive_Frameworks.md`
CF-001, Layer 0 mechanical truth doctrine,
Layer 1 hardware watchdog enforcement.

### Multi-Agent Consensus (MAC)

MAC is distinct from hardware TMR. Conflating
the two produces false confidence in both.

**Hardware TMR:** Three physical systems with
independent silicon, firmware, and power paths.
Tolerates random hardware faults and transient
corruption. Vulnerable to correlated failures
from shared manufacturing origin or firmware.

**Multi-Agent Consensus (MAC):** Three AI models
asked the same engineering question. Majority
agreement increases confidence. Does not tolerate
correlated reasoning failures from shared training
data. Not a substitute for hardware safety systems.

MAC is a verification step, not a safety mechanism.
It improves the quality of engineering decisions
before implementation. Hardware TMR constrains
behavior after implementation. Both are needed.
Neither replaces the other.

**MAC limitations:**
- Three models trained on overlapping data share
  blind spots — consensus on a wrong answer is
  still a wrong answer
- MAC operates pre-implementation; hardware TMR
  operates during execution
- MAC requires human review when models disagree
  significantly — disagreement is signal, not noise
- MAC cannot substitute for physical safety
  constraints (Layer 0)

Cross-reference: `Architecture/Cognitive_Frameworks.md`
Framework D, CF-002 correlated AI failure modes.

---

## V. Fault Response & Support Raft Integration

When TMR fails — either through hardware fault or
split-brain — the Support Raft is the resolution
mechanism.

| Fault State | TMR Outcome | Action |
|---|---|---|
| Nominal | 3/3 or 2/3 consensus | Continue mission |
| Logic conflict | 1/1/1 split or 0/3 | Enter Stasis Mode — see `Tests/Support_Raft.md` |
| Critical offline | Voter failure | Automatic Raft retrieval via magnetic grapple |
| Bit-flip detected | Single voter anomaly | Flag, log, continue on 2/3 consensus |
| Firmware integrity failure | Hash mismatch detected | Halt all autonomous action — Logic-Zero and reflash before restart |

**Logic-Zero Fail-Safe:**
When a Leviathan unit enters split-brain:
- Mechanical systems lock in neutral state via
  hardware watchdog relay — no uncommanded movement
- Recovery beacon activates — low-frequency pulse
  for Support Raft magnetic grapples
- Unit enters Stasis per `Tests/Support_Raft.md`
  Stasis Mode protocol
- Collected material offloaded to Material
  Separation Gate while unit is in triage —
  mission continues

**Guardian Protocol (future):**
The Raft simulates the Leviathan's next move on
a local digital twin before the unit physically
executes it. If simulation shows collision or
logic loop, Raft overrides and pulls unit into
dock. Route to `Admin/Trajectories.md` v2/v3 scope.

---

## VI. Dual-Use Awareness in Electronics

Electronic components are dual-use by nature —
the same sensor that detects material composition
can detect human presence. The same motor
controller that drives a conveyor can drive a
weapon system.

Apply the Dual-Use Annotation Standard from
`Architecture/Components.md` to all salvaged
electronics:
- **Low** — general purpose logic, passive
  components, power regulators: standard handling
- **Medium** — high-power switching, precision
  timing, RF modules: log provenance, flag if
  patterns emerge
- **High** — guidance logic, targeting sensors,
  detonation circuits: Full Stop — route to
  `Admin/Ethical_Constraints.md`

The Component Triage Station 0 ethical flag
(per `Operations/Gate_02_Triage.md` Principle 6)
applies to electronic components as much as
mechanical ones.

---

## VII. Integration Hooks

- `Operations/Gate_02_Triage.md` — electronic
  components follow the same gate routing;
  Station 1 is the primary electrical triage
  station
- `Architecture/Forge_flow.md` — gate logic
  governs; electronic waste follows Reduction →
  Purification for material recovery
- `Operations/Air_Scrubber.md` — chemical etch
  waste stream, flux fumes, solder smoke, BFR
  dust, and CNC milling particulate require
  scrubbing
- `Operations/Gate_05_Separation_Thermal.md` —
  recovered copper and trace metals from PCBs
  are feedstock candidates
- `Tests/Leviathan_testing.md` — TMR architecture
  and fault response are primary test targets
  for Leviathan autonomy
- `Tests/Support_Raft.md` — fault response
  integration; Raft as TMR resolution
  infrastructure
- `Admin/Ethical_Constraints.md` — dual-use
  electronic components route here for escalation
- `Operations/Energy.md` — salvaged power
  electronics are candidate contributors to
  Forge energy infrastructure
- `Architecture/Cognitive_Frameworks.md` —
  TMR philosophy (Framework D), CF-001 watchdog
  standard, CF-002 correlated failure modes

---

## VIII. Guiding Axioms

- A salvaged IC with a known pinout is worth
  more than a new one with an assumed one.
- Solder is cheap. Delaminated pads are not.
- Physical recovery of a chip does not guarantee
  the integrity of its embedded logic.
- Three voters who disagree are safer than one
  voter who is always confident.
- Diversity matters more than quantity in
  redundancy.
- The watchdog must be trusted before it can
  be trusted to protect.
- The nervous system of the Forge is built from
  the nervous systems we threw away — but it
  must be verified before it is connected.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| — | — | — | — | No operational entries yet — pre-build | — | — |
| 2026-05-09 | Audit Review | TMR presented as providing statistical independence for salvaged components from different donor boards | Salvaged components may share production batch, thermal history, firmware lineage, or supply chain origin — independence is not guaranteed by physical separation | Architectural diversity requirement made explicit — silicon, firmware, power-path, thermal, and procurement diversity all required for true TMR independence. Correlated failure risk logged as EL-007 | Analogous | Yes — first TMR prototype must include adversarial correlated failure testing |
| 2026-05-09 | Audit Review | AI multi-agent consensus treated as equivalent to hardware TMR | MAC and hardware TMR are distinct mechanisms with different failure modes and different operating stages. Conflating them produces false confidence in both | MAC section separated from hardware TMR section. MAC is a pre-implementation verification step. Hardware TMR is a runtime safety constraint. Neither replaces the other | Analogous | No — distinction is permanent doctrine |
| 2026-05-09 | Audit Review | Electrical testing treated as sufficient validation for salvaged programmable components | A component passing all electrical tests may carry compromised firmware, backdoored logic, or covert surveillance capability | Firmware trust doctrine added — Logic-Zero wipe and firmware hash verification required before any salvaged programmable device enters forge systems. EL-006 logged | Analogous | Yes — validate Logic-Zero protocol against first salvaged MCU batch |
| 2026-05-09 | Audit Review | Hardware watchdog treated as a software concern | If the watchdog itself is compromised or programmable, it provides false assurance while removing the last safety backstop | Discrete hardware watchdog implementation specified — no programmable firmware. RC timer and relay circuit as the minimum architecture. ASM-005 documents the recursive trust problem | Analogous | Yes — validate watchdog hardware design before first autonomous operation |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts currently active.
Design tensions exist (hardware vs software voter,
discrete vs programmable watchdog, v0 hash
verification vs full cryptographic signing) but
all are deferred pending first hardware prototype.
Tracked as unknowns, not disputes. Revisit after
first TMR prototype operational.*

---

## Auditor Notes & Unknowns

### EL-001 — Forge-Standard voltage and interface spec not yet defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The specific voltage rails,
communication protocols, and mechanical connector
standard that define the Forge-Standard interface
are not yet defined. Cannot be finalized until
Leviathan unit power envelope is specified.

**Why It Matters:** Without a defined standard,
salvaged components cannot be validated for
Forge-Standard compatibility. Every integration
requires custom adaptation rather than
plug-compatible assembly.

**Resolution Path:**
- Define as Placeholder pending Leviathan hardware
  iteration. Inputs needed: LT-001 (Leviathan
  power envelope) and first physical prototype.
- Until defined, document current best-guess
  (12V/5V, I2C/UART) as Placeholder.
- Payment via Specification — once Leviathan
  hardware iteration defines power envelope,
  move to body as Analogous.

---

### EL-002 — PCB trace width and design rules not yet specified for v0 tooling

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Minimum trace width, clearance,
and via size achievable with actual v0 CNC or
laser tooling are unknown. Design rules cannot
be stated until tooling is characterized.

**Resolution Path:**
- Run test cuts on scrap copper-clad with
  available tooling. Measure actual minimum
  feature size.
- Document as Measured once characterized.
  Placeholder until first tooling test.
- Payment via Specification — once tooling is
  characterized, move to Section III as Measured.

---

### EL-003 — TMR voter implementation not yet specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The voter circuit that arbitrates
between three TMR logic blocks has not been
specified beyond the conceptual level. Hardware
voter vs. software voter choice is unresolved.

**Why It Matters:** The voter is the single point
of failure in a TMR system — if the voter fails
or is compromised, the redundancy benefit is lost.
The implementation choice (hardware vs. software)
determines the trust properties of the entire
architecture.

**Resolution Path:**
- First Leviathan prototype defines the voter
  implementation. v0 recommendation: software
  voter on dedicated, Logic-Zero'd MCU.
- Hardware voter is v1+ target for safety-critical.
- Payment via Specification — once first TMR
  prototype is built and voter tested, move to
  Section IV as Analogous.

---

### EL-004 — Chemical etch waste stream management not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Ferric chloride and other etch
chemistries produce hazardous waste streams that
require neutralization and disposal protocols
not yet defined.

**Why It Matters:** Improperly disposed etch waste
contaminates water and soil. Neutralization is
simple but must be defined before first use.

**Resolution Path:**
- Define neutralization protocol: sodium carbonate
  to iron hydroxide sludge (non-hazardous).
- Define disposal path for neutralized sludge.
- Cross-reference `Operations/Air_Scrubber.md`
  waste stream handling.
- Payment via Specification — once protocol
  defined and first use validates it, move to
  Section III as Analogous.

---

### EL-005 — Toxic dust and BFR emission profile not characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Actual particulate composition and
BFR emission rates during CNC milling and bulk
furnace reflow of salvaged PCBs have not been
characterized. Current doctrine relies on analogous
industrial data.

**Why It Matters:** BFR dust and fiberglass
microdust are serious respiratory hazards. If
actual emissions exceed what the Air Scrubber can
handle, current PPE and scrubber doctrine is
insufficient — unknown until characterized.

**Resolution Path:**
- Characterize emissions during first CNC milling
  and bulk reflow operations.
- Cross-reference `Operations/Air_Scrubber.md`
  capacity against measured emission profile.
- Payment via Specification — once characterized,
  move PPE and scrubber requirements to Section II
  as Measured.

---

### EL-006 — Firmware trust and reflashing validation not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Security                             |
| Blocking      | Yes — prerequisite for first salvaged MCU integration |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The cryptographic key management
infrastructure and root-of-trust architecture
required for full firmware signing and verification
are not defined. Current practice (hash verification
of known-good images) is the minimum interim
standard.

**Why It Matters:** Hash verification is better
than nothing but is not a full root-of-trust. A
compromised known-good image produces a matching
hash. Full cryptographic signing with hardware key
storage is the v1+ target. Until then, the firmware
trust boundary has a known gap.

**Resolution Path:**
- Define minimum v0 practice: hash verification
  from trusted source, provenance log mandatory.
- Define v1+ target: cryptographic firmware signing,
  hardware key storage, root-of-trust architecture.
- Cross-reference `Admin/Security_Protocols.md`
  for key management infrastructure.
- Payment via Specification — once v0 minimum
  practice is validated against first MCU batch,
  move to Section II as Analogous. Full resolution
  deferred to v1+ cryptographic infrastructure.

---

### EL-007 — Correlated failure modes in homogeneous salvage TMR not characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The independence assumption in
hardware TMR — that three systems from different
donor boards fail independently — has not been
validated. Salvage-derived components may share
production batch, thermal history, firmware
lineage, or supply chain origin, creating
correlated failure modes that bypass TMR
protection.

**Why It Matters:** TMR only works if failures
are independent. Correlated failures produce
simultaneous incorrect outputs that appear as
consensus. Three components that fail the same
way at the same time produce a confident wrong
answer rather than a detectable disagreement.

**Resolution Path:**
- First TMR prototype must include adversarial
  correlated failure testing — deliberately
  induce failure in one system and verify others
  remain independent.
- Characterize actual diversity between selected
  components — silicon family, firmware source,
  thermal history.
- Cross-reference `Architecture/Cognitive_Frameworks.md`
  CF-002 for AI consensus correlated failure
  parallel.
- Payment via Specification — once independence
  is demonstrated through adversarial testing,
  move to Section IV as Measured.

---

### EL-008 — Counterfeit salvage component detection doctrine not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Security                             |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Counterfeit and remarked
components — recycled parts relabeled as higher
spec, cloned chips with altered ROM behavior,
fraudulent components with falsified datasheets
— are present in salvage streams. Detection
criteria and doctrine beyond provisional guidance
in Section II are not yet defined.

**Why It Matters:** A counterfeit MOSFET labeled
for higher current than it can handle fails under
load in ways that may not be immediately apparent.
A cloned MCU with altered ROM behavior may pass
electrical testing while executing subtly different
logic. Counterfeit components undermine the
reliability assumptions the forge's TMR and
watchdog systems depend on.

**Resolution Path:**
- Define detection criteria per component class
  — marking inspection protocols, performance
  testing at rated limits, cross-reference with
  known counterfeit databases.
- Define high-risk source categories — certain
  market sectors and geographic origins have
  higher counterfeit prevalence. Document and
  apply elevated scrutiny.
- Cross-reference EL-006 firmware trust doctrine
  — counterfeit MCUs with altered ROM are a
  distinct threat class from firmware compromise
  but require similar mitigation.
- Payment via Specification — once detection
  criteria are defined and validated against
  first operational harvesting cycle, move to
  Section II as Analogous.

---

### Resolution Log

- 2026-05-19: EL-001 through EL-004 — Reformatted
  from prose to structured sidecar table format.
  Content preserved, provenance dates maintained.
- 2026-05-19: EL-005, EL-006, EL-007 — Migrated
  from multi-agent audit 2026-05-09. Reformatted
  to structured tables.
- 2026-05-19: EL-008 — New entry. Counterfeit
  component detection doctrine gap identified
  in meta-audit. Provisional detection guidance
  added to Section II.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from `Admin/Forge_Audit_Kit.md`
  to `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary UNK-006 reference updated to
  `Architecture/Facilities.md` FA-001 (PC-002).
- 2026-06-08: Hardware Watchdog Doctrine section
  expanded with CF-001 minimum standard — τ=50ms
  windowed WDT, cryptographic heartbeat requirement,
  H-bridge gate driver cutoff, spring-return neutral
  enforcement, discrete hardware implementation
  requirement. Parameters from Gemini Synthesizer
  analysis; confidence Analogous pending first
  hardware prototype validation. Closes CF-001
  resolution path from
  Architecture/Cognitive_Frameworks.md.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-09 | Electrical testing treated as sufficient for component validation | A component passing all electrical tests may carry compromised firmware, backdoored logic, or covert surveillance capability. Electrical testing detects damage, not compromise | No — firmware trust doctrine is permanent. Electrical testing is necessary but not sufficient |
| 2026-05-09 | TMR independence assumed from physical separation of donor boards | Components from different boards may share production batch, thermal history, firmware lineage, or supply chain origin. Physical separation does not guarantee statistical independence | No — architectural diversity requirement is permanent. Independence must be demonstrated |
| 2026-05-09 | MAC (multi-agent AI consensus) conflated with hardware TMR | MAC and hardware TMR are distinct mechanisms with different failure modes and different operating stages. Conflating them produces false confidence in both | No — permanent distinction. MAC is pre-implementation verification. Hardware TMR is runtime safety |
| 2026-05-09 | Software watchdog treated as equivalent to hardware watchdog | A software watchdog can be compromised by the same firmware failure it is meant to detect. It provides false assurance while removing the last safety backstop | No — discrete hardware watchdog is permanent doctrine for safety-critical applications |
| 2026-05-19 | Salvage stream treated as passive — not actively seeded with compromised hardware | Hardware supply chain compromise has been documented in industrial controllers, networking equipment, and consumer electronics. High-value forge operations are credible targets | Reconsider threat model as forge operations grow in strategic value — threat level scales with target value |

---

## Drift Indicators

The following conditions trigger mandatory re-audit
of this file. All canonical drift indicators from
`Admin/File_Template.md` apply. The following are
additional local triggers specific to Electronics.md:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Salvaged programmable device integrated without Logic-Zero wipe and firmware verification | Permanently abandoned path — EL-006 prerequisite. Physical recovery does not guarantee firmware integrity |
| TMR implemented with components from same production batch or firmware source without diversity verification | Independence must be demonstrated, not assumed. Correlated failure risk bypasses TMR protection |
| MAC results used as safety system substitute rather than pre-implementation verification | MAC and hardware TMR are permanently distinct. MAC cannot substitute for runtime physical safety constraints |
| Hardware watchdog implemented with programmable firmware rather than discrete hardware | Discrete hardware implementation is permanent doctrine for safety-critical watchdog — programmable watchdog creates recursive trust problem |
| CNC milling or bulk furnace reflow performed without Air Scrubber operation and respiratory protection | EL-005 Critical — BFR dust and fiberglass microdust are serious health hazards. Air Scrubber prerequisite |
| Dual-use High components processed without escalation to `Admin/Ethical_Constraints.md` | Dual-use escalation is mandatory — no local override permitted |
| Counterfeit detection skipped for components from high-risk source categories | EL-008 — elevated scrutiny is doctrine for high-risk sources, not optional |
| Forge-Standard interface revised without cross-validation against EL-001 and LT-001 | Interface standard changes propagate to all connected forge instances — unilateral revision creates hidden incompatibility |
| Locked-bootloader devices routed to component library rather than material recovery | Locked bootloader devices cannot be firmware-verified — they cannot be trusted for forge integration |
| Electronics.md scope expands to include cryptographic key management without EL-006 resolution | Key management infrastructure has no owner — absorbing it here without resolution creates specification pressure on an Exploration document |

### Canonical Drift Triggers

*All mandatory re-audit conditions from
`Admin/File_Template.md` Section 11 apply without
exception. Local triggers above are additive,
not substitutes.*

# Energy.md — Energy Strategy & Governance

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Salvaged electrochemical batteries with unknown state-of-health present catastrophic thermal runaway and toxic hydrofluoric acid outgassing risks. Containment and isolation protocols are mandatory before any salvaged battery bank is commissioned (EV-003). Do not install salvaged storage in unventilated or uninsulated enclosures. Air Scrubber operation is strictly required during any battery handling, charging, or thermal failure event. **When in doubt, isolate the battery bank and do not proceed.**
>
> Multi-source operation (grid + motor-generators + biogas + solar + thermal recovery) introduces voltage, frequency, and ripple instability risks. The Energy Arbitration Layer (EAL) and Source Stability & Harmonization Layer are proposed doctrine, drafted this session and not yet audited — treat as structural specification, not a validated safety mechanism, until it clears Gate 1.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                                |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-31 (original, Gemini); EGL/Storage Model expansion drafted 2026-08-01, not yet audited |
| Auditor          | Gemini (original, 2026-05-31); Grok — drafted Energy Governance Layer expansion (human-directed, 2026-08-01), pending Gate 1 pass |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*High risk reflects uncharacterized salvaged battery thermal behavior (EV-003) and the absence of measured power-demand data (EV-001). The Energy Governance Layer adds proposed constitutional structure for demand/generation/arbitration/thermal routing; it has not passed Gate 1 (Fallacy Check) or Gate 2 (Physical Plausibility) and does not yet carry the confidence its presence in this file might imply. Spec Gates remains at 1/6 — drafting the layer is not the same as clearing a gate for it.*

---

## Scope Boundary

**This file DOES define:**
- Design philosophy for incremental energy integration at v0–v1
- Energy lifecycle progression from external grid reliance to partial thermal/waste recovery
- Real-world generation interlocks for syngas and biomass loops
- Calibrated power mode envelopes and actionable voltage sag protocols
- Hard-coded physical protection parameters and isolation boundaries for salvaged batteries
- Primary and secondary falsifiable performance metrics
- **Energy Governance Layer (EGL)** — Demand Model, Generation Model, Energy Arbitration Layer (EAL), Thermal Integration Architecture (TIA) *(proposed, drafted 2026-08-01, not yet audited)*
- Storage Model & Battery Governance (expansion of EV-003)
- Source Stability & Harmonization Layer
- Energy Capability Trajectory (v0 → v3)

**This file DOES NOT define:**
- Deep-environment battery degradation physics modeling (→ `Tests/Leviathan_testing.md` LT-002)
- Leviathan power envelope specification (→ `Tests/Leviathan_testing.md` LT-001)
- Mechanical drawings for battery containment structures
- Detailed chemistry sorting algorithms for unknown cells (→ `Operations/Gate_02_Triage.md`)
- Full cryptographic key management or root-of-trust for energy controllers (cross-ref `Operations/Electronics.md` EL-006)
- Detailed superconductivity materials science (exploratory horizon only)
- The canonical meaning of Spec Gates 1–6 (→ `Admin/Verification_Gates_LF.md` — this file does not redefine what a gate is)

---

## File Purpose

This file defines the energy strategy and governance substrate for the Lazarus Forge. The Forge is energy-intensive by nature — reduction, thermal separation, fabrication, and autonomous operation all draw significant power. Energy.md provides a plausible, incremental path from external grid dependency toward partial self-sufficiency through salvaged and waste energy sources, without claiming energy independence that has not been demonstrated.

Its primary function as a cross-reference anchor is the Power Demand stub and the (proposed) Energy Governance Layer — a demand-side and allocation baseline that allows Leviathan power envelope scoping, per-module energy accounting, and safety interlocks to integrate against a common reference point, even before actual figures are measured.

If this file disappeared, the repository would have no shared energy accounting baseline, no demand-side anchor for cross-module power budgeting, and no drafted arbitration or thermal-coupling doctrine for future validation. Every autonomous system the Forge builds would rest on unvalidated power assumptions.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Grid power is available at v0 bootstrap site | v0 terrestrial deployment context | Medium | Off-grid or remote deployment confirmed — bootstrap strategy changes |
| ASM-002 | Salvaged motor-generators can be back-driven to produce usable electricity | Standard electromechanical reversibility principle | Medium | First salvaged motor-generator characterized for output efficiency |
| ASM-003 | Biogas output can overcome parasitic overheads via thermal recovery | Bound to 35°C digestate tank rule | Medium | EV-002 baseline measurements prove net-negative balance |
| ASM-004 | Salvaged batteries retain sufficient usable capacity to serve as energy buffer | Common salvage practice; SoH unknown | Low | First salvaged battery bank characterized for SoH and cycle capacity |
| ASM-005 | Waste heat from Spin Chamber and other thermal processes is available for opportunistic reuse | `Operations/Gate_05_Separation_Thermal.md` exhaust profile | Low | SC-007 resolved — exhaust heat load characterized |
| ASM-006 | Discrete or minimal-firmware controllers can implement EAL priority logic without introducing new programmable attack surface | Cross-ref `Architecture/Cognitive_Frameworks.md` CF-001 (hardware watchdog minimum standard) / discrete watchdog doctrine, as implemented in `Operations/Electronics.md` | Low | First EAL hardware prototype validated against adversarial firmware compromise |

---

## Design Philosophy

- **Energy demand is acknowledged, not hidden:** Power budgets must reflect real electromechanical and thermal loads, not idealized values.
- **Early stages prioritize learning over efficiency:** Robust, basic containment and crude power transformation trump high-efficiency micro-grids at v0 bootstrap.
- **Salvage-first applies to power systems as well:** Repurposing industrial automotive alternator blocks and salvaged battery cells is the primary hardware path.
- **Multiple small contributors are preferred over single large sources:** Spreading generation across solar, syngas, and grid links prevents single-point failure cascades.
- **Energy is a proposed constitutional substrate:** The design intent is for every other subsystem to stand on the Energy Governance Layer once it is validated. Until then, this is drafted doctrine, not an operating guarantee.

---

## Energy Lifecycle

```
[Stage 1: Bootstrap] ──► Primary reliance on external Grid Power / Watchdog Loops
         │
         ▼
[Stage 2: Supplement] ──► Modular Solar Integration + Salvaged Motor-Generators
         │
         ▼
[Stage 3: Recovery]  ──► Regulated Biogas Digestion + Syngas Generation
         │
         ▼
[Stage 4: Loop Close]──► Opportunistic Thermal Recovery (Gate 05 Heat Sink Exchanger)
         │
         ▼
[Stage 5: Trajectory]──► Partial self-sufficiency → hybrid remote → full loop closure (v2–v3)
```

---

## Energy Sources & Generation Interlocks (v0–v1 Scope)

### 1. Grid Power (Bootstrap)

Primary early-stage energy source. Enables primary reduction, separation, and control systems. Treated as a temporary dependency, not a permanent fixture.

### 2. Salvaged Motor-Generators

Recovered motors repurposed as generators back-driven via turbines, belts, or engines.

> ⚙️ **Real-World Interlock — The Tar Minimization Rule**
> Open-loop biomass gasification is strictly prohibited for raw processing unless a multi-stage mechanical particulate filter and oil-bubbler quenching system are placed inline. Unscrubbed syngas will gum internal combustion valves within less than 12 operational hours, triggering a critical mechanical power failure cascade.

### 3. Anaerobic Digestion (Biogas)

Organic waste converted into methane-rich gas to drive generators or provide process heat.

> ⚙️ **Real-World Interlock — The Parasitic Biogas Threshold [Ref: EV-002]**
> Biogas generation cannot be accounted for as a net-positive primary energy source unless the ambient thermal temperature of the digestate tank exceeds 35°C via passive solar or thermal recovery streams. The electrical cost of continuous mechanical mixing and gas compression must not exceed 22% of the total calculated methane output value.

### 4. Solar (Supplemental)

Modular photovoltaic panels with direct DC routing where possible. Offsets control and daytime utility loads to minimize peak grid draw spikes.

### 5. Thermal Recovery (Opportunistic)

Waste heat reused to stabilize or preheat incoming feedstocks and to feed TEG banks. Not counted as a primary grid input. Cross-reference: `Operations/Gate_05_Separation_Thermal.md` exhaust profile (SC-007).

---

## Energy Governance Layer (EGL) — Proposed Unified Architecture

**Status: Drafted 2026-08-01, not yet audited. Payment via Specification only — presence of this section does not constitute a validated operating guarantee.**

The Energy Governance Layer is a proposed model for how the Forge would consume, produce, route, recover, throttle, and safely shut down all energy flows — electrical and thermal — across every subsystem, once validated. It is intended as the constitutional backbone of the Forge's energy system, but it has not yet cleared even Gate 1 (Fallacy Check).

The EGL integrates four load-bearing components:

- **Demand Model** — what the Forge needs
- **Generation Model** — what the Forge produces
- **Energy Arbitration Layer (EAL)** — how the Forge allocates
- **Thermal Integration Architecture (TIA)** — how the Forge routes heat

Together they are intended to form a closed governance loop that prevents catastrophic brownouts, thermal runaway, generator stall, battery collapse, and cross-module instability.

### I. Closed Governance Loop (proposed)

1. Model Demand
   \[
   D(t) = L(t) + W(t) + S(t) + P_{\text{mode}}(t) + P_{\text{transient}}(t) + P_{\text{thermal}}(t)
   \]

2. Model Generation
   \[
   G_{\text{net}}(t) = \sum_i P_{i,\text{net}}(t)
   \]

3. Arbitrate Allocation
   \[
   P_{\text{alloc}}(t) = \text{EAL}(D(t), G_{\text{net}}(t))
   \]

4. Route Thermal Energy
   \[
   Q(t) = \text{TIA}(T_1, T_2, T_3, T_4)
   \]

This loop is designed to run continuously and, once validated, would form the Forge's real-time energy constitution.

---

### II. Demand Model — Consumption Architecture

#### Layer 1 — Baseline Rails (Non-Negotiable)

- **Logic Rail (L)**
  \[
  L(t) = L_{\text{base}} + L_{\text{sense}}(t)
  \]
  \(L_{\text{base}} \approx 10\text{–}15\,\text{W}\)

- **Watchdog Rail (W)**
  \[
  W(t) = W_{\text{fixed}} = 5\text{–}10\,\text{W}
  \]
  Must never brown out. Hard safety boundary (cross-ref `Architecture/Cognitive_Frameworks.md` CF-001).

- **Scrubber Rail (S)**
  \[
  S(t) = S_{\text{fan}} + S_{\text{compressor}} + S_{\text{diagnostic}}
  \]
  Typical v0 range: 50–150 W. Must remain operational during any hazardous process.

Governance constraint (proposed): If \(L(t) + W(t) + S(t)\) cannot be maintained, all other loads must be shed and Safe Halt entered.

#### Layer 2 — Operational Modes

| Mode              | Target Consumption          | Tolerable Voltage Ripple | Mandated Source Allocation                  | Actionable Sag Protocol                          |
|-------------------|-----------------------------|---------------------------|---------------------------------------------|--------------------------------------------------|
| Logic / Watchdog  | < 15 W baseline             | ±1%                      | Primary TEG / Isolated Lead-Acid Buffer     | Maintain state indefinitely; keep-alive telemetry |
| Mechanical Milling| 1.5 kW peak                 | ±5%                      | Hydro-Engine / Main Battery (SoH > 70%)     | Cycle spindle 50%; halt axis steppers            |
| Nominal           | 15–40 kW                    | ±5%                      | Grid / Scaled Generators + Air Scrubber     | Throttle feed rates; pause secondary axes        |
| Thermal Melt (G5) | 8.0 kW burst                | ±10%                     | Direct Generator / Biomass Syngas Loop      | Safety clamp; dump molten charge to safe crucible|

*Note: "G5" above refers to `Operations/Gate_05_Separation_Thermal.md`, not Spec Gate 5 (Cross-Reference Integrity) in `Admin/Verification_Gates_LF.md`. Retained from the original table; flagging to prevent conflation between the two G5 usages.*

#### Layer 3 — Transient Loads

- Motor inrush: \(k_{\text{motor}} = 3\text{–}7 \times P_{\text{rated}}\)
- Heater ramp and compressor start: 2–3 × steady-state
- Transient envelope must remain ≤ 1.25 × source peak rating.

#### Layer 4 — Thermal Loads

\[
P_{\text{thermal}}(t) = P_{\text{pump}} + P_{\text{fan}} + P_{\text{sink}} + P_{\text{coolant}}
\]

Typical v0 range: 50–300 W.

#### Full Demand Equation

\[
D(t) = L(t) + W(t) + S(t) + P_{\text{mode}}(t) + P_{\text{transient}}(t) + P_{\text{thermal}}(t)
\]

Proposed as the canonical reference for all energy budgeting, generator sizing, battery sizing, and safety interlocks — pending validation.

---

### III. Generation Model — Supply Architecture

#### Source Classes

| ID | Source                  | Equation / Notes                                      | Governance Constraint                          |
|----|--------------------------|---------------------------------------------------------|--------------------------------------------------|
| G₁ | Grid                     | \(P_{\text{grid}}(t) = P_{\text{contract}} - P_{\text{ripple}}\) | Bootstrap only; not assumed for v1+           |
| G₂ | Salvaged Motor-Generators | \(P_{\text{MG}}(t) = \eta_{\text{MG}} \cdot \tau(t) \cdot \omega(t)\) | Tar Minimization Rule mandatory               |
| G₃ | Biogas                   | \(P_{\text{biogas}}(t) = \eta_{\text{gen}} \cdot \dot{m}_{\text{CH}_4} \cdot LHV\) | Net-positive only if digestate > 35 °C and parasitic < 22% |
| G₄ | Solar                    | \(P_{\text{solar}}(t) = \eta_{\text{PV}} \cdot A \cdot I_{\text{solar}}(t)\) | Supplemental; offsets control loads           |
| G₅ | Thermal Recovery (TEG)   | \(P_{\text{thermal}}(t) = \eta_{\text{TEG}} \cdot Q_{\text{waste}}(t)\) | \(\eta_{\text{TEG}} \approx 3\text{–}7\%\); stabilizes baseline rails |

*Note: these G₁–G₅ source-class labels are local notation for this table only and are unrelated to Spec Gates 1–6.*

#### Net Generation

\[
G_{\text{net}}(t) = \sum_i P_{i,\text{net}}(t)
\]

where each \(P_{i,\text{net}}\) subtracts friction, cooling, mixing, compression, and charge-controller losses.

#### Source Stability & Harmonization (proposed)

- Bus voltage must remain within ±5% of nominal.
- Frequency deviation > 2% triggers mode downgrade.
- Ripple above threshold sheds P₄ loads first.
- No source may back-feed another without verified isolation.
- Priority order for source selection: Grid → MG → Biogas → Solar → Thermal.

---

### IV. Energy Arbitration Layer (EAL) (proposed)

#### Priority Classes

- **P₁ — Non-Negotiable Safety Rails**
  Watchdog, Logic, Air Scrubber, battery containment sensors, thermal-runaway detectors, emergency relays.
  If P₁ cannot be maintained → Immediate Safe Halt.

- **P₂ — Critical Operational Loads**
  Thermal quench pumps, Stage D/E monitoring, axis steppers during active milling, feedstock conveyors during thermal separation.

- **P₃ — Productive Loads**
  Milling spindle, Leviathan actuators, syngas compressors, biogas mixers.

- **P₄ — Opportunistic Loads**
  Thermal recovery pumps, non-critical sensors, auxiliary lighting, secondary logic nodes.

#### Arbitration Rules

\[
P1 > P2 > P3 > P4
\]

No exceptions. No software overrides — pending hardware validation of this claim (see ASM-006).

Canonical allocation (proposed):

\[
P_{\text{alloc}}(t) =
\begin{cases}
P_1 & \text{if } G_{\text{net}} < P_1 \\
P_1 + P_2 & \text{if } G_{\text{net}} < P_1 + P_2 \\
P_1 + P_2 + P_3 & \text{if } G_{\text{net}} < P_1 + P_2 + P_3 \\
P_1 + P_2 + P_3 + P_4 & \text{otherwise}
\end{cases}
\]

#### Mode Downgrade Engine

\[
\text{Thermal Melt} \rightarrow \text{Nominal} \rightarrow \text{Milling} \rightarrow \text{Logic}
\]

Hysteresis buffer \(\Delta\) prevents oscillation.

#### Failure Semantics

- Brownout (\(V_{\text{rail}} < V_{\text{min}}\)): shed P₄ → P₃ → downgrade mode.
- Two brownouts within 10 s → force Logic Mode.
- Safe Halt: P₁ maintained for 30 s; all other loads shed.
- Hard Shutdown (P₁ lost): Watchdog → H-bridge cutoff → mechanical neutral (Layer 0).

---

### V. Thermal Integration Architecture (TIA) (proposed)

#### Thermal Classes

- **T₁ Hazardous** — Spin Chamber exhaust, pyrolysis outflow, molten crucibles, battery runaway. Must be contained.
- **T₂ Process** — Stage C/D heating, digestate warming, quench loops.
- **T₃ Recoverable** — Jacket heat, motor casings, hydraulic loops → TEG path.
- **T₄ Ambient** — Enclosure, electronics bay, battery ambient. Triggers ventilation.

#### Routing Paths

- C₁ Containment (hazard → verified sink)
- C₂ Process (heat → required subsystem)
- C₃ Recovery (\(R_{\text{thermal}} = \eta_{\text{TEG}} \cdot Q_{\text{waste}}\))
- C₄ Dissipation (excess → ambient)

#### Thermal Arbitration

\[
T1 > T2 > T3 > T4
\]

If T₁ cannot be maintained → Safe Halt + Air Scrubber Max-Flow + H-bridge cutoff.

#### Thermal–Electrical Coupling

\[
P_{\text{thermal}}(t) = P_{\text{pump}} + P_{\text{fan}} + P_{\text{sink}} + P_{\text{coolant}}
\]

\[
R_{\text{thermal}}(t) = \eta_{\text{TEG}} \cdot Q_{\text{waste}}(t)
\]

Both terms feed the Demand Model and Generation Model.

---

## Electrochemical Battery Containment Protocol / Storage Model & Battery Governance [Ref: EV-003]

Salvaged battery state-of-health (SoH), cycle history, and remaining capacity are uncharacterized at v0. To safely leverage these assets without risking catastrophic structural fires, the following physical and governance rules apply:

- **Physical Isolation:** Salvaged lithium-ion or lead-acid cell packs must reside in an isolated, external, pressure-vented enclosure separated from primary computational nodes and volatile feedstocks by a minimum 2-hour fire-rated containment barrier.
- **The Over-Extraction Guard:** Discharge cut-off parameters must be locked via hard-coded physical voltage dividers at 3.0V per cell for lithium-class chemistry. This suppresses internal copper shunting and subsequent self-heating runaway during sub-nominal recharge cycles.
- **The Scrubber Prerequisite:** If any cell temperature probe registers greater than 55°C, the main battery disconnect relay must open immediately via hardware trip, and the `Operations/Air_Scrubber.md` variant 0 positive-pressure loop must automatically lock into max-flow mode to purge hydrofluoric acid gas byproducts away from human operators.
- **SoH Classification (proposed, v1 target):**
  – Class A: SoH ≥ 80%, usable for productive loads
  – Class B: 50–80%, restricted to opportunistic / buffer use
  – Class C: < 50% or unknown, material recovery only
- **Buffer Sizing (proposed):** Baseline rails must be supportable from isolated buffer for ≥ 30 minutes under Safe Halt conditions.
- **Degradation Tracking (proposed):** Cycle count and capacity fade logged; slope feeds falsifiable metrics.

*The Physical Isolation, Over-Extraction Guard, and Scrubber Prerequisite rules above are the original, audited EV-003 doctrine (2026-05-31) and remain load-bearing. The SoH Classification, Buffer Sizing, and Degradation Tracking items are new proposed extensions drafted 2026-08-01, not yet audited.*

---

## Hardware Power Mode Profiles [Ref: EV-001]

To prevent logic-loop crashes from supply-rail sag, all autonomous processing actions must align with verified hardware power envelopes. See Layer 2 — Operational Modes above for the current table (unchanged from the original values; folded in as part of the EGL Demand Model layer structure rather than duplicated as a separate table).

---

## Superconductivity Horizons (Exploratory / v1+)

### Philosophy & Strategic Value
Superconductivity represents a high-leverage multiplier for the Forge's core metric: **Value recovered per kWh**. Zero-resistance transmission, high-field magnets, efficient motors, and lossless energy storage could dramatically lower parasitic loads across reduction, fabrication, and Leviathan-scale operations. However, per the Forge doctrine, we treat this as an engineering target rather than a speculative miracle.

Key guiding principles drawn from disciplined analysis:
- **Superconductivity is a phase transition, not gradual resistance reduction.** Simply purifying materials or lowering scattering does not automatically produce a Cooper-paired condensate. This distinction guards against intuitive but unproductive optimization paths.
- **Ambient-pressure progress is the priority.** Cryogenic solutions have limited bootstrap utility in salvage/remote contexts. Records such as the 151 K ambient-pressure milestone (Hg-1223 metastable phase) highlight meaningful engineering headroom without extreme infrastructure.
- **Shift from discovery to architecture/engineering.** Quantum geometry, deliberate strain, and controlled metastable phases offer more practical levers than multi-element "cocktail" doping, which often leads to segregation, instability, or insulating byproducts.
- **Space metallurgy as a long-horizon enabler.** Microgravity and vacuum conditions can stabilize structures difficult on Earth, but they will not magically create superconductors — only enable deliberate engineering of candidate materials.

### Integration Pathways for the Forge
1. **Transmission & Distribution**
   Lossless or near-lossless power routing between gates and modules would improve overall energy accounting and enable distributed Leviathan deployments.

2. **Magnetic Systems**
   Stronger, more efficient magnets for separation (eddy currents, induction melting), motors/generators, and potential maglev internal logistics.

3. **Energy Storage & Recovery**
   Persistent current loops or high-efficiency SMES (Superconducting Magnetic Energy Storage) as buffers, complementing salvaged battery protocols.

### v0–v1 Guardrails & Falsifiable Gates
- **No dedicated R&D budget at v0–v1.** Monitor external progress and salvage opportunities only.
- **Test any candidate materials** via simple four-point probe resistance + basic susceptibility checks before integration.
- **Maintain fallback to conventional conductors.** All designs must support graceful degradation to copper/aluminum baselines.
- **Unknowns to Track** (link to main Unknowns.md):
  - SC-H1: Practical ambient-pressure materials viable below 200 K under Forge bootstrap constraints.
  - SC-H2: Salvage-compatible fabrication routes for superconducting wire/joints.
  - SC-H3: Net system-level kWh benefit after accounting for cooling/strain infrastructure.

### Cross-References & Migration Path
- Strong empirical or prototype success → migrate detailed implementation to **Engineering.md** (pragmatic fabrication focus).
- Ties to: `Operations/Gate_05_Separation_Thermal.md` (induction efficiency), `Tests/Leviathan_testing.md`, `Challenges/Critical_Minerals.md` (rare-earth magnet alternatives), and `Architecture/Cognitive_Frameworks.md` (emergent optimization of energy loops).

**Drift Indicator:** Treating superconductivity as assumed or near-term rather than exploratory triggers re-audit and potential removal of optimistic language.

---

## Energy Capability Trajectory (proposed)

| Stage | Horizon | Capability Target                                      | Key Gate                          |
|-------|---------|----------------------------------------------------------|--------------------------------------|
| v0    | Bootstrap | Grid + isolated buffer + basic motor-generators       | EV-001 measured, EV-003 enclosure validated |
| v1    | Hybrid  | Solar + regulated biogas + TEG banks + full EAL/TIA   | EGL passes Gate 1–2, multi-source stability demonstrated |
| v2    | Partial self-sufficiency | Closed thermal loops, remote-capable buffers         | Net-positive biogas under cold-start, SoH Class A banks |
| v3    | Loop closure | High-efficiency recovery + optional superconductivity | Full falsifiable kWh/kg economics, remote Leviathan support |

*Column header retained as "Key Gate" per original convention; entries here describe unknown-resolution and file-Spec-Gate milestones for this document only, not the canonical Verification Gates process.*

---

## Metrics (Falsifiable)

**Primary metric:** kWh consumed per kg of recovered usable output
("Usable output" = material that passes `Operations/Gate_02_Triage.md` electrical or mechanical verification.)

**Secondary indicators:**
- % energy supplied by recovered/salvaged sources
- Internal combustion generator uptime logs
- Storage capacity degradation slope
- Parasitic load ratio (biogas, motor-generators)
- Time spent in each operational mode and Safe Halt frequency

---

## Explicit Non-Goals (v0–v1)

- Total energy self-sufficiency or immediate off-grid autonomy
- Zero-greenhouse-emission operating targets
- Novel or experimental power generation physics
- Industrial-scale conversion efficiency optimization

---

## Lessons Learned

| Date       | Evidence Type   | What Was Tried                  | What Failed                          | What Was Learned                                      | Confidence | Revalidation Needed |
|------------|-----------------|----------------------------------|----------------------------------------|-----------------------------------------------------------|------------|----------------------|
| 2026-05-31 | Field / Audit   | Raw syngas combustion routing   | Valve gumming and internal carbon fouling within 12 hours | Multi-stage particulate filtration and oil-bubbler quenching are mandatory prerequisites | High       | No                   |
| 2026-08-01 | Architecture (drafted, unaudited) | Flat power budgeting without arbitration | Identified as a cascading-brownout risk under multi-source operation, in a proposed model not yet validated | A full Demand + Generation + EAL + TIA model was drafted as a candidate constitutional layer; it has not been audited or hardware-tested | Analogous  | Yes — Gate 1 pass, then first hardware validation |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-------------------|---------------------------|------|--------|-------|
| —  | No active disputes | —                          | —    | —      | —     |

---

## Auditor Notes & Unknowns

### EV-001 — Forge power demand uncharacterized at any operating mode

| Field         | Value                                                               |
|---------------|-----------------------------------------------------------------------|
| Status        | In Progress                                                           |
| Risk          | Medium                                                                |
| Priority      | Major                                                                 |
| Type          | Technical                                                             |
| Blocking      | Yes — blocks v1 operating cost model and `Admin/Economics.md` EC-002 |
| Owner         | `Operations/Energy.md`                                                |
| First Logged  | 2026-05-27                                                            |
| Last Reviewed | 2026-08-02                                                            |

**Description:** Actual consumption of the physical bootstrap hardware remains an estimate based on industrial analogs. The proposed Demand Model gives those estimates equation structure; measured data still does not exist.

**Why It Matters:** EV-001 is the demand-side anchor for all cross-module energy accounting. Without measured figures, every power budget claim — including every term in the proposed Demand Model — carries Placeholder confidence.

**Resolution Path:** Replace analog values in the Demand Model with real shunt-resistor / current-transformer telemetry as hardware validation completes. Payment via Specification once measured figures replace Placeholder values.

---

### EV-002 — Parasitic and thermal startup loads for biogas streams uncharacterized

| Field         | Value             |
|---------------|-------------------|
| Status        | In Progress       |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | `Operations/Energy.md` |
| First Logged  | 2026-05-27         |
| Last Reviewed | 2026-08-02         |

**Description:** Total net energy yield of anaerobic digestion loops is unmeasured under cold-start conditions.

**Resolution Path:** Enforce 35°C thermal interlock and 22% maximum compressor energy rule. Capture gas-flow meter data against input feedstock mass vectors during initial operational loops. Payment via Specification once first cycle data characterizes net yield.

---

### EV-003 — Salvaged battery thermal containment and ventilation strategy undefined

| Field         | Value                                              |
|---------------|-----------------------------------------------------|
| Status        | In Progress                                          |
| Risk          | High                                                 |
| Priority      | Critical                                             |
| Type          | Technical / Safety                                    |
| Blocking      | Yes — before enclosed battery bank commissioning     |
| Owner         | `Operations/Energy.md`                                |
| First Logged  | 2026-05-27                                            |
| Last Reviewed | 2026-08-02                                            |

**Description:** Unknown state-of-health battery modules present catastrophic thermal runaway vectors. Full containment and ventilation doctrine not yet physically validated. A proposed SoH classification and buffer-sizing extension has been drafted but not audited or physically validated.

**Resolution Path:** Physical isolation rules, locked 3.0V/cell hard-guards, and Air Scrubber Max-Flow auto-trigger remain codified and audited. Move to resolved once the external fire-rated enclosure physical build passes cold safety audit. Payment via Specification once enclosure is physically verified.

---

### Resolution Log

- 2026-05-27: EV-001–003 logged and structured.
- 2026-05-31: Spec Gate 1 baseline; Tar Minimization and 35°C/22% interlocks integrated; EV-001 bound to hardware envelope table; EV-003 physical isolation codified.
- 2026-06-08: Navigation Anchors and Verification Ref corrected; sidecar format normalized.
- 2026-07-12: Abandoned Paths / Drift Indicators reordered per template.
- 2026-08-01: Grok drafted a full Energy Governance Layer expansion (Demand + Generation + EAL + TIA), a Storage Model expansion of EV-003, and an Energy Capability Trajectory, claiming Spec Gates advanced to 2/6 and File Status → Transitional.
- 2026-08-02: **Corrective merge, human-directed.** Verified the 2026-08-01 draft against source and against `Admin/Verification_Gates_LF.md`/`Admin/File_Template.md` before integrating. Merged in: EGL (Demand/Generation/EAL/TIA), Storage Model SoH classing, Source Stability & Harmonization, Energy Capability Trajectory — all explicitly marked **proposed / not yet audited**, distinct from the original 2026-05-31 audited body. Cut/corrected: (1) `Status` and `Body Stability` fields reverted to valid `Admin/File_Template.md` enum values (Draft / Transitional) — the draft had written a Body-Stability value ("Transitional") into the Status field and invented a non-canonical Body Stability value ("Improving"); (2) Spec Gates reverted 2/6 → 1/6 and the draft's invented file-local "Spec Gates Definition" table (which redefined G1–G6 as content milestones) removed — Gate 2 was self-declared "Closed (structural)" with no Gate 1 Fallacy Check or Gate 2 Physical Plausibility pass by a different agent, and the canonical G1–G6 meanings are fixed by `Admin/Verification_Gates_LF.md`, not locally redefinable per file; (3) restored the Superconductivity section's original Integration Pathways and Cross-References & Migration Path content, which the draft had cut despite claiming full preservation — stripped only the non-substantive citation-card render artifacts; (4) corrected ASM-006's citation from `Operations/Electronics.md` CF-001 to `Architecture/Cognitive_Frameworks.md` CF-001 (owning file), noting Electronics.md as implementer; (5) added inline notes disambiguating the table's "G5" (Gate_05_Separation_Thermal.md) and the Source Classes table's "G₁–G₅" labels from canonical Spec Gates 1–6, to prevent future conflation. Open Unknowns unchanged at 3; no new unknowns registered for the proposed EGL pending a real Gate 1 pass.

---

## Abandoned Paths

| Date       | Path                                      | Why Abandoned                                                              | Reconsider? |
|------------|--------------------------------------------|-------------------------------------------------------------------------------|-------------|
| 2026-08-02 | File-local redefinition of Spec Gates 1–6 | Conflicts with canonical gate definitions in `Admin/Verification_Gates_LF.md`; would desync this file's gate semantics from the rest of the repo | No — use canonical gates only |

---

## Drift Indicators

Mandatory re-audit conditions:

- Power Demand mode definitions revised without updating the hardware power envelope limits or Demand Model equations
- Biogas counted as a net-positive source if digestate core temp drops below 35°C for sustained periods
- Salvaged battery storage commissioned in an enclosed space without a verified 2-hour fire barrier or independent ventilation routing
- Hard-coded lithium voltage cutoff shifted below 3.0V via software override patches
- The falsifiable primary metric (kWh per kg) is replaced with non-measurable efficiency targets
- EAL priority ordering (P₁ > P₂ > P₃ > P₄) altered or software-bypassed, or any part of the EGL is treated as validated/operative before it passes Gate 1
- Thermal Class T₁ loads routed without verified containment path
- Superconductivity treated as assumed or near-term rather than exploratory
- Multi-source hybrid configuration commissioned without Source Stability & Harmonization validation
- Spec Gates 1–6 redefined locally within this file rather than deferring to `Admin/Verification_Gates_LF.md`

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

*End of Energy.md*

# Gate_01_Intake

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Gate_01_Intake is the system's first and only opportunity
> to catch hazards before they enter the processing stream.
> Hazards missed here propagate through every downstream gate.
> Energetic materials — batteries, capacitors, compressed gas
> — must be identified and discharged before any further
> processing. Chemical and radiological hazards cannot be
> reliably detected by visual inspection alone. See GI-002
> and GI-003. When in doubt, hold. The cost of a missed
> hazard is always higher than the cost of a hold.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-19                                                          |
| Auditor          | Claude — Skeptic/Auditor (actioning ChatGPT audit 2026-05-19)       |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Entry protocol for all items entering the Forge system
- Safety screening doctrine — hazards, energetics,
  biological, chemical, and radiological identification
- Physical document handling — scan on arrival,
  digital retention, network contribution
- Digital reference database lookup doctrine —
  primary automatic, secondary operator-assisted,
  tertiary unknown protocol
- Item tagging and provenance recording at entry
- Parts list generation doctrine for known assemblies
- Unknown item hold and inspect protocol before
  escalation to Human/AI Oversight Gate
- Fastener and small component recovery doctrine —
  preserve before reduction
- Integration with Architecture/Forge_Net.md reference
  database as primary lookup source
- Handoff to Classification and Triage
  (Operations/Gate_02_Triage.md)

**This file DOES NOT define:**
- Classification and triage workflow detail
  (Operations/Gate_02_Triage.md)
- Reference database content, schema, or maintenance
  (Architecture/Forge_Net.md — GI-001)
- Cognitive save state format or portability
  (Architecture/Forge_Net.md — FN-005)
- Network sync protocol for intake records
  (Architecture/Forge_Net.md)
- Detailed contamination handling beyond Intake
  screening (Architecture/Forge_flow.md Defined Terms,
  Operations/Gate_02_Triage.md)
- Energetic material disposal doctrine
  (not yet assigned — GI-002)
- Provenance tracking system specification
  (Admin/Ship_of_Theseus.md grain system)
- Air handling during intake screening
  (Operations/Air_Scrubber.md)
- Facility siting and intake area safety
  (Architecture/Facilities.md — FA-001)

---

## File Purpose

Gate_01_Intake is the entry point for all items entering
the Lazarus Forge system. Every component, assembly, and
material that the Forge will ever process passes through
here first. Intake does not make recovery decisions — it
makes the information available for recovery decisions to
be made correctly downstream.

The primary functions are safety screening, identification,
and tagging. Safety screening catches hazards before they
reach gate logic — a battery missed at Intake becomes a
Reduction incident; a lead-contaminated item missed at
Intake becomes an alloy contamination problem. Identification
connects the item to whatever is known about it — manuals,
parts lists, repair history — so that downstream gates have
the best available information rather than starting blind.
Tagging creates the provenance record that follows the item
through every subsequent gate.

At v0, Intake is primarily a human-judgment process
supported by digital lookup. The operator screens for
hazards, initiates the reference database query, scans
any physical documentation, generates a preliminary parts
list for known assemblies, and tags the item before
handoff to Classification and Triage. Automation is a
future capability, not a v0 assumption.

If this file disappeared, items would enter the Forge
system without safety screening, without identification,
and without provenance records. Hazards would propagate
downstream. Gate decisions would be made without context.
The grain system would have no starting point. The network
would receive no intake data to learn from.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | A human operator is present and capable of performing safety screening at every intake event | v0 human-judgment primary doctrine | Medium | Automated hazard detection validated and deployed — human presence becomes optional |
| ASM-002 | The reference database contains sufficient coverage of common appliances and assemblies to produce useful lookup results at v0 | Digital lookup primary path; database content not yet defined — see GI-001 | Low | Reference database content scope defined and validated against representative v0 feedstock samples |
| ASM-003 | Physical documents arriving with items contain recoverable information worth scanning — degradation is the exception, not the rule | Scan-on-arrival doctrine; document arrival is rare but signals owner care | Low | Scan yield data from first operational cycle shows documents are consistently too degraded to be useful |
| ASM-004 | Operators can identify most hazardous materials through visual inspection and basic testing at Intake | Safety screening doctrine; visual indicators exist for common hazards | Low | Intake safety incident occurs from a hazard that visual inspection cannot detect — detection capability must be augmented |
| ASM-005 | Items arrive in processable condition — not requiring special handling before entering the Intake protocol | Entry protocol — no pre-Intake triage exists | Medium | Item arrives in condition that cannot safely enter Intake without prior intervention — triggers pre-Intake protocol creation |
| ASM-006 | Provenance data recorded at Intake is compatible with the grain system format in Admin/Ship_of_Theseus.md | Tagging doctrine — grain system format not yet specified | Low | Grain system format defined — Intake tagging schema must be cross-validated and updated to match |
| ASM-007 | Fastener and small component recovery during Intake processing is net-positive at v0 scale — handling overhead is justified by component value | Junk drawer doctrine; inter-forge trade ecology | Low | Operational data shows recovery overhead exceeds component value at v0 scale — recovery threshold adjusted upward |

*Four Low confidence assumptions reflect genuine uncertainty
about detection capability, database coverage, document yield,
and grain system compatibility. ASM-004 is the most safety-
critical — visual inspection cannot detect lead, radiation,
or many chemical contaminants. Detection capability beyond
human visual inspection should be treated as a prerequisite
for unsupervised Intake operation. ASM-006 is load-bearing
for the Admin/Ship_of_Theseus.md grain system — Intake
tagging and grain format must be cross-validated before
either is treated as stable.*

---

## 1. Entry Protocol

All items entering the Lazarus Forge system pass through
Gate_01_Intake before any gate logic is applied. No item
proceeds to Classification and Triage without completing
Intake. No exceptions.

**Operator cognitive fatigue doctrine:**
Intake is cognitively expensive — ambiguity-heavy,
judgment-dependent, and interruption-heavy. A fatigued
operator is a systemic hazard propagation vector at
the system's first safety barrier.

- **Shift duration guidance** — sustained Intake
  operation beyond 2–3 hours without a break
  degrades judgment quality. *(Placeholder —
  validated against first operational cycle)*
- **Second-review triggers** — after three
  consecutive unknown or ambiguous items, a
  second operator reviews the next item before
  routing. Repeated ambiguity indicates either
  unusual feedstock or operator fatigue.
- **Mandatory escalation after repeated unknowns**
  — five consecutive unknown items without
  resolution triggers escalation to Human/AI
  Oversight Gate regardless of individual item
  status. Pattern recognition, not just item
  assessment.
- **Stop Intake authority** — any operator may
  suspend Intake operations without justification
  required. Queue accumulation never overrides
  operator judgment. Items in hold are safe.
  Items routed incorrectly are not.

**Intake backlog collapse doctrine:**
Intake can become a bottleneck under real salvage
conditions. Queue collapse is not theoretical — it
is an expected operational condition.

- **Maximum unresolved hold threshold** — when
  hold queue exceeds available physical storage,
  new intake is suspended until hold queue clears.
  *(Placeholder — threshold defined by physical
  facility capacity)*
- **Hold queue triage** — items in hold are
  reviewed in hazard priority order, not arrival
  order. Energetic and radiological holds are
  resolved before ambiguous-identity holds.
- **Physical quarantine overflow** — if quarantine
  space is saturated, intake of new items suspected
  to require quarantine is suspended. Accept only
  items that can be cleared or routed immediately.
- **Intake shutdown criteria** — intake stops when:
  hold queue is full, quarantine is saturated, or
  operator capacity is exhausted. Shutdown is not
  failure. Resuming with backlog is failure.

1. Visual inspection — gross condition, obvious hazards,
   visible contamination, structural integrity
2. Safety screening — identify energetic materials,
   chemical contamination indicators, biological matter,
   and any condition requiring special handling before
   processing. See Section 2.
3. Physical document handling — if documentation arrives
   with the item, scan immediately and retain digitally.
   See Section 3.
4. Reference database lookup — automatic query by model
   number, serial number, or visual identification.
   See Section 4.
5. Parts list generation — for known assemblies, generate
   preliminary parts list from database or operator
   knowledge. See Section 5.
6. Fastener and small component recovery — identify
   recoverable fasteners and small components before
   the item enters gate logic. See Section 6.
7. Item tagging — assign unique identifier, record
   provenance data, log intake condition. See Section 7.
8. Handoff — item enters Classification and Triage
   (Operations/Gate_02_Triage.md)

If any step cannot be completed safely, the item is
held at Intake until the blocking condition is resolved.
Intake is not a throughput gate — it is a safety gate.
Speed is never a success metric here.

**Degraded operation doctrine:**
Intake assumes digital infrastructure — scanning,
database lookup, digital record retention, network
sync — but must survive without it. Power loss,
network outage, or equipment failure must not stop
Intake from performing its core safety function.

| Condition | Degraded Response |
|---|---|
| Power loss during Intake | Switch to paper fallback intake log. Physical tag items manually. Sync digital records when power restores. |
| Database unavailable | Operator-assisted lookup only. Flag items as database-unverified. Do not skip safety screening. |
| Scanner unavailable | Log document presence in paper record. Scan when equipment restores. Physical document retained. |
| Network unavailable | Continue local logging. Queue network contributions. Do not delay Intake for sync. |
| Digital record system unavailable | Paper log is primary. Minimum record: item description, hazard status, tag number, date, operator. |

*Minimum survivable Intake operation: visual safety
screening, physical tagging, paper log entry. These
three functions must be executable without any
digital infrastructure. Everything else degrades
gracefully — safety screening does not.*

Cross-reference: `Operations/Energy.md`,
`Architecture/Forge_Net.md` sync doctrine.

---

## 2. Safety Screening

Safety screening is the most critical function of Intake.
Hazards missed here propagate through every downstream
gate. The cost of a missed hazard is always higher than
the cost of a hold.

**Hazard categories to screen at Intake:**

| Category | Examples | Visual Indicators | Detection Limit |
|---|---|---|---|
| Energetic | Lithium batteries, capacitors, compressed gas vessels | Swelling, leakage, pressure relief markings | Visual inspection — moderate reliability |
| Chemical | Lead, cadmium, mercury, solvents, flux residues | Corrosion patterns, coating discoloration, warning labels | Visual inspection — low reliability. See GI-003 |
| Biological/organic | Oils, fluids, biological matter | Staining, odor, visible growth | Visual inspection — moderate reliability |
| Radiological | Radiation-emitting materials | Warning markings only — no visual indicator without markings | Visual inspection — very low reliability. See GI-003 |
| Unknown | Any item that cannot be screened with confidence | No obvious indicators | Route to hold immediately |
| Digital/firmware | Malware-bearing storage devices, compromised firmware, infected embedded systems, hostile control boards | No visual indicator — presence of storage media, network interfaces, or programmable controllers is the trigger | Isolate from all networked systems before any connection attempt — see GI-007 |

**Screening doctrine:**
- Screen before any disassembly begins — disassembly
  can release contained hazards
- When in doubt, hold — do not route ambiguous items
  forward under throughput pressure
- Energetic materials must be discharged or safely
  isolated before any further processing — see GI-002
- Chemical and radiological hazards beyond visual
  detection require augmented detection capability —
  see GI-003
- **Digital hazard screening** — any item containing
  storage media, network interfaces, or programmable
  controllers must be treated as potentially hostile
  before any connection to forge systems. Do not
  plug in, power up connected to forge network, or
  allow firmware execution without isolation protocol.
  Cross-reference: GI-007, `Operations/Electronics.md`,
  `Architecture/Forge_Net.md`
- New hazard categories not listed above route to
  Human/AI Oversight Gate and trigger a new category
  entry per `Architecture/Forge_flow.md` contamination
  doctrine

**Operator safety:**
Physical separation from unknown items during initial
screening. Do not handle items showing energetic
distress signs — swollen batteries, leaking vessels,
deformed pressure containers. Log and hold for
specialist assessment.
Cross-reference: `Architecture/Facilities.md` FA-001 — siting and clearance
requirements not yet confirmed.

---

## 3. Physical Document Handling

Physical documentation arriving with an item is rare
and signals something about the previous owner's care
level — worth noting in the intake record as a quality
signal.

**Handling doctrine:**
- Scan all physical documents on arrival regardless
  of apparent condition — partial information is
  better than no information
- Retain digitally — paper documents degrade,
  digital copies persist
- Contribute scan to `Architecture/Forge_Net.md`
  reference database when network connectivity
  allows — one forge's manual becomes every
  forge's resource
- Note document type and condition in intake record:
  complete manual, partial manual, warranty card,
  repair receipt, or other
- Do not discard physical documents after scanning —
  retain until item completes gate routing, then
  archive or discard per local policy

**Document quality signal:**
An item arriving with complete, well-maintained
documentation warrants a note in the intake record.
It suggests the previous owner valued the item —
which may correlate with better maintenance history
and higher functional recovery probability.

---

## 4. Reference Database Lookup

The reference database is the primary knowledge source
for item identification at Intake. It connects items
to known assembly structures, parts lists, repair
guides, and hazard profiles.

**Lookup sequence:**
1. Automatic query — model number or serial number
   if visible. Primary path.
2. Visual identification query — description or
   image-based lookup if no model number available.
   Secondary path.
3. Operator-assisted lookup — operator identifies
   item from experience or external search.
   Tertiary path.
4. Unknown — no identification possible. Item
   proceeds with incomplete intake record.
   See Section 8.

**Database dependency:**
The reference database lives in
`Architecture/Forge_Net.md` local cache, synced from
the network when connectivity allows. At v0 bootstrap,
the local cache may be sparse — common appliances
and tools prioritized first. See GI-001.

**Lookup outcome recording:**
- Positive identification: record model, manufacturer,
  known assembly structure, hazard profile if any
- Partial identification: record what is known,
  flag gaps explicitly
- No identification: flag as unknown, proceed to
  Section 8

*Lookup is not a gate — a failed lookup does not
stop Intake. It produces an incomplete record that
downstream gates must account for.*

---

## 5. Parts List Generation

For identified assemblies, a preliminary parts list
documents the recoverable components before disassembly
begins. This is Gate A intelligence arriving before
Gate A — knowing what's inside before opening the item.

**Parts list doctrine at v0:**
- Human judgment primary — operator generates list
  from database lookup or direct knowledge
- Parts list is preliminary — actual disassembly
  may reveal differences from expected structure
- Record expected vs. actual at disassembly —
  discrepancies feed back to the reference database
- Fasteners, small components, and hardware are
  explicitly included — not ignored as bulk material.
  See Section 6.

**Parts list scope constraint:**
The parts list is a helpful approximation, not
structural certainty. Explicit limits at v0:
- No guarantee of completeness — hidden assemblies,
  non-standard modifications, and undocumented
  variants are not captured
- No inferred hidden assemblies — only what is
  known from documentation or direct operator
  knowledge is listed
- No automation assumption — the list is generated
  by human judgment, not machine vision or
  predictive modeling
- No dependency on database completeness — if the
  database has no entry, the parts list is blank
  until the operator fills it from knowledge
- "Gate A intelligence arriving before Gate A"
  means helpful context, not predictive certainty.
  Gate A makes the actual routing decision.

**Parts list minimum content:**
- Item identifier (linked to intake tag)
- Assembly model and manufacturer if known
- Expected major components with condition notes
- Known hazardous sub-components flagged
- Estimated recovery class for each component:
  Class A (functional), Class B (degraded),
  Class C (material only)

*Parts list is an estimate, not a commitment.
Gate logic makes the actual routing decisions.*

---

## 6. Fastener and Small Component Recovery

Fasteners and small components are the most commonly
discarded items in real-world scrapping and among the
most practically useful. A screw in the Component
Library is available for use. A screw through the
shredder is particulate.

**Recovery doctrine at v0:**
- Identify recoverable fasteners and small hardware
  during Intake visual inspection and parts list
  generation
- Route to Component Library as Class A salvage
  by default — do not route to bulk Reduction
  without explicit reason
- Common fastener types worth recovering: machine
  screws, bolts, nuts, washers, standoffs, clips,
  and springs in good condition
- Condition threshold: functional geometry, no
  significant corrosion, thread intact. Damaged
  fasteners route to Class C material.
- Handling overhead vs. recovery value: at v0 scale,
  human judgment governs whether recovery overhead
  is justified. See ASM-007. A formal fastener
  registry is a v1+ consideration when volume
  justifies it.

*The junk drawer instinct is correct. Systematize
it when scale demands — not before.*

---

## 7. Item Tagging and Provenance

Every item that completes Intake receives a unique
identifier and a provenance record. This is the
starting point for the grain system in
`Admin/Ship_of_Theseus.md`.

**Minimum intake record at v0:**
- Unique item identifier (sequential or hash-based)
- Date and location of intake
- Item description — what it is, condition on arrival
- Identification status — known, partial, unknown
- Hazard screening outcome — clear, hold, or flagged
- Physical document status — none, scanned, attached
- Parts list reference — linked if generated
- Operator identifier — who performed Intake
- Intake notes — anything unusual worth recording

**Tagging method at v0:**
- Physical tag attached to item (durable label,
  cable tie tag, or equivalent)
- Digital record created in local system
- Record contributed to `Architecture/Forge_Net.md`
  when connectivity allows

**Grain system compatibility:**
Intake tagging format must be cross-validated against
`Admin/Ship_of_Theseus.md` grain system requirements
before either is treated as stable. See ASM-006,
GI-004.

**Chain of custody integrity:**
The tag is the physical link between the item and
its record. Tag loss or detachment breaks the
provenance chain at its first link. Provisional
doctrine pending GI-006 resolution:
- Tags must be physically durable and attached
  securely — not adhesive labels on oily or wet
  surfaces, not paper tags on items that will
  be moved repeatedly
- If a tag is lost before the item completes
  gate routing: stop, re-identify the item
  against intake records, re-tag before routing
- Duplicate identifier prevention — tag numbers
  are sequential and never reused, even after
  an item is fully processed
- Record/item reconciliation — at handoff to
  `Operations/Gate_02_Triage.md`, the physical tag is verified
  against the digital record before the item
  proceeds. Mismatches are held, not routed.
- Cross-reference: GI-006, `Admin/Ship_of_Theseus.md`

---

## 8. Unknown Item Protocol

An item that cannot be identified through database
lookup or operator knowledge is not routed forward
blind. Unknown items receive a hold and inspect
protocol before escalating to the Human/AI Oversight
Gate.

**Unknown item sequence:**
1. Complete safety screening regardless of
   identification status — unknown items are not
   exempt from hazard screening
2. Record as unknown in intake record — explicit
   flag, not an omission
3. Hold and inspect — operator performs closer
   physical examination. Does any marking, label,
   or physical feature enable partial identification?
4. Extended lookup — operator attempts identification
   through external resources if connectivity allows
5. If partial identification achieved: proceed with
   incomplete record, flag gaps explicitly
6. If no identification after hold and inspect:
   escalate to Human/AI Oversight Gate with full
   inspection notes
7. Do not route unknown items to gate logic without
   at least partial identification — gate decisions
   made without context risk misrouting hazardous
   or high-value items

**Intake-to-Triage contamination authority boundary:**
Intake and Gate_02_Triage share responsibility for
contaminated items but with distinct roles:
- **Intake owns** initial containment and hazard
  flagging — the item is held, labeled, and
  physically isolated here
- **Gate_02_Triage owns** routing classification —
  once Intake has established the hazard state,
  Triage determines the downstream path
- **Human/AI Oversight Gate owns** unresolved
  hazard arbitration — contaminated-but-valuable
  items requiring partial disassembly or deferred
  classification escalate here, not to Triage

**Oversight Gate escalation capacity:**
The unknown item protocol assumes Oversight is
available when needed. No doctrine exists for
Oversight saturation. Provisional guidance:
- Items awaiting Oversight review remain in hold —
  they do not route forward while waiting
- If Oversight queue exceeds defined threshold,
  new escalations are logged and queued; priority
  order is safety-critical first, then age of hold
  *(Placeholder — threshold defined operationally)*
- Items in safe indefinite hold do not expire —
  a correctly held item is always better than a
  prematurely routed one
- Cross-reference: `Architecture/Forge_flow.md`
  Human/AI Oversight Gate doctrine

**Unknown item as network contribution:**
An unidentified item that is eventually identified
through human expertise or extended research is a
high-value network contribution. Record the
identification path and contribute to the reference
database — the next forge to encounter the same
item benefits from this forge's work.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Intake conceived as simple safety screen and tag | Scope expanded significantly during drafting — document lookup, parts list generation, fastener recovery, unknown item protocol, and network contribution all surfaced as load-bearing functions | Intake is not a trivial entry gate. It is the system's first and only opportunity to catch hazards, establish provenance, and seed the network with knowledge. Underspecifying Intake underspecifies everything downstream | Analogous | No — expanded scope is correct |
| 2026-05-15 | Audit Review | Visual inspection assumed sufficient for hazard detection | Chemical and radiological hazards have no reliable visual indicators. Lead, radiation, and many solvents are invisible to unaided inspection | Visual inspection is necessary but not sufficient for complete hazard screening at v0. Augmented detection capability is required before unsupervised Intake operation. See GI-003 | Analogous | Yes — validate detection capability before first unsupervised run |
| 2026-05-15 | Audit Review | Fasteners treated as bulk material defaulting to Reduction | Fasteners are among the most practically useful recoverable items and are routinely lost to shredding in conventional scrapping | Fastener and small component recovery doctrine added — Class A salvage by default, not bulk Reduction. Formal registry deferred to v1+ when volume justifies overhead. The junk drawer instinct is correct | Analogous | Yes — validate recovery overhead vs. value at first operational scale |
| 2026-05-19 | Audit Review | Digital hazards not included in safety screening categories | Items with storage media, network interfaces, or programmable controllers can carry malware or hostile firmware invisible to physical inspection. Given Forge_Net.md integration, digital contamination propagates faster and further than physical contamination | Digital contamination added as explicit hazard category in Section 2. Isolation before any forge system connection required. GI-007 logged | Analogous | Yes — validate isolation protocol before first electronics intake |
| 2026-05-19 | Audit Review | Intake assumed to have continuous digital infrastructure availability | Power loss, network outage, and equipment failure are real operational conditions. Safety screening must survive without digital infrastructure | Degraded operation doctrine added to Section 1. Minimum survivable Intake: visual screening, physical tagging, paper log. Everything else degrades gracefully | Analogous | No — degraded doctrine is correct |
| 2026-05-19 | Audit Review | Operator cognitive fatigue not acknowledged as a hazard | Intake is the first safety barrier and is cognitively expensive. Fatigued operator is a hazard propagation vector, not just a performance issue | Cognitive fatigue doctrine added — shift guidance, second-review triggers, stop-intake authority. Backlog collapse doctrine added | Analogous | Yes — validate thresholds against first operational cycle |
| 2026-05-19 | Audit Review | Parts list generation framed as Gate A intelligence without explicit scope limits | "Intelligence arriving before Gate A" risks implying predictive modeling capability that does not exist at v0 | Parts list scope constraint added — no hidden assemblies, no automation, no database dependency, helpful approximation not structural certainty | Analogous | No — scope constraint is permanent |
| 2026-05-19 | Audit Review | Chain of custody between physical item and digital record not formally addressed | Tag loss breaks the provenance chain at its first link. The grain system depends on an unbroken chain from Intake forward | Provisional chain-of-custody doctrine added to Section 7. GI-006 logged. Record/item reconciliation at Gate_02 handoff added | Analogous | Yes — validate against grain system requirements when GI-004 and GI-006 resolve |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts currently active. Several
design tensions exist (automation vs. human judgment
at v0, fastener recovery overhead vs. value at small
scale, document scan yield vs. handling cost) but all
are deferred pending first operational data. Tracked
as unknowns in sidecar, not disputes. Revisit after
first operational Intake cycle produces yield data.*

---

## Auditor Notes & Unknowns

### GI-001 — Reference database content and coverage not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The reference database that
Gate_01_Intake queries for item identification has
no defined content scope, schema, or initial
population strategy.

**Why It Matters:** A sparse or poorly scoped database
makes the primary lookup path unreliable from first
operation. Operators fall back to tertiary paths —
external search or judgment — which are slower, less
consistent, and produce no network contribution.
Database coverage directly determines Intake
throughput and identification quality.

**Resolution Path:**
- Define minimum content scope for v0 — common
  household appliances, power tools, consumer
  electronics, and mechanical assemblies most
  likely to appear in salvage feedstock.
- Define schema — minimum fields: model identifier,
  manufacturer, assembly structure, known hazard
  profile, parts list reference.
- Define initial population strategy — manual entry,
  web scraping of public repair databases (iFixit
  and equivalents), or manufacturer documentation.
- Cross-reference `Architecture/Forge_Net.md` —
  database lives in local cache, synced from
  network. Content strategy must align with
  network contribution doctrine.
- Payment via Specification — once content scope,
  schema, and population strategy are defined,
  move to Section 4 as Placeholder promoting
  toward Analogous after first operational cycle.

---

### GI-002 — Energetic material discharge doctrine not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Batteries, capacitors, compressed gas
vessels, and other energetic materials identified at
Intake must be discharged or safely isolated before
any further processing. How this discharge happens
safely is not yet defined.

**Why It Matters:** Energetic materials in an
undischarged state are the most acute hazard in the
Forge processing stream. A lithium battery entering
Reduction is a fire and explosion risk. A compressed
gas vessel entering a shredder is a projectile risk.
Discharge doctrine is a safety prerequisite for
Intake operation, not a refinement.

**Resolution Path:**
- Define discharge doctrine by energetic category:
  - Lithium batteries — deep discharge procedure,
    safe storage protocol, disposal or recycling
    path for non-recoverable cells
  - Other batteries — category-appropriate discharge,
    electrolyte handling if applicable
  - Capacitors — safe discharge procedure, voltage
    verification before handling
  - Compressed gas — controlled release or isolation
    protocol, vessel marking after discharge
- Define safe isolation for energetics that cannot
  be immediately discharged — storage location,
  container type, maximum hold duration
- Define operator safety requirements — PPE,
  distance, tooling
- Must be resolved before first operational Intake
  run — hard prerequisite, not a deferral
- Cross-reference: `Architecture/Facilities.md` FA-001 siting requirements,
  `Operations/Air_Scrubber.md` for off-gassing
- Payment via Specification — once discharge
  doctrine is defined and tested, move to
  Section 2 as Analogous.

---

### GI-003 — Augmented hazard detection capability not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Visual inspection cannot reliably
detect chemical contamination (lead, cadmium, mercury,
solvents) or radiological hazards. Augmented detection
capability is required for complete hazard screening
but specific tools, methods, and protocols are not
yet defined.

**Why It Matters:** Lead is present in consumer
products without visible indicators. Radiation sources
have no visual signature without markings. An Intake
process relying solely on visual inspection has a
known blind spot for the most serious contamination
categories — alloy contamination, equipment fouling,
and operator health risk downstream.

**Candidate augmentation options for v0:**
- Lead test swabs — low cost, simple, reliable for
  surface lead detection. Available commercially.
  Suitable for v0 bootstrap. *(Analogous)*
- Geiger counter — detects radiation. Low cost for
  basic models, no consumables, simple operation.
  Should be standard Intake equipment. *(Analogous)*
- Chemical test strips — basic pH, solvent, and
  contaminant screening. Low cost, limited scope.
  *(Analogous)*
- XRF analyzer — broad spectrum elemental analysis,
  non-destructive. High cost, high capability.
  Purchase-what-cannot-be-produced doctrine applies
  if budget allows. *(Analogous)*

**Resolution Path:**
- Select minimum augmentation kit for v0 bootstrap
  — geiger counter and lead test swabs address
  the two most critical blind spots at lowest cost.
- Define testing protocol — when to test, how to
  interpret results, what threshold triggers a hold.
- Augmented detection is a prerequisite for
  unsupervised Intake operation — human oversight
  partially compensates until detection is in place.
- Payment via Specification — once augmentation kit
  is selected, protocols defined, and first
  operational cycle validates detection reliability,
  move to Section 2 as Analogous.
- Cross-reference: ASM-004,
  `Operations/Air_Scrubber.md` for chemical hazard
  handling.

---

### GI-004 — Intake tagging schema not cross-validated against grain system

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The intake tagging schema has not
been cross-validated against the grain system
requirements in `Admin/Ship_of_Theseus.md`. Incompatible
schemas break the provenance chain at its first link.

**Why It Matters:** Intake tagging is the starting
point for the grain system. A schema mismatch means
every provenance record created at Intake requires
manual conversion. The legal and philosophical value
of the grain system depends on an unbroken provenance
chain — a schema mismatch breaks that chain at the
first link.

**Resolution Path:**
- Review `Admin/Ship_of_Theseus.md` grain system
  requirements — what fields does a grain record
  require at minimum?
- Cross-validate against Section 7 minimum intake
  record — do the fields align?
- If misaligned: extend the intake record to include
  grain system required fields — do not reduce grain
  system requirements.
- Intake schema should be a superset of grain system
  requirements.
- Payment via Specification — once schemas are
  cross-validated and aligned, move to Section 7
  as Analogous.
- Cross-reference: ASM-006,
  `Admin/Ship_of_Theseus.md`.

---

### GI-005 — Pre-Intake protocol for items requiring special handling not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** No pre-Intake protocol exists for
items that are too damaged, contaminated, or dangerous
to enter standard Intake without prior intervention.

**Why It Matters:** Some items will arrive in
conditions that standard Intake cannot safely handle
— a leaking chemical container, a severely damaged
lithium battery showing thermal distress, an unlabeled
pressure vessel. Without a pre-Intake protocol,
operators face these situations without doctrine.
Improvised responses to hazardous conditions are a
primary source of workplace incidents.

**Resolution Path:**
- Define pre-Intake categories:
  - Active energetic distress (swollen, leaking,
    hot battery or capacitor)
  - Active chemical leak or visible fuming
  - Biological contamination beyond surface soiling
  - Structural instability creating collapse or
    falling hazard
  - Unidentifiable condition with no safe handling
    path
- Define pre-Intake response for each category —
  isolation, containment, specialist assessment,
  or controlled disposal.
- Define invocation authority — any operator should
  be able to call a hold without management approval.
- Cross-reference: GI-002 energetic discharge
  doctrine, `Architecture/Facilities.md` FA-001 siting requirements,
  `Operations/Air_Scrubber.md`.
- Payment via Specification — once pre-Intake
  categories and responses are defined and operator
  training covers them, move to Section 1 entry
  protocol as Analogous.

---

### GI-006 — Intake chain-of-custody integrity not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Governance                           |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Intake establishes provenance,
hazard status, and grain initiation for every item.
No formal chain-of-custody doctrine exists to ensure
the physical item and its digital record stay linked
through the entire gate flow.

**Why It Matters:** Without chain integrity, provenance
can be corrupted, hazard-cleared items can be swapped
for unchecked ones, and records can drift from the
physical objects they describe. The grain system in
`Admin/Ship_of_Theseus.md` depends on an unbroken provenance
chain — Intake is where that chain starts.

**Resolution Path:**
- Define tag physical durability requirements —
  material, attachment method, environmental
  resistance for storage and handling conditions.
- Define re-identification protocol for lost tags —
  how is an untagged item matched back to its
  intake record?
- Define duplicate identifier prevention — tag
  numbers are sequential and never reused.
- Define record/item reconciliation at Gate_02
  handoff — physical tag verified against digital
  record before routing.
- Cross-validate with `Admin/Ship_of_Theseus.md`
  grain system requirements — GI-006 and GI-004
  may resolve together.
- Payment via Specification — once chain-of-custody
  doctrine is defined and tested, move to Section 7
  as Analogous.

---

### GI-007 — Digital contamination and hostile firmware handling not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Security                             |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Items containing storage media,
network interfaces, or programmable controllers may
carry malware, hostile firmware, or compromised
embedded systems. No isolation or handling protocol
exists for digital contamination at Intake.

**Why It Matters:** Given `Architecture/Forge_Net.md` network
integration, a compromised device connected to forge
systems before isolation could propagate malware to
the reference database, corrupt cognitive save states,
or compromise network trust scoring. Digital
contamination is invisible, fast-propagating, and
potentially irreversible at the network level. Physical
contamination hazards are better understood — digital
hazards are not yet acknowledged in the system.

**Resolution Path:**
- Define digital hazard indicators at Intake —
  presence of storage media, network interfaces,
  wireless capability, or programmable controllers
  triggers isolation protocol before any connection.
- Define isolation protocol — air-gapped assessment
  before any forge system connection. No exceptions
  for "probably safe" items.
- Define assessment capability — what tools and
  expertise are required to clear a device for
  connection? This may require external expertise
  at v0 bootstrap.
- Cross-reference: `Operations/Electronics.md`,
  `Architecture/Forge_Net.md`, `Architecture/
  Cognitive_Frameworks.md` rogue unit doctrine.
- Payment via Specification — once isolation protocol
  is defined and tested, move to Section 2 as
  Analogous.

---

### Resolution Log

- 2026-05-19: GI-006, GI-007 — New entries logged
  following ChatGPT audit 2026-05-19. Chain-of-
  custody integrity and digital contamination both
  identified as structurally important gaps given
  Forge_Net.md integration. Provisional chain-of-
  custody doctrine added to Section 7. Digital
  contamination category added to Section 2 hazard
  table. Degraded operation doctrine added to
  Section 1. Cognitive fatigue and backlog collapse
  doctrine added to Section 1. Intake-to-Triage
  authority boundary added to Section 8. Parts list
  scope constraint added to Section 5.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from `Admin/Forge_Audit_Kit.md`
  to `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary and sidecar UNK-006 references
  updated to `Architecture/Facilities.md` FA-001
  (PC-002). Section 2 operator safety cross-reference
  updated to match.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Intake as a simple pass-through screen — visual check and tag only | Underspecifies the entry point for the entire system. Hazard detection, document handling, database lookup, parts list generation, fastener recovery, and unknown item protocol all surfaced as load-bearing functions that a simple screen misses entirely | No — expanded scope is correct and necessary |
| 2026-05-15 | Direct escalation of unknown items to Human/AI Oversight Gate without hold and inspect | Wastes Oversight Gate capacity on items that a closer inspection could resolve. Hold and inspect recovers partial identification in many cases and produces higher-quality intake records and network contributions | No — hold and inspect is correct doctrine |
| 2026-05-15 | Fasteners routed to bulk Reduction by default | Fasteners are among the most practically useful salvage items and are routinely lost to shredding in conventional scrapping. Default Reduction wastes recoverable value and contradicts preserve-before-destruction doctrine | No — Class A salvage default is correct |
| 2026-05-15 | Formal fastener registry at v0 | Registry overhead not justified at v0 scale. Human judgment governs recovery threshold until volume data exists. A formal registry is a v1+ consideration when throughput makes manual judgment impractical | Reconsider at v1 when operational volume data justifies registry overhead |
| 2026-05-15 | Visual inspection as sole hazard detection method | Visual inspection cannot detect lead, radiation, or most chemical contaminants. Relying on it alone creates a known blind spot for the most serious contamination categories. Augmented detection capability required — see GI-003 | No — augmented detection is permanent doctrine once established |
| 2026-05-15 | Continuous document scanning as an ongoing Intake task | Documents arrive rarely. Treating document scanning as a routine continuous task creates overhead without proportional value. Scan-on-arrival when documents are present is correct — not a standing workflow step | No — scan-on-arrival is correct scoping |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
`Admin/File_Template.md` apply. The following are
additional local triggers specific to Gate_01_Intake:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| GI-002 energetic discharge doctrine remains undefined at first operational Intake run | Energetic materials without discharge doctrine are an acute safety hazard — hard prerequisite, not a deferral |
| GI-003 augmented detection capability remains undefined at first unsupervised Intake run | Visual inspection alone cannot detect lead or radiation — unsupervised operation without augmented detection has a known safety blind spot |
| Visual inspection reinstated as sole hazard detection method after augmented detection is established | Abandoned path — reverting requires explicit human authorization and documented justification |
| Fastener recovery default changed from Class A salvage to bulk Reduction without operational data justifying the change | Preserve-before-destruction doctrine applies to fasteners — override requires evidence that recovery overhead exceeds value at operational scale |
| Unknown items routed to gate logic without hold and inspect protocol completed | Unknown items proceeding without inspection risk misrouting hazardous or high-value material — hold and inspect is mandatory before escalation |
| Intake tagging schema revised without GI-004 cross-validation against grain system | Schema changes that break grain system compatibility sever the provenance chain at its first link |
| Reference database lookup removed from Intake sequence | Database lookup is the primary identification path — removal degrades identification quality to operator-judgment only and reduces network contribution |
| Automation introduced at Intake without GI-002 and GI-003 resolution | Automated Intake without validated hazard detection removes the human compensating factor — both safety prerequisites must be resolved first |
| Pre-Intake protocol invocation authority restricted to management approval only | Any operator must be able to call a hold without approval — restricting this creates pressure to proceed with unsafe items |
| Document scan-on-arrival practice abandoned without evidence that document yield is consistently too low to justify | Scan-on-arrival preserves rare but high-value documentation and contributes to network knowledge base — abandonment requires operational yield data |

### Canonical Drift Triggers

*All mandatory re-audit conditions from `Admin/File_Template.md`
Section 11 apply without exception. Local triggers above are
additive, not substitutes.*
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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-07-17 (body); §XII proposed extension drafted 2026-08-02, not yet audited |
| Auditor          | ChatGPT — Synthesizer; Claude — Engineer; Claude — Embedded Value Preservation cross-reference added (human-directed), 2026-07-17; Copilot — drafted TIL/TAL/TCM/TMV + CIR-Triage extension (human-directed), 2026-08-02; Claude — verified against source and `Admin/Verification_Gates_LF.md`, corrective merge (human-directed), 2026-08-02 |
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
  (→ `Admin/Verification_Gates_LF.md` — this file does not define its own
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
| ASM-006 | Dual-use and weaponization patterns are recognizable by a trained operator at Station 0 | Current EC-002 status — Placeholder | Low       | EC-002 pattern-matching mechanism defined                   |

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
claim survives contact with the source files: `Admin/Verification_Gates_LF.md`
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

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                       | What Failed                                                              | What Was Learned                                                                                           | Confidence | Revalidation Needed |
|----------|---------------|------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | "Scrap" used as terminal bin label                   | Operators may interpret as disposal rather than material recovery        | Replaced with "Material Recovery"; vocabulary note added                                                   | Replicated | No                  |
| May 2026 | Audit Review  | Station 3 routed Fail directly to disassembly        | Missing Human/AI Oversight Gate — irreversible action without hold       | Triage Terminal added as mandatory hold before any material recovery proceeds                              | Replicated | No                  |
| May 2026 | Audit Review  | Queues treated as passive storage                    | Risk of latent hoarding, decision fatigue, dead inventory accumulation   | Queues are active allocations with decay, saturation behavior, and reassessment triggers                   | Replicated | No                  |
| May 2026 | Audit Review  | Single triage axis (operational utility only)        | Strategically irreplaceable components destroyed at same confidence threshold as common components | Strategic Recoverability added as second triage axis; four-tier classification system | Analogous  | Yes                 |
| 2026-08-02 | Cross-agent draft review | Copilot drafted TIL/TAL/TCM/TMV as an already-binding constitutional extension | Wrote candidate architecture as though it were ratified: invented a "Spec Gate: Constitutional" category not present in `Admin/Verification_Gates_LF.md`, and bound it into `Admin/CIR_Gov.md` despite that file's own Binding Status explicitly forbidding this | Cross-agent architectural drafts are useful but default to overclaiming operative status; every such draft needs to be checked against the actual gate/ratification state of every file it claims to extend, not just against plausibility | Analogous | Yes — recheck if §XII is ever promoted toward actual gate passage |

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
| Last Reviewed | 2026-05-23                     |

**Description:** Quantitative or contextual definition of acceptable degraded
performance for forge-duty components remains incompletely defined.

**Why It Matters:** Without a calibrated threshold, triage decisions at the
Gate A/C boundary rely entirely on operator judgment — reproducibility and
cross-operator consistency cannot be verified.

**Resolution Path:** Working definition added: "A component is sufficient if
it materially contributes to closure of the current operational loop." Populate
Baseline Performance Table after N≥50 observations per component class.
Cross-reference `Architecture/Forge_flow.md` FL-001 (gate logic determinism).

---

### TS-002 — Contamination routing protocol incomplete

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Gate_02_Triage.md   |
| First Logged  | May 2026                       |
| Last Reviewed | 2026-05-23                     |

**Description:** Full decontamination criteria, routing for components that
cannot be decontaminated, and provenance tag requirements for contamination
status remain undefined.

**Why It Matters:** Contamination bypass is the highest-risk triage failure
mode — a contaminated component reaching electrical or mechanical stations
creates secondary contamination and potential operator harm.

**Resolution Path:** Station 0 contamination check and Contaminated bin added.
Full decontamination protocol still needed. Cross-reference
`Operations/Air_Scrubber.md` AS-003 (scrubber waste stream and saturation).

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
| Last Reviewed | 2026-05-23                     |

**Description:** Deterministic routing for all item types at Gate A/C and
Gate C/D boundaries remains incomplete. Strategic tier override creates
additional boundary cases requiring worked examples.

**Why It Matters:** Non-deterministic boundary cases produce inconsistent
triage outcomes across operators and audit cycles — institutional memory
cannot accumulate reliable patterns.

**Resolution Path:** Gate Correspondence table added. Motor worked example
added. Additional worked examples needed for Strategic tier override paths.
Cross-reference `Architecture/Forge_flow.md` FL-001.

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
| Last Reviewed | 2026-08-02                     |

**Description:** §XII.1 proposes converting triage events into structured
knowledge (failure-mode distributions, repair-likelihood curves, etc.). No
log, database, or manual-review process for this currently exists.

**Why It Matters:** TS-001's threshold-revision bar (N≥50 consistent
observations) already exists independently of TIL; TIL would be the
mechanism for actually reaching it, so its absence keeps TS-001 open too.

**Resolution Path:** Stand up the v0 minimal form described in §XII.1 (a
structured log, manually reviewed) as a real, low-effort first step, before
any more elaborate TIL tooling is drafted.

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
| Last Reviewed | 2026-08-02                     |

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
| Last Reviewed | 2026-08-02                     |

**Description:** §XII.3's v0/v1/v2+ maturity ladder across testing, repair,
repurpose, decontamination, and embedded-value extraction has not been
checked against what tooling actually exists at the Forge's current stage.

**Why It Matters:** An overstated capability rung could make Gate B/C/D
routing look more justified than the Forge can actually deliver on.

**Resolution Path:** Populate the v0 rung of each domain against
`Operations/Electronics.md`, `Operations/Air_Scrubber.md`, and
`Architecture/Precision.md`'s actual current tooling before treating any
rung above v0 as real.

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
| Last Reviewed | 2026-08-02                     |

**Description:** §XII.4 proposes a five-dimension 0–3 maturity score. No
one is designated to assign these scores, at what cadence, or against what
evidence standard.

**Why It Matters:** An unscored or self-scored maturity vector attached to
a destruction-authorization rule (Gate D for Strategic/Critical tier) would
be worse than no vector at all — it would look quantitative without being
verifiable.

**Resolution Path:** Do not cite TMV scores in any actual Gate D decision
until a scoring owner and cadence are assigned and logged here.

---

### Resolution Log

- 2026-08-02: **§XII Proposed Triage Intelligence & Governance Extension added, corrective merge, human-directed.** Copilot drafted a four-layer extension (Triage Intelligence Layer, Triage Arbitration Layer, Triage Capability Model, Triage Maturity Vector) plus a "CIR-Triage" constitutional-integration block. Verified against source before integrating. Merged in: the TIL/TAL/TCM/TMV architecture itself, as a clearly-marked proposed/unaudited §XII, with governance hooks reframed as candidate rules that formalize existing doctrine (Principle 9, the Oversight Gate requirement, ASM-005's N≥50 bar) rather than new authority. Cut: (1) the "CIR-Triage" section binding these predicates into `Admin/CIR_Gov.md` as constitutional law — CIR_Gov.md is Proposed — Not Ratified, 0/6 gates, and its own Binding Status section states nothing should issue a CIR-VERIFIED transition until GOV-008 is ratified; (2) the invented "Spec Gate: Constitutional" category, which does not exist in `Admin/Verification_Gates_LF.md`'s six canonical gates; (3) all framing that implied Gate D routing, threshold revision, or Oversight Gate decisions are already governed by these predicates — none are, until §XII passes its own Gate 1. Registered TS-005 through TS-008 to track the four sub-layers' lack of implementation, rather than leaving them unregistered. Open Unknowns 3 → 7. Spec Gates unchanged at 2/6 — drafting §XII is not a gate pass.
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
- 2026-06-06: Navigation Anchors block added. Verification Ref corrected to Admin/Verification_Gates_LF.md. Electronics.md cross-reference corrected to Operations/Electronics.md. Duplicate separator removed. Interfaces table updated — Precision.md and Facilities.md added as upstream references. CT-002 cross-reference entry added to sidecar. Open Unknowns updated 3 → 4.
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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
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
  `Admin/Verification_Gates_LF.md` (PC-001). Scope Boundary
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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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
| Last Reviewed | 2026-05-15                                       |

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

---

### Resolution Log

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
  from `Forge_Audit_Kit.md` to `Admin/Verification_Gates_LF.md`
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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-07-31 (SC-009 registered; SC-004 expanded with Driving Mechanism Options) |
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
  (downstream — not yet assigned)
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
| Last Reviewed | 2026-05-15                     |

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
| Last Reviewed | 2026-05-15                     |

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
| Last Reviewed | 2026-05-15                     |

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
| Last Reviewed | 2026-07-31                     |

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
specifically — CLF-003 already notes it "applies most strongly to
any mechanical or high-pressure contact die and least strongly to
pure MHD or dieless paths." This does not touch CLF-003's
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
| Last Reviewed | 2026-05-15                     |

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
| Last Reviewed | 2026-05-15                     |

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
| Last Reviewed | 2026-07-28                     |

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
| Last Reviewed | 2026-07-28                     |

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
| Last Reviewed | 2026-07-31 |

**Description:** §9 Atmosphere Control above (passive reducing environment preferred; charcoal bed or inert purge if available; oxygen ingress minimized, not eliminated; precision gas chemistry out of scope for v0) is adequate for the aluminum-class melts this file currently scopes around, but not for titanium or other reactive/refractory metals. These metals react readily with both oxygen and nitrogen when hot or molten — nitrogen contamination in particular causes severe embrittlement, which is why a simple nitrogen purge (fine for many steels or aluminum) is actively harmful here. Real titanium welding or wire-arc additive manufacturing requires either full high-purity argon shielding (residual O₂ typically <50–300 ppm, entire cooling surface protected until <~400°C) or true vacuum (~10⁻²–10⁻³ Pa or better for aerospace-grade work). Titanium currently appears nowhere in this repository as a feedstock, salvage target, or fabrication material — its only existing mention is `Architecture/Chemistry.md`'s galvanic series table (most noble/cathodic metal, high-end marine hardware reference). Raised 2026-07-31 in response to a claim that titanium welding capability would make CLF-003 (nozzle/die wear) moot; verified against source that no such capability or material pathway currently exists.

**Why It Matters:** If titanium (or an equivalent reactive metal) is ever admitted as a salvage stream or fabrication material, this file's existing atmosphere doctrine cannot be silently inherited — doing so would produce embrittled, non-load-bearing product while appearing to have succeeded. It also would not resolve CLF-003 (`Challenges/Closed_Loop_Feedstock.md`): any titanium wire still has to be drawn through a die (harder problem, not easier), and any titanium part welded from near-net shape still needs cutting/trimming, where titanium's low thermal conductivity and rapid work-hardening make tool wear worse than for steel or aluminum, not moot.

**Resolution Path:** (1) G2 Physical Plausibility gate first — confirm whether reactive-metal processing is in scope for any near-term version; if not, this stays parked. (2) If pursued, define minimum atmosphere spec (residual O₂/N₂ limits, shielding vs. blanket, monitoring), explicitly exclude nitrogen as a purge gas, and identify the hardware delta from the current charcoal-bed baseline (full argon shielding vs. vacuum pumping train). (3) Register any external argon/vacuum-hardware dependency against `Challenges/Closed_Loop_Feedstock.md`'s closed-loop premise. (4) `Admin/Trajectories.md` TR-MET-002 records that Astroid-miner's `Propulsion_Economy_isru/zero_g_fabrication.md` independently specifies Induction Heating + EM Levitation (crucible-free, vacuum-native, high-purity) as a fabrication technique well-suited to this exact problem — but per UNK-003 (Cross-repo assumption contracts, Deferred pending Leviathan milestone) that is supporting detail for a v3+ off-world capability, not a resolution path for this terrestrial v0–v2 unknown.

**Cross-references:** §9 (this file, current atmosphere doctrine); SC-004 (wire extrusion nozzle — any titanium wire path inherits this unknown); `Challenges/Closed_Loop_Feedstock.md` CLF-003 (die/nozzle wear — titanium would add a harder second front, not remove the first); `Architecture/Chemistry.md` (galvanic series, sole existing titanium mention); `Admin/Trajectories.md` TR-MET-002 (Astroid-miner cross-repo note, parked).

---

### Resolution Log

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
  Verification Ref corrected from `Verification_Gates_LF.md`
  to `Admin/Verification_Gates_LF.md` (PC-001). Facilities.md
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
# Gate_06_Fabrication

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Arc welding produces UV radiation, infrared, and arc
> flash hazards that cause permanent eye damage in
> seconds without proper shielding. Arc eye gives no
> immediate pain warning — operators do not realize
> they have been injured until hours later. A welding
> helmet with appropriate shade lens, flame-resistant
> gloves, and protective clothing are non-negotiable
> prerequisites before the first arc is struck. Welding
> fumes from unknown alloy base metal — particularly
> galvanized or zinc-coated material — cause metal fume
> fever. Ventilation is not optional. PPE is a
> prerequisite, not a preference.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-19; revised 2026-06-08                                      |
| Auditor          | Claude — Skeptic/Auditor (actioning ChatGPT audit 2026-05-19)       |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Medium risk reflects operator safety exposure from arc
welding — UV radiation, infrared, and arc flash are
credible hazards requiring PPE and physical shielding.
Fabrication failures are recoverable — parts can be
remade, welds can be ground out, excess material
accommodates rework. Risk is operator-facing, not
process-irreversible. Distinct from Gate_03_Reduction
High risk which reflects process irreversibility.*

---

## Scope Boundary

**This file DOES define:**
- Fabrication doctrine and priority order
- Arc welding as the v0 proof-of-concept gatekeeper
  capability and the entry point for all subsequent
  fabrication method introduction
- Add-to-excess and mill-to-spec as the primary
  dimensional control philosophy
- Welding wire feedstock requirements and
  qualification criteria
- Precision ceiling doctrine — how the forge tracks
  its current precision capability and how precision
  improvement unlocks new fabrication capabilities
- Operator safety requirements for arc welding —
  PPE, shielding, ventilation
- Method introduction and qualification criteria —
  how new fabrication methods enter the system
- Fabrication priority order — what gets made first
  and why
- Feedback loop to gate classification rules —
  fabricated parts feed back into Component Library
  and repair capability
- Integration with upstream material outputs from
  Gate_04_Separation_Mechanical.md and
  Gate_05_Separation_Thermal.md
- Integration with Utilization as the downstream
  performance validation stage

**This file DOES NOT define:**
- Wire extrusion nozzle design and draw speed
  control (Operations/Gate_05_Separation_Thermal.md
  — SC-004)
- Welding wire chemical qualification beyond
  functional performance testing
  (not yet assigned — UNK-008)
- Laser welding specification
  (deferred — Admin/Trajectories.md)
- Powder welding specification
  (deferred — Admin/Trajectories.md)
- Machining and milling hardware specification
  (not yet assigned — GF-003)
- Casting, pressing, or forging methods
  (deferred — Admin/Trajectories.md)
- Energy accounting for fabrication operations
  (Operations/Energy.md)
- Facility siting and fabrication area safety
  beyond operator PPE doctrine
  (`Architecture/Facilities.md` — FA-001)
- Component Library specification and management
  (`Architecture/Components.md`)
- Utilization performance metrics
  (`Operations/Gate_07_Utilization.md`)
- Precision ceiling doctrine ownership
  (`Architecture/Precision.md`)

---

## File Purpose

Gate_06_Fabrication is the constructive stage of the
Lazarus Forge — the point where recovered and purified
material becomes functional parts, tools, and
infrastructure. Every upstream gate exists to deliver
material here in a condition suitable for fabrication.
Every downstream stage depends on what fabrication
produces.

Arc welding is the v0 proof-of-concept capability and
the gatekeeper for all subsequent fabrication method
introduction. It was chosen because it has the lowest
overhead path to joining metal parts, requires no
precision machining or expensive tooling to begin, and
produces structural capability from variable-quality
feedstock. Once arc welding works, the forge can
fabricate, repair, and begin closing the self-replication
loop. Subsequent methods — powder welding, laser
welding, casting, pressing — are introduced through
the method qualification framework this file defines,
not independently.

The primary dimensional control philosophy is
add-to-excess and mill-to-spec. Fabrication builds
or joins with intentional material surplus. Material
removal — grinding, milling, filing — achieves final
dimensions. This approach accommodates variable
feedstock quality and imprecise forming methods by
separating the joining step from the precision step.
The weld gets close. The mill finds the truth.

Precision is tracked as a first-class capability
metric. The forge's current precision ceiling
determines which components and capabilities are
within reach. Precision improvement — through better
tooling, better metrology, better process control —
opens fabrication paths that were previously
unavailable. Gate_06 owns this tracking because
fabrication is where the precision ceiling gets
tested against real part requirements.

If this file disappeared, the forge would have no
governing doctrine for its constructive stage. Arc
welding would have no qualification pathway. New
fabrication methods would have no introduction
criteria. The precision ceiling would have no owner.
The self-replication loop would have no fabrication
doctrine to close against.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Welding wire produced by Gate_05_Separation_Thermal.md extrusion path is of sufficient quality for structural arc welding — external wire sourcing may be required at bootstrap if internal production is not yet validated | SC-004 wire extrusion planned path; purchase-what-cannot-be-produced doctrine covers bootstrap gap | Low | SC-004 wire extrusion validated and first arc weld with internally produced wire demonstrates structural adequacy |
| ASM-002 | Add-to-excess is achievable — forming methods consistently produce sufficient material surplus for mill-to-spec removal to reach final dimensions | Dimensional control philosophy; analog fabrication practice | Medium | First operational fabrication cycle characterizes how much excess is achievable and whether removal tooling can reach final dimensions |
| ASM-003 | Material removal capability exists at v0 bootstrap — angle grinder, file, or equivalent available before precision milling equipment | Mill-to-spec step; purchase-what-cannot-be-produced doctrine | Medium | Precision milling equipment acquired — removal capability upgrades from manual to machine |
| ASM-004 | The forge's current precision ceiling is measurable — metrology capability exists to determine what tolerances are currently achievable | Precision ceiling doctrine; Architecture/Components.md Metrology item | Low | Metrology capability specified and validated — precision ceiling becomes a measured value rather than an estimate |
| ASM-005 | Arc welding on variable-quality Spin Chamber output alloys produces structurally adequate welds for v0 applications — alloy composition variation does not prevent functional joining | Arc welding with gradient output; weldability varies by alloy | Low | First arc welding trials characterize weldability of actual Spin Chamber output — acceptable alloy range defined |
| ASM-006 | Fabricated parts meeting v0 functional requirements are sufficient to begin closing the self-replication loop — precision parts are not required at v0 | Self-replication pathway; bootstrap doctrine | Medium | Self-replication loop requires precision parts that v0 fabrication cannot produce — precision ceiling becomes a blocking constraint |
| ASM-007 | Operator PPE for arc welding is available at bootstrap — welding helmet with appropriate shade, gloves, and protective clothing can be sourced before first weld | Operator safety doctrine; purchase-what-cannot-be-produced | Medium | PPE sourcing confirmed before first arc welding operation — non-negotiable prerequisite |

*ASM-001 and ASM-005 are the most technically load-bearing
— wire quality and base metal weldability together determine
whether the arc welding proof-of-concept closes at v0 with
internally produced wire or requires external wire sourcing
at bootstrap. ASM-004 is quietly critical — an unmeasurable
precision ceiling cannot be tracked or improved. Both connect
to Architecture/Components.md Metrology and Baseline
Observability items. Purchase-what-cannot-be-produced doctrine
covers bootstrap gaps in wire, PPE, and metrology equipment.
See README.md.*

---

## 1. Fabrication Doctrine

Fabrication is the constructive stage. Its purpose
is to convert recovered and purified material into
functional parts, tools, and infrastructure that
serve the forge and the ecology it belongs to.

**Priority order:**
1. Tools or components the forge currently lacks
   and cannot obtain through other means
2. Infrastructure that expands forge capability —
   repairs, upgrades, and improvements to existing
   modules
3. Components for inter-forge trade and ecology
   support
4. Output for external use or exchange

This priority order follows Architecture/Forge_flow.md
want/need policy — fabrication serves demonstrated
needs, not hypothetical future uses.

**Fabrication is not terminal:**
A fabricated part that sits unused is not a success.
Utilization and real-world performance are the
validation stage. Fabrication produces candidates
for use — Utilization determines whether they are
fit for purpose.

**The forge fabricates to its current capability:**
Do not attempt fabrication that requires precision
beyond the current ceiling. A part that cannot be
made to spec at current capability waits until
capability improves — it does not get made badly
and used anyway. See Section 5.

**Dynamic and adaptive:**
The fabrication method set is not fixed. Arc welding
opens the door. Operational experience, capability
growth, and network knowledge determine what comes
next. New methods enter through the qualification
framework in Section 6 — not through informal
adoption.

---

## 2. Operator Safety

Arc welding produces hazards that are not visible
until damage is done. UV radiation causes permanent
eye damage — arc eye — from exposures measured in
seconds. Infrared causes skin burns. Fumes from
base metal and coatings are respiratory hazards.
Spatter creates fire and burn risk.

**Minimum PPE for arc welding at v0:**
- Welding helmet with appropriate shade lens —
  shade 10 minimum for MMA/stick welding.
  Auto-darkening preferred. Not optional.
- Leather or flame-resistant welding gloves
- Flame-resistant clothing — no synthetic fabrics
  that melt rather than char
- Closed-toe leather footwear
- Respiratory protection if working with coated,
  painted, or unknown alloy base metal

**Physical shielding:**
- Welding screen or curtain required — protect
  bystanders and equipment from arc flash
- No bystanders within arc flash range without
  appropriate eye protection
- Fire-resistant work surface or welding table

**Fume ventilation:**
- Cross-reference Operations/Air_Scrubber.md —
  welding fumes must be captured or exhausted
- Unknown alloy base metal warrants enhanced
  ventilation — galvanized metal produces zinc
  fumes that cause metal fume fever
- Never weld galvanized, zinc-coated, or
  lead-painted metal without respiratory
  protection and forced ventilation

**Unknown salvage alloy contamination defaults:**
Arc welding unknown salvage metal is materially
different from welding known commercial stock.
The current fume doctrine names galvanized zinc
but does not generalize. Salvage environments
introduce additional hazards:

- **Chromium-bearing alloys** — welding stainless
  or chrome-plated material produces hexavalent
  chromium fumes. Carcinogenic. Forced ventilation
  and P100 respirator minimum.
- **Cadmium coatings** — present on some hardware
  and older plated fasteners. Acute cadmium
  poisoning is rapid and severe. No welding of
  cadmium-plated material without full respiratory
  protection and outdoor/forced ventilation.
- **Lead contamination** — old paint, solder,
  bearing materials. Lead fumes are cumulative
  toxins. Treat any old painted or soldered
  material as lead-suspect.
- **Oil-impregnated scrap** — combustion products
  from welding oily material create respiratory
  hazards and fire risk. Clean or degrease before
  welding.
- **Unknown thermal decomposition products** —
  plastics, coatings, adhesives, and composite
  materials produce unpredictable fumes under
  welding heat.

**Default doctrine for unknown salvage metal:**
Treat all salvage metal as potentially contaminated
until characterized. Initial fabrication trials
with uncharacterized material must use:
- Outdoor or forced-exhaust ventilation
- Full respiratory protection — not just dust mask
- Pre-cleaning and coating removal before welding
- No welding of sealed vessels, batteries, coated
  pressure systems, or chemically contaminated scrap

Cross-reference: Operations/Gate_02_Triage.md
contamination routing, GI-003 detection capability.

**PPE is a prerequisite, not a preference:**
First arc welding operation does not begin until
PPE is confirmed available and fitted. See ASM-007.
Cross-reference: `Architecture/Facilities.md` FA-001
siting requirements.

---

## 3. Arc Welding as Gatekeeper

Arc welding is the v0 proof-of-concept fabrication
capability. It gates access to all subsequent
fabrication method introduction.

**Fabrication phases — resolving welding process ambiguity:**

The file previously oscillated between MMA/stick
and MIG/GMAW welding without committing. This
changes power requirements, gas requirements,
SC-004 criticality, and wire feedstock dependency.
Three phases clarify the progression:

| Phase | Process | Wire Source | SC-004 Dependency | Gate |
|---|---|---|---|---|
| A — Bootstrap | MMA/stick welding | External consumable electrodes — no wire feed required | Decoupled | Arc welding qualified with external consumables |
| B — Internal wire trial | MIG/GMAW experimental | Externally sourced MIG wire | Optional | First internal wire samples tested against MIG requirements |
| C — Closed loop | MIG/GMAW integrated | Internally produced via SC-004 | Foundational | Internal wire qualified; self-replication loop closes |

**v0 baseline is Phase A.** MMA/stick welding with
externally sourced electrodes. No wire feed required.
No gas required for basic SMAW process. Lowest
overhead, most bootstrap-compatible.

Phase B begins when SC-004 produces first wire
samples or when MIG equipment becomes available —
whichever comes first. Phase B does not wait for
Phase A to be complete for all applications, but
Phase A qualification must precede Phase B trials.

Phase C closes the self-replication loop. It is
a milestone, not a v0 assumption.

**Why MMA/stick first:**
- Lowest overhead path to joining metal parts
- No precision machining or expensive tooling
  required to begin
- No shielding gas required for basic SMAW
- Produces structural capability from variable-
  quality feedstock
- Equipment is purchasable at bootstrap —
  basic MMA welder is commercially available
  at low cost
- Skill is learnable — operator develops
  competency on scrap before functional parts

**Arc welding qualification criteria (v0):**
Arc welding is considered qualified when:
1. Operator can consistently produce welds that
   pass visual inspection — no visible porosity,
   cracks, or incomplete fusion on test pieces
2. Destructive test of sample weld demonstrates
   adequate strength for v0 structural applications
   — weld fails in base metal, not at weld joint
3. Wire feedstock is confirmed — internally
   produced from SC-004 or externally sourced
   per purchase-what-cannot-be-produced doctrine
4. PPE confirmed available and operator trained
   in its use
5. Ventilation confirmed adequate per
   Operations/Air_Scrubber.md

**What arc welding qualification unlocks:**
- Structural fabrication from Spin Chamber output
- Equipment repair capability within the forge
- Self-replication pathway becomes operational
- Method introduction framework opens for
  subsequent methods — see Section 6

*Arc welding qualification is the single most
important milestone in v0 fabrication. Everything
else in this file depends on it.*

---

## 4. Add-to-Excess and Mill-to-Spec

The primary dimensional control philosophy of
Gate_06_Fabrication. Fabrication builds or joins
with intentional material surplus. Material removal
achieves final dimensions. The forming step gets
close. The removal step finds the truth.

**Why this approach:**
- Variable feedstock quality means forming precision
  is inherently limited — alloy composition, surface
  condition, and thermal behavior all vary
- Arc welding distortion is real and predictable —
  parts move during welding. Building to excess
  accommodates distortion and allows correction.
- Material removal is more precise than material
  addition at v0 capability levels
- A part with too much material can be corrected.
  A part with too little cannot.

**Add-to-excess doctrine:**
- Design fabrication to produce intentional surplus
  — typically 1–3mm on surfaces requiring dimensional
  accuracy *(Placeholder — excess allowance defined
  by material and process during first operational
  cycle)*
- Weld buildup on worn or damaged surfaces adds
  material before removal to spec
- Cast or formed parts include machining allowance
  in the design

**Mill-to-spec doctrine:**
- Final dimensions achieved through material removal
  — angle grinder, file, lathe, mill in order of
  increasing precision
- Match removal method to required tolerance:
  - Angle grinder — rough shaping, >1mm tolerance
  - File — intermediate, 0.5–1mm tolerance
  - Lathe/mill — precision, <0.5mm tolerance
    *(Placeholder — tolerance ranges defined by
    first operational capability assessment.
    See GF-002)*
- Stop when spec is reached — do not remove beyond
  spec chasing a better surface finish
- If removal overshoots spec: add material and
  restart removal, or assess whether the part
  still meets functional requirements with
  reduced dimensions

**Standardization note:**
Tooling for material removal should be selected
from standardized stock — grinding discs, cutting
wheels, lathe tooling — that can be sourced,
shared, or traded between forge instances.
Bespoke tooling creates single-forge dependencies.

---

## 5. Precision Ceiling

The precision ceiling is the tightest tolerance the
forge can currently achieve and verify. It is a
first-class capability metric — tracked, reported,
and actively improved.

**Why precision ceiling matters:**
- Components and capabilities are gated by precision.
  A bearing seat that requires 0.01mm tolerance
  cannot be fabricated by a forge whose ceiling
  is 0.5mm — the part waits until capability
  improves.
- Attempting fabrication beyond the current ceiling
  produces parts that appear correct but fail in
  service. Silent failure is worse than acknowledged
  limitation.
- Precision improvement is a force multiplier —
  raising the ceiling opens fabrication paths that
  were previously unreachable.

**Precision ceiling components:**
- **Metrology** — what can be measured. A tolerance
  that cannot be measured cannot be held. The
  precision ceiling cannot exceed metrology
  capability. Cross-reference: Architecture/
  Components.md Metrology item.
- **Process control** — what can be repeatably
  produced. Metrology reveals what was made.
  Process control determines what can be made
  again.
- **Tooling** — what the available equipment can
  achieve. A file has a different ceiling than
  a CNC mill.

**Measurement capability does not imply fabrication capability:**
This distinction is load-bearing. A forge with
±0.02mm caliper resolution cannot conclude it
can fabricate to ±0.02mm. The precision ceiling
is bounded by the worst-performing stage across
the entire fabrication process:

- Measurement resolution
- Fixturing stability — how securely is the
  workpiece held during removal?
- Thermal expansion — material grows and shrinks
  during and after welding
- Operator repeatability — can the same operator
  achieve the same result on the third attempt
  as the first?
- Part geometry — complex shapes are harder to
  measure and hold than flat surfaces

The precision ceiling is the achievable and
verifiable tolerance under realistic operating
conditions — not the theoretical limit of the
best tool in the forge.

**Precision ceiling doctrine:**
- Do not fabricate parts requiring tolerance beyond
  the current ceiling — acknowledge the limitation
  and either source the part externally or wait
  for capability improvement
- Purchase precision instruments at bootstrap —
  a commercial caliper outperforms anything a v0
  forge can self-fabricate to measure itself with.
  Per README.md: precision is seeded deliberately,
  not bootstrapped from nothing.
- Track the ceiling explicitly — what is the
  tightest tolerance currently achievable and
  verified? Update when capability changes.
- Report ceiling honestly in fabrication records —
  a part made to 0.5mm tolerance should say so,
  not claim tighter tolerance it was not verified
  to hold

**Precision ceiling at v0 bootstrap (Placeholder):**
- Metrology: commercial caliper — ±0.02mm
  measurement capability *(Analogous)*
- Process: manual grinding and filing —
  ±0.5mm achievable with care *(Analogous)*
- Tooling ceiling: lathe if available —
  ±0.1mm with skilled operator *(Analogous)*

*These are starting estimates. First operational
cycle establishes actual v0 ceiling. See GF-002.*

---

## 6. Method Introduction and Qualification

New fabrication methods enter the system through
a qualification framework. Informal adoption —
using a method before it is qualified — is not
permitted. An unqualified method has unknown
capability, unknown failure modes, and unknown
safety requirements.

**Qualification prerequisites for any new method:**
1. Safety requirements identified and PPE confirmed
   available before first operation
2. Operator training completed — not self-taught
   on functional parts. Practice on scrap first.
3. Capability characterization — what tolerances
   can the method achieve? What materials does it
   suit? What are its failure modes?
4. Integration with existing workflow confirmed —
   how does the method interact with upstream
   material preparation and downstream finishing?
5. Energy requirements characterized and cross-
   referenced to Operations/Energy.md budget

**Consumables lifecycle doctrine:**
Fabrication capability can be lost operationally
before it is lost theoretically. A forge with a
welder and no electrodes has no fabrication
capability. Consumables are load-bearing infrastructure.

- **Electrode and consumable tracking** — maintain
  a running inventory of welding electrodes,
  grinding discs, cutting wheels, contact tips,
  and measuring tool calibration status
- **Duty cycle cooling** — welders have thermal
  duty cycles. Continuous operation beyond rated
  duty cycle degrades equipment and weld quality.
  Respect cooling periods.
- **Tool inspection intervals** — grinding discs
  crack and fragment under stress. Inspect before
  each use. Retire at first sign of damage.
- **Calibration verification cadence** — measuring
  tools drift. Calipers should be zero-checked
  before each precision session. Damaged measuring
  tools produce false confidence in tolerances.
- **Salvage prioritization for consumables** —
  grinding discs, contact tips, and electrodes
  from salvage are acceptable if undamaged.
  Measuring tools from salvage require calibration
  verification before trust. Welding helmets from
  salvage require lens integrity verification.
- **Minimum operational stock** — define a minimum
  consumable stock level below which fabrication
  operations are suspended pending resupply.
  *(Placeholder — stock levels defined during
  first operational cycle)*

**Method introduction sequence:**
1. Identify need — what fabrication capability
   gap does this method address?
2. Assess prerequisites — is upstream material
   preparation compatible? Is PPE available?
3. Practice qualification — operator demonstrates
   competency on scrap material
4. Capability characterization — produce test
   pieces, measure outcomes, document ceiling
5. First functional use — supervised, on a
   non-critical part
6. Log outcomes — feed back to Lessons Learned
   and Architecture/Forge_Net.md

**Deferred methods (Exploration-level notes):**
- Powder welding — requires powder feedstock
  production capability and laser or plasma
  energy source. Higher precision than arc
  welding. Route to Admin/Trajectories.md v1+.
- Laser welding — requires precision laser
  source and controlled atmosphere. Very high
  precision, low heat input. Route to
  Admin/Trajectories.md v2+.
- Casting — requires mold fabrication capability
  and controlled pour. Lower precision than
  machining but good for complex geometry.
  Route to Admin/Trajectories.md v1+.
- Pressing and forging — requires tooling and
  force application infrastructure. Good for
  high-strength parts. Route to
  Admin/Trajectories.md v2+.

*Each deferred method becomes available when
arc welding qualification is complete and the
relevant upstream capability exists. The system
is dynamic and adaptive — the method set grows
with the forge.*

---

## 7. Welding Wire Feedstock

Welding wire is the consumable that enables arc
welding. At v0, wire sourcing follows a defined
priority path.

**Wire sourcing priority:**
1. Internally produced — Gate_05_Separation_Thermal
   wire extrusion path (SC-004) when validated
2. Externally sourced — commercial welding wire
   purchased per purchase-what-cannot-be-produced
   doctrine until internal production is validated
3. Inter-forge trade — wire produced by another
   forge instance in the ecology

**Wire qualification for arc welding:**
Wire is considered qualified for v0 structural
arc welding when:
- Consistent diameter within acceptable range
  for selected welding process *(Placeholder —
  diameter spec defined by welding process
  selection. See GF-001)*
- No visible surface contamination, oxidation,
  or moisture
- Test weld produces acceptable fusion and
  bead profile on representative base metal
- Destructive test confirms weld strength
  adequate for v0 structural applications

**Wire quality and alloy composition:**
Internally produced wire from Spin Chamber
output will have variable alloy composition.
Variable alloy wire is acceptable for structural
applications where precise mechanical properties
are not required. It is not acceptable for:
- Pressure-bearing applications
- Safety-critical structural members
- Applications requiring known conductivity

For these applications, externally sourced wire
with known composition is required until internal
wire qualification improves.
Cross-reference: UNK-008, SC-004, ASM-001, ASM-005.

---

## 8. Fabrication Feedback Loop

Fabrication is not a terminal process. Every
fabrication event produces data that improves
the system.

**Feedback targets:**
- Gate classification rules — fabricated parts
  reveal what recovered components are actually
  useful for. Classification heuristics improve
  with fabrication experience.
- Precision ceiling tracking — fabrication outcomes
  update the documented ceiling. A part successfully
  made to tighter tolerance raises the ceiling.
  A part that failed to hold tolerance confirms
  the current limit.
- Wire quality characterization — weld quality
  correlates with wire alloy composition. Outcomes
  feed back to Spin Chamber operating parameters
  and SC-002 segregation effectiveness evaluation.
- Method qualification — every use of a method
  produces data on its capability, failure modes,
  and appropriate applications.
- Network contribution — fabrication logs,
  method outcomes, and wire quality data
  contributed to Architecture/Forge_Net.md
  reference database. One forge's fabrication
  experience becomes every forge's knowledge.

**Fabrication record minimum content:**
- Part identifier and description
- Material source — which gate output, which
  forge instance
- Method used
- Wire feedstock source and qualification status
- Dimensional outcome — target vs. achieved
- Precision ceiling applied
- Weld quality assessment if applicable
- Operator identifier
- Outcome — passed, failed, reworked

**Fabrication output tag:**
Every fabricated part that enters service receives
a physical output tag seeding its grain record in
Admin/Ship_of_Theseus.md. The tag connects the
part's service history back to its material origin.

Minimum output tag content:
- **Forge instance identifier** — which forge
  produced this part
- **Fabrication sequence number** — unique,
  sequential, never reused
- **Fabrication phase** — A (MMA bootstrap),
  B (MIG trial), or C (closed-loop internal wire)
- **Date and operator identifier**
- **Material source reference** — which gate
  output batch, which Spin Chamber run if thermal
- **Wire feedstock batch identifier** — if MIG;
  internal or external sourcing noted
- **Method used**
- **Precision ceiling applied at fabrication**
- **Initial quality assessment** — pass, conditional,
  rework

When a part fails in service, this tag traces
back to the forge, operator, feedstock batch,
alloy source, and Spin Chamber run that produced
it. Cross-forge quality patterns become visible
in the network — if one forge's wire consistently
produces inferior welds, the ecology learns it.

Cross-reference: Admin/Ship_of_Theseus.md grain
system, GI-006 chain-of-custody doctrine,
Architecture/Forge_Net.md quality contribution.

*A fabrication record that documents a failure
is more valuable than one that documents a
success without detail. Failures teach. Successes
without records teach nothing.*

---

## 9. Integration Hooks

- `Architecture/Forge_flow.md` — governing flow;
  Fabrication is the constructive outcome path
- `Operations/Gate_04_Separation_Mechanical.md`
  — upstream material source; mechanical
  separation output feeds fabrication stock
- `Operations/Gate_05_Separation_Thermal.md`
  — upstream material source and wire extrusion
  path; SC-004 wire feeds arc welding directly
- `Operations/Air_Scrubber.md` — welding fume
  capture and ventilation; required operational
  during arc welding
- `Operations/Energy.md` — fabrication energy
  not yet characterized; welding power draw
  feeds energy accounting
- `Architecture/Components.md` — Metrology
  and Baseline Observability items; precision
  ceiling references component taxonomy
- `Architecture/Forge_Net.md` — fabrication
  logs and method outcomes contributed to
  network reference database
- `Admin/Trajectories.md` — deferred methods
  (powder welding, laser welding, casting,
  pressing) routed here for version targeting
- `Admin/Ship_of_Theseus.md` — fabricated
  parts that enter service begin their own
  grain provenance record
- `Unknowns.md` — GF-001 through GF-005
  indexed once logged

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Fabrication conceived as terminal endpoint — material goes in, parts come out, process ends | Fabrication without a feedback loop produces parts but no learning. Classification rules, precision ceiling, wire quality, and method capability all improve through fabrication data | Fabrication is a data-generating stage, not just a production stage. Every outcome — success or failure — feeds back to upstream gates, network knowledge, and precision ceiling tracking. A fabrication record that documents a failure is more valuable than one that documents a success without detail | Analogous | No — feedback loop doctrine is correct |
| 2026-05-15 | Audit Review | Wire production assumed to close self-replication loop automatically once SC-004 is validated | Wire quality from variable-alloy Spin Chamber output may not be sufficient for all arc welding applications. External wire sourcing at bootstrap is a valid and expected path | Purchase-what-cannot-be-produced doctrine applies to welding wire at bootstrap. Internal wire production is the goal, not the prerequisite. Arc welding with externally sourced wire still validates the fabrication capability even if wire is not yet internally produced | Analogous | Yes — validate internal wire quality against arc welding requirements once SC-004 is operational |
| 2026-05-15 | Audit Review | Precision ceiling treated as fixed background condition — assumed known without active tracking | An untracked precision ceiling produces parts that appear correct but fail in service when actual ceiling is lower than assumed. Silent failure from overconfident tolerance claims is worse than acknowledged limitation | Precision ceiling is a first-class tracked metric, not a background assumption. It cannot exceed metrology capability. It must be documented honestly in fabrication records. Purchasing precision instruments at bootstrap is correct doctrine — precision is seeded deliberately, not bootstrapped from nothing | Analogous | Yes — establish actual v0 precision ceiling during first operational fabrication cycle |
| 2026-05-15 | Audit Review | Add-to-excess framed as workaround for imprecise forming | Add-to-excess is not a workaround — it is the correct philosophy for a system working with variable feedstock and inherently imprecise forming methods | The weld gets close. The mill finds the truth. This is not a limitation to overcome — it is the correct approach for v0 capability levels. The philosophy should be stated as doctrine, not as a compromise | Analogous | No — add-to-excess and mill-to-spec is permanent v0 doctrine |
| 2026-05-19 | Audit Review | File oscillated between MMA/stick and MIG/GMAW without committing to a baseline process | Ambiguity changed power requirements, gas requirements, SC-004 criticality, and wire dependency simultaneously — different readers could derive different bootstrap architectures | Welding process phase split added to Section 3 — Phase A (MMA bootstrap, no wire), Phase B (MIG trial with external wire), Phase C (closed-loop internal wire). v0 baseline is Phase A | Analogous | No — phase split is correct architecture |
| 2026-05-19 | Audit Review | Fume doctrine named galvanized zinc but did not generalize to salvage contamination | Chromium, cadmium, lead, oil-impregnated scrap, and unknown coatings all produce different hazards. Unknown salvage metal defaults were absent | Unknown salvage alloy contamination defaults added to Section 2. All salvage metal treated as potentially contaminated until characterized. Initial trials require outdoor/forced ventilation and full respiratory protection | Analogous | Yes — validate against first fabrication operational cycle |
| 2026-05-19 | Audit Review | Precision ceiling framed through metrology capability without explicitly separating measurement from fabrication capability | "I can measure ±0.02mm therefore I can fabricate ±0.02mm" is a real failure mode. Fixturing, thermal expansion, repeatability, and part geometry all affect achievable precision independently | Explicit disclaimer added to Section 5 — measurement capability does not imply fabrication capability. Ceiling bounded by worst-performing stage across the entire process | Analogous | No — distinction is permanent doctrine |
| 2026-05-19 | Audit Review | Consumables lifecycle not addressed — fabrication capability treated as stable once equipment is acquired | A forge with a welder and no electrodes has no fabrication capability. Consumable depletion, tool wear, and calibration drift are operational failure modes that don't require equipment failure | Consumables lifecycle doctrine added to Section 6 — inventory tracking, duty cycle, tool inspection, calibration verification, salvage prioritization, minimum stock doctrine | Analogous | Yes — define minimum stock levels during first operational cycle |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | Whether internally produced wire from Spin Chamber output is sufficient for v0 arc welding without external sourcing at bootstrap | Position A: Internal wire production from SC-004 is the goal and should be validated before arc welding qualification begins — using external wire delays the self-replication proof of concept. Position B: External wire sourcing at bootstrap is correct doctrine per purchase-what-cannot-be-produced — arc welding qualification should not wait on SC-004 validation, which is itself unvalidated | Low | Open | Operations/Gate_06_Fabrication.md |

*DS-001 is a sequencing dispute, not a technical one.
Both positions agree that internal wire production is
the goal. The disagreement is whether arc welding
qualification should wait for internal wire or proceed
with external wire. Position B is the current standing
doctrine — purchase-what-cannot-be-produced applies,
and delaying arc welding qualification to wait for
SC-004 validation unnecessarily gates two unresolved
unknowns on each other. Revisit when SC-004 produces
first wire samples and quality can be assessed against
arc welding requirements.*

---

## Auditor Notes & Unknowns

### GF-001 — Welding wire diameter specification
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Wire diameter specification for v0
arc welding has not been defined. Wire diameter
determines amperage range, deposition rate, and
suitable base metal thickness. SC-004 draw speed
controls diameter — without a target diameter,
draw speed cannot be set.

**Why It Matters:** Wire diameter is the primary
parameter connecting SC-004 wire extrusion to arc
welding process selection. An undefined diameter
means the extrusion path cannot be configured and
welding process parameters cannot be established.

**Resolution Path:**
- Select v0 arc welding process — MMA stick welding
  requires no wire; MIG/GMAW requires wire feed.
  If MIG is selected, wire diameter must be
  specified before SC-004 draw speed can be set.
- Common v0 MIG wire diameters for steel:
  0.6mm, 0.8mm, 0.9mm, 1.0mm *(Analogous)*
- Common v0 MIG wire diameters for aluminum:
  0.8mm, 1.0mm, 1.2mm *(Analogous)*
- Select diameter based on available welding
  equipment wire feed capability and target
  base metal thickness range.
- Cross-reference: SC-004 in
  Operations/Gate_05_Separation_Thermal.md,
  UNK-008.
- Payment via Specification — once welding
  process and wire diameter are selected, move
  to Section 7 as Analogous.

---

### GF-002 — Precision ceiling not characterized
at v0 bootstrap

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The actual precision ceiling —
tightest tolerance achievable and verifiable at
v0 bootstrap — has not been characterized. Section
5 provides Analogous estimates but these are not
measured values.

**Why It Matters:** An uncharacterized precision
ceiling produces overconfident fabrication claims.
Parts made to an assumed tolerance that hasn't
been verified may fail in service silently.

**Resolution Path:**
- Establish metrology baseline — confirm available
  measurement tools and their resolution.
  Commercial caliper is the minimum v0 instrument.
- Produce test pieces using each available removal
  method — angle grinder, file, lathe if available.
- Measure achieved dimensions against targets
  across multiple attempts.
- Document actual achievable tolerance range per
  method — this becomes the characterized ceiling.
- Update Section 5 from Analogous estimates to
  Measured values.
- Cross-reference: Architecture/Components.md
  Metrology item, ASM-004.
- Payment via Specification — once ceiling is
  characterized through test pieces, move to
  Section 5 as Measured.

---

### GF-003 — Material removal hardware not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Specific material removal equipment
for the mill-to-spec step has not been specified
for v0 bootstrap.

**Why It Matters:** Material removal capability
determines the precision ceiling. The add-to-excess
and mill-to-spec philosophy depends on removal
capability being available before fabrication begins.

**Resolution Path:**
- Minimum v0 removal capability: angle grinder
  and hand files. Purchasable at bootstrap.
  *(Analogous)*
- Preferred v0 removal capability: bench grinder
  plus angle grinder plus file set.
- Precision v0 removal capability: manual lathe
  if available. Purchase per purchase-what-cannot-
  be-produced doctrine if budget allows.
- Standardized consumables selected from common
  stock for inter-forge parts sharing.
- Payment via Specification — once removal
  equipment is confirmed at bootstrap, move to
  Section 4 as Analogous.
- Cross-reference: GF-002, ASM-003.

---

### GF-004 — Fabrication energy consumption not
characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Energy consumption of arc welding
and material removal operations has not been
characterized or cross-referenced to
Operations/Energy.md power budget.

**Why It Matters:** Arc welding draws significant
peak power — a basic MMA welder draws 2–5kW at
operating current. If fabrication competes with
Spin Chamber operation for available power,
scheduling conflicts arise.

**Resolution Path:**
- Characterize welding power draw for selected
  welding process and typical operating current.
  *(Analogous — commercial welder specifications)*
- Characterize material removal power draw —
  angle grinder 1–2kW, lathe 1–3kW typical.
  *(Analogous)*
- Cross-reference Operations/Energy.md bootstrap
  power budget — can fabrication and Spin Chamber
  operate simultaneously or must they be sequenced?
- Payment via Specification — once power draw
  is characterized and cross-referenced to
  Energy.md, move to Section 9 as Analogous.
- Cross-reference: Operations/Energy.md.

---

### GF-005 — Utilization stage has no owning file

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural                                    |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The Utilization stage — where
fabricated parts enter service and real-world
performance is validated — has no owning
specification file in the repository.

**Why It Matters:** Fabrication produces candidates
for use. Utilization determines whether they are
fit for purpose. Without a Utilization specification,
performance feedback has no governance and the
learning loop that improves fabrication quality
over time has no closing mechanism.

**Resolution Path:**
- Create Gate_07_Utilization.md — minimum content:
  performance metrics captured, failure mode
  logging, maintenance frequency tracking, and
  feedback path to Gate_06 fabrication records
  and Architecture/Forge_Net.md.
- At v0, Utilization may be as simple as a
  logging discipline — record what was made,
  how it performed, and what failed.
- The feedback loop in Section 8 assumes
  Utilization data exists — GF-005 is the
  prerequisite for that assumption to be grounded.
- Recommend creating Gate_07_Utilization.md
  as the next file after Gate_06 is loaded.
- Cross-reference: Architecture/Forge_flow.md
  Section 6 Utilization.

---

### GF-006 — Structural adequacy criteria undefined
for v0 fabrication qualification

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Section 3 qualification criteria
reference "adequate strength for v0 structural
applications" but no operational definition exists
for structural adequacy — load classes, acceptable
weld defects, fatigue expectations, or safety factor
assumptions.

**Why It Matters:** Without even coarse structural
classes, "qualified weld" risks semantic drift
between operators and across forge instances.
A weld qualified for a bracket is not necessarily
qualified for a load-bearing frame member. The
distinction matters before parts enter service.

**Resolution Path:**
- Define minimum destructive testing doctrine —
  what coupon geometry, what loading method,
  what pass/fail criterion for Phase A qualification?
- Define coarse load classes at v0:
  - Static non-load-bearing (brackets, covers)
  - Static structural (frames, supports)
  - Dynamic or cyclic (anything that moves or vibrates)
  - Safety-critical (operator protection, containment)
- Define safety factor assumptions per class —
  even rough values reduce ambiguity.
- Define acceptable weld defect limits by class —
  porosity acceptable in a bracket may not be
  acceptable in a structural frame.
- Cross-reference: Admin/Trajectories.md for
  higher precision qualification in later versions.
- Payment via Specification — once structural
  classes and minimum qualification criteria are
  defined and tested, move to Section 3 as Analogous.

---

### GF-007 — Fabrication-area fire suppression
and hot-work doctrine undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Operator PPE is well-covered but
facility-level fire mitigation for arc welding
operations is not defined. Spark containment,
fuel separation, extinguisher class requirements,
ventilation/fire interaction, and hot-work shutdown
procedures are all absent.

**Why It Matters:** Arc welding creates credible
ignition hazards in salvage environments where
upstream operations may have introduced oil residue,
plastics, dust, battery remnants, and solvents.
A salvage forge is not a clean commercial workshop —
the fire risk profile is materially different.

**Resolution Path:**
- Define spark containment — welding curtains,
  spark-resistant flooring or covers, minimum
  clearance from combustibles.
- Define fuel separation radius — minimum distance
  between active welding and oil, solvent, plastic,
  or combustible dust.
- Define extinguisher class requirements — Class B
  for flammable liquids, Class D for metal fires
  from aluminum or magnesium fines. Both may be
  needed in a salvage forge environment.
- Define hot-work shutdown — what must be cleared,
  cooled, and confirmed before leaving a welding
  area unattended.
- Ventilation/fire interaction — forced ventilation
  can feed rather than suppress a fire. Define
  shutdown sequence for ventilation in fire event.
- Consider as seed entry for `Architecture/Facilities.md`
  hot-work zone doctrine — GF-007 fire suppression
  requirements belong in the siting layer.
- Payment via Specification — once fire doctrine
  is defined and validated, move to Section 2
  as Analogous.
- Cross-reference: `Architecture/Facilities.md` FA-001,
  `Operations/Air_Scrubber.md`.

---

### Resolution Log

- 2026-05-19: GF-006, GF-007 — New entries logged
  following ChatGPT audit 2026-05-19. Structural
  adequacy criteria and fire suppression doctrine
  both identified as gaps. Welding process phase
  split (A/B/C) added to Section 3 resolving
  MMA vs MIG ambiguity. Unknown salvage alloy
  contamination defaults added to Section 2.
  Precision ceiling overclaiming disclaimer added
  to Section 5. Consumables lifecycle doctrine
  added to Section 6. Fabrication output tag
  added to Section 8.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to
  `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary updated — `Architecture/Facilities.md`
  now exists and owns siting doctrine (PC-002);
  `Architecture/Precision.md` added as precision
  ceiling doctrine owner (PC-003);
  `Operations/Gate_07_Utilization.md` reference
  corrected (GF-005 now resolved). PPE section
  UNK-006 reference updated to
  `Architecture/Facilities.md` FA-001. GF-007
  resolution path updated to reference
  `Architecture/Facilities.md`.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Fabrication as terminal endpoint — material goes in, parts come out, process ends | Fabrication without a feedback loop produces parts but no learning. Classification rules, precision ceiling, wire quality, and method capability all improve through fabrication data. A terminal fabrication stage breaks the learning loop that the entire system depends on | No — feedback loop doctrine is permanent |
| 2026-05-15 | Waiting for internal wire production to be validated before beginning arc welding qualification | Gates two unresolved unknowns on each other — SC-004 and arc welding qualification are both unvalidated. Delaying arc welding qualification until SC-004 produces qualified wire means neither advances. External wire sourcing at bootstrap per purchase-what-cannot-be-produced doctrine allows arc welding to qualify independently | Reconsider if SC-004 produces wire samples before arc welding equipment is sourced — opportunistic parallel validation is valid if both happen to be available simultaneously. See DS-001 |
| 2026-05-15 | Single precision ceiling for all fabrication methods | Different methods have different ceilings — an angle grinder and a lathe operate at fundamentally different precision levels. A single ceiling overclaims what rough tools can achieve or underclaims what precision tools can achieve | No — method-specific precision ceiling tracking is correct |
| 2026-05-15 | Achieving dimensional accuracy through forming precision alone | Variable feedstock and inherent forming imprecision make first-pass dimensional accuracy unreliable. Attempting to hit spec on the forming step produces parts that are sometimes correct and sometimes not, with no consistent path to correction | No — add-to-excess and mill-to-spec is permanent doctrine |
| 2026-05-15 | Introducing fabrication methods informally before qualification | Informal method adoption means unknown capability, unknown failure modes, and unknown safety requirements operating on real parts. An unqualified method that produces a structural failure on a critical component sets back the entire fabrication program | No — formal method introduction is permanent doctrine |
| 2026-05-15 | Treating PPE as optional or operator-discretionary for arc welding | Arc eye from UV exposure occurs in seconds. The damage is permanent and not immediately painful — operators do not realize they have been injured until hours later. Making PPE discretionary means relying on operators to self-protect against a hazard that gives no immediate warning signal | No — PPE as prerequisite is permanent doctrine |
| 2026-05-15 | Powder welding and laser welding as v0 fabrication methods | Both require upstream capabilities that do not exist at v0 — powder feedstock production, precision laser sources, controlled atmosphere. Introducing them before arc welding is qualified adds complexity without the baseline capability that justifies the complexity | Reconsider powder welding at v1+ when powder feedstock production is demonstrated. Reconsider laser welding at v2+ when precision energy delivery is validated. Route both to Admin/Trajectories.md |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to Gate_06_Fabrication:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Arc welding operation begins without PPE confirmed available and fitted | PPE is a non-negotiable prerequisite — arc eye from UV exposure is permanent and gives no immediate warning. No exceptions. |
| Arc welding qualification bypassed to begin fabricating functional parts | Qualification on scrap before functional parts is permanent doctrine — an unqualified weld on a structural component has unknown failure mode |
| Precision ceiling claimed without GF-002 characterization completed | Uncharacterized ceiling produces overconfident fabrication claims — parts made to assumed tolerance may fail in service silently |
| Fabrication records not kept for operational runs | Fabrication without records breaks the feedback loop — precision ceiling, wire quality, and method capability cannot improve without outcome data |
| New fabrication method introduced without qualification framework completion | Informal method adoption is a permanently abandoned path — unknown capability and unknown failure modes operating on real parts |
| Wire feedstock used for structural arc welding without qualification status confirmed | Unqualified wire of unknown alloy composition may produce brittle, porous, or cracked welds — wire qualification status must be known before structural use |
| Add-to-excess philosophy abandoned in favor of first-pass dimensional accuracy | Permanently correct doctrine for v0 capability levels — abandonment requires demonstrated forming precision that makes excess unnecessary, supported by GF-002 data |
| DS-001 resolved without SC-004 wire quality assessment | Wire sequencing dispute resolution must include actual wire quality data — resolving DS-001 by assumption rather than evidence reopens the unknown |
| Powder or laser welding introduced before arc welding qualification is complete | Arc welding is the gatekeeper — higher methods require the baseline to be established first. Abandoned path with version-specific reconsider conditions |
| Utilization feedback loop broken — fabricated parts enter service without performance logging | Section 8 feedback doctrine requires Utilization data — if parts enter service without logging, the learning loop closes and precision ceiling cannot improve. GF-005 prerequisite |
| PPE requirements reduced for welding on known clean base metal | Arc flash UV hazard exists regardless of base metal composition — PPE reduction based on material class is not valid. Helmet shade and gloves are always required |

### Canonical Drift Triggers

*All mandatory re-audit conditions from Admin/File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*
# Gate_07_Utilization

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Utilization is where fabricated parts and recovered
> components meet operational reality. Silent failures
> — fatigue, dimensional drift, slow property loss —
> are not detectable by v0 logging discipline alone.
> Safety-critical and load-bearing parts carry higher
> silent failure risk. Inspect at shorter intervals
> than standard. Do not assume a part is safe because
> it has not visibly failed. Observable failure is a
> lagging indicator. See GU-004.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-19; revised 2026-06-08                                      |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Low risk reflects that Utilization itself performs
no irreversible actions and creates no physical
hazards. Risk is informational — a missed utilization
record is a missed learning opportunity, not a safety
event. The safety advisory above addresses the silent
failure risk that logging discipline cannot eliminate,
not a Utilization operation risk.*

---

## Scope Boundary

**This file DOES define:**
- After action review doctrine for all fabricated
  parts and recovered components in service
- Performance logging minimum content —
  what gets recorded about every part in service
- Failure mode capture — how failures are logged,
  classified, and routed back into the system
- Maintenance frequency tracking — how often a
  part requires intervention
- Feedback path to Gate_06_Fabrication.md —
  how utilization data improves fabrication
  decisions and precision ceiling tracking
- Feedback path to Architecture/Forge_Net.md —
  how utilization data contributes to network
  knowledge base
- Feedback path to Architecture/Forge_flow.md
  classification rules — how real-world performance
  improves upstream gate routing heuristics
- Retirement handoff doctrine — when a part's
  utilization record triggers re-entry into the
  gate flow at Gate_02_Triage
- Forge Regeneration Threshold (FRT) per-cycle logging —
  measurement and record of reinvestment fraction against
  declared FRT floor (doctrine in Admin/Trajectories.md)
- Part lifecycle termination conditions — when
  a part exits the system permanently

**This file DOES NOT define:**
- Retirement routing decisions
  (Operations/Gate_02_Triage.md)
- Fabrication methods or precision ceiling
  (Operations/Gate_06_Fabrication.md)
- Component taxonomy or graduation rules
  (Architecture/Components.md)
- Network contribution validation or trust
  weighting (Architecture/Forge_Net.md)
- Gate logic governing what gets fabricated
  (Architecture/Forge_flow.md)
- Energy accounting for operational use
  (Operations/Energy.md)
- Facility siting or operational safety beyond
  logging doctrine (`Architecture/Facilities.md`
  — FA-001)
- Formal quality certification or standards
  compliance (not yet assigned — GU-003)
- FRT floor declaration and v1 economic baseline
  (`Admin/Economics.md` — EC-002)

---

## File Purpose

Gate_07_Utilization is the after action review stage
of the Lazarus Forge. It is where fabricated parts
and recovered components meet operational reality —
where the system learns whether what it made actually
worked, how long it lasted, how it failed, and what
that means for the next fabrication cycle.

Utilization does not make decisions. It produces the
record that makes decisions better. A part in service
without a utilization record is an opportunity lost —
the forge cannot learn from what it cannot observe.
A part with a complete utilization record feeds
precision ceiling improvement, wire quality
correlation, gate routing refinement, and network
knowledge contribution simultaneously.

At v0, Utilization is a logging discipline. The
operator records what was deployed, how it performed,
when it required maintenance, and how it eventually
failed or was retired. No automation is assumed. No
sensor infrastructure is required. A written log
entry after each maintenance event or failure is
sufficient to close the fabrication feedback loop
and begin accumulating the institutional memory
the forge needs to improve.

The after action review framing is intentional.
Every part that fails teaches something. Every part
that outlasts its expected service life teaches
something different. The forge that captures both
learns faster than the forge that only records
successes. If this file disappeared, fabricated
parts would enter service and disappear — the
precision ceiling would stagnate, wire quality
problems would repeat, and the self-replication
loop would have no performance signal to close
against.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Parts in service remain within observable range — the forge has access to deployed parts for performance logging | Logging doctrine; v0 deployment assumed local | Medium | Parts deployed externally or to other forge instances without feedback path — observation continuity breaks |
| ASM-002 | Operators who deploy parts maintain logging responsibility — or a reliable handoff of observation duty exists between deployment and retirement | Logging discipline; human judgment primary | Low | Automated monitoring deployed — observation continuity no longer depends on operator handoff |
| ASM-003 | Failure modes are recognizable when they occur — operators can identify when a part has failed and characterize the failure type | Failure mode capture; obvious failure assumed observable | Low | Silent failure mode identified — fatigue, dimensional drift, or gradual property loss not externally observable without instrumentation |
| ASM-004 | The fabrication output tag from Gate_06_Fabrication.md survives service and remains traceable when a part is retired or fails | Feedback path to Gate_06; tag durability in service assumed | Low | Tag loss in service breaks traceability — re-identification protocol required |
| ASM-005 | Utilization data from individual forge instances generalizes enough at network scale to benefit other forges | Network contribution value; ecology learning model | Low | Cross-forge learning found to be context-dependent — locally adaptive knowledge must be classified separately per Forge_Net.md doctrine |
| ASM-006 | Retired parts re-entering the gate flow carry sufficient utilization history to improve Gate_02 routing decisions | Retirement handoff value; assumes complete record | Medium | Utilization records found too sparse or inconsistent to improve routing — logging discipline requires revision |
| ASM-007 | At v0 scale, manual logging is sustainable — the volume of parts in service does not exceed human logging capacity | Logging discipline; v0 throughput assumed low | Medium | Parts in service volume exceeds manual logging capacity — automated or assisted logging required |

*ASM-002, ASM-003, and ASM-004 are the most
operationally fragile — they all depend on human
continuity and tag durability that cannot be
guaranteed in real field conditions. ASM-003
explicitly acknowledges that silent failures are
beyond v0 detection capability. The forge learns
from observable failures at v0. Silent failures
require instrumentation that is a future capability,
not a current assumption. Gate_06 fabrication output
tag (ASM-004) is the traceability foundation —
tag survival in service determines whether failure
data traces back to its fabrication origin.*

---

## 1. Utilization Doctrine

Utilization is the after action review stage. Its
purpose is to observe, record, and feed back the
real-world performance of every part and component
the forge deploys.

**What Utilization is:**
- A logging discipline at v0 — no automation
  required, no sensor infrastructure assumed
- The closing mechanism of the fabrication
  feedback loop
- The primary source of precision ceiling
  improvement data
- The system's institutional memory of what
  worked, what failed, and why

**What Utilization is not:**
- A decision-making gate — retirement and
  routing decisions belong to Gate_02_Triage
- A quality certification system — formal
  standards compliance is out of scope at v0
- A real-time monitoring system — v0 logging
  is event-driven, not continuous

**Core doctrine:**
- Every part that enters service gets a
  utilization record opened at deployment
- Every maintenance event is logged
- Every failure is logged, classified, and
  routed as a feedback signal
- Every retirement triggers a handoff record
  to Gate_02_Triage
- A part that leaves service without a
  utilization record is a missed learning
  opportunity — not a system fault, but a
  gap the forge should work to close

**Observation continuity:**
The forge can only learn from what it can observe.
Parts deployed externally — to other forges, to
end users, to field use beyond the forge's reach —
have no guaranteed feedback path. At v0, prioritize
deploying parts within observable range first.
External deployment is valid but explicitly noted
as reduced-feedback in the utilization record.

---

## 2. Performance Logging

Performance logging is the primary output of
Gate_07_Utilization. Every part in service has
an active log. Every log feeds back to fabrication,
network, and gate routing.

**Utilization record minimum content:**

| Field | Content | Notes |
|---|---|---|
| Part identifier | From Gate_06 fabrication output tag | Links back to forge, operator, feedstock, method |
| Deployment date | When part entered service | |
| Deployment context | What application, what load class | Coarse is acceptable — "structural bracket," "bearing mount," "electrical connector" |
| Expected service life | Operator estimate at deployment | Compared against actual at retirement |
| Maintenance events | Date, type, outcome for each | Running log throughout service life |
| Failure event | Date, failure mode, severity | If applicable |
| Retirement date | When part left service | |
| Retirement reason | Planned end of life, failure, upgrade, lost | |
| Actual service life | Calculated from deployment to retirement | |
| Performance assessment | Met expectations, exceeded, fell short | Operator judgment |
| Feedback flags | Precision ceiling relevant, wire quality relevant, gate routing relevant | Tag what this record should feed back to |

**Logging cadence:**
- Open record at deployment
- Log each maintenance event within 24 hours
  of occurrence *(Placeholder — cadence validated
  operationally)*
- Close record at retirement with full summary
- No minimum logging interval between maintenance
  events — log what happens when it happens

**Observation gap doctrine:**
If a part cannot be observed for a period —
external deployment, inaccessible location,
operator change — log the gap explicitly.
A known gap is better than a false continuity.

---

## 2b. Forge Regeneration Threshold (FRT) Logging

The FRT is a system health metric defined in `Admin/Trajectories.md`.
Gate_07_Utilization owns the per-cycle measurement record. This section
defines what gets logged and when.

**What FRT logging captures:**

| Field | Content | Notes |
|---|---|---|
| Cycle identifier | Operating period this record covers | Month, audit cycle, or declared throughput batch — per operator declaration at commissioning |
| Total throughput value | Estimated value of material processed this cycle | Analogous or measured — label confidence level |
| Reinvestment amount | Value reinvested in Forge capability development this cycle | See Trajectories.md §What Counts as Reinvestment |
| Reinvestment fraction | Reinvestment ÷ throughput value | Compare against declared FRT floor |
| FRT floor (declared) | Operator-declared threshold for this Forge instance | Placeholder [2–5%] until calibrated — see TR-002 |
| FRT status | Above floor / Below floor / Placeholder (not yet calibrated) | |
| Below-floor note | If below floor: reason and recovery plan | Required if below floor — operator documented |
| Cumulative below-floor cycles | Running count of consecutive cycles below declared floor | Trigger review if count exceeds [N] — Placeholder |

**Logging cadence:** Once per declared FRT cycle — at cycle close,
before the next cycle opens.

**FRT floor calibration:** The FRT floor begins as Placeholder [2–5%].
After first operational cycle, the operator reviews actual reinvestment
patterns and declares a calibrated floor. Log the calibration event in
the Resolution Log with date and basis.

**Below-floor response:**
- 1 cycle below floor: log reason, document recovery plan
- [N] consecutive cycles below floor: flag as systemic decline indicator,
  escalate to human review, open GU-005 status update
- *(N is Placeholder — declared by operator at commissioning)*

**Relationship to v1 exit condition:**
FRT data feeds directly into TR-001 (v1 profitability baseline). A Forge
that has run sufficient cycles to calibrate its FRT floor has one of the
required inputs for the v1 economic model.

**v0 honest acknowledgment:** At v0, throughput value and reinvestment
amount may be rough estimates. Label all values with confidence level
(Measured / Analogous / Placeholder). An approximate FRT record is better
than none — the pattern across cycles matters more than precision in any
single cycle.

---

## 3. Failure Mode Capture

Failure records are the highest-value utilization
output. A part that fails teaches more than a part
that outlasts its expected service life without
observation.

**Failure classification at v0:**

| Class | Description | Example |
|---|---|---|
| Weld failure | Failure at or near a weld joint | Cracked bead, incomplete fusion propagation |
| Base material failure | Failure in parent material away from weld | Alloy brittleness, fatigue crack |
| Dimensional failure | Part no longer meets dimensional requirement | Wear beyond tolerance, thermal distortion |
| Surface failure | Coating, finish, or surface integrity loss | Corrosion, erosion, adhesion failure |
| Fit failure | Part no longer fits its application | Deformation, creep, mating surface wear |
| Unknown | Failure mode not identifiable | Log what was observed, not what is inferred |

**Failure record minimum content:**
- Part identifier and utilization record reference
- Failure date and service life at failure
- Failure class from table above
- Failure location — weld zone, base material,
  surface, dimensional, fit
- Failure description — what the operator observed
- Contributing factors if identifiable — overload,
  corrosion, fatigue, improper installation
- Downstream impact — did the failure propagate?
  Did it cause secondary damage?
- Feedback flags — what does this failure suggest
  about fabrication process, material quality,
  or gate routing?

**Failure doctrine:**
- All failures are logged regardless of severity —
  minor failures teach as much as catastrophic ones
- Failures are not blamed — they are classified
  and learned from
- A weld failure routes feedback to Gate_06
  Section 3 qualification criteria and GF-006
- A base material failure routes feedback to
  Gate_05_Separation_Thermal.md SC-002
  segregation effectiveness
- An unknown failure is logged as unknown —
  do not infer cause without evidence

---

## 4. Feedback Paths

Utilization data is only valuable if it reaches
the decisions it can improve. Four feedback paths
are active at v0.

**Path 1 — Gate_06_Fabrication.md:**
- Weld failure data informs qualification criteria
  and structural adequacy assessment (GF-006)
- Dimensional failure data informs precision
  ceiling characterization (GF-002)
- Wire quality correlation — weld failures on
  internally produced wire feed back to SC-002
  segregation effectiveness and SC-004 wire
  extrusion quality
- Fabrication phase tracking — which phase
  (A, B, or C) produced the part affects how
  failure data is interpreted

**Path 2 — Architecture/Forge_Net.md:**
- All utilization records are candidates for
  network contribution when connectivity allows
- Failure mode classifications with part
  identifiers contribute to shared knowledge base
- Cross-forge pattern detection — if multiple
  forges report the same failure mode on the
  same application, the network learns a
  systemic issue
- Locally adaptive knowledge — failure modes
  specific to a deployment environment
  (marine corrosion, high temperature, dusty
  conditions) are classified as locally adaptive
  per Forge_Net.md knowledge classification

**Path 3 — Architecture/Forge_flow.md:**
- Performance data improves classification
  heuristics — a component type that consistently
  underperforms in a specific application routes
  differently at Gate_02 in future cycles
- Expected vs. actual service life data improves
  the want/need policy — a part that lasts
  longer than expected changes the replacement
  urgency calculation

**Path 4 — Architecture/Components.md:**
- Parts that consistently exceed performance
  expectations may graduate to higher component
  classification
- Parts that consistently underperform may be
  downgraded in the component taxonomy
- Precision ceiling improvements documented
  in utilization records feed Components.md
  Metrology and Baseline Observability items

**Feedback contribution minimum:**
At the close of each utilization record, the
operator identifies which feedback paths are
relevant and tags the record accordingly.
A record tagged for Gate_06 feedback is
reviewed against current fabrication parameters
at the next fabrication planning cycle.

---

## 5. Retirement Handoff

When a part leaves service — by planned end of
life, failure, upgrade, or loss — its utilization
record closes and a retirement handoff initiates
re-entry into the gate flow.

**Retirement triggers:**

| Trigger | Next Step |
|---|---|
| Planned end of life — service life reached | Close record, assess for Gate_02 re-entry |
| Failure — part no longer functional | Close record, route to Gate_02 with failure classification |
| Upgrade — replaced by better part | Close record, assess retired part for Gate_02 re-entry |
| Loss — part cannot be located | Close record with loss notation, log tag number as missing |
| External retirement — part retired outside forge | Request retirement data if available, close record with gap notation |

**Retirement handoff record minimum content:**
- Part identifier and complete utilization record
- Retirement trigger and date
- Actual service life
- Performance summary — met, exceeded, or fell
  short of expectations
- Failure classification if applicable
- Fabrication output tag status — intact,
  damaged, or lost
- Recommended Gate_02 entry classification:
  - Functional — route to Gate A assessment
  - Repairable — route to Gate B assessment
  - Material only — route to Gate D / Reduction
  - Hazardous — hold for specialist assessment
  - Lost — no physical item to route

**Retirement handoff doctrine:**
- Gate_07 recommends the Gate_02 entry
  classification. Gate_02 makes the routing
  decision. Gate_07 does not override Gate_02.
- A part retired due to failure is not
  automatically routed to Reduction — it may
  have repairable or repurposable value.
  Gate_02 assessment determines this.
- The fabrication output tag travels with the
  retired part to Gate_02. If the tag is lost,
  log it. Gate_02 can still route the part —
  but the traceability chain is broken and
  the feedback value is reduced.

---

## 6. Integration Hooks

- `Architecture/Forge_flow.md` — governing flow;
  Utilization is the final stage; feedback to
  classification rules lives here
- `Operations/Gate_02_Triage.md` — receives
  retired parts with utilization records;
  makes routing decisions based on retirement
  handoff recommendations
- `Operations/Gate_06_Fabrication.md` — primary
  feedback recipient; weld quality, dimensional
  outcomes, and precision ceiling data all feed
  fabrication improvement
- `Operations/Gate_05_Separation_Thermal.md` —
  base material failures feed back to segregation
  effectiveness (SC-002) and wire quality (SC-004)
- `Architecture/Forge_Net.md` — utilization
  records contributed to network knowledge base;
  cross-forge failure pattern detection
- `Architecture/Components.md` — performance
  data feeds component graduation and taxonomy
  updates; precision ceiling improvements noted
- `Admin/Ship_of_Theseus.md` — utilization
  record closes the grain provenance chain
  for each part; full lifecycle documented
- `Unknowns.md` — GU-001 through GU-004
  indexed once logged

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-19 | Audit Review | Utilization conceived as terminal stage — parts enter service and system moves on | Without feedback loop, fabrication becomes industrial output not adaptive learning. Precision ceiling stagnates, wire quality problems repeat, self-replication loop has no performance signal | Utilization reframed as after action review — closing mechanism of fabrication feedback loop. Every part in service is an active data source | Analogous | No — after action review framing is correct |
| 2026-05-19 | Audit Review | Feedback assumed to happen naturally once utilization data exists | Data does not route itself. Four distinct feedback paths each require explicit operator tagging and routing | Explicit feedback path doctrine added to Section 4. Operator tags each record for relevant paths at close. Feedback contribution is deliberate, not automatic | Analogous | Yes — validate feedback routing against first operational cycle |
| 2026-05-19 | Audit Review | Failure records treated as negative outcomes to minimize | Minimizing failure records produces a forge that appears to succeed but does not learn. Silent failure accumulation is the worst outcome | Failure doctrine added — all failures logged regardless of severity, failures classified not blamed, unknown failures logged as unknown | Analogous | No — failure doctrine is permanent |
| 2026-05-19 | Audit Review | Retirement assumed to mean Reduction | Retired part may be functional in reduced application, repairable, or hazardous. Automatic Reduction wastes recovery value | Retirement handoff doctrine — Gate_07 recommends Gate_02 classification, Gate_02 makes routing decision | Analogous | No — retirement handoff doctrine is correct |
| 2026-05-19 | Audit Review | Silent failures not acknowledged as v0 limitation | Fatigue, dimensional drift, and slow property loss are not externally observable without instrumentation | ASM-003 explicitly acknowledges silent failure limitation. The forge learns what it can observe. Silent failure detection is future capability | Analogous | Yes — revisit when instrumentation capability develops |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | Whether Gate_07 should own fitness-for-purpose assessment or strictly after action review | Position A: Gate_07 assesses whether a part remains fit for continued service at each maintenance event — keeps assessment close to performance data. Position B: Fitness-for-purpose is a routing decision belonging at Gate_02_Triage — Gate_07 owns the record, Gate_02 owns the decision | Low | Open | Operations/Gate_07_Utilization.md |

*DS-001 reflects a genuine boundary tension between
observation and decision. Position B is the current
standing doctrine — Gate_07 produces records, Gate_02
makes routing decisions. This keeps the after action
review role clean and prevents Gate_07 from absorbing
triage responsibility. Revisit if operational experience
shows Gate_02 consistently lacks context needed to make
good retirement decisions. Trigger: three consecutive
retirement routing disagreements between Gate_07
recommendation and Gate_02 decision.*

---

## Auditor Notes & Unknowns

### GU-001 — Performance metric schema not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The performance metric schema —
field types, value formats, and comparable data
structures — is defined at minimum content level
but not at schema level. Cross-forge comparison
requires compatible record structures.

**Why It Matters:** Utilization data contributed
to Architecture/Forge_Net.md is only comparable
across forge instances if records share a compatible
schema. A record logging "held up well" cannot be
meaningfully compared with "load bearing cycles:
1,247." Cross-forge pattern detection depends on
schema compatibility.

**Resolution Path:**
- Define minimum field types and value formats
  for each utilization record field.
- Define performance assessment scale — even a
  coarse three-point scale produces more comparable
  data than free text.
- Cross-validate schema against Forge_Net.md
  contribution format requirements once FN-001
  validation criteria are defined.
- Payment via Specification — once schema is
  defined and validated against first operational
  cycle records, move to Section 2 as Analogous.
- Cross-reference: FN-001, GI-006.

---

### GU-002 — Retirement handoff protocol not
cross-validated with Gate_02_Triage

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The retirement handoff record
format and recommended classification scheme have
not been cross-validated against Gate_02_Triage
intake requirements.

**Why It Matters:** If the recommendation format
is incompatible with Gate_02's decision logic,
the utilization record becomes noise rather than
signal at the most important handoff in the
retirement cycle.

**Resolution Path:**
- Review Gate_02_Triage.md intake requirements.
- Cross-validate Section 5 retirement handoff
  record minimum content against Gate_02 needs.
- Define how Gate_02 receives and acts on a
  Gate_07 routing recommendation.
- Payment via Specification — once handoff format
  is cross-validated and tested through at least
  one operational retirement cycle, move to
  Section 5 as Analogous.
- Cross-reference: Operations/Gate_02_Triage.md,
  DS-001.

---

### GU-003 — Formal quality certification and
standards compliance unowned

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Formal quality certification —
pressure ratings, load certifications, electrical
safety standards — is explicitly out of scope for
v0 Utilization. No file currently owns this future
requirement.

**Why It Matters:** As the forge ecology grows
and fabricated parts enter external trade or
critical applications, standards compliance
becomes operationally necessary. The absence
of an owner is not a current blocker but is
a trajectory gap.

**Resolution Path:**
- Discharge via Trajectory — route to
  Admin/Trajectories.md as v2+ consideration.
- When standards compliance becomes operationally
  necessary, create dedicated file or assign
  ownership to existing governance file.
- Cross-reference: Admin/Trajectories.md,
  Admin/Ship_of_Theseus.md.

---

### GU-004 — Silent failure detection capability
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Silent failures — fatigue crack
initiation, gradual dimensional drift, slow
conductivity loss, creep deformation — are not
externally observable without instrumentation.
At v0, the forge learns from observable failures
only.

**Why It Matters:** Safety-critical and load-bearing
parts may exhibit silent failure progression before
visible failure occurs. This is an acknowledged
v0 limitation, not a gap to paper over — but it
needs a defined upgrade path.

**Resolution Path:**
- Acknowledge explicitly that v0 utilization
  logging captures observable failures only.
- Define upgrade path — strain gauges, temperature
  sensors, vibration monitoring on high-criticality
  parts as first instrumentation step.
- Safety-critical parts per GF-006 flagged for
  shorter inspection intervals.
- Payment via Specification — once instrumentation
  capability exists and silent failure detection
  is validated, move to Section 3 as Measured.
- Cross-reference: ASM-003, GF-006,
  Architecture/Components.md Baseline Observability.

---

---

### GU-005 — Forge Regeneration Threshold cycle definition and floor not yet declared

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-23                                       |
| Last Reviewed | 2026-05-23                                       |

**Description:** The FRT cycle definition (month / audit cycle / throughput
batch) and the calibrated FRT floor have not been declared by an operator.
The Placeholder floor [2–5%] applies until first operational cycle data exists.

**Why It Matters:** Without a declared cycle definition, FRT logging cannot
begin. Without a calibrated floor, the systemic decline threshold is undefined.
Both are prerequisites for FRT records feeding meaningfully into the v1
economic model (TR-001).

**Resolution Path:** Discharge via Lessons Learned — operator declares cycle
definition at v0 commissioning. After first cycle, review actual reinvestment
patterns and calibrate floor. Log calibration event in Resolution Log with
date and basis. Cross-reference TR-002 (Trajectories.md) — same unknown,
different owning file. FRT floor calibration closes both.

---

### Resolution Log

- 2026-05-23: GU-005 added — FRT cycle definition and floor declaration
  pending operator commissioning decision. FRT logging section (Section 2b)
  added to body. Scope Boundary updated. Open unknowns count updated to 5.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected
  from `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates_LF.md`
  (PC-001). Scope Boundary updated — `Architecture/Facilities.md` reference
  added replacing `UNK-006` (PC-002); `Admin/Economics.md` added as FRT
  floor and v1 economic baseline owner (PC-003).

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-19 | Utilization as terminal stage — parts enter service and system moves on without structured feedback | Terminal stage produces parts but no learning. Precision ceiling stagnates, wire quality problems repeat, self-replication loop has no performance signal. The forge that does not debrief does not improve | No — after action review doctrine is permanent |
| 2026-05-19 | Gate_07 making retirement routing decisions | Retirement routing is a triage decision belonging at Gate_02_Triage where full gate logic applies. Gate_07 owns the record and recommendation — not the decision | Reconsider if operational experience shows Gate_02 consistently lacks context for retirement decisions — see DS-001 trigger condition |
| 2026-05-19 | Automatic Reduction routing for all retired parts | Retired part may be functional in reduced application, repairable, or hazardous. Automatic Reduction wastes recovery value and contradicts preserve-before-destruction doctrine | No — Gate_02 assessment of retired parts is permanent doctrine |
| 2026-05-19 | Continuous real-time monitoring as v0 utilization doctrine | Sensor infrastructure and automated monitoring require capability that does not exist at v0 bootstrap. Treating real-time monitoring as baseline makes utilization conditional on infrastructure that may never exist at small forge scale | Reconsider at v2+ when sensor capability and power budget justify continuous monitoring |
| 2026-05-19 | Failure records treated as negative outcomes to minimize | Minimizing failure records produces a forge that appears to succeed but does not learn. A culture that discourages failure logging produces silent failure accumulation | No — failure logging culture is permanent doctrine |
| 2026-05-19 | Utilization data assumed to route itself to relevant feedback targets | Data does not route itself. Four distinct feedback paths each require explicit operator tagging and routing. Without deliberate contribution, utilization data accumulates locally and never improves the system | No — explicit feedback path tagging is permanent doctrine |

---

## Drift Indicators

The following conditions trigger mandatory re-audit
of this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to
Gate_07_Utilization:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Parts enter service without utilization records opened at deployment | After action review doctrine requires records open at deployment — retroactive logging loses deployment context |
| Failure records not logged because failure was minor or embarrassing | Failure logging culture is permanent doctrine — all failures regardless of severity. Selective logging produces false confidence and silent failure accumulation |
| Gate_07 begins making retirement routing decisions without DS-001 resolution | Permanently abandoned path — Gate_07 recommends, Gate_02 decides. Boundary change requires explicit audit cycle and DS-001 resolution |
| Retired parts routed directly to Reduction without Gate_02 assessment | Permanently abandoned path — retired parts are not exhausted parts. Gate_02 assessment is mandatory before Reduction |
| Feedback path tagging abandoned in favor of unstructured free-text records | Explicit feedback path tagging is permanent doctrine — unstructured records do not route to the decisions they can improve |
| GU-001 schema remains undefined when cross-forge utilization comparison is attempted | Schema compatibility is prerequisite for cross-forge learning — comparison without compatible schemas produces misleading patterns |
| GU-002 retirement handoff format remains unvalidated at first operational retirement | Handoff format must be cross-validated with Gate_02 before first retirement — incompatible formats make utilization record noise at handoff |
| Safety-critical parts per GF-006 not flagged for shorter inspection intervals | Silent failure risk is higher for load-bearing parts — standard inspection interval is insufficient |
| Real-time monitoring introduced as replacement for event-driven logging before v2 instrumentation capability | Continuous monitoring is v2+ capability — introducing before power budget and sensor capability are validated creates infrastructure dependency |
| FRT logging omitted from cycle close | FRT records are a required output of each cycle close — omission breaks the system health measurement chain and TR-001 input path |
| Fabrication output tag from Gate_06 not verified at retirement handoff | Tag survival is the traceability chain — unverified tag status at retirement breaks feedback loop between service performance and fabrication origin |

### Canonical Drift Triggers

*All mandatory re-audit conditions from
Admin/File_Template.md Section 10 apply without
exception. Local triggers above are additive,
not substitutes.*
# Plastics.md — Salvaged Polymers & Pyrolytic Fuel Recovery

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Thermal depolymerization (pyrolysis) operates at high temperatures (300°C–500°C)
> and generates highly flammable, toxic hydrocarbons and synthetic gas. Enclosure
> breach or oxygen ingress creates an immediate risk of explosive pressure buildup
> or flashback fire. Halogenated plastics (PVC, Teflon) release hydrochloric acid
> gas and dioxins at pyrolysis temperatures — reactor corrosion and toxic bypass are
> credible failure modes if triage misses contaminated feedstock. See PL-001.
> Air Scrubber operation, continuous venting, and oxygen exclusion are
> non-negotiable prerequisites before heating begins. When in doubt, do not heat.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-27 (Grok — Skeptic/Auditor); revised 2026-06-08             |
| Auditor          | Grok — Skeptic/Auditor                                              |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Triage routing doctrine for salvaged industrial and consumer polymers
- Conceptual framework for low-pressure, oxygen-free thermal depolymerization
  (pyrolysis)
- High-level design requirements for a batch-fed reaction chamber and condenser array
- Safety and chemical containment boundaries for off-gas treatment
- Char and solid residue handling doctrine

**This file DOES NOT define:**
- Precise temperature profiles for individual or unique polymer blends
- Mechanical blueprints for custom extrusion screws or filament-drawing rigs
- Refining or fractional distillation specifications for separating fuel oil into
  specialized fuel grades
- Air Scrubber hardware specification or alkaline buffering stage design
  (→ `Operations/Air_Scrubber.md`)
- Energetic or radiological hazard screening at intake
  (→ `Operations/Gate_01_Intake.md`)
- Contamination routing beyond plastic stream identification
  (→ `Operations/Gate_02_Triage.md`)
- Energy accounting for pyrolysis reactor operation
  (→ `Operations/Energy.md`)
- Facility siting, clearance, and hot-work zone requirements
  (→ `Architecture/Facilities.md` — FA-001)
- Operator PPE standards and hearing/respiratory conservation program
  (→ `Admin/Safety_Protocols.md`)

---

## File Purpose

This document establishes the processing path for salvaged plastics within the
Lazarus Forge. Mixed or contaminated polymers represent both a recovery opportunity
and a significant logistical hazard — they cannot be safely routed to thermal
processing alongside metals, and mechanical repurposing yields diminish rapidly
with degradation. This file defines the triage hierarchy that routes plastics
toward the highest-value recovery path available, and specifies the pyrolytic fuel
recovery framework that handles what mechanical repurposing cannot.

Pyrolysis is positioned as a last-resort recovery path for otherwise intractable
mixed waste, not as a primary recycling method. Its core claim is falsifiable: mixed
low-value plastics can be safely converted to usable pyrolytic oil and syngas via
oxygen-free batch pyrolysis, provided halogenated streams are rejected at triage and
off-gases are captured by the Air Scrubber. If this file disappeared, mixed plastic
waste would have no governed processing path, and operators would lack the safety
doctrine required to handle pyrolysis off-gases and halogenated contamination.

---

## Assumptions

| ID      | Assumption                                                                                         | Basis                                                    | Confidence | Expiry Trigger                                                                 |
|---------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------|--------------------------------------------------------------------------------|
| ASM-001 | Sourced plastic feedstock will contain unrecognized or highly degraded multi-layer polymers        | Consumer and industrial salvage is fundamentally mixed; high-purity sorting cannot be guaranteed at v0 | High | First operational triage cycle characterizes actual feedstock purity distribution |
| ASM-002 | Mechanical recycling yields diminish rapidly after multiple heat cycles                            | Polymers shorten and degrade during mechanical re-extrusion; chemical breakdown path required for persistence | High | Operational filament-drawing data shows acceptable yield beyond current assumed threshold |
| ASM-003 | Waste heat from Spin Chamber or external sources can bootstrap reactor thermal demand              | Analogous — industrial waste heat recovery practice; cross-reference `Operations/Gate_05_Separation_Thermal.md` SC-007 | Low | SC-007 resolved — exhaust heat load characterized and available capacity confirmed |
| ASM-004 | Halogenated plastics (PVC, Teflon) are identifiable and rejectable at triage before reactor entry  | Beilstein test and density sorting are established detection methods | Low | PL-001 resolved — triage protocol validated against representative feedstock sample |
| ASM-005 | Pyrolytic oil from mixed plastic feedstock is usable as heating fuel or generator input without significant refining | Analogous — small-scale pyrolysis literature; oil quality varies by feedstock | Low | PL-003 resolved — oil stability and contaminant profile characterized |

---

## I. General Plastics Triage Hierarchy

Consistent with the principle of *Salvage Before Reduction*, plastics enter a
progressive depth triage sequence:

1. **Direct Component Reuse:** Structural panels, enclosures, or functional hardware
   are preserved intact.
2. **Mechanical Repurposing (RepRap / Filament):** High-purity, cleanly identified
   single-stream plastics (e.g., clean PLA, ABS, PETG) are routed toward shredding
   and drawing into custom fabrication stock.
3. **Thermal Depolymerization (Pyrolysis):** Mixed, degraded, contaminated, or
   low-value bulk plastics that cannot support mechanical repurposing enter the
   chemical recovery loop.

**Triage decision boundary for mechanical vs. pyrolysis routing:**
The threshold at which plastic is too degraded for mechanical repurposing is
not yet formally defined — see PL-004. Provisional indicators that favor pyrolysis
routing over filament drawing: visible embrittlement or chalking, unknown polymer
identity, multi-layer or composite construction, visible contamination or bonded
dissimilar materials, or melt-flow behavior inconsistent with a known single
polymer class.

**Halogenated polymer rejection:**
PVC, Teflon, and other halogenated plastics must not enter the pyrolysis reactor.
At triage, suspected halogenated material is identified using the Beilstein test
(copper wire combustion — green flame indicates halogen presence) or density
sorting (PVC density ~1.4 g/cm³ is distinctly higher than most common
thermoplastics). Confirmed halogenated material routes to specialist disposal,
not to the reactor. See PL-001.

---

## II. Pyrolytic Fuel Recovery Framework

Pyrolysis breaks down long-chain hydrocarbon molecules into shorter-chain liquid
and gaseous fuels. The process requires a closed system operating under three phases.

**Critical dependency:** This entire section depends on `Operations/Air_Scrubber.md`
being operational and maintaining alkaline buffering capacity before and during any
reactor run. Pyrolysis off-gas is toxic and flammable. Scrubber shutdown during an
active run is an emergency stop condition — see Drift Indicators. The alkaline
buffering stage in the scrubber is specifically required to neutralize any HCl
that bypasses halogenated feedstock rejection at triage. Cross-reference:
`Operations/Air_Scrubber.md` AS-003 (scrubber waste stream and saturation thresholds).

### A. Thermal Breakdown (The Reactor)

- Feedstock is sealed into an airtight batch reactor chamber
- The chamber is purged of oxygen — via inert gas purge or vacuum extraction —
  before heating begins. Purge completion must be logged before heat is applied.
- External heat raises the chamber temperature to **350°C–450°C** *(Analogous —
  standard pyrolysis temperature range for mixed polyolefins; halogen-free feedstock
  assumed)*
- At temperature, carbon-carbon bonds fracture, vaporizing solid plastic into
  gaseous hydrocarbons
- Reactor wall corrosion from residual acid gas is a credible long-term failure mode —
  see PL-002 for maintenance access and inspection requirements

### B. Condensation & Liquid Capture

- Vaporized gases are channeled from the reactor into a multi-stage condensation array
- Heavy-to-medium hydrocarbon chains condense at decreasing temperatures, producing
  pyrolytic oil (synthetic crude)
- Condensation array fouling from wax paraffins and heavy fractions is a maintenance
  item — cleaning access must be designed in from the start. See PL-002.
- Pyrolytic oil is stored for use as heating fuel, motor-generator input, or feedstock
  for downstream Forge thermal processes
- Oil stability and contaminant profile are uncharacterized at v0 — see PL-003

### C. Non-Condensable Syngas Channeling

- Light hydrocarbon gases (methane, ethane, propane fractions) will not condense at
  ambient temperatures and must be continuously drawn from the end of the condensation
  array
- Continuous draw maintains low-pressure state in the reactor — pressure buildup is
  a rupture risk. See PL-002.
- **Critical Safety Boundary:** Syngas must never accumulate in unvented spaces.
  Route immediately to a designated burner for controlled combustion, or channel
  directly into the Air Scrubber intake manifold for capture. The Air Scrubber is
  not a combustion device — syngas routed to the scrubber must pass through a
  dedicated combustion or thermal oxidation stage upstream of the scrubber inlet.
  Direct routing of unburned syngas into scrubbing liquid is not acceptable.

### D. Char and Solid Residue

- Real-world pyrolysis produces 5–20% solid char and ash residue by feedstock mass,
  depending on polymer type and contamination level *(Analogous — pyrolysis
  literature for mixed plastic feedstock)*
- Char composition is unknown at v0 — it may contain concentrated heavy metals,
  carbon black, inorganic fillers, and residual halogenated compounds from
  insufficiently rejected feedstock
- Char is not discarded as inert waste — it routes to `Operations/Gate_02_Triage.md`
  for assessment: potential carbon feedstock, potential hazardous waste requiring
  specialist handling
- Do not assume char is inert. Treat as potentially hazardous until characterized.
  See PL-005.

---

## Integration Hooks

- `Operations/Air_Scrubber.md` — primary safety dependency; off-gas capture,
  HCl neutralization via alkaline buffering stage, syngas combustion upstream
  of scrubber inlet; cross-reference AS-003 for saturation thresholds
- `Operations/Gate_01_Intake.md` — halogenated polymer detection at entry;
  GI-003 augmented detection capability applies to plastic stream identification
- `Operations/Gate_02_Triage.md` — upstream routing decision for all plastics;
  char residue routes back here for hazardous vs. recoverable classification
- `Operations/Gate_03_Reduction.md` — pyrolysis is reduction-adjacent; shredding
  of bulk plastic feedstock before reactor loading follows Reduction doctrine
- `Operations/Gate_06_Fabrication.md` — mechanical repurposing path (filament
  drawing) connects to fabrication feedstock; RepRap stock quality feeds back
  to PL-004 threshold definition
- `Operations/Energy.md` — pyrolytic oil and syngas are candidate energy inputs
  to motor-generators and heating systems; reactor thermal demand feeds energy
  accounting
- `Operations/Gate_05_Separation_Thermal.md` — waste heat from Spin Chamber
  is a candidate bootstrap heat source for reactor thermal demand (ASM-003,
  SC-007)
- `Admin/Trajectories.md` — fractional distillation, filament extrusion hardware
  specification, and deep characterization of oil quality are v1+ scope items
- `Architecture/Facilities.md` — siting and hot-work zone requirements;
  pyrolysis reactor clearance zones and ventilation topology (FA-001)
- `Admin/Safety_Protocols.md` — operator PPE standards; respiratory protection
  requirements for toxic off-gas handling

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Document created without syngas combustion stage specified | Syngas routed directly to Air Scrubber without noting that scrubber is not a combustion device — silent safety gap | Syngas must pass through dedicated combustion or thermal oxidation stage before scrubber inlet. Direct routing of unburned syngas into scrubbing liquid is not acceptable | Analogous | Yes — validate combustion stage design before first hot run |
| 2026-05-27 | Audit Review  | Char residue not acknowledged in initial draft | Pyrolysis always produces solid residue; omitting it created an incomplete material balance and a potential untracked hazardous waste stream | Char handling added as Section D. Char routes to Gate_02_Triage for classification — do not assume inert | Analogous | Yes — characterize char composition during first operational run |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### PL-001 — Halogenated Polymer Contamination (PVC / Teflon)

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Chemical Safety                                  |
| Blocking      | Yes (before any hot operational runs)            |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-05-27                                       |

**Description:** PVC and other halogenated plastics release hydrochloric acid (HCl)
gas and toxic dioxins when subjected to pyrolysis temperatures. Even small quantities
contaminate the entire reactor batch.

**Why It Matters:** HCl corrodes steel reactor vessels from the inside out over
repeated cycles and easily bypasses basic carbon filtration, creating both a
structural failure risk and a toxic environmental hazard. Dioxin release is a
severe long-term health and contamination risk.

**Resolution Path:** Define and validate a triage rejection protocol before first
hot run — minimum: Beilstein test (copper wire, green flame = halogen present)
and density sorting (PVC ~1.4 g/cm³). Cross-reference `Operations/Gate_01_Intake.md`
GI-003 for augmented detection capability. Verify that `Operations/Air_Scrubber.md`
alkaline buffering stage (cross-reference AS-003) is capable of neutralizing
accidental acid gas bypass from imperfect triage rejection. Payment via
Specification once triage protocol is validated against a representative
feedstock sample and scrubber alkaline stage is confirmed.

---

### PL-002 — Reactor Thermal Runaway, Pressure Control, and Maintenance Access

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Major                                            |
| Type          | Mechanical Engineering / Safety                  |
| Blocking      | Yes (before reactor fabrication)                 |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-05-27                                       |

**Description:** The rate of vapor generation must not exceed the throughput
capacity of the condensation plumbing. Additionally, the reactor and condensation
array will experience progressive corrosion (acid attack from trace HCl), wax
fouling in condenser passages, and thermal cycling fatigue — none of which have
defined inspection intervals or maintenance access provisions.

**Why It Matters:** Rapid gas expansion inside a hot sealed container can cause
explosive mechanical rupture. Progressive corrosion or fouling without maintenance
access creates silent failure modes — the reactor degrades without visible
external indicators until a breach occurs.

**Resolution Path:** Specify a passive, high-reliability mechanical pressure
relief system (liquid-sealed bubbler lock) that allows emergency pressure relief
without admitting ambient air to the hot reactor. Define maintenance access points
for reactor interior inspection, condenser cleaning, and corrosion assessment.
Establish minimum inspection interval cadence (Placeholder — to be defined during
first operational cycle). Payment via Specification once relief system design is
validated and maintenance access provisions are incorporated into reactor design.

---

### PL-003 — Pyrolytic Fuel Stability and Contaminant Profile

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Minor                                            |
| Type          | Fuel Chemistry                                   |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-05-27                                       |

**Description:** Recovered synthetic crude oil from mixed plastic pyrolysis is
often acidic and contains wax paraffins that separate and solidify at room
temperature. Contaminant profile varies by feedstock composition.

**Why It Matters:** Unrefined oil may clog secondary engine injectors or rapidly
corrode standard fuel storage containers if left untreated. Acidic oil damages
motor-generator components not designed for fuel oil service.

**Resolution Path:** Characterize minimum filtration or post-process washing steps
required to render oil stable for long-term storage in Forge auxiliary power
reserves. Cross-reference `Operations/Energy.md` for integration with motor-generator
fuel input. Payment via Specification once oil quality is characterized from first
operational reactor run.

---

### PL-004 — Mechanical Filament-Drawing Threshold Not Defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical Specification                          |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-05-27                                       |

**Description:** The exact conditions under which mechanical plastic recycling
(RepRap filament drawing) becomes unfeasible due to contamination or structural
degradation are unquantified. Triage routing between mechanical and pyrolysis
paths currently relies on operator judgment against provisional visual heuristics.

**Why It Matters:** Without a defined boundary, subjective routing during triage
may cause degraded feedstock to clog the fabrication gate or viable feedstock to
be prematurely destroyed.

**Resolution Path:** Establish formal triage heuristics — minimum: brittleness
snap test, melt-flow observation, polymer identity check (Beilstein, density,
or burn characteristics). Define pass/fail criteria for mechanical repurposing
routing. Candidate methods: melt-flow index testing (simple improvised version
feasible at v0), density measurement in water bath. Payment via Specification
once heuristics are validated against first operational triage cycle with
representative mixed feedstock.

---

### PL-005 — Char and Solid Residue Composition Uncharacterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Chemical Safety / Waste Management               |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-05-27                                       |

**Description:** Pyrolysis produces 5–20% solid char and ash residue by feedstock
mass. Char composition from mixed plastic feedstock is unknown — it may contain
concentrated heavy metals, carbon black, inorganic fillers, and residual halogenated
compounds.

**Why It Matters:** If char is treated as inert waste and disposed of without
characterization, hazardous materials may be released into the environment or
contaminate downstream processing streams. If char has carbon or mineral recovery
value, uncharacterized disposal wastes recoverable material.

**Resolution Path:** Characterize char composition from first operational reactor
run using available analytical methods — at minimum, visual inspection and
solubility testing. Cross-reference `Operations/Gate_02_Triage.md` for routing
to hazardous hold or material recovery as appropriate. Cross-reference
`Operations/Gate_03_Reduction.md` GR-003 (biological and chemical waste disposal
doctrine) for hazardous char disposition path. Payment via Specification once
char composition is characterized and a routing decision tree is defined.

---

### Resolution Log

- 2026-05-27: PL-002 — Scope expanded from pressure control only to include
  maintenance access and corrosion inspection requirements. Finding from Grok
  Skeptic/Auditor audit 2026-05-27.
- 2026-05-27: PL-004 — Resolution path expanded to include specific candidate
  triage methods (melt-flow index, density bath, Beilstein). Finding from Grok
  Skeptic/Auditor audit 2026-05-27.
- 2026-05-27: PL-005 — New entry. Char and solid residue handling gap identified
  in Grok Skeptic/Auditor audit 2026-05-27. Section D added to body.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary updated — `Architecture/Facilities.md` added for siting and
  hot-work zone requirements (PC-002); `Admin/Safety_Protocols.md` added for
  operator PPE and respiratory protection standards (PC-003). Both added to
  Integration Hooks.

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                                                      | Reconsider? |
|------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-27 | Direct syngas routing to Air Scrubber without combustion stage    | Air Scrubber is not a combustion device — routing unburned flammable gas into scrubbing liquid creates fire and explosion risk inside the scrubber | No — combustion stage upstream of scrubber inlet is permanent doctrine |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Pyrolysis reactor heated without logged oxygen purge completion
- Air Scrubber not operational or not verified before reactor heating begins
- Halogenated polymer triage rejection protocol bypassed or made optional
- Syngas routed directly to Air Scrubber without upstream combustion stage
- Char residue treated as inert and disposed of without characterization
- PL-001 triage protocol introduced without Beilstein test or equivalent
  halogen detection method
- Reactor fabricated without pressure relief system per PL-002
- Pyrolytic oil used in motor-generators without PL-003 characterization
- Mechanical repurposing path used for visibly degraded or unknown-identity polymer
  without PL-004 heuristic check
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.
  # Woodworking.md — Timber Sourcing, Processing & Fabrication

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Felling operations carry lethal risk from falling trees, barber-chair failures, and chainsaw kickback — never fell alone and always establish two escape routes before the first cut. Power tool operations produce blade ejection, kickback, and entanglement hazards that cause permanent injury in fractions of a second. Fine wood dust is explosive at sufficient airborne concentration and causes permanent respiratory damage from chronic exposure — source capture dust extraction is required at all power tool stations. Several common species (walnut, cedar, yew) produce toxic or sensitizing dust; mixed-species milling has uncharacterized synergistic exposure effects — see WW-004. PPE (eye, ear, respiratory) and machine guarding are non-negotiable prerequisites before any powered operation begins. When in doubt, shut down. The cost of a stopped run is always recoverable.

---

## File State
| Field | Value |
|---|---|
| Status | Draft |
| Body Stability | Volatile |
| Spec Gates | 0/6 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-30 (Gemini — Systems/Auditor); revised 2026-06-08           |
| Auditor | Gemini — Systems/Auditor |
| Open Unknowns | 5 |
| Active Disputes | 0 |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

## Scope Boundary
**This file DOES define:**
 * Timber sourcing hierarchy — salvage, urban, storm-fall, and standing tree.
 * Felling and chainsaw safety doctrine for small-scale operations.
 * Green wood handling, rough dimensioning, anisotropic behavior, and drying doctrine.
 * Structural deployment of woodgrain (utilizing natural fiber orientation as an asset).
 * Power tool and hand tool milling workflows for irregular salvage stock.
 * CNC/router fixturing methods for slabs and live-edge material.
 * Heat treatment and surface modification methods.
 * Joinery, adhesive selection, and assembly doctrine.
 * Finishing doctrine for indoor and outdoor applications.
 * Waste valorization hierarchy through to basic paper making.
 * Dust and species-specific hazard doctrine based on climate-zone variables.

**This file DOES NOT define:**
 * CNC toolpath generation, G-code, or CAM software workflows.
 * Full shop-wide dust extraction system design (→ `Operations/Air_Scrubber.md`).
 * Structural engineering calculations for load-bearing wooden members.
 * Commercial lumber grading standards or large-scale industrial forestry operations.
 * Facility siting, shop layout, and clearance zone requirements
   (→ `Architecture/Facilities.md` — FA-001).
 * Formal hearing conservation program and PPE sourcing standards
   (→ `Admin/Safety_Protocols.md`).

## File Purpose
This file governs the full processing chain for wood within the Lazarus Forge — from standing tree or salvage source through to finished functional or structural object. Its emphasis is on salvaged and urban timber, irregular and green stock, and low-to-high technology methods appropriate for a self-reliant fabrication environment across variable high-humidity environments.

Wood is an anisotropic, living material. Unlike metal or polymers, it cannot be treated as a uniform substrate. Premature milling of green stock, ignoring grain orientation, inadequate drying, improper fixturing of irregular slabs, and uncontrolled dust exposure are recurring failure modes that destroy material and injure operators. This file establishes a durable baseline from the first cut to the finished surface.

## Assumptions
| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Basic power tools and hand tools are available at v0 bootstrap | Typical fabrication shop context | Medium | Fully off-grid or remote deployment confirmed — tool availability reassessed |
| ASM-002 | Target biome features diverse hardwood/softwood distribution with high seasonal humidity | Global temperate/subtropical deployment assumption | High | Relocation to arid or arctic biomes |
| ASM-003 | Dust extraction and PPE are implemented per Operations/Air_Scrubber.md doctrine | Cross-module dependency | Medium | Independent shop air quality measurement validates or invalidates current approach |
| ASM-004 | Salvaged and urban timber is structurally usable after proper drying and defect assessment | Analogous — urban timber salvage practice | Low | WW-002 resolved — long-term performance of salvaged urban timber characterized |
| ASM-005 | Air drying schedules must scale dynamically based on local ambient relative humidity (RH) | Standard timber physics | High | WW-001 resolved — deployment-site validated drying metrics established |

---

## 1. Sourcing Hierarchy & Material Selection
Consistent with the *Salvage Before Reduction* principle, timber enters a sourcing priority sequence:
 1. **Salvaged urban and storm timber** — downed trees, demolition lumber, storm fall. Highest priority. Zero harvest cost, reduces waste stream.
 2. **Pallet and packaging wood** — widely available, often kiln-dried, usable for smaller stock. Inspect for heat treatment stamps (HT) vs. methyl bromide treatment (MB — **reject** for indoor use).
 3. **Standing tree harvest** — only when salvage sources are insufficient for the application. Requires felling doctrine.
 4. **Commercial lumber** — purchased per *purchase-what-cannot-be-produced* doctrine when salvage stock cannot meet dimensional or quality requirements.

**Ingrown Foreign Matter (IFM) Screening Protocol**

Salvaged urban and storm timber carries a high probability of containing embedded metal or stone (fences, spikes, wire, overgrown signage). Processing unverified salvage stock carries terminal risk to tooling and high kinetic hazard to the operator.

 * *Visual Triage:* Scan log surfaces for localized swelling, unnatural bark patterns, or metallic staining (iron tannin reactions manifest as deep blue/black streaks in oaks).
 * *Electromagnetic Screening:* Every piece of salvage timber must pass a dual-axis metal detector scan prior to hitting any powered blade (bandsaw, jointer, planer, or CNC). Flag and isolate any deep-signal zones. See WW-005.
 * *The "Bike-in-a-Tree" Rule:* If a log segment shows deep, unextractable structural contamination, it is immediately downgraded from fabrication feedstock and routed to high-clearance mechanical splitters for firewood, or bypassed directly to biochar reduction.

### Standard Functional Typologies (Biome-Agnostic)
Rather than limiting documentation to specific regional flora, timber is classified by structural archetype:
 * **High-Density Siliceous/Interlocked Hardwoods:** (e.g., White Oak equivalents, Hickory equivalents). Chosen for extreme shock resistance, tool handles, high-stress structural joints, and rot-resistant outdoor deployments.
 * **Highly Unstable/Tension-Prone Hardwoods:** (e.g., Sweetgum/Eucalyptus equivalents). Plentiful but prone to severe warping. Must be dried under extreme physical restraint and restricted to non-structural utilities.
 * **Resinous Softwoods:** (e.g., Pine/Fir equivalents). Rapid growth, highly accessible structural stock. Soft, easy to mill, but requires chemical or thermal stabilization for exterior ground-contact use.
 * **High-Tannin/Phenolic Woods:** (e.g., Cedar/Walnut equivalents). Excellent natural insect and rot resistance. Dust is universally a high-tier respiratory sensitizer.

## 2. Utilizing Woodgrain as an Asset (Anisotropic Engineering)
Wood is completely non-isotropic; its tensile, compressive, and shear strengths depend entirely on grain direction. Forge components must be engineered to exploit these mechanics rather than fighting them.

### Grain Alignment Rules
 * **The Tensile/Columnar Asset:** Wood fibers have massive tensile strength along the grain. Structural columns, levers, and handles must align the grain continuously along the axis of primary force.
 * **Avoiding Shear Splitting:** Wood splits effortlessly *parallel* to the grain. Never position fasteners or drill holes in a perfectly straight line along a single grain line, as this acts as a wedge, inducing a mechanical cleavage plane.
 * **Curvilinear Grain Tracking:** When fabricating curved functional parts (e.g., tool handles, structural brackets), do not cut a curved profile across flat, straight-grained wood. This creates dangerous "short grain" zones that fail instantly under minimal load. Seek out natural tree forks, crotches, or curved limbs where the wood fiber naturally grew in a curve, capturing continuous structural integrity.

### Managing Dynamic Moisture Movement
Wood moves perpetually across its life cycle, expanding and contracting as relative humidity changes.
 * **Tangential vs. Radial Shift:** Wood shrinks and expands roughly twice as much *tangential* to the growth rings as it does *radially*, and virtually not at all *longitudinally* (along the length).
 * **Design for Movement:** Joints must never restrict cross-grain movement. Gluing or hard-fastening a wide solid tabletop grain perpendicular to a rigid cross-brace will cause the wood to self-destruct, split, or cup drastically. Use slotted mechanical fasteners or floating joinery.

## 3. Felling and Chainsaw Doctrine
Felling is the highest-risk operation in this file. It is governed by a conservative doctrine regardless of tree size.

**Never fell alone.** A second person is required for any felling operation — not to assist with cutting, but to maintain a wider spatial awareness and call stop if conditions change unexpectedly.

**Pre-fell assessment:**
 * Identify the natural lean direction of the tree.
 * Identify two escape routes at 45° angles behind and away from the planned fall direction — clear these routes before the first cut.
 * Assess for widow-makers (dead branches overhead) — do not fell under them.
 * Assess for barber-chair risk: trees under tension, leaning trees, or trees with significant rot at the base can split vertically and kick the butt backward unpredictably. If barber-chair risk is present, do not fell without specialist assessment.
 * Check fall zone for people, structures, and utility lines.

**Cutting sequence:**
 1. Face cut (notch) on the fall side — depth 1/4 to 1/3 of trunk diameter, angle 60–70°. This controls the fall direction.
 2. Back cut on the opposite side — slightly above the bottom of the face cut. Leave a hinge of uncut wood. The hinge steers the fall.
 3. Do not cut through the hinge. A severed hinge loses directional control.
 4. When the tree begins to move, disengage the saw, set the brake, and move immediately along one of the pre-cleared escape routes — do not watch the tree fall.

**Chainsaw safety minimums:**
 * Cut-resistant chaps or chainsaw trousers.
 * Helmet with face shield and integrated hearing protection.
 * Steel-toe boots and high-dexterity gloves.
 * Chain brake functional and tested before each session.
 * Never operate a chainsaw above shoulder height.

**Limbing and bucking (sectioning the felled tree):**
 * Work from the trunk outward on limbs.
 * Assess tension and compression in each limb before cutting — a branch under compression will pinch the bar; a branch under tension will kick.
 * Buck (cross-cut) into manageable sections at the felling site before transport — moving whole logs is a separate injury risk.

## 4. Green Wood Handling and Drying
Green wood milled to final dimension will warp, check, and crack as it dries. The correct sequence is: **rough dimension → dry → final mill.**

**Rough dimensioning before drying:**
 * Crosscut to rough length (add 6–12 inches over final length for end checking).
 * Rip to rough width (add 1–2 inches over final width).
 * Do not plane or joint to final dimension while green.
 * End-seal all exposed end grain immediately after crosscutting — paint, wax, or commercial end-grain sealer. End grain dries 10–15× faster than face grain and is the primary checking site.

**Moisture content targets:**
 * Outdoor structural use: 15–19% MC acceptable.
 * Indoor furniture and electronics integration: 6–8% MC.
 * Measurement: Pin-type moisture meter minimum; pinless preferred for non-destructive checking of drying progress.

**Air drying stack doctrine:**
 * Stack on stickers (1-inch square spacers) at 12–16 inch intervals across the width.
 * Stickers must be aligned perfectly vertically across the stack — misaligned stickers introduce localized leverage points that cause permanent bowing.
 * Elevate the stack off the ground minimum 12 inches to clear ground moisture and maximize base airflow.
 * Cover the top only — sides must remain open for cross-ventilation.
 * Baseline calculation: 1 year per inch of thickness, adjusted dynamically via local equilibrium moisture content (EMC) tracking (see WW-001).
 * Tension-prone species: Dry under physical restraint (heavy weights or ratcheted straps over the top of the stack) to limit twist.

**Accelerated drying options:**
 * Solar kiln: Simple construction, greenhouse-effect air cycling, significant time reduction, suitable for v0 bootstrap.
 * Dehumidifier kiln: Closed insulation loop, requires dedicated power draw.
 * Do not accelerate drying beyond the wood's specific fiber saturation threshold — surface checking and case-hardening (dry shell trapping a wet core) both result from premature ambient relative humidity drops.

## 5. Milling — Hand Tools, Power Tools, and CNC

⚠️ **Pre-Milling Gatekeeper: Hard Inclusions**
Prior to the first face pass on a jointer or resaw on a bandsaw, verify the piece has cleared the IFM Screening Protocol. Hitting embedded steel or stone with high-speed tool steel or carbide cutters induces instantaneous tool fracturing, projectile ejection, and severe machine damage.

### Hand Tools
Hand tools are the baseline capability — they function without power, develop operator material sense, and handle operations that power tools cannot safely perform on irregular stock.
 * *Core kit minimum:* hand saw, jack plane, smoothing plane, chisels (1/4", 1/2", 3/4", 1"), marking gauge, combination square, mallet.
 * Hand tools are primary for final fitting of joinery, working with short or awkward pieces that cannot be safely fed through power tools, and finishing surfaces where power tool tearout is structurally unacceptable.

### Power Tool Milling Sequence
For converting rough stock to dimensioned lumber:
 1. **Jointer** — flatten one face (reference face).
 2. **Planer** — flatten opposite face parallel to reference face; establish thickness.
 3. **Tablesaw or bandsaw** — rip to width with reference face against fence.
 4. **Crosscut saw or miter saw** — cut to final length.

**Irregular and live-edge stock:**
Salvage timber frequently arrives without a flat reference face. The jointer cannot safely process highly cupped, bowed, or live-edge stock without a sled.
 * *Router sled method:* Build a flat track wider than the workpiece; secure the workpiece to the track base with wedges/hot glue in waste areas; run the router across the surface to establish a reference plane; flip and joint or plane the opposite face.
 * *Bandsaw sled method:* Secure the workpiece to a flat sled; resaw to establish one flat face; proceed to planer.

### CNC and Router Fixturing for Slabs and Irregular Stock
CNC routing of salvage slabs represents a significant work-holding problem. Irregular geometry, variable thickness, and live edges work against standard hold-down methods.

**Vacuum fixturing:**
 * Effective for flat or near-flat stock with sufficient surface area.
 * Requires a vacuum pump and spoilboard with vacuum channels or gasket grids.
 * Minimum surface area for reliable hold: approximately 50% of spoilboard coverage with the workpiece — irregular slabs with large voids or live edges may not achieve sufficient contact.
 * Test hold before running: attempt to physically shift the workpiece by hand before beginning the cut cycle.

**Mechanical fixturing for slabs:**
 * Sacrifice screws driven directly into waste areas outside the finished boundary — most reliable method for highly irregular stock.
 * Locate screw positions digitally before generating toolpaths — screws must not intercept the path of any tool bit.
 * Toggle clamps or cam clamps at the perimeter where geometry allows.
 * Wedge packs under low corners to prevent workpiece rocking before clamping down.

**Surfacing irregular slabs (flattening):**
 * First pass: Large-diameter surfacing bit (spoilboard cutter or fly cutter), shallow passes (1–2mm), to establish a reference plane across the full slab.
 * Do not attempt to surface in a single deep pass — deflection and chatter increase with depth, and slab rocking under cut load is a real risk.
 * After first-face surfacing, flip and surface the second face parallel — this requires either a reference surface on the spoilboard or a thickness gauge to set the second-face pass depth.

**Tooling for wood CNC:**
 * *Upcut spiral:* Good chip evacuation, but pulls fibers upward — tearout on top surface of through-cuts.
 * *Downcut spiral:* Pushes fibers down — cleaner top surface, poorer chip evacuation, high heat buildup in deep slots.
 * *Compression spiral:* Upcut geometry at tip, downcut above — clean top and bottom surfaces, best for sheet goods and shallow-profile work.
 * *For live-edge preservation:* Climb-cutting the edge profile reduces tearout on irregular grain at the boundary — use with caution, requires a rigid hold-down.

**Probing irregular surfaces:**
Where CNC controller supports it, touch-probe the slab surface at a grid of points before running 3D toolpaths — this maps the actual surface topology and compensates for residual bow or twist not fully removed by surfacing. Manual shimming is the v0 alternative: shim the slab flat to the spoilboard before fixturing, verify with straightedge.

## 6. Heat Treatment and Surface Modification
 * **Steam bending:** Softens lignin for curves; requires a simple steam box and bending forms. Species matters — straight-grained green stock bends best; kiln-dried stock is brittle.
 * **Shou Sugi Ban (charred finish):** Torch char the surface to a consistent depth; wire brush to remove loose char; oil finish seals. Provides genuine weather and insect resistance. Depth of char controls durability vs. aesthetics.
 * **Oven stabilization:** Low-temperature oven treatment (90–120°C) drives residual moisture and can produce color change in some species. Not a substitute for proper drying — a wet core will still move after oven treatment.

## 7. Joinery and Assembly
**Traditional joinery** (mortise and tenon, dovetail, lap joint) requires no consumables and produces strong, repairable joints. Skill-dependent but tool-minimal.

**Modern joinery** (pocket screws, biscuits, domino loose tenons) is faster and more forgiving of minor dimensional variation — appropriate for utility work and jigs.

**CNC-cut joinery:** Finger joints, box joints, and custom mortise and tenon profiles are well-suited to CNC. Generates consistent, repeatable joints from variable stock.

**Adhesive selection:**
 * *PVA (wood glue):* Standard for indoor work, excellent strength, water cleanup.
 * *Epoxy:* Gap-filling, bonds dissimilar materials, waterproof — use for irregular fits, voids, and outdoor joinery.
 * *Polyurethane:* Expands slightly during cure (gap-filling), waterproof, bonds to slightly damp surfaces — useful for green or partially dried stock.

## 8. Finishing
**Surface preparation:**
 * Sand through grits — do not skip grits. Typical progression: 80 → 120 → 150 → 180 → 220.
 * Sand with the grain on final passes — cross-grain scratches telegraph through finish.
 * Raise the grain with a damp cloth after 150 grit on water-based finishes; sand lightly at 220 after drying to remove raised fibers.

**Finish selection:**
| Application | Recommended Finish | Notes |
|---|---|---|
| Indoor furniture | Tung oil, danish oil, hardwax oil | Penetrating — easy repair, low build |
| Indoor structural | Varnish, polyurethane | Film finish — durable, harder to repair |
| Outdoor | Marine varnish, teak oil + UV protectant | UV inhibitors critical under raw sunlight exposure |
| Highly porous/punky wood | Epoxy stabilization first, then topcoat | Consolidates weak fiber before finishing |
| Charred (Shou Sugi Ban) | Linseed or tung oil seal | Seals char; enhances weather resistance |

## 9. Waste Valorization
Wood waste follows a hierarchy consistent with Salvage Before Reduction doctrine:
 1. **Usable offcuts** — route to component storage; minimum useful size is application-dependent but a 12-inch square is a reasonable v0 threshold.
 2. **Chips and shavings** — animal bedding, garden mulch, compost amendment, smoking/BBQ fuel (species-appropriate).
 3. **Firewood** — larger offcuts and poor-quality material not suitable for fabrication.
 4. **Biochar** — controlled incomplete combustion produces biochar for soil amendment; cross-reference Operations/Energy.md for integration with biogas and thermal systems.
 5. **Mushroom substrate** — hardwood chips and sawdust support oyster and shiitake cultivation; low-cost, high-value output.
 6. **Paper pulp** — retting and beating cellulose fiber into sheet form; viable for low-volume applications from clean softwood fiber.

## 10. Dust and Species Hazard Doctrine
Wood dust is a respiratory hazard, a carcinogen at chronic exposure levels for certain species, and an explosion risk at sufficient airborne concentration. This is not optional PPE territory.

**Minimum PPE for all powered wood operations:**
 * *Dust mask:* N95 minimum for general operations; P100 half-face respirator for known sensitizers (walnut, cedar, exotic species).
 * *Eye protection:* Safety glasses minimum; face shield for lathe and routing.
 * *Hearing protection:* Foam plugs or earmuffs for all sustained power tool use.

**Source capture dust collection:**
 * Dust collector connected at the tool is more effective than ambient air filtration alone — capture at the source before dust becomes airborne.
 * *Minimum:* Shop vac with HEPA filter at hand tools and router; dedicated dust collector at tablesaw, planer, and jointer.
 * Cross-reference Operations/Air_Scrubber.md for system-level air management.

**Species-specific hazards:**
| Species Class | Hazard | Additional PPE |
|---|---|---|
| High-Tannin Walnut Typologies | Juglone sensitizer; respiratory | P100 respirator |
| Resinous Cedar Typologies | Respiratory irritant, sensitizer | P100 respirator |
| Toxic Alkaloid Typologies | Toxic (e.g., taxine alkaloids) | P100; avoid skin contact |
| Unknown salvage | Unknown profile | P100 until species confirmed |

**Dust explosion risk:**
Fine wood dust suspended in air is explosive. Do not allow dust to accumulate on surfaces — a sudden disturbance that raises accumulated dust into a cloud creates an immediate ignition risk. Empty dust collectors regularly. No open flames or ignition sources in dust-generating areas. Cross-reference WW-004 for mixed-species exposure threshold unknowns.

## Integration Hooks
 * `Operations/Air_Scrubber.md` — dust extraction system design, toxic species off-gas management, source capture integration.
 * `Operations/Gate_02_Triage.md` — salvage timber condition assessment follows triage logic; defect classification and routing to fabrication vs. firewood.
 * `Operations/Gate_03_Reduction.md` — low-value wood waste that cannot be repurposed follows Reduction doctrine to biochar or compost.
 * `Operations/Gate_06_Fabrication.md` — wood is a fabrication feedstock; fixturing, joinery, and finishing doctrine connects to fabrication workflow.
 * `Operations/Energy.md` — biochar and wood gas (gasification) are candidate energy inputs; firewood and offcuts feed thermal systems.
 * `Admin/Trajectories.md` — gasification of wood waste as an energy source, large-scale timber processing, and structural engineering calculations are v1+ scope items.
 * `Architecture/Facilities.md` — shop siting, floor loading for heavy log stock, clearance zones for power tool operation (FA-001).
 * `Admin/Safety_Protocols.md` — hearing conservation program; PPE sourcing standards for sustained power tool and chainsaw operations.

## Lessons Learned
| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| 2026-05-29 | Anecdotal | Immediate final milling of green stock | Severe warping and cracking after milling to dimension | Always rough dimension first, then dry to target MC, then final mill. Green stock milled to final dimension will move. | Anecdotal | Yes — validate drying schedule against local species per WW-001 |

## Active Disputes
| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### WW-001 — Ambient-relative humidity drying schedules not quantified

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Precise air-drying and kiln schedules for common local species under variable microclimate humidity conditions have not been validated. The one-year-per-inch rule of thumb is a generic analog estimate, not a locally measured figure.

**Why It Matters:** Improper drying leads to high material loss through checking, warping, and case-hardening. Underdried stock in joinery causes joint failure as the wood continues to move in service.

**Resolution Path:** Compile regional baseline forestry/extension data relative to the deployment node's climate envelope; cross-reference USDA Forest Products Laboratory drying schedules. Validate against first operational drying stack with moisture meter tracking.

---

### WW-002 — Long-term performance of salvaged urban timber uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Durability differences between urban salvaged timber and forest-grown timber are not characterized. Urban trees grow under different stress conditions — pollutant uptake, asymmetric wind stresses, soil compaction — that may affect structural performance and finishing behavior.

**Why It Matters:** Routing urban salvage to structural applications without understanding its performance profile introduces an uncharacterized failure mode in load-bearing assemblies.

**Resolution Path:** Survey available literature on urban timber structural performance. Flag salvaged urban timber as Analogous confidence for structural use until local destructive/non-destructive testing data exists.

---

### WW-003 — CNC fixturing best practices for live-edge slabs not validated

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Section 5 provides fixturing guidance for irregular slabs but the methods have not been validated against actual live-edge slab operations. Vacuum hold performance on high-void slabs is particularly uncertain.

**Why It Matters:** Workpiece movement during CNC routing damages tooling, destroys the workpiece, and creates a projectile hazard at spindle speeds.

**Resolution Path:** Validate vacuum fixture hold-down force against representative slab geometries during first operational CNC cycle. Document actual minimum surface area requirements for reliable vacuum hold.

---

### WW-004 — Dust toxicity thresholds for mixed-species milling uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical / Safety |
| Blocking | Yes (for sustained mixed-species operations without P100 respirator) |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Precise exposure limits and synergistic effects when milling mixed local species simultaneously are not characterized. Sensitizer species mixed with inert species may produce combined exposures that exceed single-species thresholds at lower individual concentrations.

**Why It Matters:** Chronic wood dust exposure causes occupational asthma, nasal cancer, and sensitization reactions that can become debilitating. Mixed exposure profiles are harder to evaluate than single-species profiles.

**Resolution Path:** Until WW-004 is resolved, treat all mixed-species milling as requiring P100 half-face respirator minimum — do not rely on N95 alone. Cross-reference Operations/Air_Scrubber.md for source capture requirements.

---

### WW-005 — NDT standards for IFM detection not validated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical / Safety |
| Blocking | Yes (for processing raw urban salvage through powered machinery) |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-30 |
| Last Reviewed | 2026-05-30 |

**Description:** The precise workflow and hardware sensitivity requirements for detecting deeply embedded ferrous and non-ferrous objects within dense hardwood logs have not been calibrated for the v0 shop environment.

**Why It Matters:** Undetected metal striking high-speed cutting machinery creates an immediate operator shrapnel hazard and can cause catastrophic failure of bootstrap tooling that cannot be easily fabricated or replaced.

**Resolution Path:** Source or fabricate a reliable deep-penetration wand metal detector. Establish a clear Scan-and-Mark workflow for all incoming urban salvage logs. Validate detection depth limits using a known control sample (e.g., a 16d nail driven into a test block at varying depths). Payment via Specification once detection workflow is validated and minimum detection depth is characterized.

---

### Resolution Log

- 2026-06-08: Navigation Anchors block added. Safety Advisory
  formatting corrected — horizontal rule added after advisory,
  stray `>` removed. Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates_LF.md`
  (PC-001). Scope Boundary updated — `Architecture/Facilities.md`
  added for shop siting and clearance zones (PC-002);
  `Admin/Safety_Protocols.md` added for hearing conservation
  program and PPE sourcing standards (PC-003). Integration Hooks
  updated to canonical backtick paths; Facilities.md and
  Safety_Protocols.md added.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet | —    |

---

## Drift Indicators
Mandatory re-audit conditions for this document:

| Trigger | Reason |
|---|---|
| WW-004 remains unresolved and N95 masks used for mixed-species milling | Blocking unknown — P100 is the minimum until characterization is complete |
| WW-005 remains unresolved and urban salvage processed through powered machinery without electromagnetic screening | Blocking unknown — IFM screening is mandatory before any powered cut on salvage stock |
| Felling operations conducted without a second person present | Permanently required — never fell alone is non-negotiable doctrine |
| Green stock milled to final dimension without drying to target MC | Permanently abandoned path — always rough dimension, dry, then final mill |
| CNC operations begun without fixturing hold-down verified by hand | Workpiece movement at spindle speed is a projectile hazard — verify before running |
| Urban salvage timber used in structural applications before WW-002 is resolved | Uncharacterized structural performance — flag as Analogous confidence at minimum |
| Dust collector bypassed or disconnected at any power tool station | Source capture dust collection is non-negotiable — not an optional convenience |
| Geographic proper nouns or localized tracking vectors injected | Violates biome-agnostic system intent and breaches operational opacity guardrails |
| Structural design cuts elements directly across natural curved fibers | Short-grain structural vulnerability — forces curved components into failure |
| Ethical Anchor field absent, altered, or does not match canonical string | Load-bearing integrity requirement — applies to all files |

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.
