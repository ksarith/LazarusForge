# Plastics.md — Salvaged Polymers & Pyrolytic Fuel Recovery

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Thermal depolymerization (pyrolysis) operates at high temperatures (300°C–500°C)
> and generates highly flammable, toxic hydrocarbons and synthetic gas. Enclosure
> breach or oxygen ingress creates an immediate risk of explosive pressure buildup
> or flashback fire. Halogenated plastics (PVC, Teflon) release hydrochloric acid
> gas and dioxins at pyrolysis temperatures — reactor corrosion and toxic bypass are
> credible failure modes if triage misses contaminated feedstock. See PL-001.
> Air Scrubber operation, continuous venting, and oxygen exclusion are
> non-negotiable prerequisites before heating begins. When in doubt, do not heat.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-27 (Grok — Skeptic/Auditor); revised 2026-06-08             |
| Auditor          | Grok — Skeptic/Auditor                                              |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Triage routing doctrine for salvaged industrial and consumer polymers
- Conceptual framework for low-pressure, oxygen-free thermal depolymerization
  (pyrolysis)
- High-level design requirements for a batch-fed reaction chamber and condenser array
- Safety and chemical containment boundaries for off-gas treatment
- Char and solid residue handling doctrine

**This file DOES NOT define:**
- Precise temperature profiles for individual or unique polymer blends
- Mechanical blueprints for custom extrusion screws or filament-drawing rigs
- Refining or fractional distillation specifications for separating fuel oil into
  specialized fuel grades
- Air Scrubber hardware specification or alkaline buffering stage design
  (→ `Operations/Air_Scrubber.md`)
- Energetic or radiological hazard screening at intake
  (→ `Operations/Gate_01_Intake.md`)
- Contamination routing beyond plastic stream identification
  (→ `Operations/Gate_02_Triage.md`)
- Energy accounting for pyrolysis reactor operation
  (→ `Operations/Energy.md`)
- Facility siting, clearance, and hot-work zone requirements
  (→ `Architecture/Facilities.md` — FA-001)
- Operator PPE standards and hearing/respiratory conservation program
  (→ `Admin/Safety_Protocols.md`)

---

## File Purpose

This document establishes the processing path for salvaged plastics within the
Lazarus Forge. Mixed or contaminated polymers represent both a recovery opportunity
and a significant logistical hazard — they cannot be safely routed to thermal
processing alongside metals, and mechanical repurposing yields diminish rapidly
with degradation. This file defines the triage hierarchy that routes plastics
toward the highest-value recovery path available, and specifies the pyrolytic fuel
recovery framework that handles what mechanical repurposing cannot.

Pyrolysis is positioned as a last-resort recovery path for otherwise intractable
mixed waste, not as a primary recycling method. Its core claim is falsifiable: mixed
low-value plastics can be safely converted to usable pyrolytic oil and syngas via
oxygen-free batch pyrolysis, provided halogenated streams are rejected at triage and
off-gases are captured by the Air Scrubber. If this file disappeared, mixed plastic
waste would have no governed processing path, and operators would lack the safety
doctrine required to handle pyrolysis off-gases and halogenated contamination.

---

## Assumptions

| ID      | Assumption                                                                                         | Basis                                                    | Confidence | Expiry Trigger                                                                 |
|---------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------|--------------------------------------------------------------------------------|
| ASM-001 | Sourced plastic feedstock will contain unrecognized or highly degraded multi-layer polymers        | Consumer and industrial salvage is fundamentally mixed; high-purity sorting cannot be guaranteed at v0 | High | First operational triage cycle characterizes actual feedstock purity distribution |
| ASM-002 | Mechanical recycling yields diminish rapidly after multiple heat cycles                            | Polymers shorten and degrade during mechanical re-extrusion; chemical breakdown path required for persistence | High | Operational filament-drawing data shows acceptable yield beyond current assumed threshold |
| ASM-003 | Waste heat from Spin Chamber or external sources can bootstrap reactor thermal demand              | Analogous — industrial waste heat recovery practice; cross-reference `Operations/Gate_05_Separation_Thermal.md` SC-007 | Low | SC-007 resolved — exhaust heat load characterized and available capacity confirmed |
| ASM-004 | Halogenated plastics (PVC, Teflon) are identifiable and rejectable at triage before reactor entry  | Beilstein test and density sorting are established detection methods | Low | PL-001 resolved — triage protocol validated against representative feedstock sample |
| ASM-005 | Pyrolytic oil from mixed plastic feedstock is usable as heating fuel or generator input without significant refining | Analogous — small-scale pyrolysis literature; oil quality varies by feedstock | Low | PL-003 resolved — oil stability and contaminant profile characterized |

---

## I. General Plastics Triage Hierarchy

Consistent with the principle of *Salvage Before Reduction*, plastics enter a
progressive depth triage sequence:

1. **Direct Component Reuse:** Structural panels, enclosures, or functional hardware
   are preserved intact.
2. **Mechanical Repurposing (RepRap / Filament):** High-purity, cleanly identified
   single-stream plastics (e.g., clean PLA, ABS, PETG) are routed toward shredding
   and drawing into custom fabrication stock.
3. **Thermal Depolymerization (Pyrolysis):** Mixed, degraded, contaminated, or
   low-value bulk plastics that cannot support mechanical repurposing enter the
   chemical recovery loop.

**Triage decision boundary for mechanical vs. pyrolysis routing:**
The threshold at which plastic is too degraded for mechanical repurposing is
not yet formally defined — see PL-004. Provisional indicators that favor pyrolysis
routing over filament drawing: visible embrittlement or chalking, unknown polymer
identity, multi-layer or composite construction, visible contamination or bonded
dissimilar materials, or melt-flow behavior inconsistent with a known single
polymer class.

**Halogenated polymer rejection:**
PVC, Teflon, and other halogenated plastics must not enter the pyrolysis reactor.
At triage, suspected halogenated material is identified using the Beilstein test
(copper wire combustion — green flame indicates halogen presence) or density
sorting (PVC density ~1.4 g/cm³ is distinctly higher than most common
thermoplastics). Confirmed halogenated material routes to `Operations/Gate_02_Triage.md`'s
Contaminated bin (non-decontaminable state, 2026-08-15 shared-destination extension),
not to the reactor and not to an undefined "specialist disposal" — the same named
hold `Challenges/Waste.md` WA-002's hazardous fractions use, pending
EC-014/GR-003 for final disposition. See PL-001.

---

## II. Pyrolytic Fuel Recovery Framework

Pyrolysis breaks down long-chain hydrocarbon molecules into shorter-chain liquid
and gaseous fuels. The process requires a closed system operating under three phases.

**Critical dependency:** This entire section depends on `Operations/Air_Scrubber.md`
being operational and maintaining alkaline buffering capacity before and during any
reactor run. Pyrolysis off-gas is toxic and flammable. Scrubber shutdown during an
active run is an emergency stop condition — see Drift Indicators. The alkaline
buffering stage in the scrubber is specifically required to neutralize any HCl
that bypasses halogenated feedstock rejection at triage. Cross-reference:
`Operations/Air_Scrubber.md` AS-003 (scrubber waste stream and saturation thresholds).

### A. Thermal Breakdown (The Reactor)

- Feedstock is sealed into an airtight batch reactor chamber
- The chamber is purged of oxygen — via inert gas purge or vacuum extraction —
  before heating begins. Purge completion must be logged before heat is applied.
- External heat raises the chamber temperature to **350°C–450°C** *(Analogous —
  standard pyrolysis temperature range for mixed polyolefins; halogen-free feedstock
  assumed)*
- At temperature, carbon-carbon bonds fracture, vaporizing solid plastic into
  gaseous hydrocarbons
- Reactor wall corrosion from residual acid gas is a credible long-term failure mode —
  see PL-002 for maintenance access and inspection requirements

### B. Condensation & Liquid Capture

- Vaporized gases are channeled from the reactor into a multi-stage condensation array
- Heavy-to-medium hydrocarbon chains condense at decreasing temperatures, producing
  pyrolytic oil (synthetic crude)
- Condensation array fouling from wax paraffins and heavy fractions is a maintenance
  item — cleaning access must be designed in from the start. See PL-002.
- Pyrolytic oil is stored for use as heating fuel, motor-generator input, or feedstock
  for downstream Forge thermal processes
- Oil stability and contaminant profile are uncharacterized at v0 — see PL-003

### C. Non-Condensable Syngas Channeling

- Light hydrocarbon gases (methane, ethane, propane fractions) will not condense at
  ambient temperatures and must be continuously drawn from the end of the condensation
  array
- Continuous draw maintains low-pressure state in the reactor — pressure buildup is
  a rupture risk. See PL-002.
- **Critical Safety Boundary:** Syngas must never accumulate in unvented spaces.
  Route immediately to a designated burner for controlled combustion, or channel
  directly into the Air Scrubber intake manifold for capture. The Air Scrubber is
  not a combustion device — syngas routed to the scrubber must pass through a
  dedicated combustion or thermal oxidation stage upstream of the scrubber inlet.
  Direct routing of unburned syngas into scrubbing liquid is not acceptable.

### D. Char and Solid Residue

- Real-world pyrolysis produces 5–20% solid char and ash residue by feedstock mass,
  depending on polymer type and contamination level *(Analogous — pyrolysis
  literature for mixed plastic feedstock)*
- Char composition is unknown at v0 — it may contain concentrated heavy metals,
  carbon black, inorganic fillers, and residual halogenated compounds from
  insufficiently rejected feedstock
- Char is not discarded as inert waste — it routes to `Operations/Gate_02_Triage.md`
  for assessment: potential carbon feedstock, potential hazardous waste requiring
  specialist handling
- Do not assume char is inert. Treat as potentially hazardous until characterized.
  See PL-005.

---

## Integration Hooks

- `Operations/Air_Scrubber.md` — primary safety dependency; off-gas capture,
  HCl neutralization via alkaline buffering stage, syngas combustion upstream
  of scrubber inlet; cross-reference AS-003 for saturation thresholds
- `Operations/Gate_01_Intake.md` — halogenated polymer detection at entry;
  GI-003 augmented detection capability applies to plastic stream identification
- `Operations/Gate_02_Triage.md` — upstream routing decision for all plastics;
  char residue routes back here for hazardous vs. recoverable classification
- `Operations/Gate_03_Reduction.md` — pyrolysis is reduction-adjacent; shredding
  of bulk plastic feedstock before reactor loading follows Reduction doctrine
- `Operations/Gate_06_Fabrication.md` — mechanical repurposing path (filament
  drawing) connects to fabrication feedstock; RepRap stock quality feeds back
  to PL-004 threshold definition
- `Operations/Energy.md` — pyrolytic oil and syngas are candidate energy inputs
  to motor-generators and heating systems; reactor thermal demand feeds energy
  accounting
- `Operations/Gate_05_Separation_Thermal.md` — waste heat from Spin Chamber
  is a candidate bootstrap heat source for reactor thermal demand (ASM-003,
  SC-007)
- `Admin/Trajectories.md` — fractional distillation, filament extrusion hardware
  specification, and deep characterization of oil quality are v1+ scope items
- `Architecture/Facilities.md` — siting and hot-work zone requirements;
  pyrolysis reactor clearance zones and ventilation topology (FA-001)
- `Admin/Safety_Protocols.md` — operator PPE standards; respiratory protection
  requirements for toxic off-gas handling

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Document created without syngas combustion stage specified | Syngas routed directly to Air Scrubber without noting that scrubber is not a combustion device — silent safety gap | Syngas must pass through dedicated combustion or thermal oxidation stage before scrubber inlet. Direct routing of unburned syngas into scrubbing liquid is not acceptable | Analogous | Yes — validate combustion stage design before first hot run |
| 2026-05-27 | Audit Review  | Char residue not acknowledged in initial draft | Pyrolysis always produces solid residue; omitting it created an incomplete material balance and a potential untracked hazardous waste stream | Char handling added as Section D. Char routes to Gate_02_Triage for classification — do not assume inert | Analogous | Yes — characterize char composition during first operational run |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### PL-001 — Halogenated Polymer Contamination (PVC / Teflon)

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Chemical Safety                                  |
| Blocking      | Yes (before any hot operational runs)            |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** PVC and other halogenated plastics release hydrochloric acid (HCl)
gas and toxic dioxins when subjected to pyrolysis temperatures. Even small quantities
contaminate the entire reactor batch.

**Why It Matters:** HCl corrodes steel reactor vessels from the inside out over
repeated cycles and easily bypasses basic carbon filtration, creating both a
structural failure risk and a toxic environmental hazard. Dioxin release is a
severe long-term health and contamination risk.

**Resolution Path:** Define and validate a triage rejection protocol before first
hot run — minimum: Beilstein test (copper wire, green flame = halogen present)
and density sorting (PVC ~1.4 g/cm³). Cross-reference `Operations/Gate_01_Intake.md`
GI-003 for augmented detection capability. Verify that `Operations/Air_Scrubber.md`
alkaline buffering stage (cross-reference AS-003) is capable of neutralizing
accidental acid gas bypass from imperfect triage rejection. Payment via
Specification once triage protocol is validated against a representative
feedstock sample and scrubber alkaline stage is confirmed.

**Grok review 2026-08-15:** Path adequate. Beilstein + density sorting are concrete v0 methods; GI-003 and AS-003 cross-refs are real and correctly load-bearing. Blocking Yes before any hot run is correct. **Grok approved (path adequate).** Remains Open — triage protocol still needs definition + validation; do not run hot pyrolysis until closed.

**Spec-depth pass, 2026-08-15 (digital-only — no equipment exists yet):** Verified against source before acting on Grok's shared-cluster proposal. This file's "specialist disposal" destination and `Challenges/Waste.md` WA-002's "routed per WA-004/GR-003" were two different sentences pointing at the same undefined place — neither named a real path. Resolved by extending `Operations/Gate_02_Triage.md` TS-002's existing Contaminated bin non-decontaminable state (built earlier this session) to explicitly cover compositional hazards, not only surface contamination — no new destination invented, an existing one reused. Both files now converge on the same named hold. Does not change PL-001's disposition status or Blocking Yes — final disposal still correctly awaits EC-014/GR-003.

---

### PL-002 — Reactor Thermal Runaway, Pressure Control, and Maintenance Access

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Major                                            |
| Type          | Mechanical Engineering / Safety                  |
| Blocking      | Yes (before reactor fabrication)                 |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The rate of vapor generation must not exceed the throughput
capacity of the condensation plumbing. Additionally, the reactor and condensation
array will experience progressive corrosion (acid attack from trace HCl), wax
fouling in condenser passages, and thermal cycling fatigue — none of which have
defined inspection intervals or maintenance access provisions.

**Why It Matters:** Rapid gas expansion inside a hot sealed container can cause
explosive mechanical rupture. Progressive corrosion or fouling without maintenance
access creates silent failure modes — the reactor degrades without visible
external indicators until a breach occurs.

**Resolution Path:** Specify a passive, high-reliability mechanical pressure
relief system (liquid-sealed bubbler lock) that allows emergency pressure relief
without admitting ambient air to the hot reactor. Define maintenance access points
for reactor interior inspection, condenser cleaning, and corrosion assessment.
Establish minimum inspection interval cadence (Placeholder — to be defined during
first operational cycle). Payment via Specification once relief system design is
validated and maintenance access provisions are incorporated into reactor design.

**Grok review 2026-08-15:** Path adequate. Passive bubbler-lock relief (no air ingress) is the right architecture for an oxygen-free hot reactor; maintenance access and corrosion inspection are correctly co-specified. Blocking Yes before fabrication is correct. **Grok approved (path adequate).** Remains Open — design still needs to be written and validated.

---

### PL-003 — Pyrolytic Fuel Stability and Contaminant Profile

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Minor                                            |
| Type          | Fuel Chemistry                                   |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Recovered synthetic crude oil from mixed plastic pyrolysis is
often acidic and contains wax paraffins that separate and solidify at room
temperature. Contaminant profile varies by feedstock composition.

**Why It Matters:** Unrefined oil may clog secondary engine injectors or rapidly
corrode standard fuel storage containers if left untreated. Acidic oil damages
motor-generator components not designed for fuel oil service.

**Resolution Path:** Characterize minimum filtration or post-process washing steps
required to render oil stable for long-term storage in Forge auxiliary power
reserves. Cross-reference `Operations/Energy.md` for integration with motor-generator
fuel input. Payment via Specification once oil quality is characterized from first
operational reactor run.

**Grok review 2026-08-15:** Path adequate. Correctly deferred to first operational run for characterization; Energy.md cross-ref is real. Non-Blocking is appropriate. **Grok approved (path adequate).** Remains Open — needs measured oil quality data.

---

### PL-004 — Mechanical Filament-Drawing Threshold Not Defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical Specification                          |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-26                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The exact conditions under which mechanical plastic recycling
(RepRap filament drawing) becomes unfeasible due to contamination or structural
degradation are unquantified. Triage routing between mechanical and pyrolysis
paths currently relies on operator judgment against provisional visual heuristics.

**Why It Matters:** Without a defined boundary, subjective routing during triage
may cause degraded feedstock to clog the fabrication gate or viable feedstock to
be prematurely destroyed.

**Resolution Path:** Establish formal triage heuristics — minimum: brittleness
snap test, melt-flow observation, polymer identity check (Beilstein, density,
or burn characteristics). Define pass/fail criteria for mechanical repurposing
routing. Candidate methods: melt-flow index testing (simple improvised version
feasible at v0), density measurement in water bath. Payment via Specification
once heuristics are validated against first operational triage cycle with
representative mixed feedstock.

**Grok review 2026-08-15:** Path adequate. Heuristics are concrete and v0-feasible; correctly resists inventing numeric thresholds without data. **Grok approved (path adequate).** Remains Open — needs validation against real mixed feedstock.

---

### PL-005 — Char and Solid Residue Composition Uncharacterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Chemical Safety / Waste Management               |
| Blocking      | No                                               |
| Owner         | Operations/Plastics.md                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Pyrolysis produces 5–20% solid char and ash residue by feedstock
mass. Char composition from mixed plastic feedstock is unknown — it may contain
concentrated heavy metals, carbon black, inorganic fillers, and residual halogenated
compounds.

**Why It Matters:** If char is treated as inert waste and disposed of without
characterization, hazardous materials may be released into the environment or
contaminate downstream processing streams. If char has carbon or mineral recovery
value, uncharacterized disposal wastes recoverable material.

**Resolution Path:** Characterize char composition from first operational reactor
run using available analytical methods — at minimum, visual inspection and
solubility testing. Cross-reference `Operations/Gate_02_Triage.md` for routing
to hazardous hold or material recovery as appropriate. Cross-reference
`Operations/Gate_03_Reduction.md` GR-003 (biological and chemical waste disposal
doctrine) for hazardous char disposition path. Payment via Specification once
char composition is characterized and a routing decision tree is defined.

**Grok review 2026-08-15:** Path adequate. Correctly sequences after first operational run; GR-003 and Gate_02 cross-refs are real. Non-Blocking is appropriate until char exists to characterize. **Grok approved (path adequate).** Remains Open — needs measured char data + routing tree.

---

### Resolution Log

- 2026-08-15: **Grok resolution-path review (Operations continuation — Plastics).** All five PL unknowns reviewed against source. Every Resolution Path judged adequate; residual evidence needs (triage validation, reactor design, first-run characterization) correctly retained. Cross-refs (GI-003, AS-003, Energy.md, Gate_02, GR-003) verified real. Markers added; Last Reviewed → 2026-08-15 on all five. **No PL-* closed.** Open Unknowns remain 5. Blocking status unchanged (PL-001 and PL-002 Yes). Human-directed.

- 2026-08-15: **PL-001's disposal destination named — points to
  `Operations/Gate_02_Triage.md` TS-002's Contaminated bin instead of an
  undefined "specialist disposal."** Same pass wired WA-002 to the same
  destination. No change to PL-001's Blocking status or triage protocol
  requirement. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **5** = PL-001–005, matches local
  sidecar and `Unknowns.md`. (2) PL-001 correctly **Blocking Yes / Critical**
  (before any hot operational runs). (3) PL-002 correctly **Blocking Yes**
  (before reactor fabrication). (4) No PL-* closed; no pyrolysis claims
  advanced. Human-directed.

- 2026-05-27: PL-002 — Scope expanded from pressure control only to include
  maintenance access and corrosion inspection requirements. Finding from Grok
  Skeptic/Auditor audit 2026-05-27.
- 2026-05-27: PL-004 — Resolution path expanded to include specific candidate
  triage methods (melt-flow index, density bath, Beilstein). Finding from Grok
  Skeptic/Auditor audit 2026-05-27.
- 2026-05-27: PL-005 — New entry. Char and solid residue handling gap identified
  in Grok Skeptic/Auditor audit 2026-05-27. Section D added to body.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates.md` (PC-001).
  Scope Boundary updated — `Architecture/Facilities.md` added for siting and
  hot-work zone requirements (PC-002); `Admin/Safety_Protocols.md` added for
  operator PPE and respiratory protection standards (PC-003). Both added to
  Integration Hooks.

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                                                      | Reconsider? |
|------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-27 | Direct syngas routing to Air Scrubber without combustion stage    | Air Scrubber is not a combustion device — routing unburned flammable gas into scrubbing liquid creates fire and explosion risk inside the scrubber | No — combustion stage upstream of scrubber inlet is permanent doctrine |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Pyrolysis reactor heated without logged oxygen purge completion
- Air Scrubber not operational or not verified before reactor heating begins
- Halogenated polymer triage rejection protocol bypassed or made optional
- Syngas routed directly to Air Scrubber without upstream combustion stage
- Char residue treated as inert and disposed of without characterization
- PL-001 triage protocol introduced without Beilstein test or equivalent
  halogen detection method
- Reactor fabricated without pressure relief system per PL-002
- Pyrolytic oil used in motor-generators without PL-003 characterization
- Mechanical repurposing path used for visibly degraded or unknown-identity polymer
  without PL-004 heuristic check
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.
