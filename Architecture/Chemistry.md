# Chemistry.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

> ⚠️ **Operational Safety Advisory**
> Chemical and electrochemical processes present hazards that are frequently
> invisible until damage is done. Corrosive acids and bases cause chemical burns
> without warning. Toxic gases — hydrogen sulfide, chlorine, hydrogen cyanide,
> carbon monoxide — are odorless at lethal concentrations or lose their warning
> odor under chronic exposure. Galvanic cells in humid environments generate
> current without any visible indication until structural failure occurs.
> Flammable hydrogen gas evolves silently from overcharged or short-circuited
> lead-acid and lithium cells.
> **Never assume a chemical process is inert because it is slow. Never assume
> a gas is absent because you cannot smell it. Never assume a container is safe
> because it has been sitting still. When in doubt, ventilate, test, and hold.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-07-31                                                          |
| Auditor          | Claude (2026-06-02); ChatGPT informal (2026-06-11); Claude retrofit; Claude — CE-006 logged (human-directed) 2026-07-07; Claude — CE-006 directed approach added (human-directed), 2026-07-17; Claude — CE-006 mechanism correction, CE-007 registered (Grok flag, cross-checked against source), 2026-07-19; Claude — Synthesizer, §2.3 expanded to full doctrine, §2.4 Dilution Doctrine added (CE-008, corrected from proposed CE-004 to avoid ID collision), §1.2 SCC extended, §3.2 NOₓ subsection added, CE-005 narrowed to In Progress, CE-006/CE-007 given quantitative scrubber chemistry and storage doctrine (Grok content, verified against source before adoption), human-directed, 2026-07-31; Claude — CE-006 vessel design sketch integrated after two rounds of correction (thermal-sink sizing, AS-003 prerequisite gate) verified against Air_Scrubber.md source; CE-006 moved Open → In Progress, human-directed, 2026-07-31 |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Life Preservation; chemical dual-use awareness; hazardous material handling |
| `Admin/Safety_Protocols.md` | PPE doctrine for chemical handling; acid, solvent, and toxic gas exposure limits |
| `Architecture/Facilities.md` | RDC climate baseline for humidity and corrosion context — substitute via `Facilities.md` §VII |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Operations/Plastics.md` | Halogenated polymer rejection (PL-001) built on §4.1 Beilstein and §5 polymer degradation |
| `Operations/Electronics.md` | Battery chemistry (§6); BFR hazard (§5.1); PCB etch neutralization (§2) |
| `Operations/Air_Scrubber.md` | Scrubber design and AS-003 saturation monitoring built on §2 acid-base doctrine |
| `Operations/Gate_05_Separation_Thermal.md` | Oxide burden (CE-002); redox chemistry of metal separation (§3.1) |
| `Operations/Gate_03_Reduction.md` | Combustion chemistry (§3.2); contamination indicators (§4.3) |
| `Operations/Energy.md` | Salvaged cell assessment doctrine (§6); EV-003 containment |
| `Operations/Gate_01_Intake.md` | Contamination identification (§4); GI-003 augmented detection |
| `Operations/Gate_02_Triage.md` | Polymer identification (§5.2); Beilstein at Station 0 |
| `Tests/Support_Raft.md` | Galvanic corrosion mitigation SR-001 (§1.1–1.3) |
| `Challenges/Biofouling.md` | MIC mechanism (§1.2); cathodic protection (§1.3) |
| `Architecture/Mechanical_Structures.md` | Galvanic compatibility of mixed-metal salvage assemblies (§1.1) |
| `Architecture/Friction_Dynamics.md` | Peer file — lubrication chemistry; tribochemistry at interfaces |
| `Architecture/Thermal_Systems.md` | Peer file — thermal effects on electrochemical reactions |

---

## Scope Boundary

**This file DOES define:**
- Electrochemical corrosion doctrine — galvanic series, corrosion mechanisms,
  cathodic protection principles, and sacrificial anode selection
- Acid-base chemistry fundamentals relevant to Forge processing and containment
- Oxidation-reduction (redox) principles governing metal recovery and separation
- Contamination identification chemistry — field-applicable detection methods
  for hazardous material streams
- Polymer degradation chemistry — why specific polymer classes are hazardous
  at elevated temperatures
- Surface chemistry fundamentals — adhesion, passivation, oxide formation,
  contact angle, and corrosion interfaces. *Note: surface treatment procedures
  (phosphating, anodizing, blackening, Cerakote) may eventually migrate to an
  Operations/Surface_Treatments.md file as the repository matures. Chemistry.md
  retains the underlying principles; the procedures are implementation detail.*
- Battery and electrochemical cell chemistry — principles governing salvaged
  cell assessment, failure modes, and safe handling
- Forge integration map — how chemical and electrochemical doctrine applies
  across gate operations, marine systems, and material processing
- **Chemical Operator Minimum Competency** appendix — minimum chemical literacy
  standard for Forge operators

**This file DOES NOT define:**
- Foundational engineering principles, safety factors, or materials behavior
  overview (→ `Architecture/Engineering.md` — peer file)
- Heat transfer in reactive systems or thermal runaway mechanics
  (→ `Architecture/Thermal_Systems.md` — peer file)
- Fluid flow in chemical processing systems
  (→ `Architecture/Friction_Dynamics.md` — peer file)
- Air Scrubber hardware specification, stage sizing, or filter selection
  (→ `Operations/Air_Scrubber.md`)
- Pyrolysis reactor design, operating parameters, or polymer feedstock triage
  (→ `Operations/Plastics.md`)
- PCB etch chemistry procedures or waste stream handling protocols
  (→ `Operations/Electronics.md`)
- Battery thermal containment hardware or fire suppression
  (→ `Operations/Energy.md` EV-003)
- Specific chemical product recommendations, brands, or procurement sources
- Regulatory compliance or hazardous materials disposal law
  (jurisdiction-dependent — human governing party decision)

**Peer file relationship:** `Architecture/Engineering.md`,
`Architecture/Thermal_Systems.md`, and `Architecture/Friction_Dynamics.md`
are peer files — same authority level, each owning a distinct domain. This
file owns chemical and electrochemical principles. Where a question is
thermal, mechanical, or fluid in nature, the relevant peer file governs.
Intersections — electrochemical heat generation, chemically driven corrosion
of mechanical structures, reactive fluid flow — require both files and
neither overrides the other. Conflicts escalate to a human contributor.

---

## File Purpose

This file establishes the chemical and electrochemical doctrine for the
Lazarus Forge — the foundational knowledge layer that governs how matter
transforms, how surfaces degrade, how hazardous streams are identified, and
how electrochemical processes are understood and directed across all Forge
systems.

Chemical processes are present in every gate. Metal separation in Gate_05
is fundamentally a high-temperature chemistry problem. Corrosion of the
Support Raft's hull is an electrochemical problem. The decision to reject
PVC from the pyrolysis reactor is a polymer degradation chemistry problem.
The Air Scrubber's alkaline buffering stage is an acid-base chemistry
problem. Battery assessment for salvaged cells is an electrochemical
cell problem. Without a common doctrine layer, each domain file makes its
own chemical assumptions, uses inconsistent hazard classifications, and
misses cross-domain interactions — the electrochemistry driving corrosion
in a bearing housing, the polymer chemistry producing HCl in a mixed
plastic stream, the redox chemistry governing what the Spin Chamber
actually separates.

Without this file, the Forge has no shared chemical language and no
systematic basis for identifying, handling, or exploiting the chemical
processes it encounters constantly.

**Relationship to peer Architecture files:** `Architecture/Engineering.md`
owns broad engineering principles. `Architecture/Thermal_Systems.md` owns
heat transfer and energy conversion. `Architecture/Friction_Dynamics.md`
owns flow, drag, and surface interaction. This file owns chemical and
electrochemical principles. All four are peers. Where domains intersect,
both files apply and neither overrides the other.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|----|------------|-------|------------|----------------|
| CE-ASM-001 | Operators have basic chemistry literacy — can read a pH scale, understand acid/base distinction, recognize common hazard symbols | Reasonable entry level for Forge operators | Medium | Confirmed lower baseline — training materials required before chemical handling begins |
| CE-ASM-002 | Operating environment: high humidity (RDC baseline: 60–95% summer RH), occasional standing water, variable pH in surface water. Builders in drier climates will see lower baseline corrosion rates; builders in coastal or tropical environments may see higher. Substitute via `Architecture/Facilities.md` §VII. | RDC climate baseline — see `Architecture/Facilities.md` §VII | Medium | Forge deployed to significantly different geochemical environment — substitute via Facilities.md §VII |
| CE-ASM-003 | Salvaged materials have unknown chemical history — surface treatments, coatings, contamination, and prior chemical exposure are not documented | Salvage doctrine | High | Provenance documentation confirms chemical history for a specific material class |
| CE-ASM-004 | Field identification methods (Beilstein test, pH strips, visual indicators) are the primary chemical assessment tools at v0 — laboratory analysis is not assumed available | v0 resource constraints | High | Laboratory analytical capability confirmed available at deployment site |

---

## Body

### Section 1 — Electrochemistry Fundamentals

Electrochemistry governs the behavior of charged species at interfaces —
the transfer of electrons between materials, the dissolution of metals in
solution, the generation and storage of electrical energy, and the
degradation of structures in conductive environments. Every metal surface
in a humid or aqueous environment is participating in electrochemical
reactions whether or not they are visible.

#### 1.1 The Galvanic Series

When two dissimilar metals are in electrical contact in the presence of
an electrolyte (any conductive liquid — seawater, rainwater, condensation,
even humid air), a galvanic cell forms. The more active metal (the anode)
oxidizes and loses material. The less active metal (the cathode) is
protected. This process requires no external power — it is driven
entirely by the electrochemical potential difference between the metals.

**Galvanic series — active to noble (partial list for Forge-relevant metals):**

| Position | Metal / Alloy | Forge Context |
|----------|--------------|---------------|
| Most active (anodic) | Magnesium | Sacrificial anode candidate |
| | Zinc | Primary sacrificial anode material |
| | Aluminum alloys | Hull material, structural members |
| | Mild steel / carbon steel | Primary structural material |
| | Cast iron | Common salvage feedstock |
| | Lead | Solder, ballast — contamination risk |
| | Tin | Solder, coating — common in electronics salvage |
| | Copper | Wiring, heat exchangers |
| | Bronze / brass | Fittings, valves |
| | Stainless steel (passive) | Corrosion-resistant applications |
| Most noble (cathodic) | Titanium | High-end marine hardware |
| | Platinum / gold | Electronics contacts |

**Forge implications:**
- Steel bolts into aluminum structure in a marine environment will rapidly
  destroy the aluminum. The steel is more noble; the aluminum is the anode.
- Copper fittings on steel pipe accelerate steel corrosion at every joint.
- Mixed-metal salvage assemblies always contain galvanic cells when wet.
  Assessment of galvanic compatibility is a prerequisite for any
  design using multiple metal types in humid or aqueous environments.

**Galvanic current equation:**

The corrosion rate scales with the area ratio between cathode and anode.
A large cathode area coupled to a small anode area produces rapid anode
destruction — the small anode must supply electrons to the large cathode.
This is why a small steel fastener in a large aluminum plate corrodes
far faster than a steel fastener in a small aluminum plate.

```
Area ratio effect: corrosion rate ∝ A_cathode / A_anode
```

Design rule: when dissimilar metals must be joined, make the more active
metal the larger area. Or isolate with a non-conductive barrier. Or use
a sacrificial anode to intentionally provide the active material.

#### 1.2 Corrosion Mechanisms

**Uniform corrosion** — general oxidation across the entire exposed surface.
The most predictable form; rate can be estimated from corrosion data tables
for specific metal-environment combinations. *(Illustrative values from
standard references: Steel in neutral soil ~0.1–0.5 mm/year; Steel in seawater
~0.1–0.3 mm/year — these are strongly environment-dependent and vary with alloy
composition, oxygen content, chloride concentration, temperature, and microbial
activity. Treat as order-of-magnitude only; CE-001 owns quantitative corrosion
rate characterization for the deployment environment.)*

**Pitting corrosion** — localized attack producing small, deep pits that
penetrate far more rapidly than surface loss suggests. Initiated at surface
defects, inclusions, or coating breaks. Particularly dangerous because
visual inspection sees minimal surface change while structural failure
progresses. Stainless steel is susceptible to pitting in chloride
environments despite its general corrosion resistance.

**Crevice corrosion** — localized attack in confined geometry where oxygen
is depleted relative to the bulk environment. Occurs under gaskets, in
lap joints, under deposits, and in any tight space where solution can
enter but not circulate. The depleted oxygen zone becomes anodic relative
to the bulk surface; accelerated corrosion follows. Design doctrine:
eliminate crevices where possible; seal them where elimination is not
possible.

**Microbiologically Influenced Corrosion (MIC)** — electrochemical
corrosion accelerated by microbial activity. Sulfate-reducing bacteria
(SRB) under anaerobic biofilms consume sulfate and produce hydrogen
sulfide directly at the metal surface, driving corrosion rates 10–100×
faster than abiotic conditions. Iron-oxidizing bacteria create differential
aeration cells. MIC is the mechanism underlying the most severe biofouling
corrosion cases in the Forge's marine deployment context.

Detection: black deposits (iron sulfide) at pitting sites, hydrogen
sulfide odor when deposits are disturbed, anomalously rapid corrosion
under apparently intact biofilm. MIC is typically only identified after
significant damage has occurred — prevention through cathodic protection
and coating integrity is more reliable than detection.

**Stress corrosion cracking (SCC)** — brittle fracture of a normally
ductile metal under combined tensile stress and specific corrosive
environment. Certain alloys are susceptible in specific environments:
stainless steel in chloride solution, brass in ammonia, aluminum alloys
in salt water under stress. SCC cracks propagate rapidly once initiated
and fail with little warning. Salvaged structural members with unknown
stress history and unknown alloy composition in chloride environments
should be treated as SCC candidates.

**SCC-susceptible alloy/environment pairs (Forge-relevant):**

| Alloy | Environment | Notes |
|------------------------|----------------------|-------|
| 304/316 stainless | Chloride | Pitting initiates SCC under tensile load |
| Brass | Ammonia | Dezincification + SCC |
| Aluminum alloys | Salt water / cyclic stress | High risk for salvage structural members |
| High-strength steels | Hydrogen (from CP overprotection or acid) | Hydrogen embrittlement |

**Inspection doctrine:** SCC cracks are narrow, follow grain boundaries,
may be invisible under paint or corrosion products, and preferentially
occur at welds, cold bends, or residual-stress zones. Any salvaged
structural member with unknown alloy history that has been exposed to
chloride + tensile load is an SCC candidate until proven otherwise.

**Mitigation strategies:**
- Reduce residual tensile stress (re-torque, redesign load path,
  stress-relieve if possible).
- Remove chloride contamination (fresh-water rinse followed by
  passivation where applicable).
- Isolate brass components from ammonia sources.
- Apply cathodic protection carefully — overprotection can increase
  hydrogen embrittlement risk in high-strength steels.
- Prefer known alloys or apply isolation barriers for mixed-metal marine
  assemblies.

**Salvage rejection criteria:** Reject the component if cracks follow
grain boundaries or appear at welds/bends, cracks continue to propagate
after cleaning, or the alloy is unknown and the service environment was
chloride-rich or ammonia-bearing. Cross-reference
`Architecture/Mechanical_Structures.md` and `Tests/Support_Raft.md`
SR-001.

#### 1.3 Cathodic Protection

Cathodic protection (CP) suppresses corrosion by making the protected
structure the cathode of the electrochemical system rather than the anode.
Two methods:

**Sacrificial anode CP:** A more active metal is electrically bonded to
the protected structure. The anode corrodes; the protected structure does
not. The anode must be periodically replaced as it is consumed.

Anode material selection:
- **Zinc** — standard for seawater applications; effective in high-chloride
  environments; well-characterized consumption rates *(Analogous)*
- **Aluminum alloys** — higher capacity than zinc per unit mass; effective
  in seawater; preferred for weight-critical applications *(Analogous)*
- **Magnesium** — most active; effective in low-conductivity fresh water
  and soil; overly active in seawater (drives hydrogen evolution) *(Analogous)*

Sizing rule of thumb: sacrificial anode capacity in amp-hours must exceed
the estimated cathodic current demand of the protected surface over the
service interval. Current demand depends on surface area, coating
condition, and electrolyte conductivity. Full sizing must also
incorporate coating breakdown factor, electrolyte resistivity,
temperature, flow velocity, and biofouling state; quantitative doctrine
remains under CE-001 / `Tests/Support_Raft.md` SR-001.

**Impressed current CP:** External DC power source drives the protected
structure cathodic. More controllable and longer-lasting than sacrificial
anodes but requires continuous power and monitoring. Not assumed available
in v0 remote deployments — sacrificial anode CP is the Forge's primary
approach.

**Forge integration:** Sacrificial anodes produced from recovered zinc,
aluminum, and magnesium fractions from `Operations/Gate_05_Separation_Thermal.md`
and `Operations/Gate_04_Separation_Mechanical.md` are the Forge's native CP
material stream. See `Tests/Support_Raft.md` SR-001 and
`Architecture/Geck_forge_seed.md` GK-002 for open unknowns on material
selection and deployment geometry.

---

### Section 2 — Acid-Base Chemistry

Acid-base reactions govern scrubber neutralization, contamination
identification, waste stream management, and the chemical environment
inside many Forge process zones.

#### 2.1 pH and the Proton Transfer Model

pH measures the concentration of hydrogen ions (H⁺) in aqueous solution:

```
pH = -log₁₀[H⁺]
```

| pH | Character | Forge Examples |
|----|-----------|----------------|
| 0–2 | Strongly acidic | Concentrated sulfuric acid, battery electrolyte |
| 3–5 | Weakly acidic | Acid rain, MIC-generated acids, ferric chloride etch waste |
| 6–7 | Near neutral | Clean rainwater, most process water targets |
| 7 | Neutral | Pure water at 25°C |
| 8–10 | Weakly alkaline | Air Scrubber neutralization target zone |
| 11–14 | Strongly alkaline | Sodium hydroxide, concrete leachate |

**Neutralization:** acid + base → salt + water. The Air Scrubber's alkaline
buffering stage uses this reaction to neutralize HCl from halogenated
polymer combustion. Sodium carbonate (washing soda) neutralizes ferric
chloride etch waste from PCB fabrication, producing iron hydroxide sludge.
Knowing the acid being neutralized determines the appropriate base and
the waste product generated.

**Buffer systems:** Solutions containing both a weak acid and its conjugate
base resist pH change when small amounts of acid or base are added. The
Air Scrubber's scrubbing liquid is a buffer system — it maintains neutralizing
capacity over time rather than shifting immediately to high pH. Buffer
capacity is exhausted when the weak acid or base is consumed — this is
the chemistry underlying AS-003 (saturation threshold).

#### 2.2 Forge-Relevant Acid and Base Streams

**Sulfuric acid (H₂SO₄):** Battery electrolyte. Present in every
lead-acid cell encountered in salvage. Concentrated sulfuric acid
causes severe burns and rapidly destroys most metals. Dilute sulfuric
acid (battery grade, ~35%) is corrosive to skin, fabric, and many
metals. Neutralize with sodium bicarbonate or lime. Do not neutralize
on the battery — neutralize spills in a container.

**Hydrochloric acid (HCl):** Generated by combustion of PVC and other
chlorinated polymers. Also present in ferric chloride PCB etch waste.
Produces highly corrosive vapor that attacks metal surfaces, mucous
membranes, and concrete. The Air Scrubber alkaline buffering stage
exists specifically for HCl. See `Operations/Plastics.md` PL-001 and
`Operations/Air_Scrubber.md` for doctrine on managing this stream.

**Acetic acid:** Weak acid produced by wood decomposition, vinegar.
Low acute hazard but relevant for adhesive cure chemistry and some
surface treatment processes.

**Sodium hydroxide (NaOH) / caustic soda:** Strong base. Present in
some cleaning formulations and drain cleaners found in salvage streams.
Causes severe burns — equally dangerous to strong acid despite producing
no visible immediate reaction on skin. Neutralize acid spills cautiously.

**Ammonia (NH₃):** Weak base produced by biological decay and some
industrial processes. Vapor is strongly irritating. In combination with
copper alloys, ammonia causes stress corrosion cracking. Relevant in
biological waste streams at Gate_03.

---

### Section 2.3 — Solution Chemistry and Precipitation

Solution chemistry governs every wet process in the Forge. Precipitation,
solubility limits, scaling, and dissolved-metal behavior determine
scrubber saturation (AS-003), sludge formation in Gate_03 wet processing,
carbonate scaling in heat exchangers, iron hydroxide floc in runoff,
filter fouling, and water chemistry in Living Waters systems. These
phenomena are predictable chemical behaviors, not contamination or
failure signals.

#### 2.3.1 Solubility and Ionic Equilibria

Solubility is governed by the equilibrium between dissolved ions and the
solid phase:

```
Mⁿ⁺ + nX⁻ ⇌ MXₙ(s)
```

When the ionic product exceeds the solubility product (Ksp), precipitation
occurs.

**Forge-relevant Ksp values (order-of-magnitude only):**

| Compound | Ksp (approx.) | Implication |
|--------------|---------------|-------------|
| CaCO₃ | ~10⁻⁹ | Hard-water scaling in heat exchangers and wet scrubbers |
| Fe(OH)₃ | ~10⁻³⁸ | Iron hydroxide sludge forms readily once pH rises above ~3–4 |
| Mg(OH)₂ | ~10⁻¹¹ | Precipitates under alkaline conditions; reduces buffer capacity |
| CaSO₄ | ~10⁻⁵ | Gypsum scaling possible in high-sulfate streams |

**Operational rule:** Rising pH drives metal-hydroxide precipitation.
Rising carbonate concentration or CO₂ degassing drives Ca/Mg carbonate
precipitation. Both reduce effective reagent capacity and foul equipment.

#### 2.3.2 Precipitation in Scrubber Systems

The Air Scrubber's alkaline buffer neutralizes acids:

```
2HCl + Na₂CO₃ → 2NaCl + H₂O + CO₂↑
```

As local pH increases, dissolved iron (from corrosion products or
feedstock runoff) precipitates:

```
Fe³⁺ + 3OH⁻ → Fe(OH)₃(s)
```

This sludge reduces buffer capacity, fouls pumps and sensors, and
accelerates AS-003 saturation. **Doctrine:** Scrubber sump drainage and
filtration are expected maintenance, not failure indicators.
Cross-reference `Operations/Air_Scrubber.md` AS-003 and CE-005 resolution
path.

#### 2.3.3 Hard Water and Carbonate Scaling

Hard water (elevated Ca²⁺/Mg²⁺) produces scale when heated or when CO₂
degasses:

```
Ca²⁺ + CO₃²⁻ → CaCO₃(s)
```

Scaling reduces heat-exchanger efficiency, clogs spray nozzles, and
deposits in wet-processing lines. **Mitigation:** Periodic dilute acetic
or citric acid wash. Never use strong mineral acids on aluminum
components. Cross-reference `Architecture/Thermal_Systems.md` for
heat-exchanger fouling interactions.

#### 2.3.4 Filter Fouling and Floc Formation

Iron oxidation in wet environments produces floc:

```
Fe²⁺ → Fe³⁺ → Fe(OH)₃(s)
```

Floc clogs filters, increases pump load, reduces flow, and is a
diagnostic signature of upstream corrosion or MIC activity. **Doctrine:**
Treat the upstream corrosion source; do not treat floc as an isolated
filtration problem. Cross-reference §1.2 MIC and `Challenges/Biofouling.md`.

---

### Section 2.4 — Dilution Doctrine

Dilution is one of the highest-risk routine operations in chemical
handling. Incorrect order of addition produces violent boiling, acid
ejection, and severe burns.

**Fundamental rule:** Always add acid to water. Never add water to
concentrated acid.

Adding water to concentrated sulfuric or hydrochloric acid causes
instantaneous surface boiling and ejection of hot acid droplets.

**Heat of dilution:** Dilution of strong acids is strongly exothermic.
Perform slowly, with continuous stirring, in a heat-resistant container
(glass or HDPE). Allow the mixture to cool before further handling.

**Container compatibility (minimum):**
- Concentrated H₂SO₄ / HCl: glass or HDPE. Unsafe in steel, aluminum, or
  most concrete.
- NaOH solutions: HDPE. Attacks aluminum.
- Default when uncertain: HDPE.

**Minimum PPE for dilution operations:** face shield + chemical goggles,
chemical-resistant gloves (nitrile or better), long sleeves, and forced
ventilation. This is non-negotiable and aligns with
`Admin/Safety_Protocols.md`.

Cross-reference battery electrolyte handling (§6.1) and etch-waste
neutralization (`Operations/Electronics.md`). See CE-008.

---

### Section 3 — Oxidation-Reduction (Redox) Chemistry

Oxidation-reduction reactions involve the transfer of electrons between
chemical species. Corrosion is a redox process. Combustion is a redox
process. The Spin Chamber's separation of metal streams by density exploits
the different redox histories of different alloy fractions. Understanding
oxidation state is foundational to understanding what the Forge's thermal
processing is actually doing to material.

#### 3.1 Oxidation States and Metal Recovery

A metal in its pure form has oxidation state zero. When it corrodes, it
loses electrons to become a positively charged ion (oxidized). When it is
reduced back to metal from an ore or oxide, it gains electrons (reduced).

```
Oxidation:    Fe → Fe²⁺ + 2e⁻    (iron rusts — loses electrons)
Reduction:    Fe²⁺ + 2e⁻ → Fe    (iron is smelted — gains electrons)
```

**Oxide layers:** Most common metals form an oxide layer spontaneously in
air. Aluminum oxide (Al₂O₃) is dense and adherent — it passivates the
surface and dramatically slows further corrosion. Iron oxide (Fe₂O₃ —
rust) is porous and non-adherent — it does not passivate and allows
corrosion to continue beneath it. This is why aluminum corrodes slowly
in air while iron corrodes progressively.

**Forge implication for separation:** Heavily oxidized metal surfaces in
the Spin Chamber feedstock carry oxide burden that affects melt chemistry,
alloy purity, and slag composition. Pre-reduction of feedstock (removing
oxide layers before melting) reduces slag volume and improves output
quality. This is a chemistry problem, not a thermal problem.

**Passivation:** The condition in which a metal surface is protected by a
dense, adherent oxide or other compound layer. Stainless steel is passive
in most environments; its chromium oxide layer is self-healing when
damaged. Passivation can be intentionally induced (phosphoric acid
treatment on steel, anodizing on aluminum) to improve corrosion resistance.
Passivation can be disrupted by chloride ions, which penetrate the passive
layer and initiate pitting — the mechanism behind stainless steel corrosion
in seawater.

#### 3.2 Combustion Chemistry Relevant to Forge Operations

Combustion is rapid oxidation releasing heat. The Forge encounters
combustion in pyrolysis syngas handling, biogas generation, and hot-work
fabrication operations. The key chemistry distinctions:

**Complete combustion** (sufficient oxygen):
```
CH₄ + 2O₂ → CO₂ + 2H₂O    (methane burns cleanly)
```

**Incomplete combustion** (insufficient oxygen):
```
2CH₄ + 3O₂ → 2CO + 4H₂O    (carbon monoxide produced)
```

Carbon monoxide (CO) is odorless, colorless, and lethal at low
concentrations. It is the primary acute hazard of incomplete combustion.
Any combustion process in a confined space without adequate ventilation
is a CO risk. Syngas combustion stages upstream of the Air Scrubber must
have confirmed combustion air supply — incomplete combustion that produces
CO defeats the scrubber.

**Halogen-containing combustion:**
```
PVC → HCl + various hydrocarbons (simplified)
```

Chlorinated polymers produce HCl gas under thermal decomposition. This
is not a minor impurity — a significant HCl fraction is produced per unit
mass of PVC. At pyrolysis temperatures, this becomes a corrosive gas that
attacks reactor walls, scrubber components, and operator airways. The
Beilstein test exists to catch this before the reactor does. See Section 4.

**Nitrogen oxides (NOₓ) formation:** High-temperature combustion of any
nitrogen-containing air or fuel produces thermal NOₓ:

```
N₂ + O₂ → 2NO
2NO + O₂ → 2NO₂
```

NO is colorless; NO₂ is brown and strongly irritating. Both are toxic and
form nitric/nitrous acids in the presence of moisture:

```
2NO₂ + H₂O → HNO₂ + HNO₃
```

**Hazards and scrubber load:** NOₓ causes acute respiratory injury,
increases wet-system corrosion, and adds an acid burden to the Air
Scrubber independent of HCl load. **Doctrine:** An unexplained scrubber
pH drop with low measured HCl may indicate NOₓ loading. Buffer
replacement frequency must increase during high-temperature or confined
combustion operations. Cross-reference `Operations/Air_Scrubber.md`
Stage D and AS-003.

**Mitigation:** Ensure excess combustion air (complete combustion reduces
both CO and thermal NOₓ). Control peak flame temperature where practical.
Treat scrubber pH monitoring as continuous, not snapshot. Route any
high-NOₓ exhaust through the wet caustic stage before discharge.

---

### Section 4 — Contamination Identification Chemistry

Field identification of chemical hazards with minimal laboratory equipment
is a core Forge capability. The following methods are the primary tools
at v0.

#### 4.1 The Beilstein Test (Halogen Detection)

**Purpose:** Detect the presence of chlorine, bromine, or fluorine in
a polymer sample before thermal processing. The Forge's primary screen
for PVC and other halogenated materials.

**Procedure:**
1. Heat a copper wire to red heat in a clean flame until no color change
   is produced (remove surface contamination).
2. Touch the heated wire briefly to a small sample of the material to
   be tested.
3. Return the wire to the flame.
4. A **green or blue-green flame** indicates halogen presence. The copper
   halide salt formed at the wire surface colors the flame.
5. No color change (yellow-orange from sodium impurities is normal) —
   halogen likely absent.

**Sensitivity:** Detects halogen content as low as a few percent by mass.
Reliable for PVC, PVDC, chlorinated PE, and Teflon. Less sensitive for
highly diluted halogen content.

**False positives:** Some nitrogen-containing compounds produce green
color. Verify with a second sample if result is ambiguous. When in doubt,
reject the material from thermal processing.

**Cross-reference:** `Operations/Plastics.md` PL-001 for the doctrine on
halogenated polymer rejection. This test is the gate that protects the
pyrolysis reactor and everyone downstream of it.

#### 4.2 pH Measurement

**Purpose:** Characterize acidity or alkalinity of liquid streams —
scrubber water, waste runoff, process water, battery electrolyte
assessments.

**Methods at v0:**
- **pH indicator strips** — sufficient for most Forge applications.
  Read against color chart. ±0.5 pH unit accuracy typical. Adequate
  for determining whether a stream is strongly acidic, neutral, or
  alkaline.
- **pH meter with electrode** — better accuracy (±0.1 pH unit), requires
  calibration with buffer solutions. Preferred for scrubber monitoring
  where saturation detection depends on pH tracking over time.
- **Visual indicators:** litmus (broad range), phenolphthalein
  (colorless below pH 8.2, pink above — useful for detecting alkalinity
  in scrubber buffer), universal indicator solution.

**Forge applications:** Air Scrubber sump pH monitoring (AS-003 saturation
detection), etch waste neutralization confirmation, battery electrolyte
characterization for salvaged cells, runoff monitoring in wet processing
areas.

#### 4.3 Visual and Olfactory Contamination Indicators

Chemical training matters here: the goal is pattern recognition, not
analytical precision.

> **Doctrine: Odor is a warning signal, never a clearance signal.**
> The absence of odor does not mean the absence of hazard. H₂S causes
> rapid olfactory fatigue — concentration can remain lethal after you
> stop smelling it. CO is odorless at all concentrations. A space that
> smells safe may not be safe. Ventilate, test, and hold.

| Indicator | Possible Contaminant | Action |
|-----------|---------------------|--------|
| Sweetish / ether-like odor | Solvents (acetone, MEK, ethyl acetate) | Ventilate, avoid ignition sources |
| Rotten egg odor (H₂S) | Sulfide contamination, MIC activity, battery failure | Evacuate immediately — H₂S is rapidly lethal |
| Sharp / bleach-like odor | Chlorine gas, HCl vapor | Evacuate, do not re-enter without respiratory protection |
| Ammonia odor | Biological decay, cleaning agents | Ventilate; check for copper alloy components nearby |
| Oily / petroleum odor | Hydrocarbon contamination | Fire risk; separate from ignition; route to pyrolysis feedstock assessment |
| Blue-green staining on metal | Copper corrosion products | Indicates copper present; galvanic concern in mixed-metal assembly |
| Black deposit at pitting site | Iron sulfide — MIC signature | Structural assessment required; biofouling-driven corrosion |
| White efflorescence on concrete | Calcium carbonate / leachate | pH monitoring; may indicate alkaline runoff affecting nearby water |

**Critical warning:** H₂S causes rapid olfactory fatigue — you stop
smelling it before the concentration drops to safe levels. Never re-enter
an area that smelled of rotten eggs without confirmed ventilation and
gas monitoring. The Beilstein test, pH measurement, and visual indicators
are always safer than relying on smell alone for chemical assessment.

---

### Section 5 — Polymer Degradation Chemistry

Understanding why specific polymer classes are hazardous at elevated
temperatures is load-bearing knowledge for every Forge operator. The
hazard is not in the solid plastic — it is in what the plastic becomes
when heated.

#### 5.1 Thermal Degradation Pathways

Polymers are long-chain molecules. At elevated temperatures, those chains
break — a process called thermal degradation or pyrolysis. The products
depend on the polymer's chemistry.

**Polyolefins (PE, PP):** Degrade to shorter-chain hydrocarbons —
paraffins, olefins, and eventually smaller gases. No intrinsically toxic
breakdown products at moderate temperatures, though combustion products
include CO under oxygen-limited conditions. The primary feedstock for
productive pyrolysis.

**Polystyrene (PS):** Degrades to styrene monomer and other aromatic
hydrocarbons. Styrene is a suspected carcinogen and strong sensory
irritant. Higher hazard than polyolefins.

**PVC (polyvinyl chloride):** Contains ~57% chlorine by mass. At elevated
temperatures, the chlorine is released as HCl gas before the carbon
backbone pyrolyzes. HCl evolution begins around 200°C — well below
productive pyrolysis temperatures. Cannot be safely co-processed with
other polymers. **Hard rejection at triage is the only acceptable
doctrine.** See `Operations/Plastics.md` PL-001.

**PTFE (Teflon) and fluoropolymers:** Thermally stable but decompose
above ~400°C to produce highly toxic perfluorinated compounds including
PFIB (perfluoroisobutylene), which is lethal at sub-ppm concentrations.
Teflon coating on cookware produces toxic fumes at temperatures achievable
on a domestic stove. In a pyrolysis reactor, fluoropolymer contamination
is acutely dangerous.

**Brominated flame retardants (BFRs):** Not a polymer class themselves
but additives found in electronics housings, foam, and textiles. Release
brominated dioxins and furans under thermal decomposition — persistent
organic pollutants with severe long-term toxicity. The hazard from
CNC milling of old PCBs (EL-005) is partly BFR dust. The hazard from
bulk furnace reflow of electronics is partly BFR vapor. Air Scrubber
operation is non-negotiable for any thermal processing of electronics
waste.

#### 5.2 Identifying Polymer Classes in the Field

When database lookup is unavailable and the polymer class is unknown:

| Test | Polyolefin (PE/PP) | PVC | PS | Nylon |
|------|--------------------|-----|-----|-------|
| Beilstein | No color | Green flame | No color | No color |
| Float in water | Floats | Sinks | Floats | Sinks |
| Burn behavior | Burns slowly, drips, waxy odor | Chars, self-extinguishes, HCl odor | Burns readily, black smoke, sweet odor | Burns slowly, self-extinguishes, celery odor |
| Flexibility | Flexible to semi-rigid | Rigid or flexible | Rigid, brittle | Tough, semi-rigid |

**Default doctrine for unidentified polymers:** If Beilstein is positive
or if burn behavior suggests halogen (self-extinguishing, HCl-like odor),
reject from thermal processing regardless of other characteristics.
The asymmetry is correct: the cost of rejecting a non-halogenated
polymer is a missed feedstock opportunity. The cost of processing a
halogenated polymer is a damaged reactor, HCl exposure, and possible
dioxin generation.

---

### Section 6 — Battery and Electrochemical Cell Chemistry

Salvaged batteries appear throughout the Forge intake stream. Understanding
the electrochemistry determines how they are assessed, handled, and either
recovered or safely disposed of.

#### 6.1 Common Cell Chemistries in Salvage Streams

**Lead-acid:** Electrolyte is dilute sulfuric acid (~35% H₂SO₄ by mass).
Produces hydrogen gas during charging — explosive at 4% concentration in
air. Sulfation (lead sulfate crystal growth) is the primary aging failure
mode; partially reversible with slow charging. Sulfuric acid spills are
acute hazards. Heavy — high energy density per dollar but poor energy
per kilogram. Widely available in salvage.

**Lithium-ion (various cathode chemistries — LCO, NMC, LFP, NCA):**
No liquid electrolyte hazard under normal conditions, but thermal runaway
produces highly toxic HF (hydrofluoric acid) vapor from electrolyte
decomposition. HF causes severe, delayed-onset chemical burns that
penetrate tissue before pain signals occur. Puncture, crush, overcharge,
and deep discharge are the primary thermal runaway triggers. State of
health (SoH) assessment before any Forge use is mandatory — see EV-003.
LFP chemistry is significantly more thermally stable than NMC or LCO.

**Nickel-metal hydride (NiMH):** Alkaline electrolyte (potassium
hydroxide). Less acute hazard than lithium-ion. Memory effect (reduced
capacity from incomplete discharge cycles) is manageable. Common in
older consumer electronics and hybrid vehicle packs in salvage.

**Nickel-cadmium (NiCd):** Alkaline electrolyte. Cadmium is a severe
cumulative toxin — cadmium dust from damaged cells is a critical hazard.
Largely phased out but still present in older industrial and power tool
salvage. Handle with appropriate respiratory protection. Cadmium
contamination of soil and water is an environmental risk.

#### 6.2 Cell Assessment Without Laboratory Equipment

**Open-circuit voltage (OCV):** Measure with a multimeter at cell
terminals without load. Indicates state of charge, not state of health,
but severe voltage depression (well below nominal) suggests sulfation
or deep discharge damage.

| Chemistry | Nominal Voltage | Healthy OCV (fully charged) | Concern Threshold |
|-----------|----------------|----------------------------|-------------------|
| Lead-acid (12V) | 12V | 12.6–12.8V | <11.8V |
| Li-ion (single cell) | 3.6–3.7V | 4.1–4.2V | <3.0V |
| LFP (single cell) | 3.2V | 3.4–3.6V | <2.8V |
| NiMH (single cell) | 1.2V | 1.35–1.4V | <1.0V |

**Load test:** Apply a known resistive load for 30 seconds. Measure voltage
under load. Significant voltage drop under load with recovery when load is
removed indicates high internal resistance — capacity loss, sulfation, or
aging. A battery that cannot hold voltage under load is not useful regardless
of its OCV.

**Visual indicators of failure:** Swelling or bulging (lithium-ion —
gas generation from electrolyte decomposition, elevated thermal runaway
risk), leakage (any chemistry — electrolyte exposure, immediate containment
required), corrosion at terminals (increased internal resistance,
connection quality concern), case damage or puncture (lithium-ion —
treat as immediate thermal runaway risk, isolate and observe outdoors).

**Forge doctrine:** Salvaged batteries with unknown SoH enter the
system as unknown-state components until assessed. See `Operations/Energy.md`
EV-003 for containment requirements before commissioning in an enclosed
installation.

---

### Section 7 — Surface Chemistry: Adhesion, Passivation, and Coatings

Surface chemistry governs how materials bond to each other, how they
resist environmental attack, and how treatments change their behavior.

#### 7.1 Surface Energy and Adhesion

Surface energy is the thermodynamic work required to create a new surface —
essentially how much the material "wants" to be bonded to something.
High surface energy materials (metals, glass, ceramics) adhere well to
most adhesives. Low surface energy materials (polyolefins, PTFE) repel
adhesives and resist adhesion.

**Contact angle** is the practical measurement: a water droplet on a high
surface energy surface spreads flat (contact angle near 0°). On a low
surface energy surface, it beads up (contact angle near 90° or above).

**Forge implication:** Welding, bonding, and coating salvaged surfaces
requires understanding what is on the surface before attempting adhesion.
Oil, oxide, release agents, and polymer coatings all reduce surface energy
and compromise bond quality. Surface preparation (grinding, solvent wipe,
acid etch) changes the chemistry of what the adhesive or weld is actually
bonding to.

#### 7.2 Passivation and Protective Treatments

**Phosphating:** Iron phosphate conversion coating on steel. Provides
mild corrosion resistance and an excellent adhesion base for paint.
Applied from dilute phosphoric acid solution. Produces a gray or dark
surface that cannot be confused with bare metal.

**Anodizing:** Electrochemical growth of aluminum oxide layer on aluminum
alloys. Thicker and harder than the native oxide. Can be sealed for
improved corrosion resistance or dyed for identification. Requires
controlled electrolyte bath and DC power. Candidate for v1+ capability.

**Blackening / oxide treatments on steel:** Hot caustic blackening
(hot bluing) produces magnetite (Fe₃O₄) surface layer with mild corrosion
resistance and characteristic black appearance. Cold blackening uses
selenium dioxide — toxic, not recommended without appropriate containment.

**Cerakote / ceramic coatings:** Polymer-ceramic composite applied by
spray and baked. Excellent chemical and abrasion resistance. Requires
spray equipment and curing oven. Commercially available; not
self-producible at v0.

**Wax and oil treatments:** Simplest and most bootstrap-compatible
protection. Lanolin, linseed oil, and cosmoline (petroleum-based
preservative) displace moisture and provide barrier protection. Not
permanent — requires periodic reapplication. Entirely appropriate for
v0 component storage and short-term corrosion protection of fabricated
parts.

---

### Section 8 — Forge Chemical Integration Map

| Downstream File | Relevant Sections | Dependency |
|----------------|-------------------|------------|
| `Operations/Plastics.md` | §4.1 (Beilstein test), §5.1–5.2 (polymer degradation chemistry) | Halogenated polymer rejection doctrine is built on these principles |
| `Operations/Electronics.md` | §4.2 (pH for etch waste), §5.1 (BFR degradation), §6.1–6.2 (battery chemistry) | PCB etch neutralization, BFR hazard awareness, salvaged cell assessment |
| `Operations/Air_Scrubber.md` | §2.1–2.2 (acid-base, HCl neutralization), §3.2 (combustion chemistry) | Scrubber chemistry design and saturation monitoring are acid-base problems |
| `Operations/Gate_05_Separation_Thermal.md` | §3.1 (oxidation states, oxide burden), §3.2 (combustion in thermal processing) | Spin Chamber separation exploits redox chemistry; oxide burden affects melt |
| `Operations/Gate_03_Reduction.md` | §5.1 (combustion products from mixed feedstock), §4.3 (contamination indicators) | Reduction of chemically contaminated feedstock produces hazardous off-gas |
| `Operations/Energy.md` | §6.1–6.2 (battery chemistry, cell assessment) | EV-003 salvaged battery containment doctrine depends on chemistry understanding |
| `Tests/Support_Raft.md` | §1.1–1.3 (galvanic series, MIC, cathodic protection) | SR-001 galvanic corrosion mitigation is an applied electrochemistry problem |
| `Challenges/Biofouling.md` | §1.2 (MIC mechanism), §1.3 (cathodic protection) | MIC is the chemical mechanism behind the most severe biofouling corrosion |
| `Architecture/Mechanical_Structures.md` | §1.1 (galvanic compatibility of mixed-metal salvage assemblies) | Dissimilar metal fasteners in humid environments create galvanic cells |
| `Operations/Gate_01_Intake.md` | §4 (contamination identification methods) | GI-003 augmented detection capability is partly chemical field testing |
| `Operations/Gate_02_Triage.md` | §5.2 (polymer identification), §4.1 (Beilstein) | Station 0 contamination check includes chemical identification |
| `Operations/Woodworking.md` | §2.2 (acid behavior relevant to wood tannin chemistry), §7.2 (surface treatments) | Finishing and wood-metal interaction chemistry |

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|--------------|----------------|-------------|------------------|------------|---------------------|
| 2026-06-02 | Modeling / doctrine | — | — | File created; no operational chemistry lessons yet | — | At first operational chemical processing event |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-02 | Including specific product specifications and brand recommendations | Product availability varies by location and changes over time; principle-level doctrine is durable where specific products are not | No — principle-level doctrine is the correct scope |
| 2026-06-02 | Including regulatory compliance guidance | Jurisdiction-dependent; rapidly changing; requires legal expertise not available at repository level | No — human governing party decision |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Galvanic series table revised without a documented source and confidence label
- Beilstein test procedure modified without a cross-reference update to
  `Operations/Plastics.md` PL-001
- Battery chemistry section revised without cross-reference update to
  `Operations/Energy.md` EV-003
- Scope boundary revised to absorb polymer processing procedures from
  `Operations/Plastics.md` or etch chemistry procedures from
  `Operations/Electronics.md`
- MIC mechanism description diverges from `Challenges/Biofouling.md`
  without a logged reconciliation entry
- Contamination identification section loses Beilstein test or H₂S
  olfactory fatigue warning
- Integration map loses coverage of a file that has introduced chemical
  or electrochemical design decisions
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### CE-001 — Galvanic corrosion rates for salvaged mixed-metal assemblies not characterized

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-06-02 |
| Last Reviewed | 2026-06-11 |

**Description:** Section 1.1 provides the galvanic series and area-ratio
doctrine, but actual corrosion rates for specific salvage-relevant metal
pairings in the Forge's high-humidity RDC operating environment are not
characterized. Published corrosion data assumes specific environments and
alloy compositions that may not match salvage stock. Builders in arid or
coastal environments should note their corrosion baseline differs from
the RDC — substitute via `Architecture/Facilities.md` §VII.

**Why It Matters:** Structural lifetime predictions for mixed-metal Forge
assemblies cannot be made without environment-specific corrosion rate data.
Under-prediction leads to unexpected structural failure; over-prediction
leads to excessive material use in protective coatings and anodes.

**Resolution Path:** Compile from ASM corrosion data handbooks for
steel-aluminum, steel-copper, and aluminum-copper pairings in humid
subtropical environments. Label as Analogous until first operational
corrosion monitoring data from deployed hardware exists. Cross-reference
EN-001 (validated safety factors for salvaged materials) — corrosion rate
data feeds structural derating factors for humid environments.

---

### CE-002 — Oxide burden effect on Spin Chamber output quality not quantified

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical — cross-module |
| Blocking | No |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-06-02 |
| Last Reviewed | 2026-06-02 |

**Description:** Section 3.1 establishes that oxide layers on feedstock
affect Spin Chamber melt chemistry and slag composition, but the
quantitative relationship between feedstock oxidation state and output
quality is not defined.

**Why It Matters:** Heavily rusted or oxidized salvage feedstock may
produce significantly different Spin Chamber outputs than clean feedstock.
Without characterization, output quality claims cannot be made and wire
extrusion quality (SC-004) cannot be predicted from feedstock condition.

**Resolution Path:** During first Spin Chamber operational runs, vary
feedstock oxidation state deliberately (clean vs. heavily oxidized
samples of known composition) and measure output differences. Cross-reference
SC-002 (segregation effectiveness) — oxide burden is a confounding variable
in segregation experiments.

---

### CE-003 — Field polymer identification reliability not validated for mixed salvage stream

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | **Critical** |
| Priority | **Critical** |
| Type | Technical / Safety |
| Blocking | **Yes — blocks first hot pyrolysis run** |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-06-02 |
| Last Reviewed | 2026-06-11 |

**Description:** Section 5.2 polymer identification table and Section 4.1
Beilstein test are established methods, but their combined reliability for
correctly identifying polymer class in actual mixed salvage streams — with
aged, contaminated, multi-layer, and composite materials — has not been
validated at Forge operating conditions.

**Why It Matters:** False negatives on halogenated polymer detection are
the critical failure mode. A PVC-containing material that passes the
Beilstein test and enters the reactor produces HCl and potentially dioxins.
Real salvage plastics are messy — multi-layer packaging, contaminated
feedstocks, brominated housings, weathered polymers, fillers, and coatings
are exactly where laboratory identification assumptions fail. PL-001
(hard rejection doctrine) depends on the correctness of this identification.
If CE-003 fails, PL-001 fails with it.

**Resolution Path:** Validate Beilstein test and polymer identification
table against a representative sample of real salvage plastic stream
(minimum 50 items from intake, spanning multiple material types, ages,
and contamination states). Document false positive and false negative
rates. This validation is a mandatory prerequisite before first hot
pyrolysis run. Cross-reference PL-001.

---

### CE-004 — Chemical Operator Minimum Competency

| Field | Value |
|-------|-------|
| Status | **In Progress** |
| Risk | High |
| Priority | Major |
| Type | Governance / Safety |
| Blocking | No |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-06-02 |
| Last Reviewed | 2026-06-11 |

**Description:** CE-ASM-001 assumes basic chemistry literacy. The minimum
competency standard for Forge operators handling chemical streams is not
formally defined as a testable checklist. Converted from open unknown to
In Progress — core checklist content promoted to Appendix A of this file.
Formal sign-off and integration with `Admin/Engineer_Protocols.md` remain
open.

**Resolution Path:** Appendix A (Chemical Operator Minimum Competency)
is the resolution artifact. Closure requires: (1) integration with
`Admin/Engineer_Protocols.md` operator training doctrine, (2) designated
sign-off mechanism for Forge instance initialization.

---

### CE-005 — Solution chemistry and precipitation doctrine not established

| Field | Value |
|-------|-------|
| Status | In Progress |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-06-11 |
| Last Reviewed | 2026-07-31 |

**Description:** Solubility, precipitation, scaling, hard water behavior,
and dissolved metal dynamics are now addressed in full at Section 2.3
(2026-07-31 — Ksp table, scrubber precipitation, hard-water scaling, and
filter-fouling/floc doctrine added, verified against source before
insertion). These phenomena affect Air_Scrubber scrubber buffering
saturation (AS-003), wet processing in Gate_03, Living Waters
condensation water quality, and biofouling chemistry.

**Why It Matters:** A scrubber that silently scales over weeks loses
effectiveness without obvious failure signal. Iron hydroxide precipitation
in wet processing creates sludge that fouls equipment and requires disposal
doctrine (GR-003). Hard water reduces reagent efficiency in neutralization
operations.

**Resolution Path:** Section 2.3 stub expanded into full qualitative
doctrine (2026-07-31) — Ksp values, scaling prediction, hard-water
treatment, and floc/sludge diagnosis are now documented. Two items remain
before full Resolution: (1) quantitative Ksp validation against actual
Forge feedstock streams rather than order-of-magnitude literature values;
(2) sludge disposal routing to GR-003 — note `Operations/Gate_03_Reduction.md`
currently shows GR-003 itself as "not yet assigned," so this dependency is
presently blocked on that file, not on Chemistry.md. Remains In Progress,
not Resolved, until both close.

---

### CE-006 — Chlorine containment doctrine undefined for on-site chlor-alkali acid synthesis

| Field | Value |
|-------|-------|
| Status | In Progress |
| Risk | High |
| Priority | Critical |
| Type | Technical / Safety |
| Blocking | Yes (for `Challenges/Closed_Loop_Feedstock.md` CLF-004 candidate pathway) |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-07-07 |
| Last Reviewed | 2026-08-15 |

**Description:** A candidate pathway logged in `Challenges/Closed_Loop_Feedstock.md` CLF-004 proposes on-site acid synthesis via salt-water electrolysis with a homemade ion-selective membrane (chlor-alkali-type process), using salt, water, and electricity as precursors. Standard chlor-alkali electrolysis co-produces chlorine gas at the anode. No containment, venting, or scrubbing doctrine exists in this file for that byproduct.

**Why It Matters:** `Admin/Ethical_Constraints.md`'s §Toxic and Hazardous Material Handling prohibits active release and permits only passive encapsulated use. Chlorine gas is acutely toxic even at low concentration — this file's own Navigation Anchors already list it among the toxic gases requiring warning-signal doctrine, not clearance-signal doctrine. CLF-004 cannot adopt this pathway as a resolution until a containment answer exists here; without one, the candidate remains an idea rather than a viable option.

**Resolution Path:** ~~Define minimum containment doctrine for small-scale chlor-alkali electrolysis~~ — superseded 2026-07-19 by the mechanism correction above. Route this pathway's chlorine off-gas through `Operations/Air_Scrubber.md` Stage D (Wet Scrubbing / Water Column) with a caustic (NaOH) reagent dose, not through Stage E. Remaining work: (1) sealed reaction vessel design confirming no anode-side leak path before the scrubber stage; (2) caustic dosing rate and residence time adequate at this process's actual Cl₂ generation rate and flow (cross-reference `Operations/Air_Scrubber.md` AS-003 calibration doctrine); (3) detection/alarm threshold consistent with acute toxicity limits; (4) disposal-or-reuse routing for the resulting NaOCl liquor — see CE-007. Cross-reference back to `Challenges/Closed_Loop_Feedstock.md` CLF-004 once resolved.

**Directed approach, 2026-07-17 (human governing authority):** capture and nullification, not venting-with-treatment, is the proposed resolution direction — chlorine off-gas is fully captured before any point where release could occur, then chemically neutralized rather than merely scrubbed toward a lower-but-nonzero release. `Operations/Air_Scrubber.md`'s existing Stage E KMnO₄ chemisorption mandate (Spec Gates 3/6, already carrying an automated interlock sensor matrix per AS-003) is the most directly applicable existing mechanism — potassium permanganate and comparable alkaline scrubbing agents convert Cl₂ to less hazardous chloride/hypochlorite species, which is nullification in substance, not just dilution. This is a directional decision, not a completed one: it narrows what CE-006 needs to specify (verify chemisorption capacity and reaction kinetics are adequate at this process's chlorine generation rate and flow, and confirm sealed-vessel capture prevents any anode-side leak path before the scrubber stage) rather than choosing among unrelated containment strategies from scratch. **The governing caveat is unchanged and takes precedence over this directed approach if they ever conflict:** Attempt to do no harm. If capture-and-nullification cannot be verified adequate at the vessel and flow rates this process actually requires, that is a reason to hold the pathway, not to relax the standard.

**Mechanism correction, 2026-07-19 (Grok flag, cross-checked against source before adoption):** the 2026-07-17 directed approach's premise does not hold. Stage E's KMnO₄-impregnated-alumina bed is an oxidizing chemisorbent, purpose-built for reducing-species VOCs (CO, formaldehyde, light hydrocarbons) — Cl₂ is itself already an oxidizer, and there is no oxidation pathway for KMnO₄ to act on it through. Checked against a primary industrial gas-filtration manufacturer's own product catalog (PureAir® Filtration, chemisorbant media line, accessed 2026-07-19): their pure KMnO₄/alumina media (PureAir 4/8/12/12-SP — same media class as Stage E) is rated for H2S, SO2, NO2, NO, HCHO, mercaptan, dimethyl sulfide, phosphine, ethylene, and alcohol — **Cl₂ is absent from that list.** Chlorine appears only under their separate acid-gas media (Sulphasorb 2™), a dedicated chlorine emergency media (Safetysorb), or a blend explicitly combining permanganate media with acid-gas media (PP Blend) — the manufacturer maintains these as distinct product lines precisely because permanganate alone does not do this job. Stage E as currently specified is not a valid containment mechanism for this pathway's chlorine byproduct.

The correct mechanism is a wet caustic (NaOH) absorption stage, not Stage E's dry chemisorption bed — and `Operations/Air_Scrubber.md`'s **Stage D (Wet Scrubbing / Water Column)** is already architected for exactly this: a recirculating liquid loop with continuous chemical monitoring, the standard industrial form for chlorine gas absorption (Cl₂ + 2NaOH → NaCl + NaOCl + H₂O). This is not a new stage requirement — it's routing this pathway's off-gas through Stage D with a caustic reagent dose, rather than relying on Stage E. See `Operations/Air_Scrubber.md`'s own Resolution Log for the cross-referenced update.

**Turning the problem into a solution, 2026-07-19:** every caustic chlorine scrubber produces sodium hypochlorite (NaOCl) — dilute bleach — as its natural reaction product, not as a secondary waste to further process. Small-scale NaOH-scrubber-to-hypochlorite apparatus is an established, patented approach (US Patent 4,308,123, "Apparatus for the small-scale manufacture of chlorine and sodium hydroxide or sodium hypochlorite"), not a novel or speculative direction. Framing Stage D's output as **nullification-with-recoverable-value** rather than pure hazard neutralization is consistent with this file's own precedent (§ toward `Challenges/Closed_Loop_Feedstock.md`'s epigraph — "The Forge optimizes for the closure of loops, not the purity of outputs") and with `Operations/Air_Scrubber.md`'s existing Waste as a Managed Output doctrine, which already mandates testing captured material for reuse potential before hazardous immobilization. Sodium hypochlorite has direct salvage value as a disinfectant/sanitizer — relevant to `Challenges/Water.md`'s potable-water doctrine and general facility sanitation — rather than needing disposal. This does not relax any safety requirement: NaOCl solutions decompose over time (faster with heat, UV, and concentration), can release Cl₂ gas back if mismanaged, and are incompatible with several common reagents (sulfites, peroxide, acids) — see CE-007 below for the storage/stability/utility doctrine this introduces.

**Scrubber chemistry and operating parameters, 2026-07-31 (Grok, verified against standard chlor-alkali/wet-scrubbing references before adoption — closes item 2 of the four-item Resolution Path and provides the quantitative basis for item 1):**

*Primary absorption reaction:* Cl₂ + 2NaOH → NaOCl + NaCl + H₂O — fast, irreversible disproportionation (one Cl atom oxidized to +1 in hypochlorite, the other reduced to −1 in chloride). Stoichiometry (weight basis): 1 kg Cl₂ requires 1.128 kg NaOH (exact from molecular weights: 2×40.0/70.9) and yields ≈1.05 kg NaOCl+NaCl+H₂O combined. The reaction is strongly exothermic (≈1,460 kJ/kg Cl₂ absorbed) — temperature rise is a primary design constraint, not a side concern.

*Critical operating conditions:*

| Parameter | Preferred Range | Why It Matters |
|-----------|-----------------|----------------|
| pH / excess NaOH | pH ≥ 11–12 (or ≥ 0.5–2% free NaOH residual) | Ensures complete absorption and stabilizes NaOCl. Below ~pH 10–11, absorption slows and over-chlorination risk rises. |
| Temperature | Keep below 40–50°C (ideally < 30–35°C) | High temperature accelerates NaOCl-destroying side reactions and can boil the liquor, reducing mass-transfer efficiency. |
| NaOH concentration | Typically 5–20 wt% | Higher strength gives more capacity per volume but less thermal mass and higher rapid-temperature-rise risk; lower strength needs larger liquor volume. |
| Contact time / L:G ratio | Adequate packed-bed height or residence time + sufficient liquid recirculation | Reaction is essentially instantaneous once Cl₂ dissolves — gas–liquid contact (mass transfer), not reaction kinetics, is rate-limiting. |

**Over-chlorination hazard:** if free NaOH is exhausted, residual Cl₂ reacts with NaOCl to form HOCl, which disproportionates to chlorate (NaOCl + Cl₂ + H₂O → 2HOCl + NaCl; 2HOCl + NaOCl → NaClO₃ + 2HCl) — this destroys product value and can drop pH, risking Cl₂ re-evolution. Conductivity or ORP monitoring is preferred over pH probes for strong caustic solutions, since pH electrodes saturate above ~pH 14.

**Detection / alarm thresholds, 2026-07-31 (closes item 3 of the four-item Resolution Path):** Cl₂ is denser than air and accumulates in low-lying or poorly ventilated spaces; odor threshold (~0.08–0.3 ppm) is typically below occupational limits, but olfactory fatigue occurs rapidly — absence of odor is **never** a clearance signal, consistent with §4.3 doctrine. Given the Forge's remote, high-humidity operating context and limited continuous medical support, the conservative end of published exposure guidelines is the design target:

| Threshold | Value | Basis | Action |
|-----------|-------|-------|--------|
| Action / warning | ≤ 0.5 ppm | NIOSH REL (15-min ceiling) / AEGL-1 | Investigate, increase ventilation, or pause process |
| High alarm | 1–2 ppm | OSHA PEL ceiling / ERPG-1 / AEGL-2 (short duration) | Evacuate and isolate |
| Immediate danger | 10 ppm | NIOSH IDLH | Full emergency response, SCBA or equivalent, process shutdown |

Continuous monitoring with interlock capability (matching Air_Scrubber.md's existing AS-003 sensor-matrix doctrine) is the preferred engineering control over point-in-time checks. Materials for scrubber liquor contact: HDPE, PVC, FRP, or PTFE-lined; avoid aluminum, copper alloys, and mild steel. Properly designed packed or spray towers with excess caustic routinely achieve >99% Cl₂ removal in a single stage when pH and temperature are controlled — this is mature, well-characterized industrial chemistry, not a novel or speculative process for the Forge to pioneer.

**Status of the four-item Resolution Path after this pass:** item 2 (dosing rate/residence time) and item 3 (detection/alarm thresholds) now have a concrete quantitative and doctrinal basis above. Item 1 (sealed vessel design) now has a concrete conceptual/architectural sketch — see below — but not a built vessel. The calibration half of item 2 (matching these parameters to this specific process's actual, measured Cl₂ generation rate and flow) remains genuinely open regardless of the sketch's existence — it requires real flow-rate data, which paper doctrine cannot substitute for. This is the same category of gap `Challenges/Closed_Loop_Feedstock.md` CLF-003 has for its extrusion hardware: the chemistry and the acceptance criteria are now specified; the hardware that must be measured against them does not yet exist. CE-006 moves to **In Progress** (doctrine and conceptual design now complete) but stays short of Resolved pending that hardware.

**Vessel design sketch, 2026-07-31 (Grok, revised after two corrections; verified against Air_Scrubber.md source before adoption — addresses item 1):**

*Architecture:* Divided cell (diaphragm or ion-selective membrane, homemade or scavenged acceptable at v0). Anode compartment (Cl₂ generation) fully sealed, isolated from cathode compartment (H₂ + dilute NaOH). Anode headspace has exactly one gas exit — a single dedicated off-gas line running directly to Stage D's inlet, with no vents, pressure-relief-to-atmosphere, or secondary openings. Cathode-side H₂ is vented or captured separately and needs its own handling doctrine (not covered by CE-006).

*Non-negotiable design rules:*
1. **Single-path anode off-gas** — exactly one exit, routed exclusively to Stage D.
2. **Negative-pressure / liquid-seal protection** — leverages Stage D's already-existing negative-pressure operation (see Air_Scrubber.md) so any leak tendency is inward, not outward.
3. **Over-pressure relief routes only to Stage D** (or a dedicated secondary caustic scrubber) — never to atmosphere.
4. **Materials:** Anode compartment and Cl₂ line — PVC, CPVC, PTFE, glass, or FRP. Stage D's own wet side may use **316L stainless**, already approved under Air_Scrubber.md's Corrosion Isolation doctrine for halogenated exhaust; "avoid most steels" applies to the anode/Cl₂-line side, not to Stage D's already-vetted hull material.
5. **Instrumentation and interlocks:** Anode-side Cl₂ detector using the thresholds above (≤0.5 ppm warning, 1–2 ppm high alarm, 10 ppm IDLH); Stage D free-NaOH/conductivity/ORP monitoring. **Hard prerequisite, not assumed infrastructure:** AS-003 calibration must be complete and the interlock system no longer operating on estimated values before this vessel is permitted to run — AS-003 is currently In Progress, blocked on the Gate 4 Cold Verification Harness running first.

*Thermal management — explicit requirement, not a generic "heat balance TBD":* Stage D already carries a hard Thermal Sink Requirement (see `Operations/Air_Scrubber.md`), logged after a 2026-05 audit finding where Stage D was specified without one and hot exhaust overwhelmed the scrubbing liquid's quench capacity — a hidden failure mode. The Cl₂ + NaOH reaction adds a **second, independent heat load** (≈1.46 MJ/kg Cl₂ absorbed) on top of whatever this vessel's Stage D deployment is already sized for from other exhaust sources. Any CE-006 thermal-sink sizing must be calculated as the **sum** of the existing design heat load plus this reaction's exotherm at the maximum intended Cl₂ generation rate — not treated as a separate, smaller, or optional calculation.

*Operating sequence (with gates, not just steps):* (1) confirm Stage D circulating with verified excess caustic **and** AS-003 interlocks calibrated and live; (2) confirm thermal-sink capacity adequate for the combined heat load; (3) fill cell, close all anode openings except the single off-gas line; (4) apply DC current only after gates 1–2 are satisfied; (5) Cl₂ flows solely to Stage D, absorbed as NaOCl+NaCl; (6) monitor free-NaOH residual, stop or replenish before over-chlorination; (7) recover NaOCl liquor per CE-007.

*Remaining quantification (genuinely open, not paper-closeable):* membrane/diaphragm selection and sealing method; first-article Cl₂ generation rate (suggested starting envelope 10–100 g/h); explicit thermal-sink sizing calculation combining both heat loads; fail-safe interlock behavior if Stage D recirculation or power is lost (cell must stop, not merely alarm).

This sketch closes item 1 of the four-item Resolution Path at the conceptual/architectural level — a concrete, evaluable vessel design now exists where none did before. It does not close it at the hardware level: no vessel has been built, AS-003 is not yet calibrated, and the combined thermal-sink calculation has not been performed. CE-006 moves to **In Progress** — this is architecture, not a finished system.

**Spec-depth pass, 2026-08-15 (digital-only — no equipment exists yet to generate operational data; three of the four remaining quantification items are paper-closeable regardless, one is not):**

*Generation-rate model (grounds the "10–100 g/h" envelope in electrochemistry rather than an arbitrary guess):* Faraday's law gives Cl₂ production directly from current: mass rate = (I × M × η) / (n × F), where I = current (A), M = 70.9 g/mol (Cl₂), n = 2 (electrons per Cl₂ molecule), F = 96,485 C/mol, η = current efficiency (chlor-alkali cells typically 90–97% at reasonable current density; use 0.90 as a conservative v0 planning figure). Worked examples at that efficiency:

| Current | Cl₂ rate |
|---|---|
| 5 A | ≈5.9 g/h |
| 20 A | ≈23.6 g/h |
| 50 A | ≈59 g/h |
| 100 A | ≈118 g/h |

The previously-stated 10–100 g/h envelope corresponds to roughly 8–85 A at this efficiency — a plausible range for salvage-sourced DC supply and small electrode area. This does not select a final design current (that depends on electrode area and acceptable current density, still open); it gives the vessel design a formula to plug a chosen current into rather than treating the g/h figure as asserted.

*CE-006's own exotherm, as a function of that same rate (not yet a combined total):* Q = 1.46 MJ/kg × Cl₂ rate. At the worked examples above: 5.9 g/h ≈ 2.4 W; 23.6 g/h ≈ 9.6 W; 59 g/h ≈ 24 W; 118 g/h ≈ 48 W (continuous-equivalent). This term is now a formula ready to add to Stage D's base exhaust heat load — but that base load is still Placeholder (`Operations/Air_Scrubber.md` ASM-004, pending `Gate_05_Separation_Thermal.md` exhaust characterization), which is real operational data no amount of paper work substitutes for. **The combined thermal-sink number stays open until Gate_05 produces that figure — this pass narrows what's missing to exactly one still-unknown term, it does not close the calculation.**

*Fail-safe interlock behavior on loss of Stage D recirculation or power (fully paper-specifiable, addresses the interlock item):* DC supply to the anode compartment is wired through Stage D's recirculation-pump and power-monitoring circuit as a hard series interlock, not a software-polled check — loss of circulation flow or Stage D power immediately opens the DC supply's contactor, stopping Cl₂ generation at the source within the same fault-detection latency Air_Scrubber.md's own Fault 04 pathway already uses. This is a stop, not an alarm: per the file's own governing caveat, a fault state that only alarms while generation continues is not acceptable for an acutely toxic gas with no vent path. No new sensor class is required — it reuses Stage D's existing flow/power monitoring as the interlock's own trigger rather than adding a duplicate detection layer.

*Membrane/diaphragm candidates (narrows options; final selection still requires sourcing/testing, correctly left open):* At v0 salvage-first scope, two realistic candidate classes: (a) a simple porous ceramic or asbestos-free diaphragm (lower selectivity, higher NaCl carryover to cathode side, but salvageable from ceramic filter stock or fabricable from Gate_04/06 material streams) versus (b) a cation-exchange membrane (Nafion-type or equivalent), which gives cleaner separation and lower H₂/Cl₂ cross-contamination risk but is not a plausible salvage item — it would be an external dependency, which CLF-004's closed-loop premise (already cross-referenced above) requires registering explicitly if pursued. Diaphragm-first is the doctrine-consistent default for v0; membrane remains a documented upgrade path, not a v0 requirement.

**Status after this pass:** membrane/diaphragm selection narrowed to two candidate classes (final choice still open); first-article generation rate now has a formula tying current to output (specific current still open, pending electrode-area decision); thermal-sink calculation has CE-006's own term fully specified as a formula, with the combined total correctly still blocked on Gate_05's exhaust-load data; fail-safe interlock behavior now fully specified at the doctrine level. Of the four "genuinely open, not paper-closeable" items from 2026-07-31, three now have real paper specification; the fourth (combined thermal-sink number) remains honestly blocked on hardware-derived data, not something this pass claims to have closed. CE-006 stays **In Progress** — no claim of Resolved.

---

### CE-007 — Sodium hypochlorite byproduct storage, stability, and reuse doctrine undefined

| Field | Value |
|-------|-------|
| Status | In Progress |
| Risk | Medium |
| Priority | Major |
| Type | Technical / Safety |
| Blocking | No — CE-006's containment resolution does not depend on this; only the value-recovery framing does |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-07-19 |
| Last Reviewed | 2026-07-31 |

**Description:** CE-006's Stage D caustic-scrubbing mechanism produces sodium hypochlorite (NaOCl) liquor as its natural output. No file in the repository currently defines storage concentration limits, decomposition/venting risk over time, incompatible-reagent doctrine, or a downstream utility pathway (disinfection, sanitation, or other reuse) for this output. Without this, CE-006's captured chlorine converts from an atmospheric hazard into a stored chemical hazard with no governing doctrine.

**Why It Matters:** NaOCl solutions decompose over time — faster with heat, UV exposure, and higher concentration — releasing Cl₂ gas back if stored improperly, which would silently defeat CE-006's containment purpose. NaOCl is also incompatible with several common reagents (sulfites, hydrogen peroxide, acids), creating a secondary hazard-mixing risk if stored near other Forge chemical streams without labeling/segregation doctrine. `Admin/Ethical_Constraints.md`'s do-no-harm standard applies to this stored output exactly as it does to the original gas.

**Storage, stability, and reuse doctrine, 2026-07-31 (Grok, verified against standard hypochlorite chemistry before adoption — addresses all four Resolution Path items below):**

*Decomposition pathways:* NaOCl decomposes via two main routes — thermal/concentration-driven chlorate formation (3NaOCl → NaClO₃ + 2NaCl, dominant under alkaline conditions) and oxygen-evolving decomposition (2NaOCl → 2NaCl + O₂, catalyzed by transition metals, UV, or heat). Decomposition rate roughly doubles to quadruples per +10°C, and accelerates with higher concentration, UV/sunlight exposure, and transition-metal impurities (Fe, Cu, Ni, Co).

*Acidification risk (the failure mode that most directly threatens CE-006's containment purpose):* if liquor pH falls below ~4–5 (especially < 2), the equilibrium HOCl + Cl⁻ + H⁺ ⇌ Cl₂(aq) + H₂O → Cl₂(g) shifts toward free chlorine gas release — the classic "bleach + acid = chlorine gas" hazard. This is why segregation from acids is not a generic chemical-safety footnote here but a direct reopening path for CE-006 if violated.

**(1) Storage concentration and container material:** Store cool, dark, and at high pH (>11–12) to minimize decomposition. HDPE, PVC, FRP, or PTFE-lined containers; avoid most metals (especially aluminum, copper alloys, mild steel), consistent with CE-006's own scrubber-materials doctrine above.

**(2) Decomposition monitoring / blowdown schedule:** Periodic blow-down or batch replacement is required as NaOCl + NaCl accumulate and free NaOH is consumed in the scrubber liquor loop itself; stored product should be used or diluted before significant decomposition occurs rather than held indefinitely at high concentration.

**(3) Segregation/incompatibility doctrine:** Segregate from acids, sulfites, peroxides, and ammonia to prevent Cl₂ re-evolution or violent reactions. Cross-reference `Admin/Safety_Protocols.md` for general incompatible-reagent storage doctrine.

**(4) Downstream utility pathway:** The liquor is a usable dilute bleach stream with direct salvage value as a disinfectant/sanitizer — cross-reference `Challenges/Water.md` for potable-water disinfection use, or general facility sanitation, as the most direct application. This chemistry is mature and well-characterized (small-scale NaOH-scrubber-to-hypochlorite apparatus is an established, patented approach — US Patent 4,308,123), not a novel or speculative direction for the Forge to validate from scratch.

**Resolution Path:** All four items above now have doctrinal answers. Remaining before full Resolution: quantitative sizing (actual storage volume, blowdown frequency, and NaOCl concentration) depends on CE-006's own remaining hardware gap (sealed vessel design, actual Cl₂ generation rate) — this file cannot close ahead of CE-006's vessel-design item. Payment via Specification once CE-006's hardware exists and these doctrinal answers are calibrated against real flow/volume data.

---

### CE-008 — Dilution doctrine competency validation not established

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Minor |
| Type | Technical / Safety |
| Blocking | No |
| Owner | `Architecture/Chemistry.md` |
| First Logged | 2026-07-31 |
| Last Reviewed | 2026-07-31 |

**Description:** Section 2.4 (Dilution Doctrine) documents the acid-to-water rule, heat-of-dilution hazard, container compatibility, and minimum PPE for dilution operations — added 2026-07-31. This is qualitative safety doctrine, not yet a validated operator competency item. It is distinct from CE-004 (Chemical Operator Minimum Competency), which already exists and is In Progress with its own Appendix A checklist; CE-008 is registered separately to avoid colliding with that existing ID.

**Why It Matters:** Dilution is one of the highest-risk routine chemical operations in the Forge — incorrect order of addition produces violent boiling, acid ejection, and severe burns. Written doctrine alone does not confirm operators will follow it correctly under real conditions.

**Resolution Path:** Add a dilution-specific item to CE-004's Appendix A competency checklist (cross-reference, do not duplicate content) once that checklist is next revised. Payment via Specification once dilution competency is folded into the existing Appendix A structure rather than maintained as a separate standalone check.

---

### Resolution Log

- 2026-08-15: **CE-006 spec-depth pass — digital-only, no equipment exists.**
  Given James's confirmation that no physical equipment exists yet, this pass
  deliberately worked only the three of four "remaining quantification" items
  from 2026-07-31 that are genuinely paper-closeable: (1) grounded the
  10–100 g/h Cl₂ generation-rate envelope in Faraday's law (mass rate as a
  function of current, worked examples at 5/20/50/100 A); (2) expressed
  CE-006's own reaction exotherm as a formula on that same rate
  (Q = 1.46 MJ/kg × rate), explicitly left un-combined with Stage D's base
  exhaust heat load since that term is still Placeholder pending
  `Gate_05_Separation_Thermal.md` exhaust characterization — real operational
  data, not something paper work can substitute for; (3) specified fail-safe
  interlock behavior (DC supply hard-wired through Stage D's recirculation/
  power monitoring as a series trip, not a software poll) fully at the
  doctrine level; (4) narrowed membrane/diaphragm choice to two candidate
  classes (salvage-first ceramic diaphragm vs. external-dependency
  cation-exchange membrane), final selection still open. The fourth original
  item (combined thermal-sink number) is explicitly **not** claimed closed —
  stays blocked on Gate_05 hardware data. CE-006 remains **In Progress**, not
  advanced to Resolved. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 1/6. (1) Open Unknowns **8** = CE-001–008, matches local
  sidecar and `Unknowns.md`. (2) CE-003 correctly **Blocking Yes / Critical**
  (blocks first hot pyrolysis). (3) CE-006 correctly **Blocking Yes** for
  CLF-004 candidate pathway. (4) No CE-* closed; no physical/chemical
  validation claims advanced. Human-directed.

- 2026-07-31: **CE-006 vessel design sketch integrated; status moved Open →
  In Progress.** Grok proposed a small-scale sealed chlor-alkali cell
  concept (divided cell, single-path anode off-gas to Stage D, no
  atmospheric release path). Checked against `Operations/Air_Scrubber.md`
  source before adoption: the sketch correctly leveraged Stage D's existing
  negative-pressure doctrine, but (1) did not connect its own "heat balance
  TBD" open point to Stage D's existing, named Thermal Sink Requirement —
  logged after a real 2026-05 hidden-failure-mode incident — despite the
  Cl₂+NaOH exotherm being a second, independent heat load on top of
  whatever Stage D is already sized for; (2) assumed AS-003's interlock
  system was working infrastructure, when AS-003 is actually In Progress
  and blocked on the Gate 4 Cold Verification Harness. Sent back for
  revision; Grok's second pass made both gaps explicit design
  requirements (combined thermal-sink sizing calculation; AS-003
  calibration as a hard operating prerequisite, not assumed
  infrastructure) rather than open points. Revised sketch verified and
  integrated as CE-006's vessel-design artifact, closing item 1 of the
  four-item Resolution Path at the conceptual/architectural level only —
  no vessel built, AS-003 uncalibrated, thermal-sink calculation not yet
  performed. Also noted 316L stainless as already-approved (via Air_
  Scrubber.md's Corrosion Isolation doctrine) for Stage D's own hull,
  distinct from the anode/Cl₂-line materials rule. CE-006 moved to In
  Progress alongside CE-005/CE-007, same precedent: doctrine and design
  now complete, hardware and calibration remain. Operating as Synthesizer
  per Auditor_Protocols.md v0.29, human-directed.

- 2026-07-31: **Corrected audit findings, then closed real gaps; one new CE- entry
  added (CE-008), avoiding a collision with the already-existing CE-004.**
  Copilot's audit contained three demonstrably false claims, checked against
  source before any action: (1) "file ends abruptly mid-sentence" — false, the
  cited sentence is complete; (2) "Chemical Operator Minimum Competency
  appendix is missing" — false, CE-004/Appendix A already exists and is In
  Progress; (3) corrosion-rate order-of-magnitude qualifier "missing" — false,
  already present verbatim. Grok's proposal to insert new "Dilution Doctrine"
  content as CE-004 would have collided with the real CE-004 — registered as
  **CE-008** instead. Grok's downstream-file audit also cited malformed
  filenames (missing underscores); not carried into this file.

  Real gaps closed: §2.3 stub replaced with full Solution Chemistry and
  Precipitation doctrine (Ksp table, scrubber precipitation, hard-water
  scaling, filter fouling/floc). New §2.4 Dilution Doctrine added (CE-008).
  §1.2 SCC extended with alloy/environment table, inspection doctrine,
  mitigation strategies, and salvage rejection criteria (real content already
  existed; extended, not replaced). §1.3 CP sizing sentence extended with
  temperature/flow/biofouling factors (partial gap — coating and electrolyte
  conductivity were already covered). §3.2 NOₓ formation and scrubber-load
  subsection added (genuinely new).

  CE-005 narrowed from Open to **In Progress** — §2.3 now complete;
  quantitative Ksp validation and sludge-disposal routing to GR-003 remain
  (GR-003 itself is currently unassigned in `Operations/Gate_03_Reduction.md`,
  so this dependency is blocked on that file, not on Chemistry.md).

  CE-006 given quantitative scrubber chemistry (stoichiometry, operating
  parameter table, over-chlorination hazard) and concrete detection/alarm
  thresholds (NIOSH/OSHA/EPA AEGL/AIHA ERPG-sourced, Grok content verified
  against standard references before adoption) — closes items 2 and 3 of its
  four-item Resolution Path. Items 1 (sealed vessel design) and the
  calibration half of item 2 remain genuinely open pending real hardware —
  same category of gap as `Challenges/Closed_Loop_Feedstock.md` CLF-003.
  CE-006 remains Open, not Resolved.

  CE-007 narrowed from Open to **In Progress** — decomposition pathways,
  acidification-to-Cl₂-release risk, storage/container doctrine,
  segregation/incompatibility doctrine, and downstream utility pathway
  (potable-water disinfection, cross-referenced to `Challenges/Water.md`) now
  answer all four of its Resolution Path items at the doctrine level;
  quantitative sizing still depends on CE-006's hardware gap.

  Open Unknowns: 7 → 8 (CE-008 added). Operating as Synthesizer per
  Auditor_Protocols.md v0.29, human-directed.

- 2026-07-19: **CE-006 — mechanism correction; CE-007 registered (Grok flag, cross-checked against
  source, human-directed adoption).** The 2026-07-17 directed approach's premise — that Stage E's
  KMnO₄ chemisorption bed neutralizes Cl₂ — does not hold; verified against a primary manufacturer's
  product catalog (PureAir® Filtration) showing pure KMnO₄/alumina media does not target Cl₂, which
  requires a separate acid-gas or dedicated chlorine media in their own product line. Redirected to
  `Operations/Air_Scrubber.md` Stage D (Wet Scrubbing / Water Column) with caustic (NaOH) dosing —
  the standard industrial mechanism for Cl₂ absorption, and already the correct architecture for a
  liquid-phase capture stage. Reframed as value-recovery rather than pure nullification: caustic
  chlorine scrubbing naturally produces sodium hypochlorite (dilute bleach), an established small-scale
  process (US Patent 4,308,123), consistent with this repository's salvage-first, closure-of-loops
  philosophy rather than treating the byproduct as waste. CE-007 registered for the resulting
  storage/stability/reuse doctrine gap, which did not exist anywhere in the repository before this entry.
  Open Unknowns 6 → 7.

- 2026-07-17: **CE-006 — directed approach added (human governing authority):**
  capture and nullification (not vent-with-treatment) named as the resolution
  direction, pointing to `Operations/Air_Scrubber.md`'s existing Stage E
  KMnO₄ chemisorption mechanism as the most directly applicable existing
  infrastructure. Narrows the remaining work to verifying chemisorption
  capacity/kinetics and sealed-vessel capture at this process's actual
  generation rate, rather than open-ended containment-strategy selection.
  Still Open — a directional decision, not a completed resolution. Ethical
  Anchor / do-no-harm standard stated as taking precedence over this
  direction if the two ever conflict.

- 2026-07-07: CE-006 logged (human-directed), sourced from a candidate acid-sourcing
  pathway raised in `Challenges/Closed_Loop_Feedstock.md` CLF-004 — on-site chlor-alkali
  electrolysis using salt, water, and a homemade ion-selective membrane. Chlorine gas
  co-production has no containment doctrine in this file; logged as Critical/Blocking
  against CLF-004's candidate pathway pending resolution. Open Unknowns 5→6. Last Audit
  updated.

- 2026-06-11: ChatGPT informal audit integrated. Eight findings actioned:
  (1) Navigation Anchors, Upstream/Downstream tables added. (2) Spec Gate
  advanced 0→1. (3) All owner fields corrected from Chemistry_Electrochemistry.md
  to Chemistry.md. (4) CE-ASM-002 and CE-001 body converted to RDC framing.
  (5) CE-003 elevated from Major to Critical — Blocking status added; PL-001
  dependency made explicit. (6) Odor section doctrine header added — "warning
  signal, never clearance signal." (7) Corrosion rate numbers annotated as
  illustrative; CE-001 declared as quantitative owner. (8) Surface chemistry
  scope note added — treatments may migrate to Operations/Surface_Treatments.md.
  CE-004 converted to In Progress — Appendix A (Chemical Operator Minimum
  Competency) created with 10-item checklist. CE-005 added (solution chemistry
  and precipitation stub). Section 2.3 stub added. Open Unknowns updated 4→5.
  Last Audit updated.

- 2026-06-02: File created as `Architecture/Chemistry_Electrochemistry.md`.
  Establishes electrochemistry, acid-base, redox, contamination identification,
  polymer degradation, battery chemistry, and surface chemistry doctrine as
  peer Architecture file alongside Engineering.md, Thermal_Systems.md,
  Friction_Dynamics.md, and Mechanical_Structures.md. CE-001 through CE-004
  logged. Integration map covers 13 downstream files. Scope boundary
  explicitly excludes operational procedures (owned by Operations/ files)
  and regulatory compliance (human governing party decision).

---

## Relationship to Existing Documents

- `Architecture/Engineering.md` — peer file; broad engineering principles;
  this file extends into the chemical and electrochemical domain
- `Architecture/Thermal_Systems.md` — peer file; thermal domain; intersects
  at thermochemistry and electrochemical heat generation
- `Architecture/Friction_Dynamics.md` — peer file; fluid and surface domain;
  intersects at surface chemistry and fluid chemistry
- `Architecture/Mechanical_Structures.md` — galvanic compatibility doctrine
  here applies to all salvaged mixed-metal assemblies governed there
- `Operations/Plastics.md` — polymer degradation chemistry here is the
  foundational doctrine; PL-001 triage rejection depends on understanding
  why halogenated polymers are dangerous
- `Operations/Electronics.md` — battery chemistry and etch waste chemistry
  here provide the doctrine basis for EL-004, EL-005, and EV-003 protocols
- `Operations/Air_Scrubber.md` — acid-base chemistry here is the doctrine
  basis for scrubber design and AS-003 saturation monitoring
- `Operations/Gate_05_Separation_Thermal.md` — redox chemistry of metal
  separation is load-bearing for Spin Chamber operating doctrine
- `Tests/Support_Raft.md` — cathodic protection doctrine here directly
  addresses SR-001 (galvanic corrosion mitigation)
- `Challenges/Biofouling.md` — MIC mechanism defined here; the chemical
  basis for the biofouling challenge
- `Admin/Ethical_Constraints.md` — chemical hazards are a primary category
  of harm this file helps prevent; chemical dual-use awareness is relevant
- `Unknowns.md` — CE-001 through CE-004 to be indexed at next update

---

## Status

Version 0.1 — initial draft (2026-06-02).

**Gate status:** G1 (internal coherence) and G2 (physical plausibility as
a doctrine document) assessed as passing at Draft/Exploration stage.
G3 through G6 require formal audit pass by a different agent.

**What must remain constant:**

**Chemistry is happening whether or not it is understood.**

**The Beilstein test protects the reactor. The galvanic series protects the structure.**

**Unknown chemical history is the default assumption for all salvaged material.**

---

## Appendix A — Chemical Operator Minimum Competency

*Converted from CE-004. Defines the minimum chemical literacy standard that every
Forge operator must demonstrate before conducting any chemical processing operations —
Beilstein tests, pH monitoring, battery assessment, chemical waste neutralization,
or contamination identification. Integration with `Admin/Engineer_Protocols.md` is
pending (CE-004 resolution trigger). Until formally integrated, this appendix is
the operative standard.*

| # | Competency | Key Test | Reference |
|---|---|---|---|
| 1 | pH scale and neutralization | Can correctly identify whether a substance needs acid or base addition to reach neutral; understands neutral ≠ safe | §2 |
| 2 | Strong acids vs. strong bases — dilute does not mean safe | Can name the three mineral acids in §2.1 and state their primary hazard | §2.1 |
| 3 | H₂S olfactory fatigue — smell disappears before the hazard does | Can explain why "I can't smell it anymore" is not a safety clearance | §4.3 |
| 4 | CO invisibility — no sensory warning at any concentration | Can state that CO detection requires instrumentation, not smell | §4.3 |
| 5 | Beilstein test — correct procedure, interpretation, and failure modes with aged or composite polymers | Can perform test and interpret result; knows a negative result is not a guarantee | §4.1, CE-003 |
| 6 | Battery chemistry hazards — hydrogen off-gassing, acid/electrolyte exposure, thermal runaway | Can identify the three failure modes and their immediate response actions | §6 |
| 7 | Galvanic corrosion basics — mixed metals in electrolyte, general galvanic series direction | Can correctly predict which metal corrodes faster in a steel-aluminum pairing | §1.1 |
| 8 | Unknown chemical history doctrine — no documented history means treat as unknown until tested | Can state the correct intake response for an unlabeled container | §4 |
| 9 | Ventilation-first response — any chemical odor requires immediate ventilation before investigation | Can state the correct first action when any chemical odor is detected | §4.3 |
| 10 | "Slow does not mean safe" — gradual exposures accumulate; delayed symptoms are common | Can explain why a comfortable-feeling process can still cause harm | §4.3 |

*A Forge operator who cannot answer the key test for any row has not met the
minimum competency standard and must not conduct chemical processing operations
unsupervised. This is a hard prerequisite aligned with Ethical_Constraints.md
Life Preservation doctrine.*
