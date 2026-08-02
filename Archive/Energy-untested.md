Here is the complete **Energy.md v1.1** — a full regeneration that preserves every original safety interlock, assumption, unknown, drift indicator, and cross-reference while incorporating the unified Energy Governance Layer (Demand Model + Generation Model + Energy Arbitration Layer + Thermal Integration Architecture), a new Storage Model, and a Capability Trajectory.

```markdown
# Energy.md — Energy Strategy & Governance

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Salvaged electrochemical batteries with unknown state-of-health present catastrophic thermal runaway and toxic hydrofluoric acid outgassing risks. Containment and isolation protocols are mandatory before any salvaged battery bank is commissioned (EV-003). Do not install salvaged storage in unventilated or uninsulated enclosures. Air Scrubber operation is strictly required during any battery handling, charging, or thermal failure event. **When in doubt, isolate the battery bank and do not proceed.**
>
> Multi-source operation (grid + motor-generators + biogas + solar + thermal recovery) introduces voltage, frequency, and ripple instability risks. The Energy Arbitration Layer (EAL) and Source Stability & Harmonization Layer are mandatory before any hybrid configuration is commissioned.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Transitional                                                        |
| Body Stability   | Improving                                                           |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-31 (original); expanded 2026-08-01                          |
| Auditor          | Gemini (original); multi-agent expansion (Demand / EAL / TIA / Generation) |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*High risk reflects uncharacterized salvaged battery thermal behavior (EV-003) and the absence of measured power-demand data (EV-001). The Energy Governance Layer now provides the constitutional structure; measurement and physical validation remain required before Spec Gate 3.*

---

## Scope Boundary

**This file DOES define:**
- Design philosophy for incremental energy integration at v0–v1
- Energy lifecycle progression from external grid reliance to partial thermal/waste recovery
- Real-world generation interlocks for syngas and biomass loops
- Calibrated power mode envelopes and actionable voltage sag protocols
- Hard-coded physical protection parameters and isolation boundaries for salvaged batteries
- Primary and secondary falsifiable performance metrics
- **Energy Governance Layer (EGL)** — Demand Model, Generation Model, Energy Arbitration Layer (EAL), Thermal Integration Architecture (TIA)
- Storage Model & Battery Governance (expansion of EV-003)
- Source Stability & Harmonization Layer
- Energy Capability Trajectory (v0 → v3)

**This file DOES NOT define:**
- Deep-environment battery degradation physics modeling (→ `Tests/Leviathan_testing.md` LT-002)
- Leviathan power envelope specification (→ `Tests/Leviathan_testing.md` LT-001)
- Mechanical drawings for battery containment structures
- Detailed chemistry sorting algorithms for unknown cells (→ `Operations/Gate_02_Triage.md`)
- Full cryptographic key management or root-of-trust for energy controllers (cross-ref Electronics.md EL-006)
- Detailed superconductivity materials science (exploratory horizon only)

---

## File Purpose

This file defines the energy strategy and governance substrate for the Lazarus Forge. The Forge is energy-intensive by nature — reduction, thermal separation, fabrication, and autonomous operation all draw significant power. Energy.md provides a plausible, incremental path from external grid dependency toward partial self-sufficiency through salvaged and waste energy sources, without claiming energy independence that has not been demonstrated.

Its primary function as a cross-reference anchor is the Power Demand stub and the Energy Governance Layer — a demand-side and allocation baseline that allows Leviathan power envelope scoping, per-module energy accounting, and safety interlocks to integrate against a common reference point, even before actual figures are measured.

If this file disappeared, the repository would have no shared energy accounting baseline, no demand-side anchor for cross-module power budgeting, no real-time arbitration doctrine, and no thermal-to-electrical coupling model. Every autonomous system the Forge builds would rest on unvalidated power assumptions.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Grid power is available at v0 bootstrap site | v0 terrestrial deployment context | Medium | Off-grid or remote deployment confirmed — bootstrap strategy changes |
| ASM-002 | Salvaged motor-generators can be back-driven to produce usable electricity | Standard electromechanical reversibility principle | Medium | First salvaged motor-generator characterized for output efficiency |
| ASM-003 | Biogas output can overcome parasitic overheads via thermal recovery | Bound to 35°C digestate tank rule | Medium | EV-002 baseline measurements prove net-negative balance |
| ASM-004 | Salvaged batteries retain sufficient usable capacity to serve as energy buffer | Common salvage practice; SoH unknown | Low | First salvaged battery bank characterized for SoH and cycle capacity |
| ASM-005 | Waste heat from Spin Chamber and other thermal processes is available for opportunistic reuse | `Operations/Gate_05_Separation_Thermal.md` exhaust profile | Low | SC-007 resolved — exhaust heat load characterized |
| ASM-006 | Discrete or minimal-firmware controllers can implement EAL priority logic without introducing new programmable attack surface | Cross-ref Electronics.md CF-001 / discrete watchdog doctrine | Low | First EAL hardware prototype validated against adversarial firmware compromise |

---

## Design Philosophy

- **Energy demand is acknowledged, not hidden:** Power budgets must reflect real electromechanical and thermal loads, not idealized values.
- **Early stages prioritize learning over efficiency:** Robust, basic containment and crude power transformation trump high-efficiency micro-grids at v0 bootstrap.
- **Salvage-first applies to power systems as well:** Repurposing industrial automotive alternator blocks and salvaged battery cells is the primary hardware path.
- **Multiple small contributors are preferred over single large sources:** Spreading generation across solar, syngas, and grid links prevents single-point failure cascades.
- **Energy is a constitutional substrate:** Every other subsystem stands on the Energy Governance Layer. Safety rails (P₁) never brown out; thermal hazards never propagate; mode transitions are predictable and governed.

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

## Energy Governance Layer (EGL) — Unified Architecture

The Energy Governance Layer defines how the Forge consumes, produces, routes, recovers, throttles, and safely shuts down all energy flows — electrical and thermal — across every subsystem. It is the constitutional backbone of the Forge’s energy system.

The EGL integrates four load-bearing components:

- **Demand Model** — what the Forge needs  
- **Generation Model** — what the Forge produces  
- **Energy Arbitration Layer (EAL)** — how the Forge allocates  
- **Thermal Integration Architecture (TIA)** — how the Forge routes heat  

Together they form a closed governance loop that prevents catastrophic brownouts, thermal runaway, generator stall, battery collapse, and cross-module instability.

### I. Closed Governance Loop

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

This loop runs continuously and forms the Forge’s real-time energy constitution.

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
  Must never brown out. Hard safety boundary (cross-ref Electronics.md CF-001).

- **Scrubber Rail (S)**  
  \[
  S(t) = S_{\text{fan}} + S_{\text{compressor}} + S_{\text{diagnostic}}
  \]
  Typical v0 range: 50–150 W. Must remain operational during any hazardous process.

Governance constraint: If \(L(t) + W(t) + S(t)\) cannot be maintained, all other loads must be shed and Safe Halt entered.

#### Layer 2 — Operational Modes

| Mode              | Target Consumption          | Tolerable Voltage Ripple | Mandated Source Allocation                  | Actionable Sag Protocol                          |
|-------------------|-----------------------------|---------------------------|---------------------------------------------|--------------------------------------------------|
| Logic / Watchdog  | < 15 W baseline             | ±1%                      | Primary TEG / Isolated Lead-Acid Buffer     | Maintain state indefinitely; keep-alive telemetry |
| Mechanical Milling| 1.5 kW peak                 | ±5%                      | Hydro-Engine / Main Battery (SoH > 70%)     | Cycle spindle 50%; halt axis steppers            |
| Nominal           | 15–40 kW                    | ±5%                      | Grid / Scaled Generators + Air Scrubber     | Throttle feed rates; pause secondary axes        |
| Thermal Melt (G5) | 8.0 kW burst                | ±10%                     | Direct Generator / Biomass Syngas Loop      | Safety clamp; dump molten charge to safe crucible|

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

This is the canonical reference for all energy budgeting, generator sizing, battery sizing, and safety interlocks.

---

### III. Generation Model — Supply Architecture

#### Source Classes

| ID | Source                  | Equation / Notes                                      | Governance Constraint                          |
|----|-------------------------|-------------------------------------------------------|------------------------------------------------|
| G₁ | Grid                    | \(P_{\text{grid}}(t) = P_{\text{contract}} - P_{\text{ripple}}\) | Bootstrap only; not assumed for v1+           |
| G₂ | Salvaged Motor-Generators | \(P_{\text{MG}}(t) = \eta_{\text{MG}} \cdot \tau(t) \cdot \omega(t)\) | Tar Minimization Rule mandatory               |
| G₃ | Biogas                  | \(P_{\text{biogas}}(t) = \eta_{\text{gen}} \cdot \dot{m}_{\text{CH}_4} \cdot LHV\) | Net-positive only if digestate > 35 °C and parasitic < 22% |
| G₄ | Solar                   | \(P_{\text{solar}}(t) = \eta_{\text{PV}} \cdot A \cdot I_{\text{solar}}(t)\) | Supplemental; offsets control loads           |
| G₅ | Thermal Recovery (TEG)  | \(P_{\text{thermal}}(t) = \eta_{\text{TEG}} \cdot Q_{\text{waste}}(t)\) | \(\eta_{\text{TEG}} \approx 3\text{–}7\%\); stabilizes baseline rails |

#### Net Generation

\[
G_{\text{net}}(t) = \sum_i P_{i,\text{net}}(t)
\]

where each \(P_{i,\text{net}}\) subtracts friction, cooling, mixing, compression, and charge-controller losses.

#### Source Stability & Harmonization

- Bus voltage must remain within ±5% of nominal.
- Frequency deviation > 2% triggers mode downgrade.
- Ripple above threshold sheds P₄ loads first.
- No source may back-feed another without verified isolation.
- Priority order for source selection: Grid → MG → Biogas → Solar → Thermal.

---

### IV. Energy Arbitration Layer (EAL)

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

No exceptions. No software overrides.

Canonical allocation:

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

### V. Thermal Integration Architecture (TIA)

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

### VI. Storage Model & Battery Governance (Expansion of EV-003)

Salvaged battery state-of-health (SoH), cycle history, and remaining capacity are uncharacterized at v0. The following physical and governance rules apply:

- **Physical Isolation:** Lithium-ion or lead-acid packs must reside in an isolated, external, pressure-vented enclosure separated from primary computational nodes and volatile feedstocks by a minimum 2-hour fire-rated containment barrier.
- **Over-Extraction Guard:** Discharge cut-off locked via hard-coded physical voltage dividers at 3.0 V per cell for lithium-class chemistry. Suppresses copper shunting and subsequent self-heating runaway.
- **Scrubber Prerequisite:** Any cell temperature > 55 °C forces main battery disconnect relay open via hardware trip and locks `Operations/Air_Scrubber.md` variant-0 positive-pressure loop into max-flow mode.
- **SoH Classification (v1 target):**  
  – Class A: SoH ≥ 80 %, usable for productive loads  
  – Class B: 50–80 %, restricted to opportunistic / buffer use  
  – Class C: < 50 % or unknown, material recovery only  
- **Buffer Sizing:** Baseline rails must be supportable from isolated buffer for ≥ 30 minutes under Safe Halt conditions.
- **Degradation Tracking:** Cycle count and capacity fade logged; slope feeds falsifiable metrics.

---

### VII. EGL Constitutional Guarantees

1. Safety rails (P₁) never brown out.  
2. Thermal hazards (T₁) never propagate.  
3. Generators never stall under uncontrolled load.  
4. Battery banks never enter runaway without containment and scrubber response.  
5. Scrubber always remains operational during hazardous processes.  
6. Mode transitions are predictable and governed.  
7. Energy claims are falsifiable and auditable.  
8. No subsystem can override energy safety boundaries.

---

## Superconductivity Horizons (Exploratory / v1+)

Superconductivity remains a high-leverage multiplier for Value recovered per kWh, but is treated strictly as an engineering target, not a near-term assumption.

- Ambient-pressure progress is the priority.  
- No dedicated R&D budget at v0–v1; monitor external progress and salvage opportunities only.  
- Any candidate material must pass four-point probe + basic susceptibility checks before integration.  
- All designs must support graceful degradation to copper/aluminum baselines.  
- Unknowns tracked externally: SC-H1 (practical materials < 200 K), SC-H2 (salvage-compatible wire/joints), SC-H3 (net system kWh benefit after cooling/strain infrastructure).

**Drift Indicator:** Treating superconductivity as assumed or near-term rather than exploratory triggers re-audit.

---

## Energy Capability Trajectory

| Stage | Horizon | Capability Target                                      | Key Gate                          |
|-------|---------|--------------------------------------------------------|-----------------------------------|
| v0    | Bootstrap | Grid + isolated buffer + basic motor-generators       | EV-001 measured, EV-003 enclosure validated |
| v1    | Hybrid  | Solar + regulated biogas + TEG banks + full EAL/TIA   | Spec Gate 3, multi-source stability demonstrated |
| v2    | Partial self-sufficiency | Closed thermal loops, remote-capable buffers         | Net-positive biogas under cold-start, SoH Class A banks |
| v3    | Loop closure | High-efficiency recovery + optional superconductivity | Full falsifiable kWh/kg economics, remote Leviathan support |

---

## Metrics (Falsifiable)

**Primary metric:** kWh consumed per kg of recovered usable output  
(“Usable output” = material that passes `Operations/Gate_02_Triage.md` electrical or mechanical verification.)

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
|------------|-----------------|---------------------------------|--------------------------------------|-------------------------------------------------------|------------|---------------------|
| 2026-05-31 | Field / Audit   | Raw syngas combustion routing   | Valve gumming within 12 h            | Multi-stage particulate filtration + oil-bubbler mandatory | High       | No                  |
| 2026-08-01 | Architecture    | Flat power budgeting without arbitration | Cascading brownout risk under multi-source operation | Full Demand + Generation + EAL + TIA required as constitutional layer | Analogous  | Yes — first hardware validation |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### EV-001 — Forge power demand uncharacterized at any operating mode

| Field         | Value                                                               |
|---------------|---------------------------------------------------------------------|
| Status        | In Progress                                                         |
| Risk          | Medium                                                              |
| Priority      | Major                                                               |
| Type          | Technical                                                           |
| Blocking      | Yes — blocks v1 operating cost model and `Admin/Economics.md` EC-002 |
| Owner         | `Operations/Energy.md`                                              |
| First Logged  | 2026-05-27                                                          |
| Last Reviewed | 2026-08-01                                                          |

**Description:** Actual consumption of the physical bootstrap hardware remains an estimate based on industrial analogs. Demand Model equations now exist; measured data does not.

**Why It Matters:** EV-001 is the demand-side anchor for all cross-module energy accounting. Without measured figures, every power budget claim carries Placeholder confidence.

**Resolution Path:** Replace analog values in the Demand Model with real shunt-resistor / current-transformer telemetry as hardware validation completes. Payment via Specification once measured figures replace Placeholder values.

---

### EV-002 — Parasitic and thermal startup loads for biogas streams uncharacterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | `Operations/Energy.md`                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-08-01                                       |

**Description:** Total net energy yield of anaerobic digestion loops is unmeasured under cold-start conditions.

**Resolution Path:** Enforce 35 °C thermal interlock and 22 % maximum compressor energy rule. Capture gas-flow meter data against input feedstock mass vectors during initial operational loops. Payment via Specification once first cycle data characterizes net yield.

---

### EV-003 — Salvaged battery thermal containment and ventilation strategy undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | Yes — before enclosed battery bank commissioning |
| Owner         | `Operations/Energy.md`                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-08-01                                       |

**Description:** Unknown state-of-health battery modules present catastrophic thermal runaway vectors. Full containment and ventilation doctrine not yet physically validated. Storage Model now defines classification and buffer requirements; physical build remains open.

**Resolution Path:** Physical isolation rules, locked 3.0 V/cell hard-guards, and Air Scrubber Max-Flow auto-trigger now codified. Move to resolved once the external fire-rated enclosure physical build passes cold safety audit. Payment via Specification once enclosure is physically verified.

---

### Resolution Log

- 2026-05-27: EV-001–003 logged and structured.
- 2026-05-31: Spec Gate 1 baseline; Tar Minimization and 35 °C/22 % interlocks integrated; EV-001 bound to hardware envelope table; EV-003 physical isolation codified.
- 2026-06-08: Navigation Anchors and Verification Ref corrected; sidecar format normalized.
- 2026-07-12: Abandoned Paths / Drift Indicators reordered per template.
- 2026-08-01: Full Energy Governance Layer (Demand + Generation + EAL + TIA) integrated; Storage Model expanded from EV-003; Capability Trajectory added; Spec Gates advanced to 2/6; File Status → Transitional.

---

## Abandoned Paths

| Date       | Path                                      | Why Abandoned                                      | Reconsider? |
|------------|-------------------------------------------|----------------------------------------------------|-------------|
| 2026-08-01 | Flat power budgeting without arbitration  | Cascading brownout and generator-stall risk under multi-source operation | No — EAL is permanent doctrine |

---

## Drift Indicators

Mandatory re-audit conditions:

- Power Demand mode definitions revised without updating the hardware power envelope limits or Demand Model equations
- Biogas counted as a net-positive source if digestate core temp drops below 35 °C for sustained periods
- Salvaged battery storage commissioned in an enclosed space without a verified 2-hour fire barrier or independent ventilation routing
- Hard-coded lithium voltage cutoff shifted below 3.0 V via software override patches
- The falsifiable primary metric (kWh per kg) is replaced with non-measurable efficiency targets
- EAL priority ordering (P₁ > P₂ > P₃ > P₄) altered or software-bypassed
- Thermal Class T₁ loads routed without verified containment path
- Superconductivity treated as assumed near-term capability rather than exploratory horizon
- Multi-source hybrid configuration commissioned without Source Stability & Harmonization validation

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Spec Gates Definition (Energy.md)

| Gate | Description                                      | Status (v1.1) |
|------|--------------------------------------------------|---------------|
| 1    | Bootstrap interlocks and containment codified    | Closed        |
| 2    | Energy Governance Layer (Demand + Generation + EAL + TIA) defined | Closed (structural) |
| 3    | Measured demand and generation data replace analogs | Open          |
| 4    | Multi-source stability and EAL hardware validated | Open          |
| 5    | Storage Model SoH classification and buffer sizing demonstrated | Open          |
| 6    | Full falsifiable economics and Capability Trajectory Stage v2 readiness | Open          |

---

*End of Energy.md v1.1*
```

This version is ready for direct use as the canonical file. It advances Spec Gates to 2/6 on structural completeness, keeps every original safety rule and unknown intact, and embeds the full Energy Governance Layer as the constitutional core.
