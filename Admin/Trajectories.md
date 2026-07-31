# Lazarus Forge — Trajectory (v0 → Interstellar)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-23; revised 2026-06-08; revised 2026-06-24; audited 2026-06-26 |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Version trajectory from v0 through v5
- Survival threshold and exit condition per version
- Forge Regeneration Threshold (FRT) doctrine and floor value
- Revenue allocation framework (operator-defined layer)
- Scope routing destination for out-of-version capabilities
- Design doctrine notes governing version advancement
- Economic model placeholder for v1 profitability baseline
- v0→v1 Trajectory Items registry — discharged knowns awaiting deferred activation

**This file DOES NOT define:**
- Component taxonomy or implementation specs for future versions
  (defined in module documents when versions become active)
- Detailed economic model (→ `Admin/Economics.md`)
- FRT measurement and logging procedures
  (→ Operations/Gate_07_Utilization.md)
- Component procurement doctrine
  (→ Architecture/Geck_forge_seed.md)
- Formal quality certification standards (→ future v2+ assignment)

---

## File Purpose

This document outlines the evolutionary trajectory of the Lazarus Forge as a
system. Each version represents a capability threshold, not a finished product.
The Forge is treated as a living industrial organism: it begins fragile, gains
resilience, and eventually becomes location-independent.

This is the scope routing destination for the repository. When a capability or
feature is identified as beyond the current version's scope, it routes here.
Version milestones are survival thresholds — not specifications. Component
taxonomy and implementation specs for future versions do not exist in this
document; they are defined in module documents when those versions become active.

Without this file, out-of-scope capabilities accumulate in operational documents,
blurring the boundary between what the Forge can do now and what it is designed
to eventually become.

*Exit conditions are labeled **[Placeholder]** unless operational data or analog
systems provide a basis for a higher confidence label. All exit conditions require
external or proxy validation — see individual notes.*

---

---

## v0 — Proof of Persistence (Terrestrial Seed)

**Question answered:** Can a Forge exist at all?

**Core Characteristics**
- Single-location, Earth-bound
- Human-supervised operation
- Narrow material scope (1–2 metals)
- Energy externally supplied

**Required Capabilities**
- Melt, refine, and form basic metal stock
- Process recovered material into usable feedstock
- Maintain thermal control without catastrophic failure
- Document processes and outcomes

**Exit Condition** [Placeholder]
> The Forge can repair itself faster than it degrades.

*Verification note: This exit condition cannot be self-reported by the Forge — the detector and the thing being detected are the same system at v0. Verification requires an external observer or proxy metric (e.g., mean time between failures trending downward over N cycles, tracked by human operator). See UNK-026 / CO-001 in Components.md.*

---

## v1 — Self-Sustaining Industrial Node

**Question answered:** Can a Forge stay alive?

**Core Characteristics**
- Modular subsystems
- Semi-autonomous operation
- Expanded alloy handling
- On-site power generation (partial) — see `Operations/Energy.md`; UNK-011 / EV-001 tracks demand baseline

**Required Capabilities**
- Closed-loop material recovery
- Powderization and feedstock standardization
- Component fabrication for adjacent systems
- Environmental control (air, slag, heat)

**Exit Condition** [Placeholder]
> The Forge can operate profitably while reinvesting in itself.

*"Profitably" definition [Placeholder — see TR-001]:* Revenue or barter value generated from external outputs exceeds operating costs while maintaining a reinvestment rate sufficient to sustain v1 capability. Economic model and baseline not yet defined.

---

## v2 — Replicable Forge Network

**Question answered:** Can a Forge reproduce?

**Core Characteristics**
- G.E.C.K.-based seeding — see `Architecture/Geck_forge_seed.md` for G.E.C.K. definition and minimum viable seed. Marine and environmental variants tracked in UNK-005 / GK-003.
- Standardized interfaces
- Distributed documentation and learning
- Minimal expert intervention

**Exit Condition** [Placeholder]
> A Forge can be built without the original builders present.

*G.E.C.K. variant note: Applies to terrestrial deployments. Marine and off-world variants require additional seeding specifications — see UNK-005.*

---

## v3 — Off-World Industrialization

**Question answered:** Can a Forge leave Earth?

**Core Characteristics**
- Reduced gravity tolerance
- Vacuum-compatible processes
- Radiation-hardened control systems
- Extreme material reuse

**Required Capabilities**
- Regolith and asteroid material processing
- Autonomous maintenance cycles — *contingent on UNK-008 / LT-003 resolution in `Tests/Leviathan_testing.md`*
- Energy scavenging (solar, nuclear, thermal) — *nuclear energy scavenging introduces radiation containment, shielding, and decay management requirements not addressed at v0; see TR-003 (formalized 2026-07-05) — nuclear capability must not activate before that entry reaches Provisional Spec.*
- Zero-waste material flows
- Autonomous structural repair against micro-collision damage — *proposed capability, see TR-MET-001 in v3+ Trajectory Items (Proposed) below; contingent on the same autonomy dependency as autonomous maintenance cycles above*

**Exit Condition** [Placeholder]
> The Forge can survive without Earth resupply.

---

## v4 — Autonomous Stellar Industry

**Question answered:** Can industry scale without humans nearby?

**Core Characteristics**
- Fully autonomous operation — *contingent on UNK-008 / LT-003 (autonomy architecture) resolution*
- Adaptive process optimization
- Long-duration reliability

**Exit Condition** [Placeholder]
> The Forge can expand faster than it fails.

---

## v5 — Interstellar Propagation (Conceptual Horizon)

**Question answered:** Can civilization carry itself forward?

*Note: v5 is a conceptual horizon, not a testable milestone. No exit condition is defined — this is intentional. If a falsifiable exit condition ever becomes articulable, add it at that time.*

**Core Characteristics**
- Self-contained industrial ecosystems
- Multi-generational operation
- Minimal external instruction

---

## Design Doctrine Notes

- Version numbers reflect survival thresholds, not feature lists
- Each version must be stable before advancement
- Skipping versions leads to systemic fragility
- Capabilities listed under future versions are trajectory markers — component taxonomy and implementation specs for those versions do not exist until those versions become active

> A Forge that cannot begin humbly will never reach the stars.

---

## Forge Regeneration Threshold (FRT)

### Doctrine

A system that consumes more than it regenerates is in decline regardless of
how productive it appears in the short term. The birthrate analogy applies
directly: a country that falls below its population replacement threshold is
shrinking even while its current population remains active and productive.
A Forge that processes material indefinitely without reinvesting in its own
capability is extractive, not regenerative — and that contradicts the core
mission.

The Forge Regeneration Threshold is the minimum fraction of material
throughput value that must be reinvested in Forge capability development
to keep the system alive and growing.

This is not an efficiency metric. It is a survival metric.

### Definition

> **Forge Regeneration Threshold (FRT):** The minimum fraction of material
> throughput value reinvested in Forge capability development per operating
> cycle. A Forge operating below its declared FRT for more than [N]
> consecutive cycles is considered to be in systemic decline.

**FRT floor:** [2–5%] *(Placeholder — not yet validated against first
operational cycle. Apply conservative end of range until calibrated.
See TR-002.)*

**FRT cycle definition:** [Placeholder — one operating month, one audit
cycle, or one defined throughput batch. To be declared by operator at v0
commissioning.]*

### What Counts as Reinvestment

Reinvestment in Forge capability development includes:

- Purchase of precision components or tooling the Forge cannot yet
  self-fabricate (bootstrap procurement doctrine — correct at v0)
- Repair or replacement of degraded Forge subsystems
- Tooling upgrades that expand the precision ceiling
- Calibration equipment and measurement capability
- Documentation and institutional memory infrastructure
- Energy system improvements that reduce per-cycle draw

Reinvestment does not include:

- General operating costs (utilities, consumables, labor)
- Materials purchased for external fabrication jobs
- Revenue distributed to operator or community

### Revenue Allocation Framework

Beyond the FRT floor, remaining throughput value allocation is
operator-defined. The repository does not prescribe how the remainder
is distributed. Common paths include:

| Allocation Path | Notes |
|----------------|-------|
| Utilities and operating costs | Non-negotiable operational floor |
| Community contribution | Consistent with Axiom P-3 (Collaboration and Mutual Benefit) |
| Materials sale → component purchase | Trading recovered material value for purchased precision capability is not a failure of salvage-first doctrine — it is the bootstrap path applied to the regeneration cycle |
| Operator/owner return | Legitimate at any allocation above FRT floor |
| Additional capability reinvestment above FRT | Accelerates version advancement |

The only constraint the repository places on this allocation is the FRT
floor. Everything above that floor is the operator's domain.

### Relationship to Existing KPIs

The FRT is a companion metric to the primary KPI:

| Metric | Measures |
|--------|---------|
| Value recovered per kWh consumed | Operational efficiency per cycle |
| Forge Regeneration Threshold | System health across cycles |

A Forge can be highly efficient per cycle while still declining if it
never reinvests. Both metrics are needed to characterize a healthy system.

### FRT and Version Advancement

FRT doctrine applies differently across versions:

| Version | FRT Relevance |
|---------|--------------|
| v0 | FRT floor declared; measurement begins; Placeholder value applies |
| v1 | FRT calibrated against first operational data; incorporated into profitability baseline (TR-001) |
| v2 | FRT must be positive across the forge network — not just per instance |
| v3+ | FRT applied to off-world resource loops; definition extends beyond monetary value |

### Logging

FRT measurement and per-cycle logging lives in
`Operations/Gate_07_Utilization.md`. This document owns the doctrine and
floor value. Gate_07 owns the measurement record.

---

## v0→v1 Trajectory Items

Items explicitly discharged to this file from owning file sidecars. These are real but out-of-scope for v0 — they activate when the repository transitions toward v1 or when the conditions noted in each entry are met. Full entry detail remains in the owning file's sidecar; this section is the navigation registry.

| ID | Title | Owning File | Activation Condition | First Logged |
|---|---|---|---|---|
| CT-003 | Dependency_Priority_Map.md — explicit dependency ordering between governance, ontology, integrity, audit, and security files | `Admin/Canonical_Terms.md` | v0→v1 governance stabilization pass | 2026-05-27 |
| CT-007 | ID namespace allocation doctrine — IDs may not be reused; prefixes registered on cluster creation; collision resolution defined | `Admin/Canonical_Terms.md` | v0→v1 transition; activate before new file clusters added at v1 scale | 2026-06-23 |
| AP-015 | External contributor role classification — declaration class or waiver mechanism for non-governance contributors | `Admin/Auditor_Protocols.md` | v0→v1 transition; activate when Forge moves toward community deployment or network expansion | 2026-06-24 |
| AP-020 | Golden Dataset / textual calibration harness — model-agnostic audit calibration test matrix | `Admin/Auditor_Protocols.md` | v0→v1 transition; activate when multi-contributor or community deployment increases the calibration surface area | 2026-06-24 |
| GH-005 | Human vs. autonomous intervention fraction — what fraction of edge-case triage and fabrication problems benefit from human heuristic intervention vs. extended autonomous planning | `Tests/Cognitive_Salvage_Layer.md` | Activate with empirical data from first Leviathan operational cycles | 2026-06-24 |
| FAK-005-ceiling | Forge_Audit_Kit.md character ceiling — 12,000-char limit in Drift Indicators is structurally unachievable with current load-bearing content; ceiling parameter requires revisiting before v1 kit governance | `Admin/Forge_Audit_Kit.md` | v0→v1 kit governance pass; reassess ceiling against actual v1 content volume | 2026-06-24 |

*These entries do not carry unknown IDs — they are discharged knowns routed here for deferred activation, not open questions. They require no resolution pass in the current cycle.*

---

## v3+ Trajectory Items (Proposed)

Items proposed during session discussion but not yet part of any owning file's
active sidecar — distinct from the v0→v1 registry above, which routes items
*discharged from* existing sidecars. These are candidate future capabilities
only; logging them here prevents loss, not commitment. No resolution pass or
activation work is implied until a version's planning phase formally begins.

| ID | Title | Notes | First Logged |
|---|---|---|---|
| TR-MET-001 | Autonomous micro-meteorite repair swarm — small-scale autonomous units detecting and repairing micro-collision damage to off-world Forge structures/hulls | Proposed mid-session, not yet developed into a capability spec or routed to an owning file. Likely shares the UNK-008 / LT-003 autonomy dependency already tracked for v3/v4. No owning file assigned yet — candidate: `Tests/Leviathan_testing.md` (autonomy testbed) or a future off-world-specific test file. | 2026-07-05 |
| TR-MET-002 | Reactive-metal (titanium, Zr, Nb, etc.) atmosphere processing — `Operations/Gate_05_Separation_Thermal.md` §9's oxygen-tolerant, precision-gas-free atmosphere doctrine cannot support titanium or similar reactive metals (nitrogen embrittlement, oxygen pickup); would require full argon shielding or true vacuum. Astroid-miner's `Propulsion_Economy_isru/zero_g_fabrication.md` independently specifies Induction Heating + EM Levitation (crucible-free, high-purity, vacuum-native) as a primary technique for exactly this class of metal — confirmed present in the 2026-07-31 companion-repo upload. Per UNK-003 (Cross-repo assumption contracts, Deferred pending Leviathan milestone) and the 2026-07-19 Leviathan_testing.md merge anchor, this is recorded as supporting detail for a v3+ off-world capability, not a resolution to any current terrestrial unknown — see the Gate_05/reactive-metal item still open in that file's sidecar for v0–v2 status. | 2026-07-31 |

*This section holds candidate ideas only. An item graduates out of this table
when it is either (a) assigned an owning file and registered as a proper
sidecar entry there, or (b) explicitly declined and moved to Abandoned Paths
below with rationale.*

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                            | What Failed                                                           | What Was Learned                                                                                                   | Confidence | Revalidation Needed |
|----------|---------------|-----------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | Exit conditions written without confidence labels         | Implied false precision — conditions read as verified targets         | All exit conditions labeled [Placeholder]; verification notes added                                               | Replicated | No                  |
| May 2026 | Audit Review  | v5 written with same structural pattern as v0–v4          | Implied testable milestone status                                     | v5 explicitly designated as conceptual horizon with rationale for absent exit condition                           | Replicated | No                  |
| 2026-05-23 | Modeling    | No system health metric existed alongside efficiency KPI  | A Forge could be efficient per cycle while declining across cycles — the gap was invisible | FRT doctrine added. Efficiency and regeneration are distinct dimensions; both required to characterize a healthy system | Analogous | Yes |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                                      | Reconsider? |
|------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------|
| May 2026   | Exit conditions as verified targets without confidence labels     | False precision — implies operational validation that does not exist at v0                                         | No          |
| May 2026   | v5 as testable milestone with defined exit condition              | No falsifiable exit condition is currently articulable — forcing one produces theater                              | Yes — if falsifiable condition becomes articulable |
| 2026-05-23 | Fixed FRT percentage as mandatory doctrine                        | False precision at v0 — denominator unknown, operational cycles not yet run. Floating value with declared floor is more honest | No — floor remains floating until calibrated |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- FRT floor value claimed as validated without operational cycle data
- FRT floor removed or set to zero without explicit human rationale
- Revenue allocation framework prescribes operator allocation above FRT floor
- Exit conditions upgraded from Placeholder without external validation evidence
- Version capabilities listed as implementation specs rather than trajectory markers
- Stale flat filenames present in cross-references
- TR-001 or TR-002 unknown entries closed without resolution evidence
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### TR-001 — v1 profitability baseline undefined

| Field         | Value                  |
|---------------|------------------------|
| Status        | Open                   |
| Risk          | Medium                 |
| Priority      | Major                  |
| Type          | Architectural          |
| Blocking      | Yes                    |
| Owner         | Admin/Trajectories.md  |
| First Logged  | May 2026               |
| Last Reviewed | 2026-05-23             |

**Description:** What "profitably" means in the v1 exit condition remains
undefined — economic model, profit baseline, reinvestment definition, and
required rate are all absent.

**Why It Matters:** Without a defined profitability baseline, the v1 exit
condition cannot be verified — advancement from v0 to v1 is blocked.

**Resolution Path:** Full economic model is a v0→v1 transition task. Inputs
needed: (1) operating cost model from `Operations/Energy.md` — feeds from
EV-001; (2) revenue model for external outputs; (3) FRT-calibrated reinvestment
rate definition. `Admin/Economics.md` now owns the economic model and barter
doctrine — route TR-001 closure work there. FRT doctrine (TR-002) is a prerequisite input.

---

### TR-002 — Forge Regeneration Threshold floor value not yet calibrated

| Field         | Value                  |
|---------------|------------------------|
| Status        | Open                   |
| Risk          | Medium                 |
| Priority      | Major                  |
| Type          | Architectural          |
| Blocking      | No                     |
| Owner         | Admin/Trajectories.md  |
| First Logged  | 2026-05-23             |
| Last Reviewed | 2026-05-23             |

**Description:** The FRT floor is declared at [2–5%] Placeholder. The actual
minimum viable reinvestment rate has not been validated against operational
data. The cycle definition has not been declared by an operator.

**Why It Matters:** A floor that is too low allows systemic decline while
appearing compliant. A floor that is too high creates unsustainable obligation
at bootstrap scale.

**Resolution Path:** Discharge via Lessons Learned — calibrate FRT floor
against first operational cycle data. Operator declares cycle definition at
v0 commissioning. Update floor from Placeholder to Analogous once first cycle
data exists. Cross-reference TR-001 — FRT is a required input to the v1
economic model.

---

### TR-003 — Off-world nuclear containment architecture undefined

| Field         | Value                  |
|---------------|------------------------|
| Status        | Open                   |
| Risk          | High                   |
| Priority      | Major                  |
| Type          | Architectural / Safety |
| Blocking      | No — not yet active; blocks v3 nuclear capability specifically |
| Owner         | Admin/Trajectories.md  |
| First Logged  | 2026-07-05             |
| Last Reviewed | 2026-07-05             |

**Description:** v3's Required Capabilities list nuclear energy scavenging
as a candidate power source, with inline text already noting that it
"introduces radiation containment, shielding, and decay management
requirements not addressed at v0" and flagging itself as an "architectural
dependency when v3 planning begins." That flag was prose, not a tracked
unknown — this entry formalizes it. No containment/safety specification
exists anywhere in the repository for off-world nuclear capability.

**Why It Matters:** This is a hazard class distinct from everything else
currently tracked (structural, economic, governance) — radiation containment
failure is not a gracefully-degrading condition. Leaving it as inline prose
rather than a tracked unknown means it could be silently missed when v3
planning actually begins, since it would not appear in any Expiry Watch or
Open Unknowns count.

**Resolution Path:** Not active work at v0/v1 — this is a placeholder to
prevent the dependency from being lost. When v3 planning begins: (1) define
minimum containment/shielding/decay-management specification before nuclear
capability is activated in any v3 build; (2) route to whichever
Architecture/ file eventually owns power systems for off-world deployment;
(3) cross-reference `Admin/Ethical_Constraints.md` Life Preservation and
`Admin/Safety_Protocols.md` for hazard doctrine that should extend to this
case. Do not activate nuclear capability in any deployment before this
entry reaches at least Provisional Spec.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-05 Exploration audit —
formalizing a dependency the file's own v3 text had already flagged in
prose since 2026-06-26 but never registered as a tracked unknown.*

---

### Resolution Log

- 2026-07-05 (second entry, same day): **TR-003 logged** (off-world nuclear
  containment architecture) — formalizes a dependency v3's own text had
  flagged in prose since 2026-06-26 but never registered as a tracked
  unknown. Open Unknowns 2 → 3. High risk, not currently Blocking (v3 is
  not active), but nuclear capability may not activate before this reaches
  Provisional Spec. v3's Required Capabilities line updated to cross-
  reference it directly.

- 2026-07-05: **TR-MET-001 logged** (autonomous micro-meteorite repair
  swarm) as a proposed candidate item — new `v3+ Trajectory Items
  (Proposed)` section added, distinct from the existing v0→v1 discharged-
  knowns registry since this item was never anchored in an owning file's
  sidecar. No owning file assigned yet; not yet a formal unknown. v3's
  Required Capabilities gained one cross-reference line. Same dual-audit
  session (Grok + Gemini, Exploration audit) proposed six additional
  "institutional integrity" gaps (mission drift, value transmission,
  constitutional preservation, incentive capture, institutional memory
  degradation, cultural forking, external capture) — not registered here.
  These are real candidate questions worth a future look, but registering
  six new speculative unknowns in one pass during an already-heavy
  escalation period runs against the spirit of the Administrative Fatigue
  Governor doctrine (`Admin/Auditor_Protocols.md`) — held for human
  governing authority decision rather than auto-logged.

- May 2026: All exit conditions labeled [Placeholder]. Verification notes added per condition.
- May 2026: v5 designated as conceptual horizon — explicit rationale for absent exit condition.
- May 2026: G.E.C.K. cross-references added at v2. UNK-008 / LT-003 autonomy dependency noted at v3 and v4.
- May 2026: v0 exit condition verification note added — self-reporting circularity acknowledged, human proxy defined.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected
  from `Verification_Gates_LF.md` to `Admin/Verification_Gates_LF.md`
  (PC-001). Scope Boundary updated — `economics_v0.md` reference corrected
  to `Admin/Economics.md` (PC-003). TR-001 resolution path updated —
  `Admin/Economics.md` now owns economic model and barter doctrine.
- 2026-06-24: v0→v1 Trajectory Items section added. Six items registered:
  CT-003 (Dependency_Priority_Map.md), CT-007 (ID namespace allocation),
  AP-015 (external contributor roles), AP-020 (Golden Dataset),
  GH-005 (human vs. autonomous intervention fraction),
  FAK-005-ceiling (Forge_Audit_Kit.md 12,000-char ceiling revisit).
- 2026-06-26: Gemini + ChatGPT dual Skeptic/Auditor pass (Exploration audit).
  Three findings resolved: (1) Semantic drift — "Recycle scrap" → "Process
  recovered material" (v0); "Closed-loop material recycling" → "Closed-loop
  material recovery" (v1). (2) Lifecycle truncation — nuclear energy scavenging
  (v3) now carries containment/shielding dependency note. TR-001 and TR-002
  confirmed under Expiry Watch (6–7 cycles open, resolution paths exist).
  Gates cleared: G1, G2, G4, G5, G6. G3 deferred (Exploration stage).
