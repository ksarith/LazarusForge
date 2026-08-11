# Hydrologic_Resource_Cascade.md
*Tests/Hydrologic_Resource_Cascade.md*

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-06-28                                                          |
| Auditor          | Grok (Synthesizer); revised Gemini + Claude (Synthesizer/Auditor)   |
| Open Unknowns    | 2 Formal / 6 Unregistered (HR-003–HR-010 pending sidecar registration) |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Hydrologic Resource Cascade concept as a multi-benefit flood resource recovery system
- Sequential zones and their functions (intake, heavy mineral concentration, aggregate, fine sediment, wetland polishing, recreation)
- Episodic flood-driven operation philosophy integrated with continuous base-flow and optional passive circulation
- Hydraulic operating modes across drought, normal flow, seasonal high water, flood, recovery, and containment conditions
- Research unknowns and proposed test parameters (HR-001 through HR-010)
- Integration with Lazarus Forge principles (salvage-first, multi-output, passive systems, landscape-scale salvage)
- Flood resilience infrastructure framing with recreation and resource recovery as co-benefits
- Site characterization needs and promotion criteria

**This file DOES NOT define:**
- Detailed engineering drawings, site-specific hydrology models, or full permitting doctrine
- Power systems or energy integration (see `Operations/Energy.md`)
- Material processing gate details (see `Operations/Gate_05_Separation_Thermal.md`)
- Leviathan marine extensions or Support Raft integration
- Full economic valuation model (see `Admin/Economics.md`)
- Detailed contaminant remediation protocols
- Downstream sediment starvation modeling, water rights doctrine, or diversion permitting law
- Co-incident risk management for human-machinery conflicts during active material harvesting

---

## File Purpose

The Hydrologic Resource Cascade explores a nature-based, episodic flood-driven system for sediment management, resource recovery, flood mitigation, and public benefit in flat, flood-prone areas. It treats flood sediment as a salvage resource rather than waste, using passive hydraulic sorting in sequential zones to produce usable fractions (heavies, sand, silt/clay) while providing recreation, habitat, and education.

This file lives in Tests/ because core assumptions about consistent separation efficiency, material quality, flood resilience, and net public benefit remain unvalidated at pilot scale. It serves as the seed for a landscape-scale salvage experiment within the Lazarus Forge framework.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| HR-ASM-001 | Natural flood flows and hydraulic geometry can be engineered to achieve economically useful sediment segregation without excessive maintenance | Hydrodynamic sorting principles and existing sediment trap analogs | Medium | Pilot data shows insufficient yield or excessive maintenance |
| HR-ASM-002 | Recovered silt/clay and sand meet quality thresholds for ceramics/growing media and recreation without extensive additional processing | Analogous river sediment uses | Low | Material testing (HR-004) disproves usability |
| HR-ASM-003 | Episodic flood operation reduces energy/maintenance needs compared to continuous systems while leveraging natural replenishment | Passive hydrology and nature-based solutions literature | Medium | First flood cycle data shows net negative outcomes |
| HR-ASM-004 | Multi-benefit design (flood control + resources + recreation) strengthens regulatory and funding viability | Avoided cost arguments in resilience projects | Medium | Site-specific permitting reveals conflicts |
| HR-ASM-005 | Optional passive circulation systems (wind, hydraulic ram, animal power) provide sufficient head to maintain recreational and ecological velocity during inter-flood periods | Historical wind-pump performance and low-head hydraulic analogs | Medium | Pilot shows stagnation under average conditions despite passive systems |
| HR-ASM-006 | Continuous river-coupled base-flow diversion does not cause adverse downstream erosion or siltation in standard bypass mode | River diversion and canal engineering analogs | Medium | Field observation of scouring at return weir or excessive deposition in main channel |
| HR-ASM-007 | Base-flow diversion volume can be kept low enough to avoid starving the downstream channel of its natural sediment budget ("hungry water" effect) | Diversion/canal engineering literature on downstream channel degradation | Low | Field observation of downstream channel incision, armoring, or bank erosion beyond baseline |

---

## Body

### Organizing Principle

The system functions as a **Flood Resource Recovery Basin** with a **Hydrologic Resource Cascade**. Flood events drive sediment-laden water through sequential zones optimized for velocity reduction, sorting, and value extraction. Between floods, the system supports recreation, habitat, and maintenance through continuous base-flow diversion from an adjacent waterway augmented by optional passive circulation.

**Episodic Operation Doctrine:** Floods are the primary process driver. The system is designed for passive capture during high flows and low-intervention use otherwise. Continuous mechanical pumping is de-emphasized in favor of passive gravity-driven and natural hydrology systems.

**River-Coupled Base Flow:** Where an adjacent waterway exists, a controlled intake gate diverts a modest fraction of base flow through the cascade, returning via a safe weir downstream. This eliminates stagnation, maintains dissolved oxygen, supports wetland function, and keeps recreation viable year-round without large energy inputs.

**Optional Passive Momentum Systems:** During low-flow periods, circulation may be supplemented by passive mechanical systems. Options include wind-driven Archimedes screws, paddle wheels, hydraulic rams (where elevation permits), animal power, solar pumps, or other locally appropriate technologies. The cascade should not depend on any single circulation method — the appropriate choice is site-specific and should be selected from what is locally salvageable and maintainable.

### Hydraulic Operating Modes

The system behaves differently across hydrologic conditions. Operational posture shifts accordingly:

| Mode | Primary Driver | Primary Goal | Trigger / Control Mechanism |
|---|---|---|---|
| Drought | Passive/wind circulation or base-flow diversion | Maintain habitat, water quality, recreation | Intake gate at minimum sustaining flow; river at or below normal pool |
| Normal Flow | River base-flow diversion | Recreation, wetland polishing, monitoring | Passive gravity weir intake |
| Seasonal High Water | Increased diversion rate | Sediment capture begins | Crest-level overflow spillway activates |
| Flood | Natural overflow + maximum intake | Maximum storage and resource recovery; flood attenuation | Automated/passive choke-gate limits intake to prevent blowout |
| Recovery | Controlled drainage | Inspection, material harvesting, structural restoration | Recreation Loop locked out; sluice gates opened for dredging access |
| Containment | Isolation of affected zone(s) | Prevent contaminated material reaching public-access or recreation zones | Triggered when HR-UNK-002 contaminant thresholds are exceeded in any zone; affected zone sealed from downstream flow and public access until remediation or safe disposal pathway confirmed |

**Containment Mode** is not tied to a hydrologic condition — it can be entered from any other mode upon contaminant threshold breach, and exited only after HR-UNK-002 resolution criteria are met for the affected zone. This converts contamination from a static risk into a defined operational state with entry/exit conditions.

### Sequential Zones and River-Coupled Flow

```
[ Upstream Main River ]
        │
        ├──► [ Controlled Intake Gate ]
        │           │
        │           ▼
        │     (1) Flood/Base-flow Intake
        │     (reduces velocity, captures coarse debris)
        │           │
        │           ▼
        │     (2) Heavy Mineral Concentrators
        │     (spiral bends, vortex pits, collection sumps)
        │           │
        │           ▼
        │     (3) Aggregate / Beach Zone ◄── Optional Passive
        │     (sand bars, recreation beaches,    Circulation Loop
        │      construction aggregate)               ▲
        │           │                                │
        │           ▼                                │
        │     (4) Fine Sediment Lagoons              │
        │     (clay/silt for ceramics, adobe,        │
        │      compressed earth, growing media)      │
        │           │                                │
        │           ▼                                │
        │     (5) Wetland Polishers ─────────────────┘
        │     (nutrient removal, habitat,
        │      water clarification)
        │           │
        │           ▼
        │     (6) Recreation Loop
        │     (tubing, kayaks, nature walks,
        │      environmental education)
        │           │
        │           ▼
        └──◄ [ Safe Return Weir ]
                    │
[ Downstream Main River ]
```

Each zone improves water quality for the next while generating distinct value streams. Floods replenish sediment; minor restoration maintains function. The spillway/weir entry and exit act as pressure valves — modest base-flow diversion under normal conditions; maximum intake during flood events with excess bypassing safely down the main channel.

**Public Safety / Harvesting Separation:** Zones 3 and 4 are subject to periodic heavy-machinery material harvesting (excavators, vacuum trucks) during Recovery Mode. The Recreation Loop (Zone 6) must be physically isolated or operationally locked out from public access during any active harvesting window in upstream zones. This is a hard operational requirement, not a scheduling preference — see Hydraulic Operating Modes, Recovery row.

### Integration with Lazarus Forge

- **Salvage-First**: Flood sediment as primary feedstock
- **Multi-Output**: Resources, flood mitigation, recreation, habitat, education, water quality
- **Passive/Low-Energy**: Gravity and natural hydrology dominant; mechanical inputs are supplements not requirements
- **Resilience**: Floods as asset; design for overbank flows and natural restoration
- **Public Goods**: Avoided costs (dredging, damage) + direct benefits support funding

**Framing**: Position as flood resilience infrastructure with co-benefits, improving public and regulatory acceptance. The recreational and habitat dimensions are not afterthoughts — they are the primary mechanism for public support and permitting.

### Proposed Test Parameters / Research Questions

**Core parameters (HR-001 through HR-008):**
- **HR-001**: Can engineered hydraulic geometry consistently separate useful fractions? (Pilot channel tests)
- **HR-002**: Annual sediment yield vs. maintenance cost
- **HR-003**: Heavy mineral concentration efficiency
- **HR-004**: Clay/silt suitability for ceramics/growing media (lab analysis)
- **HR-005**: Flood resilience after repeated high-flow events
- **HR-006**: Ecological impacts vs. traditional detention basins
- **HR-007**: Contaminant management and water quality post-cascade
- **HR-008**: Net economic/public value including avoided costs

**Extended parameters (HR-009 through HR-010 — added 2026-06-28):**
- **HR-009 (Wind-Kinetic Efficiency)**: Correlate local wind speed intervals with resulting flow velocity (m/s) in the Recreation Loop via passive mechanical pump array. Determines whether wind-driven circulation is viable at the site or whether alternative passive systems are needed.
- **HR-010 (Diversion Hydraulics)**: Map the optimal intake gate geometry to capture maximum target sediment fractions during a design flood event while preventing system blowout or return weir silting. Informs the transition between operating modes.

**Pilot Approach**: Small-scale basin in a representative site. Monitor one or more flood cycles. Measure deposition, sorting, material properties, hydraulic performance, ecology, and visitor metrics. Track across all operating modes, including Containment.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| — | — | — | — | No entries yet — pre-deployment | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### HR-UNK-001 — Consistent sediment separation efficiency under variable flood conditions

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical                                        |
| Blocking      | Operational                                      |
| Owner         | Tests/Hydrologic_Resource_Cascade.md             |
| First Logged  | 2026-06-28                                       |
| Last Reviewed | 2026-06-28                                       |

**Description:** Hydraulic geometry and zone design may not reliably segregate fractions across variable flood magnitudes, sediment loads, and velocities. The sorting efficiency that works for a 2-year flood may be completely different from a 10-year or 50-year event.

**Why It Matters:** Core value proposition depends on usable material yields. If the cascade sorts well only at specific flow rates, the economic case weakens significantly. The entire resource recovery premise rests on this assumption.

**Resolution Path:** Pilot deployment and monitoring (HR-001). Payment via Specification once pilot data validates consistent separation across at least two flood cycles of different magnitudes.

---

### HR-UNK-002 — Material quality, contaminant risk, and usability thresholds

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | Operational                                      |
| Owner         | Tests/Hydrologic_Resource_Cascade.md             |
| First Logged  | 2026-06-28                                       |
| Last Reviewed | 2026-06-28                                       |

**Description:** Recovered fractions (especially silt/clay from first-flush urban or agricultural runoff) may contain heavy metals, pesticides, E. coli, or industrial contaminants. If fine clay lagoons accumulate toxins, zones 4 and 5 pivot from resource generation to hazardous waste remediation. Material usability thresholds for ceramics, growing media, and construction aggregate are unvalidated.

**Why It Matters:** Safety-critical. A cascade that concentrates heavy metals in the fine sediment lagoons creates a liability rather than a resource. The contaminant pathway must be characterized before any material extraction or public access is permitted.

**Resolution Path:** Lab testing of pilot materials (HR-004) including heavy metals screen, pesticide panel, and microbiological assessment. Must establish a contaminant decision tree: what contamination levels trigger remediation mode vs. resource extraction mode. Cross-reference `Challenges/Waste.md` WA-002 (hazardous fraction identification) and `Admin/Ethical_Constraints.md` for harm thresholds. Payment via Specification once contaminant characterization is complete and decision tree is defined. Once a contaminant decision tree is defined, its thresholds become the formal trigger conditions for Containment Mode (see Hydraulic Operating Modes). Resolution of this unknown therefore directly defines the Containment Mode entry/exit criteria, not just a static safety note.

*(Additional unknowns for long-term morphology changes, regulatory pathways, recreational compatibility conflicts, and wind-kinetic efficiency are noted as research questions HR-003 through HR-010 in the body. Formal sidecar registration deferred to first audit pass.)*

---

### Resolution Log

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Formal Open Unknowns **2** = HR-UNK-001, HR-UNK-002
  (matches `Unknowns.md`); HR-003–010 remain body research questions with
  formal registration explicitly deferred — not a stale registration note,
  and no new IDs invented (AP-035). (2) Both formal unknowns Blocking
  **Operational**; HR-UNK-002 safety-critical language consistent with
  Containment Mode. (3) No HR-UNK-* closed; no extraction claims advanced.
  Human-directed.

- 2026-06-28: **Initial file creation** by Grok (Synthesizer). Core architecture, six sequential zones, episodic operation doctrine, four assumptions, eight research questions, two formal unknowns.
- 2026-06-28: **Agent revision pass** (Gemini + Claude). Wind/river coupling added: river-coupled base-flow doctrine, Optional Passive Momentum Systems framing (technology-agnostic), Hydraulic Operating Modes table (five modes). HR-ASM-005 and HR-ASM-006 added to Assumptions. HR-009 and HR-010 added as extended research parameters. HR-UNK-002 expanded with contaminant pathway detail and cross-references. Open Unknowns corrected 8 → 2 (HR-003 through HR-010 are body research questions; formal sidecar registration deferred to first audit pass). Flow diagram updated with river-coupling architecture.
- 2026-06-30: **Multi-agent audit pass** (Claude, ChatGPT, Gemini). Open Unknowns metadata corrected to "2 Formal / 6 Unregistered" to resolve self-flagged Drift Indicator violation. HR-ASM-007 added (downstream sediment starvation / "hungry water" risk). Scope Boundary expanded to exclude downstream sediment budgeting/water rights doctrine and human-machinery co-incident risk. Hydraulic Operating Modes table gained a Trigger/Control Mechanism column and a new Containment Mode, converting contaminant exceedance (HR-UNK-002) from a static risk note into a defined operational state. Public Safety / Harvesting Separation note added under Sequential Zones to formally require Recreation Loop lockout during active material harvesting.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-28 | Wind-driven circulation as primary circulation mechanism | Locks system to single technology; site conditions vary; Forge doctrine favors technology-agnosticism | No — replaced with Optional Passive Momentum Systems framing |
| 2026-06-28 | Continuous mechanical pumping (lazy river style) for recreation loop | High energy cost; contradicts Episodic Operation Doctrine and low-energy design philosophy | No |

---

## Drift Indicators

- Body claims separation efficiency or material usability without pilot data
- Continuous pumping reintroduced as primary mode without energy justification
- Flood mitigation benefits overstated without hydraulic modeling
- Ethical constraints on contaminants or downstream impacts weakened
- Passive Momentum Systems locked to a specific technology without site characterization
- Open Unknowns count diverges from formally registered sidecar entries
- River-coupling added as requirement rather than option without site confirmation
- Unknown count grows without Resolution Pass
- Containment Mode entry/exit criteria altered without corresponding HR-UNK-002 resolution update
- Recreation Loop access permitted during active harvesting without explicit override documented

**Compound Drift Rule:** Multiple simultaneous triggers escalate to human review.

---

*This file seeds the Hydrologic Resource Cascade experiment. Promotion to partial Operations/ requires validated pilot data on at least one primary pathway (separation + one output stream) and resolution of blocking unknowns. The current architecture remains Exploration — testable hypotheses, not confirmed doctrine.*
