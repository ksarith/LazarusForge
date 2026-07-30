# Facilities.md — LazarusForgeV0

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

> ⚠️ **Operational Safety Advisory**
> This file governs the physical environment in which arc welding, induction heating,
> pyrolysis-adjacent processes, and powered reduction equipment operate. An inadequate
> facility is not a degraded-mode problem — it is a silent prerequisite failure that
> makes every other module unsafe by default. Combustible flooring beneath a welding
> station, inadequate airflow topology, or uncontrolled egress paths cannot be
> compensated for by process-level precautions alone. Open unknown FA-001 (site
> confirmation) means no specific facility has been validated against these constraints.
> When in doubt about site adequacy, hold — do not begin hot operations until flooring,
> airflow, and egress have been physically verified.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-07-29                                                          |
| Auditor          | Claude — Architect/Auditor; Claude — Synthesizer/Auditor, Section VII "Operational Launch, defined" + deferred-parameters reference added, scoped down from a broader multi-agent proposal (human-directed), 2026-07-29 |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Life Preservation doctrine; operator safety as a hard constraint |
| `Admin/Safety_Protocols.md` | PPE doctrine; heat stress thresholds; hearing conservation; cross-reference for operator capability assumptions |
| `Admin/Governance_Charter.md` | Constitutional constraints on site operations |
| `Operations/Air_Scrubber.md` | Negative pressure doctrine that Airflow Topology section implements at facility level |
| `Operations/Energy.md` | Grid power assumption (ASM-001); load planning for sequential vs. concurrent operation |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Operations/Gate_01_Intake.md` | Site-level intake zone constraints |
| `Operations/Gate_03_Reduction.md` | Hot Zone flooring and airflow prerequisites for reduction equipment |
| `Operations/Gate_04_Separation_Mechanical.md` | Floor loading and Hot Zone constraints for rotor operation |
| `Operations/Gate_05_Separation_Thermal.md` | Hot Zone prerequisites for induction heating |
| `Operations/Gate_06_Fabrication.md` | Welding zone and triangle workstation layout |
| `Operations/Electronics.md` | Warm Zone constraints for chemical handling and soldering |
| `Operations/Woodworking.md` | Dust and combustible storage zone separation |
| `Architecture/Friction_Dynamics.md` | Climate parameter context for airflow and tribology sizing |
| `Architecture/Thermal_Systems.md` | Climate parameter context for thermal load calculations |
| `Admin/Safety_Protocols.md` | FA-002 (Hot Zone radius) feeds heat stress and PPE doctrine |

---

## Scope Boundary

**This file DOES define:**
- Minimum physical environment constraints for v0 Forge operations
- Nonburnable flooring as a hard prerequisite for hot operations
- Airflow topology doctrine (negative pressure zones, exhaust routing hierarchy)
- Triangle workstation layout principle
- **Reference Deployment Context (RDC)** — a declared climate and site baseline used throughout this file. Builders must substitute their own deployment parameters before any sizing or scheduling decisions. See Section VII — Site Initialization Checklist.
- Utility access doctrine (grid power, water, egress)
- Hazard zone separation principles
- Floor loading classification guidance for heavy equipment
- Bootstrap facility proxy — operating with available space under stated constraints
- **Site Initialization Checklist** — the structured interface between generic Forge doctrine and any specific deployment context

**This file DOES NOT define:**
- Air Scrubber hardware specifications or staging (→ `Operations/Air_Scrubber.md`)
- Safety program, PPE requirements, or hearing conservation (→ `Admin/Safety_Protocols.md` [PLANNED])
- Energy infrastructure beyond grid connection requirements (→ `Operations/Energy.md`)
- Specific module layouts or equipment footprints (→ owning gate files)
- Noise exposure limits (→ `Admin/Safety_Protocols.md` [PLANNED])
- Legal zoning compliance or permitting (→ FA-003 — human decision)
- Marine or off-site deployment environments (→ `Tests/Support_Raft.md`, `Tests/Leviathan_testing.md`)

---

## File Purpose

This file exists to resolve UNK-006 — the facility siting unknown referenced by seven
repository files with no owning document. Its purpose is not to specify a particular
building or layout, but to define the minimum physical environment constraints that any
v0 site must satisfy before hot operations begin. Without this file, every module that
depends on physical space assumptions is operating on undeclared premises. If this file
disappeared, no principled site assessment could be made and the repository would have
no record of what the facility is expected to provide versus what individual modules
are responsible for providing themselves.

**Portability note:** This file uses a Reference Deployment Context (RDC) rather than
a specific geographic location. The RDC is a temperate/humid continental climate
baseline — hot summers, mild winters, storm exposure. It is not a prescription.
Builders anywhere in the world can use this file by completing the Site Initialization
Checklist (Section VII), which surfaces every climate and site parameter the other
Forge files expect to be filled in. The doctrine is generic. The parameters are yours
to supply.

---

## Assumptions

| ID      | Assumption                                                                   | Basis                                      | Confidence | Expiry Trigger                                              |
|---------|------------------------------------------------------------------------------|--------------------------------------------|------------|-------------------------------------------------------------|
| ASM-001 | Grid power available at v0 bootstrap site                                    | Inherited from Components.md ASM-001       | Medium     | Off-grid deployment confirmed — route to Energy.md          |
| ASM-002 | Covered indoor or semi-enclosed space available                              | RDC climate — humidity, storm exposure | Medium     | Site survey contradicts covered space availability          |
| ASM-003 | Nonburnable flooring available or installable at acceptable cost             | Concrete slab common in industrial/garage  | Medium     | Site survey shows combustible-only flooring with no remedy  |
| ASM-004 | Adequate natural or forced airflow achievable at v0 bootstrap                | Air_Scrubber.md negative pressure doctrine | Medium     | Airflow modeling shows inadequate exhaust path              |
| ASM-005 | Human operator physically present during all hot operations at v0            | Bootstrap Doctrine — inherited from Components.md | High  | Autonomous operation capability demonstrated and validated  |
| ASM-006 | Reference Deployment Context (RDC) climate baseline applies — hot-humid summers, mild winters, storm exposure. Builders outside this climate zone must substitute their own parameters via the Site Initialization Checklist (Section VII). | Geographic context — see Section VII | Medium       | Deployment site confirmed outside RDC climate zone — substitute parameters via Section VII |

---

## I. Core Constraint — Nonburnable Flooring

Nonburnable flooring is the single hardest facility constraint at v0. It is not a
preference, a best practice, or a future upgrade path. It is a prerequisite for any
hot operation — arc welding, induction heating, pyrolysis staging, or reduction
equipment with spark potential.

**What qualifies:**
- Poured concrete slab (preferred — common in garages, warehouses, agricultural buildings)
- Concrete block or brick over packed earth (acceptable with inspection)
- Bare compacted earth with no embedded combustibles (marginal — document and review)

**What disqualifies:**
- Wood subfloor or plywood decking, regardless of surface treatment
- OSB, particle board, or engineered wood panel
- Rubber matting or foam underlayment as the primary floor surface over combustibles
- Carpet, vinyl, or laminate over combustible substrate

**Bootstrap proxy:** If a site has partial nonburnable flooring, hot operations are
restricted to the nonburnable zone. Combustible-floor areas may support intake, storage,
triage, and cold assembly only. Document the boundary. Do not let the boundary drift.

**Upgrade path:** Poured concrete overlay is achievable over existing slabs and some
subfloors. Route to FA-001 for site-specific assessment.

---

## II. Airflow Topology Doctrine

This file owns the spatial logic of airflow through the facility. Hardware specifications
for capture, filtration, and scrubbing belong to `Operations/Air_Scrubber.md`. What this
file defines is where exhaust goes, how zones relate to each other, and what the negative
pressure hierarchy looks like at the facility level.

### Negative Pressure Hierarchy

Hot process zones (arc welding, induction, pyrolysis staging, reduction) must operate
at negative pressure relative to adjacent areas. This means:

- Exhaust paths must exit the building, not recirculate to occupied or storage zones
- Fresh air supply enters from the cleanest available direction (away from exhaust outlets)
- Triage, intake, and storage zones sit upstream (positive pressure side) of process zones
- Human operator positions are always on the fresh-air side of any process exhaust plume

### Minimum Airflow Topology at Bootstrap

At v0 with minimal equipment, the minimum acceptable configuration is:
1. At least one dedicated exhaust path from the hot process zone to outside
2. Makeup air available (open door, vent, or window) on the opposite side of the space
3. No recirculation of process exhaust through HVAC into occupied areas

Forced ventilation (fans, blowers) supplements but does not replace directional topology.
A powerful fan exhausting in the wrong direction is worse than no fan.

### Reference Deployment Context (RDC) Climate Consideration

*The following values reflect the RDC baseline (hot-humid summers, mild winters, storm exposure). Substitute your deployment region's parameters — see Section VII.*

High summer humidity (RDC baseline: regularly 70–90% RH) affects airflow planning:
- Humid makeup air accelerates corrosion on exposed metal stock — storage zones need
  separation from process exhaust makeup air paths where possible
- Summer heat load inside enclosed spaces demands airflow even when process exhaust
  is not the primary concern — operator heat stress is a real failure mode
- Storm season (RDC baseline: spring/early summer) means exhaust penetrations need
  weather protection — an exhaust path that floods during rain is an airflow path
  that fails when most needed

**Substitution note:** High-arid deployments replace humidity corrosion concern with
dust infiltration management. Cold-climate deployments add frozen condensate risk
in exhaust penetrations. Tropical deployments intensify both humidity and heat stress
baselines. Document your substitution in the Site Initialization Checklist.

---

## III. Triangle Workstation Layout Principle

The triangle workstation principle applies where human operators coordinate multiple
process steps in sequence. The core idea: the three most frequently accessed positions
in a work sequence form a triangle, minimizing travel distance and keeping the operator
oriented without turning their back on active processes.

**Application to Forge layout:**

A v0 Forge workstation triangle typically connects:
1. Intake / staging position (where material arrives)
2. Active process position (welding, triage, assembly)
3. Output / verification position (where finished or processed material exits)

**Constraints:**
- Triangle vertices must all be on nonburnable flooring if any vertex involves hot work
- No vertex should place the operator between an active process exhaust and a fresh air
  supply — the operator should never be downwind of their own process exhaust
- The triangle should not cross a hazard zone boundary — a triangle that spans a welding
  zone and a storage zone without a clear boundary is a layout error, not a layout

**Bootstrap realism:** At v0, the triangle may be implicit rather than designed. The
principle is a check against layouts that force unnecessary travel, back-turning on
active equipment, or crossing of hazard zone boundaries repeatedly. If the natural
working pattern already satisfies these constraints, no redesign is needed.

---

## IV. Hazard Zone Separation

The facility contains zones with different hazard profiles. Separation prevents cascade
failures where an incident in one zone compromises another.

### Zone Classes

**Hot Zone** — Arc welding, induction heating, pyrolysis staging, reduction equipment.
Requires: nonburnable flooring, negative pressure airflow, clear egress, no combustible
storage within defined radius (FA-002 — radius not yet defined).

**Warm Zone** — Electronics harvesting, soldering, chemical handling (flux, acids,
cleaning agents). Requires: ventilated but not necessarily negative-pressure; nonburnable
or protected flooring; no open flame within the zone.

**Cold Zone** — Intake, triage, storage, cold assembly, artifact memory and compute.
Requires: covered space, humidity management (per RDC or your deployment climate — see Section VII), physical separation
from Hot Zone exhaust.

**Egress Corridor** — Unobstructed path from any zone to outside. Must remain clear
at all times. Not a storage location. Not a workspace. Not a temporary staging area.

### Separation Logic

Zones need not be separate rooms — a single open space can contain multiple zones if
the boundaries are marked, respected, and documented. Separation is functional, not
architectural. What matters:
- A zone boundary is defined
- Hot Zone exhaust does not cross into Cold Zone
- Egress corridors do not pass through Hot Zone
- Combustible storage does not occur in or adjacent to Hot Zone

---

## V. Floor Loading

Heavy equipment at v0 (reduction mill, induction unit, large compressor) may exceed
the load capacity of some floors. This is a site-assessment item, not a specification
item — the Forge works with available space.

**Minimum guidance:**
- Poured concrete residential slab: typically 40–50 lbs/sq ft distributed load
- Commercial or industrial slab: typically 125–250 lbs/sq ft
- Equipment with concentrated load points (single feet, skids) requires local
  assessment — a 500 lb machine on four 2-inch pads concentrates load significantly

**Bootstrap proxy:** If floor loading is uncertain, distribute equipment weight across
the largest practical footprint (plywood spreader plates over concrete are acceptable
for this purpose — the combustibility concern is the surface, not the substructure).
Document any equipment that exceeds estimated floor rating. Route to FA-001.

---

## VI. Utility Access Doctrine

### Grid Power

Grid power is assumed available at v0 (Components.md ASM-001). Minimum requirements:
- 240V single-phase service for arc welding (standard residential/light commercial)
- Surge protection on all sensor and compute circuits (Components.md Critical item 6/7)
- Circuit capacity sufficient for simultaneous operation of the expected hot process
  load — do not assume all processes run simultaneously at v0 bootstrap

**Bootstrap proxy:** If grid service is undersized, phase operations sequentially
rather than concurrently. Document the constraint. Route to Energy.md for load planning.

### Water

Water access for wet scrubbing (Air_Scrubber.md Variant 0–3) and general cleaning.
Minimum: outdoor hose bib or indoor utility sink within reasonable distance of scrubber
staging. Drain path required for wet scrubber effluent — do not discharge untreated
scrubber waste to surface water.

### Egress

Minimum two independent egress paths from the Hot Zone. At least one egress path must
be usable while carrying a person — not a roof hatch, not a window requiring a ladder.
Egress paths are marked, unobstructed, and reviewed at the start of each operating session.

---

## VII. Site Initialization Checklist

This checklist is the structured interface between the generic Forge doctrine in this file and any specific deployment context. Every Forge initialization must complete this checklist before the constraint values elsewhere in this file are treated as calibrated.

**How to use:** For each parameter, record your deployment value. Where the RDC baseline is the correct value for your context, note "RDC applies." Where it differs, note your local value and identify which file sections need re-reading with your substituted value.

---

### A. Climate Parameters

| Parameter | Why It Matters | Files That Use It | RDC Baseline | Your Value |
|---|---|---|---|---|
| Summer ambient temperature range | Operator heat stress; thermal load on process equipment | `Facilities.md` §II, `Architecture/Thermal_Systems.md`, `Admin/Safety_Protocols.md` | 85–100°F / 29–38°C (heat index higher) | _______________ |
| Summer humidity range | Airflow planning; corrosion on stored metal; condensation in exhaust paths | `Facilities.md` §II, `Architecture/Friction_Dynamics.md` §5 | 70–90% RH | _______________ |
| Winter ambient low | Fluid viscosity; cold startup loads; condensation in pneumatic systems | `Architecture/Thermal_Systems.md`, `Operations/Energy.md` | 25–40°F / −4–4°C | _______________ |
| Precipitation and storm exposure | Exhaust penetration design; covered space requirement; flood risk | `Facilities.md` §II, §VI | Significant storm season spring/early summer; periodic flooding possible | _______________ |
| Prevailing wind direction | Exhaust outlet placement; makeup air intake direction | `Facilities.md` §II | Variable; SE/SW prevailing summer | _______________ |
| Dust and particulate baseline | Air Scrubber sizing; bearing and sensor protection | `Architecture/Friction_Dynamics.md` §7, `Operations/Air_Scrubber.md` | Low-moderate | _______________ |

---

### B. Site Parameters

| Parameter | Why It Matters | Files That Use It | Minimum Required | Your Value |
|---|---|---|---|---|
| Floor type | Hard prerequisite for hot operations | `Facilities.md` §I | Nonburnable (concrete preferred) | _______________ |
| Floor area available for Hot Zone | Zone separation feasibility | `Facilities.md` §IV | ≥ 200 sq ft dedicated | _______________ |
| Covered/enclosed space | Weather protection for equipment and operators | `Facilities.md` §II | Yes — indoor or semi-enclosed | _______________ |
| Ceiling height at Hot Zone | Welding fume rise; overhead clearance for reduction equipment | `Facilities.md` §IV | ≥ 10 ft / 3 m recommended | _______________ |
| Grid power service | Arc welding and induction heating | `Facilities.md` §VI, `Operations/Energy.md` | 240V single-phase minimum | _______________ |
| Water access | Wet scrubbing; general cleaning | `Facilities.md` §VI, `Operations/Air_Scrubber.md` | Hose bib or utility sink within 50 ft | _______________ |
| Independent egress paths | Emergency exit from Hot Zone | `Facilities.md` §VI | Minimum 2, one person-width | _______________ |

---

### C. Regulatory Parameters

| Parameter | Why It Matters | Files That Use It | Action Required | Your Status |
|---|---|---|---|---|
| Zoning class | Industrial hot work may be prohibited in residential or commercial zones | `Facilities.md` FA-003 | Human decision before first hot operation | _______________ |
| Hot work permit requirement | Some jurisdictions require permit for arc welding or open flame | `Facilities.md` FA-003 | Verify with local authority | _______________ |
| Chemical storage limits | Acid, solvent, and flux storage may be regulated by quantity | `Operations/Electronics.md`, `Operations/Air_Scrubber.md` | Verify with local fire code | _______________ |
| Noise ordinance | Reduction equipment and blowers may exceed residential limits | `Facilities.md`, `Admin/Safety_Protocols.md` SP-003 | Verify before sustained operations | _______________ |

---

### D. Operational Parameters

| Parameter | Why It Matters | Files That Use It | RDC Baseline | Your Value |
|---|---|---|---|---|
| Operator count at v0 | Affects zone layout; supervision capacity; escalation paths | `Admin/Safety_Protocols.md`, `Facilities.md` ASM-005 | 1 operator minimum; 2 recommended for hot operations | _______________ |
| Primary salvage stream | Drives which gate files are most operationally relevant | `Architecture/Forge_flow.md`, `Operations/Gate_02_Triage.md` | Mixed consumer electronics and small appliances | _______________ |
| Operating hours | Heat stress risk; noise ordinance compliance window | `Facilities.md` FA-004, `Admin/Safety_Protocols.md` | Daytime, seasonal avoidance of peak heat | _______________ |
| Off-grid or grid power | Changes energy accounting baseline | `Operations/Energy.md` ASM-001 | Grid power available | _______________ |

---

### Operational Launch, defined

A site reaching "operational launch" is not a checklist state — it's this:
**FA-001 is resolved for a specific, physically-surveyed site, and the first hot-work
session under the verified constraints begins.** Completing this Section VII checklist
is not sufficient on its own; it's the pre-survey instrument FA-001's own Resolution
Path already requires before the physical survey. Nothing here creates a new gate,
status, or promotion state beyond what FA-001 and Section I–VI already define.

**Deferred governance parameters — informational, not part of the checklist above.**
These are values that cannot be honestly set yet anywhere in the repository, because
no site has reached operational launch and no real audit-cycle data exists to derive
them from. Listed here, once, so they don't stay scattered:

| Parameter | Owning file | Why it's deferred |
|---|---|---|
| GOV-012 stagnation-decay cycle count | `Admin/Governance_Charter.md` | Set to zero cycles, formally deferred 2026-07-19 — no elapsed operational time to calibrate against |
| Semantic Drift Score threshold (Post-Exit Monitoring) | `Admin/Auditor_Protocols.md` (AP-031) | Formally deferred 2026-07-29, same reasoning as GOV-012 |
| Unknown Accumulation Rate cycle count (Post-Exit Monitoring) | `Admin/Auditor_Protocols.md` (AP-031) | Inherits GOV-012's Cycle-unit ambiguity directly, not a separate gap |

**Re-derivation rule, stated once:** each value above is set from real elapsed-time /
audit-cycle data collected after this file's own operational launch (defined above),
using the method GOV-012 already specifies. None of them get a second guess — they
get a first real measurement.

---

*Builders initializing a Forge outside the RDC baseline: once you have completed columns D and E above, re-read Sections II, IV, and FA-004 with your substituted values. Any section that references "RDC baseline" should be re-evaluated against your local conditions.*

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### FA-001 — Site not yet confirmed or assessed

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | High               |
| Priority      | Critical           |
| Type          | Operational        |
| Blocking      | Yes — blocks all hot operations |
| Owner         | Facilities.md      |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** No specific v0 site has been confirmed, surveyed, or assessed against
the constraints defined in this file.

**Why It Matters:** All hot operation assumptions — flooring, airflow, floor loading,
utility access — are unvalidated until a site is physically assessed. A site that fails
the nonburnable flooring constraint cannot be remediated by process-level precautions.

**Resolution Path:** Physical site survey against Section I (flooring), Section II
(airflow), Section IV (zone separation), Section V (floor loading), Section VI (utility
access). Document findings. Promote to Draft when at least one site has passed minimum
assessment.

---

### FA-002 — Hot Zone minimum radius not defined

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Major         |
| Type          | Technical     |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** The minimum clearance radius between active Hot Zone processes and
combustible storage has not been defined. Referenced in Section IV but left as a
placeholder.

**Why It Matters:** Without a defined radius, the zone separation doctrine has no
enforceable boundary. An operator can comply with the letter of zone separation while
storing combustibles too close to active welding.

**Resolution Path:** Cross-reference AWS welding safety standards and NFPA 51B for
hot work minimum clearances. Define as a Facilities.md constraint once sourced.
Human verification required — FA-003 may apply.

---

### FA-003 — Legal zoning and permitting not assessed

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Major         |
| Type          | Governance    |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** Local zoning, fire code compliance, and operating permits for
industrial hot work and chemical handling at a v0 site have not been assessed.

**Why It Matters:** Operating without required permits is a legal and safety risk.
Some jurisdictions require inspection of welding and pyrolysis operations regardless
of scale.

**Resolution Path:** Human decision. Scope is jurisdiction-specific and cannot be
resolved by AI audit. Assign to human operator at site selection. Not blocking for
Exploration — blocking for first hot operation.

---

### FA-004 — RDC heat load impact on operator safety not quantified

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Minor         |
| Type          | Technical     |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-11    |

**Description:** Process heat from arc welding and induction combined with RDC summer
ambient conditions (heat index regularly exceeding 100°F in hot-humid baseline) may
create operator heat stress conditions that affect safe operation. No threshold or
mitigation doctrine is defined. Deployments in hotter or more humid climates face
elevated risk; deployments in cooler climates may be able to deprioritize this unknown.

**Why It Matters:** Operator impairment from heat stress is a silent failure mode —
the process continues but judgment degrades. This is relevant to the Human Override
Interface (Components.md Critical item 8) — an impaired operator is not a reliable
override mechanism.

**Resolution Path:** Route to `Admin/Safety_Protocols.md` for heat stress doctrine.
The Site Initialization Checklist (Section VII) now captures the deployment-specific
ambient temperature parameter that feeds this unknown. Resolution is partially unlocked
by Section VII deployment — a builder in a cool climate can note this as non-blocking
for their context. Builders in hot climates must treat as Critical before first summer
hot operation.

---

### FA-005 — Relationship between Facilities.md and UNK-006 resolution status

| Field         | Value              |
|---------------|-------------------|
| Status        | **Resolved**       |
| Risk          | —                 |
| Priority      | Minor             |
| Type          | Governance        |
| Blocking      | No                |
| Owner         | Facilities.md     |
| First Logged  | 2026-06-05        |
| Resolved      | 2026-06-11        |

**Resolution:** Facilities.md is confirmed as the owning file for the domain previously
tracked as UNK-006. Downstream dependent files (Gate_01, Gate_03, Gate_04, Gate_05,
Gate_06, Electronics, Woodworking) now reference Facilities.md in their Upstream
Dependencies tables following the PC-002 and PC-003 correction passes. UNK-006 is
resolved. Discovery.md Cross-Module Unknowns table updated. FA-005 closed.

---

### Resolution Log

- 2026-07-29: Section VII gained an "Operational Launch, defined" block
  and a "Deferred governance parameters" reference table — a scoped-down
  response to a multi-agent proposal (Grok, ChatGPT, Gemini) that had
  grown into a full four-tier parameter taxonomy, a formal site-lifecycle
  state machine, and a new canonical artifact schema. All three agents'
  factual citations checked out against source (§VII's actual content,
  FA-002/FA-004, Auditor_Protocols.md's Highest Verified Baseline
  doctrine, Forge_Audit_Kit.md's Verification Maturity Model — none
  fabricated), but the proposed apparatus itself was scope creep beyond
  what was asked: a plain-language launch definition tied to FA-001's
  existing Resolution Path, plus a one-time pointer list for AP-031's
  and GOV-012's deferred values. No new gate, status, or promotion state
  introduced. Claude — Synthesizer/Auditor, human-directed.
- 2026-07-28: Open Unknowns count corrected 3 → 4. All four of
  FA-001 through FA-004 checked individually and confirmed genuinely
  Open — surfaced by a Grok-run repo-wide desync audit, verified
  against source before correcting. FA-005 remains correctly
  Resolved and excluded. Claude — Synthesizer/Auditor,
  human-directed.
- 2026-06-11: Navigation Anchors block added. Upstream Dependencies and Downstream
  Dependents tables added. ASM-006 converted from Arkansas-specific to Reference
  Deployment Context (RDC) abstraction. Section II Arkansas Climate Consideration
  renamed and expanded with RDC substitution guidance and climate-type notes.
  Section VII Site Initialization Checklist added — structured interface between
  generic doctrine and deployment-specific parameters. FA-004 updated to RDC
  framing; resolution partially unlocked by Section VII. FA-005 resolved —
  UNK-006 ownership confirmed, downstream dependents confirmed referencing
  Facilities.md. Open Unknowns count updated 5→3. Last Audit updated.

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-06-05 | Prescribing a specific facility layout or floor plan | The Forge works with available space. A prescribed layout would be fictional at Exploration stage and would not survive first contact with an actual site. Constraints-based approach adopted instead. | No |
| 2026-06-05 | Deferring this file further due to lack of content | UNK-006 has 7 dependents. The cost of no file exceeds the cost of a thin Exploration file with honest assumptions. Minimum constraint doctrine is sufficient content to open the file. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional triggers
specific to this file:*

- A site is selected and operated without FA-001 being resolved
- Hot operations begin on a site with unverified flooring
- Zone separation boundaries are documented but not physically marked at the site
- Egress corridors are used for storage or staging
- FA-003 (zoning/permitting) is not assigned to a human owner before first hot operation
