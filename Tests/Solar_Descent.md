# Solar_Descent.md
*Tests/Solar_Descent.md*

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
| Verification Ref | Admin/Verification_Gates_LF.md |
| Last Audit | 2026-07-30 |
| Auditor | Claude (Synthesizer), Gemini (Auditor), ChatGPT (Synthesizer), Grok (Synthesizer); Gemini — Skeptic/Auditor Exploration audit, Claude — Synthesizer/Auditor (verification against source, corrections applied), 2026-07-28; Grok — Skeptic/Auditor Exploration audit, Claude — Synthesizer/Auditor (verified against source, SD-UNK-015 registered, SD-UNK-007 resolution path corrected), 2026-07-28; 2026-07-30 Phase 0 hygiene — Ethical Anchor canonicalized, SD-UNK-013/014/015 mirrored to Unknowns.md (Synthesizer); 2026-07-30 Phase 1 Resolution Pass — open unknowns 15 → 8 (Synthesizer) |
| Open Unknowns | 8 |
| Active Disputes | 0 |
| Forward References | Astroid-miner companion repository |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Solar Descent organizing principle and diverge/reconverge architecture.
- SD-001 optical downlink pathway and its sub-components including the molten tin termination concept.
- SD-002 thermal/fluid downlink pathway and its sub-components.
- The shared underground chamber architecture where both pathways reconverge.
- Chamber geometry candidate (geodesic/spherical) and modular panel expansion approach.
- Power conversion cascade from the underground chamber.
- Safety governance doctrine for both pathways.
- Proposed test parameters for each pathway and shared systems.
- Forward reference to Astroid-miner companion system and declared technology transfer paths.
- Open unknowns requiring resolution before promotion consideration.

**This file DOES NOT define:**
- General energy storage doctrine (see Operations/Energy.md).
- High-temperature thermal processing doctrine (see Operations/Gate_05_Separation_Thermal.md).
- Pyrolysis doctrine (see Operations/Plastics.md).
- Water distillation from waste heat cascade (see Tests/Living_Waters.md LW-001 and LW-008).
- Geotechnical excavation specifications — out of scope at current development interval.
- Site-specific geology assessment — site-conditioned; no universal answer possible.
- Grid-scale power generation — out of scope for v0 Forge.

---

## File Purpose

Solar Descent is a concentrated solar energy architecture that deliberately separates the surface collection layer from the underground processing and storage mass. Energy harvested at the surface is routed downward — either as photons via optical downlink or as enthalpy via thermal fluid downlink — to an insulated subterranean chamber where it performs high-temperature industrial work, drives power conversion, and cascades waste heat to secondary systems.

The organizing paradox: the surface exists only to collect. The underground exists only to work. By separating these functions, the system gains thermal stability from planetary mass, removes high-temperature processing from surface exposure, enables larger thermodynamic differentials for conversion efficiency, and concentrates industrial heat at a point protected from environmental degradation.

Two downlink pathways diverge at the transport stage and reconverge at the underground chamber:

- **SD-001 — Optical Downlink:** Concentrated sunlight is routed underground as light via fiber optic bundles or reflective light wells.
- **SD-002 — Thermal/Fluid Downlink:** Concentrated sunlight heats a working fluid at the surface; that fluid carries enthalpy underground via insulated piping.

Both pathways feed the same underground chamber. The chamber architecture, power conversion cascade, and safety systems are shared. Pathway selection is site-conditioned and resource-conditioned — the two are not mutually exclusive and may be co-deployed.

This file lives in Tests/ because excavation requirements are unvalidated at Forge scale, temperature claims are theoretical, and no prototype combining salvage-first construction with underground solar concentration has been demonstrated.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Fiber optic bundles sourced from salvage can sustain sufficient flux density for meaningful underground heat delivery | Analogous — research fiber solar systems demonstrated; salvage-grade fiber durability unknown. Telecom fiber likely unsuitable — designed for information transmission, not power density | **Very Low** | SD-TEST-101 flux measurement |
| ASM-002 | Achievable underground focal temperature at Forge build quality falls within useful industrial range | Research literature peaks at 1000–2000°C; Forge-scale with salvaged components likely underperforms significantly. Conservative expectation: 300–800°C. Stretch: 800–1500°C. Research peak: 2000°C+. Conservative range still supports Stirling, pyrolysis, distillation, and thermal storage. | Low | SD-TEST-103 temperature measurement |
| ASM-003 | Molten salt or synthetic oil working fluid can be sourced or synthesized from salvage stream | Analogous — industrial availability; Forge sourcing unconfirmed | Low | Component audit |
| ASM-004 | Host geology at target site can sustain subterranean chamber without thermal fracturing | General geomechanical literature; site-specific geology unknown | Very Low | SD-TEST-201 geomechanical assessment |
| ASM-005 | Underground chamber thermal self-discharge rate is manageable without active insulation beyond packed earth and salvaged insulation board | Analogous — passive underground thermal storage literature | Low | SD-TEST-205 chamber self-discharge measurement |
| ASM-006 | Stirling engine or sCO₂ turbine can be sourced from salvage stream in suitable configuration | Analogous — Stirling engines appear in salvage; sCO₂ turbines unlikely at v0 | Medium for Stirling; Very Low for sCO₂ | Component audit |

---

## Body

### Organizing Principle

Conventional concentrated solar power places all thermal mass, processing, and conversion infrastructure at or near the surface. This exposes high-temperature systems to environmental degradation, imposes surface footprint costs, and limits the thermodynamic differential available for conversion efficiency.

Solar Descent inverts this. The surface layer is minimized to a collection aperture. Everything that benefits from stability, insulation, and thermal mass is placed underground. The planet itself becomes the insulation jacket, the vibration damper, and the thermal reservoir.

The two downlink pathways diverge in transport physics but share a destination:

```
Surface Collection Layer (heliostats, parabolic concentrators, tracking arrays)
      ↓                              ↓
SD-001 Optical Downlink     SD-002 Thermal/Fluid Downlink
(photons via fiber/well)    (enthalpy via molten salt/oil)
      ↓                              ↓
      └──────────────┬───────────────┘
                     ↓
         Underground Chamber (shared)
                     ↓
         Power Conversion Cascade
                     ↓
         Primary Output (electrical / mechanical)
                     ↓
         Waste Heat Cascade (LW-001, space heating, process heat)
```

---

### Surface Collection Layer (Shared)

Both downlink pathways draw from the same surface collection infrastructure.

**Aperture Design**
- Low-profile heliostat arrays or static parabolic concentrators optimized for flux density, not immediate conversion.
- Surface footprint minimized — collection area is the only justified surface presence.
- Tracking systems preferred for maximum daily flux capture; static concentrators acceptable for bootstrap phase.

**Structural Shielding**
- Surface components require durable environmental protection: self-cleaning glass covers, automated dust shutters, UV-resistant housing.
- Sacrificial outer surfaces preferred over protected inner components — replace the shield, not the concentrator.
- Biofouling management required in humid climates. See Challenges/Biofouling.md.

**Salvage Component Targets**
- Parabolic dish reflectors: salvaged satellite dishes, resurfaced with reflective film or polished aluminum sheet.
- Tracking actuators: salvaged linear actuators, stepper motors, automotive window motors.
- Structural frames: salvaged steel tube and angle iron.
- Cover glass: tempered glass salvaged from appliances, shower enclosures, commercial glazing.

**Cold-Start / Bootstrap Power (provisional)**
Tracking actuators must not depend on the underground conversion cascade for initial orientation. Required independent of chamber state: (1) a small dedicated PV panel and/or battery reserve sized only for tracking-motor duty cycle, or (2) a passive/manual fallback tracking mode usable during cold-start. Cross-reference `Operations/Energy.md` for small-scale power doctrine before inventing a parallel mechanism. Empirical sizing remains open; the independence requirement is binding for any motorized array design.

---

### SD-001 — Optical Downlink

**Concept**

Concentrated sunlight is coupled into fiber optic bundles or vertical reflective light wells and routed directly underground as photons. The underground focal point receives light and converts it to heat at the chamber receiver.

**Advantages**
- No working fluid required — eliminates pump complexity and fluid sourcing.
- Optical energy can be directed with precision to a small focal zone.
- Modular — additional fiber bundles add capacity without redesigning the fluid circuit.
- Compatible with direct photochemical reactions at the focal point (solar fuels, chemical synthesis) in addition to thermal applications.

**Challenges**
- Fiber attenuation limits total flux delivery over long vertical runs.
- Fiber entry ends require cooling or protection against damage at high input flux (>400 kW/m² demonstrated to cause damage in research systems).
- Coupling efficiency between concentrator and fiber bundle is a significant loss point.
- Dust and contamination in the shaft degrade optical transmission over time.

**Achievable Temperature Range (proposed — unvalidated at Forge scale)**

| Configuration | Projected Temperature | Confidence |
|---|---|---|
| Salvage-grade silica fiber, single dish | 500–1000°C | Low |
| Optimized silica fiber bundle, multi-dish array | 1000–1700°C | Low — bounded by silica softening point (~1200°C sustained; ~1710°C melt) |
| Sapphire fiber, inert atmosphere cavity | 1700–2040°C | Very Low — bounded by sapphire melting point |
| Research peak (Israeli fiber solar, narrow hot zone) | ~2400°C reported | External reference only — purpose-built fiber; not Forge-achievable |

All figures are proposed parameters pending empirical testing at Forge build quality. Degraded performance should be assumed for initial planning.

**Salvage Component Targets**
- Fiber optic bundles: industrial process fiber, medical fiber optic light guides. **Telecommunications fiber is likely unsuitable** — designed for information transmission, not power density; may fail almost immediately under concentrated flux. Requires explicit characterization before use.
- **Light well alternative (parallel test arm — not a promoted primary path):** Polished stainless steel tube or salvaged aluminum irrigation pipe with reflective interior lining. Claimed advantages over fiber (no melting risk, no coupling losses, easier shaft cleaning, greater scalability) are unvalidated at Forge scale. Tracked exclusively by SD-TEST-106 as a parallel arm to SD-TEST-101; do not treat as elevated-priority doctrine until comparative flux data exist. See SD-UNK-015 (Vehicle).
- Secondary concentrators at fiber or well input: compound parabolic concentrators (CPC) fabricated from polished salvaged sheet metal.

---

#### SD-001a — Molten Tin Fiber Termination (Experimental Sub-Concept)

**Concept**

At the underground end of the optical downlink, glass rods or fiber ends are submerged in a shallow pool of molten tin. The molten tin acts as a reflective liquid interface — redirecting light that exits the fiber ends into the chamber receiver while the tin bath itself absorbs and transfers heat to the surrounding thermal storage medium.

**Analogous Phenomena (not direct physical basis)**
- Molten tin is highly reflective for visible and near-infrared wavelengths due to free-electron metallic reflectivity.
- The float glass process demonstrates stable glass-tin contact at controlled temperatures — however, fiber ends submerged in molten tin is a substantially different geometry from flat glass floating on a large tin bath. The analogy is weak and should not be used to imply experimental support stronger than actually exists.
- A liquid tin interface could act as a dynamic, self-healing secondary reflector in principle — minor surface contamination re-merges into the liquid bath rather than permanently fouling a solid surface. This remains undemonstrated at relevant flux densities.

**Temperature Constraints**
- Molten tin melting point: ~232°C. Boiling point: ~2602°C.
- At focal temperatures approaching silicon vaporization (>2600°C), tin would vaporize, creating convective instability and optical disruption.
- Practical operating window: **800–1100°C** for salvage-grade silica rod infrastructure. Silica softens rapidly near 1200°C and transitions to liquid near 1710°C — the upper tin bath surface temperature must be throttled to 1100°C to preserve structural utility of silica rods. Sapphire rods extend operational ceiling to **~1500°C** under strict thermal throttling.
- Silica glass rods soften under sustained load below 1700°C — sapphire rods (melting point ~2040°C) are mandatory for operation above 1100°C.

**Failure Modes**
- Tin oxidation forming dross layer — destroys reflectivity. Mitigation: inert atmosphere (argon purge) in the termination cavity.
- Tin vapor contamination of downstream processing zone — critical concern for any purity-sensitive application (silicon processing, chemical synthesis). Mitigation: physical separation of tin bath from processing zone.
- Glass rod wetting failure — bubbles or tin penetration at the interface scatter light. Mitigation: mechanical immersion pressure; evaluate gallium or gallium-indium alloys as alternative liquid metal with lower vapor pressure.
- Convective turbulence at high flux — disrupts optical interface geometry. Mitigation: limit input flux to maintain bath below boiling threshold.

**Alternatives Worth Evaluating**
- Gallium or gallium-indium (Galinstan) alloys — lower melting point (~30°C for Galinstan), lower vapor pressure than tin at elevated temperatures, demonstrated in liquid metal mirror applications.
- Shallow molten tin pool above the fiber termination rather than submersion — fiber ends deliver light downward onto the tin surface rather than through it.
- Liquid metal mirrors (gallium alloys) adapted from telescope mirror applications.

**Status:** Highly experimental. Partial viability demonstrated in analogous applications. Requires dedicated test rig before any integration into main SD-001 pathway.

---

**SD-001 Proposed Test Parameters**

- **SD-TEST-101 (Flux Delivery Measurement):** Measure actual photon flux delivered to underground focal point per unit collection area across fiber bundle lengths of 5 m, 10 m, 20 m. Establish attenuation rate per meter and minimum viable bundle specification.
- **SD-TEST-102 (Fiber Entry Cooling):** Characterize thermal damage threshold at fiber input end under concentrated flux. Establish cooling requirement (passive, active airflow, water jacket) to sustain continuous operation.
- **SD-TEST-103 (Underground Focal Temperature):** Measure actual temperature achieved at underground cavity receiver under SD-001 delivery at Forge-scale collection area. Compare against ASM-002 projected range.
- **SD-TEST-104 (Molten Tin Interface Stability):** Dedicated test rig for SD-001a. Measure reflectivity, optical interface stability, and contamination rate over sustained operation under controlled atmosphere. Establish viable operating temperature window.
- **SD-TEST-105 (Shaft Contamination Rate):** Measure optical transmission degradation over 30-day period in shaft environment. Establish cleaning cycle interval.
- **SD-TEST-106 (Light-Well Comparative Flux Delivery):** Run as a parallel arm alongside SD-TEST-101. Measure delivered flux, coupling loss, and contamination rate for a reflective light-well against the fiber bundle baseline over equivalent shaft lengths. See SD-UNK-015.

---

### SD-002 — Thermal/Fluid Downlink

**Concept**

Concentrated sunlight heats a working fluid at a surface receiver. The fluid — molten salt or high-temperature synthetic oil — carries thermal energy underground via vacuum-insulated vertical piping. Underground, the fluid transfers heat to the storage medium and returns to the surface to be reheated.

**Advantages**
- Mature technology base — molten salt thermal storage is well-established in commercial CSP.
- No optical coupling losses — thermal transfer is more tolerant of surface contamination than fiber optics.
- Working fluid doubles as thermal storage medium if circulated through the underground chamber directly.
- Easier to scale throughput by increasing pipe diameter or adding parallel circuits.

**Challenges**
- Working fluid sourcing — molten salts and synthetic oils are industrial products; salvage sourcing is uncertain.
- Freeze risk — molten salt systems must maintain minimum temperature continuously or face solidification and pipe blockage.
- Gravitational head pressure management — downward column assists pumping down; return pump must overcome full fluid column weight back to surface.
- Vacuum insulation on vertical piping is demanding to fabricate from salvaged materials.
- Fluid degradation at extreme temperatures — synthetic oils have upper temperature limits (~400°C); molten salts extend to ~600°C; liquid metals (sodium, tin) required above that.

**Working Fluid Options**

| Fluid | Operating Range | Salvage Compatibility | Risk |
|---|---|---|---|
| Synthetic thermal oil (Therminol, Dowtherm) | Up to ~400°C | Low — specialty product | Freeze point low; manageable |
| Molten nitrate salt (60% NaNO₃ / 40% KNO₃) | 220–600°C | Medium — industrial chemical | Freeze risk below 220°C |
| Liquid sodium | 98–880°C | Low — specialist handling | High reactivity with water; serious safety concern |
| Molten tin | 232–2600°C | Medium — recoverable from salvage | High temp viable; vapor pressure at extremes |

**Pressure and Head Loss**
- At 20 m depth, a molten nitrate salt column (ρ ≈ 1800 kg/m³) exerts approximately **353 kPa (~0.35 MPa)** additional head pressure on the return pump (P = ρgh = 1800 × 9.81 × 20). Prior figure of ~40 kPa was in error by nearly an order of magnitude — corrected per ChatGPT audit 2026-06-14.
- Downward pumping is gravity-assisted; fluid column weight reduces pump work on the descent stroke.
- Net energy cost of fluid circulation must be characterized against thermal delivery — this is the parasitic load of SD-002.

**Salvage Component Targets**
- High-temperature piping: salvaged steam boiler pipe, stainless industrial process pipe.
- Insulation: salvaged mineral wool, ceramic fiber blanket, perlite fill for annular insulation.
- Pumps: salvaged centrifugal or gear pumps rated for high-temperature fluid.
- Surface receiver: salvaged pressure vessel, modified with selective absorber coating.

**SD-002 Proposed Test Parameters**

- **SD-TEST-201 (Fluid Delivery Efficiency):** Measure thermal energy delivered underground vs. collected at surface across pipe lengths of 5 m, 10 m, 20 m. Establish heat loss rate per meter and minimum viable insulation specification.
- **SD-TEST-202 (Parasitic Pump Load):** Measure electrical energy required to circulate working fluid through vertical circuit. Establish net energy delivery ratio (thermal delivered / pump energy consumed). Reject configurations below ratio of 10:1.
- **SD-TEST-203 (Freeze Recovery Protocol):** Simulate loss of surface collection (night, cloud cover) and measure time-to-freeze at minimum insulation specification. Establish freeze prevention protocol (trace heating, drain-back, minimum flow).
- **SD-TEST-204 (Fluid Degradation Rate):** Measure working fluid thermal stability over 30-day sustained operation at target temperature. Establish fluid replacement interval.
- **SD-TEST-205 (Chamber Self-Discharge Measurement):** Dedicated test, distinct from SD-TEST-202's parasitic pump load scope. Measure chamber heat loss rate into surrounding bedrock over a sustained period at known insulation R-value, isolated from pump-circuit losses. See SD-UNK-007.

---

### Underground Chamber (Shared — Both Pathways)

The underground chamber is the reconvergence point. Whether energy arrives as photons (SD-001) or as fluid enthalpy (SD-002), it enters a common thermal storage and conversion environment.

**Chamber Architecture**

- **Thermal storage medium:** Rock/gravel bed, packed sand, or phase-change material matrix. High-grade heat injected at chamber top; cool medium drawn from bottom and returned to surface loop.
- **Thermal stratification:** Natural buoyancy maintains temperature gradient. Hot zone at top, cool zone at bottom. Preserves temperature differential for conversion efficiency.
- **Insulation:** Chamber walls lined with salvaged mineral wool, ceramic fiber, or perlite. Surrounding earth becomes passive secondary insulation jacket as it equilibrates over time.
- **Geomechanical constraint:** Operating temperature ceiling strictly bounded by host rock thermal expansion limits. Temperature must remain below fracturing threshold for local geology. See SD-UNK-004.
- **Atmosphere:** Inert atmosphere (argon or nitrogen purge) preferred for any pathway involving molten metal components or high-purity processing. Passive gravity-fed pressure relief venting for steam spike or containment breach.

**Shaft / conduit penetration envelope (conceptual requirement)**
Any light-delivery shaft or fluid conduit that pierces the chamber boundary must preserve (1) inert-gas containment and (2) thermal isolation sufficient that the penetration is not the dominant self-discharge path. Solar_Descent owns this operating envelope (atmosphere integrity + thermal-break intent at the interface). Structural civil detailing of the seal (grout, bellows, window frames, shaft lining) is out of scope here and belongs with site/facilities doctrine (`Architecture/Facilities.md` when that interface is registered). Candidate elements (quartz/sapphire window for optical paths; bellows or labyrinth seals for fluid paths) are Analogous only until specified.

**Chamber Geometry — Design Candidate**

Rectangular flat-walled chambers develop thermal stress concentrations at corners under repeated heating and cooling cycles. At the conservative-to-stretch operating range ASM-002 establishes (300–1500°C, with 2000°C+ treated there as an unconfirmed research-peak ceiling, not a design target), this is a structural failure pathway over time.

A geodesic or near-spherical geometry — analogous to a truncated icosahedron (soccer ball form) — distributes thermal stress evenly across the entire surface. No stress concentration points. Thermal expansion loads are shared uniformly by the shell.

*Modular panel expansion:* Rather than committing to full excavation upfront, the chamber can begin as a minimal viable sphere and expand by adding panels outward as validated performance justifies increased volume. Each expansion stage is independently testable before the next is committed.

This geometry also has a declared forward relevance: a self-contained spherical processing vessel that can be scaled and separated into panels is directly analogous to the architecture needed for asteroid body processing in the Astroid-miner companion system. See Forward Reference section.

**Status:** Design candidate — not a committed specification. Geometry selection is deferred to SD-UNK-004 (host geology) resolution, as excavation method constrains achievable chamber shape.

**Self-Discharge Rate**

Heat leaks into surrounding bedrock continuously. Self-discharge rate (% of stored energy lost per day) is a function of insulation thickness, temperature differential, and chamber geometry. **Diurnal / overnight** loss bounds must be characterized before any claim of overnight or cloudy-day hold — see SD-UNK-007 (Open, Minor) and SD-TEST-205. **Multi-month / seasonal** storage loss is out of v0 Exploration scope and is routed to `Admin/Trajectories.md` (discharged from this file's active unknown set in Phase 1).

---

### Power Conversion Cascade (Shared)

Energy extraction from the underground chamber follows a grade-prioritized cascade. Higher-grade heat performs higher-value work first; waste heat from each stage becomes input to the next.

```
Underground Chamber (high-temperature thermal storage)
      ↓
Tier 1 — High-Grade Heat (>500°C)
      → Stirling engine (mechanical / electrical output)
      → sCO₂ turbine if available (higher efficiency, lower salvage probability)
      → Direct high-temperature industrial process (pyrolysis feed, chemical reduction)
      ↓
Tier 2 — Mid-Grade Waste Heat (200–500°C)
      → Secondary Stirling stage
      → Process heat for Gate_05_Separation_Thermal.md operations
      ↓
Tier 3 — Low-Grade Waste Heat (<200°C)
      → LW-001 Vacuum Distillation (waste heat as thermal input — direct synergy)
      → LW-008 Multi-Effect Vacuum Distillation
      → Space heating
      → Drying operations (lumber, salvage materials)
      ↓
Thermal baseline reset (fluid returns to cold side of storage)

**Living_Waters interface boundary:** Solar_Descent owns thermal energy delivery up to the heat-exchanger interface (target: usable waste heat at return, provisionally ≥90°C where distillation is intended). `Tests/Living_Waters.md` owns distillation vessel fluid dynamics, purity doctrine, and yield rates. Neither file may unilaterally redefine the other's side of this boundary.
```

**Conversion Technology Assessment**

| Technology | Salvage Probability | Efficiency | Notes |
|---|---|---|---|
| Stirling engine | Medium — appears in specialty salvage | 25–40% thermal-to-mechanical | Preferred v0 candidate |
| sCO₂ turbine | Very Low — industrial specialty | 45–55% | Declared future pathway; not v0 viable |
| Steam turbine (small) | Low-Medium | 15–25% at small scale | Requires pressure vessel certification |
| Thermoelectric generator (TEG) | High — consumer electronics | 5–8% | Low efficiency; viable for bootstrap instrumentation power only |

---

### Safety Governance

Consistent with Forge doctrine: physical boundaries and passive mechanisms take precedence over software overrides.

**Optical Shutoff (SD-001)**
- Mechanical optical shutters at surface concentrator output drop automatically on thermal runaway signal — physically severs photon delivery without requiring electrical power.
- Gravity-actuated design preferred: shutter falls closed on loss of holding current rather than requiring active closure signal.

**Fluid Circuit Shutoff (SD-002)**
- Gravity-fed bypass valves redirect working fluid away from the underground chamber on overpressure or overtemperature signal.
- Drain-back design: fluid drains to a surface holding tank by gravity on pump failure, preventing underground solidification.

**Underground Chamber**
- Passive weighted pressure-relief vents prevent catastrophic pressure buildup from steam spike or fluid breach.
- Acoustic emission monitoring for structural shifting — anomalous readings trigger defocused state at surface collection array.
- Temperature sensors at multiple chamber depths — triple-redundant per Architecture/Cognitive_Frameworks.md doctrine; sensors lie, cross-reference is required.

**Thermal Runaway Definition**
- Chamber temperature exceeds host geology fracturing threshold: immediate full shutoff, both pathways.
- Self-discharge rate increases >50% above baseline without change in insulation: investigate structural integrity before resuming operation.

---

## Forward Reference — Asteroid Processing System

Solar Descent is the terrestrial validation stage for a space-based solar concentration and material processing architecture. Every unknown resolved here reduces risk in the Astroid-miner companion system. The relationship is explicit and directional: prove it underground first, then translate to vacuum.

**Technology Transfer Paths**

| Solar Descent Element | Asteroid System Equivalent | Transfer Notes |
|---|---|---|
| SD-001 fiber optic downlink | Space-based fiber or mirror array routing solar flux to processing vessel | No atmosphere means no scattering loss; higher flux density achievable; continuous solar availability eliminates day/night cycle constraint |
| Underground chamber (sealed, inert atmosphere) | Asteroid processing vessel (vacuum environment) | Vacuum eliminates oxidation problems that complicate SD-001a molten tin termination on Earth — SD-001a may be more viable in space than underground |
| Staged thermal cascade by temperature grade | Staged volatile extraction from asteroid body under solar heating | Same physics: different materials release at different temperatures; capture at each stage segregates by composition |
| Stirling conversion (large thermal differential) | Stirling or equivalent (2.7K space background as cold sink) | Space cold sink produces a thermodynamic differential orders of magnitude larger than underground; conversion efficiency ceiling rises dramatically |
| Spherical modular chamber geometry | Self-contained processing vessel; separable panel expansion | Direct architectural analogue — a vessel that can grow by adding panels works identically in both environments |
| Vacuum pump integration (LW-001 synergy) | Vacuum capture of volatiles freeing at staged temperatures | On Earth: pump creates vacuum to lower boiling point. In space: vacuum is the ambient condition; staged heating drives volatiles off sequentially |

**The Staged Asteroid Extraction Sequence**

Solar concentration heats an asteroid body or captured fragment under ambient vacuum. Different materials sublime or outgas at different temperatures, enabling fractional segregation without mechanical separation:

```
Solar concentration applied to asteroid body
      ↓
Stage 1 — Noble gases and light volatiles (H₂, He, N₂) — lowest temperature
      → Vacuum capture at Stage 1 temperature band
      ↓
Stage 2 — Water ice sublimation (~150–200K onset in vacuum)
      → Capture → feedstock for life support or propellant production
      ↓
Stage 3 — CO₂, SO₂, and volatile ices
      → Capture and segregate
      ↓
Stage 4 — Organic compound fractions (temperature-banded by boiling point)
      → Capture → chemical feedstock
      ↓
Stage 5 — Silicate and metal processing (high temperature)
      → Structural and manufacturing feedstock
```

This is fractional distillation of an asteroid body under solar heat — the same organizing principle as LW-001 vacuum distillation and SD-001's staged thermal cascade, applied at planetary material scale.

**Scope Declaration**

The asteroid processing system is out of scope for this file. Solar Descent defines terrestrial underground solar concentration. The forward reference exists to:

1. Preserve the conceptual connection so it is not reinvented independently later.
2. Declare that SD test results (especially SD-TEST-101 through SD-TEST-104) are inputs to Astroid-miner system design, not only to Forge Operations/ promotion.
3. Flag SD-001a (molten tin termination) as potentially more viable in vacuum than underground — a finding that may be relevant to the space system before it is resolved terrestrially.

**Repository Pointer:** `Astroid-miner` companion repository. Activates when Leviathan deployment is underway per Discovery.md cross-repo relationship declaration. Solar Descent findings should be formally transferred to that repository at activation.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — file is pre-empirical | — | — |

---

## Active Disputes

*(none at first draft)*

---

## Auditor Notes & Unknowns

### SD-UNK-001 — Flux delivery at Forge-scale fiber unvalidated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical |
| Blocking | Yes — blocks SD-001 pathway viability assessment |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** No measurement exists of photon flux delivered underground via salvage-grade fiber optic bundle at Forge-relevant collection area and shaft depth. Research systems use purpose-built high-flux fiber; salvage-grade fiber thermal tolerance and attenuation are uncharacterized.

**Resolution Path:** SD-TEST-101 empirical measurement.

---

### SD-UNK-002 — Achievable underground temperature at Forge build quality unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical |
| Blocking | Yes — blocks power conversion pathway selection |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** ASM-002 projects 1000–2000°C based on research literature. Forge build quality using salvaged components will underperform research systems. Actual achievable temperature determines which conversion technologies are viable and which industrial processes can be driven.

**Resolution Path:** SD-TEST-103 empirical measurement. Until resolved, power conversion planning must assume conservative lower bound (~500°C) to avoid designing for temperatures the system cannot reach.

---

### SD-UNK-003 — Molten tin termination (SD-001a) viability unconfirmed

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Minor |
| Type | Technical |
| Blocking | No — SD-001 viable without SD-001a; optional sub-concept only |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |

**Description:** The molten tin fiber termination concept has physical basis but faces oxidation, contamination, boiling instability, and glass compatibility challenges at target operating temperatures. Gallium alloy alternatives are unassessed.

**Resolution Path:** SD-TEST-104 dedicated test rig. SD-001a is not a dependency for SD-001 core pathway — it is an efficiency enhancement candidate only.

---

### SD-UNK-004 — Host geology fracturing threshold unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | Critical |
| Priority | Critical |
| Type | Site-Conditioned |
| Blocking | Yes — blocks any excavation or chamber construction |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The maximum safe operating temperature of the underground chamber is bounded by the thermal expansion and fracturing threshold of the host rock. This is entirely site-specific — limestone, granite, sandstone, and clay all behave differently under thermal cycling. No universal answer is possible.

**Resolution Path:** Discharge via Trajectory — site geomechanical assessment required before chamber design can proceed. Remains open until first deployment site confirmed. Parallels FA-001 (facility siting) in governance weight.

---

### SD-UNK-005 — Working fluid salvage sourcing (SD-002) unconfirmed

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks SD-002 optimization, not SD-001 |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Molten salt and high-temperature synthetic oil are industrial specialty products. Salvage sourcing path has not been identified. Molten tin is more recoverable from the salvage stream but introduces contamination and vapor pressure risks at high temperatures.

**Resolution Path:** Component audit of local industrial salvage stream. If no viable fluid is found, SD-002 requires new-purchase input — a doctrine conflict requiring human decision.

---

### SD-UNK-006 — Parasitic pump load for SD-002 uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The energy cost of circulating working fluid through a vertical circuit (down and up) has not been measured. If parasitic pump load is a significant fraction of thermal delivery, SD-002 net efficiency drops materially.

**Resolution Path:** SD-TEST-202 parasitic pump load measurement.

---

### SD-UNK-007 — Diurnal chamber self-discharge rate unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Minor |
| Type | Technical |
| Blocking | No — blocks overnight/cloudy hold claims, not initial flux or geology work |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |

**Description:** Diurnal / overnight heat loss from the underground chamber into surrounding bedrock has not been measured or modeled for target chamber geometry and insulation. Sets minimum daily solar input for overnight or cloudy-day hold. Multi-month / seasonal loss discharged to `Admin/Trajectories.md` in Phase 1 (2026-07-30).

**Resolution Path:** SD-TEST-205 (Chamber Self-Discharge Measurement) — measure heat loss over a sustained period at known insulation R-value, isolated from pump-circuit losses. Thermal modeling may substitute if direct measurement is impractical at this stage.

---

### SD-UNK-008 — Stirling engine salvage availability at required scale unconfirmed

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Medium |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |
| Resolution | Discharge via Trajectory — site component audit at deployment; fall back to TEG / direct process heat already stated in prior path |

**Closed 2026-07-30 (Phase 1):** Salvage availability is site-conditioned. Body conversion table already records Stirling as preferred with TEG/process-heat fallback. Active tracking moved off this sidecar; reopen only if a deployment site audit finds no viable path and fallback is rejected.

---

### SD-UNK-009 — Excavation feasibility at Forge scale unassessed

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | High |
| Priority | — |
| Type | Site-Conditioned |
| Blocking | — |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |
| Resolution | Discharge via Trajectory — parallels FA-001; site assessment required |

**Closed 2026-07-30 (Phase 1):** Path was already declared in-sidecar. Excavation method/depth remain blocked by FA-001 / SD-UNK-004; this entry no longer carries a separate open unknown.

---

### SD-UNK-010 — Waste heat cascade interface with Living_Waters.md undefined

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Low |
| Priority | — |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Solar_Descent.md + Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |
| Resolution | Payment via Specification — Body interface boundary under Power Conversion Cascade Tier 3 |

**Closed 2026-07-30 (Phase 1):** Solar_Descent owns delivered heat quality up to the exchanger; Living_Waters owns distillation doctrine and yield. Reciprocal note on Living_Waters.md still recommended; boundary text is binding here.

---

### SD-UNK-011 — Receiver material survivability uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Minor |
| Type | Technical |
| Blocking | No — blocks sustained-operation specification; T1 coupon work, not excavation gate |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |

**Description:** The underground receiver exposed to concentrated solar flux may experience thermal shock, oxidation, creep, spalling, and localized melting. Receiver material lifetime determines maintenance interval and sets a practical ceiling on maximum sustainable operating temperature — independent of what the fiber or fluid downlink can theoretically deliver.

**Resolution Path:** Dedicated receiver endurance testing under sustained flux at target operating temperature. Receiver material selection must account for thermal cycling, not just peak temperature.

---

### SD-UNK-012 — Dust and alignment stability uncharacterized

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Medium |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-07-30 |
| Resolution | Vehicle — SD-TEST-105 (dust) owns contamination; alignment stability folded as explicit extension of that test arm / maintenance-interval protocol |

**Closed 2026-07-30 (Phase 1):** Unmanaged unknown retired. Empirical dust/alignment work remains; tracked only via SD-TEST-105 (and any later alignment extension), not as a free-floating sidecar entry. Not empirically resolved.

---

### SD-UNK-013 — Surface Collection Bootstrap & Tracking Power Source

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Medium |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-07-28 |
| Last Reviewed | 2026-07-30 |
| Resolution | Payment via Specification — Body Cold-Start / Bootstrap Power requirement under Surface Collection Layer |

**Closed 2026-07-30 (Phase 1):** Independence from the underground cascade is specified (dedicated PV/battery duty-cycle reserve or passive/manual fallback). Sizing and Energy.md cross-check remain implementation work, not an open architectural unknown.

---

### SD-UNK-014 — Shaft Penetration Sealing & Thermal Isolation

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Medium |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-07-28 |
| Last Reviewed | 2026-07-30 |
| Resolution | Payment via Specification (narrow) — Body penetration envelope; civil seal detailing toward Architecture/Facilities.md |

**Closed 2026-07-30 (Phase 1):** Operating envelope (containment + thermal-break intent) defined here. Structural seal design is not owned by this file; register or co-own under Facilities when site civil work starts. Not a blank transfer without owner.

---

### SD-UNK-015 — Light-well vs. fiber comparative flux delivery unassessed

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | Medium |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Solar_Descent.md |
| First Logged | 2026-07-28 |
| Last Reviewed | 2026-07-30 |
| Resolution | Vehicle — SD-TEST-106 (Tier 0 / parallel arm to SD-TEST-101) |

**Closed 2026-07-30 (Phase 1):** Priority claim no longer unmanaged. Comparative flux remains empirically open until SD-TEST-106 runs; tracked only by that test ID. Body light-well language demoted from "elevated priority" to parallel test arm.

---

### Resolution Log

- 2026-07-30: Phase 1 Resolution Pass — Open unknowns **15 → 8** (10-entry
  sidecar rule satisfied). No physics claims closed by prose.

  **Still Open (8):**
  - Critical / Blocking: SD-UNK-001 (flux), SD-UNK-002 (temperature band),
    SD-UNK-004 (host geology ‖ FA-001)
  - Major: SD-UNK-005 (working-fluid salvage), SD-UNK-006 (parasitic pump load)
  - Minor: SD-UNK-003 (molten tin / SD-001a optional), SD-UNK-007 (diurnal
    self-discharge only; seasonal half discharged), SD-UNK-011 (receiver
    survivability, T1)

  **Closed / discharged (7):**
  - SD-UNK-008 → Discharge via Trajectory (site Stirling audit; TEG/process
    heat fallback already in Body)
  - SD-UNK-009 → Discharge via Trajectory (excavation ‖ FA-001; path was
    pre-declared)
  - SD-UNK-010 → Payment via Specification (Living_Waters interface boundary
    in Power Conversion Cascade Tier 3)
  - SD-UNK-012 → Vehicle SD-TEST-105 (+ alignment as test-arm extension);
    not empirically resolved
  - SD-UNK-013 → Payment via Specification (Cold-Start / Bootstrap Power
    under Surface Collection Layer)
  - SD-UNK-014 → Payment via Specification, narrow (penetration envelope in
    Underground Chamber; civil seal toward Facilities)
  - SD-UNK-015 → Vehicle SD-TEST-106; Body "elevated priority" language
    retired

  **Also:** ASM-005 expiry trigger corrected to SD-TEST-205; SD-UNK-007
  narrowed to diurnal/overnight; seasonal multi-month loss noted for
  `Admin/Trajectories.md`. Count verified by direct sidecar enumeration
  of Status=Open entries. Operating as Synthesizer per
  Auditor_Protocols.md v0.29.

- 2026-07-30: Phase 0 hygiene pass — Ethical Anchor corrected to canonical
  plain-text string (was non-canonical `Admin/`-prefixed variant; same
  PC-006 class drift already closed on eight other files 2026-07-12 /
  Energy_Scarcity 2026-07-19). SD-UNK-013, SD-UNK-014, and SD-UNK-015
  registered into `Unknowns.md` Solar Descent table (local sidecar had
  carried them since 2026-07-28; global index lagged at 001–012 only).
  Open Unknowns count unchanged at 15 — no demotion or discharge this
  pass. Index lag closed only; Resolution Pass (10-entry rule) deferred
  to Phase 1. Operating as Synthesizer per Auditor_Protocols.md v0.29.

- 2026-07-28: SD-UNK-015 registered — surfaced by Grok's Skeptic/Auditor
  pass and verified as a genuine, previously unaddressed gap before
  registering (light-well alternative carried an "elevated priority"
  claim with no dedicated unknown or test ID). SD-TEST-106 added to
  SD-001 Proposed Test Parameters as its resolution path. SD-UNK-007's
  Resolution Path corrected — previously referenced "SD-TEST-202
  (extended)," but SD-TEST-202 is scoped exclusively to parasitic pump
  load (SD-002); self-discharge measurement now has its own test ID,
  SD-TEST-205, added to SD-002 Proposed Test Parameters. Open Unknowns
  count: 14 → 15. Verified and registered by Claude — Synthesizer/
  Auditor, human-directed.

- 2026-07-28: SD-UNK-013 and SD-UNK-014 registered — both surfaced by
  Gemini's Skeptic/Auditor pass and verified as genuine, previously
  unaddressed gaps before registering. Four unprefixed canonical
  cross-references corrected to their folder-prefixed form (Ethical
  Anchor field, Cognitive_Frameworks.md, File_Template.md,
  Safety_Protocols.md), also from the same audit. Chamber Geometry
  section's thermal-stress passage corrected — it stated a flat
  "500–2000°C" target operating range where ASM-002 itself already
  tiers the same numbers (300–800°C conservative, 800–1500°C stretch,
  2000°C+ unconfirmed research-peak ceiling, Low confidence
  throughout); the passage now carries that same tiering rather than
  restating the aspirational ceiling as if it were a design target.
  Not treated as a document-wide contradiction — ASM-002's own framing
  was already appropriately hedged; this was one downstream passage
  failing to carry that hedge forward. Open Unknowns count: 12 → 14.
  Verified and registered by Claude — Synthesizer/Auditor,
  human-directed.

*(empty — no unknowns resolved at time of first draft)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| 2026-06-14 | sCO₂ turbine as v0 power conversion target | Very low salvage probability. Industrial specialty equipment. Declared future pathway for v2+ when Forge has fabrication capability to source or build turbomachinery. | Yes — revisit at v2 |
| 2026-06-14 | Liquid sodium as working fluid for SD-002 | Violent reactivity with water makes salvage-context handling unacceptably dangerous. Any moisture intrusion in piping or chamber is a serious safety event. | No — requires purpose-built containment infrastructure incompatible with salvage-first doctrine |
| 2026-06-14 | Grid-scale power generation as design target | Out of scope for v0 Forge. Solar Descent at v0 targets industrial process heat and local power bootstrap, not grid export. | Yes — reconsider at v3+ |

---

## Drift Indicators

Standard mandatory re-audit conditions per Admin/File_Template.md apply.

**Additional file-specific drift indicators:**

- SD-UNK-004 (host geology) remains open and Body content begins specifying chamber dimensions → mandatory human review. Chamber design without geology assessment is a safety violation.
- SD-UNK-002 (achievable temperature) remains unresolved and power conversion pathway is selected based on ASM-002 alone → flag as premature commitment; re-audit before any hardware procurement.
- SD-001a (molten tin) content migrates from sub-concept to primary pathway without SD-TEST-104 completion → reject migration; return to sub-concept status.
- Liquid sodium reappears as a working fluid candidate without dedicated containment infrastructure assessment → immediate escalation to Admin/Safety_Protocols.md review.
- Any reference to grid-scale power export targets before v3 milestone → scope violation; flag for human review.
- SD-UNK-015 (or Body light-well text) is restored to "elevated priority" or primary-path language without SD-TEST-106 results → reject; return to parallel test-arm status.
- Closed Phase 1 entries (008–010, 012–015) reopen without Epistemic Ledger / contradictory evidence → treat as silent priority/status change; re-audit.
