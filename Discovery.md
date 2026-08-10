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
    ├── Verification_Gates.md            — Canonical 6 document promotion gates
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
    ├── Nothingness_Theorem.md              — Philosophical substrate; foundational framework for salvage-first doctrine, distributed disagreement, and anti-entropy maintenance principles; Tier 0 / functionless by doctrine
    ├── Computational_Institutional_Reasoning.md — Formal theoretical paper; axiomatic state-machine model of institutional epistemics; Unknown Conservation, Governance Stability, Epistemic Debt Instability, and Institutional Memory Dominance theorems; non-linear Verification Algebra specification
    ├── CIR_Gov.md                          — CIR v2.0 predicate-kernel packaging; Proposed — Not Ratified; does not claim constitutional authority
    ├── Autonomy_Divergence_Protocol.md     — Graduated response to observed autonomous-subsystem divergence; Draft — PROPOSED NOT RATIFIED
    ├── Governance_Migration_Protocol.md    — Tier 1 Axiom amendment procedures
    ├── PROBE_INVOCATION.md                 — Copy-paste cold-start template for Mission Drift Review (AP-030); not doctrine, an operational prompt
    ├── Hardware_Diversity_Ladder.md         — Four-tier path to a hardware-diverse GOV-008 quorum; Draft, declarable-not-achieved
    ├── Progress_Log.md                      — Active notebook: rolling lessons/continuity tracking (2026-08-09)
    └── BATTERY_SEED.md                      — Frozen prompt block for a genuine AP-017 cold-session Adversarial Battery run

Automation/                                 — Scripts supporting verification and integrity checks
    ├── AUDIT_HARNESS.py                    — Primary automated verification script
    ├── audit_lib.py                        — Shared audit library functions
    ├── parser.py                           — Routing/registry parsing
    ├── integrity_check.py                  — Integrity verification script
    ├── cold_session_bundler.py             — Cold-session audit bundling
    ├── Cold_session_manifest.py            — Cold-session manifest generation
    ├── Colab_Launcher.py                   — Colab environment launcher
    ├── Colab_Integrity.py                  — Colab integrity checks
    └── Colab_cold_session.py               — Colab cold-session runner

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
    ├── Ops_Scope_Map.md                     — Per-file scope/dependency index for this folder (2026-08-08)
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
    ├── Tst_Scope_Map.md                     — Per-file scope/dependency index for this folder (2026-08-08)
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
    ├── Cha_Scope_Map.md                     — Per-file scope/dependency index for this folder (2026-08-08)
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
    ├── Rename_Registry.md                   — Frozen filename-change history, migrated from Discovery.md (2026-08-09)
    └── Logs/                                — Split-out full changelogs (condensed current versions remain in the main files)
        ├── Unknowns_Changelog.md           — Full version history for Unknowns.md pre-v4.29
        ├── Governance_Charter_Changelog.md — Full version history for Governance_Charter.md
        ├── Forge_Audit_Kit_Changelog.md    — Full version history for Forge_Audit_Kit.md
        ├── AUDIT_HARNESS_CHANGELOG.md      — Full version history for AUDIT_HARNESS.py
        ├── Auditor_Protocols_Logs.md       — Full version history + AP-series registration log
        ├── Progress_Log_Changelog.md       — Rotated entries from Admin/Progress_Log.md (2026-08-09)
        └── Discovery_Changelog.md          — Migrated correction-note history from Discovery.md (2026-08-09)
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
- `Architecture/Arc_Scope_Map.md` — created 2026-08-08 ✓, second folder in the rollout, same method; found one concrete stale cross-reference (`Forge_flow.md`'s UNK-008 claim, wrong since 2026-07-19) and one softer asymmetric-documentation gap (Forge_flow.md/Canonical_Terms.md vocabulary authority) — both fixed same-day in `Forge_flow.md` directly, per instruction to correct errors as found rather than only catalog them.
- `Operations/Ops_Scope_Map.md` — created 2026-08-08 ✓, third folder in the rollout; found and fixed two more instances of the same UNK-008 staleness pattern (`Gate_05_Separation_Thermal.md`, `Gate_06_Fabrication.md`) — three files total now corrected after one 2026-07-19 ownership reassignment. One look-alike (GF-003) checked and confirmed genuinely fine, not a fourth instance. No missing Scope Boundary sections in this folder.
- `Challenges/Cha_Scope_Map.md` — created 2026-08-08 ✓, fourth folder in the rollout. Structurally different from the prior three: two subtypes (Problem-Statement/Solution-Track) with genuinely different File State fields, and a folder-wide numbered-heading convention (`## 2. Scope Boundary`) that caused one extraction false-positive, caught and documented rather than misreported. No corrections needed this pass — no stale references, no missing sections. One genuine Blocking cross-reference surfaced (Water.md → Thermal_Systems.md TH-003).
- `Tests/Tst_Scope_Map.md` — created 2026-08-08 ✓, fifth folder in the rollout. No corrections needed, second folder clean in a row after Challenges/. Confirmed one forward reference (`Cognitive_Salvage_Layer.md` → `Operations/Leviathan.md`) as accurately-labeled-planned, not stale. Found one real unknown-tracking inconsistency (`Hydrologic_Resource_Cascade.md`'s partially-unregistered HR-003–010) worth a future decision, not fixed this pass. Noted `Field_Logs.md` is still empty as of this build — infrastructure exists, unused so far. Pending: Automation/ — the last folder, and structurally different (scripts, not doctrine).
- `Architecture/Characterization.md` — **[PLANNED]**, referenced as a forward dependency by `Closed_Loop_Feedstock.md`; not yet created.
- `Operations/Metals.md` — **[PLANNED]**, referenced as a forward dependency by `Closed_Loop_Feedstock.md`; not yet created.

**Routing.md completeness:** Verified complete as of 2026-08-04 (`Tests/Pyrolysis_Cascade.md` added, same date as file creation). Prior verification 2026-06-28 (`Tests/Cognitive_Salvage_Layer.md`, `Tests/Hydrologic_Resource_Cascade.md`, and `Admin/Computational_Institutional_Reasoning.md` added). Any gaps found on future audit passes are tracked as PC cluster entries in `Unknowns.md`.

This file's correction history (five entries, 2026-07-04 through
2026-08-09) has been migrated to `Archive/Logs/Discovery_Changelog.md` —
it had been accumulating as inline blockquotes mid-file since 2026-07-04
with no dedicated home, the same pattern that also affected the Rename
Registry and the Attention Required table (both fixed the same day). Full
correction history, including this migration itself, is there now. This
file's own "verified complete" and "refreshed" claims should still be
read as bounded by what was checked at the time — see that changelog for
why that caveat exists.

---

**Rename Registry migrated to `Archive/Rename_Registry.md` (2026-08-09)** — last entry dated 2026-06-11; didn't belong in a navigation-layer file. Stale filename references should be resolved against that file now.

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
| PC-006 | Six inline "Scope Map — X/" sections (Root Files, Admin/, Architecture/, Operations/Gates, Operations/Domain, Tests/, Challenges/) migrated out to five per-folder `*_Scope_Map.md` files, once all five existed and were verified against source | Resolved 2026-08-09 — see `Repository Maturity Snapshot`'s preceding correction note and each `*_Scope_Map.md`'s own Resolution Log |
| PC-007 | "Cross-Module Unknowns — Attention Required" table 19 versions stale; Rename Registry frozen since 2026-06-11, didn't belong in a navigation-layer file; `Unknowns.md`'s own "What vX.X Means" section stale by nine version bumps, violating its own Size Management Rule 1 | Resolved 2026-08-09 — table removed (superseded by `Unknowns.md`'s Active Index), Rename Registry migrated to `Archive/Rename_Registry.md`, lessons migrated to new `Admin/Progress_Log.md` |
| PC-008 | This file's own five-entry correction history (2026-07-04 through 2026-08-08) had accumulated as inline blockquotes mid-file since creation, with no dedicated home — same pattern as PC-007, caught by direct human review of the PC-007 patch rather than independently | Resolved 2026-08-09 — migrated verbatim to `Archive/Logs/Discovery_Changelog.md`, replaced with a short pointer |

---

## Repository Maturity Snapshot

| File | Status | Spec Gates | Highest Risk |
|------|--------|-----------|--------------|
| `Admin/Governance_Charter.md` | Draft | 6/6 vs. `Admin/Verification_Gates.md` — execution quality (see GOV-011, resolved 2026-07-05); promotion separately blocked by open unknowns (GOV-003, GOV-005) and Enforcement Checkpoint 2 — Bootstrap Paradox | Critical (GOV-013, GOV-015, GOV-018 — see `Archive/Logs/Governance_Charter_Changelog.md`; promotion-blocking risk unchanged from GOV-003/GOV-005) |
| `Admin/Ethical_Constraints.md` | Exploration | 0/6 | High |
| `Admin/Auditor_Protocols.md` | Draft | 4/6 (G1, G3, G4, G6 clear — G3 cleared 2026-08-03 via AP-017 Resolved; G5 conditional on cross-ref fixes below; G2 N/A — no physical/quantitative claims of its own) | High |
| `Admin/Forge_Audit_Kit.md` | Draft | 0/6 | — |
| `Admin/Verification_Gates.md` | Draft | 2/6 | High |
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
| `Admin/Hardware_Diversity_Ladder.md` | Draft — Proposed implementation reference only | 0/6 | unlabeled |
| `Admin/Progress_Log.md` | Active — Living Document | N/A — progression log, not a specification | N/A |
| `Admin/BATTERY_SEED.md` | Draft | N/A — operational prompt template, not a doctrine or specification claim | — |
| `Automation/AUDIT_HARNESS.py` | Active | — | — |
| `Automation/audit_lib.py` | Active | — | — |
| `Automation/parser.py` | Active | — | — |
| `Automation/integrity_check.py` | Active | — | — |
| `Automation/cold_session_bundler.py` | Active | — | — |
| `Automation/Cold_session_manifest.py` | Active | — | — |
| `Automation/Colab_Launcher.py` | Active | — | — |
| `Automation/Colab_Integrity.py` | Active | — | — |
| `Automation/Colab_cold_session.py` | Active | — | — |
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


## Scope Map — Root Files & Folder Pointers

> ⚠️ **Migration, 2026-08-09: six inline per-file Scope Map sections (Root Files, Admin/, Architecture/, Operations/Gates, Operations/Domain, Tests/, Challenges/ — roughly 456 lines, close to half this file's total length) removed and replaced with pointers to the five per-folder `*_Scope_Map.md` files built 2026-08-07/08.** Those files are now the better source: built by checking every file's actual Scope Boundary section directly against the live repository, all dated this week, versus this content, which had been patched incrementally since May and was where two more real gaps (`Hardware_Diversity_Ladder.md`, `BATTERY_SEED.md` missing from the tree; `Automation/` never broken out) were found the same day this migration happened. Four genuinely useful orientation callouts that existed only here — the Admin/ governance-tier hierarchy, Architecture/'s vocabulary-authority note and reading order, Operations/'s gate-flow sequence, and Challenges/'s "define problems, don't freeze solutions" principle — were checked against all five new files first, confirmed not duplicated, and preserved below rather than silently dropped. Root Files (`Routing.md`, `Unknowns.md`) have no dedicated Scope_Map file and are kept here in full, since creating a sixth file for two entries wasn't worth it. This migration was explicitly called reversible by human governing authority before being executed — nothing here was deleted outright; the full removed content remains recoverable from this file's own version history if ever needed. Prompted by a direct request to check whether Discovery.md content should migrate into the new per-folder files, immediately after the same request caught `Routing.md`'s far more serious divergence from reality (see that file's own 2026-08-08 Resolution Log entry) — worth naming plainly: that catch is why this migration got the scrutiny above rather than being executed as a quick trim.

Per-file scope detail (Purpose/Does/Does-Not, Upstream/Downstream, open-item flags) for each of the six folders now lives in that folder's own `*_Scope_Map.md` file, migrated out of this file 2026-08-09 once all five were built and verified (Automation/ deliberately excluded — code, not doctrine; see `Admin/Adm_Scope_Map.md`'s Resolution Log for that decision). This file previously held all of it inline; that content had grown to roughly half this file's total length and was increasingly duplicating, and drifting from, the more recently-verified per-folder files. Two root-level files have no dedicated Scope_Map — kept here since there are only two:

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

**Admin/** — see `Admin/Adm_Scope_Map.md`
> Governance tier hierarchy: Tier 1 (Governance_Charter + Ethical_Constraints) →
> Tier 2 (Auditor_Protocols) → Tier 3 (Forge_Audit_Kit) →
> Support layer (all others).

**Architecture/** — see `Architecture/Arc_Scope_Map.md`
> **Vocabulary authority:** `Architecture/Forge_flow.md` is the operational
> vocabulary standard. For any undefined operational term, consult
> `Architecture/Forge_flow.md` §Defined Terms before `Admin/Canonical_Terms.md`.
> **Reading order:** Forge_flow (vocabulary/gate logic) → Components (what must
> exist) → Facilities (where) → Geck_forge_seed (how to seed it) → Engineering
> (foundational principles) → Precision (build ceiling) → Mechanical_Structures →
> Thermal_Systems → Friction_Dynamics → Chemistry.

**Operations/** — see `Operations/Ops_Scope_Map.md`
> **Gate flow:** G01 → G02 → G03 → G04 → G05 → G06 → G07
> **Feedback loops:** G07→G02, G07→G06, G06→Components, G02→G04/G06
> Gate files define *how*; Forge_flow defines *what* and *when*.

**Challenges/** — see `Challenges/Cha_Scope_Map.md`
> Challenges/ files define problems and requirements. They do not freeze solutions.

**Tests/** — see `Tests/Tst_Scope_Map.md`

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

Removed 2026-08-09 — this table was 19 versions stale (last refreshed at
`Unknowns.md` v4.29, live file at v4.47+ by the time this was caught) and
duplicated content `Unknowns.md`'s own Active Index already provides,
filterable by Priority and Blocking status without needing a second copy
anyone has to remember to update. For the same information, go to
`Unknowns.md` directly. For the rolling "what's currently hot, what did
we just learn" content this table was trying to approximate, see
`Admin/Progress_Log.md`.
