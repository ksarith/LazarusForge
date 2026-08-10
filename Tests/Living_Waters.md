# Living_Waters.md
*Tests/Living_Waters.md*

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field | Value |
|---|---|
| Status | Exploration |
| Body Stability | Volatile |
| Spec Gates | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Last Audit | 2026-07-30 |
| Auditor | James (Owner), Claude (Synthesizer), Gemini (Auditor), ChatGPT (Synthesizer), Grok (Synthesizer); 2026-07-30 — ASM-004 / AWG energy band softened, arid sorption+waste-heat preference noted, Solar Descent heat interface reciprocal text added (Synthesizer) |
| Open Unknowns | 9 |
| Active Disputes | 0 |
| Highest Risk | Critical — LW-UNK-001 (volatile co-distillation) and LW-UNK-003 (lumen implosion) both carry immediate safety consequences if bypassed |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Legacy cross-reference fields (retained for continuity):**

| Field | Value |
|---|---|
| Version | v0.4 |
| Depends On | Energy.md, Safety_Protocols.md, Unknowns.md, Economics.md |
| Feeds Into | Operations/ (pending validation) |

---

## Scope Boundary

**This file DOES define:**
- The Living Waters Initiative's four separation mechanisms (thermal, pressure, phase change, chemical/biological) and the ten experimental pathways built on them (LW-001 through LW-010).
- The Water Hierarchy tiering purification effort to intended use.
- Site-conditioned pathway selection guidance.
- Sequencing doctrine (purification before atmospheric harvesting).
- Promotion criteria for partial advancement of individual pathways to Operations/.

**This file DOES NOT define:**
- Power sourcing engineering specifications for pumps, compressors, or thermal inputs (see `Energy.md`).
- PPE and handling doctrine for contaminated streams (see `Safety_Protocols.md`).
- Marine deployment ethical/environmental impact assessment or brine disposal doctrine (see `Ethical_Constraints.md`).
- Resource valuation of recovered salt and minerals (see `Economics.md`).
- A formal Site Characterization → Pathway Selection decision framework — declared future work, not yet written (LW-UNK-008).

---

## File Purpose

The Living Waters Initiative explores methods of producing potable and process water from contaminated, saline, atmospheric, or waste streams.

This file lives in Tests/ because neither primary pathway has been validated at Forge scale. Assumptions are not permitted to harden into doctrine until experimental data supports promotion to Operations/.

The initiative investigates pressure-driven, thermal, biological, and electrochemical separation approaches while preserving compatibility with Forge philosophy:

- Salvage-first.
- Energy-aware.
- Scalable from household to distributed network operation.
- Resilient under degraded conditions.
- Favoring repairability over consumable dependence.

**Declared Trajectory:** Living Waters is intended to evolve into the hydrological counterpart to Energy.md — eventually covering purification, storage, atmospheric harvesting, wastewater recycling, mineral recovery, biological treatment, and closed-loop water architecture. This file is the seed of that scope, not its ceiling.

**Sequencing Doctrine:** Purification precedes moisture farming. Atmospheric harvesting brings in variable-quality input streams — microplastics, industrial residues, biological aerosols. A validated purification baseline must exist before atmospheric yields can be safely processed. Moisture farming is supplemental until that baseline is established.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Purification must precede atmospheric harvesting because condensate carries airborne contaminants that require treatment before closed-loop storage | Sequencing Doctrine, stated design philosophy | Medium | An arid-context deployment demonstrates safe direct-to-storage harvesting without a purification baseline |
| ASM-002 | Ambient hydrostatic pressure at 400–600 m depth can substitute for mechanical high-pressure pumps in reverse osmosis (LW-003) | Flux model $J = A(\Delta P - \Delta\pi)$; osmotic pressure of seawater (~2.7 MPa) compared against hydrostatic pressure at depth | Low — theoretical, no empirical validation yet | LW-TEST-301/302/304 completed |
| ASM-003 | Vacuum distillation (LW-001) is energy-unviable without heat recycling, making Mechanical Vapor Recompression or multi-effect design a hard design requirement, not an optimization | Stated energy figures: ~628 kWh/m³ without recycling vs. 10–25 kWh/m³ with MVR | Medium — figures are Analogous/literature-derived, not Forge-measured | LW-TEST-101 (MVR Efficiency) completed |
| ASM-004 | Active refrigeration AWG can approach ~0.8–1.5 kWh/L under warm, high-RH conditions with good hardware; arid and mixed climates are substantially worse (often ~2–6+ kWh/L). The older commercial marketing band of 0.3–0.5 kWh/L at >70% RH is a best-case ceiling, not a Forge planning baseline — especially with salvaged compressors (COP degraded vs new). | Peer-tested residential/commercial AWG ranges + OEM best-case claims; salvage COP penalty explicit | Low — planning band only until measured | LW-TEST-502 (Energy Intensity Validation) completed across RH/T matrix |
| ASM-005 | Local relative-humidity reduction from atmospheric harvesting (LW-005a) is a plausible secondary effect but not a design target, and no atmospheric-scale claim is intended | Explicit scope limitation in LW-005a; consistent with this file's DOES NOT define atmospheric-scale effects | High — this is a scope decision, not an empirical claim | Body content proposes atmospheric-scale effects as a design objective (would itself be a Drift Indicator trigger) |

---

## Body

### Governing Principle

Water purification is fundamentally the separation of water molecules from everything else.

The Forge recognizes four major separation mechanisms:

| Mechanism | Separation Driver |
|---|---|
| Thermal | Boiling and condensation |
| Pressure | Vacuum or membrane gradients |
| Phase Change | Freezing, evaporation, sublimation |
| Chemical / Biological | Adsorption, ion exchange, metabolism |

**Unifying Observation:** LW-001 and LW-003 share a common underlying principle — changing pressure changes the phase behavior of water. This suggests a broader category: **Pressure-Driven Water Separation**. Nature provides atmospheric pressure, vacuum, and hydrostatic pressure. Civilization normally adds pumps to create pressure differentials. Living Waters investigates whether naturally occurring pressure environments can substitute for mechanical complexity.

---

### Water Hierarchy

The Forge recognizes that not all water requires drinking quality. Producing unnecessarily pure water for low-grade uses is avoidable energy expenditure. Quality requirements must match intended use.

| Tier | Use | Purity Requirement |
|---|---|---|
| 1 | Potable / drinking | Highest — pathogen and contaminant free |
| 2 | Food preparation | High |
| 3 | Hygiene | Moderate |
| 4 | Process water | Application-dependent |
| 5 | Cooling water | Low — scaling and corrosion control only |
| 6 | Irrigation | Low — pathogen aware |
| 7 | Non-contact utility | Minimal |

This hierarchy parallels the degraded modes logic in Energy.md. Purification effort scales to use. Potable-grade production is reserved for potable-grade need.

---

### Site Context

**The answer for different Forges will naturally vary. Location is the key determination.**

Pathway selection is site-conditioned, not universal. A Forge that knows where it is can focus experimental resources on viable pathways and flag inapplicable ones without wasting test cycles.

| Site Condition | Favored Pathways | Notes |
|---|---|---|
| Coastal / ocean access | LW-003 (DSRO), LW-001 | Primary candidates. Depth and seawater availability. |
| Inland / surface water | LW-001, LW-004, LW-006 | Contaminated rivers, aquifers, industrial runoff. |
| Arid / desert | LW-005 accelerated, LW-001 | Moisture farming pressure higher; purification baseline still first. |
| Arctic / cold climate | LW-004 competitive as primary | Freeze separation viable where energy is scarce and cold is abundant. |
| High waste-heat availability | LW-006, LW-008 | Membrane distillation and multi-effect distillation benefit directly. |
| Dense salvage environment | LW-001 | Refrigeration compressors, condensers, pressure vessels most recoverable. |

**Site Characterization Inputs (pre-pathway selection):**
- Proximity to ocean, surface water, or groundwater.
- Climate zone and seasonal variation.
- Elevation and atmospheric pressure baseline.
- Salvage availability and component inventory.
- Energy profile (see Energy.md).
- Known contaminant classes in local water sources.

*A formal Site Characterization → Pathway Selection decision framework is a declared future addition to this file.*

---

### Experimental Pathways

#### LW-001 — Vacuum Distillation

**Concept**

Reducing chamber pressure lowers water's boiling point. At sufficiently low pressure, evaporation occurs at ambient temperatures. The resulting vapor is condensed into purified water, leaving dissolved solids and most contaminants behind.

**Advantages**
- Removes salts and heavy metals.
- Compatible with low-grade or waste heat.
- Works with seawater and heavily contaminated sources.
- Tolerant of salvaged components.
- No chemical inputs required.

**Challenges**
- Vacuum pump durability under sustained operation.
- Seal integrity — micro-leak accumulation degrades vacuum depth over time.
- **Volatile co-distillation [CRITICAL]:** Low-boiling organics (fuels, solvents, benzene, ethanol, gasoline fractions, some biological metabolites) will co-distill with or ahead of water vapor under vacuum. In salvage-context sources where input stream composition is unpredictable, initial distillate may be a concentrated toxin stream, not potable water. Fractional staging is required. See LW-UNK-001 and LW-TEST-102.
- **Energy cost [CRITICAL]:** Without latent heat recycling, vacuum distillation consumes approximately 628 kWh/m³ — the full latent heat of vaporization. This is unviable for the Forge energy budget. Heat recycling is not optional; it is a design requirement. See LW-UNK-005 and LW-TEST-101.
- Scaling behavior unknown.

**Energy Profile**

| Configuration | Specific Energy Consumption |
|---|---|
| No heat recycling | ~628 kWh/m³ — **unviable** |
| With Mechanical Vapor Recompression (MVR) or Multi-Effect Design | 10–25 kWh/m³ |
| Surface RO baseline (industrial, with energy recovery) | 2.5–4.0 kWh/m³ |
| Surface RO (salvaged pump, no energy recovery) | 8–12 kWh/m³ |

LW-001 with MVR is less efficient than industrial RO but may be more achievable from salvage. The energy gap narrows further when waste heat is available as input.

**Potential Salvage Components**
- Refrigeration compressors (vacuum source and MVR).
- Stainless pressure vessels.
- Automotive condensers.
- Solar thermal collectors (low-grade heat input).

**Volatile Fractionation Staging**

Input streams containing VOCs require a two-stage decompression cycle:

```
[Contaminated Feed]
      ↓
[Stage 1 — Mild Vacuum ~10–15 kPa]
      → VOC vapor → Reject / fuel storage line
      ↓
[Stage 2 — Deep Vacuum <4.5 kPa]
      → Water vapor → Condenser → Potable output
```

Stage 1 strips high-volatility compounds before water recovery begins. This prevents distillate contamination without chemical consumables.

**Proposed Test Parameters**
- **LW-TEST-101 (MVR Efficiency):** Measure compressor electrical input against volumetric output. Reject configurations exceeding 25 kWh/m³.
- **LW-TEST-102 (Volatile Fractionation):** Validate two-stage decompression cycle. Stage 1 (~10–15 kPa) strips volatiles to waste/fuel line. Stage 2 (<4.5 kPa) recovers water. Confirm fractionation valve presence and first-stage rejection routing.
- **LW-TEST-103 (Seal Degradation Tolerance):** Simulate micro-leak at +0.5 kPa/hr. Establish failure threshold at which boiling ceases and thermal input would be required.
- **LW-TEST-104 (Latent Heat Recycling):** Validate that condensation heat is routed back to pre-heat incoming feed-water.

**Status:** Experimental — No design assumptions permitted.

---

#### LW-002 — Conventional Reverse Osmosis

**Concept**

Pressure forces water through a semi-permeable membrane while rejecting dissolved salts and contaminants.

**Advantages**
- Mature, well-documented technology.
- High throughput.
- No phase change energy losses.

**Challenges**
- Membrane fouling and consumable dependence conflict with Forge repairability doctrine.
- High mechanical pressure requirements (5.5–7.0 MPa for seawater).
- Less compatible with salvage sourcing than LW-001 or LW-003.

**Status:** Reference pathway. Included as comparative baseline. Not a primary Forge candidate without membrane sourcing solution. See LW-UNK-006.

---

#### LW-003 — Pressure-Assisted Deep Water Osmosis (DSRO)

**Concept**

The ocean contains enormous ambient hydrostatic pressure. At depth:

| Depth | Approximate Pressure |
|---|---|
| 100 m | ~10 bar (1.0 MPa) |
| 300 m | ~30 bar (3.0 MPa) |
| 500 m | ~50 bar (5.0 MPa) |
| 1000 m | ~100 bar (10.0 MPa) |

Osmotic pressure of seawater is approximately 2.7 MPa. At 300–500 m depth, ambient hydrostatic pressure exceeds osmotic pressure without mechanical pumping. The energy cost shifts from pressurizing feed-water to lifting product water to the surface — significantly lower.

**Research Question:** Can ambient hydrostatic pressure substitute for mechanical high-pressure pumps in reverse osmosis?

**Flux Model**

`J = A(ΔP − Δπ)`

Where A is membrane permeability, ΔP is hydrostatic pressure differential, and Δπ is osmotic pressure differential. Target deployment window: 400–600 m depth, where ΔP reliably exceeds Δπ without excessive membrane compaction risk.

**Lift Energy Note**

The freshwater lumen interior is at or near atmospheric pressure. If osmotic flux generates sufficient internal head pressure, product water rises partway or fully to the surface without high-pressure pumping — requiring only a low-pressure surface skim pump. This is a significant energy advantage over surface RO that requires explicit validation.

**Advantages**
- Major reduction in energy input vs. surface RO.
- Consistent feedwater quality (cold, low-organics, low-algae at depth).
- No high-pressure pump infrastructure required.

**Challenges**
- Membrane survivability at sustained depth pressure.
- Biofouling at the membrane surface.
- **Lumen implosion risk [CRITICAL]:** At 500 m depth, exterior hydrostatic pressure is ~5.0 MPa. Interior freshwater lumen is at ~0.1 MPa atmospheric. Net crushing load: ~4.9 MPa. Standard PVC and thin-walled salvage tubing will implode. Salvage targets: HDPE SDR-9 pipe, thick-walled steel tubing, or hydraulic hose sleeves rated for >5.5 MPa external crush load. See LW-UNK-003 and LW-TEST-301.
- Recovery and maintenance logistics at depth.
- Mooring and tether management.
- Brine disposal and marine impact unknown.

**External Reference:** Flocean-style submerged RO systems have explored this concept as prototypes. Treat as observational only — compatibility with Forge salvage and repairability doctrine has not been assessed.

**Proposed Test Parameters**
- **LW-TEST-301 (Crush Depth Simulation):** Calculate and test implosion threshold of freshwater conduit. Minimum structural rating: >5.5 MPa external load at target deployment depth.
- **LW-TEST-302 (Osmotic Equilibrium Depth):** Verify deployment depth held strictly between 400–600 m. Below 600 m risks membrane compaction; above 400 m risks insufficient ΔP margin.
- **LW-TEST-303 (Biofouling and Flow Decay):** Measure flux decay over simulated time blocks. Establish maintenance interval and evaluate acoustic anti-fouling pulse cycle effectiveness.
- **LW-TEST-304 (Lift Energy Characterization):** Measure actual pumping energy required to surface product water. Validate whether passive artesian rise reduces or eliminates surface pump requirement.

**Status:** Unknown / Experimental — No design assumptions permitted.

---

#### LW-004 — Freeze Separation

**Concept**

Ice formation preferentially excludes dissolved salts and many contaminants. Repeated freeze-thaw cycles progressively concentrate contaminants in the liquid phase while producing cleaner ice.

**Advantages**
- Low complexity.
- No membrane consumables.
- In arctic or cold-climate Forges, ambient cold substitutes for refrigeration energy — potentially making this a primary rather than supplemental pathway.

**Challenges**
- Slow cycle times.
- Multiple cycles required for meaningful purification.
- Contaminant carryover in ice crystal boundaries.
- Limited throughput in temperate climates.

**Status:** Supplemental in temperate contexts. Primary candidate in arctic / cold-climate Forges.

---

#### LW-005 — Atmospheric Water Harvesting

**Concept**

Capture of water vapor from ambient air via:
- Passive radiative cooling and condensation.
- Desiccant adsorption/desorption cycles.
- Fog net interception.
- Active refrigeration condensation (see LW-005a).

**Constraint**

Atmospheric harvesting is supplemental until a reliable purification baseline exists. Harvested condensate carries airborne contaminants — microplastics, industrial aerosols, biological particulates — and requires treatment before entering closed-loop storage. In arid Forges where no surface water exists, sequencing pressure may force earlier deployment; purification integration must be planned from the start in those cases.

**Status:** Supplemental — dependent on LW-001 or LW-003 validation first. May be accelerated in desert-context Forges.

**Climate-conditioned method preference (planning, not Spec)**

| Climate class | Prefer | Deprioritize as primary |
|---|---|---|
| Warm / humid (high absolute humidity) | Active refrigeration AWG (LW-005a) | Large passive-only fields |
| Temperate seasonal | Seasonal LW-005a + storage; expect weak winter yield | Year-round intensity claims |
| Arid / low RH | **Sorption (desiccant / hydrogel) cycled with solar or low-grade waste heat**; radiative dew as area-limited supplement | Pure vapor-compression AWG as main water source |

Active refrigeration remains the primary **humid-site** salvage path (compressors and coils are abundant). In arid Forges, refrigeration energy intensity rises sharply while yield falls — sorption regenerated by **solar thermal or process/Solar Descent waste heat** is the preferred architectural direction until measured otherwise. Desiccant cycles are already named under LW-005 Concept; they are not yet a detailed sub-pathway equivalent to LW-005a.

**Interface — Solar Descent / low-grade heat (reciprocal)**

- `Tests/Solar_Descent.md` owns thermal energy delivery up to a heat-exchanger or desorption interface (waste-heat quality and availability).
- This file owns water-side use of that heat: (1) boosting or replacing electrical load on active AWG where useful, (2) **regenerating sorption beds** for arid atmospheric harvesting, (3) any shared treatment of condensate once produced.
- Neither file may unilaterally redefine the other's side of the boundary. Empirical coupling (temperatures, duty cycle, which tier of SD cascade feeds which LW use) remains unvalidated — declared synergy only.

---

#### LW-005a — Refrigeration-Based Atmospheric Condensation (Active AWG)

**Concept**

Forced humid air across a chilled heat exchanger surface causes water vapor to condense. Unlike passive methods, active refrigeration provides reliable condensation independent of ambient radiative conditions. This is the highest-yield atmospheric pathway under high-humidity conditions and the most compatible with salvage-sourced components.

This sub-pathway was developed from iterative design work across two implementation forms:
- **Vertical downward-venting units** — freestanding, centralized refrigeration, higher output density.
- **Fence-mounted distributed units** — modular deployment along fence lines, solar or grid powered.

The vertical unit architecture is the primary Forge candidate due to greater compatibility with salvaged components and centralized refrigeration efficiency.

**Vertical Unit Architecture (Primary)**

Five-unit array, each unit 1–1.5 m tall, designed for deployment in a defined perimeter area.

*Per unit:*
- Inner core: 5–8 cm diameter aluminum mesh tube with helical impeller or static vanes producing vortex airflow.
- Outer heat exchanger: 20–25 cm diameter tube with copper coils or plates (~2.5–3 m² surface area), enhanced with crinkled aluminum foil and fins, hydrophobic coated.
- Airflow: Top-mounted angled fans (0.1–0.2 m³/s per unit) driving humid air downward through core and across chilled surface.
- Cooling: Centralized 5–7 kW vapor-compression refrigeration unit (target COP 3–4) chilling circulating water to 5–10°C, keeping heat exchanger surface at 10–15°C.
- Heat rejection: Single vertical shaft (20–30 cm diameter) with blower venting condenser heat upward.
- Ionization: High-voltage DC enhancement (+20–25 kV on core, −15 to −20 kV on tube surface) to improve droplet nucleation. See shared electrical architecture note below.
- Collection: Condensate drains to bottom trays and collects in tanks or buckets.

*Proposed performance parameters (unvalidated — empirical testing required):*

| Parameter | Proposed Value | Confidence |
|---|---|---|
| Condensate per unit | 4.5–10 L/hour | Low — modeling estimate |
| Power per unit | 0.37–0.75 kW | Low — modeling estimate |
| Energy intensity | ~0.8–1.5 kWh/L humid planning; ≥2–3 kWh/L mixed; ≥3–6 kWh/L arid (until measured) | Low — literature/field band; 0.3–0.5 kWh/L is best-case OEM ceiling only |
| Five-unit array total | 22.5–50 L/hour | Low — unvalidated aggregate |
| Local RH reduction (2000 ft² area) | 70% → 40–50% | Very Low — modeling only; atmospheric dynamics unconfirmed |

**Note on energy intensity:** Marketing figures of 0.3–0.5 kWh/L apply only under favorable warm, high-RH conditions with good new hardware. Independent tests of residential-scale units more often fall in roughly **0.8–3+ kWh/L**, with arid operation much worse. For Forge planning, treat **~1–2 kWh/L (humid)** and **≥3 kWh/L (dry)** as working assumptions until LW-TEST-502 measures salvaged refrigeration COP and full-system kWh/L. Do not size energy systems against the 0.3–0.5 band.

**Note on RH reduction claim:** Local humidity reduction in a bounded area is plausible as a secondary effect but is not a design target for this pathway. Water production is the Forge-relevant objective. Atmospheric-scale effects are out of scope at current development interval.

**Fence-Mounted Variant (Alternative Deployment)**

Two form factors developed:
- *2 ft solar unit:* 24" × 10" × 7", 5–7 lbs, 10–15W solar, 110–230 CFM airflow, ~3–4.5 kg/hour output. Cost target: $650–$900 new manufacture.
- *8 ft rollable grid unit:* 96" × 10" × 1" unrolled, 15–20 lbs, 120V grid → 24V DC (14–22W), 90–180 CFM, ~6–9 kg/hour output. Cost target: $700–$925 new manufacture.

**Forge compatibility assessment:** Fence-mounted units assume new manufacture at defined cost targets. This conflicts with salvage-first doctrine. These variants are noted as reference designs for context; they are not primary Forge build candidates unless component sourcing from salvage can be demonstrated. See LW-UNK-009.

**Shared Electrical Architecture Note**

The high-voltage ionization system in LW-005a (+20–25 kV DC) uses the same general electrode configuration as the ionization enhancement explored in LW-001 (vacuum distillation volatility management). A shared high-voltage supply architecture may be feasible across both pathways where both are deployed. This is a declared synergy candidate, not a confirmed design.

**Salvage Component Targets**
- Vapor-compression refrigeration unit: commercial refrigeration compressors (abundant in salvage stream).
- Copper coils: HVAC evaporator coils, refrigerator evaporators.
- Aluminum fins and mesh: window AC units, salvaged heat exchangers.
- Fans: salvaged computer server fans, HVAC blower assemblies.
- High-voltage supply: salvaged neon sign transformers, flyback transformers (requires qualification).
- Sorption media (arid path): silica gel, zeolite beds, or improvised hygroscopic salts from industrial salvage — regeneration heat from solar thermal or Solar Descent / process waste heat; not a substitute for measured cycle design.

**Proposed Test Parameters**
- **LW-TEST-501 (Condensation Rate vs. RH):** Measure actual condensate output per unit at varying ambient humidity levels. Establish minimum viable RH threshold for positive water yield.
- **LW-TEST-502 (Energy Intensity Validation):** Measure kWh consumed per liter produced across humidity and temperature range. Compare against 0.3–0.5 kWh/L commercial benchmark.
- **LW-TEST-503 (Ionization Enhancement Delta):** Measure condensate yield with and without HV ionization active. Quantify improvement or confirm negligible effect at this scale.
- **LW-TEST-504 (Salvage Component COP):** Measure actual COP of salvaged refrigeration compressor in this configuration. Reject configurations below COP 2.0 as energy-unviable.
- **LW-TEST-505 (Condensate Quality):** Test condensate for airborne contaminants — particulates, biological matter, VOCs. Confirm purification requirements before potable use classification.

**Status:** Exploratory — proposed parameters unvalidated. Salvage compatibility partially confirmed by component availability. Empirical testing required before yield claims can be made.

---

#### LW-006 — Membrane Distillation

**Concept**

Combines heat gradients with hydrophobic membranes to transport water vapor while rejecting liquid-phase contaminants.

**Potential Synergies**
- Solar thermal heat input.
- Waste heat from Forge operational systems.
- Biogas combustion byproduct heat.

**Status:** Exploratory. Synergy potential with existing Forge thermal systems warrants further investigation. See LW-008 for multi-effect extension.

---

#### LW-007 — Forward Osmosis

**Concept**

Uses osmotic concentration gradients rather than high-pressure pumps to draw water across a semi-permeable membrane into a concentrated draw solution. The draw solution is subsequently regenerated to release purified water.

**Advantages**
- Lower mechanical stress than pressure-driven RO.
- Lower energy requirements at the membrane stage.
- Potential synergy with solar regeneration of draw solution.

**Challenges**
- Draw solution regeneration adds process complexity.
- Regeneration energy cost must be accounted for in full system balance.
- Salvage-compatible draw solution chemistry not yet identified.

**Status:** Exploratory — draw solution regeneration is the key unknown before test design is possible.

---

#### LW-008 — Multi-Effect Vacuum Distillation

**Concept**

A direct descendant of LW-001. Rather than wasting condensation heat from a single distillation stage, successive stages operate at progressively lower pressures. Each stage uses the latent heat released by the previous stage's condensation to drive the next stage's evaporation.

**Advantages**
- Substantially improved energy efficiency over single-effect LW-001.
- Compatible with waste heat input at the first effect.
- Strong synergy with Energy.md thermal management.
- Reduces MVR compressor dependency.

**Relationship to LW-001**

LW-001 must be validated first. LW-008 is the efficiency evolution of a proven concept, not an independent research track.

**Status:** Declared future pathway. Dependent on LW-001 validation.

---

#### LW-009 — Constructed Wetlands / Biological Polishing

**Concept**

Uses microbial action, plant uptake, and sedimentation in engineered wetland systems for wastewater recovery and secondary treatment.

**Advantages**
- Very low energy requirement.
- Resilient and self-repairing under normal operating conditions.
- No membrane consumables.
- Produces biomass as secondary output.

**Challenges**
- Pathogen control — biological systems require monitoring.
- Seasonal variation in treatment efficiency.
- Land area requirements.
- Not suitable as primary purification for heavily contaminated streams.

**Role in Closed Loop**

LW-009 is a polishing and recovery stage, not a primary purification pathway. It belongs downstream of LW-001 or LW-003, processing secondary effluent and returning treated water to the irrigation or process tier.

**Status:** Exploratory — most applicable to Forges with available land and an established primary purification stage.

---

#### LW-010 — Mineral Recovery

**Concept**

Purification processes produce brine and concentrate streams as waste. LW-010 treats these as feedstock rather than disposal problems.

**Potential Outputs (location-dependent)**
- Sodium chloride (table salt, preservation, chemical feedstock).
- Magnesium compounds.
- Gypsum.
- Lithium-bearing brines (specific geological contexts).
- Calcium and potassium salts.

**Relationship to Economics.md**

Brine-as-resource transforms a waste disposal problem into a production line. The economic value is site-dependent and must be assessed against local market and barter conditions. See Economics.md.

**Status:** Exploratory — dependent on primary purification pathway producing consistent brine output.

---

### Long-Term Vision

```
Water Source
      ↓
Site Characterization (input stream typing, location context)
      ↓
Pathway Selection (site-conditioned)
      ↓
Purification (primary pathway)
      ↓
Biological Polishing (LW-009, where applicable)
      ↓
Storage
      ↓
Monitoring
      ↓
Reuse / Redistribution (tiered by Water Hierarchy)
      ↓
Recovery (wastewater as feedstock → LW-009 → LW-010)
      ↓
Mineral Recovery (LW-010)
```

Living Waters ultimately seeks a closed-loop water architecture where:

- Wastewater becomes feedstock.
- Salt becomes recoverable resource.
- Humidity becomes reservoir.
- Reliability exceeds abundance.

**Four-Domain Observation:** Energy and water are tightly coupled. Energy produces water. Water stores and transports heat. Water enables biology. Biology produces waste streams. Waste streams become feedstock. Living Waters, Energy.md, and future files covering atmosphere and biology may form four major resource domains around which the rest of the Forge organizes. This is a declared long-horizon observation, not a current commitment.

---

### Promotion Criteria

This file may be considered for partial promotion to Operations/ when:

1. At least one primary pathway (LW-001 or LW-003) has produced validated purification output at bench or pilot scale.
2. LW-UNK-001 (volatile co-distillation) has been characterized and a safe operating envelope defined.
3. Energy budget for the validated pathway has been documented against Forge operational constraints in Energy.md.
4. A salvage-compatible component list for the validated pathway has been confirmed.
5. Water Hierarchy has been applied — purification target tier is specified, not assumed to be Tier 1 for all uses.

Promotion is partial and pathway-specific. Unvalidated pathways remain in Tests/.

---

### Cross-References

- `Energy.md` — Power sourcing for vacuum pumps, thermal inputs, MVR compressors, and product water lifting.
- `Safety_Protocols.md` — PPE and handling doctrine for contaminated input streams and VOC rejection staging.
- `Unknowns.md` — LW-UNK entries pending migration.
- `Ethical_Constraints.md` — Governs marine deployment impact assessment for LW-003; brine disposal doctrine.
- `Economics.md` — Resource valuation of recovered salt and mineral byproducts (LW-010).

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — no LW-TEST has been physically executed | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

*Full sidecar conversion, 2026-07-12 — prior format was a flat ID/Description/Status table, self-labeled "candidates for migration to Unknowns.md pending triage." Converted to the standard per-entry format below; Unknowns.md global index registration remains a separate, not-yet-completed step (see Resolution Log).*

### LW-UNK-001 — Volatile co-distillation characterization for LW-001

| Field | Value |
|---|---|
| Status | Open (Partially Addressed) |
| Risk | Critical |
| Priority | Blocking |
| Type | Technical / Safety |
| Blocking | Yes — Promotion Criteria #2 names this unknown explicitly |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Low-boiling organics (fuels, solvents, benzene, ethanol, gasoline fractions, some biological metabolites) will co-distill with or ahead of water vapor under vacuum in LW-001. In salvage-context sources where input composition is unpredictable, initial distillate may be a concentrated toxin stream rather than potable water.

**Why It Matters:** This is flagged [CRITICAL] in the pathway description itself — bypassing it produces a system that appears to make water while actually concentrating toxins into the output stream. Directly implicates the Ethical Anchor if deployed without resolution.

**Resolution Path:** LW-TEST-102 (Volatile Fractionation) defines the two-stage decompression cycle test approach — Stage 1 (~10–15 kPa) strips volatiles to a reject/fuel line, Stage 2 (<4.5 kPa) recovers water. Empirical validation of the fractionation valve and first-stage rejection routing is pending.

---

### LW-UNK-002 — Membrane survivability for LW-003 at sustained operational depth

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Blocking |
| Type | Technical |
| Blocking | Yes — LW-003 cannot be validated without a membrane rated for sustained depth pressure |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Whether an available membrane can survive sustained operation at the 400–600 m target deployment window without excessive compaction or failure is untested.

**Why It Matters:** LW-003's entire energy-advantage case depends on operating in a narrow depth band where ambient hydrostatic pressure exceeds osmotic pressure without excessive compaction risk. A membrane that fails at depth invalidates the pathway's core proposition.

**Resolution Path:** LW-TEST-302 (Osmotic Equilibrium Depth) — verify deployment depth held strictly within 400–600 m and characterize membrane behavior across that band.

---

### LW-UNK-003 — Lumen structural integrity limits for LW-003 freshwater conduit

| Field | Value |
|---|---|
| Status | Open (Partially Addressed) |
| Risk | Critical |
| Priority | Blocking |
| Type | Technical / Safety |
| Blocking | Yes |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** At 500 m depth, net crushing load on the freshwater lumen is approximately 4.9 MPa (5.0 MPa exterior hydrostatic vs. ~0.1 MPa interior atmospheric). Standard PVC and thin-walled salvage tubing will implode. Flagged [CRITICAL] in the pathway text.

**Why It Matters:** Lumen implosion at depth is both an equipment-loss and a recovery-logistics hazard — this isn't a performance shortfall, it's a structural failure mode with direct safety consequences.

**Resolution Path:** Implosion threshold has been calculated (salvage targets identified: HDPE SDR-9 pipe, thick-walled steel tubing, hydraulic hose sleeves rated >5.5 MPa external crush load). LW-TEST-301 (Crush Depth Simulation) will validate this empirically. Salvage material validation against the calculated threshold is the remaining gap.

---

### LW-UNK-004 — Biofouling rate characterization for LW-003

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No — affects maintenance interval, not core validation |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Biofouling rate at the membrane surface in target deployment zones is uncharacterized.

**Why It Matters:** Determines maintenance interval and whether acoustic anti-fouling pulse cycling is necessary for sustained operation.

**Resolution Path:** LW-TEST-303 (Biofouling and Flow Decay) — measure flux decay over simulated time blocks, establish maintenance interval, evaluate acoustic anti-fouling pulse cycle effectiveness.

---

### LW-UNK-005 — Energy balance: LW-001 with MVR vs. LW-002 surface RO

| Field | Value |
|---|---|
| Status | Open (Partially Addressed) |
| Risk | High |
| Priority | Blocking |
| Type | Technical |
| Blocking | Yes — Promotion Criteria #3 requires documented energy budget against Forge operational constraints |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** LW-001 is flagged [CRITICAL] on energy cost — without heat recycling it consumes ~628 kWh/m³, versus 10–25 kWh/m³ with MVR and 2.5–4.0 kWh/m³ for industrial RO baseline. Whether MVR-equipped LW-001 is energy-competitive with surface RO at equivalent throughput, specifically using salvaged components, is not yet validated.

**Why It Matters:** Determines whether LW-001 is a viable primary pathway at all, or only viable in narrow contexts (e.g., high waste-heat availability).

**Resolution Path:** LW-TEST-101 (MVR Efficiency) — measure compressor electrical input against volumetric output; reject configurations exceeding 25 kWh/m³. Energy profiles are established from literature/Analogous sources; Forge-scale empirical validation is the remaining gap.

---

### LW-UNK-006 — Salvage-compatible membrane sourcing for any RO pathway

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical / Sourcing |
| Blocking | No — LW-002 is a reference/comparative pathway, not a primary candidate; does not block LW-001 or LW-003 |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** No confirmed salvage-compatible membrane source has been identified for reverse-osmosis-family pathways (LW-002, LW-003, LW-007).

**Why It Matters:** LW-002 is explicitly held as "not a primary Forge candidate without membrane sourcing solution" — this unknown is the reason that pathway stays a reference baseline rather than an active candidate.

**Resolution Path:** Not yet defined — requires a salvage stream survey for membrane-bearing salvaged equipment (water filtration units, medical dialysis equipment, existing RO systems).

---

### LW-UNK-007 — Draw solution regeneration chemistry and energy cost for LW-007

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No — LW-007 is Exploratory, not a primary pathway |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Forward osmosis (LW-007) requires draw solution regeneration to release purified water; no salvage-compatible draw solution chemistry has been identified, and regeneration energy cost is unaccounted for.

**Why It Matters:** This is the key unknown blocking test design for LW-007 — without it, no meaningful test parameters can be written.

**Resolution Path:** Not yet defined — identify candidate draw solution chemistries compatible with salvage sourcing and solar regeneration before test design proceeds.

---

### LW-UNK-008 — Site characterization → pathway selection decision framework

| Field | Value |
|---|---|
| Status | Open (Declared) |
| Risk | Low |
| Priority | Minor |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** A formal framework converting Site Characterization Inputs (proximity to water, climate, elevation, salvage availability, energy profile, contaminant classes) into a specific pathway recommendation has been declared as future work but not yet written. Currently the Site Context table provides informal guidance only.

**Why It Matters:** Without a formal framework, pathway selection depends on manual interpretation of the Site Context table rather than a repeatable decision procedure — a scaling risk once multiple Forges need to make this determination independently.

**Resolution Path:** Payment via Specification — write the formal decision framework as a dedicated addition to this file, once enough pathway validation data exists to make the framework's outputs meaningful rather than speculative.

---

### LW-UNK-009 — Salvage sourcing path for fence-mounted AWG variant (LW-005a)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Sourcing |
| Blocking | No — fence-mounted is an alternative deployment form, not the primary Forge candidate (vertical unit architecture is primary) |
| Owner | Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The fence-mounted AWG variants (2 ft solar unit, 8 ft rollable grid unit) currently assume new manufacture at defined cost targets, which conflicts with salvage-first doctrine. No salvage sourcing path has been demonstrated.

**Why It Matters:** Until resolved, these variants remain reference designs for context rather than actual Forge build candidates — required before this variant could be considered for build candidacy at all.

**Resolution Path:** Not yet defined — requires demonstrating that the variant's component list (solar panel, DC fan, controller) can be salvage-sourced at comparable performance to the new-manufacture reference design.

---

### Resolution Log

- 2026-07-30: AWG planning hygiene (no unknown closures).
  - ASM-004 and Body energy-intensity note: replaced 0.3–0.5 kWh/L as implied Forge baseline with climate-banded planning ranges (~0.8–1.5 humid; higher in mixed/arid); 0.3–0.5 retained only as best-case OEM ceiling. LW-TEST-502 remains the measurement gate.
  - LW-005: added climate-conditioned method preference table — arid sites prefer sorption + solar/waste-heat regeneration over pure vapor-compression AWG.
  - LW-005: added reciprocal interface with `Tests/Solar_Descent.md` (SD owns heat delivery; Living_Waters owns water-side use including sorption desorption and condensate handling). Matches SD Phase 1 Tier-3 boundary direction; coupling still unvalidated.
  - Open Unknowns unchanged (9). Operating as Synthesizer per Auditor_Protocols.md v0.29.

- 2026-07-12: **Template-skeleton backfill and full sidecar conversion, v0.3 → v0.4.** Added Navigation Anchors (previously absent). Converted File State to the canonical field set, retaining the legacy fields (Version, Depends On, Feeds Into) as a secondary table for continuity. Added a standalone Scope Boundary section (previously absent). Retitled "Purpose" to "File Purpose." Added a standalone Assumptions section (5 entries, extracted from existing Governing Principle, LW-001, and LW-003 content — no new claims introduced). Wrapped Governing Principle through Cross-References under a new `## Body` header; individual LW-00x pathway headers demoted to `####` to nest correctly under the new `### Experimental Pathways` subheader. Converted the flat Open Unknowns table (9 entries) into full per-entry sidecar format (Status/Risk/Priority/Type/Blocking/Owner/Resolution Path) under a new `## Auditor Notes & Unknowns` section — Risk and Priority values derived from existing [CRITICAL] flags and Promotion Criteria references in the source text, not newly asserted. Added Lessons Learned, Active Disputes, Abandoned Paths, and Drift Indicators sections (all previously absent). **Unknowns.md global index registration for LW-UNK-001 through 009 — confirmed complete.** *(Correction, 2026-07-19: this note originally said registration "remains outstanding," but `Unknowns.md` v4.18, published the same day as this backfill, already confirmed the LW-UNK cluster complete with no action needed. The note sat stale and uncorrected for a week.)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| — | — | No paths formally abandoned yet. LW-002 (conventional RO) and the fence-mounted AWG variants (LW-005a) are deprioritized behind other candidates (see LW-UNK-006 and LW-UNK-009) but remain open, not rejected — they're held as reference/comparative pathways pending sourcing solutions, not dead ends. | — |

---

## Drift Indicators

- Body proposes deploying LW-001 without the two-stage volatile fractionation cycle (LW-UNK-001) — this is the specific failure mode that turns "water production" into "toxin concentration"
- Body proposes deploying LW-003 without a validated crush-depth-rated conduit (LW-UNK-003)
- LW-001 yield or efficiency claims are stated without the "peak-condition" or "unvalidated modeling estimate" qualifiers already present in the source data
- Atmospheric-scale effects (regional humidity reduction, weather modification) are proposed as a design objective rather than an explicitly out-of-scope secondary effect
- A pathway is promoted to Operations/ without satisfying all five Promotion Criteria, or promoted as a blanket file-level change rather than pathway-specific
- Water Hierarchy tiering is skipped and all output is treated as requiring Tier 1 (potable) purity by default
- Ethical Anchor field is absent, altered, or does not match the canonical string
- LW-UNK entries remain unmigrated to Unknowns.md's global index past a reasonable interval without that gap being flagged (see Resolution Log, 2026-07-12)
- Active AWG energy systems are sized against 0.3–0.5 kWh/L as a baseline rather than climate-banded planning figures pending LW-TEST-502
- Arid-context primary water strategy is pure vapor-compression AWG with no sorption/waste-heat alternative acknowledged

---

*Civilizations rise where water becomes reliable. The first harvest is not food. The first harvest is trust in the water.*
