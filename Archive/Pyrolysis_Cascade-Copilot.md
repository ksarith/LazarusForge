> **MERGED — see Tests/Pyrolysis_Cascade.md Resolution Log.** This is archived raw material, already processed into the live file.

Wanting to draft a new test.
Pyrolysis_Cascade.md
The idea is can we load a furnace full of garbage, use current Pyrolysis methods and cook the contents down recovering the fuel outputs.  Afterwards offload the what would be coke(unburned remnants of Pyrolysis) to a bloomery type furnace to do subsequent extractions.  The heat from the bloomery channeled to the Pyrolysis chamber(s).  
Controlling off-gas is expected every step. Air_Scrubber.md should be expected.  Separation of materials is the goal.  The system would be expected to lose money initially, but could the gains eventually be realized?  

Concise takeaway:  
A pyrolysis–bloomery cascade can be engineered as a closed‑loop materials‑separation system, but its economic viability depends on throughput, feedstock consistency, energy integration efficiency, and the value of recovered fractions. Technically feasible; economically challenging but not impossible.

---

Pyrolysis Cascade: Technical Architecture

1. Primary Pyrolysis Furnace
A garbage‑fed pyrolysis chamber operating at 400–700 °C produces:
- Syngas (CO, H₂, light hydrocarbons)  
- Pyro‑oil (tar, phenolics, mixed organics)  
- Char/coke‑like solids (carbonaceous residue + metals + glass + inert fines)

Key engineering requirements:
- Continuous feed system with shredding + moisture control  
- Oxygen‑starved environment  
- Real‑time off‑gas monitoring  
- Heat‑recapture channels from downstream bloomery  

2. Bloomery Furnace Stage
The char/coke fraction is transferred to a bloomery‑type furnace (1100–1300 °C) for:
- Reduction of metal oxides  
- Melting/separation of ferrous vs non‑ferrous metals  
- Further carbon burnout  
- Slag formation (glass, ceramics, silicates)

The bloomery’s waste heat is ducted back to the pyrolysis chamber, reducing external fuel demand.

3. Air Scrubber System
Air_Scrubber.md is essential because:
- Pyrolysis off‑gas contains benzene, PAHs, dioxin precursors  
- Bloomery exhaust contains particulates, SOx/NOx, metal fumes  
- A multi‑stage scrubber (cyclone → wet scrubber → activated carbon → catalytic oxidizer) is required for compliance

---

Material Separation Pathways

1. Hydrocarbon Recovery
- Syngas → power generation or methanation  
- Pyro‑oil → hydrotreating → usable fuel fractions  
- Condensable tars → chemical feedstock  

2. Metals Recovery
Bloomery output yields:
- Ferrous bloom  
- Non‑ferrous melt pools (Al, Cu, Zn)  
- Slag that can be crushed for mineral recovery  

3. Carbon Recovery
Char → activated carbon, soil amendment, or reductant for metallurgical processes.

---

Thermodynamic Integration

Heat Cascade Logic
1. Bloomery produces high‑grade heat (1100–1300 °C).  
2. Pyrolysis requires moderate heat (400–700 °C).  
3. Heat exchangers + refractory ducting allow bloomery waste heat to preheat pyrolysis feedstock.  
4. Syngas from pyrolysis can also fire the bloomery.

This creates a two‑way energy loop.

---

Economic Viability Analysis

Short‑Term (Negative Margin Expected)
Reasons:
- High capital cost (furnaces, scrubbers, shredders, conveyors)  
- Complex permitting (air quality, waste processing)  
- Mixed waste streams reduce efficiency  
- Skilled labor requirement  

Long‑Term (Conditional Positive Margin)
Profitability depends on:
- Feedstock contracts (municipal waste tipping fees often $40–$120/ton)  
- Recovered metals (ferrous + non‑ferrous)  
- Carbon products (activated carbon has high market value)  
- Fuel outputs (syngas + pyro‑oil)  
- Heat integration efficiency (≥60% recapture is ideal)  

A well‑run system can eventually break even or become profitable if:
- Throughput exceeds ~50–100 tons/day  
- Feedstock is consistent  
- Scrubber efficiency keeps regulatory costs low  
- Recovered materials have stable buyers  

---

Non‑Obvious Insight
The real economic engine is not the fuel output—it’s the tipping fees + metals recovery.  
If municipalities pay you to take garbage, the pyrolysis cascade becomes a materials‑mining operation disguised as waste management.

---

Table: Requirements → Outcomes

| Requirement | Outcome | Risk |
| --- | --- | --- |
| High‑temperature bloomery | Metal separation + heat recapture | Refractory wear |
| Multi‑stage scrubber | Regulatory compliance | High OPEX |
| Continuous feed pyrolysis | Stable syngas/oil output | Feedstock variability |
| Heat integration | Lower fuel cost | Complex ducting |
| Materials sorting | Revenue streams | Labor + automation cost |

---

Recommendation
Build a pilot‑scale unit (1–5 tons/day) to validate:
- Heat‑integration efficiency  
- Syngas quality  
- Char composition  
- Metal recovery yield  
- Scrubber performance  

If the pilot shows ≥40% energy recapture and ≥70% metals recovery, scaling becomes viable.

---

Follow‑up (choose one)
Would you like to explore:
- A full engineering specification for PyrolysisCascade.md  
- A financial model estimating break‑even throughput  
- A process‑flow diagram with all furnace and scrubber stages

Concise takeaway:  
Below is a full engineering specification for Pyrolysis_Cascade.md, written as a rigorous technical document suitable for integration into your governance architecture and systems‑design corpus. It is structured as a formal engineering spec: scope, functional requirements, thermodynamic model, control systems, safety, and economic parameters.

---

Pyrolysis_Cascade.md — Engineering Specification
(Version 1.0 — Draft)

1. Purpose and Scope
The Pyrolysis Cascade System (PCS) is a multi‑stage thermal‑processing architecture designed to convert mixed municipal solid waste (MSW) into separable material fractions—hydrocarbons, metals, carbon solids, and inert slag—through a controlled sequence of pyrolysis and bloomery‑type reduction. The system integrates heat flows, off‑gas scrubbing, and materials handling to maximize recovery while minimizing emissions.

The PCS is intended for:
- Waste‑to‑resource conversion  
- Materials separation and recovery  
- Energy recapture and internal reuse  
- Long‑term economic viability through tipping fees + recovered materials  

---

2. System Overview

2.1 Major Subsystems
- Primary Pyrolysis Furnace  
- Bloomery Reduction Furnace  
- Air Scrubber System  
- Feedstock Pre‑Processing Line  
- Heat‑Exchange and Ducting Network  
- Condensation & Fractionation Train  
- Materials Separation & Post‑Processing Line  
- Supervisory Control and Data Acquisition (SCADA)  

---

3. Feedstock Requirements

3.1 Acceptable Inputs
- Mixed MSW (post‑shredding)  
- Plastics (PE, PP, PS, PET)  
- Biomass, paper, cardboard  
- Rubber  
- Organics (food waste, yard waste)  
- Light metals (Al, Cu, Zn)  
- Ferrous metals  
- Glass, ceramics  

3.2 Prohibited Inputs
- Pressurized vessels  
- Explosives  
- High‑chlorine industrial waste (unless scrubber capacity is expanded)  
- Radioactive materials  

3.3 Pre‑Processing
- Shredding to <50 mm particle size  
- Moisture reduction to <20%  
- Magnetic pre‑sort (optional)  
- Density separation (optional)

---

4. Primary Pyrolysis Furnace Specification

4.1 Operating Conditions
- Temperature: 400–700 °C  
- Pressure: Slight negative (−5 to −20 Pa)  
- Atmosphere: Oxygen‑starved (<2% O₂)  
- Residence time: 20–60 min  

4.2 Outputs
- Syngas (CO, H₂, CH₄, C₂–C₄ hydrocarbons)  
- Pyro‑oil (condensable organics)  
- Char/Coke Fraction (carbon solids + metals + inert materials)  
- Non‑condensable off‑gas  

4.3 Furnace Construction
- Refractory lining: High‑alumina + SiC  
- Heating method:  
  - Bloomery waste‑heat ducting  
  - Supplemental syngas burners  
- Feed mechanism: Continuous auger or ram‑feed  
- Off‑gas port: High‑temperature alloy, corrosion‑resistant  

---

5. Bloomery Reduction Furnace Specification

5.1 Operating Conditions
- Temperature: 1100–1300 °C  
- Atmosphere: Reducing (CO‑rich)  
- Residence time: 1–3 hours  

5.2 Functions
- Reduction of ferrous oxides → metallic bloom  
- Melting of non‑ferrous metals → separate melt pools  
- Carbon burnout → slag formation  
- Thermal output → ducted to pyrolysis chamber  

5.3 Construction
- Refractory: Magnesia‑carbon brick  
- Tuyere system: Forced air or syngas injection  
- Slag tapping port  
- Metal tapping port  

---

6. Heat Integration Network

6.1 Heat Flow Logic
1. Bloomery produces high‑grade heat.  
2. Heat exchangers transfer this to pyrolysis chamber.  
3. Pyrolysis syngas fires bloomery burners.  
4. Excess heat used for feedstock drying.

6.2 Efficiency Targets
- ≥60% heat recapture  
- ≤15% external fuel requirement  

6.3 Components
- Refractory ducting  
- Recuperative heat exchangers  
- Syngas burners  
- Thermal monitoring nodes  

---

7. Off‑Gas Handling and Scrubbing

7.1 Multi‑Stage Scrubber (Air_Scrubber.md)
- Cyclone separator → particulates  
- Venturi wet scrubber → acid gases  
- Activated carbon bed → VOCs, dioxin precursors  
- Catalytic oxidizer → final cleanup  

7.2 Emission Targets
- Particulates <10 mg/m³  
- VOCs <5 mg/m³  
- SOx/NOx within local regulatory limits  
- Dioxins/furans: nondetectable  

---

8. Condensation & Fractionation Train

8.1 Stages
- Primary condenser (water‑cooled)  
- Secondary condenser (glycol‑cooled)  
- Tar separator  
- Fractionation column (optional)  

8.2 Outputs
- Light pyro‑oil  
- Heavy tar  
- Water phase  
- Non‑condensable gas  

---

9. Materials Separation Line

9.1 Char Processing
- Magnetic separation  
- Eddy‑current separation  
- Density table  
- Carbon solids → activation or sale  

9.2 Metal Recovery
- Ferrous bloom → forging or remelt  
- Non‑ferrous melt → casting or sale  

9.3 Slag Handling
- Quenching  
- Crushing  
- Mineral recovery (optional)  

---

10. Control Systems (SCADA)

10.1 Sensors
- Thermocouples (Type K, Type S)  
- O₂ sensors  
- CO/CO₂/H₂ analyzers  
- Pressure transducers  
- Flow meters  

10.2 Control Logic
- PID loops for temperature  
- Negative‑pressure maintenance  
- Gas‑composition feedback  
- Automated slag tapping alerts  

10.3 Data Logging
- 1 Hz sampling minimum  
- Full audit trail for regulatory compliance  

---

11. Safety Systems

11.1 Thermal Safety
- Over‑temperature shutdown  
- Refractory integrity monitoring  

11.2 Gas Safety
- CO/H₂ alarms  
- Automatic flare stack for emergency venting  

11.3 Mechanical Safety
- Interlocks on feed system  
- Emergency quench system  

---

12. Economic Model Parameters

12.1 Cost Centers
- Capital: Furnaces, scrubbers, conveyors, SCADA  
- Operating: Labor, refractory replacement, utilities  
- Maintenance: Annual shutdown, ducting inspection  

12.2 Revenue Streams
- Tipping fees ($40–$120/ton typical)  
- Recovered metals  
- Activated carbon  
- Pyro‑oil (if refined)  
- Syngas (internal energy offset)  

12.3 Break‑Even Conditions
- Throughput ≥50–100 tons/day  
- Heat recapture ≥40%  
- Metals recovery ≥70%  
- Scrubber OPEX within budget  

---

13. Non‑Obvious Engineering Insight
The bloomery stage is not merely a metal‑recovery unit—it is the thermal engine of the entire cascade. Its waste heat stabilizes pyrolysis temperatures, reducing external fuel demand and enabling the system to approach thermodynamic self‑sufficiency.

---

14. Recommended Next Steps
- Pilot plant design (1–5 tons/day)  
- Thermodynamic simulation  
- Materials characterization of char fraction  
- Scrubber performance modeling  

---

Follow‑up options
Choose the next step you want to develop:  
- Financial model for break‑even throughput  
- Thermodynamic simulation specification  
- Control‑system logic and SCADA architecture
Thermodynamic simulation for Pyrolysis_Cascade.md
(Version 1.0 — Draft specification)

---

1. Simulation objectives

- Primary objective:  
  Quantitatively evaluate energy flows, temperature profiles, and fuel requirements for the integrated pyrolysis–bloomery cascade, including off‑gas utilization and heat recapture.

- Secondary objectives:  
  - Determine minimum external fuel input for steady‑state operation.  
  - Assess sensitivity to feedstock composition, moisture, and throughput.  
  - Estimate syngas LHV, bloomery heat output, and net energy balance.  
  - Identify bottlenecks in heat transfer and off‑gas routing.

---

2. System boundaries and assumptions

2.1 System boundaries

- Included:  
  - Feedstock pre‑drying and pre‑heating.  
  - Primary pyrolysis furnace.  
  - Bloomery furnace.  
  - Heat‑exchange network (ducting, recuperators).  
  - Syngas burners and flare stack.  
  - Condensation train (for energy removal).  

- Excluded (for first‑pass model):  
  - Detailed scrubber thermodynamics (treated as fixed ΔT and ΔP).  
  - Mechanical work (fans, conveyors) beyond simple electrical load.  
  - Micro‑scale reaction kinetics (use lumped reaction models).

2.2 Global assumptions

- Steady‑state operation (no transient startup/shutdown).  
- Uniform feedstock properties per scenario.  
- Lumped parameter reactors (CSTR or PFR approximations).  
- Ideal gas behavior for syngas at process conditions.  
- Negligible heat loss outside specified loss coefficients.

---

3. Feedstock and stream definitions

3.1 Feedstock characterization

Define at least three canonical feedstock scenarios:

- Scenario A — MSW mixed:  
  - 40% organics, 20% plastics, 20% paper/cardboard, 10% textiles, 10% metals/inerts.  
  - Moisture: 25% (pre‑drying to 15%).  
  - HHV (dry basis): ~15–18 MJ/kg.

- Scenario B — Plastic‑rich:  
  - 60% plastics, 20% paper/cardboard, 10% organics, 10% metals/inerts.  
  - Moisture: 10%.  
  - HHV (dry basis): ~25–30 MJ/kg.

- Scenario C — Biomass‑rich:  
  - 60% organics/biomass, 20% paper/cardboard, 10% plastics, 10% metals/inerts.  
  - Moisture: 30% (pre‑drying to 20%).  
  - HHV (dry basis): ~14–17 MJ/kg.

For each scenario, define:

- Mass flow rate: \( \dot{m}_{\text{feed}} \) [kg/h].  
- Proximate analysis: moisture, volatile, fixed carbon, ash.  
- Ultimate analysis: C, H, O, N, S, Cl (mass fractions).

3.2 Stream list

Label all major streams:

- S1: Feedstock into pre‑dryer.  
- S2: Dried feedstock into pyrolysis furnace.  
- S3: Pyrolysis syngas (hot).  
- S4: Pyro‑oil + condensables.  
- S5: Char/coke + metals + inerts out of pyrolysis.  
- S6: Char/coke feed into bloomery.  
- S7: Bloomery off‑gas (hot).  
- S8: Bloomery slag + metal outputs.  
- S9: Recovered syngas to burners.  
- S10: External fuel (if any).  
- S11: Heat to ambient (losses).  

---

4. Reactor models and energy balances

4.1 Pyrolysis furnace model

Treat pyrolysis as a lumped endothermic reaction:

- Overall reaction form (conceptual):

\[
\text{Feedstock} \rightarrow \alpha \cdot \text{Syngas} + \beta \cdot \text{Pyro-oil} + \gamma \cdot \text{Char} + \delta \cdot \text{Ash}
\]

Where \(\alpha, \beta, \gamma, \delta\) are mass yield fractions dependent on feedstock and temperature.

- Energy balance (steady‑state):

\[
\dot{Q}{\text{in}} + \sum \dot{m}i hi^{\text{in}} = \sum \dot{m}j hj^{\text{out}} + \dot{Q}{\text{loss}} + \dot{Q}_{\text{rxn}}
\]

Where:

- \(\dot{Q}_{\text{in}}\): heat from bloomery + burners.  
- \(h_i^{\text{in}}\): specific enthalpy of incoming streams (feedstock, preheated).  
- \(h_j^{\text{out}}\): specific enthalpy of syngas, char, pyro‑oil.  
- \(\dot{Q}{\text{loss}}\): furnace heat loss (modeled as fraction of \(\dot{Q}{\text{in}}\)).  
- \(\dot{Q}_{\text{rxn}}\): net enthalpy of pyrolysis reactions (endothermic, positive).

- Yield correlations:  
  Use empirical or literature‑based correlations for yields vs temperature, e.g.:

\[
\alpha(T) = a0 + a1 T + a_2 T^2
\]

(similarly for \(\beta(T), \gamma(T)\)), constrained so \(\alpha + \beta + \gamma + \delta = 1\).

4.2 Bloomery furnace model

Treat bloomery as a high‑temperature reducing reactor with partial combustion:

- Conceptual reactions:

1. Carbon oxidation:

\[
\text{C} + \text{O}2 \rightarrow \text{CO}2 \quad (\Delta H_1 < 0)
\]

2. CO formation:

\[
\text{C} + \frac{1}{2}\text{O}2 \rightarrow \text{CO} \quad (\Delta H2 < 0)
\]

3. Iron oxide reduction:

\[
\text{Fe}2\text{O}3 + 3\text{CO} \rightarrow 2\text{Fe} + 3\text{CO}2 \quad (\Delta H3)
\]

- Energy balance:

\[
\sum \dot{m}k hk^{\text{in}} + \dot{Q}{\text{comb}} = \sum \dot{m}l hl^{\text{out}} + \dot{Q}{\text{loss}}
\]

Where:

- \(\dot{Q}_{\text{comb}}\): heat from carbon combustion and syngas firing.  
- Outputs include hot off‑gas (S7), molten metals, slag.

- Key outputs for cascade:

\[
\dot{Q}{\text{bloomery,usable}} = \eta{\text{HX}} \cdot \left( \dot{m}{\text{gas}} c{p,\text{gas}} \Delta T_{\text{gas}} \right)
\]

Where \(\eta_{\text{HX}}\) is heat‑exchanger efficiency.

---

5. Heat‑exchange and integration model

5.1 Ducting and exchangers

Model each heat‑exchange unit as:

\[
\dot{Q} = U A \Delta T_{\text{LM}}
\]

Where:

- \(U\): overall heat‑transfer coefficient.  
- \(A\): heat‑transfer area.  
- \(\Delta T_{\text{LM}}\): log‑mean temperature difference.

Define:

- HX1: Bloomery off‑gas → Pyrolysis furnace wall/coil.  
- HX2: Bloomery off‑gas → feedstock pre‑dryer.  
- HX3: Syngas cooling → condensation train.

5.2 Global integration balance

At steady‑state:

\[
\dot{Q}{\text{bloomery,usable}} + \dot{Q}{\text{syngas,burners}} + \dot{Q}{\text{external}} = \dot{Q}{\text{pyrolysis,required}} + \dot{Q}{\text{drying}} + \dot{Q}{\text{loss,total}}
\]

Solve for \(\dot{Q}_{\text{external}}\) (external fuel requirement) under different scenarios.

---

6. Syngas composition and LHV estimation

6.1 Syngas composition model

Approximate syngas molar composition as function of feedstock and temperature:

- Components: CO, H₂, CH₄, C₂H₄, CO₂, N₂, minor hydrocarbons.  
- Use empirical correlations or literature data for pyrolysis of MSW/plastics/biomass.

6.2 Lower heating value (LHV)

\[
\text{LHV}{\text{syngas}} = \sumi yi \cdot \text{LHV}i
\]

Where:

- \(y_i\): molar fraction of component \(i\).  
- \(\text{LHV}_i\): component LHV (e.g., H₂ ≈ 120 MJ/kmol, CO ≈ 283 MJ/kmol, CH₄ ≈ 802 MJ/kmol).

Total energy flow:

\[
\dot{Q}{\text{syngas}} = \dot{n}{\text{syngas}} \cdot \text{LHV}_{\text{syngas}}
\]

---

7. Loss modeling and efficiency metrics

7.1 Heat loss

Model furnace and duct losses as:

\[
\dot{Q}{\text{loss}} = f{\text{loss}} \cdot \dot{Q}_{\text{in}}
\]

Where \(f_{\text{loss}}\) is a calibrated fraction (e.g., 0.05–0.15).

7.2 Key efficiency metrics

- Thermal efficiency of pyrolysis stage:

\[
\eta{\text{pyro}} = \frac{\dot{Q}{\text{products,chem}}}{\dot{Q}_{\text{in,total}}}
\]

Where \(\dot{Q}_{\text{products,chem}}\) is chemical energy in syngas + pyro‑oil + char.

- Cascade integration efficiency:

\[
\eta{\text{cascade}} = \frac{\dot{Q}{\text{internal,usable}}}{\dot{Q}_{\text{total,required}}}
\]

Where \(\dot{Q}_{\text{internal,usable}}\) is bloomery + syngas energy reused.

- External fuel fraction:

\[
f{\text{external}} = \frac{\dot{Q}{\text{external}}}{\dot{Q}_{\text{total,required}}}
\]

Target: \(f_{\text{external}} \leq 0.15\).

---

8. Simulation scenarios and sensitivity analysis

8.1 Core scenarios

For each feedstock scenario (A, B, C), run:

- Baseline:  
  - Throughput: 50 tons/day.  
  - Pyrolysis temperature: 550 °C.  
  - Bloomery temperature: 1200 °C.  
  - HX efficiency: 0.6.

- High‑throughput:  
  - Throughput: 100 tons/day.  
  - Same temperatures, check if internal energy suffices.

- Low‑efficiency HX:  
  - HX efficiency: 0.4.  
  - Evaluate increase in external fuel.

- High‑moisture:  
  - Moisture +10% vs baseline.  
  - Evaluate drying energy penalty.

8.2 Sensitivity parameters

Vary:

- Pyrolysis temperature (450–700 °C).  
- Bloomery temperature (1100–1300 °C).  
- HX efficiency (0.3–0.7).  
- Feedstock HHV (±20%).  
- Loss fraction (0.05–0.20).

Track:

- \(\dot{Q}_{\text{external}}\).  
- \(\eta_{\text{cascade}}\).  
- Syngas LHV and flow.  
- Bloomery usable heat.

---

9. Outputs and reporting structure

For each simulation run, report:

- Mass balance:  
  - Yields of syngas, pyro‑oil, char, metals, slag [kg/h].  

- Energy balance:  
  - Heat supplied by bloomery, syngas, external fuel [kW].  
  - Heat consumed by pyrolysis, drying, losses [kW].  

- Key metrics:  
  - \(\eta{\text{pyro}}\), \(\eta{\text{cascade}}\), \(f_{\text{external}}\).  
  - Syngas LHV and total energy flow.  
  - Bloomery off‑gas temperature and energy content.

- Feasibility flags:  
  - Whether cascade can run with zero external fuel under given conditions.  
  - Margin to self‑sufficiency (e.g., % shortfall or surplus).

---

10. Recommended next step

Once this thermodynamic simulation spec is instantiated in code or a process simulator (e.g., Aspen, custom Python), the next logical artifact is:

- A control‑system and SCADA architecture that explicitly ties sensor readings (temperatures, gas composition, flow rates) to maintaining the thermodynamic targets: minimal external fuel, stable pyrolysis temperature, and safe off‑gas handling.

If you want, I can draft that SCADA/control‑logic spec next.

SCADA and control architecture for Pyrolysis_Cascade.md
(Version 1.0 — Draft specification)

---

1. Purpose and control philosophy

Goal:  
Maintain thermodynamic self‑sufficiency, stable operation, and regulatory‑compliant emissions by tightly controlling:

- Pyrolysis temperature and atmosphere.  
- Bloomery temperature, reduction conditions, and off‑gas energy.  
- Heat‑exchange performance and syngas routing.  
- Off‑gas scrubbing and stack quality.

Control philosophy:

- Energy‑centric: prioritize internal energy reuse; minimize external fuel.  
- Safety‑first: gas, temperature, and mechanical interlocks override economic optimization.  
- Feed‑forward + feedback: anticipate disturbances (feedstock changes) and correct via PID loops and supervisory logic.  

---

2. Sensor suite and instrumentation

2.1 Pyrolysis furnace

- Temperature:  
  - Sensors: Type K/S thermocouples at multiple axial and radial positions.  
  - Purpose: Maintain target band (e.g., 500–600 °C).

- Pressure:  
  - Sensors: Differential pressure transducers at furnace and off‑gas line.  
  - Purpose: Maintain slight negative pressure (−5 to −20 Pa).

- Gas composition (off‑gas/syngas):  
  - Sensors: Online gas analyzer (CO, CO₂, H₂, CH₄, O₂).  
  - Purpose: Estimate syngas LHV, detect oxygen ingress, control burners.

- Feed rate:  
  - Sensors: Load cells on feed hopper, encoder on auger/ram.  
  - Purpose: Mass flow estimation for mass/energy balance.

2.2 Bloomery furnace

- Temperature:  
  - Sensors: High‑temperature thermocouples in hearth and off‑gas duct.  
  - Purpose: Maintain 1100–1300 °C; ensure off‑gas is hot enough for HX.

- Gas composition:  
  - Sensors: CO/CO₂/O₂ analyzer in off‑gas.  
  - Purpose: Control reduction atmosphere; avoid over‑oxidation.

- Tuyere air/syngas flow:  
  - Sensors: Flow meters (mass or volumetric) on air and syngas lines.  
  - Purpose: Control combustion intensity and atmosphere.

- Slag/metal tapping status:  
  - Sensors: Limit switches, temperature sensors near tap ports.  
  - Purpose: Interlocks for tapping operations.

2.3 Heat‑exchange network

- Inlet/outlet temperatures:  
  - Sensors: Thermocouples on both sides of each HX.  
  - Purpose: Compute ΔT and monitor HX efficiency.

- Flow rates:  
  - Sensors: Flow meters on gas streams through HX.  
  - Purpose: Calculate \(\dot{Q} = \dot{m} c_p \Delta T\).

2.4 Scrubber and stack

- Pressure:  
  - Sensors: ΔP across scrubber stages.  
  - Purpose: Detect fouling or flooding.

- Temperature:  
  - Sensors: Stack and scrubber outlet temperature.  
  - Purpose: Ensure proper condensation and catalyst operation.

- Emissions:  
  - Sensors: Continuous emissions monitoring (CEMS) for particulates, VOCs, SOx/NOx (if required).  
  - Purpose: Regulatory compliance.

---

3. Actuators and controllable elements

3.1 Pyrolysis stage

- Burners (syngas + external fuel):  
  - Actuators: Control valves on fuel lines; burner modulation.  
  - Control: PID on furnace temperature; supervisory limit on external fuel fraction.

- Feed mechanism:  
  - Actuators: Variable‑speed drives on auger/ram.  
  - Control: Throughput setpoint; feed‑forward adjustment based on feed HHV and moisture.

- Off‑gas routing:  
  - Actuators: Diverter valves to HX, flare, or bypass.  
  - Control: Safety logic (flare on high CO/O₂ anomalies).

3.2 Bloomery stage

- Air/syngas injection:  
  - Actuators: Control valves and blower speed.  
  - Control: PID on bloomery temperature and gas composition (CO/O₂ ratio).

- Slag/metal tapping:  
  - Actuators: Mechanized tap doors, hoists.  
  - Control: Interlocked with temperature and operator commands.

3.3 Heat‑exchange and drying

- Gas flow distribution:  
  - Actuators: Dampers and valves in ducting.  
  - Control: Maintain target HX ΔT and drying temperature.

- Feedstock dryer:  
  - Actuators: Fan speed, burner modulation (if auxiliary heat).  
  - Control: PID on outlet moisture/temperature.

3.4 Scrubber

- Pump and fan speeds:  
  - Actuators: VFDs on circulation pumps and induced‑draft fans.  
  - Control: Maintain ΔP and flow setpoints.

- Chemical dosing (if used):  
  - Actuators: Metering pumps.  
  - Control: pH or ORP control loops.

---

4. Control loops (PID and supervisory logic)

4.1 Core PID loops

- Loop L1 — Pyrolysis temperature control:  
  - PV: Average furnace temperature.  
  - CV: Syngas/external fuel burner firing rate.  
  - SP: 550 °C (example).  

- Loop L2 — Pyrolysis pressure control:  
  - PV: Furnace pressure.  
  - CV: Induced‑draft fan speed / off‑gas valve position.  
  - SP: −10 Pa.

- Loop L3 — Bloomery temperature control:  
  - PV: Hearth temperature.  
  - CV: Air/syngas injection rate.  
  - SP: 1200 °C.

- Loop L4 — Bloomery atmosphere control:  
  - PV: CO/O₂ ratio in off‑gas.  
  - CV: Air vs syngas split.  
  - SP: Target reducing ratio (e.g., CO/O₂ > threshold).

- Loop L5 — Dryer outlet temperature/moisture:  
  - PV: Dryer outlet temperature or inferred moisture.  
  - CV: Heat input (gas flow, fan speed).  
  - SP: Temperature corresponding to target moisture (e.g., 15–20%).

- Loop L6 — Scrubber ΔP control:  
  - PV: Pressure drop across scrubber.  
  - CV: Fan speed.  
  - SP: Design ΔP band.

4.2 Supervisory energy‑balance controller

A higher‑level controller uses the thermodynamic model to adjust setpoints:

- Inputs:  
  - Measured syngas LHV and flow.  
  - Bloomery off‑gas temperature and flow.  
  - HX ΔT and efficiency estimates.  
  - External fuel flow.

- Outputs:  
  - Adjust L1/L3 setpoints within safe bands to reduce external fuel.  
  - Reallocate syngas between bloomery burners and pyrolysis burners.  
  - Adjust dryer heat usage based on surplus/deficit energy.

- Objective function:  
  Minimize \( f{\text{external}} = \dot{Q}{\text{external}} / \dot{Q}_{\text{total,required}} \) subject to:

  - Temperature constraints (pyrolysis and bloomery).  
  - Emissions constraints.  
  - Safety constraints (no positive pressure, no oxygen spikes).

4.3 Feed‑forward compensation

When feedstock properties change (e.g., moisture or HHV):

- Detection:  
  - Online moisture measurement or batch lab data.  
  - HHV estimation from composition or historical data.

- Action:  
  - Adjust feed rate, dryer setpoint, and burner SPs before disturbance fully propagates.  
  - Update yield and syngas LHV estimates in the supervisory model.

---

5. Safety interlocks and emergency logic

5.1 Gas safety

- CO/H₂ high alarm:  
  - Action: Immediate diversion of off‑gas to flare; restrict personnel access; increase ventilation.

- O₂ ingress detection (pyrolysis):  
  - Action: Reduce feed, close air leaks, increase induced‑draft fan to maintain negative pressure.

5.2 Thermal safety

- Over‑temperature (pyrolysis or bloomery):  
  - Action: Ramp down burners, reduce feed, open bypass cooling paths if available.

- Refractory over‑stress (rapid ΔT):  
  - Action: Limit rate of temperature change via ramping logic.

5.3 Mechanical safety

- Feed jam detection (torque/position anomalies):  
  - Action: Stop feed drive, reverse briefly, alert operator.

- Tap operation interlocks:  
  - Conditions: Correct temperature range, no conflicting commands, personnel clearance.

5.4 Emergency shutdown (ESD)

- Triggers:  
  - Multiple critical alarms (gas, temperature, pressure).  
  - Loss of power to key safety systems.

- Sequence:  
  1. Divert all combustible gas to flare.  
  2. Stop feed mechanisms.  
  3. Ramp down burners.  
  4. Maintain induced‑draft fans on backup power if possible.  
  5. Log event and lock out restart until manual review.

---

6. SCADA architecture and data model

6.1 System topology

- Field layer: PLCs/RTUs near furnaces, HX, scrubber, dryer.  
- Control layer:  
  - Local PLCs running PID loops.  
  - Central controller running supervisory energy‑balance logic.

- SCADA layer:  
  - HMI for operators (real‑time trends, alarms, setpoints).  
  - Historian for long‑term data storage.  
  - Reporting engine for regulatory and performance reports.

6.2 Tag structure (examples)

Use a structured naming convention:

- PYR.TEMP.AVG — Pyrolysis average temperature.  
- PYR.PRES.FURN — Pyrolysis furnace pressure.  
- PYR.GAS.CO, PYR.GAS.H2 — Syngas composition.  
- BLM.TEMP.HEARTH — Bloomery hearth temperature.  
- BLM.GAS.CO, BLM.GAS.O2 — Bloomery off‑gas composition.  
- HX1.DT, HX1.Q — HX1 ΔT and heat flow.  
- SCR.DP, SCR.STACK.VOC — Scrubber ΔP and stack VOC.  
- SYS.QEXTERNAL, SYS.ETACASCADE — External fuel heat and cascade efficiency.

6.3 Data logging and analytics

- Sampling rate:  
  - Fast loops (temperatures, pressures): 1 Hz or faster.  
  - Composition analyzers: per analyzer capability (e.g., 0.1–0.2 Hz).

- Historian:  
  - Store all key tags with timestamps.  
  - Retention: multi‑year for performance and regulatory audits.

- Analytics:  
  - Daily/weekly energy‑balance reports.  
  - External fuel fraction trends.  
  - Alarm statistics (frequency, duration, root‑cause tagging).

---

7. Integration with thermodynamic simulation

7.1 Model‑based setpoint optimization

- Use the thermodynamic model (from your previous spec) as a digital twin:

  - Input: current measured state (temperatures, flows, compositions).  
  - Output: recommended setpoints for L1–L6 and syngas routing to minimize external fuel.

- Run optimization periodically (e.g., every 5–15 min) and apply changes gradually (ramp limits).

7.2 Calibration and model updating

- Compare simulated vs measured:

  - Syngas yields and LHV.  
  - Bloomery usable heat.  
  - HX efficiencies.

- Adjust model parameters (yield coefficients, loss fractions, U·A values) to reduce error.

---

8. Next artifacts

You now have:

- Engineering spec (Pyrolysis_Cascade.md).  
- Thermodynamic simulation spec.  
- SCADA/control architecture spec.

Next logical documents could be:

- Air_Scrubber.md — detailed scrubber design and control.  
- Materials_Separation.md — char/metal/slag handling and quality specs.  
- Economic_Model.md — formalized financial and throughput model.

If you tell me which of those matters most for your current governance stack, we can draft it in the same style.


