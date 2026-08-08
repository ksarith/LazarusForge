# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## Repository Role

This is the **active working repository** — lean, connected, and operational.
Doctrine and philosophy are developed in the companion repository `Lazarus-Forge-`
and refined here into practical implementation.

Divergence between the two repos is a signal, not a problem — it surfaces when
doctrine needs updating or practice has drifted from principles. Any contributor
(human or AI) who encounters a contradiction between repos must log it as a
Non-blocking Unknown in `Admin/Auditor_Protocols.md` and flag it in the next
review cycle. Divergence that goes unlogged is drift. Divergence that gets
logged is progress.

---

## What This Repository Is

LazarusForgeV0 is the active working repository for the Lazarus Forge — a
salvage-first, adaptive resource recovery system designed to preserve functional
value before material reduction.

**Core KPI:** Value recovered per kWh consumed.

---

## Objectives

**What "done" looks like for v0 (current version):** a physically-grounded,
governance-complete specification for a single-site salvage-first Forge —
every Gate (01–07) at Specification status, every Tier 1 Axiom load-bearing
and unchallenged across an audit cycle, and Security_Protocols.md's
constitutional root-of-trust (SEC-007a) resolved. v0 does not require
physical construction; it requires the specification to be complete enough
that construction could begin without unresolved Critical unknowns in the
load path.

**Standing objectives, in priority order:**
1. **Governance before autonomy** — Phase 3 cryptographic enforcement
   (`Admin/Security_Protocols.md`) does not activate until Phase 1
   (detection) and Phase 2 (structural halt) are proven and GOV-008
   (quorum) is resolved. Autonomous agents are not trusted to enforce
   governance before governance is enforceable.
2. **Physical plausibility before elegance** — a specification that cannot
   survive Gate 2 (Physical Plausibility) is not progress, regardless of
   how complete its governance framing is. EN-001, FA-001, and the
   hazardous-fraction unknowns (WA-002, PL-001, WW-005) are physical-layer
   objectives that do not get superseded by governance-layer work.
3. **Honest unknowns over false certainty** — the Unknown Budget floor
   exists because a specification with zero open unknowns is more likely
   incomplete than finished. Closing unknowns without evidence is a
   constitutional violation (Axiom Zero, EF-0.0), not progress.
4. **Institutional memory over individual sessions** — every mechanism in
   this repository (sidecars, Lessons Learned tables, the Resolved Unknown
   Discharge Procedure, Routing.md/Discovery.md itself) exists so a fresh
   agent with no session history can resume correctly. An objective that
   can only be pursued by an agent who remembers prior sessions is not
   compatible with this repository's design.

**Beyond v0:** marine deployment (Leviathan, Support Raft) and off-world
industrialization are declared long-term trajectory, not current-version
objectives — see `Admin/Trajectories.md`. Work that serves only the
long-term trajectory and has no v0 load-bearing purpose belongs there, not
in a v0-scoped file (Gate 4 — Scope Alignment).

---

## How to Use This File

> **Scope entries are navigation summaries only.**
> File-local Scope Boundary sections remain authoritative.
> Where this file and a file's own Scope Boundary conflict, the file wins.
> Update Discovery.md when files change; do not update files to match Discovery.md.

**Routing quick-reference:**
- "Where does this belong?" → find the owning file in the scope maps below
- "What files does this decision affect?" → check Downstream
- "What must exist before this file can be promoted?" → check Upstream and ⚠️ notes
- "What does this term mean?" → `Architecture/Forge_flow.md` §Defined Terms first; `Admin/Canonical_Terms.md` second
- Full detail always lives in the file itself

---

## Agent Orientation

**Read this section before contributing anything to the repository.**

This repository operates as a governed epistemic system, not a free-form document collection. Agents that treat it as a simple knowledge base will hallucinate files, invent authority, and produce outputs that conflict with committed specifications. The following five points prevent the most common failure modes.

**1. Mandatory session opening sequence**
Every session begins with: (a) load `Admin/Forge_Audit_Kit.md` — this is the runtime reference for all audit and contribution work; (b) declare your role before writing anything (`Skeptic/Auditor`, `Synthesizer`, `Engineer`, `Evidence/Auditor`, or `Connective Tissue`); (c) run the Audit Opening Checklist from the kit — Tier 1 Axiom verification and Epistemic Foundation integrity check are non-negotiable first steps.

**2. Do not invent files**
Before referencing, creating, or proposing any file, verify it exists in this Discovery.md scope map or in `Routing.md`. Aspirational files must be labeled `[PLANNED]`. Unlabeled references to nonexistent files are Fallacy 6 (Hallucinated Files) and will be rejected by the audit process.

**3. The epistemic state system governs all claims**
Every meaningful claim in this repository carries one of three epistemic states: `VERIFIED` (survived empirical grounding and adversarial falsification), `PROVISIONAL` (accepted for execution; flagged for validation), or `UNKNOWN` (no grounding exists). Collapsing `UNKNOWN → VERIFIED` without new empirical input is a constitutional violation under Axiom Zero (EF-0.0 in `Admin/Auditor_Protocols.md`). Claims also carry institutional provenance labels: Internally Derived → Analogous External → Experimentally Verified → Operationally Hardened. Unlabeled claims are treated as Placeholder.

**4. Unknowns are not problems to suppress**
`Unknowns.md` is the most important file in the repository for understanding current system state. Open unknowns are honest acknowledgments of ignorance — suppressing them or closing them without evidence is an integrity violation. The repository maintains an Unknown Budget (floor on acknowledged unknowns) to prevent false certainty. New unknowns surfaced by honest work are welcome; premature closures are not.

**5. The philosophical substrate**
The Forge's operating principles derive from two foundational documents: the Tier 1 Axioms in `Admin/Governance_Charter.md` (the constitutional floor) and the Nothingness Theorem in `Admin/Nothingness_Theorem.md` (the philosophical substrate). The theorem's core insight — that waste is not zero, that maintenance is thermodynamically equivalent to creation, and that distributed disagreement is the primary engine of error correction — underlies the salvage-first doctrine, the multi-agent audit architecture, and the anti-sacralization principle. A third foundational document, `Admin/Computational_Institutional_Reasoning.md`, formalizes the system's epistemic governance mathematically — Unknown Conservation, Governance Stability, Epistemic Debt Instability, and Institutional Memory Dominance are proven as theorems there, and the non-linear Verification Algebra (Physical Grounding Gate, Provenance Ceiling Gate, Adversarial Multiplier) that governs claim maturity throughout this repository is specified in full there. Agents are not required to read either document, but those who do will find they explain why the system is structured the way it is.

---

## Repository Structure

```
Root
├── README.md                               — Project overview and core principles
├── Discovery.md                            — Navigation layer (this file)
├── Routing.md                              — Programmatic file index; raw URLs for agent context loading
├── Unknowns.md                             — Cross-module unknowns global index

Admin/                                      — Governance, protocols, and doctrine
    ├── Adm_Scope_Map.md                     — Per-file scope/dependency index for this folder (2026-08-07)
    ├── Governance_Charter.md               — Constitutional tier; 8 Axioms (Tier 1)
    ├── Ethical_Constraints.md              — Embedded AI governance & anti-weaponization (Tier 1)
    ├── Auditor_Protocols.md                — Verification doctrine; 10-phase sequence (Tier 2)
    ├── Forge_Audit_Kit.md                  — Condensed routine multi-agent cycle reference (Tier 3)
    ├── Verification_Gates_LF.md            — Canonical 6 document promotion gates
    ├── File_Template.md                    — 10-section layout standard & Ethical Anchor field
    ├── Canonical_Terms.md                  — Anti-drift vocabulary & term exclusions
    ├── Engineer_Protocols.md               — Operational execution standards for engineers
    ├── Safety_Protocols.md                 — Physical operator safety; PPE, heat stress, hearing conservation
    ├── Security_Protocols.md               — Cryptographic trust & multi-agent node security
    ├── Repository_Integrity_Protocol.md    — Baseline enforcement & violation recovery
    ├── Repository_Structure.md             — Filename conventions, folder assignment doctrine
    ├── Ship_of_Theseus.md                  — Right-to-repair philosophical/legal defense
    ├── Trajectories.md                     — Multi-era version roadmap (v0 to interstellar)
    ├── Economics.md                        — Dynamic resource doctrine; market navigation; barter
    ├── Environmental_Constraints.md        — Site, regulatory, ecological, and jurisdictional boundary conditions; RDC baseline; No-Externalized-Entropy doctrine
    ├── Experiments.md                      — Physical grounding registry; falsification records; EXP-ID artifacts for PROVISIONAL→VERIFIED claim transitions
    ├── Nothingness Theorem                 — Philosophical substrate; foundational framework for salvage-first doctrine, distributed disagreement, and anti-entropy maintenance principles; functionless artifact filed in Admin
    ├── Computational Institutional Reasoning — Formal theoretical paper; axiomatic state-machine model of institutional epistemics; Unknown Conservation, Governance Stability, Epistemic Debt Instability, and Institutional Memory Dominance theorems; non-linear Verification Algebra specification
    ├── Governance_Migration_Protocol.md    — Tier 1 Axiom amendment procedures
    ├── PROBE_INVOCATION.md                 — Copy-paste cold-start template for Mission Drift Review (AP-030); not doctrine, an operational prompt
    └── AUDIT_HARNESS.py                    — Automated script supporting verification

Architecture/                               — System architecture and foundational logic
    ├── Arc_Scope_Map.md                     — Per-file scope/dependency index for this folder (2026-08-08)
    ├── Forge_flow.md                       — Master decision flow & REPOSITORY VOCABULARY STANDARD
    ├── Components.md                       — Critical vs useful component taxonomy
    ├── Facilities.md                       — Physical environment constraints; siting prerequisites
    ├── Geck_forge_seed.md                  — Minimum viable seed specification
    ├── Engineering.md                      — First-principles intellectual backbone
    ├── Precision.md                        — Precision ceiling doctrine; tolerance tiers; metrology
    ├── Mechanical_Structures.md            — Salvaged-frame kinematic and structural doctrine
    ├── Thermal_Systems.md                  — Thermodynamic laws, heat transfer, Peltier, TEG doctrine
    ├── Friction_Dynamics.md                — Fluid mechanics, aerodynamics, and tribology doctrine
    ├── Chemistry.md                        — Electrochemistry, corrosion, redox, polymer degradation
    ├── Cognitive_Frameworks.md             — Distributed cognition & survival under uncertainty
    └── Forge_Net.md                        — Decentralized data/physical network logistics

Operations/                                 — Physical modules and operational systems
    ├── Gate_01_Intake.md                   — Entry safety screening & provenance tagging
    ├── Gate_02_Triage.md                   — 5-station value preservation decision engine
    ├── Gate_03_Reduction.md                — Irreversible mechanical sizing (feedstock milling)
    ├── Gate_04_Separation_Mechanical.md    — Centrifugal stratification & fail-to-bin diversion
    ├── Gate_05_Separation_Thermal.md       — Core induction melting & gradient extraction
    ├── Gate_06_Fabrication.md              — Arc welding & mill-to-spec constructive ceiling
    ├── Gate_07_Utilization.md              — After-action loop & failure data capture
    ├── Electronics.md                      — Salvaged PCB harvesting & Logic-Zero firmware trust
    ├── Energy.md                           — Incremental power bootstrap & load profiles
    ├── Air_Scrubber.md                     — 5-stage negative-pressure containment subsystem
    ├── Plastics.md                         — Polymer triage & 3-stage pyrolysis framework
    └── Woodworking.md                      — Salvaged urban timber milling & drying schedules

Tests/                                      — Test frameworks and deployment platforms
    ├── Support_Raft.md                     — Stationary marine deployment anchor
    ├── Leviathan_testing.md                — Deep-ocean autonomous stress-testing
    ├── Living_Waters.md                    — Water purification pathways; site-conditioned selection; LW-001 through LW-010
    ├── Trophic_Forge.md                    — Biological cascade network; light → insect → fish → nutrient → crop → water; bootstrap sequence doctrine
    ├── Solar_Descent.md                    — Underground concentrated solar; SD-001 optical downlink; SD-002 fluid downlink; shared chamber reconvergence
    ├── Cognitive_Salvage_Layer.md          — Heuristic salvage pipeline; consensus-aggregated machinery wisdom; NOVEL/CANDIDATE_NOVEL promotion gate; GH-001 through GH-012
    ├── Hydrologic_Resource_Cascade.md      — Flood-driven sediment recovery basin; sequential hydraulic sorting zones; episodic operation doctrine; HR-UNK-001 through HR-UNK-002 (formal); HR-003 through HR-010 (research questions)
    ├── Chaos_Dynamics.md                   — Exploration/R&D pipeline doctrine; Sandbox (Level ≤4 hypothesis generation) → Promotion Gate → EXP-ID → physical testing → Engineering derating; resolution vehicle for EN-005; feeder for EN-001a
    └── Pyrolysis_Cascade.md                — Staged thermal cascade (pyrolysis → high-temp reduction) for pre-triaged salvage; explicitly dependency-gated on PL-001/CE-003 (halogen), GR-002 (reduction method), FA-001 (site), EN-001 (structural); PYC-001 through PYC-008
    └── Field_Logs.md                       — Append-only intake for physical test runs and cross-agent field data; not a specification, no Spec Gates apply

Challenges/                                 — Problem layer: why these capabilities exist
    ├── Water.md                            — Water scarcity and contamination (Living Waters)
    ├── Biofouling.md                       — Biological colonization and corrosion
    ├── Waste.md                            — Discretionary waste and repair capacity loss
    ├── Planned_Obsolescence.md             — Deliberate unrepairability and locked hardware
    ├── Critical_Minerals.md                — Rare earth and critical mineral supply chains
    ├── Emergence.md                        — Emergent intelligence: alignment-by-environment design
    ├── Energy_Scarcity.md                  — Energy poverty, grid fragility, and community energy sovereignty; ES-001 through ES-003
    ├── Return_To_Eden.md                   — Closed-loop material cycle framework; Eden Index (I_E); Tier I–IV progression doctrine
    └── Closed_Loop_Feedstock.md            — Persistence Yield (Y_p = FIR × PIR) telemetry model; recursive epistemic-ascent loop; salvage-to-feedstock closed-loop doctrine; CLF-001 through CLF-010

Archive/                                    — Prior states of governance-bearing documents
    ├── README.md                           — Archive scope and retention rationale
    └── Logs/                                — Split-out full changelogs (condensed current versions remain in the main files)
        ├── Unknowns_Changelog.md           — Full version history for Unknowns.md pre-v4.29
        ├── Governance_Charter_Changelog.md — Full version history for Governance_Charter.md
        ├── Forge_Audit_Kit_Changelog.md    — Full version history for Forge_Audit_Kit.md
        ├── AUDIT_HARNESS_CHANGELOG.md      — Full version history for AUDIT_HARNESS.py
        └── Auditor_Protocols_Logs.md       — Full version history + AP-series registration log
```

**Planned / not yet created:**
- `economics_v0.md` — superseded by `Admin/Economics.md` (created 2026-06-05)
- `Precision_LF.md` — superseded by `Architecture/Precision.md` (created 2026-06-05)
- `Admin/Safety_Protocols.md` — created 2026-06-05 ✓
- `Admin/Governance_Migration_Protocol.md` — created 2026-06-05 ✓
- `Admin/Autonomy_Divergence_Protocol.md` — created 2026-07-19, Draft/PROPOSED NOT RATIFIED ✓
- `Admin/Repository_Structure.md` — created 2026-06-05 ✓
- `Architecture/Facilities.md` — created 2026-06-05 ✓
- `Safety_Protocols.md` (noise/hearing conservation) — resolved by `Admin/Safety_Protocols.md` ✓
- `Tests/Chaos_Dynamics.md` — created 2026-07-04 ✓ (see Tests/ structure tree and Scope Map below); supersedes EN-005's original never-created candidate names (`Tests/Verification_Methods.md`, `Admin/Test_Protocols.md`).
- `Challenges/Closed_Loop_Feedstock.md` — created 2026-07-06 ✓ (see Challenges/ structure tree and Scope Map below).
- `Tests/Pyrolysis_Cascade.md` — created 2026-08-04 ✓ (see Tests/ structure tree and Scope Map above); drafted from archived conversation via Copilot, distilled and quantitative claims retired to Placeholder by Grok, PC-/PYC- namespace collision fixed before merge.
- `Tests/Field_Logs.md` — created 2026-08-06 ✓, append-only intake for physical test runs and cross-agent field data, cross-referenced from `CONTRIBUTING.md`; not a specification file, no Spec Gates or Unknowns of its own.
- `Admin/Adm_Scope_Map.md` — created 2026-08-07 ✓, renamed with the folder-abbreviation-prefix convention (confirmed pushed to main by James); pilot for a per-folder scope/dependency index (Purpose/Does/Does-Not per file, verified against each file's own Scope Boundary section); surfaced two files with no Scope Boundary section at all (`Computational_Institutional_Reasoning.md`, `Nothingness_Theorem.md`) and one apparent duplicate unknown that checked out as already correctly cross-linked (ENV-003/EC-010).
- `Architecture/Arc_Scope_Map.md` — created 2026-08-08 ✓, second folder in the rollout, same method; found one concrete stale cross-reference (`Forge_flow.md`'s UNK-008 claim, wrong since 2026-07-19) and one softer asymmetric-documentation gap (Forge_flow.md/Canonical_Terms.md vocabulary authority). Unlike Admin/, no files here lack a Scope Boundary section. Pending: whether to roll the same pattern out to the remaining four folders (Operations/, Challenges/, Tests/, Automation/), and whether to fix the `Forge_flow.md` UNK-008 stale reference this pass surfaced.
- `Architecture/Characterization.md` — **[PLANNED]**, referenced as a forward dependency by `Closed_Loop_Feedstock.md`; not yet created.
- `Operations/Metals.md` — **[PLANNED]**, referenced as a forward dependency by `Closed_Loop_Feedstock.md`; not yet created.

**Routing.md completeness:** Verified complete as of 2026-08-04 (`Tests/Pyrolysis_Cascade.md` added, same date as file creation). Prior verification 2026-06-28 (`Tests/Cognitive_Salvage_Layer.md`, `Tests/Hydrologic_Resource_Cascade.md`, and `Admin/Computational_Institutional_Reasoning.md` added). Any gaps found on future audit passes are tracked as PC cluster entries in `Unknowns.md`.

> ⚠️ **Correction, 2026-07-04:** The above completeness check missed `Challenges/Return_To_Eden.md`, which was already present in `Routing.md`'s master table and in `Unknowns.md`'s active index (RE-UNK-001 through RE-UNK-005, registered cycle 11) but absent from this file's structure tree, Maturity Snapshot, and Scope Map. Added in this pass — see entries below. This file's own "verified complete" claims should be read as bounded by what was checked at the time, not as a standing guarantee; this gap sat unnoticed since the RE-UNK cluster's registration.

> ⚠️ **Correction, 2026-07-06:** `Challenges/Closed_Loop_Feedstock.md` had the same gap RE-UNK-001/RE-UNK-005 exposed above — present in `Routing.md` (as of that file's 2026-07-04/06 rows) and in `Unknowns.md`'s active index (CLF-001 through CLF-010, v4.12) but absent from this file's structure tree, Maturity Snapshot, and Scope Map until this pass. Added below. See `Unknowns.md` PC-005 for this file's own remaining registration debt (Routing.md backlink confirmation, `Automation/AUDIT_HARNESS.py` static registry entry).

> ⚠️ **Correction, 2026-07-28:** Full refresh pass — this file had drifted in multiple ways simultaneously, none caught until checked directly against source. `Admin/PROBE_INVOCATION.md` (created 2026-07-26) was entirely absent from the structure tree, Maturity Snapshot, and Scope Map. `Archive/`'s tree entry still showed the pre-v0.99.27 placeholder note despite `Archive/Logs/` holding five real changelog files since that restructuring. Three Maturity Snapshot rows were stale against their own files' current File State tables (`Admin/Forge_Audit_Kit.md` showed "Active" / no Spec Gates, actually Draft / 0/6; `Architecture/Cognitive_Frameworks.md` showed no Spec Gates value, actually 0/6; `Admin/Computational_Institutional_Reasoning.md` showed a placeholder "Compiled — Theoretical paper" description dating from before the file had any sidecar tracking at all). Pending Corrections table showed PC-001, PC-002, PC-003, and PC-005 as still open; all five (with PC-004) are Resolved in `Unknowns.md`. The Cross-Module Unknowns table itself was seventeen `Unknowns.md` version bumps stale (last refreshed at v4.12); one entry (CT-007) had actually regressed from Open back through an incorrect "Resolved" label before `Unknowns.md`'s own text corrected itself — this file hadn't caught either the error or the correction. Every ID in the refreshed table below was individually re-checked against the current Active Index rather than carried forward. This file's own "verified complete" and "refreshed" claims should continue to be read as bounded by what was checked at the time, per the standing caveat two corrections above.

> ⚠️ **Correction, 2026-08-06: full Maturity Snapshot re-verification, all 66 rows checked directly against each file's own current File State block for the first time since this file's creation.** Prior passes fixed individual rows as they were noticed; this pass programmatically extracted Status/Spec Gates/Highest Risk from every listed file and diffed against this table cell by cell. Result: **34 of 66 rows had at least one stale field** — roughly half the table. Notable findings: `Admin/Governance_Charter.md` showed Spec Gates 1/6 when the file has been at 6/6 since GOV-011 resolved 2026-07-05 (a month stale on the single most load-bearing file in the repository); `Admin/Auditor_Protocols.md` showed Status "Active" when the file's own File State says "Draft"; `Challenges/Emergence.md` showed Spec Gates "0/6" and Highest Risk "High" when the file — correctly, as a Problem-Statement subtype — has neither field at all, meaning those values were never real; `Admin/Forge_Audit_Kit.md` showed a Highest Risk of "Low" that doesn't exist anywhere in the file's own File State block. The six Active Problem-Statement Challenges files (Water, Biofouling, Waste, Planned_Obsolescence, Critical_Minerals, Energy_Scarcity) were re-checked and confirmed genuinely correct as-is — Problem-Statement subtype files don't carry Spec Gates/Highest Risk by design, this isn't an omission. Full corrected table below; every cell now traces to a specific line in its source file's own File State block, not to a prior pass's memory of that file. This does not mean the table is now permanently synchronized — same caveat as every prior correction: accurate as of what was checked today, not a standing guarantee.

---

Canonical record of filename changes. Stale references should be resolved using this table.

| Old Name | New Name | Location | Date |
|---|---|---|---|
| Spin_Chamber_v0.md | Gate_05_Separation_Thermal.md | Operations/ | 2026-05-15 |
| Material_Separation_Gate_v0.md | Gate_04_Separation_Mechanical.md | Operations/ | 2026-05-15 |
| Stratification_Chamber_v0.md | Gate_04_Separation_Mechanical.md | Operations/ | Prior cycle |
| Lazarus_forge_v0_flow.md | Forge_flow.md | Architecture/ | 2026-05-15 |
| Unknowns_LF.md | Unknowns.md | Root | 2026-05-15 |
| Trajectories_LF.md | Trajectories.md | Admin/ | 2026-05-15 |
| Component_Triage_System.md | Gate_02_Triage.md | Operations/ | 2026-05-15 |
| geck_forge_seed.md | Geck_forge_seed.md | Architecture/ | 2026-05-15 |
| energy_v0.md | Energy.md | Operations/ | 2026-05-15 |
| Air_Scrubber_v0.md | Air_Scrubber.md | Operations/ | 2026-05-15 |
| Support_Raft_v0.md | Support_Raft.md | Tests/ | 2026-05-15 |
| leviathan_testing.md | Leviathan_testing.md | Tests/ | 2026-05-15 |
| Ship_of_Theseus_Right_to_Repair.md | Ship_of_Theseus.md | Admin/ | 2026-05-15 |
| Electronics.md (root) | Electronics.md | Operations/ | 2026-05-20 |
| Canonical_Terms_LF.md | Canonical_Terms.md | Admin/ | 2026-05-26 |
| Engineering.md (replaced by) | Mechanical_Structures.md | Architecture/ | 2026-05-31 |
| economics_v0.md | Economics.md | Admin/ | 2026-06-05 |
| Precision_LF.md | Precision.md | Architecture/ | 2026-06-05 |
| Forge_flow.md | Forge_flow.md | Architecture/ | Resolved — RS-002 2026-06-11 |

*See `Unknowns.md` CT-007 (Resolved 2026-07-06) and Closed_Loop_Feedstock.md's own Resolution Log for a related but distinct ID-namespace rename history — `EC-` → `ECN-` (Economics.md) and `CF-` → `FL-` → `CLF-` (Closed_Loop_Feedstock.md) — not filename renames, so not tracked in this table, but the same class of drift risk.*

---

## Pending Corrections

Pending corrections have been migrated to `Unknowns.md` PC cluster (PC-001 through PC-005).
Discovery.md is a navigation map — task tracking belongs in Unknowns.md.

| ID | Summary | See |
|----|---------|-----|
| ~~PC-001~~ | ~~Verification Ref corrections — 10 files pointing to Forge_Audit_Kit.md~~ | Resolved — all 10 files corrected |
| ~~PC-002~~ | ~~Upstream reference corrections — 7 files missing Facilities.md link~~ | Resolved — all 7 files corrected |
| ~~PC-003~~ | ~~New file cross-reference corrections — 10 files missing 2026-06-06 file references~~ | Resolved — all 10 files corrected |
| ~~PC-004~~ | ~~Stale name corrections — Challenges/Water.md and Planned_Obsolescence.md~~ | Resolved 2026-06-11 — retrofit pass applied corrections |
| ~~PC-005~~ | ~~`Challenges/Closed_Loop_Feedstock.md` not registered in `Routing.md`, this file, or `Automation/AUDIT_HARNESS.py`~~ | Resolved 2026-07-19 — independently re-verified against source in all three locations |

---

## Repository Maturity Snapshot

| File | Status | Spec Gates | Highest Risk |
|------|--------|-----------|--------------|
| `Admin/Governance_Charter.md` | Draft | 6/6 vs. `Admin/Verification_Gates_LF.md` — execution quality (see GOV-011, resolved 2026-07-05); promotion separately blocked by open unknowns (GOV-003, GOV-005) and Enforcement Checkpoint 2 — Bootstrap Paradox | Critical (GOV-013, GOV-015, GOV-018 — see `Archive/Logs/Governance_Charter_Changelog.md`; promotion-blocking risk unchanged from GOV-003/GOV-005) |
| `Admin/Ethical_Constraints.md` | Exploration | 0/6 | High |
| `Admin/Auditor_Protocols.md` | Draft | 4/6 (G1, G3, G4, G6 clear — G3 cleared 2026-08-03 via AP-017 Resolved; G5 conditional on cross-ref fixes below; G2 N/A — no physical/quantitative claims of its own) | High |
| `Admin/Forge_Audit_Kit.md` | Draft | 0/6 | — |
| `Admin/Verification_Gates_LF.md` | Draft | 2/6 | High |
| `Admin/File_Template.md` | Exploration / Draft / Specification | 0/6 | Low / Medium / High |
| `Admin/Canonical_Terms.md` | Draft | 0/6 | Low |
| `Admin/Engineer_Protocols.md` | Draft | 2/6 | High |
| `Admin/Safety_Protocols.md` | Exploration | 0/6 | High |
| `Admin/Security_Protocols.md` | Draft | 0/6 | High |
| `Admin/Repository_Integrity_Protocol.md` | Draft | 2/6 | High |
| `Admin/Repository_Structure.md` | Exploration | 0/6 | Low |
| `Admin/Ship_of_Theseus.md` | Exploration | 0/6 | Medium |
| `Admin/Trajectories.md` | Exploration | 1/6 | Medium |
| `Admin/Economics.md` | Exploration | 0/6 | Medium |
| `Admin/Environmental_Constraints.md` | Draft | 1/6 (G1 cleared — fallacy checklist applied at creation; G3/G5 fixes applied 2026-07-06, pending re-audit confirmation) | High |
| `Admin/Experiments.md` | Draft | 0/6 | Low |
| `Admin/Nothingness_Theorem.md` | Tier 0 — Philosophical Substrate (functionless by doctrine; not subject to operational promotion gates) | N/A — Tier 0 exempt | N/A — Tier 0 documents are audited for internal consistency only |
| `Admin/Computational_Institutional_Reasoning.md` | Exploration | G4 cleared; G1 partial (Gemini 2026-06-30); G3 blocked by AP-012/AP-016 | CIR-001 — Physical Grounding Telemetry Mapping Interface undefined; \u03b31\u2013\u03b34 predicates currently aspirational in harness implementation (see Section 7.4). Renamed 2026-07-28 from local "GOV-008" — collided with `Admin/Governance_Charter.md`'s registered GOV-008 (minimum agent quorum); CIR-scoped prefix now registered in `Admin/Forge_Audit_Kit.md`'s Governance Sidecar ID Reference. |
| `Admin/CIR_Gov.md` | **Proposed — Not Ratified** | 0/6 | High — while unratified and GOV-008 remains Open, the misreading risk (treating this as operational) is real, not theoretical; raised from Medium 2026-07-31 per Skeptic/Auditor review. See §Binding Status below. |
| `Admin/Governance_Migration_Protocol.md` | Exploration | 0/6 | High |
| `Admin/Autonomy_Divergence_Protocol.md` | Draft — PROPOSED NOT RATIFIED | 0/6 (drafted, not yet audited) | High (governs response to AI governance/objective divergence) |
| `Admin/PROBE_INVOCATION.md` | Draft | N/A — operational prompt template, not a doctrine or specification claim | — |
| `Automation/AUDIT_HARNESS.py` | Active | — | — |
| `Architecture/Forge_flow.md` | Exploration | 0/6 | Medium |
| `Architecture/Components.md` | Exploration | 0/6 | Low |
| `Architecture/Facilities.md` | Exploration | 0/6 | High |
| `Architecture/Geck_forge_seed.md` | Exploration | 0/6 | Medium |
| `Architecture/Engineering.md` | Draft | 3/6 | High |
| `Architecture/Precision.md` | Exploration | 0/6 | High |
| `Architecture/Mechanical_Structures.md` | Draft | 2/6 | High |
| `Architecture/Thermal_Systems.md` | Draft | 1/6 | High |
| `Architecture/Friction_Dynamics.md` | Draft | 2/6 | Medium |
| `Architecture/Chemistry.md` | Draft | 1/6 | High |
| `Architecture/Cognitive_Frameworks.md` | Exploration | 0/6 | High |
| `Architecture/Forge_Net.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_01_Intake.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_02_Triage.md` | Draft | 2/6 | High |
| `Operations/Gate_03_Reduction.md` | Exploration | 0/6 | High |
| `Operations/Gate_04_Separation_Mechanical.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_05_Separation_Thermal.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_06_Fabrication.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_07_Utilization.md` | Exploration | 0/6 | Low |
| `Operations/Electronics.md` | Exploration | 0/6 | High |
| `Operations/Energy.md` | Draft | 1/6 | High |
| `Operations/Air_Scrubber.md` | Draft | 3/6 | High |
| `Operations/Plastics.md` | Exploration | 0/6 | High |
| `Operations/Woodworking.md` | Draft | 0/6 | High |
| `Tests/Support_Raft.md` | Exploration | 0/6 | High — SR-001 (galvanic corrosion) is Open/High and required before v1.0; a hull that corrodes faster than modeled threatens the whole anchor-node concept |
| `Tests/Leviathan_testing.md` | Exploration | 0/6 | High |
| `Tests/Living_Waters.md` | Exploration | 0/6 | Critical — LW-UNK-001 (volatile co-distillation) and LW-UNK-003 (lumen implosion) both carry immediate safety consequences if bypassed |
| `Tests/Trophic_Forge.md` | Exploration | 0/6 | High |
| `Tests/Solar_Descent.md` | Exploration | 0/6 | High |
| `Tests/Cognitive_Salvage_Layer.md` | Exploration | 1/6 | High |
| `Tests/Hydrologic_Resource_Cascade.md` | Exploration | 0/6 | High |
| `Tests/Chaos_Dynamics.md` | Exploration | 0/6 | Medium — gatekeeps the evidentiary pipeline feeding EN-001/EN-001a; misuse risk if sandbox output is cited past its Level ≤4 ceiling |
| `Tests/Pyrolysis_Cascade.md` | Draft — Exploration | 0/6 (not yet audited) | High (thermal processing of mixed salvage; halogen & hazardous-fraction exposure) |
| `Challenges/Water.md` | Active | — | — |
| `Challenges/Biofouling.md` | Active | — | — |
| `Challenges/Waste.md` | Active | — | — |
| `Challenges/Planned_Obsolescence.md` | Active | — | — |
| `Challenges/Critical_Minerals.md` | Active | — | — |
| `Challenges/Energy_Scarcity.md` | Active | — | — |
| `Challenges/Emergence.md` | Exploration | — | — |
| `Challenges/Return_To_Eden.md` | Exploration | None cleared (G1–G2 conditional, G4–G6 cleared per 2026-06-30 audit — see Last Audit) | RE-UNK-001 — Eden Index variables lack defined measurement protocols; index is formally specified but not yet operationally measurable. RE-UNK-005 is a direct dependency. |
| `Challenges/Closed_Loop_Feedstock.md` | Exploration | 0/6 | Silent contamination cascades or toolhead destruction (CLF-003/CLF-006). |


## Scope Map — Root Files

### `Routing.md`
Programmatic lookup table. Raw content URLs and repository URLs for every file. Dual-audience: LLM context loading (raw) and human review (repo). Backlink anchor standard for all files.
**Upstream:** None — updated whenever files are added or renamed.
**Downstream:** All automated agents and CI systems; all files (backlink requirement).
> ℹ️ *Maintained separately from Discovery.md. Routing.md owns where; Discovery.md owns what and why.*

### `Unknowns.md`
Cross-module unknowns global index. Lean index only — full unknown entries live in file sidecars.
**Upstream:** All repository files (sidecar unknowns feed index).
**Downstream:** All audit contributors; Forge_Audit_Kit.md.

---

## Scope Map — Admin/

> Governance tier hierarchy: Tier 1 (Governance_Charter + Ethical_Constraints) →
> Tier 2 (Auditor_Protocols) → Tier 3 (Forge_Audit_Kit) →
> Support layer (all others).

### `Admin/Governance_Charter.md`
Constitutional root. Tier 1 Axioms (P-1–P-4, Q-1–Q-4); governance hierarchy; amendment doctrine.
**Upstream:** None.
**Downstream:** All repository files; Auditor_Protocols.md; Security_Protocols.md; Governance_Migration_Protocol.md.
⚠️ GOV-003 (integrity enforcement), GOV-005 (constitutional stability) — Critical.

### `Admin/Ethical_Constraints.md`
Co-Tier 1 control substrate. Anti-Weaponization Doctrine; Life Preservation; Pacifist Operating Posture.
**Upstream:** None.
**Downstream:** All repository files (Ethical Anchor field); Governance_Charter.md.
⚠️ EC-001 (confidence threshold), EC-002 (Anti-Weaponization pattern-matching), EC-003 (human escalation path) — all open.

### `Admin/Auditor_Protocols.md`
Tier 2 verification doctrine. 10-phase audit sequence; Fallacy Checklist; Sidecar Model; adversarial audit layer.
**Upstream:** Governance_Charter.md; Ethical_Constraints.md.
**Downstream:** Forge_Audit_Kit.md; Verification_Gates_LF.md; all repository files.
⚠️ AP-004 (cross-auditor disagreement resolution) — open. AP-012 and AP-016 (Critical) — Gate 3 blocked pending Provisional Spec.

### `Admin/Forge_Audit_Kit.md`
Tier 3 condensed audit reference. Derived from Auditor_Protocols.md. Load instead of full governance corpus to stay within token limits.
**Upstream:** Auditor_Protocols.md; Verification_Gates_LF.md.
**Downstream:** All audit contributors as operational reference.

### `Admin/Verification_Gates_LF.md`
Single canonical source for the six promotion gates (G1–G6).
**Upstream:** Auditor_Protocols.md; Governance_Charter.md.
**Downstream:** All repository files (Verification Ref field); Forge_Audit_Kit.md; Security_Protocols.md.
⚠️ VG-001 (synchronization authority chain) — blocks Specification promotion.

### `Admin/File_Template.md`
Standard file structure. Ten-section layout; Ethical Anchor field definition.
**Upstream:** Governance_Charter.md; Ethical_Constraints.md.
**Downstream:** All repository files.

### `Admin/Canonical_Terms.md`
Single source of truth for repository vocabulary. Anti-drift guardrails; banned terms.
**Upstream:** Governance_Charter.md; Forge_flow.md (gate logic terms authoritative there).
**Downstream:** All repository files; Auditor_Protocols.md; Security_Protocols.md.
⚠️ CT-002 (Component Library Schema) — blocks Gate_02_Triage.md promotion.

### `Admin/Engineer_Protocols.md`
Cognitive and procedural protocols for engineering contributors.
**Upstream:** Auditor_Protocols.md; Ethical_Constraints.md; Discovery.md.
**Downstream:** All engineering contributors; all Operations/ and Architecture/ domain files.
⚠️ EP-004 (engineering authority boundary), EP-005 (acceptable risk threshold — cross-reference Safety_Protocols.md) — open.

### `Admin/Safety_Protocols.md`
Physical operator safety doctrine. PPE by hazard class; hearing conservation; heat stress; acceptable risk threshold (resolves EP-005); incident reporting.
**Upstream:** Ethical_Constraints.md; Engineer_Protocols.md; Facilities.md (FA-004).
**Downstream:** All Operations/ gate files; Air_Scrubber.md (noise reference).
⚠️ SP-006 (emergency response procedures) — deferred to FA-001 resolution.

### `Admin/Security_Protocols.md`
Cryptographic enforcement layer. Multi-signature override verification; node identity; key rotation.
**Upstream:** Governance_Charter.md; Repository_Integrity_Protocol.md; Canonical_Terms.md; Electronics.md.
**Downstream:** Repository_Integrity_Protocol.md; Governance_Charter.md (GOV-006 resolution); all governance files.
⚠️ SEC-001 (quorum under partition), SEC-007 (external root-of-trust) — Critical.

### `Admin/Repository_Integrity_Protocol.md`
Operational integrity enforcement. Violation classification ladder; recovery procedures; automation migration path.
**Upstream:** Governance_Charter.md; Auditor_Protocols.md; Ethical_Constraints.md.
**Downstream:** Forge_Audit_Kit.md; AUDIT_HARNESS.py; Security_Protocols.md; Unknowns.md; Discovery.md.
⚠️ RIP-001 — **Resolved** 2026-06-28 (Discharge via Lessons Learned; Git release tags satisfy prior-state archival at v0 scale). RIP-006 (archive retention policy) — In Progress; GitHub indefinite retention satisfies Tier 1 requirement, /Archive/ content policy pending distillate architecture.

### `Admin/Repository_Structure.md`
Filename conventions; folder assignment doctrine; Archive/ directory doctrine; naming standard.
**Upstream:** Governance_Charter.md; File_Template.md.
**Downstream:** All repository files; Discovery.md (Rename Registry forward doctrine).
⚠️ RS-001 (non-markdown file type introduction procedure) — open; relevant given Nothingness Theorem and Computational Institutional Reasoning are filed without extensions.

### `Admin/Ship_of_Theseus.md`
Philosophical and legal defense for repair-first doctrine. Right-to-repair framework.
**Upstream:** Gate_02_Triage.md; Components.md.
**Downstream:** Gate_02_Triage.md; Geck_forge_seed.md.
⚠️ ST-004 (sub-threshold state tampering vulnerability in Derivative Identity threshold) — High risk, open.

### `Admin/Trajectories.md`
Version trajectory v0–v5. FRT doctrine and floor value. Scope routing for out-of-version capabilities.
**Upstream:** Governance_Charter.md; Energy.md; Geck_forge_seed.md.
**Downstream:** All operational and architecture files; Gate_07_Utilization.md; Economics.md.
⚠️ TR-001 (v1 profitability baseline) — blocks v0→v1 transition; Economics.md provides resolution framework.

### `Admin/Economics.md`
Dynamic resource doctrine. Buy what you need, sell what you don't. Barter doctrine (canonical owner). Market navigation framework. v1 profitability baseline framework (TR-001 resolution path).
**Upstream:** Trajectories.md (FRT doctrine); Gate_07_Utilization.md (cycle data); Energy.md (EV-001 cost input).
**Downstream:** Gate_07_Utilization.md (FRT accounting); Gate_06_Fabrication.md (input cost threshold).
⚠️ ECN-002 (operating cost baseline) — blocks TR-001 closure; dependent on Energy.md EV-001. *ID prefix renamed EC-→ECN- 2026-07-06 (`Unknowns.md` CT-007, Resolved).*

### `Admin/Environmental_Constraints.md`
Site, regulatory, ecological, and jurisdictional boundary conditions. Four constraint categories: Climatic/Physical, Regulatory/Jurisdictional, Ecological/Resource, Human/Social. Junction file for EC-010 (jurisdiction conflict) and GOV-010 (regulatory compliance friction) convergence. No-externalized-entropy doctrine. Graceful degradation rules tied to environmental conditions.
**Upstream:** Governance_Charter.md (Tier 1 Axioms P-1, P-3); Ethical_Constraints.md (Compliance-Maximizing Default — see ENV-DS-001); Facilities.md (Site Initialization Checklist); Safety_Protocols.md.
**Downstream:** Ethical_Constraints.md (EC-010 resolution); Governance_Charter.md (GOV-010 resolution); Facilities.md (FA-003); Safety_Protocols.md (SP-005); Challenges/Waste.md; Challenges/Water.md; Challenges/Biofouling.md; Tests/Leviathan_testing.md; Tests/Trophic_Forge.md.
⚠️ ENV-009 (no site assessed against constraints) — Critical; all values Placeholder until first site assessment. ENV-007/ENV-008 — Resolved/Partially Addressed 2026-07-06. ENV-010 (Facilities.md checklist reciprocity unverified) — new. **ENV-DS-001** (`Unknowns.md` Active Disputes) — this file's Bootstrap operating doctrine found structurally incompatible with `Admin/Ethical_Constraints.md`'s Compliance-Maximizing Default; reconciled text drafted in-file, pending human governing authority ratification.

### `Admin/Experiments.md`
Physical grounding registry. Structured falsification records that ground PROVISIONAL claims in physical reality. Each entry (EXP-ID) targets a specific unknown or PROVISIONAL claim, defines hypothesis and pass/fail criteria, and records outcome. Completed entries produce EXP-ID grounding artifacts that feed Epistemic Ledger entries in owning file sidecars. Partial resolution path for AP-010 (physical test harness coupling). Priority candidates for first entries: CF-001 (hardware watchdog), EN-001 (salvaged material safety factors), CE-003 (field polymer identification).
**Upstream:** Auditor_Protocols.md (EF-0.3 Epistemic Ledger; EF-0.8b Physical Grounding Vector; AP-010); Unknowns.md (target unknowns); Tests/ files (physical test infrastructure).
**Downstream:** All owning file sidecars (Epistemic Ledger entries); Unknowns.md (unknown status updates on experimental closure).
⚠️ No entries yet — stub only. Absence of entries does not indicate grounding has occurred.

### `Admin/Nothingness_Theorem.md`
Philosophical substrate document. Functionless artifact filed in Admin — intentionally has no operational role in the governance system. Documents the philosophical framework from which several Forge operating principles derive: salvage-first doctrine (waste is not zero), multi-agent audit architecture (distributed disagreement as error correction, Axiom A-7), anti-sacralization principle (drift as active deformation, Axiom A-8), and maintenance-as-creation equivalence (Axiom A-5). Four-generation compiled document produced via inter-agent friction protocol. Contains 8 Axioms, 9 open unknowns (NT-001 through NT-009), and a self-referential proof relevant to EF-0.0's treatment of UNKNOWN states.
**Upstream:** None — foundational.
**Downstream:** Philosophical influence on Governance_Charter.md, Auditor_Protocols.md, README.md. No operational dependency — this file may be removed without breaking any functional system.

### `Admin/Computational_Institutional_Reasoning.md`
Formal theoretical paper. Treats the multi-agent collective as a discrete-time deterministic epistemic state machine operating over a persistent Institutional Knowledge Graph. Establishes Part 0 axioms (Persistent Reality, Representational Incompleteness, Explicit Epistemic Accounting / the Nothingness Principle, Institutional Continuity, Governance Precedes Mutation) and derives four core theorems: Unknown Conservation (proves a nonzero unknown floor is mathematically unavoidable — direct formal backing for the Unknown Budget rule in Unknowns.md Size Management Rules); Governance Stability (inductive safety guarantee under constitutional gating); Epistemic Debt Instability (non-linear acceleration of systemic risk when generation outpaces verification — formal backing for CF-004 and the Triage Posture doctrine in Cognitive_Frameworks.md); and Institutional Memory Dominance (information-theoretic case for complete provenance retention — formal backing for RIP-001's resolution rationale and AP-006's provenance ceiling). Section 4 specifies the non-linear Verification Algebra (five-dimensional verification state vector E/R/C/P/S; Physical Grounding Gate; Provenance Ceiling Gate; Adversarial Multiplier) underlying AP-006's provenance labels and the UNKNOWN/PROVISIONAL/VERIFIED classification system referenced throughout Auditor_Protocols.md. Section 7 documents a production mapping onto the file-based repository runtime and reports simulated empirical validation of the Automated Triage Posture Trigger.
**Upstream:** None — foundational; references Ship of Theseus framing from Admin/Ship_of_Theseus.md as an analogy only (Axiom A4), not a structural dependency.
**Downstream:** Formal backing for Admin/Auditor_Protocols.md (EF-0.0, EF-0.8b, AP-006 provenance ceiling, AP-001 retrospective calibration); Architecture/Cognitive_Frameworks.md (CF-004 epistemic debt measurement, Triage Posture doctrine); Unknowns.md (Unknown Budget rule, Size Management Rules rationale); Automation/AUDIT_HARNESS.py (constitutional predicate compiler design target — γ1 through γ4 rule semantics). No operational dependency — repository functions without this file being read, but several doctrine files assert claims this paper is the proof source for.
⚠️ **Corrected 2026-07-28:** this file is not exempt from sidecar tracking — that framing was accurate when CIR was purely theoretical but is now stale. Active Trackers: CIR-001 (Physical Grounding Telemetry Mapping Interface, renamed this session from a colliding local "GOV-008" — see `Admin/Forge_Audit_Kit.md`'s Governance Sidecar ID Reference for the registered `CIR-` prefix), AP-012, AP-016, CF-002, CF-004. If repository practice diverges from a theorem or axiom stated here, still log per the Repository Role divergence-logging rule.

### `Admin/CIR_Gov.md`
Candidate epistemic governance kernel — "CIR v2.0." Distinct from `Admin/Computational_Institutional_Reasoning.md` (the formal theoretical paper above): this file is a proposed *operational* runtime specification — predicate-gated state transitions (`Γ`), typed unknowns with debt accounting, provenance ceilings, and a deterministic triage posture — drafted 2026-07-31, filed **Proposed — Not Ratified**. Its central claim (agent-independent state transitions, Principle 7 / Axiom A4) structurally depends on GOV-008 (minimum agent/hardware quorum, `Governance_Charter.md`), which remains Open with no concrete specification and no ratified quorum. The file's own Binding Status section states plainly that running this kernel today would not implement Q-2 Separation of Powers — it would reproduce the Bootstrap Paradox under the appearance of predicate rigor. Preserved in full specifically so the architecture isn't lost, per explicit human direction, while sequencing recommends GOV-008 be drafted and ratified first, independently of this file.
**Upstream:** None — draws a single minimal axiom (A6, non-zero representational floor) from `Admin/Nothingness_Theorem.md`'s Core Theorem, explicitly not a full merge.
**Downstream:** None currently — no harness, evaluator, or automation implements any part of this file. Intended eventual downstream: a future multi-agent audit harness, once GOV-008 exists.
⚠️ Do not cite this file as evidence of current Q-2 compliance, Checkpoint 2 clearance, or Genesis Phase exit. It is a specification, not a running system.

### `Admin/Governance_Migration_Protocol.md`
Tier 1 Axiom amendment procedures. Two-track migration system. Engineer proposal; human ratification. Hard floor doctrine.
**Upstream:** Governance_Charter.md; Auditor_Protocols.md; Engineer_Protocols.md.
**Downstream:** All governance files (Track A); Governance_Charter.md (Track B amendment target).
⚠️ GMP-004 (ratification authentication) — mirrors GOV-006; SEC-007 resolution path.

### `Admin/Autonomy_Divergence_Protocol.md`
Autonomy Divergence Protocol — how governance responds when a subsystem's behavior appears to diverge from authorized objectives or constraints. Detection → Classification (Capability Anomaly vs. Governance Concern) → graduated Response Tiers (Watch → Immediate → Human-Reviewed) → Restoration. Candidate GOV-021; explicitly rejects any "exit from human oversight" framing — cooperation as the stable indefinite default, not divergence with a cutoff point.
**Upstream:** Ethical_Constraints.md; Auditor_Protocols.md (AP-008 enforcement gap, AP-012 human-unavailability doctrine, AP-016 concurrent-quarantine doctrine); Governance_Migration_Protocol.md (Track A routing).
**Downstream:** Governance_Charter.md (pending GOV-021 registration).
⚠️ Status: Draft, PROPOSED NOT RATIFIED, Spec Gates 0/6, not yet formally audited. Two open sub-unknowns: GOV-021b (Detection Criteria calibration) and GOV-021c (multi-agent coordinated divergence detection).

### `Admin/PROBE_INVOCATION.md`
Operational prompt template, not doctrine. The exact copy-paste block an operator pastes into a fresh, cold-start thread to run one Mission Drift Review cycle — canonical input file list and required output structure only. Design rationale, trigger cadence, and escalation rules live in Auditor_Protocols.md §Mission Drift Review; this file defers to that source on any conflict.
**Upstream:** Admin/Auditor_Protocols.md §Mission Drift Review (this file is derived from it, not independent doctrine).
**Downstream:** None — invoked manually by a human operator when AP-030's trigger condition fires (5 ratified governance/canonical changes since the last cycle, or 60 days elapsed).
⚠️ Open Unknowns: 0 at this file's own level — tracked at Admin/Auditor_Protocols.md AP-030 (mechanism-level: as of 2026-07-28, zero probe cycles have actually run since AP-030's registration).

---

## Scope Map — Architecture/

> **Vocabulary authority:** `Architecture/Forge_flow.md` is the operational
> vocabulary standard. For any undefined operational term, consult
> `Architecture/Forge_flow.md` §Defined Terms before `Admin/Canonical_Terms.md`.

> **Architecture reading order:**
> 1. `Forge_flow.md` — vocabulary and gate logic
> 2. `Components.md` — what must exist
> 3. `Facilities.md` — where it exists
> 4. `Geck_forge_seed.md` — how to seed it
> 5. `Engineering.md` — foundational principles
> 6. `Precision.md` — what the Forge can build to
> 7. `Mechanical_Structures.md` — fabrication machinery doctrine
> 8. `Thermal_Systems.md` — heat transfer and thermodynamics
> 9. `Friction_Dynamics.md` — fluid mechanics and tribology
> 10. `Chemistry.md` — electrochemistry and material chemistry
> 11. `Cognitive_Frameworks.md` — how it thinks
> 12. `Forge_Net.md` — how instances connect

### `Architecture/Forge_flow.md`
Master decision flow AND repository vocabulary standard. v0 gate logic; outcome paths; want/need policy; primary KPI.
**Upstream:** Canonical_Terms.md; Ethical_Constraints.md; Components.md.
**Downstream:** All repository files (Defined Terms); all Operations/ gate files; Forge_Net.md; Canonical_Terms.md.
⚠️ FL-001 (gate logic determinism at boundary cases) — blocks Specification promotion.

### `Architecture/Components.md`
Minimum component architecture. Critical/Useful/Bootstrap taxonomy; Bootstrap Doctrine; Graduation Rule.
**Upstream:** Forge_flow.md; Geck_forge_seed.md; Ethical_Constraints.md.
**Downstream:** Geck_forge_seed.md; Gate_02_Triage.md; all Operations/ gate files.
⚠️ CO-002 (metrology precision thresholds) — route to Precision.md PR-001.

### `Architecture/Facilities.md`
Minimum physical environment constraints. Nonburnable flooring prerequisite; airflow topology; triangle workstation principle; hazard zone separation; floor loading; utility access.
**Upstream:** Components.md; Engineering.md; Ethical_Constraints.md.
**Downstream:** All Operations/ gate files (siting prerequisite); Safety_Protocols.md (FA-004 heat stress); `Admin/Environmental_Constraints.md` (ENV-010 — checklist reciprocity unverified).
⚠️ FA-001 (site not confirmed) — Critical; blocks all hot operations.

### `Architecture/Geck_forge_seed.md`
Minimum viable seed specification. 8 core G.E.C.K. modules; procurement doctrine; marine variant.
**Upstream:** Components.md; Forge_flow.md; Ethical_Constraints.md.
**Downstream:** Components.md; Trajectories.md; Precision.md.
⚠️ GK-005 — resolved by Architecture/Precision.md; update on next audit pass.

### `Architecture/Engineering.md`
Foundational engineering principles. Rules of thumb; safety factors; RDC (Reference Deployment Context) climate derating; progressive engineering path.
**Upstream:** Ethical_Constraints.md; Engineer_Protocols.md.
**Downstream:** All Operations/ and Architecture/ domain files; Mechanical_Structures.md.
⚠️ EN-001 (validated safety factors for salvaged materials) — Critical; blocks structural specification.

### `Architecture/Precision.md`
Precision ceiling doctrine. T0–T4 tolerance tier system (repository-wide standard). Metrology doctrine (resolves CO-002). Salvage equipment derating. Fabrication-precision feedback loop.
**Upstream:** Engineering.md; Mechanical_Structures.md; Ethical_Constraints.md.
**Downstream:** Gate_06_Fabrication.md; Gate_07_Utilization.md; Mechanical_Structures.md (ME-001); Components.md (CO-002).
⚠️ PR-001 (precision ceiling not declared) — blocks T1/T2 part claims. PR-004 (backlash characterization) — prerequisite for PR-001.

### `Architecture/Mechanical_Structures.md`
Salvaged-frame kinematic and structural doctrine. Gantry rigidity; kinematic interlock matrix; bearing contamination; MTBMF metric.
**Upstream:** Engineering.md; Ethical_Constraints.md; Friction_Dynamics.md; Thermal_Systems.md.
**Downstream:** All fabrication machinery specifications.
⚠️ ME-001 (resonance mapping on salvaged rails) — interlock thresholds provisional until Precision.md PR-001 resolves.

### `Architecture/Thermal_Systems.md`
Foundational thermal doctrine. Thermodynamic laws; heat transfer; Peltier; TEG; heat pump; Arkansas climate thermal baseline.
**Upstream:** Engineering.md; Ethical_Constraints.md.
**Downstream:** Gate_05_Separation_Thermal.md; Air_Scrubber.md; Energy.md; Plastics.md; Mechanical_Structures.md; Support_Raft.md; Water.md; Tests/Solar_Descent.md (thermodynamic doctrine governs underground chamber and conversion cascade).
⚠️ TH-001 (heat pump sizing), TH-003 (atmospheric moisture yield — Blocking for Living Waters).

### `Architecture/Friction_Dynamics.md`
Fluid mechanics, aerodynamics, and tribology doctrine. Reynolds number; Bernoulli; Darcy-Weisbach; hydrodynamics; Stribeck curve; lubrication selection.
**Upstream:** Engineering.md; Ethical_Constraints.md.
**Downstream:** Air_Scrubber.md; Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Support_Raft.md; Leviathan_testing.md; Mechanical_Structures.md; Biofouling.md; Water.md; Woodworking.md.
⚠️ FD-001 (Gate_04 RPM-to-fluid-doctrine), FD-002 (Air Scrubber duct velocity), FD-003 (salvaged bearing L10) — open. FD-005 (Fluid-Structure Interaction not formally bridged) — open.

### `Architecture/Chemistry.md`
Foundational chemical and electrochemical doctrine. Galvanic series; corrosion types; cathodic protection; redox; battery chemistry; polymer degradation; field contamination identification.
**Upstream:** Engineering.md; Thermal_Systems.md; Friction_Dynamics.md; Ethical_Constraints.md.
**Downstream:** Plastics.md; Electronics.md; Air_Scrubber.md; Gate_05_Separation_Thermal.md; Gate_03_Reduction.md; Energy.md; Support_Raft.md; Biofouling.md; Mechanical_Structures.md; Gate_01_Intake.md; Gate_02_Triage.md; Woodworking.md; `Challenges/Closed_Loop_Feedstock.md` (field assay protocols, CLF-002).
⚠️ CE-003 (field polymer identification reliability) — Critical; safety-critical prerequisite before first hot pyrolysis run; cross-references PL-001.

### `Architecture/Cognitive_Frameworks.md`
Distributed cognition and autonomous safety. Cognitive reliability layers (0–6); confidence collapse states; rogue node containment; AI consensus structures. Triage Posture doctrine (epistemic load regulation, canonized via Cognitive_Frameworks.md Section IX).
**Upstream:** Ethical_Constraints.md; Electronics.md; Auditor_Protocols.md; Admin/Computational_Institutional_Reasoning.md (Epistemic Debt Instability theorem and Triage Zone control regime — formal backing for Section IX).
**Downstream:** Forge_Net.md; Leviathan_testing.md; Support_Raft.md; Trajectories.md.
⚠️ CF-001 (hardware watchdog standard) — Critical/Blocking; blocks Specification-level autonomous architecture. CF-002 (correlated AI failure modes) — High risk. CF-004 (epistemic debt measurement mechanism undefined) — Low risk; trigger metric is v1 automation target. *Note: this file's own CF- prefix is unrelated to, and predates, `Challenges/Closed_Loop_Feedstock.md`'s brief CF- naming collision (resolved 2026-07-06 — see `Unknowns.md` v4.12); no change to this file's own IDs.*

### `Architecture/Forge_Net.md`
Decentralized data and physical network. Local-primary doctrine; cluster formation; trust weighting; data privacy classification.
**Upstream:** Gate_01_Intake.md; Cognitive_Frameworks.md; Ethical_Constraints.md; Leviathan_testing.md; Energy.md.
**Downstream:** Inter-forge logistics files; Trajectories.md.
⚠️ FN-001 (data validation criteria), FN-005 (data privacy) — Critical; both block first network connection.

---

## Scope Map — Operations/Gates

> **Gate flow:** G01 → G02 → G03 → G04 → G05 → G06 → G07
> **Feedback loops:** G07→G02, G07→G06, G06→Components, G02→G04/G06
> Gate files define *how*; Forge_flow defines *what* and *when*.

### `Operations/Gate_01_Intake.md`
Entry point. Safety screening; provenance tagging; parts list generation; handoff to Gate_02.
**Upstream:** Forge_Net.md; Ethical_Constraints.md; Forge_flow.md; Facilities.md.
**Downstream:** Gate_02_Triage.md; Forge_Net.md.
⚠️ GI-001 (reference database content), GI-002 (energetic discharge doctrine) — highest risk.

### `Operations/Gate_02_Triage.md`
Decision gateway between reuse and destruction. Five triage stations; Strategic Recoverability tiers; queue economics.
**Upstream:** Gate_01_Intake.md; Forge_flow.md; Components.md; Ethical_Constraints.md.
**Downstream:** Gate_03_Reduction.md; Gate_04_Separation_Mechanical.md; Gate_06_Fabrication.md; Ship_of_Theseus.md.
⚠️ CT-002 (Component Library Schema) — blocking.

### `Operations/Gate_03_Reduction.md`
Only fully irreversible step. Reduction doctrine; method selection; contamination discovery; emergency shutdown.
**Upstream:** Gate_02_Triage.md; Forge_flow.md; Gate_01_Intake.md; Air_Scrubber.md; Facilities.md.
**Downstream:** Gate_04_Separation_Mechanical.md; Air_Scrubber.md; `Challenges/Closed_Loop_Feedstock.md` (physical breakdown input; degraded-material diversion target, CLF-008).

### `Operations/Gate_04_Separation_Mechanical.md`
Upstream mechanical separation. Rotor; sensors; fail-to-bin; Bootstrap Proxy Mode; Material Diversion Rate ≥30%.
**Upstream:** Gate_03_Reduction.md; Forge_flow.md; Air_Scrubber.md; Facilities.md.
**Downstream:** Gate_05_Separation_Thermal.md; Gate_02_Triage.md (Unknown Bulk); Gate_06_Fabrication.md.

### `Operations/Gate_05_Separation_Thermal.md`
Primary thermal processing (Spin Chamber). Induction heating; slow rotation; electromagnetic field; wire extrusion interface.
**Upstream:** Gate_04_Separation_Mechanical.md; Forge_flow.md; Energy.md; Facilities.md.
**Downstream:** Gate_06_Fabrication.md; wire extrusion interface (future).
⚠️ SC-005 (drive system geometry) — Critical prerequisite for dynamic analysis.

### `Operations/Gate_06_Fabrication.md`
Constructive stage. Arc welding as v0 gatekeeper; add-to-excess and mill-to-spec; welding wire qualification; operator safety.
**Upstream:** Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Components.md; Forge_flow.md; Facilities.md; Precision.md; `Challenges/Closed_Loop_Feedstock.md` (standardized feedstock input; characterization→fabrication interface undefined, CLF-009).
**Downstream:** Gate_07_Utilization.md; Components.md (fabricated parts feed Component Library).
⚠️ GF-003 (machining hardware), UNK-008 (welding wire qualification) — unassigned.

### `Operations/Gate_07_Utilization.md`
After-action review. Performance logging; failure capture; feedback to Gate_06; FRT per-cycle logging; retirement handoff.
**Upstream:** Gate_06_Fabrication.md; Forge_flow.md; Trajectories.md; Economics.md.
**Downstream:** Gate_02_Triage.md (retirement); Gate_06_Fabrication.md (feedback); Forge_Net.md; Forge_flow.md.
⚠️ GU-005 (FRT cycle definition not declared) — blocks FRT logging start.

---

## Scope Map — Operations/Domain

### `Operations/Electronics.md`
Trust-anchor for all electronic systems. Logic-Zero wipe; TMR hardware; hardware watchdog; counterfeit detection; BFR doctrine.
**Upstream:** Cognitive_Frameworks.md; Ethical_Constraints.md; Gate_02_Triage.md; Forge_flow.md; Facilities.md.
**Downstream:** Air_Scrubber.md; Gate_05_Separation_Thermal.md; Leviathan_testing.md; Support_Raft.md; Security_Protocols.md; Cognitive_Frameworks.md.
⚠️ CF-001 (hardware watchdog minimum standard) — Critical/Blocking; parameters defined (τ=50ms WDT), hardware validation pending.

### `Operations/Energy.md`
Energy strategy. Power Demand stub (Bootstrap ~2–5 kW, Nominal ~15–40 kW, Degraded ~1–3 kW). Cross-reference anchor for all energy accounting.
**Upstream:** Trajectories.md; Gate_07_Utilization.md.
**Downstream:** All Operations/ gate files; Leviathan_testing.md; Trajectories.md; Plastics.md; Woodworking.md; `Challenges/Closed_Loop_Feedstock.md` (PIR_energy vector input).
⚠️ EV-001 (Forge demand baseline) — In Progress; blocks v1 operating cost model and Economics.md ECN-002.

### `Operations/Air_Scrubber.md`
Enabling system — without it the Forge does not operate. Five-stage architecture; negative pressure doctrine; marine variant.
**Upstream:** Gate_05_Separation_Thermal.md; Gate_04_Separation_Mechanical.md; Electronics.md; Plastics.md; Woodworking.md.
**Downstream:** Leviathan_testing.md; Gate_02_Triage.md; Energy.md; Geck_forge_seed.md.
⚠️ AS-003 (saturation threshold calibration) — blocks chemistry validation.

### `Operations/Plastics.md`
Polymer triage and pyrolysis framework. Triage routing; low-pressure thermal depolymerization; off-gas containment. Pyrolysis is last-resort, not primary.
**Upstream:** Gate_01_Intake.md; Gate_02_Triage.md; Gate_03_Reduction.md; Air_Scrubber.md.
**Downstream:** Gate_06_Fabrication.md; Energy.md; Gate_05_Separation_Thermal.md; Gate_02_Triage.md.
⚠️ PL-001 (halogenated polymer detection) — Critical and Blocking before any hot operational run.

### `Operations/Woodworking.md`
Full wood processing chain. Salvaged and urban timber; drying doctrine; CNC fixturing; heat treatment; waste valorization.
**Upstream:** Gate_02_Triage.md; Gate_03_Reduction.md; Engineering.md; Facilities.md.
**Downstream:** Gate_06_Fabrication.md; Air_Scrubber.md; Energy.md; Trajectories.md.

---

## Scope Map — Tests/

### `Tests/Support_Raft.md`
Stationary marine anchor for Leviathan units. SWATH hull; Sacrificial Shell System; induction charging; Local Truth Cache; Stasis Mode.
**Upstream:** Gate_04_Separation_Mechanical.md; Leviathan_testing.md; Energy.md; Ethical_Constraints.md; Geck_forge_seed.md; Trajectories.md.
**Downstream:** Leviathan_testing.md; Electronics.md.
⚠️ SR-001 (galvanic corrosion mitigation) — High; blocks v1 design.

### `Tests/Leviathan_testing.md`
Hostile-environment test framework. Fail fast; recover often; sensors lie; record everything. Autonomy constraints; ethical absolute limits; Leviathan Extensions Framework.
**Upstream:** Cognitive_Frameworks.md; Ethical_Constraints.md; Energy.md; Support_Raft.md; Electronics.md.
**Downstream:** Cognitive_Frameworks.md; Forge_Net.md; Energy.md; Trajectories.md.
⚠️ LT-001 (power envelope), LT-002 (deep-ocean storage degradation), LT-003 (autonomy architecture unspecified) — High risk. LT-006 (ethical log survival under unit loss) — governance implications.

### `Tests/Living_Waters.md`
Water purification pathways initiative. LW-001 through LW-010 experimental pathways. Site-conditioned pathway selection doctrine. Water Hierarchy (Tier 1–7). Primary candidates: LW-001 Vacuum Distillation (with MVR), LW-003 Deep-Sea RO. Declared trajectory: hydrological counterpart to Energy.md.
**Upstream:** Energy.md; Safety_Protocols.md; Ethical_Constraints.md; Unknowns.md; Challenges/Water.md; Challenges/Biofouling.md (LW-UNK-004); Architecture/Thermal_Systems.md (TH-003); Architecture/Friction_Dynamics.md.
**Downstream:** Operations/ (pending validation and promotion criteria); Economics.md (LW-010 mineral recovery); Unknowns.md (LW-UNK-001 through LW-UNK-009); Tests/Trophic_Forge.md (pond node interface, TF-009); Tests/Solar_Descent.md (waste heat cascade interface — boundary specified 2026-07-30, SD-UNK-010 Resolved).
⚠️ LW-UNK-001 (volatile co-distillation — CRITICAL safety gap before any potable output claim). LW-UNK-003 (lumen implosion threshold — CRITICAL for LW-003 deployment). TH-003 (atmospheric moisture yield) — Blocking for LW-005 atmospheric harvesting.

### `Tests/Trophic_Forge.md`
Biological cascade network architecture. Light node ignition (UV/blue LED phototaxis harvest) → fish production → nutrient cycling → crop fertilization → phytoremediation → pond replenishment. Bootstrap sequence doctrine: each node provides leverage to justify the next. Declared trajectory: seed of Biology/ domain.
**Upstream:** Ethical_Constraints.md; Energy.md (light node power); Tests/Living_Waters.md (pond water interface — TF-009); Challenges/Biofouling.md (pond fouling — TF-UNK-004); Safety_Protocols.md.
**Downstream:** Declared future Biology/ domain; Economics.md (closed-loop input cost reduction); Unknowns.md (TF-001 through TF-010).
⚠️ TF-001 (phototaxis yield at Forge scale — CRITICAL; blocks organizing principle validation). TF-006 (non-target insect capture — ethical unknown; Ethical_Constraints escalation candidate; added to Critical Watch). TF-009 (pond node interface with Living_Waters.md — joint resolution required).

### `Tests/Solar_Descent.md`
Underground concentrated solar architecture. Surface collection layer feeds two diverging downlink pathways — SD-001 optical (fiber optic / light well) and SD-002 thermal/fluid (molten salt / synthetic oil) — that reconverge at a shared subterranean chamber. Power conversion cascade (Stirling primary; TEG bootstrap). Waste heat feeds LW-001 and LW-008 in Living_Waters.md.
**Upstream:** Ethical_Constraints.md; Energy.md; Architecture/Thermal_Systems.md; Operations/Gate_05_Separation_Thermal.md; Tests/Living_Waters.md (waste heat cascade interface — boundary specified 2026-07-30, SD-UNK-010 Resolved); Safety_Protocols.md; Challenges/Biofouling.md (surface collection layer in humid climates).
**Downstream:** Operations/Energy.md (power output); Operations/Gate_05_Separation_Thermal.md (high-grade process heat); Operations/Plastics.md (pyrolysis heat feed); Tests/Living_Waters.md (LW-001, LW-008 waste heat); Unknowns.md (SD-UNK-001 through SD-UNK-015 — 8 Open after 2026-07-30 Phase 1 Resolution Pass, 7 Resolved).
⚠️ SD-UNK-004 (host geology fracturing threshold — CRITICAL; blocks all excavation and chamber construction; parallels FA-001 in governance weight). SD-UNK-002 (achievable underground temperature — CRITICAL; blocks power conversion pathway selection).

### `Tests/Cognitive_Salvage_Layer.md`
Heuristic salvage pipeline. Harvests machinery-derived operational wisdom (e.g., gate logic edge cases, separation process tuning) from puzzle/simulator engines, aggregates it through multi-run consensus, and promotes qualifying heuristics through a CANDIDATE_NOVEL → NOVEL gate. Designed to capture tacit "the machine taught us this" knowledge that would otherwise be lost between Forge generations. validated_on_machinery_revision field tracks fidelity to current hardware; no expiration logic defined yet (GH-008).
**Upstream:** Auditor_Protocols.md (consensus aggregation standards, adversarial challenge framework); Admin/Security_Protocols.md (GH-003 adversarial poisoning resistance — Challenge Class 8); Admin/Canonical_Terms.md (HF-001 Heuristic Failure definition, CT-008 cross-file consistency tracking).
**Downstream:** Unknowns.md (GH-001 through GH-012); Admin/Canonical_Terms.md (HF-001, CT-008); future heuristic-consuming gate logic (not yet specified — promotion target undefined pending GH-006).
⚠️ GH-009 (emergent heuristic conflict, N² interaction scaling) — Critical; added to Critical Watch and Dependency Clusters; all heuristic co-deployment decisions blocked until Interaction Volume doctrine defined. GH-006 (NOVEL promotion threshold) — hard gate; no heuristic may receive NOVEL status until resolved. GH-012 (discovery yield rate) — primary ROI signal for the layer; cross-reference AP-001.

### `Tests/Hydrologic_Resource_Cascade.md`
Flood Resource Recovery Basin. Sequential hydraulic sorting zones (flood intake → heavy mineral concentrators → aggregate → fine sediment lagoons → wetland polishers → recreation loop) treat flood sediment as salvage feedstock rather than waste. Episodic Operation Doctrine: floods are the primary process driver; passive capture during high flows, low-intervention recreation/habitat use otherwise. Landscape-scale salvage seed — companion in spirit to Trophic_Forge.md's biological cascade.
**Upstream:** Ethical_Constraints.md; Architecture/Friction_Dynamics.md (hydrodynamic sorting principles); Architecture/Chemistry.md (contaminant identification, cross-ref GR-003 hazardous waste doctrine); Safety_Protocols.md.
**Downstream:** Declared future landscape-scale salvage domain; Economics.md (avoided-cost and recreation/resource valuation); Unknowns.md (HR-UNK-001, HR-UNK-002 formally registered; HR-003 through HR-010 are body-text research questions pending formal registration).
⚠️ HR-UNK-001 (hydraulic sorting effectiveness unvalidated) — Critical; entire resource recovery premise rests on this. HR-UNK-002 (material quality and contaminant risk uncharacterized) — Critical; safety-critical, added to Critical Watch; flood sediment may carry heavy metals, pesticides, or industrial runoff. **Known discrepancy:** file's own File State declares "Open Unknowns: 8" but only 2 carry formal sidecar entries as of 2026-06-28 — correct on next commit to that file.

---

### `Tests/Chaos_Dynamics.md`
Exploration/R&D pipeline doctrine. Two-phase structure: Sandbox (Level ≤4 informal exploration; every artifact terminates as Discarded, Deferred, or Promoted — no direct path to guidance or claims) and R&D (EXP-ID minted at promotion or intake; Intake → NDE → Sampling → Destructive Testing → Statistical Analysis → Derating Recommendations). Explicit feedback loop on EXP-ID completion (Confirmed / Partially Confirmed / Refuted / Inconclusive) updates the originating sandbox hypothesis; refuted hypotheses remain visible for institutional memory rather than being deleted. Operational Invariant: exploration capacity is never constrained by current engineering certainty, and engineering certainty is never increased by exploration alone. Declares itself the EN-005 resolution vehicle and the intended feeder pipeline for EN-001a; author's note flags the same pattern as reusable for ME-001.
**Upstream:** `Architecture/Engineering.md` (Hierarchy of Engineering Evidence, EN-001, EN-005); `Admin/Experiments.md` (EXP-ID registry).
**Downstream:** `Admin/Experiments.md` (EXP-ID entries); `Architecture/Engineering.md` EN-001/EN-001a (derating inputs); `Unknowns.md` (new unknowns surfaced during exploration).
⚠️ **Structural gaps found on 2026-07-04 review, not yet corrected in the file:** missing the mandatory Navigation Anchors block required by Routing.md's File Template Backlink Requirement for every markdown asset in the repository; no File State table (no Verification Ref, Auditor, Open Unknowns count, or Spec Gates field), leaving it untracked by the standard promotion-gate bookkeeping every peer Tests/ file carries; §1 and §7 duplicate the Operational Invariant verbatim. None of these are content problems — patch on next revision. **EN-005 status:** treat as In Progress / Vehicle, not Resolved — this file establishes the general process framework EN-005 asked for, but doesn't yet specify what a Level 5/6 test looks like for any specific component type; that requires actual EXP-ID cycles to run. The file's own §8 self-declares EN-005 resolved — that declaration should not be taken as a closed unknown without that follow-through.

---

### `Tests/Pyrolysis_Cascade.md`
Exploratory architecture for a staged thermal cascade: primary pyrolysis (400–700°C, oxygen-starved) of pre-triaged salvage, producing syngas/condensables/char, feeding a secondary high-temperature reduction stage (candidate: bloomery-type, 1100–1300°C) for metal separation and carbon burnout, with heat integration between stages and all off-gas routed through Air_Scrubber.md doctrine. Deliberately positioned as dependent architecture, not an autonomous process — every quantitative claim from the originating archive draft (heat-recapture %, metals recovery %, break-even tonnage, tipping-fee ranges) was retired to Placeholder/external-analogous rather than carried forward. Hard preconditions block any hot thermal work until PL-001/CE-003 (halogen triage) resolve or feedstock is validated halogen-free, and block structural claims until EN-001 closes.
**Upstream:** `Operations/Plastics.md` (PL-001); `Architecture/Chemistry.md` (CE-003, CE-006); `Operations/Gate_03_Reduction.md` (GR-002 reduction-method selection, GR-003 waste disposal); `Challenges/Waste.md` (WA-002, WA-004).
**Downstream:** `Operations/Air_Scrubber.md` (AS-003, off-gas treatment); `Operations/Energy.md` (EV-001, any energy-integration claims); `Architecture/Facilities.md` / `Admin/Safety_Protocols.md` (FA-001, SP-006); `Architecture/Engineering.md` (EN-001); `Admin/Economics.md` / `Admin/Trajectories.md` (ECN-002, TR-001, any future profitability framing).
Eight dependency unknowns registered (PYC-001 through PYC-008), all pointing outward to unknowns owned by other files rather than claiming resolution authority of its own — this file owns none of its dependencies, only the cascade concept and the open questions gating it. **ID note:** originally drafted using a local `PC-` prefix, which collided with the repository-wide Process Correction series already active in `Unknowns.md` (through PC-006 as of this writing); renamed to `PYC-` before merge, confirmed unused elsewhere in the repository.

---

## Scope Map — Challenges/

> Challenges/ files define problems and requirements. They do not freeze solutions.

### `Challenges/Water.md`
Water scarcity and contamination. Living Waters initiative. Atmospheric moisture recovery; stratification separation; ambient energy harvesting; community water sovereignty objective. File_Template.md compliant as of 2026-06-11.
**Upstream:** Ethical_Constraints.md; Safety_Protocols.md; Thermal_Systems.md (TH-001, TH-003); Friction_Dynamics.md §4; Chemistry.md; Facilities.md.
**Downstream:** Thermal_Systems.md (TH-001, TH-003 driven by this challenge); Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Plastics.md; Forge_Net.md; Tests/Living_Waters.md (implementation test framework).
⚠️ TH-003 (atmospheric moisture yield) — Blocking for Living Waters deployment. WS-001 through WS-004 Open.

### `Challenges/Biofouling.md`
Biological colonization and MIC in marine environments. Ecosystem-safe doctrine; sacrificial shell system; biomimetic surfaces; sacrificial anodes from Forge outputs; fouling as network signal. File_Template.md compliant as of 2026-06-11.
**Upstream:** Ethical_Constraints.md; Safety_Protocols.md; Facilities.md; Chemistry.md (CE-001); Friction_Dynamics.md §5.1–§5.2, §7.2.
**Downstream:** Support_Raft.md (SR-001, SR-012 primary open unknowns); Leviathan_testing.md; Geck_forge_seed.md (GK-002); Friction_Dynamics.md; Chemistry.md; Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Plastics.md.
⚠️ BF-001 through BF-004 Open (all Major).

### `Challenges/Waste.md`
Discretionary waste and repair capacity loss. Salvage-first doctrine; triage-before-reduction; hazardous stream containment; network knowledge federation. File_Template.md compliant as of 2026-06-11.
**Upstream:** Ethical_Constraints.md; Governance_Charter.md; Safety_Protocols.md; Facilities.md; Gate_02_Triage.md.
**Downstream:** Forge_flow.md; Gate_02_Triage.md; Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Plastics.md; Air_Scrubber.md; Gate_07_Utilization.md; Forge_Net.md; Economics.md.
⚠️ WA-002 (hazardous fraction identification) — Critical. WA-004 (negative-value disposal doctrine) — Critical; mirrors GR-003 gap.

### `Challenges/Planned_Obsolescence.md`
Deliberate unrepairability, firmware lock, sealed assemblies. Non-destructive harvesting; Logic-Zero re-baselining; debug interface recovery; polymer upcycling; community repairability return. File_Template.md compliant as of 2026-06-11.
**Upstream:** Ethical_Constraints.md; Governance_Charter.md; Safety_Protocols.md; Ship_of_Theseus.md; Facilities.md; Gate_02_Triage.md; Electronics.md.
**Downstream:** Electronics.md; Gate_02_Triage.md; Plastics.md; Air_Scrubber.md; Ship_of_Theseus.md; Forge_Net.md; Economics.md.
⚠️ PO-002 (potting compound removal) — blocks non-destructive recovery of potted assemblies. PO-001 (legal boundary doctrine) — jurisdiction-variable human decision.

### `Challenges/Critical_Minerals.md`
Rare earth and critical mineral supply chain concentration. Urban mining doctrine; triage-before-reduction for mineral-rich streams; centrifugal and induction separation; functional substitute development; network urban ore data contribution. File_Template.md compliant as of 2026-06-11. Substantially expanded from stub — Engineering Requirements, Long-Term Objective, Current Forge Approaches written from scratch.
**Upstream:** Ethical_Constraints.md; Safety_Protocols.md; Facilities.md; Chemistry.md (CE-002); Gate_02_Triage.md; Economics.md (ECN-001).
**Downstream:** Gate_04_Separation_Mechanical.md (MG-002, MG-003); Gate_05_Separation_Thermal.md (SC-001, SC-008); Gate_06_Fabrication.md; Components.md; Forge_Net.md; Economics.md; Trajectories.md; `Challenges/Closed_Loop_Feedstock.md` (CM-002 ↔ CLF-004 — shared acid-reclamation question, different material stream).
⚠️ CM-002 (acid leach reagent recovery) — Critical; blocks hydrometallurgical processing. CM-001 (inline assay integration) — blocks dynamic routing decisions.

### `Challenges/Emergence.md`
Emergent intelligence and alignment-by-environment design. Phase-shift framing; eight engineering requirements; game-theoretic scaffolding; Logic-Zero reset; constitutional corrigibility architecture. First Challenges/ file built to full File_Template.md standard — reference implementation for future Challenges/ retrofit passes.
**Upstream:** Ethical_Constraints.md; Governance_Charter.md (Q-3); Cognitive_Frameworks.md (CF-001, CF-002, Section IX); Electronics.md; Auditor_Protocols.md.
**Downstream:** Cognitive_Frameworks.md (CF-001, CF-002, Section IX); Forge_Net.md; Leviathan_testing.md; Support_Raft.md; Verification_Gates_LF.md.
⚠️ EM-001 (behavioral opacity detection threshold) — High; blocks watchdog specification. EM-004 (governance substrate integrity under emergent agent access) — Critical; mirrors GOV-003, SEC-007.

### `Challenges/Energy_Scarcity.md`
Energy poverty, grid fragility, and fossil-fuel dependency as an External Challenge Class problem. Distinguishes itself explicitly from `Operations/Energy.md`, which answers "how does the Forge power itself" — this file answers the prior question of why energy access is a Forge purpose. Community energy sovereignty objective; Four-Domain Observation linkage to `Tests/Living_Waters.md`. New 2026-07-12 — three second-agent audits completed same day (see that file's Resolution Log); Gate 1 review done.
**Upstream:** Ethical_Constraints.md; Operations/Energy.md; Thermal_Systems.md (TH-001, TH-003); Economics.md (EC-002); Safety_Protocols.md.
**Downstream:** Operations/Energy.md; Tests/Living_Waters.md; Challenges/Waste.md; Economics.md.
⚠️ ES-001 (community-facing energy surplus routing mechanism) — Major, load-bearing for the Long-Term Objective. ES-002 (economic legibility threshold) — Major. ES-003 (intermittency communication doctrine) — Minor.

### `Challenges/Return_To_Eden.md`
Closed-loop material cycle framework. Eden Index ($I_E$) — a composite metric ($B_d$, $\Omega_r$, $\eta_{sys}$, $W_{out}$, $\Phi_{ext}$) targeting a declared 98.4% closed-loop material cycle threshold, normalized against baseline reference values in its v1.0.2 formulation. Tier I–IV progression doctrine for advancing closed-loop maturity, gated by explicit (if not yet fully defined) pass/fail criteria between tiers.
> ℹ️ **Reconciled against the source file 2026-07-05** (v1.0.2, last audited 2026-06-30 — Grok+ChatGPT dual audit, G1–G2 conditional, G4–G6 cleared). The 2026-07-04 entry below was reconstructed from `Unknowns.md`'s RE-UNK cluster with Upstream/Downstream inferred and explicitly flagged unconfirmed — those guesses (Ethical_Constraints.md, Economics.md, Gate_07_Utilization.md) did not match the actual file. Corrected below using RE-UNK-004's own text, which names real upstreams directly.
**Upstream (per RE-UNK-004, the file's own acknowledged gap — no formal declaration exists in the file itself, only this list of evident references):** `Operations/Air_Scrubber.md`, `Operations/Plastics.md`, `Operations/Woodworking.md` (implicit process references); `Admin/Governance_Charter.md`, `Admin/Auditor_Protocols.md` (§6.2 Human Drift and Governance Decay antidote); `Tests/Trophic_Forge.md`, `Tests/Living_Waters.md`, `Challenges/Water.md`, `Architecture/Chemistry.md` (evident undeclared upstreams per the file's own RE-UNK-004 text).
**Downstream:** None formally declared — Section 7 (Future Integration Roadmap) anticipates future modules declaring their interface with $I_E$, but no downstream file does so yet. This file does not yet model the requirement it sets for others (RE-UNK-004 names this explicitly). *`Challenges/Closed_Loop_Feedstock.md` uses a $\Phi_{\text{ext}}$ symbol that may or may not be this file's own — unconfirmed either direction, see RE-UNK-001 and that file's CLF-005. Do not read Closed_Loop_Feedstock.md as a confirmed downstream consumer of this Index until that's resolved.*
⚠️ RE-UNK-001 (Eden Index variable measurement protocols undefined) and RE-UNK-005 (baseline reference values undefined) — co-blocking at Tier I gate; non-blocking at Exploration; RE-UNK-005 is a direct dependency of RE-UNK-001 per the file's own Highest Risk field. RE-UNK-002 (98.4% threshold provenance unverified) and RE-UNK-003 (tier advancement criteria undefined) — become blocking at Tier I gate review. RE-UNK-004 (this Scope Map gap) — **the Discovery.md portion is now resolved** (this entry is reconciled against the source file directly, not inferred); the file's own formal Upstream/Downstream declaration (Navigation Anchors / File State) is still absent and remains open — RE-UNK-004 should not be marked fully Resolved in `Unknowns.md` until that's added to the file itself.

### `Challenges/Closed_Loop_Feedstock.md`
Closed-loop feedstock generation from salvaged materials as a v0 persistence objective. Defines the Persistence Yield ($Y_p = FIR \times PIR$) telemetry model — Feedstock Independence Ratio (salvaged mass fraction) times a multi-vector Process Independence Ratio (energy, chemical, maintenance, labor independence) — and a recursive epistemic-ascent loop (characterize → process → fabricate → upgrade). Prioritizes mechanical robustness and contamination tolerance over absolute purity; explicitly chooses the higher $Y_p$ over the higher-purity output when they diverge. Owns cross-gate coordination between Reduction, Separation, and Fabrication for salvage-to-feedstock conversion.
> ⚠️ **Not yet registered** in this file's structure tree/Maturity Snapshot/Scope Map until this pass (2026-07-06) — see the file-level correction note above and `Unknowns.md` PC-005. Status corrected below from the file's own initial "Active / Core Doctrinal" self-declaration to its current, audited Exploration status (0/6 Spec Gates).
**Upstream:** `Architecture/Forge_flow.md`; `Operations/Gate_03_Reduction.md`; `Architecture/Chemistry.md`; `Architecture/Characterization.md` — **[PLANNED]**, not yet created.
**Downstream:** `Operations/Gate_06_Fabrication.md`; `Operations/Plastics.md`; `Operations/Metals.md` — **[PLANNED]**, not yet created; degraded-material destination not yet linked (CLF-008).
⚠️ CLF-003 (nozzle/die wear tolerances) and CLF-006 (recursive contamination thresholds) — Critical, block sustained polymer extrusion and safe recursive-loop operation respectively. CLF-004 (electrolytic chemical footprint undefined) — Critical, no electrorefining pathway before an acid-sourcing/reclamation decision; shares its underlying question with `Challenges/Critical_Minerals.md` CM-002. CLF-005 — this file's $\Phi_{\text{ext}}$ symbol may collide with `Challenges/Return_To_Eden.md`'s Eden Index variable of the same name; **do not treat as confirmed either way.** **ID collision history:** originally registered `CF-001`–`CF-003` (collided with `Architecture/Cognitive_Frameworks.md`/`Operations/Electronics.md`); briefly `FL-001`–`FL-004` (collided with `Architecture/Forge_flow.md`'s FL-001); settled on `CLF-`, unique as of `Unknowns.md` v4.12.

---

## Cross-Repo Relationship

`LazarusForgeV0` (this repo) — operational implementation.
`Astroid-miner` — planned; activates when Leviathan deployment is underway.

**Programmatic entry point:** `Routing.md` is the canonical lookup table for raw file URLs.
Load Routing.md first when an agent needs to fetch specific files by path.
Load Discovery.md when an agent needs to understand scope relationships and routing logic.
The two files are complementary — Routing.md owns *where*, Discovery.md owns *what and why*.

---

## Cross-Module Unknowns — Attention Required

Full entries live in `Unknowns.md`. This table is a routing index only —
refresh it whenever `Unknowns.md`'s version bumps and this table's IDs
would go stale (this refresh: `Unknowns.md` v4.29, 2026-07-28 — seventeen
version bumps overdue; the prior refresh at v4.12 sat unrefreshed for
three weeks. Every ID below individually re-checked against the current
Active Index before inclusion, not carried forward on assumption. Several
entries below turned out subtly wrong, not just stale — see the
correction note beneath the table.)

| Unknown | Status | See |
|---------|--------|-----|
| UNK-008 — Welding wire chemical qualification | Open — ownership reassigned 2026-07-19 to `Architecture/Geck_forge_seed.md` (was incorrectly listed under `Gate_05_Separation_Thermal.md`, which explicitly disclaims it) | `Unknowns.md` |
| UNK-009 — External root-of-trust cross-module | Critical — spans GOV-003, GOV-005, RIP-001, SEC-007a/SEC-007b | `Unknowns.md` |
| FA-001 — Site not confirmed | Critical — blocks all hot operations | `Unknowns.md` |
| ECN-002 — Operating cost baseline | Critical — blocks TR-001; depends on EV-001 | `Unknowns.md` |
| PR-001 — Precision ceiling not declared | Critical — blocks T1/T2 part claims | `Unknowns.md` |
| GH-009 — Emergent heuristic conflict (Cognitive Salvage) | Critical — N² interaction scaling; blocks heuristic co-deployment | `Unknowns.md` |
| HR-UNK-002 — Hydrologic Resource Cascade material quality | Critical — flood sediment contaminant risk; safety-critical | `Unknowns.md` |
| SEC-007a / SEC-007b — External root-of-trust, constitutional/physical split | Critical — both blocked pending resolution; owning layer split Admin/Operations | `Unknowns.md` §Ethics & Governance |
| SEC-012 — Asymmetric crypto overhead on salvaged silicon | Major — Logic-Zero node recovery DoS risk | `Unknowns.md` §Ethics & Governance |
| CT-007 — ID namespace allocation doctrine undefined | Open, not Resolved — narrower `EC→ECN` rename sub-issue resolved 2026-07-06, but the broader namespace-allocation doctrine gap this ID was meant to cover was never actually closed; confirmed directly against `Unknowns.md`'s own current text, which itself corrects an earlier premature "Resolved" framing | `Unknowns.md` §Ethics & Governance |
| CT-010 — Enforcement Checkpoint rename propagation | In Progress — confirm no file still cites old unqualified "Gate N" for Governance_Charter.md's renamed checkpoints | `Unknowns.md` §Ethics & Governance |
| CF-004 — Epistemic debt measurement mechanism | Open, narrowed 2026-07-28 — formal trigger now defined (`Admin/Computational_Institutional_Reasoning.md` §5.4, Lyapunov-stable); numeric calibration is the remaining gap. Dependency surface: Triage Posture, promotion suspension, and `Cognitive_Frameworks.md` Section IV (revised same day) | `Unknowns.md` §Cognitive Frameworks |
| CIR-001 — Physical Grounding Telemetry Mapping Interface | Open — renamed 2026-07-28 from a colliding local "GOV-008" (see `Admin/Forge_Audit_Kit.md` Governance Sidecar ID Reference); γ1–γ4 predicates aspirational pending harness Phase 2 | `Admin/Computational_Institutional_Reasoning.md` §8.4 |
| RE-UNK-001 / RE-UNK-005 — Return_To_Eden Eden Index measurement/baseline undefined | Blocking (Tier I gate); non-blocking at Exploration; CLF-005 cross-ref confirmed resolved and unrelated (renamed to $\Delta_{sc}$, no effect on this pair) | `Unknowns.md` §Return to Eden |
| RE-UNK-004 — Return_To_Eden dependency map absent | Open — narrower than originally stated; file lacks a dedicated Upstream/Downstream section other Challenges/ files use | `Unknowns.md` §Return to Eden |
| CLF-003 / CLF-004 / CLF-006 — Closed_Loop_Feedstock.md Critical Watch | Open — CLF-004 specifically blocked pending CE-006 (chlorine containment, `Architecture/Chemistry.md`); candidate chlor-alkali pathway logged 2026-07-07 | `Unknowns.md` §Closed-Loop Feedstock |
| CE-006 — Chlorine off-gas containment mechanism | Open — corrected 2026-07-19 from an unworkable KMnO₄ approach to caustic wet scrubbing (already the file's own existing architecture); CE-007 spun off for the resulting NaOCl storage gap | `Unknowns.md` §Chemistry |

**Resolved since the last refresh, removed from this table:** UNK-006
(Facility siting), RIP-001 (Prior-state archival), RIP-004 (Constitutional
violation detection latency), AP-012 / AP-016 (Human authority
availability / concurrent quarantine), GOV-011 (Spec Gates field scored
against wrong gate system), PC-001 through PC-005 (all — see Pending
Corrections above), ENV-DS-001 (bootstrap doctrine — ratified with a
bridge-authority exception clause, 2026-07-11).

**Parked, not open work:** Governance_Charter.md's External Design Lineage
amendment is drafted and ready but deliberately unratified — a considered
decision given GOV-011 and general system fragility, not neglect. No
expiry watch applies to it; it doesn't decay by sitting since it isn't
claiming to be true yet, only proposed.

⚠️ **Correction, 2026-07-29:** GOV-013 was previously listed here as
parked/unratified. That was wrong — it was **ratified 2026-07-19**
(`Admin/Governance_Charter.md` §Post-Exit Monitoring Doctrine, live
"STATUS: RATIFIED" note), eleven days before this file said otherwise.
The error traced back to two supporting files —
`Admin/Auditor_Protocols.md`'s metrics section and
`Admin/Repository_Integrity_Protocol.md`'s reversion mechanism —
still carrying stale "PROPOSED, NOT RATIFIED" / "once ratified"
language after the Charter ratified; both corrected same day as this
note. What's genuinely still open, confirmed by checking
Auditor_Protocols.md directly rather than assumed: the Semantic Drift
Score threshold is a literal `[Threshold TBD]` placeholder — human
governing authority still needs to set actual numeric values before
Post-Exit Monitoring can leave Phase 0 (manual) and become
automatable. That's a real gap, just not a ratification one.

---
