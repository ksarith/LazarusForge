# Air_Scrubber.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

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
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-31                                                          |
| Auditor          | Gemini                                                              |
| Open Unknowns    | 5                                                                   |
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
| **Fire Event — Hot Zone** *(added 2026-08-15, applying `Admin/Resolution_Methodology.md`)* | Method-agnostic trigger input — automatic detection hardware not yet specified; manual pull-station/operator call is the minimum viable trigger and is not equipment-gated | Any fire event confirmed in `Architecture/Facilities.md`'s Hot Zone | Forced ventilation halts immediately as part of the response, not after — negative-pressure airflow feeds a fire rather than suppressing it, so delayed shutdown actively works against suppression. Reuses this table's own Fault-latency convention rather than a separate response class. |

**Note on the Fire Event row, 2026-08-15:** `Operations/Gate_06_Fabrication.md` GF-007 named this gap but could not close it alone — the actual shutdown mechanism (halting forced ventilation) is this file's own system, so the interlock logic belongs in this table alongside the other five, not duplicated in GF-007. What stays genuinely open: the *detection* half. No automatic fire/smoke detection hardware is specified anywhere in the repository — this row deliberately keeps the trigger input method-agnostic (manual call is sufficient to exercise the interlock logic) rather than inventing a sensor specification that would itself need physical validation this session cannot produce. Automatic detection hardware selection is a separate, still-open item, not silently assumed solved by this row's existence.

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
`Admin/Verification_Gates.md`.

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
   `Admin/Verification_Gates.md` log tracking
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
| Last Reviewed | 2026-08-15                                       |

**Description:** Whether 500W worst-case scrubber
draw (surface/shallow variants) is compatible with
Forge power budget at bootstrap and nominal modes.
Thermal sink power is not yet validated in this loop.

*Grok review 2026-08-15: Resolution Path adequate; Energy.md cross-ref real. No closure.*

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
| Last Reviewed | 2026-08-15                                       |

**Description:** Detailed specification for deep-sea
Variant 4+ (greater than 50m / 5 atm) remains
undefined.

*Grok review 2026-08-15: Correctly discharged to Trajectories.md; Leviathan cross-ref real. In Progress / Minor appropriate. No closure.*

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
| Last Reviewed | 2026-08-15                                       |

**Description:** Saturation thresholds have been
bound to a multi-point differential diagnostic grid
(PID VOC, ΔP, and Sump pH). Real-world chemical
baseline data is now required to clamp the
operational float margins.

*Grok review 2026-08-15: Resolution Path sound; Blocking Yes correctly retained (Chemistry validation dependency). No closure.*

**Note, 2026-08-15 (Claude, cross-referenced from `Operations/Gate_01_Intake.md` GI-002):** GI-002's compressed-gas discharge doctrine calls for routing suspected-hazardous unknown-content vessel releases through scrubber intake, but this file currently only specifies handling for its own designed process streams (pyrolysis gas, Cl₂ via the chlor-alkali path) — there is no general unknown-content gas intake path. Registered as **AS-005** below rather than folded into this entry's scope, since AS-003 is about calibrating a known stream and AS-005 is about the absence of any path for an unknown one.

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
| Blocking      | Yes — blocks Protocol 1.4 fault-alarm audibility calibration |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-05-23                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Continuous fan and compressor noise
levels during Air Scrubber operation have not been
empirically characterized. `Admin/Safety_Protocols.md`
addresses general hearing conservation doctrine and
PPE requirements, but no site-specific SPL survey
or formal hearing conservation program for Air
Scrubber operations exists.

*Grok review 2026-08-15: Blocking Yes correctly retained (Protocol 1.4 dependency). Safety_Protocols.md cross-ref real. No closure.*

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

### AS-005 — No intake path defined for discrete unknown-content releases (non-process-stream sources)

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                              |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No — does not block Gate 4 harness or existing process-stream operation |
| Owner         | Operations/Air_Scrubber.md                       |
| First Logged  | 2026-08-15                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The Stage A→E architecture is built around one
continuous process gas stream (pyrolysis outgassing, Cl₂ off-gas from
the chlor-alkali path). Every stage assumes that stream's properties —
Stage A intercepts coarse process particulates, Stage C thermally
quenches hot pyrolysis gas specifically. There is no defined path for
a discrete, ambient-temperature, unknown-content gas release from a
different subsystem entirely — specifically, `Gate_01_Intake.md`
GI-002's compressed-gas discharge doctrine, which calls for routing
suspected-hazardous vessel releases "through scrubber intake" without
this file having ever specified what that means mechanically.

**Why It Matters:** Two bad options exist if this stays undefined.
Forcing an occasional unknown-content release through the full A→E
pipeline wastes Stage A/C capacity on a stream they weren't designed
for and, more seriously, risks introducing unidentified chemistry into
Stage D's recirculating water loop — the same loop AS-003 is already
trying to calibrate against known process chemistry. An unlogged
contaminant there could silently invalidate that calibration. The
alternative failure — operators simply venting an unknown gas because
no defined path exists — is the exact hazard GI-002 exists to prevent.

**Resolution Path:**
- Define a physically separate auxiliary release point — not a tap
  into the main A→E pipeline — using the same generic broad-spectrum
  capture approach already established as this file's own v0 baseline
  (Variant 1, aerated pond-style bubbler): simple, robust, inspectable,
  and chemically isolated from Stage D's calibrated main loop.
- Sizing depends on GI-002's own still-open vessel-volume assumptions
  (largest plausible compressed-gas vessel expected at Intake) —
  correctly deferred to GI-002 rather than guessed here.
- Once a release passes through the auxiliary point, its water/media
  becomes a separate managed-waste stream under this file's existing
  "Waste as a Managed Output" doctrine, not merged into Stage D's
  output stream.
- Cross-reference: `Operations/Gate_01_Intake.md` GI-002 (source of
  the releases this path serves); `Operations/Air_Scrubber.md` AS-003
  (the calibration this path is designed to avoid contaminating).
- Payment via Specification — once the auxiliary path's capture media
  and capacity are sized against GI-002's vessel-volume assumptions,
  move to Functional Architecture as Analogous.

**Claude review 2026-08-15:** Surfaced during GI-002's spec-depth pass
(`Operations/Gate_01_Intake.md`) — GI-002's discharge doctrine assumed
scrubber routing existed without this file ever having specified it.
Registered as its own ID rather than folded into AS-003, since the
two are architecturally distinct: AS-003 is calibration of a known,
continuous, designed-for stream; this is the absence of any path for
an unpredictable, discrete, unknown one. Deliberately does not size
the auxiliary unit — that number depends on GI-002's vessel-volume
assumptions, which are themselves still open, so guessing a capacity
here would be inventing a number to fill a gap rather than reflecting
what's actually known. Not Blocking — existing process-stream
operation and the Gate 4 harness are unaffected by this gap.

---

### Resolution Log

- 2026-08-15 (third entry, same day): **Fire Event — Hot Zone interlock row
  added — second applied case of `Admin/Resolution_Methodology.md`.**
  `Operations/Gate_06_Fabrication.md` GF-007 named the ventilation/fire
  interlock gap but couldn't close it alone, since the actual shutdown
  mechanism (halting forced ventilation) is this file's own system. Reused
  this table's existing five-row fault-interlock pattern rather than
  inventing a separate response class. Deliberately kept the trigger input
  method-agnostic — no automatic fire/smoke detection hardware is specified
  anywhere in the repository, so a manual pull-station/operator call is the
  documented minimum viable trigger, not an assumed sensor that would itself
  need physical validation. Automatic detection hardware selection remains a
  separate, still-open item. No new unknown ID registered — this closes a
  cross-file gap between two existing unknowns (GF-007, and this file's own
  fault-matrix completeness), not a new one. Human-directed.

- 2026-08-15 (second entry, same day): **AS-005 registered — auxiliary
  intake path for discrete unknown-content gas releases, closing the
  Air_Scrubber gap surfaced during GI-002's spec-depth pass.** GI-002
  (`Operations/Gate_01_Intake.md`) assumed a "scrubber intake" routing
  for suspected-hazardous compressed-gas releases that this file had
  never actually specified — the Stage A→E pipeline is architected for
  one continuous process stream (pyrolysis gas, Cl₂ off-gas), not a
  discrete unpredictable release from a different subsystem. Registered
  as its own unknown rather than folded into AS-003, since AS-003 is
  calibration of a known stream and this is the absence of any path for
  an unknown one — architecturally distinct problems. Resolution Path
  defines a physically separate auxiliary release point reusing the
  file's own Variant 1 baseline approach, chemically isolated from
  Stage D's calibrated main loop so an unknown release can't silently
  invalidate AS-003's calibration work. Deliberately does not size the
  auxiliary unit — that depends on GI-002's still-open vessel-volume
  assumption, correctly left for GI-002 to define, not guessed here.
  Open Unknowns count updated 4 → 5. Not Blocking — existing
  process-stream operation and the Gate 4 harness are unaffected.
  Cross-links added at GI-002 pointing to AS-005. Human-directed.

- 2026-08-15: **Grok review round (alphabetical continuation — Air_Scrubber.md).** All 4 AS unknowns (AS-001–004) reviewed. Last Reviewed bumped; review markers added. Cross-refs (Energy.md, Leviathan_testing.md, Trajectories.md, Chemistry validation dependency, Safety_Protocols.md) verified real. AS-003 and AS-004 Blocking Yes correctly retained. Zero closures, zero Blocking flips, zero Priority changes. Spec Gates left locked. Human-directed.

- 2026-08-10: **AS-004 Blocking No → Yes (follow-up).** File’s own Why It
  Matters states this unknown “blocks that calibration step” (Protocol 1.4
  fault-alarm audibility). Same documentation-consistency pattern as
  TS-002 / EL-005 / GI-002. Applied after Claude review confirmed the
  understatement. Spec Gates still locked; no AS-* closed. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 3/6. (1) Open Unknowns **4** = AS-001–004, matches local
  sidecar and `Unknowns.md`. (2) AS-003 correctly **Blocking Yes** (blocks
  Chemistry validation). (3) AS-004 initially logged for human review; later
  same-day follow-up flipped Blocking No → Yes (see entry above). (4) No
  AS-* closed. Human-directed.

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
  Verification Ref corrected from `Verification_Gates.md`
  to `Admin/Verification_Gates.md` (PC-001).
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
