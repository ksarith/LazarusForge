# Tests/Support_Raft.md — Regional Anchor Infrastructure

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

> *The Raft's value is measured by what it enables in the units, not what it does directly.*
> *The hull is implementation. The anchor is doctrine.*

---

## File State

| Field | Value |
|---|---|
| **Status** | Exploration |
| **Body Stability** | Volatile |
| **Spec Gates** | 0/6 |
| **Verification Ref** | `Admin/Verification_Gates.md` |
| **Last Audit** | 2026-06-11 |
| **Auditor** | Gemini (Auditor) |
| **Open Unknowns** | 13 |
| **Active Disputes** | 0 |
| **Highest Risk** | High — SR-001 (galvanic corrosion) is Open/High and required before v1.0; a hull that corrodes faster than modeled threatens the whole anchor-node concept |
| **Sidecar Link** | #auditor-notes--unknowns |
| **Ethical Anchor** | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Legacy cross-reference fields (retained for continuity):**

| Field | Value |
|---|---|
| **Version** | v0.6 |
| **Owner** | Tests/ |

---

## Scope Boundary

**This file owns:**
- The doctrine of stationary regional anchor infrastructure in the Leviathan ecosystem
- The five anchor roles (Energy, Truth, Recovery, Material, Communication) and their responsibilities
- The SWATH hull implementation and Sacrificial Shell System as current v0 answers to those roles
- The failure philosophy and succession doctrine for regional anchor infrastructure
- SR-001 through SR-013 as the owning file's sidecar unknowns

**This file does not own:**
- Leviathan unit architecture and autonomy doctrine → `Tests/Leviathan_testing.md`
- Galvanic corrosion chemistry and rates → `Architecture/Chemistry.md` CE-001
- Biofouling challenge framing and ecosystem-safe doctrine → `Challenges/Biofouling.md`
- Firmware trust and cache integrity doctrine → `Operations/Electronics.md`
- Repository integrity and cache governance → `Admin/Repository_Integrity_Protocol.md`
- Energy philosophy and bootstrap-honest accounting → `Operations/Energy.md`
- Marine GECK seed variant → `Architecture/Geck_forge_seed.md`
- Storm-survival protocol and multi-Raft coordination → `Admin/Trajectories.md`
- Identity continuity and end-of-life provenance → `Admin/Ship_of_Theseus.md`
- Material separation gate operations → `Operations/Gate_05_Separation_Thermal.md`

**Scope note:** The Support Raft is an **anchor node**, not headquarters. It does not direct Leviathan unit behavior. It provides the infrastructure conditions under which units can operate effectively and return safely. The distinction between anchor and director must be preserved as the system scales.

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Governing cached document; local decision authority boundaries; Anti-Weaponization |
| `Admin/Governance_Charter.md` | Constitutional constraints on cache integrity and local authority scope |
| `Admin/Security_Protocols.md` | Cache sanitization doctrine; SEC-007 (external root-of-trust) applies to Truth Cache |
| `Admin/Auditor_Protocols.md` | Cached reference document; Unknown Bulk escalation protocol |
| `Admin/Ship_of_Theseus.md` | End-of-life and sacrificial shell philosophical grounding |
| `Operations/Energy.md` | Energy philosophy; bootstrap-honest accounting methodology |
| `Architecture/Chemistry.md` | Galvanic corrosion (CE-001); sacrificial anode material guidance |
| `Architecture/Geck_forge_seed.md` | Marine GECK seed variant informs minimal bootstrap configuration |
| `Challenges/Biofouling.md` | Biofouling challenge framing; ecosystem-safe doctrine |
| `Tests/Leviathan_testing.md` | Unit specs; swarm coordination; autonomy doctrine; knowledge tier routing |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Tests/Leviathan_testing.md` | LT-001 (power envelope), LT-003 (autonomy architecture), LT-004 (trust model) all depend on Raft capability characterization |
| `Admin/Trajectories.md` | Storm-survival protocol; multi-Raft coordination; SR-005 (succession) feeds v1 operational planning |
| `Architecture/Geck_forge_seed.md` | GK-002 (sacrificial anode material) resolution informs Raft anode specification |
| `Architecture/Friction_Dynamics.md` | FD-004 (reverse upstream link) — non-blocking housekeeping |

---

---

## File Purpose

This file exists to establish the Support Raft as stationary regional anchor infrastructure for mobile Leviathan units — the doctrine that mobile units stay lightweight and mission-focused by offloading energy, truth-verification, recovery, material processing, and communication needs onto a stationary node they return to, rather than each unit carrying that complexity itself. Without this file, those five functions would have no shared owner, and there would be no place enforcing the anchor-not-headquarters distinction as the system scales — the Raft providing infrastructure conditions is architecturally different from the Raft directing unit behavior, and that difference matters for autonomy doctrine.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | A stationary anchor node can provide a net positive energy and data surplus to the swarm that exceeds its own hull maintenance and infrastructure overhead | Foundational constraint named directly (Gemini audit, Gate 10) | Medium — asserted as a hard requirement, not yet validated with real figures | First full energy trace across Scale & Operating Envelope figures once they leave Placeholder status |
| ASM-002 | SWATH hull configuration is the right v0 implementation choice, though not a doctrine commitment — a spar buoy, semi-submersible, or anchored platform could equally satisfy the five anchor roles | Explicitly stated as an implementation decision, chosen for being proven, stable, and having internal volume for the five functions | Medium | A future site context or scale requirement makes SWATH's tradeoffs (draft, mooring complexity) worse than an alternative |
| ASM-003 | Operational cell size (~50–200 km²), supported unit count (8–40), and revisit frequency (12–72 hours) are reasonable v0 placeholders | Analogous to research vessel support zone conventions and LEO constellation coverage patterns | Low — explicitly Placeholder, all downstream claims inherit that status | Leviathan unit physical envelope and first trial deployment data become available |
| ASM-004 | Induction charging loss in real subsea conditions (20–40%) is a more reliable planning figure than the original laboratory estimate (12%) | Lessons Learned entry — laboratory figure was corrected against real subsea conditions (seawater conductivity, alignment variance, biofouling) | Medium — corrected once already, still Analogous rather than Measured | SR-004 (induction charging pad design) resolved with field-measured loss data |
| ASM-005 | The Raft can be treated as replaceable-by-design without that undermining swarm reliability, provided a next-generation platform exists before end-of-region protocol begins | Failure Philosophy & Succession doctrine — explicit design principle | Medium — the "next-generation platform must be present first" condition (SR-005) is itself still Open | SR-005 resolved with an operational sequencing plan defining minimum generational overlap |

---

## Body

### The Five Anchor Roles

The Support Raft is the stationary regional anchor for mobile Leviathan units operating in open-ocean or high-flow environments. Its purpose is to absorb complexity so that mobile units remain lightweight and mission-focused.

The Raft does not move. The Leviathan units do. That division of labor is the foundational architectural decision — and it must be preserved as the system evolves.

The Raft's role resolves into five distinct anchor functions:

**Energy Anchor** — The Raft harvests, stores, and distributes power to the swarm. It carries battery capacity and surface-area harvesting infrastructure that no mobile unit can match. Units return to the Raft not because they are directed to, but because it is where power is.

**Truth Anchor** — The Raft holds a local read-only cache of governing documents (`Admin/Ethical_Constraints.md`, `Admin/Auditor_Protocols.md`, `Discovery.md`). During communications blackout, units can verify their operating constraints against this cache. The Raft does not author truth. It stores it, verifiably, so it is accessible when the network is not.

**Recovery Anchor** — The Raft provides docking, passive retrieval, and cold storage for units that have lost operational capacity. A unit that cannot return to the swarm has a fixed location to drift toward. A unit that is recovered but non-functional has a place to wait without blocking active infrastructure.

**Material Anchor** — When hosted, the Material Separation Gate processes recovered material locally, reducing mass transfer to shore. The Raft accumulates the feedstock of its own successor. End-of-region protocol feeds its structural members into the next-generation platform.

**Communication Anchor** — The Raft provides satellite uplink windows that individual units cannot sustain. It queues, prioritizes, and relays knowledge tier traffic. It is the boundary between swarm-local knowledge and the wider network.

**Foundational constraint** *(Gemini audit Gate 10):* The Support Raft must provide a net positive energy and data surplus to the Leviathan swarm that exceeds the energy cost of its own hull maintenance and infrastructure overhead. A Raft that consumes more than it enables has failed its purpose regardless of how well it functions in isolation.

---

### Scale & Operating Envelope (v0 Placeholder)

All energy, docking, and storage sizing assumes the following placeholder ranges:

| Parameter | Value | Confidence |
|---|---|---|
| Operational cell | ~50–200 km² | Analogous — research vessel support zone conventions |
| Supported unit count | 8–40 Leviathan units | Placeholder — scales with hull energy capacity |
| Unit revisit frequency | Every 12–72 hours | Placeholder |
| Satellite uplink availability | 2–6 windows per day | Analogous — LEO constellation coverage |

All downstream claims that depend on these figures inherit their Placeholder status.

---

### Hull Architecture — SWATH Platform

The current v0 answer to the anchor role is a **Small Waterplane Area Twin Hull (SWATH)** configuration. This is an implementation decision, not a doctrine commitment. The anchor roles above could be satisfied by a spar buoy, semi-submersible, anchored platform, or future configuration. The SWATH is chosen for v0 because it is proven, stable, and has the internal volume to host the five anchor functions.

**SWATH configuration:**
- Two submerged hulls provide buoyancy below the wave action zone
- Narrow struts transfer minimal wave energy upward to the working platform
- Platform motion dramatically reduced vs. monohull or catamaran designs
- Proven in real-world research and survey vessel deployments

**Hull interior layout:**
- Power storage, ballast systems, and critical electronics housed in submerged hulls
- Working platform above struts houses docking ports, solar arrays, satellite comms, and Material Separation Gate when active
- Strut geometry designed to isolate Material Separation Gate vibration from hull structure

**Variable draft:**
- Calm conditions: higher draft for solar harvest and docking access
- Storm conditions: increased ballast lowers platform profile, reduces wave-induced motion
- Extreme conditions: critical systems already below waterline — storm mode is a reconfiguration, not an emergency

**Anchoring:** Primary conventional mooring; secondary dynamic positioning where mooring is impractical. Choice is deployment-specific — SR-008.

**Thermal management** *(Gemini audit finding):* The Raft's thermal rejection system (heat exchangers) is specified as **modular and expandable**. It must accommodate Material Separation Gate heat loads when the Gate is hosted without being oversized for Gate-absent baseline operations. SR-010 resolved — see Resolution Log.

---

### Sacrificial Shell System

Biofouling on stationary marine structures is inevitable. For a stationary SWATH platform, fouling threatens buoyancy-to-draft ratios and intake efficiency — particularly thermal heat sinks and induction charging pads. The alternative to fighting fouling is to design for it: accept colonization on designated surfaces and manage the cycle deliberately.

**Design concept:**
The SWATH hull outer surface below the waterline is a modular **sacrificial shell** — an outer layer designed for intentional colonization, planned shedding, and rapid replacement. The load-bearing inner hull is protected and never directly exposed to marine growth.

**Shell architecture:**
- Modular panels on quick-release fixtures along hull and strut geometry
- Panels structurally independent of inner hull — shedding one does not affect structural integrity
- Replacement panels snap into vacated mounts without dry-dock or human diver requirement

**Material selection criteria** *(SR-002 — Open):*
Candidate materials must: support natural marine organism attachment without toxic leaching; be structurally separable from inner hull; transition cleanly to artificial reef substrate when shed; ideally be fabricated from Forge output materials. No candidate material specified at v0.

**The shedding cycle:**
- Fouling accumulation rate monitored as Tier 2 knowledge signal per `Tests/Leviathan_testing.md`
- Leviathan units are the intended replacement agents — panel swap is a candidate task for swarm coordination
- Shed panels deposited as structured reef substrate or routed to `Operations/Gate_05_Separation_Thermal.md` if composition warrants recovery
- Panel composition and organism profile logged as water chemistry diagnostic

**Reef transition note:**
Shed panels deposited as reef substrate are environmental contribution, not waste. Ecological impact must be monitored and logged honestly. If the contribution proves neutral or negative, the design is revised.

---

### Energy Harvesting & Trace

*All figures labeled with confidence level. Infrastructure overhead included. Bootstrap-honest accounting per `Operations/Energy.md`.*

**Intake methods:**
- Hybrid solar-capture arrays — variable output, weather-dependent, zero output at night
- Oscillating wave-surge converters — supplemental only, never assumed reliable

**Infrastructure overhead** (must be subtracted before swarm charge budget is calculated):

| Load | Estimate | Confidence |
|---|---|---|
| Ballast pump operation | 5–50 kW during active draft adjustment | Analogous |
| Satellite communications | 50–200W during active uplink windows | Analogous |
| Onboard computing and sensors | TBD | Placeholder |
| Material Separation Gate (when active) | Per `Operations/Gate_05_Separation_Thermal.md` | Inherited |
| Recovery beacon and heartbeat monitor | Design target <10W continuous | Placeholder |

**Storage:**
- Solid-state battery buffers — target 150% of standard swarm-cycle charge plus Raft overhead (Placeholder pending Scale validation — SR-003)
- Salvaged battery banks acceptable at v0 per Bootstrap Doctrine

**Distribution:**
- Leviathan units dock at induction charging pads on submerged hull sections
- Induction loss budget: 20–40% under real subsea conditions accounting for seawater conductivity, alignment variance, and biofouling (Estimated — corrected from laboratory-optimistic 12% per Lessons Learned)
- Regional transmission loss: 5% (Analogous)

---

### Stasis Mode

If energy reserves fall below 20% of capacity:

**Suspended (in order of shed):**
1. Material Separation Gate — first non-essential load shed
2. Data Tether and satellite uplink
3. Docking charging (active induction pads)
4. Ballast active positioning — Raft holds last stable draft

**Maintained regardless of energy state:**
- Unit-recovery beacon
- Heartbeat monitor
- Passive mechanical recovery (magnetic grapples, tethers)

**Cold storage rack** *(SR-006 — In Progress):* Units recovered via passive mechanical means during Stasis are routed to a cold storage rack — physically secured but not occupying active induction docking ports. This prevents a dead-unit-clog scenario where non-functional units block active docking capacity. Rack capacity target: fixed multiple of supported unit count. Exact specification depends on Leviathan unit physical envelope (SR-006 resolution trigger).

*Stasis Mode single point of failure — resolved:* Recovery beacon and passive mechanical recovery remain active regardless of energy state. Units are not dependent on the Raft for autonomous survival — per `Tests/Leviathan_testing.md` Core principles, each unit remains operationally independent when network connectivity is lost.

---

### Truth Anchor — Orchestration & Cache Doctrine

**Local Truth Cache:**
- Read-only copies of `Admin/Auditor_Protocols.md`, `Admin/Ethical_Constraints.md`, and `Discovery.md` stored locally
- Cache is not editable by Leviathan units — reference only
- Cache updated only during verified satellite uplink sessions; version hash stored alongside documents
- Hash verification on cache read — corrupted or mismatched cache triggers Tier 1 alert

**Local decision authority during comms blackout:**
- **May:** continue charging, execute Stasis Mode, execute unit recovery, shed panels per threshold
- **May NOT:** update cached reference documents, modify swarm-wide operating parameters, authorize operations outside `Admin/Ethical_Constraints.md`

**Knowledge tier routing:**

| Tier | Content | Propagation |
|---|---|---|
| Tier 1 | Critical failures | Immediate flag, priority uplink queue, wide distribution |
| Tier 2 | Degradation patterns | Opportunistic propagation, context-dependent adoption |
| Tier 3 | Optimizations | Slow, selective propagation, experimental adoption only |

**Cache security** *(SR-007 — Open):* If a Raft is physically compromised, the Local Truth Cache exposes internal governance logic. Encrypted storage with remote-wipe capability triggered by hull breach sensor or loss-of-heartbeat is the resolution path. Cross-ref `Admin/Security_Protocols.md` SEC-007. Design required before v1.0 deployment.

---

### Mechanical Design & Resilience

**Modular docking:**
- Universal docking ports on working platform and submerged hull sections
- Passive capture sufficient for recovery of non-operational units
- Cold storage rack for units recovered during Stasis (see Stasis Mode above)

**Passive recovery:**
- Mechanical tethers and magnetic grapples for lost-heartbeat unit retrieval
- Passive and near-passive systems — functional in Stasis Mode
- Retrieved units isolated from swarm network pending fault assessment

**Platform stability:**
- SWATH hull geometry provides primary stability
- Active ballast provides secondary adjustment
- Material Separation Gate mounted with vibration isolation

**Thermal management:**
- Heat exchangers specified as modular and expandable
- Baseline-rated for Raft-only operations; expandable to Gate-integrated heat loads
- SR-010 resolved — see Resolution Log

---

### Material Separation Gate Hosting

Optional hosted capability. The Raft functions without it. Not included in baseline energy or space budgeting.

**Host when:**
- Unit-to-shore transfer mass cost exceeds mass reduction from pre-separation
- Swarm scale generates sufficient throughput
- Bootstrap material for next-generation Raft construction is needed locally

If hosted: the Raft provides power draw, thermal sink for heat pipe output, and Unknown Bulk logging relay. Gate operations are the first non-essential load shed under power constraint.

---

### Marine-Specific Challenges

**Biofouling:** Managed through Sacrificial Shell System. Accumulation rate is a monitored diagnostic signal. Challenge framing owned by `Challenges/Biofouling.md`.

**Galvanic corrosion:** Mixed metals in seawater with induced currents from induction charging creates aggressive galvanic corrosion potential. SR-001 — High priority, Open. Requires marine engineering input before v1.0 specification. Corrosion chemistry owned by `Architecture/Chemistry.md` CE-001.

**Storm loading:** SWATH variable draft partially addresses this. Full storm-survival protocol deferred to `Admin/Trajectories.md`. Design philosophy: survive by reducing profile, not by resisting wave energy.

**Pressure and depth:** Hull sections below waterline must be rated for expected depth range. Placeholder pending Scale section validation — SR-008.

**Marine regulatory environment:** Not addressed at v0. Exploratory unknown — route to `Admin/Ethical_Constraints.md`.

---

### Failure Philosophy & Succession

The Raft is not indispensable. It is replaceable. Those two properties are related — the Raft's design must make its own replacement possible.

**Failure modes and detection:**

| Failure | Signal | Tier |
|---|---|---|
| Induction loss rising above 40% baseline | Pad biofouling or alignment fault | Tier 2 |
| Wave converter declining output | Mechanical degradation | Tier 2 |
| Ballast system fault | Onboard inclinometer | Tier 1 if acute |
| Cache hash mismatch | Fall back to unit-local copies | Tier 1 |
| Satellite uplink loss | Normal operating condition | Not a fault |

**Degraded operation:** Partial intake loss reduces charge rate without suspending operations unless Stasis threshold is reached. Material Separation Gate is first non-essential load shed.

**End-of-region protocol:**
1. All recoverable electronics and high-value components extracted as Class A salvage
2. Sacrificial shell panels in good condition redeployed as structured reef substrate
3. Structural members fed into `Operations/Gate_05_Separation_Thermal.md` of next-generation platform
4. Next-generation platform must be present before end-of-region protocol begins — SR-005

**Succession principle:** The Raft's final act is enabling its successor. Nothing is wasted. The material of the current Raft becomes the feedstock of the next one. The knowledge of the current swarm cycle becomes the configuration baseline of the next one. Succession is not failure — it is the Raft fulfilling its long-term function.

The relationship between Raft and swarm is symmetric, not hierarchical:

```
Leviathan swarm
      ↔ Support Raft
      ↔ Shore Forge
      ↔ Other Rafts (at scale)
```

None are masters. Each occupies a scope. The Raft is not headquarters. It is an anchor node.

---

### Explicit Non-Goals (v0)

- Directing or overriding Leviathan unit behavior
- Achieving energy self-sufficiency for the regional cell
- Replacing shore-based Forge infrastructure
- Operating as a production system
- Guaranteeing reef contribution quality without monitoring

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| May 2026 | Analogous data correction | Induction loss estimated at 12% | Laboratory-optimistic; real subsea conditions with seawater conductivity, alignment variance, and biofouling push losses to 20–40% | Always use field analog data for marine energy estimates, not laboratory figures | Analogous | Yes — pending SR-004 field-measured data |
| May 2026 | Architectural review | Stasis Mode suspended all docking without cold storage rack | Created dead-unit-clog scenario — recovered but uncharged units blocking active docking ports | Passive recovery and active charging docks must be architecturally separated | High | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

*Full sidecar conversion, 2026-07-12 — prior format was a compact Status/Risk/Resolution Path table. Converted to the standard per-entry format below, matching the precedent set in `Tests/Living_Waters.md`'s same-day backfill.*

### SR-001 — Galvanic corrosion mitigation

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Blocking |
| Type | Technical |
| Blocking | Yes — required before v1.0 specification |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Mixed metals in seawater with induced currents from induction charging creates aggressive galvanic corrosion potential across the hull.

**Why It Matters:** A hull that corrodes faster than modeled undermines the entire anchor-node concept — the Raft is meant to outlast and outperform what mobile units could sustain alone. Corrosion chemistry itself is owned by `Architecture/Chemistry.md` CE-001; this unknown is specifically the mitigation strategy at the hull-design level.

**Resolution Path:** Marine engineering analog review; sacrificial anode placement, hull material selection, charging isolation. Cross-reference `Architecture/Chemistry.md` CE-001. Required before v1.0.

---

### SR-002 — Sacrificial shell material selection

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** No candidate material is specified at v0 for the sacrificial shell. Candidates must support natural marine organism attachment without toxic leaching, be structurally separable from the inner hull, transition cleanly to artificial reef substrate when shed, and ideally be fabricated from Forge output materials.

**Why It Matters:** The Sacrificial Shell System is the Raft's entire answer to biofouling — without a validated material, the shedding cycle this file's design philosophy depends on has no real substrate to build from.

**Resolution Path:** Marine materials literature review and prototype panel field testing. Three candidate classes identified, none yet selected.

---

### SR-003 — Battery buffer sizing

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Exact battery buffer sizing requires swarm count, mission duration, and depth profile — none of which are validated yet. Current target is 150% of standard swarm-cycle charge, held as Placeholder pending Scale validation.

**Why It Matters:** Undersized buffers risk Stasis Mode triggering too often under normal operation; oversized buffers waste hull volume and mass that could serve other anchor functions.

**Resolution Path:** Leviathan unit specs and trial deployment data required before this moves past Placeholder.

---

### SR-004 — Induction charging pad design

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Pad design must accommodate a 20–40% loss range under real subsea conditions, with biofouling compensation, following the correction from the original 12% laboratory-optimistic estimate (see Lessons Learned).

**Why It Matters:** Charging loss directly determines swarm charge budget — an unresolved pad design means the Energy Anchor role can't be sized with confidence.

**Resolution Path:** Subsea charging system analog review (MBARI, WHOI AUV docking programs).

---

### SR-005 — Succession sequencing (chicken-and-egg)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Architectural / Operational |
| Blocking | No — but blocks end-of-region protocol execution specifically |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** The next-generation platform must be present before end-of-region protocol begins, but no operational sequencing plan defines the minimum overlap period between generations.

**Why It Matters:** Without this, the Raft's own Succession Principle ("the Raft's final act is enabling its successor") has no concrete trigger condition — a Raft could decommission before its replacement is actually ready.

**Resolution Path:** Operational sequencing planning — minimum overlap period between generations. Routes to `Admin/Trajectories.md` for v1.

---

### SR-006 — Cold storage rack design

| Field | Value |
|---|---|
| Status | In Progress |
| Risk | Low |
| Priority | Minor |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Capacity, securing mechanism, and separation from active docks for the cold storage rack are not yet specified.

**Why It Matters:** The rack is what prevents the dead-unit-clog scenario (a real failure mode already surfaced in Lessons Learned) — an unspecified rack risks recreating that exact problem at a different scale.

**Resolution Path:** Rack capacity declared as a fixed multiple of swarm unit count. Specification trigger: Leviathan unit physical envelope defined.

---

### SR-007 — Cache sanitization on hull compromise

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical / Security |
| Blocking | Yes — required before v1.0 deployment |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** If a Raft is physically compromised, the Local Truth Cache — read-only copies of governing documents like `Admin/Ethical_Constraints.md` and `Admin/Auditor_Protocols.md` — exposes internal governance logic.

**Why It Matters:** A physically captured Raft shouldn't become a readable copy of the Forge's own governance doctrine. This is a genuine security exposure, not just a design nicety.

**Resolution Path:** Encrypted storage with remote-wipe capability triggered by hull breach sensor or loss-of-heartbeat. Cross-reference `Admin/Security_Protocols.md` SEC-007. Design required before v1.0 deployment.

---

### SR-008 — Dynamic positioning vs. mooring

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Whether primary conventional mooring or secondary dynamic positioning is used is deployment-site dependent and not resolvable in the abstract.

**Why It Matters:** Also determines hull section depth-rating requirements (see Marine-Specific Challenges — pressure and depth).

**Resolution Path:** Site characterization required. Exploratory until first site is selected.

---

### SR-009 — Ballast pump energy draw

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No — partial resolution already applied |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Energy draw during storm-mode draft reconfiguration is not fully characterized.

**Why It Matters:** Feeds directly into total energy trace and Stasis Mode threshold calculations.

**Resolution Path:** Analogous data from semi-submersible and research vessel ballast systems already added (5–50 kW range, Analogous estimate) as partial resolution. Must be validated before total energy trace is treated as reliable.

---

### SR-010 — Thermal management modularity for optional Gate hosting

| Field | Value |
|---|---|
| Status | Resolved |
| Risk | — |
| Priority | — |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-06 |
| Last Reviewed | 2026-06-11 |

**Description:** Whether the Raft's thermal rejection system can accommodate Material Separation Gate heat loads when hosted, without being oversized for Gate-absent baseline operation.

**Why It Matters:** Resolved — kept here for institutional memory per this file's own sidecar discipline, not because it's still open.

**Resolution Path:** Declared modular/expandable in the Mechanical Design section. Heat exchangers baseline-rated for Raft-only operation; expandable for Gate integration. Resolved 2026-06-11.

---

### SR-011 — Shell ROI efficiency

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical / Economic |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Panel swap energy cost versus intake recovery gain is not modeled — whether the Sacrificial Shell System's shedding cycle is actually worth its energy cost is unconfirmed.

**Why It Matters:** If ROI is negative, the shedding cycle needs redesign or a different cadence before it's a net-positive strategy rather than a net drain.

**Resolution Path:** Mathematical ROI model required. Depends on SR-004 (pad design) and an energy budget comparison.

---

### SR-012 — Mechanical bio-damping

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** Colonization impact on wave-surge converter moving parts — quantitative impact on converter efficiency is not characterized.

**Why It Matters:** Feeds SR-001 (corrosion mitigation); biological fouling and mechanical wear may interact in ways that make either unknown harder to resolve in isolation.

**Resolution Path:** Not yet defined — requires field data on converter efficiency degradation under real colonization conditions.

---

### SR-013 — Buoyancy shift from calcifying organisms

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Support_Raft.md |
| First Logged | 2026-05-04 |
| Last Reviewed | 2026-06-11 |

**Description:** The mass accumulation limit for calcifying organisms before SWATH control is overwhelmed is uncharacterized.

**Why It Matters:** SWATH's stability advantage depends on predictable buoyancy — uncontrolled mass accumulation could erode the platform-motion benefits the whole hull choice was made for.

**Resolution Path:** Depends on SR-002 (shell material selection); first operational deployment data required.

---

### Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **13** = SR-001–013, matches local +
  `Unknowns.md`. (2) SR-001 correctly **Blocking Yes** (before v1.0). (3)
  SR-007 correctly **Blocking Yes** (before v1.0 deployment). (4) No SR-*
  closed. Human-directed.

- 2026-07-12: Ethical Anchor field corrected — was using a non-canonical variant (backticked, `Admin/`-prefixed: "Defer to `Admin/Ethical_Constraints.md` if present.") instead of the canonical plain-text string ("Defer to Ethical_Constraints.md if present."). Same drift found across 9 files in a full-repository Phase 1 sweep (ChatGPT, adapted local-disk harness run) — verified independently against source before patching. No semantic change; the anchor's meaning was never in question, only its exact text.
| Date | Entry |
|---|---|
| 2026-05-04 | Induction loss estimate corrected from 12% (laboratory) to 20–40% (real subsea conditions). Logged in Lessons Learned. |
| 2026-05-04 | Stasis Mode single-point-of-failure contradiction resolved — recovery beacon and passive mechanical recovery remain active regardless of energy state. |
| 2026-05-06 | Cold storage rack concept added to Stasis Mode section — resolves dead-unit-clog contradiction identified by Gemini audit. |
| 2026-05-06 | Foundational claim sentence added to Purpose section — addresses Gemini Gate 10 finding. |
| 2026-05-06 | Ballast pump Analogous estimate added to Infrastructure Overhead — partial resolution of SR-009. |
| 2026-06-11 | SR-010 resolved — thermal management architecture declared modular/expandable in Mechanical Design section. |
| 2026-06-11 | SR-006 moved to In Progress — cold storage rack concept implemented in Stasis Mode; specification trigger defined (Leviathan unit physical envelope). |
| 2026-06-11 | File brought to File_Template.md compliance — Navigation Anchors, File State, Scope Boundary, Upstream/Downstream tables added. All stale file references corrected. Five-anchor Purpose framing adopted. Failure Philosophy & Succession section added. |
| 2026-07-12 | **Template-skeleton backfill and full sidecar conversion, v0.5 → v0.6.** Converted File State to the canonical field set, retaining legacy fields (Version, Owner) as a secondary table. Split the merged "Purpose — The Five Anchor Roles" header into a dedicated File Purpose section plus a Body subsection, matching template order. Added a standalone Assumptions section (5 entries, extracted from existing Foundational Constraint, Scale placeholder figures, and Lessons Learned content — no new claims introduced). Wrapped all remaining content sections under a new `## Body` header. Converted Lessons Learned to the canonical 7-column schema. Added an explicit (empty) Active Disputes section. Converted the compact Open Unknowns table (13 entries) into full per-entry sidecar format (Status/Risk/Priority/Type/Blocking/Owner/Description/Why It Matters/Resolution Path) under a renamed `## Auditor Notes & Unknowns` section, mirroring the same-day `Tests/Living_Waters.md` precedent — Risk and Priority values derived from the existing compact table and body cross-references, not newly asserted. Added Abandoned Paths and Drift Indicators (both previously absent). |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| May 2026 | Stasis Mode suspending all docking (including passive recovery) below the energy threshold | Created a dead-unit-clog scenario — recovered but uncharged units blocked active docking ports, and units lost the ability to be passively recovered exactly when energy scarcity made recovery most needed | No — passive recovery and active charging docks are now architecturally separated by design |
| — | Laboratory-optimistic 12% induction loss figure | Superseded by 20–40% real-subsea-condition estimate once field analog data was applied | No — retained only as the "what failed" example in Lessons Learned |

---

## Drift Indicators

- Body proposes the Raft directing or overriding Leviathan unit behavior — violates the anchor-not-headquarters distinction this file exists to preserve
- Energy self-sufficiency for the regional cell is proposed as a design goal — explicitly listed as a Non-Goal at v0
- A Scale & Operating Envelope figure is cited as validated rather than Placeholder/Analogous without a corresponding LW-TEST-style empirical result
- SWATH is treated as a locked doctrine commitment rather than a reversible v0 implementation choice
- End-of-region protocol is initiated without a next-generation platform confirmed present (SR-005 condition)
- SR-001 (galvanic corrosion) or SR-007 (cache sanitization) remain unresolved past v1.0 specification despite both being explicitly required before that milestone
- Foundational constraint (net positive energy/data surplus to the swarm) is not re-verified once real Scale figures replace the current Placeholder values
- Ethical Anchor field is absent, altered, or does not match the canonical string

---

*See: `Tests/Leviathan_testing.md` for unit autonomy doctrine, swarm coordination, and knowledge tier classification. See: `Challenges/Biofouling.md` for the biofouling challenge framing that the Sacrificial Shell System answers. See: `Admin/Trajectories.md` for storm-survival protocol and multi-Raft coordination. See: `Admin/Ship_of_Theseus.md` for end-of-life and succession philosophical grounding. See: `Unknowns.md` for all cross-module SR unknown dependencies.*

---

*This file defines the doctrine and current implementation of regional anchor infrastructure. It does not freeze the hull form.*
*The Forge's answer to this challenge will evolve. The anchor roles it names will not.*
