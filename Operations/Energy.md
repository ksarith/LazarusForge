# Energy.md — Energy Strategy & Governance

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Salvaged electrochemical batteries with unknown state-of-health present catastrophic thermal runaway and toxic hydrofluoric acid outgassing risks. Containment and isolation protocols are mandatory before any salvaged battery bank is commissioned (EV-003). Do not install salvaged storage in unventilated or uninsulated enclosures. Air Scrubber operation is strictly required during any battery handling, charging, or thermal failure event. **When in doubt, isolate the battery bank and do not proceed.**
>
> Multi-source operation (grid + motor-generators + biogas + solar + thermal recovery) introduces voltage, frequency, and ripple instability risks. The Energy Arbitration Layer (EAL) and Source Stability & Harmonization Layer are proposed doctrine, drafted 2026-08-01 and not yet audited — treat as a candidate architectural model, not a validated safety mechanism, until it clears Gate 1.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                                |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-09 — Grok pseudo-audit (Skeptic read + minimal Synthesizer fixes); prior: 2026-08-02 dual-audit adjudication; EGL body still not Gate-1 cleared |
| Auditor          | Gemini (2026-05-31); Grok EGL draft (2026-08-01); Gemini+Grok dual-audit (2026-08-02); Grok pseudo-audit (2026-08-09) — no Spec Gate promotion |
| Open Unknowns    | 5                                                                   |
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
- The canonical meaning of Spec Gates 1–6 (→ `Admin/Verification_Gates.md` — this file does not redefine what a gate is)

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
| Logic / Watchdog  | < 15 W baseline             | ±1% [Placeholder]        | Isolated Lead-Acid/Lithium Buffer (TEG contributes only if a thermal process is concurrently active — see EV-005; not assumable at idle) | Maintain state indefinitely; keep-alive telemetry |
| Mechanical Milling| 1.5 kW peak                 | ±5% [Placeholder]        | Hydro-Engine / Main Battery (SoH > 70%)     | Cycle spindle 50%; halt axis steppers            |
| Nominal           | 15–40 kW                    | ±5% [Placeholder]        | Grid / Scaled Generators + Air Scrubber     | Throttle feed rates; pause secondary axes        |
| Thermal Melt (G5) | 8.0 kW burst                | ±10% [Placeholder]       | Direct Generator / Biomass Syngas Loop      | Safety clamp; dump molten charge to safe crucible|

*Note: "G5" above refers to `Operations/Gate_05_Separation_Thermal.md`, not Spec Gate 5 (Cross-Reference Integrity) in `Admin/Verification_Gates.md`. Retained from the original table; flagging to prevent conflation between the two G5 usages.*

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
| G₅ | Thermal Recovery (TEG)   | \(P_{\text{thermal}}(t) = \eta_{\text{TEG}} \cdot Q_{\text{waste}}(t)\) | \(\eta_{\text{TEG}} \approx 3\text{–}7\%\); opportunistic offset during active high-temperature thermal processes only — zero during idle/cold-start, see EV-005 |

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
- **Safe Maintenance Access (proposed, gap flagged 2026-08-02):** Battery modules must be testable/serviceable without dropping the P₁ Logic/Watchdog rail — isolate the pack under test via a dedicated maintenance disconnect that never shares a bus with the baseline rails, so a fault during servicing can't cascade into a P₁ brownout.
- **End-of-Life / Disposal Routing (proposed, gap flagged 2026-08-02):** Class C packs (SoH < 50% or unknown, material recovery only) route to `Operations/Gate_02_Triage.md` for disposition and, once discharged/inert, to `Challenges/Waste.md` for final handling. Not yet specified: the discharge-to-safe-storage-voltage procedure prior to handoff.

*The Physical Isolation, Over-Extraction Guard, and Scrubber Prerequisite rules above are the original, audited EV-003 doctrine (2026-05-31) and remain load-bearing. The SoH Classification, Buffer Sizing, Degradation Tracking, Safe Maintenance Access, and End-of-Life Disposal Routing items are new proposed extensions, not yet audited.*

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
- Strong empirical or prototype success → migrate detailed implementation to **`Architecture/Engineering.md`** (pragmatic fabrication focus).
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
| Blocking      | Yes — blocks v1 operating cost model and `Admin/Economics.md` ECN-002 |
| Owner         | `Operations/Energy.md`                                                |
| First Logged  | 2026-05-27                                                            |
| Last Reviewed | 2026-08-09                                                            |

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

### EV-004 — Energy Arbitration Layer (EAL) hardware watchdog and firmware isolation unvalidated

| Field         | Value                                                               |
|---------------|-----------------------------------------------------------------------|
| Status        | Open                                                                  |
| Risk          | High                                                                  |
| Priority      | Major                                                                 |
| Type          | Technical / Governance                                                |
| Blocking      | Yes — before autonomous multi-source power distribution commissioning |
| Owner         | `Operations/Energy.md`                                                |
| First Logged  | 2026-08-02                                                            |
| Last Reviewed | 2026-08-02                                                            |

**Description:** ASM-006 assumes discrete/minimal-firmware controllers can implement EAL priority logic (P₁ > P₂ > P₃ > P₄, "no software overrides") without introducing new programmable attack surface. That assumption is tracked at the Assumptions-table level but had no corresponding tracked unknown for the hardware realization and adversarial firmware-compromise resistance of the mechanism itself.

**Why It Matters:** The EAL's central claim — that safety-rail priority can't be software-bypassed — rests entirely on this unvalidated hardware isolation. If it turns out to require more than discrete logic, ASM-006 fails and the EAL's core guarantee needs rework.

**Resolution Path:** Prototype the EAL priority watchdog using discrete analog/logic circuits or minimal verified firmware per `Operations/Electronics.md` EL-006's Logic-Zero wipe doctrine. Validate hard-wire cutoff under simulated software corruption before any EAL hardware is trusted with real P₁ rails. Payment via Specification once a prototype passes adversarial testing.

---

### EV-005 — Thermoelectric Generator (TEG) net energy harvesting threshold uncharacterized

| Field         | Value                                            |
|---------------|-----------------------------------------------------|
| Status        | Open                                                 |
| Risk          | Low                                                  |
| Priority      | Minor                                                |
| Type          | Technical                                            |
| Blocking      | No                                                    |
| Owner         | `Operations/Energy.md`                                |
| First Logged  | 2026-08-02                                            |
| Last Reviewed | 2026-08-02                                            |

**Description:** TEG conversion efficiency is low (η_TEG ≈ 3–7%). Section V models `R_thermal(t) = η_TEG · Q_waste(t)` as generation without a paired, explicit net-positive check against the coolant pump and radiator fan draw (`P_pump + P_fan`) that recovery itself requires — those parasitic terms exist in the Demand Model's `P_thermal(t)`, but nothing currently confirms recovery is worth its own overhead at low delta-T, and the Source Classes table previously (and incorrectly) implied TEG could supply idle-state baseline load with no active thermal process running at all — corrected 2026-08-02, see Resolution Log.

**Why It Matters:** Below some delta-T, running coolant pumps to chase TEG recovery could be a net energy loss, not a gain — the opposite of what "thermal recovery" is for.

**Resolution Path:** Measure parasitic pump/fan draw against TEG electrical output across realistic temperature gradients during `Operations/Gate_05_Separation_Thermal.md` thermal separation tests. Define `P_5,net(t) = R_thermal(t) - (P_pump(t) + P_fan(t))` explicitly and add an automated pump/fan shutoff when `P_5,net(t) ≤ 0`. Payment via Specification once measured across a representative operating range.

---

### Resolution Log

- 2026-08-09: **Pseudo-audit (Grok — Skeptic/Auditor read + minimal Synthesizer fixes only; human-directed pilot).** Role limits: no Spec Gate promotion, no physical-unknown closure, no self-approval. **Corrections applied:** (1) EV-001 Blocking cross-ref `EC-002` → `ECN-002` (Economics ID namespace rename; confirmed against `Admin/Economics.md` and `Unknowns.md`); (2) Safety Advisory "drafted this session" → "drafted 2026-08-01" (session-relative language had gone stale). **Findings logged, not closed:** F-EN-001 — Spec Gates remains 1/6 with historical justification in 2026-08-02 log, but no independent current Gate 1 evidence package for the pre-EGL core is restated in-file; not demoted to 0/6 (that would also be a claim without dual-auditor Gate work). F-EN-002 — Unknowns.md Active Index still shows EV-001 Priority column as "Blocking" while this file's sidecar correctly separates Priority: Major and Blocking: Yes — index vocabulary overload, systemic, not unique to this file. F-EN-003 — EGL / EAL / Source Stability remain proposed/unaudited; EV-004/EV-005 correctly open. **Verified intact:** Open Unknowns count 5 matches EV-001–005; Air_Scrubber Variant 0 positive-pressure cross-ref valid against `Operations/Air_Scrubber.md`; EV-003 safety advisory and Scrubber Prerequisite still load-bearing; no `Verification_Gates_LF` residue. Spec Gates **unchanged** at 1/6. Status **unchanged** Draft.

- 2026-05-27: EV-001–003 logged and structured.
- 2026-05-31: Spec Gate 1 baseline; Tar Minimization and 35°C/22% interlocks integrated; EV-001 bound to hardware envelope table; EV-003 physical isolation codified.
- 2026-06-08: Navigation Anchors and Verification Ref corrected; sidecar format normalized.
- 2026-07-12: Abandoned Paths / Drift Indicators reordered per template.
- 2026-08-01: Grok drafted a full Energy Governance Layer expansion (Demand + Generation + EAL + TIA), a Storage Model expansion of EV-003, and an Energy Capability Trajectory, claiming Spec Gates advanced to 2/6 and File Status → Transitional.
- 2026-08-02: **Corrective merge, human-directed.** Verified the 2026-08-01 draft against source and against `Admin/Verification_Gates.md`/`Admin/File_Template.md` before integrating. Merged in: EGL (Demand/Generation/EAL/TIA), Storage Model SoH classing, Source Stability & Harmonization, Energy Capability Trajectory — all explicitly marked **proposed / not yet audited**, distinct from the original 2026-05-31 audited body. Cut/corrected: (1) `Status` and `Body Stability` fields reverted to valid `Admin/File_Template.md` enum values (Draft / Transitional) — the draft had written a Body-Stability value ("Transitional") into the Status field and invented a non-canonical Body Stability value ("Improving"); (2) Spec Gates reverted 2/6 → 1/6 and the draft's invented file-local "Spec Gates Definition" table (which redefined G1–G6 as content milestones) removed — Gate 2 was self-declared "Closed (structural)" with no Gate 1 Fallacy Check or Gate 2 Physical Plausibility pass by a different agent, and the canonical G1–G6 meanings are fixed by `Admin/Verification_Gates.md`, not locally redefinable per file; (3) restored the Superconductivity section's original Integration Pathways and Cross-References & Migration Path content, which the draft had cut despite claiming full preservation — stripped only the non-substantive citation-card render artifacts; (4) corrected ASM-006's citation from `Operations/Electronics.md` CF-001 to `Architecture/Cognitive_Frameworks.md` CF-001 (owning file), noting Electronics.md as implementer; (5) added inline notes disambiguating the table's "G5" (Gate_05_Separation_Thermal.md) and the Source Classes table's "G₁–G₅" labels from canonical Spec Gates 1–6, to prevent future conflation. Open Unknowns unchanged at 3; no new unknowns registered for the proposed EGL pending a real Gate 1 pass.
- 2026-08-02: **Dual-audit adjudication (Gemini Skeptic/Auditor + Grok Skeptic/Auditor, both against `Admin/Auditor_Protocols.md`/`Admin/Forge_Audit_Kit.md`), human-directed.** Both audits verified against source before acting on either. Merged from Gemini (found, Grok missed): (1) the Source Classes table's TEG description ("stabilizes baseline rails") and the Layer 2 Operational Modes table's Logic/Watchdog row (listing "Primary TEG" as a baseline-mode source) implied TEG can supply idle-state load with no active thermal process running — physically ungrounded, since TEG output requires `Q_waste(t) > 0`; corrected, and EV-005 registered to track the underlying net-positive-threshold gap; (2) EV-004 registered for EAL hardware watchdog/firmware-isolation validation — ASM-006 carried the assumption but nothing tracked the hardware realization itself; (3) the Safety Advisory's "treat as structural specification" phrasing revised to "candidate architectural model" — legitimate semantic-hygiene catch, since "specification" is a loaded term adjacent to the File State `Status` enum; (4) the bare "Engineering.md" cross-reference corrected to `Architecture/Engineering.md`, matching this repo's first-mention-full-path convention; (5) Voltage Ripple values in the Operational Modes table tagged `[Placeholder]`, matching the file's existing confidence-labeling convention elsewhere; (6) Storage Model gained Safe Maintenance Access and End-of-Life Disposal Routing subsections (cross-referencing `Operations/Gate_02_Triage.md` and `Challenges/Waste.md`), closing a real lifecycle-truncation gap both audits independently noted at different severities. **Rejected from Gemini's audit:** the finding that the Ethical Anchor field's unprefixed "Ethical_Constraints.md" needs an `Admin/` prefix — `Admin/File_Template.md` fixes that exact unprefixed string as the canonical, non-negotiable value across every file in this repository, and `Tests/Support_Raft.md`'s own Resolution Log records a 9-file sweep (2026-07-12) that *removed* an `Admin/`-prefixed variant to restore this same plain-text form; adding the prefix would repeat a mistake already caught and fixed once. Also not adopted: Gemini's flag on "Payment via Specification only" as semantic drift — that phrase is the file's own pre-existing, previously-audited idiom (used identically in EV-001/002/003's Resolution Paths since 2026-05-31), not new promotion-hazard language. On balance, Grok's gate verdicts (G1/G2-provisional/G4/G5/G6 cleared, G3 partial-by-design) were better calibrated to what this file actually claims about itself — Energy.md's Status has been Draft/Exploration throughout and never purported to pass any gate, so treating open physical-plausibility gaps in clearly-quarantined proposed content as file-blocking (Gemini's framing) overstates the stakes; Grok's "flag and track" framing better matches the file's own honesty about its maturity. Open Unknowns 3 → 5 (EV-004, EV-005). Status/Spec Gates unchanged (Draft, 1/6) — none of this promotes anything, it corrects and tracks.

---

## Abandoned Paths

| Date       | Path                                      | Why Abandoned                                                              | Reconsider? |
|------------|--------------------------------------------|-------------------------------------------------------------------------------|-------------|
| 2026-08-02 | File-local redefinition of Spec Gates 1–6 | Conflicts with canonical gate definitions in `Admin/Verification_Gates.md`; would desync this file's gate semantics from the rest of the repo | No — use canonical gates only |

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
- Spec Gates 1–6 redefined locally within this file rather than deferring to `Admin/Verification_Gates.md`

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

*End of Energy.md*
