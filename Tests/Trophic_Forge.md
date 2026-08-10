# Trophic_Forge.md
*Tests/Trophic_Forge.md*

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
| Last Audit | 2026-06-14 |
| Auditor | Claude (Synthesizer), Gemini (Auditor), ChatGPT (Synthesizer), Grok (Synthesizer) |
| Open Unknowns | 10 |
| Active Disputes | 0 |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Trophic Forge concept and its organizing principle.
- The base loop architecture and node properties.
- Bootstrap sequence doctrine for salvage-first deployment.
- Proposed test parameters for each node.
- Open unknowns requiring resolution before any promotion consideration.
- Naming rationale and prior art questions.

**This file DOES NOT define:**
- Detailed LED array electrical specifications (see Operations/Energy.md and Electronics.md).
- Water purification doctrine for pond or condensate streams (see Tests/Living_Waters.md).
- Fish species selection as confirmed doctrine — proposed only, pending site context.
- Crop selection or agronomic practice — out of scope at current development interval.
- Atmospheric-scale effects of moisture extraction (explicitly out of scope).
- Any claim of tornado or severe weather mitigation — out of scope at all intervals.

---

## File Purpose

The Trophic Forge is a biological cascade architecture in which each system node performs a productive transformation and passes its outputs — including byproducts previously treated as waste — as inputs to one or more adjacent nodes. The system does not recycle waste; it has no waste category by design. Every output is a resource at a different trophic level.

This file exists to develop and test that concept within the Lazarus Forge philosophy: salvage-first, low external input, resilient under degraded conditions, scalable from minimal bootstrap to field-scale operation. It currently lives in Tests/ because the bootstrap sequence is unvalidated, prior art questions are open, and the minimum viable loop has not been demonstrated empirically. If validation succeeds, this file is the seed of a Biology/ domain analogous to Energy.md and Living_Waters.md.

Without this file, the biological dimension of resource recovery has no home in the repository and the four-domain resource architecture (energy, water, biology, atmosphere) cannot develop.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Phototactic insect yield from LED array is sufficient to meaningfully supplement fish feed | Analogous — commercial fish light studies show measurable biomass; Forge-scale unvalidated | Low | TF-001 empirical test result |
| ASM-002 | Fish waste N/P/K output is sufficient to produce measurable crop fertilization effect | Analogous — aquaponics literature; specific species and stocking density unconfirmed | Low | TF-003 nutrient measurement |
| ASM-003 | Edge vegetation phytoremediation closes the water loop without auxiliary filtration | Analogous — rice-fish systems, constructed wetlands literature | Low | TF-005 water quality test |
| ASM-004 | Salvaged LED arrays can be configured to target UV/blue spectrum at adequate intensity | Analogous — salvaged hardware feasibility; wavelength tunability unconfirmed | Medium | Component audit of available salvage stream |
| ASM-005 | Loop degrades gracefully under single-node failure rather than collapsing | Structural inference from network topology; not empirically tested | Low | Stress test TF-007 |

---

## Body

### Organizing Principle

A Trophic Forge is a directed biological network, not a linear cascade and not a simple closed loop. Flows have preferred directions, but feedback paths exist at every node. Each node is independently productive. The failure of any single node degrades system output but does not propagate to collapse — this is the resilience claim that most requires empirical validation.

The defining property that distinguishes a Trophic Forge from standard aquaponics, tri-trophic systems, or closed-loop agriculture:

> **The design objective is that no purchased feed is required at steady state.** The system ignites at the light node — energy enters as light, wild insect biomass exits as the first harvest. Whether the light node alone can sustain this condition remains an empirical question and is the principal purpose of TF-TEST-001 and TF-TEST-004.

This is an architectural claim, not a validated fact. It is the hypothesis the Tests/ phase exists to test.

**Energy Efficiency Qualification (Gemini audit — 2026-06-14)**

The light node is not free energy. It converts electrical energy through cascading losses:

- Salvage-grade LED electrical-to-optical efficiency: ~30–40% (lower if driving circuitry is mismatched).
- Phototaxis yield per kWh drops significantly in cold weather, high wind, moonlight, and off-season conditions.
- Wild insect feed conversion ratio (FCR) to fish biomass: approximately 1.5–2.5 kg insects per kg fish produced.

The Trophic Forge is a machine that converts electrical energy into biological caloric energy at low net system efficiency. Under resource-constrained conditions, this tradeoff must be evaluated against direct alternatives (e.g., using the same electrical energy to pump water for direct crop irrigation). The zero-external-input claim is a steady-state target under favorable conditions — it is not a baseline operating assumption. See TF-TEST-004.

**Seasonality Failure Cascade**

Wild insect yield is highly volatile. The named failure propagation path:

```
Insect yield drops (winter / dry season / adverse weather)
      ↓
Fish biomass loss or starvation
      ↓
Fish nitrogen/phosphorus excretion drops
      ↓
Crop node starved of nutrients
      ↓
Phytoremediation edge vegetation weakened
      ↓
Return water quality degrades
      ↓
Pond water quality crashes
```

This cascade is the primary resilience risk for the system. The Biomass Capture Buffer (see Buffered Architecture below) is the structural mitigation. See TF-007.

---

### Buffered Architecture (Gemini audit — 2026-06-14)

The original base loop is a strict sequential dependency. If any node fails, all downstream nodes fail with it. The buffered architecture decouples real-time node dependencies, allowing the system to survive single-node dropout without cascading collapse.

```
       [ Energy.md / Salvaged Solar + Storage ]
                         │
                         ▼
       [ Light Node (Nocturnal UV/Blue Array) ]
                         │
                         ▼
        [ Biomass Capture Buffer ]
        (surplus dried/frozen for winter)
                         │
                         ▼
    ┌────────────► [ Fish Pond Node ] ◄────────────┐
    │                    │                         │
    │                    ▼                         │
    │         [ Nutrient-Rich Effluent ]           │
    │                    │                         │
    │                    ▼                         │
[Living_Waters.md] ◄── [ Crop Node / Fields ]      │
(Emergency Filter)       │                         │
    ▲                    ▼                         │
    └────────── [ Phytoremediation Buffer ] ───────┘
                    (Edge Vegetation)
```

**Biomass Capture Buffer:** Surplus insect biomass captured during peak season (summer) is dried or frozen for winter use. Decouples the fish node from real-time light node yield. Without this buffer, the seasonality failure cascade is inevitable in temperate climates.

**Phytoremediation Buffer:** Edge vegetation acts as a holding and filtering stage rather than a direct pass-through. Return water quality is verified before pond re-entry. If quality thresholds are not met, water is diverted to Living_Waters.md filtration pathway rather than returned to the pond.

**Supplemental Feed Fallback:** If insect biomass drops below 1% of fish stock weight for more than 7 consecutive days, the node enters a Supplemental Feed state. Black Soldier Fly larvae cultured from crop waste is the preferred fallback — it violates the pure light-ignition loop claim but preserves the fish asset. This state must be logged as a loop integrity event.

---

### The Base Loop

```
Light (UV/blue LED array — ignition node)
      ↓
Insect biomass (phototaxis harvest — free protein, pest suppression byproduct)
      ↓
Fish production (insect → feed; zero purchased feed at steady state target)
      ↓
Nutrient-rich water (fish waste → N, P, K)
      ↓
Crop fertilization + irrigation (pond water → field)
      ↓
Phytoremediation (crops + edge vegetation → filtered return water)
      ↓
Pond replenishment ←─────────────────────────────────────────────────────┘
```

---

### Node Properties

| Node | Primary Output | Secondary Output | Salvage Entry Point |
|---|---|---|---|
| Light array | Insect attraction and harvest | Pest pressure reduction in adjacent fields | Salvaged LEDs, wiring, small power source |
| Insect harvest | Fish feed biomass | Poultry supplement; compost input | Mesh collection surfaces, salvaged screen |
| Fish production | Harvestable protein | Nutrient-rich water | Pond liner (salvaged HDPE or tarp) |
| Nutrient water | Crop fertilization | Reduced synthetic input cost | Salvaged irrigation pipe |
| Crop + edge vegetation | Food / fiber | Filtered return water | Existing field infrastructure |
| Filtered water | Pond replenishment | Cleaner local water table | Gravity return or minimal pump |

---

### Bootstrap Sequence

The loop is not built all at once. Each node provides leverage to justify the next. In a salvage-first, resource-constrained Forge context, the correct build order is:

**Stage 1 — Light → Insect node**
Minimal salvage requirement: LEDs, wiring, small power source (battery or solar panel fragment). Can be operational within days of decision. Immediately yields free high-protein biomass. Proves the phototaxis harvest concept before any further investment is committed.

**Stage 2 — Insect → Fish node**
Demonstrated biomass yield from Stage 1 justifies pond construction and fish stocking. The feed problem is solved before fish arrive. Pond liner from salvaged HDPE sheet or reinforced tarp. Native or locally available species preferred over purchased stock.

**Stage 3 — Fish → Nutrient node**
Once fish are producing waste at measurable rates, irrigation infrastructure follows demonstrated nutrient yield. Avoids building irrigation for a fertilization effect that has not yet been confirmed at Forge scale.

**Stage 4 — Nutrient → Crop → Filtration → Pond**
Closes the loop. Edge vegetation phytoremediation returns water to the pond. Full loop operation begins. Stage 4 is the first point at which the Trophic Forge claim — zero external feed input at steady state — can be evaluated empirically.

Each stage is independently useful before the next stage exists. Value accrues at every construction step, not only at loop completion.

---

### Distinction from Prior Art

| System Type | Feed Input | Light Node | Forge Compatibility |
|---|---|---|---|
| Standard aquaponics | Purchased pellet feed | No | Low — consumable dependence |
| Black Soldier Fly tri-trophic | Organic waste feedstock | No | Medium — waste-stream dependent |
| Rice-fish systems | Supplemental feed common | No | Medium — crop-specific |
| **Trophic Forge** | **Zero at steady state (target)** | **Yes — ignition node** | **High — salvage-first throughout** |

The LED/phototaxis ignition node is the architecturally distinctive claim. It is also the least validated element. Empirical test of this node is the highest priority in the test sequence.

---

### Proposed Test Parameters

**TF-TEST-001 — Phototaxis Yield Baseline**
Measure actual insect biomass captured per night per unit of LED power input. Target metric: ≥0.15 kg wet insect biomass per kWh electrical input. Control variables must include at least three distinct moon phases — new moon (peak yield baseline) and full moon (floor yield). Test across humidity, temperature, and seasonal conditions to establish yield curve. Establish minimum viable yield threshold required to sustain target fish population without supplemental feed.
*Confidence target: Measured.*

**TF-TEST-002 — LED Wavelength Optimization**
Compare insect capture yield across UV (365 nm), blue (450 nm), and mixed spectrum arrays. Characterize non-target capture rate (pollinators, beneficial predators). Establish optimal wavelength or combination that maximizes pest-species yield while minimizing beneficial species impact. Physical mesh exclusion matrix must be evaluated for size threshold that retains target pests while allowing small beneficial insects to escape.
*Confidence target: Measured.*

**TF-TEST-003 — Fish Nutrient Output Characterization**
Measure N, P, K concentration in pond effluent as a function of fish species, stocking density, and feed input rate. Target metric: Total Ammonia Nitrogen (TAN) 1.0–2.0 mg/L and Nitrates (NO₃⁻) 20–40 mg/L in pond effluent prior to crop routing. Values below this range will fail to produce measurable fertilization effect without auxiliary chemical supplementation.
*Confidence target: Measured.*

**TF-TEST-004 — Zero External Feed Threshold**
Determine minimum insect biomass yield required to maintain fish population at stable weight with zero supplemental feed. Target metric: minimum daily insect input equal to 2–3% of total fish stock weight per day. Failure condition: if insect biomass drops below 1% of fish stock weight for more than 7 consecutive days, node enters Supplemental Feed state and event is logged as a loop integrity violation. This is the empirical test of the core Trophic Forge claim.
*Confidence target: Measured — this is the gate test for the organizing principle.*

**TF-TEST-005 — Phytoremediation Return Water Quality**
Measure water quality of pond return water after passage through edge vegetation filtration. Target metric: TAN reduced to <0.5 mg/L and Unionized Ammonia (NH₃) to <0.05 mg/L before gravity return to fish pond. If thresholds are not met, water routing is locked out from the pond and diverted to Living_Waters.md filtration pathway. Candidate edge vegetation: Typha latifolia (cattail), duckweed channels.
*Confidence target: Measured.*

**TF-TEST-006 — Minimum Viable Loop Scale**
Determine the smallest pond area, LED array size, and crop border length at which the full buffered loop is self-sustaining. This defines the floor for Forge deployment planning.
*Confidence target: Simulated initially; target Measured.*

**TF-TEST-007 — Single Node Failure Propagation**
Simulate or induce failure of each node in turn (power loss to LED array, fish population loss, drought, crop failure). Measure how rapidly failure propagates to adjacent nodes and at what degradation level the loop can no longer recover without external input. Verify that Biomass Capture Buffer and Phytoremediation Buffer prevent cascade collapse under single-node failure.
*Confidence target: Simulated initially; target Field Test.*

---

### Relationship to Repository Domains

The Trophic Forge is the biological analogue of the mechanical and thermal transformation systems elsewhere in the repository.

| Domain | File | Transformation Type |
|---|---|---|
| Energy | Operations/Energy.md | Electrical and thermal |
| Water | Tests/Living_Waters.md | Hydrological and chemical |
| Biology | Tests/Trophic_Forge.md (this file) | Biological and trophic |
| Atmosphere | *(declared future domain)* | Atmospheric |

**Interaction with Living_Waters.md:** The fish pond is a water system. Pond water quality, phytoremediation return, and condensate from LW-005a (atmospheric AWG) may all interact. The Trophic Forge does not own water purification doctrine — that remains with Living_Waters.md. Cross-reference is required at the pond node interface.

**Interaction with Energy.md:** The LED array is the ignition node and the primary ongoing power draw. Power sourcing, load profile, and degraded-mode operation of the light array are governed by Energy.md. The Trophic Forge owns the biological outputs of the light node; it does not own the electrical inputs.

**Declared Trajectory:** If Tests/ validation succeeds, this file promotes to a Biology/ domain folder. Biology/Trophic_Forge.md would anchor that domain the way Forge_flow.md anchors Architecture/. That promotion requires passage of all six spec gates and human ratification per Governance_Migration_Protocol.md doctrine.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — file is pre-empirical | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| DS-001 | Naming: Trophic Forge vs. Cascade Agriculture vs. Metabolic Agriculture | Resolved — Gemini audit 2026-06-14. Trophic Forge adopted. Rationale: reflects active engineering manipulation of biological energy levels; fits Forge nomenclature; Metabolic Agriculture sounds like standard organic farming. Prior art identified: entomoponics, phototactic tri-trophic aquaponics, Southeast Asian rice-fish light-trap systems. | Low | **Closed** | This file |

---

## Auditor Notes & Unknowns

### TF-001 — Phototaxis yield at Forge scale unvalidated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical |
| Blocking | Yes — blocks organizing principle validation |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** No empirical measurement exists of wild insect biomass yield per unit LED power input at Forge deployment scale.

**Why It Matters:** The entire Trophic Forge architecture rests on the claim that the light node produces sufficient biomass to sustain the fish node without purchased feed. If this claim fails, the organizing principle fails with it.

**Resolution Path:** Payment via Specification — TF-TEST-001 and TF-TEST-004 empirical results move to Body as committed parameters once measured.

---

### TF-002 — Prior art search incomplete

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Gemini audit (2026-06-14) identified closest prior art as entomoponics and phototactic tri-trophic aquaponics. Southeast Asian rice-fish light-trap systems are the closest operational analog. Full literature search not yet conducted.

**Why It Matters:** If substantial prior art exists, the Trophic Forge may be a named concept with established literature, which would either validate or constrain the current architecture. Preliminary finding suggests the LED ignition node as primary feed source (rather than purchased feed supplement) is the novel architectural claim.

**Resolution Path:** Partially addressed — Gemini audit provides initial framing. Full literature search required to characterize scope of prior art and confirm novel elements. Update Distinction from Prior Art section when complete.

---

### TF-003 — Fish nutrient output at Forge stocking density uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — does not block Stage 1–2 bootstrap |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** N/P/K output from fish waste at expected Forge-scale stocking density has not been measured or modeled for target species.

**Why It Matters:** If nutrient output is insufficient to replace synthetic fertilizer inputs, Stage 3–4 of the bootstrap sequence requires external supplementation, weakening the zero-external-input claim.

**Resolution Path:** Payment via Specification — TF-TEST-003 measurement results.

---

### TF-004 — Species selection not determined

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks Stage 2 optimization, not Stage 1 |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Fish species for the production node has not been selected. Native species, tilapia, catfish, and perch all have different feed conversion ratios, nutrient output profiles, temperature tolerances, and regulatory constraints by location.

**Why It Matters:** Species selection determines nutrient output, feed conversion efficiency, and legal viability in a given Forge location. Site context governs this decision — there is no universal answer.

**Resolution Path:** Discharge via Trajectory — species selection is site-conditioned. A decision matrix will be added to Body once site context is known. Remains open until first deployment site is confirmed.

---

### TF-005 — Phytoremediation loop closure unvalidated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks Stage 4 only |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Whether edge vegetation phytoremediation alone can return water to pond-suitable quality has not been tested. Auxiliary filtration may be required, adding complexity and potential consumable dependence.

**Why It Matters:** If phytoremediation is insufficient, the loop does not fully close without external filtration infrastructure. This interacts directly with Living_Waters.md — the water purification pathway may need to own this stage.

**Resolution Path:** Payment via Specification — TF-TEST-005 results. If auxiliary filtration is required, cross-reference Living_Waters.md for pathway selection.

---

### TF-006 — Non-target insect capture rate unknown

| Field | Value |
|---|---|
| Status | Partially Addressed |
| Risk | High — Ethical_Constraints escalation candidate |
| Priority | Major |
| Type | Ethical |
| Blocking | No — blocks wavelength optimization, not initial test |
| Escalation | If non-target capture cannot be bounded below harmful threshold, escalate to Ethical_Constraints.md review before any further system expansion |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The LED array will attract non-target species including pollinators and beneficial predators. Capture rate across wavelength configurations is unknown. This is not merely a technical parameter — systematic destruction of pollinator populations or destabilization of local predator-prey balance could make the system ecologically negative even if biomass production metrics succeed. A Trophic Forge that produces fish protein while collapsing the surrounding insect ecology violates the Ethical Anchor regardless of yield numbers.

**Why It Matters:** Systematic capture of pollinators and beneficial predators could undermine the crop node and cause net ecological harm — a direct conflict with the Ethical Anchor. The harm is not confined to the Forge boundary; it propagates into the surrounding ecosystem.

**Draft Operating Protocol (Gemini audit — 2026-06-14):**
- Restrict light node to **nocturnal operation commencing 1 hour after dusk, terminating 1 hour before dawn.** Eliminates overlap with daytime pollinator activity windows (honeybees, most beneficial Hymenoptera).
- Implement **physical mesh exclusion matrix** over harvest mechanism: mesh sized to retain target pest species while allowing small beneficial insects to escape. Specific mesh size to be determined by TF-TEST-002 species composition data.
- UV (365 nm) attracts nocturnal moths (crop pests) but also aquatic macroinvertebrates — characterize aquatic invertebrate capture rate separately and assess impact on pond ecosystem.

**Resolution Path:** Draft protocol above reduces ethical risk. TF-TEST-002 wavelength optimization and species composition data required to confirm protocol effectiveness. Full resolution requires measured non-target capture rate under protocol conditions. If measured rate exceeds acceptable threshold, escalate to Ethical_Constraints.md before proceeding.

---

### TF-007 — Single node failure propagation uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The resilience claim — that node failure degrades but does not collapse the system — has not been tested or simulated. Propagation dynamics are unknown.

**Why It Matters:** If the system is brittle rather than resilient, the Trophic Forge fails its core design requirement. A fish population collapse, for example, might propagate to algal bloom in the pond from accumulated waste, then to water quality failure, then to crop loss — a cascade failure rather than graceful degradation.

**Resolution Path:** Payment via Specification — TF-TEST-007 stress test results.

---

### TF-008 — Minimum viable loop scale unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The smallest pond area, LED array size, and crop border length at which the full loop is self-sustaining has not been determined.

**Why It Matters:** Without a minimum viable scale, Forge deployment planning cannot begin. A loop that requires 5 acres to function is architecturally different from one that functions at 500 m².

**Resolution Path:** Payment via Specification — TF-TEST-006 results. Simulation acceptable as initial estimate; field test required for confirmation.

---

### TF-009 — Interaction boundary with Living_Waters.md at pond node undefined

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Minor |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md + Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The pond node is a water system. The boundary between Trophic Forge doctrine (biological outputs of the pond) and Living_Waters.md doctrine (water quality and purification) at this interface has not been defined.

**Why It Matters:** Without a clear ownership boundary, both files may attempt to define pond water quality standards independently, producing contradictory doctrine.

**Resolution Path:** Joint resolution — a shared interface definition to be added to both files on next audit pass. Living_Waters.md owns water quality standards; Trophic_Forge.md owns biological productivity standards. Where they interact, Living_Waters.md governs.

---

### TF-010 — Seasonal and climatic variability uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks annual self-sufficiency claim |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Insect abundance varies with season, temperature, humidity, precipitation, moon phase, and geography. Biomass production sufficient during summer peak conditions may collapse to near zero during winter or drought periods. The Biomass Capture Buffer (dried/frozen surplus) partially mitigates this, but buffer capacity requirements across a full annual cycle have not been characterized.

**Why It Matters:** A system that is self-sustaining only during favorable months still requires external feed reserves or adaptive degraded-mode operation for the remainder of the year. The zero-external-input claim must be evaluated across annual cycles, not peak conditions alone. This unknown directly qualifies the organizing principle.

**Resolution Path:** Payment via Specification — longitudinal measurements across at minimum one full annual cycle. Define reserve doctrine (buffer sizing) and degraded-mode operation protocol for off-season periods. Until resolved, all yield claims are peak-condition estimates only.

---

### Constitutional Statement (Declared — Grok audit 2026-06-14)

The following statement is proposed as the Trophic Forge constitutional axiom, to be formally ratified if and when this file promotes to a Biology/ domain:

> **Every node must be independently productive. Nothing exists solely to support something else.**

This principle is more fundamental than the light node claim. If the LED array fails, fish remain fish, crops remain crops, ponds remain ponds, and edge vegetation continues filtering water. The system degrades rather than becoming useless. Each node justifies its own existence while contributing to the network — the same philosophy as the Lazarus Forge itself applied to biological transformation.

*Status: Declared candidate. Not yet ratified. Requires human confirmation before encoding as binding doctrine.*

---

### Resolution Log

### Resolution Log

- 2026-07-12: Retired a stale Drift Indicator referencing DS-001 as still-open. DS-001 was already Closed (Gemini audit, 2026-06-14) per the Active Disputes table above — the trigger condition described a dispute that no longer existed. Replaced with a reopening guard instead of deleting the entry outright, since the underlying naming decision is still worth protecting against silent reversal.

*(no other unknowns resolved at time of first draft)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| 2026-06-14 | Atmospheric-scale dew point reduction as a design objective | Scale required (millions of units) is v5+ territory. Causal chain from localized moisture extraction to tornado suppression involves atmospheric dynamics outside Forge validation capacity. Water production is the Forge-relevant objective. | No — reopen only with peer-reviewed atmospheric modeling at regional scale |
| 2026-06-14 | "Closed Loop Agriculture" as primary name | Accurate but overused. Does not communicate the node-productive, light-ignited architecture that distinguishes this concept. | No |
| 2026-06-14 | "Cascade Agriculture" as primary name | Implies linear flow without feedback. Directionally correct but structurally incomplete. | No — elements of cascade framing may return in section headings but not as the organizing name |

---

## Drift Indicators

Standard mandatory re-audit conditions per File_Template.md apply.

**Additional file-specific drift indicators:**

- ASM-001 (phototaxis yield assumption) remains unchallenged for more than 90 days without TF-TEST-001 initiation → mandatory re-audit.
- TF-006 (non-target insect capture) reaches Critical status without an operating protocol in Body → halt expansion, escalate to Ethical_Constraints.md review.
- DS-001 (naming dispute) is Closed per Active Disputes above (Gemini audit, 2026-06-14) — if this ever shows as reopened or unresolved in a future audit without a new dispute entry logged first, that mismatch is itself the drift signal → escalate to Unknowns.md for repository-level resolution.
- Body content references atmospheric mitigation effects of any kind → immediate human review required. This is a hard scope violation.
