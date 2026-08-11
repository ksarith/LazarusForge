> **MERGED — see Tests/Pyrolysis_Cascade.md Resolution Log.** This is archived raw material, already processed into the live file.

Got it. v0.99.36 is in.

From the package and the embedded File State / Unknowns notes:

**Auditor_Protocols.md → v0.36**
- Spec Gates now **4/6** (G1, G3, G4, G6 clear).
- AP-017 (Battery independence) closed 2026-08-03 — Payment via Validation, three clean cold-session instances.
- AP-033 registered + resolved same day; Rule 9 added (Resolution Claims Require Governance Access).
- Challenge Class 10 high-coupling table updated with `Governance_Migration_Protocol.md` §VII.
- Open unknowns still at 14; one active dispute (DS-001).
- Sidecar remains relocated to `Archive/Logs/Auditor_Protocols_Logs.md` (SHA-256 recorded).

**Unknowns.md → v4.42**
- Integrity correction pass: AP-017 removed from active index (already Resolved), duplicate `Open Unknowns` row in Electronics.md File State cleaned, BATTERY_SEED path mismatch flagged (Admin/ vs Automation/).

**Archive/**
Several conversation dumps are now under `Archive/` (CopilotClosedLoop, CopilotCognitiveSalvage, Energy-copilot-chat, EthicalC-Copilot, Gate2 chats, Electronics-talking, GrokGeckMaybeOverflowToo, etc.) plus the formal Logs/ sidecars and changelogs. That matches the “putting some conversations into archive” note.

What do you want next on this release — cross-check against a prior version, spot-check a specific file/cluster, run structural integrity on the relocated sidecars, or something else?

**Short take:** The cascade idea is coherent as an exploratory architecture, but it is currently sitting in the wrong maturity frame and is blocked by several Critical unknowns already registered in the live repository. Technically interesting; not yet ready to be treated as a candidate specification or even a clean Test file without major grounding work.

### What works in the draft

- **Thermal cascade logic is sound in principle.** High-grade bloomery heat (1100–1300 °C) feeding a lower-temperature pyrolysis zone (400–700 °C) is a classic heat-integration move. Using the bloomery as the thermal engine rather than an afterthought is the strongest non-obvious insight in the document.
- **Materials-separation framing is better than “waste-to-energy.”** Emphasizing tipping fees + metals + carbon products over fuel revenue is realistic for mixed urban salvage. That matches the Forge’s salvage-first posture better than pure energy recovery.
- **Air_Scrubber.md is correctly called out as non-optional.** Dioxin/furan precursors, PAHs, HCl from any PVC, metal fumes from the bloomery stage — all of that is real and already flagged elsewhere (PL-001, CE-003, GR-003/004, AS-003).
- **Control/SCADA and thermodynamic-simulation sketches are useful scaffolding.** They show the author was thinking about observability and energy balance, which is rarer in early conceptual notes.

### Where it collides with current repository reality

1. **PL-001 is still Open and Critical.**  
   Any hot pyrolysis of mixed “garbage” that may contain PVC/Teflon is blocked until halogenated-polymer triage and HCl/dioxin control are specified and validated. The cascade document treats feedstock as generic urban waste. That assumption is currently indefensible under existing doctrine.

2. **Gate_03_Reduction and Plastics ownership is unresolved.**  
   GR-002 (reduction method not selected) and the Plastics.md reactor questions (PL-002 thermal runaway/pressure, PL-003 fuel stability) are still open. A bloomery stage is a specific metallurgical reduction path; it cannot quietly become the default without an explicit decision and cross-file ownership clarification.

3. **Feedstock consistency and pre-triage are under-specified.**  
   The draft assumes continuous feed with shredding + moisture control. Mixed municipal or urban salvage streams are highly variable in moisture, halogen load, battery fragments, pressure vessels, and energetic materials. Gate_01_Intake and Gate_02_Triage already carry Critical unknowns (GI-002 energetic materials, GI-003 augmented hazard detection, TS-002 contamination routing). The cascade cannot inherit a clean feedstock by fiat.

4. **Economic claims are currently Placeholder / Analogous at best.**  
   Tipping-fee ranges, metals recovery ≥70 %, heat recapture ≥40–60 %, break-even at 50–100 t/day are plausible industry heuristics, but none of them have Forge-specific measurement or even a site. They should not be read as near-term projections.

5. **Ethical and emissions surface is larger than the draft acknowledges.**  
   Beyond Air_Scrubber performance, there is the question of what happens to residual slag, char that fails activated-carbon quality, and any liquid condensates that become concentrated toxin streams (see the parallel concern already logged for Living_Waters distillate). GR-003 (biological and chemical waste disposal doctrine) is still Critical and unassigned.

### Architectural fit inside LazarusForge

This is closer to a **Challenges/** or **Tests/** exploration than an Operations/ module. It sits at the intersection of:

- Plastics pyrolysis  
- Gate_03 reduction  
- Metallurgical separation (Gate_04 / Gate_05 territory)  
- Air scrubbing  
- Energy integration  

It is **not** a drop-in replacement for any existing gate. Promoting it prematurely would create exactly the kind of scope-bleed and ownership collision the Auditor Protocols are designed to catch.

If it moves forward, the cleanest path is:

1. Keep it exploratory (or move it under Tests/ as a named pilot concept).  
2. Explicitly declare the halogenated-polymer and energetic-material constraints as hard preconditions.  
3. Treat the bloomery stage as one candidate reduction method among others, not the assumed path.  
4. Require a minimal mass-and-energy balance (even if simulated) before any claim of “approaching thermodynamic self-sufficiency.”  
5. Route residual hazardous fractions to the still-open GR-003 / WA-002 / WA-004 cluster rather than inventing a new disposal doctrine.

### Bottom line

The idea is worth preserving as an archived concept and possibly elevating into a formal Test or Challenge once the blocking unknowns (especially PL-001, GR-002/003, and feedstock triage) have clearer resolution paths. Right now it is a coherent sketch that still rests on several assumptions the rest of the repository has already marked as Critical or Blocking.

If you want, I can:
- Draft a proper File State + Scope Boundary + Unknowns sidecar skeleton for it as a Tests/ candidate, or  
- Map every major claim in the cascade against the current Critical/Blocking index so the gaps are explicit, or  
- Stress-test the heat-cascade claim with a first-order energy-balance sketch (still Analogous, but tighter than the present qualitative loop).

Which direction is useful?

**Halogenated polymer triage** is the practical bottleneck behind PL-001. The core problem is detecting and segregating chlorine- and fluorine-bearing polymers (primarily PVC/PVDC and PTFE/PVDF) from mixed salvage before any hot pyrolysis or reduction step, because they release HCl, HF, dioxin/furan precursors, and corrosive gases that destroy equipment and create toxic off-gas.

Below is a structured inventory of methods, ordered roughly from field/low-tech to industrial, with strengths, limits, and Forge relevance.

### 1. Field / Low-Tech Screening Methods

| Method | Principle | Detection Target | Practical Notes | Limitations |
|--------|-----------|------------------|-----------------|-------------|
| **Beilstein (copper-wire flame) test** | Hot copper + halogen → volatile Cu-halide → green flame | Cl, Br, I (not F) | Classic qualitative test. Heat copper wire, touch sample, return to flame. Green = halogen present. Fast, cheap, no instruments. | Qualitative only. Does not distinguish PVC from other chlorinated materials or quantify load. Safety: ventilation required; does not detect PTFE well. False positives possible from some additives. |
| **Burn / flame behavior** | Self-extinguishing + green flame + HCl odor for PVC; PTFE smolders without flame | PVC family vs PTFE | Visual + smell cues. PVC often self-extinguishes with green tinge and acidic smell. | Subjective, hazardous (toxic fumes), unreliable on mixed/black/dirty pieces. Not suitable as sole triage. |
| **Density / float-sink** | PVC density ~1.3–1.45 g/cm³; PTFE higher | Rough separation | Sequential baths (water → salt solutions → denser media). | Overlaps with PET, POM, filled plastics. No halogen specificity. Useful only as pre-sort. |
| **UV fluorescence (ASTM D5991 Procedure A)** | Differential fluorescence under UV | PVC vs PET mainly | Used for PET flake contamination checks. PVC often fluoresces differently. | Narrow scope; interferences from other polymers and additives. Lab-oriented. |
| **Oven charring (ASTM D5991 Procedure B)** | PVC chars black at ~235 °C in air | PVC in PET | Heat sample; charred pieces are candidates, confirm with flame test. | Destructive, slow, mainly for PET streams. |
| **Dye tests (ASTM D5991 C/D)** | Selective staining of PVC | PVC | Soak in dye; PVC takes color preferentially. | Interferences (e.g., PETG); confirmation still needed. |

**Forge takeaway:** Beilstein + density + visual/burn cues form a workable manual triage ladder for small batches or early Gate_01/Gate_02 stages. They are Analogous/Measured only at laboratory scale; field reliability on dirty urban salvage is lower and needs calibration against known samples.

### 2. Instrumental Elemental Detection (Most Relevant for Throughput)

**Handheld / portable XRF (ED-XRF)**  
- Detects chlorine (and bromine) via characteristic X-ray fluorescence.  
- Industrial systems (Redwave XRF, Niton/X-MET series) already sort PVC and BFR-containing plastics on conveyors.  
- Fast (seconds), non-destructive, works on many colors and thicknesses.  
- Detection limits typically tens to hundreds of ppm Cl/Br depending on matrix and instrument.  
- Calibrate with matrix-matched plastic standards for quantitative work.  
- **Strength for Forge:** Highest practical readiness for mixed salvage. Can flag “halogen positive” items before shredding.  
- **Limits:** Surface-biased; thin films or heavily soiled pieces can under-read; does not identify polymer type, only elemental halogen; fluorine is harder (lower atomic number, weaker signal on many units).

**LIBS (Laser-Induced Breakdown Spectroscopy)**  
- Laser pulse creates plasma; optical emission shows Cl, Br, F, and other elements.  
- Rapid, can handle dark plastics better than NIR in some configurations.  
- Still more laboratory / pilot than widespread industrial PVC sorters.

**Combustion + ion chromatography / microcoulometry**  
- Burn sample, trap halides, quantify. Gold-standard total Cl/Br/F.  
- Used for verification and for pyrolysis-oil chlorine specs (often <3–10 ppm target for downstream use).  
- Not field-portable for real-time triage.

### 3. Spectroscopic Polymer Identification

| Technique | Strengths | Weaknesses for halogenated polymers |
|-----------|-----------|-------------------------------------|
| **NIR / SWIR hyperspectral** | High-throughput conveyor sorting of common polymers (PE, PP, PET, PS, PVC). Mature industrial tech. | Fails on black/carbon-black plastics; surface coatings and labels interfere. |
| **MWIR hyperspectral** | Better on some black plastics. | Higher cost, less common. |
| **ATR-FTIR / portable FTIR** | Definitive polymer fingerprint (C–Cl stretches ~600–800 cm⁻¹ for PVC; C–F for PTFE). Gold standard for lab ID. | Contact measurement; dirty/rough surfaces degrade spectra; slower for bulk sorting. |
| **Raman** | Works on black plastics; fast point measurements possible. | Fluorescence interference on some samples; laser safety. |
| **Multi-sensor fusion + ML** | Combining NIR/XRF/Raman/HSI with classifiers yields >95–99 % accuracy in recent studies. | Requires training data and compute; still emerging for dirty mixed streams. |

**Key practical point:** XRF (or LIBS) for *halogen presence* + NIR/FTIR/Raman for *polymer family* is the common industrial pattern. Neither alone is sufficient for high-confidence triage of mixed urban waste.

### 4. Emerging / Lab-Advanced Methods

- **Pyrolysis-DART-HRMS or portable pyrolyzer + optical emission:** Temperature-programmed pyrolysis releases characteristic fragments; chloride clusters or emission patterns flag PVC. Promising for rapid lab screening; not yet field-deployable at Forge scale.
- **Tracer-based sorting (fluorescent markers):** Adds detectable tracers at manufacturing; useful only if future feedstock is deliberately marked.
- **GC×GC-AED / chlorine-selective GC:** Excellent for characterizing residual organochlorines *after* pyrolysis (oil quality control), not for feedstock triage.
- **Total fluorine mass-balance approaches:** Relevant for PTFE/PFAS-containing fractions; still largely laboratory.

### 5. Process-Level Triage Strategies (Beyond Detection)

Even perfect detection leaves the question of *what to do* with the halogenated fraction:

- **Hard reject** from any hot pyrolysis/reduction stream (safest default while PL-001 remains open).
- **Dedicated low-temperature dechlorination pre-treatment** (some commercial systems do staged heating or catalytic dechlorination before main pyrolysis).
- **Separate chemical recycling path** for PVC (solvent-based or specialized pyrolysis with HCl recovery/scrubbing).
- **Density + electrostatic + XRF cascade** as a multi-stage mechanical sorter before any thermal step.

For mixed municipal/urban salvage, literature and industry practice converge on: **pre-sort for PVC/BFR via XRF or NIR, keep residual Cl in pyrolysis feedstock as low as possible (ideally <<0.1–0.5 %), and design the entire gas path for acid gas + dioxin control.**

### Forge-Relevant Assessment

| Requirement | Current Best Fit | Maturity for LazarusForge |
|-------------|------------------|---------------------------|
| Manual / low-tech gate triage | Beilstein + density + visual | Usable now for small batches; needs documented protocol + safety controls |
| Throughput screening | Handheld or belt XRF for Cl/Br | Highest readiness; salvage-compatible if units can be obtained/maintained |
| Polymer confirmation | Portable FTIR or Raman | Strong lab/bench method; field use possible with care |
| Black / dirty / coated plastics | XRF + Raman or MWIR | Partial solutions exist; residual uncertainty remains |
| Fluoropolymers (PTFE etc.) | Harder; XRF less sensitive, FTIR better for confirmation | Explicit gap |
| Quantitative residual Cl after sorting | Combustion-IC or XRF on product | Needed for any claim that a stream is “safe for pyrolysis” |
| Post-pyrolysis oil quality | Cl-selective GC or total Cl methods | Downstream of triage |

**Bottom line for PL-001:**  
No single method currently gives high-confidence, low-cost, fully automated triage of dirty mixed urban salvage under Forge constraints. The practical near-term stack is:

1. Visual + density pre-sort  
2. Handheld XRF (or equivalent elemental screen) for Cl/Br-positive items → hard segregate  
3. FTIR/Raman confirmation on ambiguous pieces  
4. Strict rejection of any positively identified halogenated fraction from the main pyrolysis/bloomery cascade until a dedicated dechlorination + scrubbing path is specified and validated  
5. Residual risk accepted only with measured total-halogen data and Air_Scrubber performance evidence

This is still **Analogous / Partially Measured** knowledge transferred from industrial recycling and lab studies. Forge-specific validation (detection limits on actual salvage, false-negative rates under field conditions, operator time, false-positive cost) does not yet exist and remains the core of the open PL-001 unknown.

I can next:
- Draft a candidate triage protocol skeleton suitable for Gate_01 / Gate_02 or Plastics.md,
- Map each method against existing Critical unknowns (PL-001, CE-003, GI-003, etc.), or
- Pull deeper detail on any single technique (XRF calibration, Beilstein SOP, FTIR libraries, etc.).

Which is most useful?

**Mapping: Major claims in `Archive/Pyrolysis_Cascade.md` vs current Critical / Blocking index (v0.99.36 / Unknowns v4.42)**

Status legend used below:  
- **Blocked** = claim cannot be acted on or treated as provisional-spec until the listed unknown(s) close or are explicitly scoped around.  
- **Constrained** = claim is still writable as Exploration, but any promotion or physical work inherits hard limits.  
- **Unsupported** = claim rests on assumptions with no corresponding measured/analogous evidence in the live repository.  
- **Unrelated** = no direct Critical/Blocking collision (still may carry Major/Open unknowns).

---

### 1. System-level framing claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| “A pyrolysis–bloomery cascade can be engineered as a closed-loop materials-separation system” | PL-001, CE-003, GR-002, WA-002, GR-003, FA-001 | **Blocked** | Mixed “garbage”/MSW feedstock + hot pyrolysis is explicitly blocked until halogenated-polymer triage is validated. Bloomery as reduction method is one candidate among unresolved GR-002 options. No site (FA-001) → no hot operations. |
| “Technically feasible; economically challenging but not impossible” | ECN-002, EV-001, FA-001, PL-001 | **Unsupported / Constrained** | Technical feasibility is unproven at Forge scale. Economic viability has no operating-cost baseline (ECN-002) and no characterized power demand (EV-001). |
| System converts mixed MSW into separable fractions (hydrocarbons, metals, carbon, slag) | WA-002, WA-004, GR-003, PL-001, GI-002/003, TS-002 | **Blocked** | Hazardous-fraction identification and negative-value disposal doctrine are both Critical. Contamination routing (TS-002) and energetic-material handling (GI-002) are open. |

---

### 2. Feedstock & pre-processing claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Acceptable inputs include mixed municipal solid waste / “garbage” | PL-001, CE-003, WA-002, GI-002, GI-003, TS-002, WW-005 | **Blocked** | PL-001 and CE-003 are the primary blockers for any hot thermal path. WW-005 blocks powered machinery on raw urban salvage until IFM screening exists. |
| High-chlorine industrial waste prohibited “unless scrubber capacity is expanded” | PL-001, CE-003, AS-003, GR-003 | **Constrained** | Even the “unless” clause is currently ungrounded; residual Cl limits and scrubber waste-stream doctrine are open. |
| Continuous feed with shredding + moisture control | WW-005, GI-002, GI-003, TS-002, EN-001 | **Constrained** | Powered size-reduction on unsorted urban material inherits IFM and energetic-material unknowns. Structural claims on any salvaged shredder inherit EN-001. |

---

### 3. Primary pyrolysis stage claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Pyrolysis chamber at 400–700 °C on mixed garbage produces syngas, pyro-oil, char/coke | PL-001, PL-002, CE-003, GR-004 | **Blocked** | PL-001 (halogens) and PL-002 (reactor pressure/thermal runaway) are explicit preconditions for any hot pyrolysis run / reactor fabrication. |
| Oxygen-starved environment + real-time off-gas monitoring | AS-001–AS-003, EC-012 | **Constrained** | Scrubber power budget and waste-stream saturation open. Any reliance on sensor honesty collides with EC-012 (epistemic spoofing via hardware/firmware). |
| Heat-recapture channels from downstream bloomery | EV-001, TH-related, EN-001 | **Unsupported** | No quantified heat-flow data or salvaged-duct/refractory safety factors at Measured confidence. |

---

### 4. Bloomery stage claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Char/coke transferred to bloomery (1100–1300 °C) for metal oxide reduction, ferrous/non-ferrous separation, carbon burnout, slag | GR-002, GR-003, GR-007, EN-001, CE-001, SC-009 | **Blocked / Constrained** | Reduction method itself is still open (GR-002). Contaminated-equipment retirement (GR-007) and chemical-waste disposal (GR-003) are Critical. Reactive-metal atmosphere requirements (SC-009) become Critical if Ti etc. appear. |
| Bloomery waste heat ducted back to pyrolysis, reducing external fuel demand | EV-001, EN-001 | **Unsupported** | Energy integration efficiency targets (≥40–60 %) have no Forge-scale measurement or even a site energy model. |
| Syngas from pyrolysis can fire the bloomery | PL-003, EV-001 | **Constrained** | Pyrolytic fuel stability/contaminant profile (PL-003) is still Minor/Open; power demand uncharacterized. |

---

### 5. Off-gas / Air Scrubber claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Multi-stage scrubber (cyclone → wet → activated carbon → catalytic oxidizer) is required and sufficient for compliance | AS-001, AS-003, AS-004, PL-001, CE-006, GR-004 | **Constrained** | Air_Scrubber.md itself carries open power-budget, waste-stream/saturation, and noise unknowns. Chlorine containment doctrine (CE-006) is Critical for any Cl-bearing path. Particulate generation (GR-004) uncharacterized. |
| Handles benzene, PAHs, dioxin precursors, SOx/NOx, metal fumes | PL-001, WA-002, GR-003 | **Blocked** until triage exists | Without upstream halogen triage, the scrubber is being asked to manage an unbounded hazard load. |

---

### 6. Materials-recovery claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Hydrocarbon recovery (syngas → power/methanation; pyro-oil → hydrotreating; tars → chemical feedstock) | PL-003, EV-001, ECN-002 | **Unsupported** | Fuel quality and energy value unmeasured; no cost baseline. |
| Metals recovery ≥70 % (ferrous bloom + non-ferrous melt pools) | GR-002, EN-003, CE-001, WA-002 | **Unsupported** | No validated recovery yields; alloy identification database open; galvanic/mixed-metal issues open. |
| Char → activated carbon / soil amendment / reductant | GR-003, WA-004, WA-002 | **Constrained** | Residual hazardous content and negative-value fraction disposal still Critical. |
| Slag crushed for mineral recovery | WA-004, GR-003, CE-related | **Constrained** | Same disposal and hazardous-fraction gaps. |

---

### 7. Heat-integration & efficiency claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| ≥40 % or ≥60 % heat recapture is achievable / ideal | EV-001, no dedicated thermal-cascade unknown | **Unsupported** | Purely Analogous; no Forge energy balance or measured HX performance. |
| Two-way energy loop (bloomery heat → pyrolysis; syngas → bloomery) approaches thermodynamic self-sufficiency | EV-001, ECN-002 | **Unsupported** | Circular claim until power demand and operating-cost baselines exist. |

---

### 8. Economic & scale claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| Tipping fees $40–120/ton are realistic revenue | ECN-002, ECN-004, FA-001, FA-003 | **Unsupported** | No site, no market-rate data maintenance, no operating-cost baseline. |
| Break-even at ≥50–100 t/day throughput | ECN-002, EV-001, FA-001, PL-001 | **Blocked** | Scale claim presupposes a site, validated triage, and cost model that do not exist. |
| Primary economic engine = tipping fees + metals recovery (not fuel) | ECN-002, WA-002, GR-003 | **Constrained** | Conceptually plausible, but still rests on unresolved hazardous-fraction and disposal doctrine. |
| Short-term negative margin expected; long-term conditional positive | ECN-002, TR-001 | **Constrained** | Consistent with repository caution, but TR-001 (v1 profitability) remains Blocking and depends on ECN-002/EV-001. |

---

### 9. Control / SCADA / safety claims

| Cascade Claim | Direct Collisions | Status | Notes |
|---------------|-------------------|--------|-------|
| PID loops, gas-composition feedback, automated interlocks, 1 Hz logging, full audit trail | CF-001, EC-012, EL-006, SEC-related | **Constrained** | Hardware watchdog (CF-001) still Blocking for autonomy claims. Firmware trust (EL-006) and epistemic spoofing (EC-012) are open. |
| Over-temperature shutdown, CO/H₂ alarms, emergency flare, quench, feed interlocks | SP-006, FA-001, GR-006, GR-008 | **Constrained** | Emergency-response procedures blocked by lack of site (FA-001 → SP-006). Jam-clearing and operator decision-support doctrine open. |
| Refractory integrity monitoring and salvaged furnace construction | EN-001, EN-005 | **Blocked** for any structural claim | No validated safety factors for salvaged materials; no verification testing protocols. |

---

### 10. Summary of load-bearing blockers

The cascade’s ability to move from archived Exploration toward any Test or Specification status is currently gated by this short list:

| Priority | Unknown | Why it kills or severely constrains the cascade |
|----------|---------|--------------------------------------------------|
| 1 | **PL-001** | No hot pyrolysis of mixed waste until halogenated-polymer triage is validated. |
| 2 | **CE-003** | Field polymer identification reliability — direct companion to PL-001. |
| 3 | **GR-002** | Reduction method not selected — bloomery is one unchosen candidate. |
| 4 | **GR-003 / WA-004** | Chemical/biological waste and negative-value fraction disposal doctrine missing. |
| 5 | **WA-002** | Hazardous-fraction identification reliability — safety-critical for mixed waste. |
| 6 | **FA-001** | No site → no hot operations, no emergency-response plan (SP-006), no real energy or cost data. |
| 7 | **PL-002** | Reactor pressure/thermal-runaway control required before any reactor fabrication. |
| 8 | **EN-001** | Structural claims on salvaged furnaces, ducting, supports blocked. |
| 9 | **ECN-002 / EV-001** | No operating-cost or power-demand baseline → economic and energy claims remain Placeholder. |
| 10 | **AS-003 / GR-004** | Scrubber waste stream and particulate generation still open. |

Secondary but material constraints: GI-002/003 (energetics & augmented hazard detection), TS-002 (contamination routing), WW-005 (IFM before powered machinery), GR-007 (contaminated equipment retirement), EC-012 (sensor honesty), CF-001 (watchdog if any autonomy is claimed).

---

**Net assessment**

Almost every operational, thermal, materials-recovery, and economic claim in the cascade is either **Blocked** or **Unsupported** relative to the current Critical/Blocking index. The document is coherent as an exploratory architecture sketch; it is not yet eligible for Gate progression or physical pilot work without explicit scoping that treats the halogenated-polymer, reduction-method, hazardous-fraction, site, and cost/energy baselines as hard preconditions rather than background assumptions.

If useful next, I can turn this map into a formal “claim → unknown → required resolution type” table suitable for a sidecar entry or for a Trajectory discharge decision.

**Claim → Unknown → Required Resolution Type**  
Source: `Archive/Pyrolysis_Cascade.md` major claims vs Unknowns.md Critical/Blocking index (v0.99.36 / Unknowns v4.42)

Resolution types follow the repository taxonomy:  
**Payment via Specification** · **Payment via Validation** · **Payment via Constitutional Decision** · **Payment via Refactoring** · **Discharge via Trajectory** · **Discharge via Lessons Learned**

Only load-bearing claims are listed. Claims that are purely descriptive scaffolding or already scoped as future work are omitted.

| # | Cascade Claim (condensed) | Primary Unknown(s) | Secondary / Related | Required Resolution Type | Notes / Minimum Closure Condition |
|---|---------------------------|--------------------|---------------------|---------------------------|-----------------------------------|
| 1 | Mixed MSW / “garbage” is acceptable feedstock for hot pyrolysis | **PL-001**, **CE-003** | WA-002, GI-002, GI-003, TS-002, WW-005 | Payment via Specification + Validation | Documented, tested halogenated-polymer triage protocol (detection limits, false-negative rate, operator procedure). Field polymer ID reliability demonstrated on actual salvage. |
| 2 | Hot pyrolysis (400–700 °C) of mixed waste is operable | **PL-001**, **PL-002** | CE-003, GR-004 | Payment via Specification + Validation | Triage closed **and** reactor pressure / thermal-runaway / maintenance-access doctrine specified and reviewed. |
| 3 | Bloomery (1100–1300 °C) is the reduction stage for char/coke | **GR-002** | GR-003, GR-007, SC-009, EN-001 | Payment via Specification **or** Discharge via Trajectory | Explicit selection (or rejection) of bloomery vs other reduction methods, with ownership assigned. If selected, contaminated-equipment retirement and reactive-metal atmosphere rules must follow. |
| 4 | System achieves materials separation into hydrocarbons, metals, carbon, slag | **WA-002**, **GR-003**, **WA-004** | PL-001, CE-003 | Payment via Specification | Hazardous-fraction identification protocol + chemical/biological/negative-value disposal doctrine assigned and written. |
| 5 | Multi-stage scrubber renders off-gas compliant (incl. dioxin precursors, acid gases, metal fumes) | **AS-003**, **PL-001**, **CE-006** | AS-001, GR-004 | Payment via Specification + Validation | Scrubber waste-stream / saturation doctrine closed; residual-Cl limits defined; chlorine-containment path (if any) specified. Performance claims require measured data. |
| 6 | ≥40–60 % heat recapture / near thermodynamic self-sufficiency via bloomery → pyrolysis + syngas return | **EV-001** | (no dedicated cascade thermal unknown) | Payment via Validation (after Spec) | First-order energy balance with measured or tightly bounded Analogous values; power-demand characterization for the cascade. Until then claim remains Placeholder. |
| 7 | Metals recovery ≥70 % (ferrous + non-ferrous) | **GR-002**, **EN-003**, **WA-002** | CE-001 | Payment via Validation | Only after reduction method selected and alloy-identification / hazardous-fraction methods exist. Yield is a measured claim, not a design assumption. |
| 8 | Char / slag fractions are usable (activated carbon, soil amendment, mineral recovery) or safely disposable | **GR-003**, **WA-004**, **WA-002** | — | Payment via Specification | Disposal / beneficial-use pathway assigned; residual hazard characterization required. |
| 9 | Continuous feed + shredding + moisture control is feasible on urban salvage | **WW-005**, **GI-002**, **GI-003**, **TS-002** | EN-001 | Payment via Specification | IFM screening, energetic-material discharge, and contamination-routing protocols before powered size reduction. |
| 10 | Structural / refractory claims for salvaged furnaces, ducting, supports | **EN-001** | EN-005 | Payment via Validation | Validated safety factors for the actual salvaged material classes used; verification testing protocol. |
| 11 | Tipping fees ($40–120/t) + metals recovery make the system eventually profitable; break-even ≥50–100 t/day | **ECN-002**, **EV-001**, **FA-001** | ECN-004, TR-001 | Payment via Validation (site-dependent) | Operating-cost baseline + power demand + confirmed site. Until then all economic numbers stay Placeholder / Analogous external. |
| 12 | Site-independent pilot or hot operation is possible | **FA-001** | SP-006, EN-002 | Payment via Specification (site assessment) | Physical site confirmed and assessed; emergency-response procedures can then be written. |
| 13 | Control system (PID, gas composition, interlocks, 1 Hz logging, sensor-driven safety) is trustworthy | **CF-001**, **EC-012**, **EL-006** | SEC-related | Payment via Specification + Validation | Hardware watchdog validated; firmware trust and anti-spoofing posture defined for any sensor-dependent safety claim. |
| 14 | Emergency shutdown, flare, quench, and operator response are defined | **SP-006**, **FA-001** | GR-006, GR-008 | Payment via Specification | Requires site; then jam-clearing and operator decision-support minimums. |
| 15 | High-chlorine streams can be accepted “if scrubber capacity is expanded” | **PL-001**, **CE-003**, **AS-003**, **CE-006** | GR-003 | Payment via Specification | Explicit residual-Cl acceptance limit + expanded scrubber design + disposal path for captured acid/salts. Default remains hard reject. |

---

### Clustered dependency order (recommended work sequence)

1. **Hard preconditions (must close or explicitly scope-out before any thermal work)**  
   PL-001 + CE-003 → WA-002 → GR-003 / WA-004 → FA-001

2. **Method selection**  
   GR-002 (accept or reject bloomery) → PL-002 (if pyrolysis reactor is retained)

3. **Energy & cost grounding**  
   EV-001 → ECN-002 → any heat-recapture or break-even claim

4. **Enabling infrastructure**  
   AS-003 / GR-004 (scrubber & particulates) · EN-001 (structures) · WW-005 / GI-002/003 / TS-002 (pre-processing) · CF-001 / EC-012 / EL-006 (if automated control is claimed)

5. **Measured performance claims** (only after 1–4)  
   Heat-recapture %, metals recovery %, residual Cl in products, scrubber efficiency, economic model

---

### Suggested disposition for the archived document

| Option | Action | Resolution type applied to the cascade as a whole |
|--------|--------|---------------------------------------------------|
| A | Keep in Archive/ as historical concept | — (no promotion) |
| B | Promote to `Tests/` or `Challenges/` as named Exploration with the table above as its initial sidecar | Payment via Specification (for the unknown set) |
| C | Discharge most thermal/economic claims to `Admin/Trajectories.md`; retain only the triage + reduction-method questions in live files | Discharge via Trajectory |
| D | Refactor into a narrow “halogen triage + reduction method decision” vehicle that feeds PL-001 / GR-002 | Payment via Refactoring |

The table above is written so it can be dropped directly into a sidecar or Resolution Log entry.

**Tests/Pyrolysis_Cascade.md** — skeleton (v0.1 candidate)

```markdown
# Pyrolysis_Cascade.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft — Exploration                                                 |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6 (not yet audited)                                               |
| Verification Ref | `Admin/Verification_Gates.md`                                    |
| First Logged     | 2026-08-04                                                          |
| Last Audit       | — (pre-audit skeleton)                                              |
| Auditor          | —                                                                   |
| Open Unknowns    | 8 (PC-001 … PC-008)                                                 |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High (thermal processing of mixed salvage; halogen & hazardous-fraction exposure) |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.  |

**Version String Registry** (self-referential citations outside File State — update on every version bump):
- §Organizing Principle (if retained)
- §Relationship to Repository Domains

---

## Scope Boundary

**This file DOES define:**
- Exploratory architecture for a staged thermal cascade: primary pyrolysis of pre-triaged salvage → secondary high-temperature reduction of the resulting char/coke fraction (bloomery-type or equivalent candidate) with heat integration between stages.
- Candidate material-separation pathways (hydrocarbons, metals, residual carbon, slag) and the open questions required to evaluate them.
- Explicit dependency surface on upstream triage, reduction-method selection, hazardous-fraction handling, site, energy, and scrubber doctrine owned by other files.
- Test concepts and measurement priorities that would be required before any claim of technical or economic viability.

**This file DOES NOT define:**
- Halogenated-polymer triage protocols or field polymer identification methods (→ `Operations/Plastics.md` PL-001, `Architecture/Chemistry.md` CE-003).
- Selection or ownership of the reduction method itself (→ `Operations/Gate_03_Reduction.md` GR-002).
- Air scrubbing design, performance, or waste-stream doctrine (→ `Operations/Air_Scrubber.md`).
- Chemical / biological / negative-value waste disposal doctrine (→ GR-003, WA-004).
- Site assessment, emergency response, or structural safety factors for salvaged furnaces (→ `Architecture/Facilities.md` FA-001, `Admin/Safety_Protocols.md` SP-006, `Architecture/Engineering.md` EN-001).
- Operating-cost baseline, power-demand characterization, or profitability claims (→ `Admin/Economics.md` ECN-002, `Operations/Energy.md` EV-001, `Admin/Trajectories.md` TR-001).
- Any Specification-level performance guarantee, yield number, or “self-sufficiency” claim.
- Fabrication procedures, experimental methodology standards beyond the test concepts listed, or canonical terminology.

**Hard preconditions (non-negotiable):**
- No hot pyrolysis or high-temperature reduction of mixed urban salvage may be proposed, piloted, or claimed under this file until PL-001 and CE-003 are resolved or the feedstock is demonstrably free of halogenated polymers by a validated method.
- No structural or refractory claims using salvaged materials may advance until EN-001 is closed for the relevant material classes.
- No site-dependent operational claims (emergency response, real energy balance, tipping-fee economics) until FA-001 is closed.

---

## File Purpose

This file records an exploratory thermal-cascade concept originally developed in archive conversation: load pre-processed salvage into a pyrolysis stage, recover condensable and gaseous hydrocarbons, transfer the solid residue to a higher-temperature reduction stage for metal separation and further carbon burnout, and integrate waste heat from the hot stage back into the pyrolysis stage while routing all off-gas through the repository’s air-scrubbing doctrine.

It exists to keep the architectural idea legible, to surface its dependency on already-registered Critical/Blocking unknowns, and to define the minimum empirical questions that would have to be answered before the concept could be considered for any higher maturity state. It does not assert that the cascade is currently feasible, safe, or economically viable.

**This document is subject to Auditor_Protocols.md.** Gate logic, fallacy checklist, and confidence-label rules apply.

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence   | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|--------------|-----------------------------------------------------|
| ASM-PC-001 | Pre-triage can reduce halogenated polymer content to a level compatible with the chosen thermal path | External industrial practice (XRF/NIR sorting) | Low (Analogous) | PL-001 / CE-003 resolution or measured residual-Cl data on Forge salvage |
| ASM-PC-002 | A bloomery-type or equivalent high-temperature stage can accept pyrolysis char and separate ferrous / non-ferrous fractions | Historical metallurgical practice; unvalidated on pyrolysis char | Low (Analogous) | GR-002 decision + char characterization |
| ASM-PC-003 | Meaningful heat integration between 1100–1300 °C and 400–700 °C stages is thermodynamically possible | Basic heat-transfer principles     | Medium (Analogous) | First energy-balance calculation with bounded yields |
| ASM-PC-004 | Off-gas from both stages can be rendered acceptable by the existing Air_Scrubber architecture once upstream halogen load is controlled | Air_Scrubber.md doctrine + external incineration practice | Low | AS-003 closure + residual-Cl acceptance limit |
| ASM-PC-005 | Mixed urban salvage will remain highly variable in moisture, metal content, and contamination | Observed Forge development state   | High         | Site-specific characterization after FA-001 |

---

## Body

### Organizing Principle (Exploratory)

> A staged thermal cascade can, in principle, convert pre-triaged salvage into separable material fractions while recovering heat between stages. Whether this is safer, more recoverable, or more economical than existing Gate_03 / Plastics pathways is an open empirical question, not a design premise.

All quantitative targets that appeared in the archived draft (heat-recapture %, metals recovery %, break-even tonnage, tipping-fee ranges) are retired to Placeholder / external-analogous status and are not repeated as claims in this file.

### Candidate Cascade Outline (non-normative)

1. **Upstream triage & pre-processing** (owned elsewhere)  
   Halogen screen → energetic-material screen → size reduction → moisture conditioning.

2. **Primary pyrolysis stage** (400–700 °C, oxygen-starved)  
   Outputs: syngas, condensables, char/coke + entrained metals/inerts.

3. **Secondary high-temperature stage** (candidate: bloomery-type 1100–1300 °C)  
   Functions under evaluation: further carbon burnout, metal melting/separation, slag formation, high-grade heat source.

4. **Heat integration**  
   Hot-stage waste heat → pyrolysis preheat / feedstock drying; pyrolysis syngas as candidate fuel for hot stage.

5. **Off-gas path**  
   Both stages → multi-stage scrubbing per Air_Scrubber.md; residual hazard streams → GR-003 / WA-004 doctrine.

6. **Product disposition**  
   Hydrocarbons, metals, residual carbon, slag — each requires an explicit beneficial-use or disposal path before any recovery claim is advanced.

### Relationship to Repository Domains

| Domain / File | Relationship |
|---------------|--------------|
| `Operations/Plastics.md` | Upstream owner of pyrolysis chemistry and PL-001 |
| `Operations/Gate_03_Reduction.md` | Owner of reduction-method selection (GR-002) and waste-disposal doctrine (GR-003) |
| `Operations/Air_Scrubber.md` | Owner of off-gas treatment |
| `Architecture/Chemistry.md` | CE-003 field polymer ID; CE-006 chlorine containment |
| `Challenges/Waste.md` | WA-002 / WA-004 hazardous & negative-value fractions |
| `Operations/Energy.md` | EV-001 power demand; any energy-integration claims |
| `Architecture/Facilities.md` / `Admin/Safety_Protocols.md` | FA-001 site; SP-006 emergency response |
| `Architecture/Engineering.md` | EN-001 salvaged-material safety factors |
| `Admin/Economics.md` / `Admin/Trajectories.md` | Cost baseline and any future profitability trajectory |

This file owns none of the above. It only records the cascade concept and the questions that must be answered before the concept can be re-evaluated.

### Test Concepts (pre-empirical)

These are candidate measurements, not approved test plans:

- **PC-TEST-001** — Residual halogen content after candidate triage methods on real salvage samples.
- **PC-TEST-002** — Mass and energy balance of a laboratory-scale pyrolysis run on pre-triaged, characterized feedstock (halogen-free or quantified).
- **PC-TEST-003** — Char composition (fixed carbon, metals, ash, residual Cl) and behavior under high-temperature reducing conditions.
- **PC-TEST-004** — First-order heat-integration calculation (not physical HX test) using measured or tightly bounded yields.
- **PC-TEST-005** — Off-gas speciation (acid gases, condensables, particulates) under controlled residual-Cl loads.

No test may be run that violates the hard preconditions in Scope Boundary.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|----------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-08-04 | Archive review + Critical/Blocking map | Promoted archived conversation draft toward live Exploration | Multiple Critical unknowns already block the core thermal claims | Cascade must be framed as dependent architecture, not autonomous process; economic and efficiency numbers retired to Placeholder | Measured (process) | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| —  | —       | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### PC-001 — Halogenated-polymer triage dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking |
| Type | Safety / Technical |
| Blocking | Yes — blocks all hot thermal work under this file |
| Owner | Tests/Pyrolysis_Cascade.md (dependency); resolution owned by Plastics.md / Chemistry.md |
| First Logged | 2026-08-04 |
| Last Reviewed | 2026-08-04 |

**Description:** The cascade assumes a feedstock that is either free of, or controlled for, halogenated polymers. PL-001 and CE-003 remain open.

**Resolution Path:** Payment via Specification + Validation on the owning files. This entry closes only when those unknowns close or when this file is rewritten to require exclusively pre-certified halogen-free feedstock.

---

### PC-002 — Reduction-method selection dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | High |
| Priority | Blocking (for bloomery-specific claims) |
| Type | Architectural |
| Blocking | Yes for any claim that the secondary stage is a bloomery |
| Owner | Tests/Pyrolysis_Cascade.md (dependency); resolution owned by Gate_03_Reduction.md (GR-002) |
| First Logged | 2026-08-04 |

**Description:** Archived draft treats bloomery-type reduction as the secondary stage. GR-002 has not selected a reduction method.

**Resolution Path:** Payment via Specification (GR-002 decision) or Discharge via Trajectory / Refactoring if bloomery is rejected.

---

### PC-003 — Hazardous-fraction and disposal dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking |
| Type | Safety |
| Blocking | Yes |
| Owner | Dependency on WA-002, GR-003, WA-004 |
| First Logged | 2026-08-04 |

**Description:** Mixed salvage and thermal residues generate hazardous and negative-value fractions whose identification and disposition are still open.

**Resolution Path:** Payment via Specification on the owning unknowns.

---

### PC-004 — Site and emergency-response dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking (for any physical pilot) |
| Type | Operational |
| Blocking | Yes for hot operations |
| Owner | Dependency on FA-001 → SP-006 |
| First Logged | 2026-08-04 |

**Resolution Path:** Payment via Specification (site assessment).

---

### PC-005 — Energy integration quantitative claims

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No (blocks only efficiency claims) |
| Owner | Tests/Pyrolysis_Cascade.md + Energy.md (EV-001) |
| First Logged | 2026-08-04 |

**Description:** Archived targets (≥40–60 % heat recapture, near self-sufficiency) have no Forge energy balance or measured yields.

**Resolution Path:** Payment via Validation after a bounded mass-and-energy model exists; until then all such numbers remain Placeholder.

---

### PC-006 — Metals-recovery yield claims

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Pyrolysis_Cascade.md (after GR-002) |
| First Logged | 2026-08-04 |

**Description:** ≥70 % metals recovery was stated without measurement or even a selected reduction method.

**Resolution Path:** Payment via Validation; claim retired to Placeholder until then.

---

### PC-007 — Structural / refractory adequacy for salvaged construction

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | High |
| Priority | Blocking (for any physical build claim) |
| Type | Safety / Structural |
| Blocking | Yes |
| Owner | Dependency on EN-001 |
| First Logged | 2026-08-04 |

**Resolution Path:** Payment via Validation on EN-001 for the material classes actually used.

---

### PC-008 — Economic viability framing

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Economic |
| Blocking | No (blocks only profitability claims) |
| Owner | Dependency on ECN-002, EV-001, FA-001, TR-001 |
| First Logged | 2026-08-04 |

**Description:** Tipping-fee ranges, break-even tonnage, and “eventual profitability” statements lack an operating-cost baseline and a site.

**Resolution Path:** Payment via Validation (site-dependent) or Discharge via Trajectory if the cascade is retained only as a technical concept.

---

### Resolution Log

- 2026-08-04: Skeleton created from archived conversation + Critical/Blocking claim map. All prior quantitative performance and economic numbers retired to Placeholder / external-analogous. Eight dependency unknowns registered. File positioned strictly as Exploration under Tests/.

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-08-04 | Treating the cascade as an autonomous, near-term operable process with stated yields and break-even economics | Direct collision with multiple Critical/Blocking unknowns (PL-001, CE-003, GR-002, FA-001, EN-001, ECN-002, etc.) | Only after the dependency set closes |

---

## Drift Indicators

Standard mandatory re-audit conditions per File_Template.md apply.

**File-specific:**
- Any Body text that re-introduces quantitative heat-recapture, metals-recovery, or break-even claims without a corresponding Payment via Validation entry.
- Any statement that softens or omits the hard preconditions in Scope Boundary (especially PL-001 / CE-003).
- Promotion of Status or Spec Gates without an independent audit event.
- Addition of ownership claims over Plastics, Gate_03, Air_Scrubber, or disposal doctrine.
- Physical test proposals that do not explicitly satisfy the hard preconditions.

---

## Status

**Version 0.1 — Draft, Exploration.**  
Skeleton only. No Body technical specification beyond the non-normative outline. All performance and economic claims from the archived draft are suspended pending resolution of the registered dependencies.

**What must remain constant:**  
Confidence never outruns verification.  
No hot thermal work under this file while PL-001 and CE-003 remain open.
```

---

This skeleton is ready to drop into `Tests/` (or to stay in Archive until a formal promotion decision). It keeps the architectural idea alive, makes every Critical collision explicit, and refuses to carry unsupported numbers or ownership claims.
The base idea evolved from separation of plastic lining in aluminum can processing.  The off gasses are a problem, so the thought emerged what would happen if they were simply tossed in a pyrolysis chamber.  What then happens to the coke that the chamber has as a byproduct?  Then we get to how do we leverage the remnants into improved functionality?  Overall, I have been chasing down the what happens next...
That origin story changes the center of gravity.

The cascade didn’t start as “process all the garbage.” It started as a concrete materials problem:

1. **Aluminum can stock** arrives with polymer lining (epoxy, acrylic, or similar).
2. Separating or thermally stripping that lining produces **off-gases** that are awkward to handle.
3. Pyrolysis becomes a candidate sink for those organics / off-gas streams.
4. Pyrolysis then leaves a **carbonaceous solid** (char/coke + any entrained fines or residual metal).
5. The open question becomes: what is the highest-value, lowest-harm next use of that solid — and can its processing also improve the energy or materials balance of the earlier steps?

That is a much tighter, more Forge-native chain than the later “mixed MSW + bloomery” expansion. The archival draft grew outward from the residue problem and picked up heat integration and metal recovery along the way. The original driver was residue management and off-gas containment inside an already-intended aluminum pathway.

### Re-centered framing

**Core sequence under investigation**

```
Aluminum can (Al + polymer lining)
        ↓
Lining separation / thermal strip
        ↓
Off-gas / organic fraction  ──→  candidate pyrolysis stage
        ↓
Pyrolysis products:
  • condensables / syngas (still need scrubbing & disposition)
  • char/coke solid
        ↓
“What happens next” to the char?
  – fuel / reductant?
  – further high-temperature treatment for residual metal recovery?
  – carbon product?
  – disposal path?
        ↓
Can any of those downstream steps return heat, carbon, or metal value
back into the aluminum or energy system?
```

This keeps the problem inside a materials-recovery logic rather than a general waste-to-energy logic. It also makes the Critical unknowns land more precisely:

- The polymer lining is a **defined, relatively consistent** organic stream, not unsorted MSW. That softens (but does not remove) the PL-001 / CE-003 problem — you still need to know whether the specific lining chemistry carries chlorine, fluorine, or other problematic substituents, and you still need off-gas control.
- The solid residue is downstream of a known metal (aluminum). Any high-temperature follow-on step is therefore interacting with aluminum chemistry, oxide films, and possible alloying elements, not with a random mixed-metal char.
- “Leverage the remnants into improved functionality” is the real design thesis: close loops, reduce external inputs, or raise the value of a fraction that would otherwise be a disposal liability.

### Implications for the Tests/ skeleton

The earlier skeleton treated the cascade as a general mixed-waste architecture. With this history, a tighter version would:

- Anchor the primary feedstock as **polymer-lined aluminum can stock** (or the separated lining + associated off-gas), not generic MSW.
- Treat mixed-waste expansion as a later, optional generalization that inherits all the existing Critical blockers.
- Keep the bloomery / high-temperature stage as one candidate answer to “what happens to the coke,” not as the assumed architecture.
- Make the central open question explicit: **what is the best next use of the pyrolysis solid when the upstream metal is aluminum?**

That reframing does not erase the earlier claim map; it simply ranks the unknowns differently. PL-001 and off-gas handling remain first-order because the lining chemistry is still not characterized. GR-002 (reduction method) and the char-disposition questions become the actual design surface rather than a general metals-recovery claim. FA-001, EN-001, and the economic baselines stay relevant only if/when a physical pilot is contemplated.

### The pattern you’re describing

“What happens next” is a useful generator, but it is also how exploratory cascades accumulate scope. Each residue creates a new process idea; each process idea creates a new residue or off-gas; the system grows. The governance posture that fits this pattern is:

- Keep the chain legible and sequential.
- Refuse to let any downstream stage silently rewrite the upstream scope or safety constraints.
- Treat every new stage as a candidate that must earn its place against the existing Critical/Blocking list rather than as an automatic continuation.

If you want to continue from here, the highest-leverage next steps are probably:

1. **Characterize the actual lining chemistry** (or the range of common can linings) enough to know the halogen and additive risk — this is the real PL-001 entry point for this concept.
2. **Define the pyrolysis solid** more carefully: expected carbon content, residual aluminum, ash, particle size, and whether it is closer to a fuel, a reductant, or a waste.
3. **List the candidate “next uses” of that solid** without committing to any of them, and mark which existing unknowns each candidate collides with.

That keeps the chase honest: every “what happens next” is paired with “what must already be true before we are allowed to try it.”
