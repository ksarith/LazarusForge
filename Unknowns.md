# Unknowns.md — Cross-Module Unknowns Global Index


**Full version history in `Unknowns_Changelog.md` (2026-07-19 cleanup pass, following the precedent set by `Admin/AUDIT_HARNESS_CHANGELOG.md` and `Admin/Forge_Audit_Kit_Changelog.md`; scrubbed to current-version-only 2026-07-28 — the "current plus last four in full" window was itself compressed further, since the Audit Trail below now carries the compressed record for every version back to v1.0, and the changelog carries full text for all of them. This block now keeps only the current version.)**

**Version 4.35 — 2026-07-31. CLF-006/CLF-009 ratified.**
`Challenges/Closed_Loop_Feedstock.md` §7 (contamination doctrine +
Material Certainty Manifest schema + validation logic) ratified by
human governing authority, adopted as one atomic unit as drafted.
CLF-006 and CLF-009 moved Open → In Progress here to match: doctrine
is now binding, numeric thresholds remain provisional pending §7.3's
instrumented-cycle validation. Mirrored same-day.

**Expiry Rule active — see `Admin/Canonical_Terms.md` §4 for the Cycle definition this rule now explicitly references (one calendar year default, not one audit pass — see CT-011). Protocol Performance metrics collecting.**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## Purpose

Cross-module unknowns index. Full entry detail lives in each owning file's sidecar. This file is the navigation layer only.

Module-specific unknowns → owning file sidecar
Cross-module unknowns → listed here, full entry in owning file
Pending corrections (task list) → PC cluster in this file
Programmatic URL routing → `Routing.md`
Navigation map and scope boundaries → `Discovery.md`
Formal axioms, theorems, and Verification Algebra backing CF-004, AP-006, and epistemic-debt doctrine → `Admin/Computational_Institutional_Reasoning.md`

**Cross-module dependencies** are owned by each file's Upstream/Downstream tables as of the v0.2 retrofit pass. See `Discovery.md` Scope Map for navigation.

**Finding an unknown's place in the architecture:** this file tracks *what* is unresolved; it does not carry Upstream/Downstream context for the owning file. If an unknown here seems disconnected from the rest of the system, check `Discovery.md`'s per-file Scope Map entry for the owning file — each entry lists Upstream/Downstream relationships and flags its highest-risk open unknowns with ⚠️. `Discovery.md` also carries a standing "Cross-Module Unknowns — Attention Required" table mirroring the highest-priority entries here; refresh it (and this pointer) whenever this file's version bumps materially change that set.

---

## What v4.35 Means

- **First ratification of the session's drafted doctrine.** §7 in `Challenges/Closed_Loop_Feedstock.md` — contamination doctrine, Material Certainty Manifest schema, and validation logic — moved from drafted-and-verified to formally binding, adopted as one atomic unit exactly as integrated on 2026-07-30, no last-minute changes.
- **Status change reflects what ratification actually does, not more than that.** CLF-006 and CLF-009 move Open → In Progress, not Open → Resolved. The doctrine is now binding (Payment via Specification), but every numeric threshold inside it stays provisional design-intent until hardened through the instrumented-cycle validation process the doctrine itself specifies. Ratifying the rulebook is not the same as validating the numbers in it.
- **No new content, no re-verification needed.** This version only updates status fields to match a governance decision already made against previously-verified text.

---

## Size Management Rules

These rules are enforced at every audit cycle opening:

1. **What vX.X Means — rolling single section.** Only the current version's What section is kept live. When a new version is cut, the prior What section is retired. Its content is already captured in the Audit Trail entry for that version. Keeping stacked What sections is redundant.

2. **Resolved entries leave the Active Index immediately.** Once an unknown is resolved, it is removed from the Active Index. Full resolution detail is recorded in the owning file's sidecar under Lessons Learned. This file carries no persistent archive of resolved entries — the Audit Trail's brief resolution notes are the only navigation-layer record maintained here. Active tables show Open, In Progress, and Reopened only.

3. **Compression trigger at 1,200 lines.** If this file exceeds 1,200 lines, a compression pass is mandatory before new entries are added. Compression scope: retire old What sections, verify all resolved actives have been removed from the index, confirm no archive accumulation has restarted.

4. **Audit Trail entries are to be in Unknowns_Changelog.md.** 

5. **Unknown Budget — floor on acknowledged unknowns.** A healthy repository maintains a nonzero active unknown count. If the active index drops below 10 open entries across all clusters, treat this as a signal of premature closure rather than epistemic health — trigger a meta-audit to verify recent resolutions were genuinely grounded and not closed under optimization pressure. The goal is not an empty index; it is an honest one.

6. **Reversion Protocol — when Resolved entries reopen.** A Resolved entry transitions to `Reopened` status when: (a) new empirical input contradicts the evidence that justified closure, (b) the resolution vehicle is shown to be insufficient or incorrect, or (c) a downstream dependency failure exposes the closure as premature. Reversion requires: an Epistemic Ledger entry in the owning file's sidecar documenting the contradictory evidence; an Audit Trail note in this file recording the reversion date and reason; and re-registration in the active index with status `Reopened` and Subtype `Active`. A closed unknown that reopens is not a failure — it is the falsification mechanism working correctly.

---

## Dependency Clusters

Critical and Blocking unknowns only. Shows which entries block others — not a full graph, just the load-bearing tier. Full entry detail in owning file sidecars. Updated when blocking relationships change.

**Trust & Integrity**
```
UNK-009 (External root-of-trust — cross-module)
├── GOV-003 (Integrity enforcement architecture)
├── GOV-005 (Constitutional stability unproven)
└── SEC-007a (External root-of-trust — constitutional layer)
        ├── SEC-007b (External root-of-trust — physical implementation; blocked pending SEC-007a)
        └── GMP-004 (Ratification authentication gap)
```

**Site & Operations**
```
FA-001 (Site not confirmed)
├── SP-006 (Emergency response — no site, no evacuation plan)
└── SD-UNK-004 (Host geology — no excavation without geomechanical assessment)
```

**Safety-Critical Processing**
```
EN-001 (Validated safety factors for salvaged materials)
└── All structural specification promotions blocked

WA-002 (Hazardous fraction identification)
└── All mixed-waste operations blocked

PL-001 (Halogenated polymer contamination)
└── CE-003 (Field polymer identification)
        └── All hot pyrolysis runs blocked

WW-005 (IFM detection)
└── All powered machinery contact with raw urban salvage blocked

CLF-004 (Closed_Loop_Feedstock.md — electrolytic chemical footprint undefined)
└── Blocks construction of any electrolytic/electrorefining pathway
        ├── Intersects PL-001, CE-003, WA-002 hazardous-material cluster
        └── CE-006 (Chemistry.md — chlorine containment undefined; blocks the candidate chlor-alkali pathway specifically)
```

**Autonomy & Hardware**
```
CF-001 (Hardware watchdog — τ=50ms defined, hardware validation pending)
└── EM-001 (Behavioral opacity detection threshold)
```

**Water**
```
TH-003 (Atmospheric moisture yield)
└── LW-005 deployment blocked (Living Waters atmospheric harvesting)
```

**Economics**
```
EV-001 (Forge power demand)
└── ECN-002 (Operating cost baseline)
        └── TR-001 (v1 profitability baseline)
```

**Epistemic / Governance**
```
AP-008 (Quarantine implementation)
└── AP-011 (Human fatigue escalation — depends on quarantine automation)

GOV-008 (Minimum quorum)
└── GOV-007 (Bootstrap governance — Genesis Phase exit condition)

AP-012 (Resolved 2026-07-03 — Human authority availability — autonomous degradation doctrine)
├── AP-016 (Resolved 2026-07-03 — Concurrent quarantine — co-resolved under AP-012 doctrine)
└── AP-011 (Human fatigue escalation — depends on AP-012's now-resolved doctrine)

AP-017 (Battery independence requirement)
└── Gate 3 clearance blocked until AP-017 reaches Provisional Spec
```

**Cognitive Salvage / Interaction Safety**
```
GH-009 (Emergent heuristic conflict — N² interaction scaling)
└── All heuristic co-deployment decisions blocked until
    Interaction Volume doctrine is defined
        └── GH-007 (Fidelity drift) — interaction testing must run
            against current machinery revision, not stale puzzle
            engine geometry
```

---

## Active Unknowns Index

### Energy & Power

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| EV-001 | Forge power demand uncharacterized | `Operations/Energy.md` | In Progress | Active | Blocking |
| EV-002 | Parasitic and thermal startup loads for biogas streams uncharacterized | `Operations/Energy.md` | In Progress | Active | Minor |
| EV-003 | Salvaged battery thermal containment and ventilation strategy undefined | `Operations/Energy.md` | In Progress | Active | Critical |

### Leviathan / Autonomy

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| LT-001 | Power envelope — no placeholder anchor | `Tests/Leviathan_testing.md` | Open | — | Blocking |
| LT-002 | Deep-ocean storage degradation | `Tests/Leviathan_testing.md` | Open | — | Blocking |
| LT-003 | Autonomy architecture unspecified | `Tests/Leviathan_testing.md` | Open | — | Blocking |
| LT-004 | Trust model mechanism undefined | `Tests/Leviathan_testing.md` | Open | — | Blocking |
| LT-005 | Priority propagation — no mechanism | `Tests/Leviathan_testing.md` | Open | — | Blocking |
| LT-006 | Ethical log survival at depth | `Tests/Leviathan_testing.md` | Open | — | Non-blocking |
| LT-007 | Corrective action authorization mechanism for a peer unit undefined — Astroid-miner cross-repo convergence, candidate ref: Fleet Consensus Validation | `Tests/Leviathan_testing.md` | Open | — | Major |

### Gate Logic & Triage

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| FL-001 | Gate logic determinism | `Architecture/Forge_flow.md` | In Progress | Active | Blocking |
| FL-002 | Reduction module unassigned | `Architecture/Forge_flow.md` | Open | — | Major |
| TS-001 | "Sufficient for forge duty" threshold | `Operations/Gate_02_Triage.md` | In Progress | Active | Blocking |
| TS-002 | Contamination routing protocol | `Operations/Gate_02_Triage.md` | Open | — | Blocking |
| TS-003 | Gate determinism (downstream) | `Operations/Gate_02_Triage.md` | In Progress | Active | Blocking |
| CO-001 | Graduation Rule detection circularity | `Architecture/Components.md` | In Progress | Active | Blocking |
| CO-002 | Metrology precision thresholds | `Architecture/Components.md` | Open | — | Minor |

### Ethics & Governance

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| EC-001 | "Sufficient confidence" threshold | `Admin/Ethical_Constraints.md` | Open | — | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Admin/Ethical_Constraints.md` | Open | — | Blocking |
| EC-003 | Human escalation path | `Admin/Ethical_Constraints.md` | In Progress | Active | Blocking |
| EC-004 | Governance failure modes lifecycle | `Admin/Ethical_Constraints.md` | In Progress | Active | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Admin/Ethical_Constraints.md` | In Progress | Active | Blocking |
| EC-006 | Ethical log survival under unit loss | `Admin/Ethical_Constraints.md` | Open | — | Non-blocking |
| EC-007 | Governance fail-safe | `Admin/Ethical_Constraints.md` | In Progress | Active | Blocking |
| EC-008 | Inferred authorization doctrine undefined | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-009 | Human authority conflict resolution undefined | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-010 | Jurisdiction conflict hierarchy undefined — `Admin/Environmental_Constraints.md` exists (created 2026-06-19) and is the declared convergence junction via its own ENV-003 entry; deferred to that file's v1-transition resolution timeline | `Admin/Ethical_Constraints.md` | In Progress | Vehicle | Minor |
| EC-011 | Human governance adversary model undefined | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-012 | Epistemic spoofing via hardware/firmware tampering | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-013 | Safe-state descent sequence undefined for active hazardous processes during governance failure | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-014 | Toxic material encapsulation standard undefined | `Admin/Ethical_Constraints.md` | Open | — | Major |
| EC-015 | Right-to-repair / anti-circumvention legal boundary undefined per jurisdiction | `Admin/Ethical_Constraints.md` | Open | — | Major |
| GOV-001 | Governance migration mechanics incompletely operationalized — `Admin/Governance_Migration_Protocol.md` created; not yet audited against charter constraints | `Admin/Governance_Charter.md` | In Progress | Vehicle | Major |
| GOV-002 | Provenance operationalization immature | `Admin/Governance_Charter.md` | In Progress | Active | Major |
| GOV-003 | Integrity enforcement architecture undefined | `Admin/Governance_Charter.md` | In Progress | Active | Critical |
| GOV-004 | Escalation calibration partially subjective | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-005 | Long-term constitutional stability unproven | `Admin/Governance_Charter.md` | Open | — | Critical |
| GOV-006 | Human override authenticity validation undefined — GOV-006-A: interim authentication rules are declarative-only; zero automated resistance until Security_Protocols.md reaches Provisional Spec | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-007 | Bootstrap governance authority initialization undefined | `Admin/Governance_Charter.md` | In Progress | Active | Major |
| GOV-008 | Minimum hardware and agent quorum for bootstrap compliance | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-009 | Bounded framework for external resource consumption and environmental interaction — `Admin/Environmental_Constraints.md` created as resolution vehicle | `Admin/Governance_Charter.md` | In Progress | Vehicle | Major |
| GOV-010 | Jurisdictional and regulatory compliance friction for physical forge deployment — cross-ref EC-010; `Admin/Environmental_Constraints.md` created as convergence resolution vehicle | `Admin/Governance_Charter.md` | In Progress | Vehicle | Minor |
| GOV-012 | Constitutional Stagnation Decay — no automated demotion mechanism for unknowns that remain Open past the Cycle threshold without substantively updated Resolution Path; threshold formally deferred to zero cycles 2026-07-19 (no elapsed operational time to derive a real value against), not neglected — re-derivation method already specified for when a site reaches operational launch | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-014 | Governance complexity ceiling undefined | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-015 | Constitutional interpretation capture — aggregate reinterpretation via subordinate doctrine volume, distinct from single-file case GMP-005 covers | `Admin/Governance_Charter.md` | Open | — | Critical |
| GOV-016 | Governance pruning doctrine absent — no reward or process for retiring obsolete doctrine | `Admin/Governance_Charter.md` | Open | — | Minor |
| GOV-017 | Institutional governance stagnation — document-level, distinct from GOV-012's unknown-level stagnation | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-018 | Governance fork reconciliation undefined | `Admin/Governance_Charter.md` | Open | — | Critical |
| GOV-019 | Conflicting authenticated human override arbitration undefined | `Admin/Governance_Charter.md` | Open | — | Major |
| GOV-020 | Governance cost metric undefined | `Admin/Governance_Charter.md` | Open | — | Minor |
| GOV-021 | Autonomy Divergence Protocol formal registration — reserved as candidate ID by `Admin/Autonomy_Divergence_Protocol.md` since 2026-07-19; not yet formally registered in `Admin/Governance_Charter.md`'s own sidecar. Sub-unknowns GOV-021b (Detection Criteria calibration) and GOV-021c (multi-agent coordinated divergence detection) tracked within that file, not yet independently registered here either. | `Admin/Governance_Charter.md` | Open | Vehicle | Major |
| GOV-022 | Reversibility as a cross-cutting operating principle — placement undecided among a new Operating Principles subsection, doctrine in `Admin/Auditor_Protocols.md`, or rejection as redundant with existing P-1/Q-3 | `Admin/Governance_Charter.md` | Open | — | Minor |
| SEC-001 | Quorum recovery under terminal partition | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-002 | Key revocation doctrine undefined | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-003 | Key rotation period undefined | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-004 | Key lifecycle doctrine incomplete | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-005 | Trusted initialization environment undefined — Design Lineage: PAT-003 | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-006 | Timestamp trust under degraded clock | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-007a | External root-of-trust — constitutional requirements for the anchor (owning layer: Admin) — vertically split from SEC-007 2026-07-02 — Design Lineage: PAT-001 | `Admin/Security_Protocols.md` | Open | — | Critical |
| SEC-007b | External root-of-trust — physical hardware implementation, e.g. offline HSM/EEPROM (owning layer: Operations) — vertically split from SEC-007 2026-07-02; blocked pending SEC-007a — Design Lineage: PAT-002 | `Admin/Security_Protocols.md` | Open | — | Critical |
| SEC-008 | Signature replay protection mechanism undefined | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-009 | Compromise detection criteria undefined — blocks revocation trigger definition | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-010 | Cryptographic algorithm migration doctrine undefined | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-011 | Long-duration cryptographic continuity undefined — entropy exhaustion, operator succession, algorithm migration at Leviathan-class timescales — Design Lineage: PAT-004 (Observe status; 2-cycle Expiry Watch) | `Admin/Security_Protocols.md` | Open | — | Major |
| SEC-012 | Asymmetric cryptographic execution overhead on resource-constrained salvaged silicon (8/16-bit MCUs) — risk of localized DoS or protocol bypass under Logic-Zero recovery; cross-ref Operations/Electronics.md EL-006 | `Admin/Security_Protocols.md` | Open | — | Major |

### Governance & Verification

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| AP-002 | Override vs. immutability boundary — EF-0.4/EF-0.5 progress; Ethical_Constraints.md confirmation pending | `Admin/Auditor_Protocols.md` | In Progress | Vehicle | Major |
| AP-003 | Audit trail schema | `Admin/Auditor_Protocols.md` | Open | — | Minor |
| AP-004 | Cross-auditor disagreement resolution — three-tier framework defined | `Admin/Auditor_Protocols.md` | In Progress | Vehicle | Major |
| AP-005 | Verification termination threshold — four necessary conditions defined | `Admin/Auditor_Protocols.md` | In Progress | Vehicle | Major |
| AP-007 | Repository integrity and doctrine lineage — EF-0.3/EF-0.2 L3 doctrine layer; enforcement gap in Security_Protocols.md | `Admin/Auditor_Protocols.md` | In Progress | Vehicle | Major |
| AP-008 | Technical implementation of quarantine actions undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-010 | Physical test harness integration with epistemic grounding layer undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-011 | Automated arbitration deadlock and human fatigue escalation | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-013 | Unknown closure authority undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-017 | Adversarial Battery independence requirement undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-018 | Saturation threshold hysteresis and smoothing undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-019 | Semantic convergence metrics for unknown resolution undefined | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-024 | Human attestation provenance insufficiently granular — "human-directed" collapses at least five distinguishable review levels into one label | `Admin/Auditor_Protocols.md` | Open | — | Major |
| AP-029 | 10-Entry Rule tripped by the sidecar's own open-count, unaddressed | `Admin/Auditor_Protocols.md` | Open | — | Minor |
| AP-030 | Mission Drift Review N=5 ratification-velocity threshold unvalidated pending first three probe cycles | `Admin/Auditor_Protocols.md` | Open | — | Minor |
| CIR-001 | Physical Grounding Telemetry Mapping Interface undefined — γ1–γ4 predicates aspirational pending harness Phase 2; renamed 2026-07-28 from a colliding local "GOV-008" (see `Admin/Forge_Audit_Kit.md`'s Governance Sidecar ID Reference); registration gap closed 2026-07-29 — this tracker existed in `Admin/Computational_Institutional_Reasoning.md`'s own sidecar since the rename but was never mirrored here, despite its sibling tracker CF-004 (same file's Active Trackers list) being registered | `Admin/Computational_Institutional_Reasoning.md` | Open | — | Critical |
| RIP-002 | AUDIT_HARNESS.py Phase 1 checks not yet implemented | `Admin/Repository_Integrity_Protocol.md` | Open | — | Major |
| RIP-003 | Violation incident log location undefined | `Admin/Repository_Integrity_Protocol.md` | Open | — | Major |
| RIP-005 | Security_Protocols.md Phase 3 dependency — file exists at v0.5; cryptographic implementation not yet operational | `Admin/Repository_Integrity_Protocol.md` | In Progress | Vehicle | Major |
| RIP-006 | Archive retention policy — partially resolved; GitHub indefinite retention satisfies Tier 1 requirement; /Archive/ directory content retention pending distillate architecture | `Admin/Repository_Integrity_Protocol.md` | In Progress | Vehicle | Minor |
| RIP-007 | Integrity incident ownership undefined | `Admin/Repository_Integrity_Protocol.md` | Open | — | Major |
| RIP-009 | No cross-file correlation mechanism for coordinated minor integrity drift | `Admin/Repository_Integrity_Protocol.md` | Open | — | Minor |
| RIP-010 | Protocol never deliberately tested against a planted violation — Protocol Validation / Integrity Fire Drill specified, first pass not yet run | `Admin/Repository_Integrity_Protocol.md` | Open | — | Minor |
| CT-001 | Legacy script integration name mapping | `Admin/Canonical_Terms.md` | Open | — | Minor |
| CT-002 | Component Library Schema standard undefined | `Admin/Canonical_Terms.md` | Open | — | Major |
| CT-003 | Dependency_Priority_Map.md needed before v1 | `Admin/Canonical_Terms.md` | Open | — | Minor |
| CT-004 | Trusted initialization environment definition | `Admin/Canonical_Terms.md` | Open | — | Major |
| CT-005 | Ethical and authorization term placeholders pending canonicalization | `Admin/Canonical_Terms.md` | Open | — | Major |
| CT-006 | Circular dependency detection undefined | `Admin/Canonical_Terms.md` | Open | — | Major |
| CT-007 | ID namespace allocation doctrine undefined — narrower EC→ECN rename sub-issue resolved 2026-07-06; the broader namespace-allocation doctrine gap it was meant to cover remains genuinely Open, confirmed directly against source | `Admin/Canonical_Terms.md` | Open | — | Major |
| CT-008 | HF-001 Heuristic Failure canonicalization status — cross-file consistency tracking | `Admin/Canonical_Terms.md` | In Progress | Vehicle | Minor |
| CT-009 | Grain System implementation consistency — tracks Canonical_Terms.md definition against ST-001/ST-002 implementation | `Admin/Canonical_Terms.md` | Open | — | Minor |
| CT-010 | Verification Gate / Enforcement Checkpoint rename propagation — confirm no file still cites unqualified "Gate N" for Governance_Charter.md's renamed checkpoints, outside Verification_Gates_LF.md and Operations/Gate_01–07 | `Admin/Canonical_Terms.md` | In Progress | Vehicle | Major |

### Engineer Protocols

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| EP-001 | Validation of Pragmatic Question Framework | `Admin/Engineer_Protocols.md` | Open | — | Major |
| EP-002 | AI vs Human Protocol optimization | `Admin/Engineer_Protocols.md` | Open | — | Minor |
| EP-003 | Integration mapping with Auditor_Protocols and Cognitive_Frameworks | `Admin/Engineer_Protocols.md` | Open | — | Major |
| EP-004 | Engineering authority boundary — tier relationship to Ethical_Constraints.md and Auditor_Protocols.md now explicit in Engineering.md File Purpose | `Admin/Engineer_Protocols.md` | Open | — | Major |
| EP-005 | Acceptable risk threshold undefined — partial resolution via Safety_Protocols.md; full threshold definition still open | `Admin/Engineer_Protocols.md` | Open | — | Major |
| EP-006 | Unknown lifecycle integration undefined | `Admin/Engineer_Protocols.md` | Open | — | Major |

### Engineering & Structures

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| EN-001 | Validated safety factors for salvaged materials — blanket 6×+ floor replaced 2026-07-05 with differentiated per-material interim table (steel/aluminum/timber/unidentified); still Internally Derived, no destructive test data yet | `Architecture/Engineering.md` | In Progress | Active | Critical |
| EN-002 | Deployment-specific environmental load data not compiled | `Architecture/Engineering.md` | Open | — | Major |
| EN-003 | Materials database for salvaged alloy identification | `Architecture/Engineering.md` | Open | — | Major |
| EN-004 | High-performance low-tech fabrication methods | `Architecture/Engineering.md` | Open | — | Minor |
| EN-005 | Verification testing protocols for structural claims | `Architecture/Engineering.md` | Open | — | Major |
| EN-006 | Advanced engineering section drift risk (topology, composites) | `Architecture/Engineering.md` | Open | — | Minor |
| EN-007 | Dissimilar material junction fatigue profiles undefined | `Architecture/Engineering.md` | Open | — | Major |
| ME-001 | Vibration resonance mapping on mismatched salvaged rails | `Architecture/Mechanical_Structures.md` | Open | — | Major |
| ME-002 | Pneumatic purge volume requirements vs. Air Scrubber capacity | `Architecture/Mechanical_Structures.md` | Open | — | Minor |
| ME-003 | Structural creep and damp-fill aging not characterized | `Architecture/Mechanical_Structures.md` | Open | — | Major |
| ME-004 | Calibration values not separated from doctrine sections | `Architecture/Mechanical_Structures.md` | Open | — | Minor |

*EN-001 is Blocking — no structural specification in any file may be promoted without validated safety factors for salvaged materials.*

### Chemistry & Electrochemistry

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| CE-001 | Galvanic corrosion rates for salvaged mixed-metal assemblies not characterized | `Architecture/Chemistry.md` | Open | — | Major |
| CE-002 | Oxide burden effect on Spin Chamber output quality not quantified | `Architecture/Chemistry.md` | Open | — | Major |
| CE-003 | Field polymer identification reliability not validated for mixed salvage stream | `Architecture/Chemistry.md` | Open | — | Critical |
| CE-004 | Chemical Operator Minimum Competency — Appendix A created in Chemistry.md | `Architecture/Chemistry.md` | In Progress | Vehicle | Major |
| CE-005 | Solution chemistry and precipitation doctrine — §2.3 expanded to full doctrine 2026-07-31; quantitative Ksp validation and sludge-disposal routing to GR-003 remain (GR-003 itself unassigned in `Operations/Gate_03_Reduction.md`) | `Architecture/Chemistry.md` | In Progress | — | Major |
| CE-006 | Chlorine gas containment doctrine — mechanism corrected 2026-07-19 to `Operations/Air_Scrubber.md` Stage D caustic scrubbing (was incorrectly directed to Stage E KMnO₄ bed, which does not target Cl₂); quantitative scrubber chemistry and detection/alarm thresholds added 2026-07-31 — cross-ref `Challenges/Closed_Loop_Feedstock.md` CLF-004 (candidate pathway this blocks) and `Admin/Ethical_Constraints.md` §Toxic and Hazardous Material Handling. Sealed vessel design and real flow-rate calibration remain open (hardware gap, same category as CLF-003). | `Architecture/Chemistry.md` | Open | — | Critical |
| CE-007 | Sodium hypochlorite (NaOCl) byproduct storage, stability, and reuse doctrine — full doctrine (decomposition pathways, acidification-to-Cl₂ risk, storage/segregation, potable-water reuse pathway) added 2026-07-31; quantitative sizing depends on CE-006's hardware gap | `Architecture/Chemistry.md` | In Progress | — | Major |
| CE-008 | Dilution doctrine (§2.4, added 2026-07-31) competency validation not folded into CE-004's existing Appendix A checklist — registered separately to avoid colliding with the already-existing CE-004 (Chemical Operator Minimum Competency) | `Architecture/Chemistry.md` | Open | — | Minor |

*CE-003 is a safety-critical prerequisite before first hot pyrolysis run — cross-references PL-001.*
*CE-006 is Critical — blocks `Challenges/Closed_Loop_Feedstock.md`'s CLF-004 candidate acid-sourcing pathway until a sealed-vessel/scrubbing design is defined.*
*CE-007 is not Blocking for CE-006's containment resolution, only for the value-recovery framing — see `Architecture/Chemistry.md` for detail.*

### Thermal Systems

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| TH-001 | Forge-specific heat pump sizing doctrine not yet developed | `Architecture/Thermal_Systems.md` | Open | — | Major |
| TH-002 | TEG harvest yield at Gate_05 exterior not characterized | `Architecture/Thermal_Systems.md` | Open | — | Minor |
| TH-003 | Atmospheric moisture yield under deployment conditions not measured | `Architecture/Thermal_Systems.md` | Open | — | Major |
| TH-004 | Salvaged Peltier device characterization protocol not defined | `Architecture/Thermal_Systems.md` | Open | — | Major |
| TH-005 | Thermal interface material doctrine undefined | `Architecture/Thermal_Systems.md` | Open | — | Major |
| TH-006 | TEG absolute efficiency range not validated for salvage stock | `Architecture/Thermal_Systems.md` | Open | — | Minor |

*TH-003 is Blocking for Living Waters deployment. Non-blocking for all other Forge operations.*

### Friction Dynamics

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| FD-001 | Gate_04 centrifugal separation RPM data not linked to Stokes settling doctrine | `Architecture/Friction_Dynamics.md` | Open | — | Major |
| FD-002 | Air Scrubber duct velocity profile not characterized per capture stage | `Architecture/Friction_Dynamics.md` | Open | — | Major |
| FD-003 | Salvaged bearing L10 life estimation protocol not defined | `Architecture/Friction_Dynamics.md` | Open | — | Major |
| FD-005 | Fluid-Structure Interaction (FSI) not formally bridged | `Architecture/Friction_Dynamics.md` | Open | — | Major |

### Cognitive Frameworks

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| CF-001 | Hardware watchdog minimum standard — parameters defined, hardware validation pending | `Operations/Electronics.md` | In Progress | Active | Critical |
| CF-002 | Correlated AI failure modes — test protocol defined, swarm deployment pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Vehicle | Major |
| CF-003 | Identity continuity during split-brain — doctrine defined, threshold calibration pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Vehicle | Major |
| CF-004 | Epistemic debt measurement mechanism — formally defined via `Admin/Computational_Institutional_Reasoning.md` §5.4 (Lyapunov-stable trigger), 2026-07-28; numeric calibration ($\theta_p$, $\varepsilon_{\text{triage}}$, $\varepsilon_{\text{exit}}$, $N$) remains open; dependency surface now includes Section IV (Confidence Collapse States, revised 2026-07-28), Triage Posture, promotion suspension — priority raised Minor → Major 2026-07-26, held at Major | `Architecture/Cognitive_Frameworks.md` | Open | — | Major |
| CF-005 | Adversarial audit loop convergence criteria undefined — Skeptic/Engineer cycle has no formal termination condition, named in body text but previously untracked | `Architecture/Cognitive_Frameworks.md` | Open | — | Minor |

*CF-001 remains Blocking — parameters are Analogous confidence pending first hardware prototype validation.*

### Emergence

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| EM-001 | Behavioral opacity detection threshold — depends on CF-001 resolution | `Challenges/Emergence.md` | Open | — | High |
| EM-002 | Correlated failure detection in multi-agent consensus | `Challenges/Emergence.md` | Open | — | High |
| EM-003 | Gradual autonomy transition detection — no current sensor doctrine | `Challenges/Emergence.md` | Open | — | Medium |
| EM-004 | Governance substrate integrity under emergent agent access — mirrors GOV-003, SEC-007a | `Challenges/Emergence.md` | Open | — | Critical |

*EM-001 depends on CF-001 resolution.*
*EM-004 is Critical — no fast resolution path; architectural decision above repository level required.*

### Energy Scarcity

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| ES-001 | Community-facing energy surplus routing mechanism undefined — load-bearing for the file's Long-Term Objective | `Challenges/Energy_Scarcity.md` | Open | — | Major |
| ES-002 | Economic legibility threshold for community-facing systems undefined — feeds `Admin/Economics.md` EC-002 | `Challenges/Energy_Scarcity.md` | Open | — | Major |
| ES-003 | Intermittency communication doctrine undefined — no standard for representing duty-cycle limits to a relying community | `Challenges/Energy_Scarcity.md` | Open | — | Minor |

*New cluster, registered 2026-07-12 alongside `Challenges/Energy_Scarcity.md`'s creation (v0.1, not yet Gate 1-reviewed). ES-001 is the load-bearing unknown — without a surplus-routing mechanism, the file's "energy-neutral or net-contributor to the surrounding community" objective remains aspirational rather than actionable.*
*`ES-` prefix chosen to avoid collision with `Operations/Energy.md`'s `EV-` prefix, `Architecture/Engineering.md`'s `EN-` prefix, and `Admin/Economics.md`'s `EC-` prefix.*

### Waste

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| WA-001 | Embedded complexity preservation metric undefined | `Challenges/Waste.md` | Open | — | Major |
| WA-002 | Hazardous fraction identification reliability — no validated identification protocol | `Challenges/Waste.md` | Open | — | Critical |
| WA-003 | Informal sector integration doctrine undefined | `Challenges/Waste.md` | Open | — | Major |
| WA-004 | Negative-value waste fraction disposal doctrine undefined | `Challenges/Waste.md` | Open | — | Critical |

*WA-002 and WA-004 are Critical — no sustained mixed-waste operations without hazardous fraction identification and negative-value disposal doctrine.*

### Biofouling

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| BF-001 | Ultrasonic antifouling energy budget not characterized | `Challenges/Biofouling.md` | Open | — | Major |
| BF-002 | Biomimetic surface topography durability not characterized | `Challenges/Biofouling.md` | Open | — | Major |
| BF-003 | Regional fouling rate differential — no maintenance cycle calibration | `Challenges/Biofouling.md` | Open | — | Major |
| BF-004 | Shed panel reef substrate viability — toxin leach unvalidated | `Challenges/Biofouling.md` | Open | — | Major |

### Planned Obsolescence

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| PO-001 | Firmware re-baselining legal boundary doctrine — operationally untested | `Challenges/Planned_Obsolescence.md` | Open | — | Major |
| PO-002 | Potting compound removal chemistry — no validated protocol | `Challenges/Planned_Obsolescence.md` | Open | — | Major |
| PO-003 | Proprietary connector adapter coverage — no systematic inventory | `Challenges/Planned_Obsolescence.md` | Open | — | Minor |
| PO-004 | Community re-baselining skill transfer standard undefined | `Challenges/Planned_Obsolescence.md` | Open | — | Major |

### Water Scarcity

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| WS-001 | Optimal energy harvesting for high-humidity low-kinetic environments | `Challenges/Water.md` | Open | — | Major |
| WS-002 | Heavy metal stabilization chemistry for tropical climates | `Challenges/Water.md` | Open | — | Major |
| WS-003 | Stratification diminishing returns threshold | `Challenges/Water.md` | Open | — | Major |
| WS-004 | Community adoption and maintenance protocol undefined | `Challenges/Water.md` | Open | — | Major |

*TH-003 remains the Blocking unknown for LW-005 atmospheric harvesting.*

### Living Waters

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| LW-UNK-001 | Volatile co-distillation characterization for LW-001 | `Tests/Living_Waters.md` | Partially Addressed — LW-TEST-102 defines test approach; empirical validation pending | — | Critical |
| LW-UNK-002 | Membrane survivability for LW-003 at sustained operational depth | `Tests/Living_Waters.md` | Open | — | Major |
| LW-UNK-003 | Lumen structural integrity limits for LW-003 under deep pressure | `Tests/Living_Waters.md` | Partially Addressed — implosion threshold characterized; salvage material validation pending | — | Critical |
| LW-UNK-004 | Biofouling rate characterization for LW-003 in target deployment zones | `Tests/Living_Waters.md` | Open | — | Major |
| LW-UNK-005 | Energy balance: LW-001 with MVR vs. LW-002 surface RO | `Tests/Living_Waters.md` | Partially Addressed — energy profiles established; empirical validation pending | — | Major |
| LW-UNK-006 | Salvage-compatible membrane sourcing for any RO pathway | `Tests/Living_Waters.md` | Open | — | Major |
| LW-UNK-007 | Draw solution regeneration chemistry and energy cost for LW-007 | `Tests/Living_Waters.md` | Open | — | Major |
| LW-UNK-008 | Site characterization → pathway selection decision framework | `Tests/Living_Waters.md` | Declared — formal framework not yet written | — | Minor |
| LW-UNK-009 | Salvage sourcing path for fence-mounted AWG variant (LW-005a) | `Tests/Living_Waters.md` | Open | — | Minor |

*LW-UNK-001 CRITICAL — distillate may be concentrated toxin stream; blocks potable output claim from LW-001.*
*LW-UNK-003 CRITICAL — 4.9 MPa net crush load at 500 m; standard salvage tubing will fail.*

### Trophic Forge

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| TF-001 | Phototaxis yield at Forge scale unvalidated | `Tests/Trophic_Forge.md` | Open | — | Critical |
| TF-002 | Prior art search incomplete | `Tests/Trophic_Forge.md` | Partially Addressed | — | Major |
| TF-003 | Fish nutrient output at Forge stocking density uncharacterized | `Tests/Trophic_Forge.md` | Open | — | Major |
| TF-004 | Fish species selection not determined | `Tests/Trophic_Forge.md` | Open | — | Major |
| TF-005 | Phytoremediation loop closure unvalidated | `Tests/Trophic_Forge.md` | Open | — | Major |
| TF-006 | Non-target insect capture rate — Ethical_Constraints escalation candidate | `Tests/Trophic_Forge.md` | Partially Addressed — draft nocturnal protocol defined; empirical validation pending | — | High — Ethical_Constraints escalation candidate |
| TF-007 | Single node failure propagation uncharacterized | `Tests/Trophic_Forge.md` | Open | — | Major |
| TF-008 | Minimum viable loop scale unknown | `Tests/Trophic_Forge.md` | Open | — | Major |
| TF-009 | Interaction boundary with Living_Waters.md at pond node undefined | `Tests/Trophic_Forge.md` + `Tests/Living_Waters.md` | Open | — | Minor |
| TF-010 | Seasonal and climatic variability uncharacterized | `Tests/Trophic_Forge.md` | Open | — | Major |

*TF-001 Critical/Blocking — entire organizing principle rests on phototaxis yield.*
*TF-006 ethical unknown — halt expansion if non-target capture threshold cannot be bounded.*

### Solar Descent

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| SD-UNK-001 | Flux delivery at Forge-scale salvage fiber unvalidated | `Tests/Solar_Descent.md` | Open | — | Critical |
| SD-UNK-002 | Achievable underground temperature at Forge build quality unknown | `Tests/Solar_Descent.md` | Open | — | Critical |
| SD-UNK-003 | Molten tin termination (SD-001a) viability unconfirmed | `Tests/Solar_Descent.md` | Open | — | Minor |
| SD-UNK-004 | Host geology fracturing threshold unknown — blocks all excavation | `Tests/Solar_Descent.md` | Open | — | Critical — parallels FA-001 |
| SD-UNK-005 | Working fluid salvage sourcing for SD-002 unconfirmed | `Tests/Solar_Descent.md` | Open | — | Major |
| SD-UNK-006 | Parasitic pump load for SD-002 uncharacterized | `Tests/Solar_Descent.md` | Open | — | Major |
| SD-UNK-007 | Diurnal chamber self-discharge rate unknown — seasonal loss discharged to Trajectories | `Tests/Solar_Descent.md` | Open | — | Minor |
| SD-UNK-008 | Stirling engine salvage availability at required scale unconfirmed | `Tests/Solar_Descent.md` | Resolved | — | Discharge via Trajectory |
| SD-UNK-009 | Excavation feasibility at Forge scale unassessed | `Tests/Solar_Descent.md` | Resolved | — | Discharge via Trajectory (‖ FA-001) |
| SD-UNK-010 | Waste heat cascade interface with Living_Waters.md undefined | `Tests/Solar_Descent.md` + `Tests/Living_Waters.md` | Resolved | — | Payment via Specification |
| SD-UNK-011 | Receiver material survivability uncharacterized | `Tests/Solar_Descent.md` | Open | — | Minor |
| SD-UNK-012 | Dust and alignment stability uncharacterized | `Tests/Solar_Descent.md` | Resolved | — | Vehicle: SD-TEST-105 |
| SD-UNK-013 | Surface Collection Bootstrap & Tracking Power Source — cold-start / low-thermal-state tracking power undefined | `Tests/Solar_Descent.md` | Resolved | — | Payment via Specification |
| SD-UNK-014 | Shaft Penetration Sealing & Thermal Isolation — chamber inert-gas / shaft interface undefined | `Tests/Solar_Descent.md` | Resolved | — | Payment via Specification (narrow) |
| SD-UNK-015 | Light-well vs. fiber comparative flux delivery unassessed — parallel arm to SD-TEST-101; priority claim previously untracked | `Tests/Solar_Descent.md` | Resolved | — | Vehicle: SD-TEST-106 |

*SD-UNK-004 carries same governance weight as FA-001 — no excavation without geomechanical assessment.*
*SD-UNK-002 Critical — all power conversion planning must assume conservative lower bound (~500°C).*
*Phase 1 Resolution Pass (2026-07-30) closed SD-UNK-008/009/010/012/013/014/015 with logged pathways (Trajectory/Specification/Vehicle, per `Tests/Solar_Descent.md` Resolution Log) and demoted SD-UNK-003/007/011 to Minor. Open set: 001, 002, 003, 004, 005, 006, 007, 011 (8 total) — matches `Tests/Solar_Descent.md` File State exactly.*

### Critical Minerals

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| CM-001 | Real-time material assay integration undefined | `Challenges/Critical_Minerals.md` | Open | — | Major |
| CM-002 | Acid leach reagent recovery and closed-loop doctrine undefined | `Challenges/Critical_Minerals.md` | Open | — | Critical |
| CM-003 | Functional substitute performance floor undefined | `Challenges/Critical_Minerals.md` | Open | — | Major |
| CM-004 | Urban ore database coverage insufficient | `Challenges/Critical_Minerals.md` | Open | — | Major |

*CM-002 Critical — no hydrometallurgical processing before closed-loop reagent recovery specified. Cross-ref CLF-004 (`Challenges/Closed_Loop_Feedstock.md`) — same underlying acid-reclamation problem, different material stream.*

### Return to Eden

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| RE-UNK-001 | Eden Index variable measurement protocols undefined — $B_d$, $\Omega_r$, $\eta_{sys}$, $W_{out}$, $\Phi_{ext}$ all lack instrument specifications, calibration procedures, and sampling intervals. **Cross-ref CLF-005 (Resolved 2026-07-07)** — confirmed as a different, unrelated variable (renamed to $\Delta_{sc}$ in `Challenges/Closed_Loop_Feedstock.md` v0.6.0); this file's own $\Phi_{ext}$ was correctly scoped and required no change. The measurement-protocol gap named in this entry is unaffected by that resolution and remains fully open. | `Challenges/Return_To_Eden.md` | Open | Active | Blocking (Tier I gate) |
| RE-UNK-002 | 98.4% closed-loop material cycle threshold provenance unverified — empirical target, thermodynamic bound, or external specification; precision implies measurement capability that RE-UNK-001 flags as absent | `Challenges/Return_To_Eden.md` | Open | Active | Major |
| RE-UNK-003 | Tier-to-tier advancement criteria undefined — no explicit pass/fail gate logic for progression between Tiers I–IV | `Challenges/Return_To_Eden.md` | Open | Active | Major |
| RE-UNK-004 | Upstream/downstream dependency map absent — Discovery.md Scope Map portion reconciled directly against source file 2026-07-05 (prior entry was inferred and partly incorrect). **Correction 2026-07-11:** the parenthetical claim that Navigation Anchors/File State "still does not exist" is stale — both are present and complete in the file (verified directly). The actual gap is narrower than originally stated: `Challenges/Return_To_Eden.md` has no dedicated Upstream Dependencies / Downstream Dependents section (the format other Challenges/ Solution-Track files use); stays Open until that section is added. | `Challenges/Return_To_Eden.md` | Open | Active | Minor |
| RE-UNK-005 | Eden Index baseline reference values undefined — $B_{d,0}$, $\Omega_{r,0}$, $W_{out,0}$, $\Phi_{ext,0}$ required by normalized formulation (v1.0.2) but have no measurement protocol; co-blocking dependency of RE-UNK-001 | `Challenges/Return_To_Eden.md` | Open | Active | Blocking (Tier I gate) |

*RE-UNK-001 and RE-UNK-005 are co-blocking at Tier I gate — both must be resolved before $I_E$ can be computed. Non-blocking at Exploration.*
*RE-UNK-002 and RE-UNK-003 become blocking at Tier I gate review; non-blocking at Exploration.*

### Hardware Modules

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| SC-001 | RPM envelope not validated | `Operations/Gate_05_Separation_Thermal.md` | In Progress | Active | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Blocking |
| SC-003 | MHD damping effectiveness | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Exploratory |
| SC-004 | Wire extrusion nozzle design | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Exploratory |
| SC-005 | Drive system geometry — dynamic imbalance blocked | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Major |
| SC-006 | Siting and area-of-operation requirements | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Major |
| SC-007 | Extraction process may disrupt segregation gradients | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Major |
| SC-008 | Graphite crucible carbon pickup in alloy | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Major |
| SC-009 | Titanium / reactive-metal atmosphere requirements undefined — current §9 doctrine (charcoal bed, optional inert purge) cannot support titanium or similar reactive metals; nitrogen embrittlement and oxygen pickup require full argon shielding or vacuum | `Operations/Gate_05_Separation_Thermal.md` | Open | — | Critical (if reactive metals enter material set); Non-blocking otherwise |
| MG-001 | Quantitative energy reduction not established | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Minor |
| MG-002 | Optimal RPM bands not characterized per feedstock | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| MG-003 | Confidence threshold not empirically validated | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| MG-004 | Geometry correction algorithm not specified | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| MG-005 | Aquatic biofouling impact on rotor balance | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Exploratory |
| MG-006 | Siting and area-of-operation requirements | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| MG-007 | Rotor jam and entanglement recovery undefined | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| MG-008 | Sensor fouling from conductive or abrasive fines | `Operations/Gate_04_Separation_Mechanical.md` | Open | — | Major |
| AS-001 | 500W power budget not validated | `Operations/Air_Scrubber.md` | Open | — | Medium |
| AS-002 | Marine bubble-column depth scope | `Operations/Air_Scrubber.md` | In Progress | Active | Low |
| AS-003 | Scrubber waste stream and saturation | `Operations/Air_Scrubber.md` | In Progress | Active | Medium |
| AS-004 | Noise exposure limits and hearing conservation program undefined | `Operations/Air_Scrubber.md` | Open | — | Major |
| SR-001 | Galvanic corrosion mitigation | `Tests/Support_Raft.md` | Open | — | Blocking |
| SR-002 | Sacrificial shell material selection | `Tests/Support_Raft.md` | Open | — | Major |
| SR-003 | Battery buffer sizing | `Tests/Support_Raft.md` | Open | — | Major |
| SR-004 | Induction charging pad design | `Tests/Support_Raft.md` | Open | — | Major |
| SR-005 | Chicken-and-egg end-of-region | `Tests/Support_Raft.md` | Open | — | Major |
| SR-006 | Cold storage rack design | `Tests/Support_Raft.md` | In Progress | Active | Minor |
| SR-007 | Cache sanitization on hull compromise | `Tests/Support_Raft.md` | Open | — | Blocking |
| SR-008 | Dynamic positioning vs. mooring | `Tests/Support_Raft.md` | Open | — | Minor |
| SR-009 | Ballast pump energy draw | `Tests/Support_Raft.md` | Open | — | Major |
| SR-011 | Shell ROI efficiency | `Tests/Support_Raft.md` | Open | — | Major |
| SR-012 | Mechanical bio-damping | `Tests/Support_Raft.md` | Open | — | Major |
| SR-013 | Buoyancy shift — calcifying organism mass limit | `Tests/Support_Raft.md` | Open | — | Major |

### Salvage & Fabrication

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GK-002 | Sacrificial anode material | `Architecture/Geck_forge_seed.md` | Open | — | Medium |
| GK-003 | Induction charging pad design | `Architecture/Geck_forge_seed.md` | Open | — | Low |
| GK-004 | Marine AM material durability | `Architecture/Geck_forge_seed.md` | Open | — | Low |
| ST-001 | Grain storage and tracking protocol | `Admin/Ship_of_Theseus.md` | Open | — | Low |
| ST-002 | QR documentation standard | `Admin/Ship_of_Theseus.md` | Open | — | Low |
| ST-003 | AI identity continuity under split-brain | `Admin/Ship_of_Theseus.md` | In Progress | Active | Medium |
| ST-004 | Sub-threshold state tampering vulnerability — Derivative Identity threshold (30%) has adversarial bypass; rolling delta mechanism required | `Admin/Ship_of_Theseus.md` | Open | — | Major |
| EL-001 | Forge-Standard interface spec | `Operations/Electronics.md` | Open | — | Medium |
| EL-002 | PCB trace width for v0 tooling | `Operations/Electronics.md` | Open | — | Low |
| EL-003 | TMR voter implementation | `Operations/Electronics.md` | Open | — | Medium |
| EL-004 | Chemical etch waste stream | `Operations/Electronics.md` | Open | — | Medium |
| EL-005 | Toxic dust and BFR emission profile not characterized | `Operations/Electronics.md` | Open | — | Critical |
| EL-006 | Firmware trust and reflashing validation not defined | `Operations/Electronics.md` | Open | — | Critical |
| EL-007 | Correlated failure modes in homogeneous salvage TMR not characterized | `Operations/Electronics.md` | Open | — | Major |
| EL-008 | Counterfeit salvage component detection doctrine not defined | `Operations/Electronics.md` | Open | — | Major |

### Reduction

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GR-001 | Output envelope not validated against Gate_04 inputs | `Operations/Gate_03_Reduction.md` | Open | — | Major |
| GR-002 | Reduction method not selected | `Operations/Gate_03_Reduction.md` | Open | — | Major |
| GR-003 | Biological and chemical waste disposal doctrine not assigned | `Operations/Gate_03_Reduction.md` | Open | — | Critical |
| GR-004 | Particulate generation rate and composition not characterized | `Operations/Gate_03_Reduction.md` | Open | — | Major |
| GR-005 | Automation introduction criteria not defined | `Operations/Gate_03_Reduction.md` | Open | — | Major |
| GR-006 | Mechanical jam clearing doctrine not defined | `Operations/Gate_03_Reduction.md` | Open | — | Major |
| GR-007 | Contaminated equipment retirement threshold not defined | `Operations/Gate_03_Reduction.md` | Open | — | Critical |
| GR-008 | Operator decision support minimum standard not defined | `Operations/Gate_03_Reduction.md` | Open | — | Major |

### Fabrication

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GF-001 | Welding wire diameter specification not defined | `Operations/Gate_06_Fabrication.md` | Open | — | Major |
| GF-002 | Precision ceiling not characterized at v0 bootstrap | `Operations/Gate_06_Fabrication.md` | Open | — | Major |
| GF-003 | Material removal hardware not specified | `Operations/Gate_06_Fabrication.md` | Open | — | Minor |
| GF-004 | Fabrication energy consumption not characterized | `Operations/Gate_06_Fabrication.md` | Open | — | Minor |
| GF-006 | Structural adequacy criteria undefined for v0 qualification | `Operations/Gate_06_Fabrication.md` | Open | — | Major |
| GF-005 | Utilization stage has no owning file | `Operations/Gate_06_Fabrication.md` | Open | — | Minor |
| GF-007 | Fabrication-area fire suppression and hot-work doctrine undefined | `Operations/Gate_06_Fabrication.md` | Open | — | Critical |

### Intake

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GI-001 | Reference database content and coverage not defined | `Operations/Gate_01_Intake.md` | Open | — | Major |
| GI-002 | Energetic material discharge doctrine not defined | `Operations/Gate_01_Intake.md` | Open | — | Critical |
| GI-003 | Augmented hazard detection capability not specified | `Operations/Gate_01_Intake.md` | Open | — | Critical |
| GI-004 | Intake tagging schema not cross-validated against grain system | `Operations/Gate_01_Intake.md` | Open | — | Major |
| GI-005 | Pre-Intake protocol for special handling not defined | `Operations/Gate_01_Intake.md` | Open | — | Major |
| GI-006 | Intake chain-of-custody integrity not defined | `Operations/Gate_01_Intake.md` | Open | — | Major |
| GI-007 | Digital contamination and hostile firmware handling not defined | `Operations/Gate_01_Intake.md` | Open | — | Critical |

### Network

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| FN-001 | Data validation criteria not defined | `Architecture/Forge_Net.md` | Open | — | Critical |
| FN-002 | Data replication factor not defined | `Architecture/Forge_Net.md` | Open | — | Major |
| FN-003 | Gaming detection criteria not defined | `Architecture/Forge_Net.md` | Open | — | Major |
| FN-004 | v0 Network transport layer not specified | `Architecture/Forge_Net.md` | Open | — | Major |
| FN-005 | Data privacy and access control not specified | `Architecture/Forge_Net.md` | Open | — | Critical |

### Utilization

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GU-001 | Performance metric schema not defined | `Operations/Gate_07_Utilization.md` | Open | — | Major |
| GU-002 | Retirement handoff protocol not cross-validated with Gate_02_Triage | `Operations/Gate_07_Utilization.md` | Open | — | Major |
| GU-003 | Formal quality certification and standards compliance unowned | `Operations/Gate_07_Utilization.md` | Open | — | Minor |
| GU-004 | Silent failure detection capability not defined | `Operations/Gate_07_Utilization.md` | Open | — | Major |
| GU-005 | FRT cycle definition and floor not yet declared | `Operations/Gate_07_Utilization.md` | Open | — | Major |

### Trajectory

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| TR-001 | v1 profitability baseline | `Admin/Trajectories.md` | Open | — | Blocking |
| TR-002 | FRT floor value not yet calibrated | `Admin/Trajectories.md` | Open | — | Major |
| TR-003 | Off-world nuclear containment architecture undefined — formalizes a dependency the file's own v3 text had flagged in prose since 2026-06-26 but never registered as a tracked unknown; not active until v3 planning begins | `Admin/Trajectories.md` | Open | — | Major |

### Plastics

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| PL-001 | Halogenated polymer contamination — HCl/dioxin release from PVC/Teflon | `Operations/Plastics.md` | Open | — | Critical |
| PL-002 | Reactor thermal runaway, pressure control, and maintenance access | `Operations/Plastics.md` | Open | — | Major |
| PL-003 | Pyrolytic fuel stability and contaminant profile | `Operations/Plastics.md` | Open | — | Minor |
| PL-004 | Mechanical filament-drawing threshold not defined | `Operations/Plastics.md` | Open | — | Minor |
| PL-005 | Char and solid residue composition uncharacterized | `Operations/Plastics.md` | Open | — | Major |

*PL-001 and PL-002 are Blocking before any hot pyrolysis run and reactor fabrication respectively.*

### Woodworking

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| WW-001 | Ambient-relative humidity drying schedules not quantified | `Operations/Woodworking.md` | Open | — | Major |
| WW-002 | Long-term performance of salvaged urban timber uncharacterized | `Operations/Woodworking.md` | Open | — | Major |
| WW-003 | CNC fixturing best practices for live-edge slabs not validated | `Operations/Woodworking.md` | Open | — | Minor |
| WW-004 | Dust toxicity thresholds for mixed-species milling uncharacterized | `Operations/Woodworking.md` | Open | — | Major |
| WW-005 | NDT standards for IFM detection not validated | `Operations/Woodworking.md` | Open | — | Critical |

*WW-004 Blocking for sustained mixed-species operations without P100 respirator.*
*WW-005 Blocking for processing raw urban salvage through any powered machinery.*

### Facilities

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| FA-001 | Site not confirmed or assessed | `Architecture/Facilities.md` | Open | — | Critical |
| FA-002 | Hot Zone minimum clearance radius not defined | `Architecture/Facilities.md` | Open | — | Major |
| FA-003 | Legal zoning and permitting not assessed | `Architecture/Facilities.md` | Open | — | Major |
| FA-004 | RDC heat load impact on operator safety not quantified | `Architecture/Facilities.md` | Open | — | Minor |

*FA-001 Critical — blocks all hot operations and SP-006 (emergency response).*

### Safety

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| SP-001 | Risk threshold cross-reference with Engineer_Protocols.md pending | `Admin/Safety_Protocols.md` | Open | — | Major |
| SP-002 | PPE specifications not sourced to standards | `Admin/Safety_Protocols.md` | Open | — | Major |
| SP-003 | Site noise levels not measured | `Admin/Safety_Protocols.md` | Open | — | Major |
| SP-004 | Heat stress doctrine not validated against operator experience | `Admin/Safety_Protocols.md` | Open | — | Minor |
| SP-005 | Regulatory compliance and permitting not assessed | `Admin/Safety_Protocols.md` | Open | — | Major |
| SP-006 | Emergency response procedures not defined | `Admin/Safety_Protocols.md` | Open | — | Major |

*SP-006 blocked by FA-001 — cannot define site evacuation without a site.*

### Economics

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| ECN-001 | Critical mineral surplus disposition path undefined | `Admin/Economics.md` | Open | — | Major |
| ECN-002 | Operating cost baseline not established | `Admin/Economics.md` | Open | — | Critical |
| ECN-004 | Market rate data not maintained | `Admin/Economics.md` | Open | — | Minor |
| ECN-005 | Legal and tax compliance not assessed | `Admin/Economics.md` | Open | — | Major |
| ECN-006 | Barter performance and default risk mechanics undefined — no verification/recourse posture for non-monetary exchanges yet | `Admin/Economics.md` | Open | — | Minor |

*ECN-002 Critical — blocks TR-001 closure; depends on EV-001.*
*ID prefix note: renamed from `EC-` to `ECN-` 2026-07-06 per CT-007 resolution — see Governance & Verification section and Audit Trail below. ECN-003 (barter valuation standard) is Resolved and does not appear in this active index per Size Management Rule 2.*

### Governance Migration

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GMP-003 | Adversarial review underspecified at v0 single-contributor | `Admin/Governance_Migration_Protocol.md` | Open | — | Major |
| GMP-004 | Ratification authentication gap mirrors GOV-006 | `Admin/Governance_Migration_Protocol.md` | Open | — | Major |
| GMP-006 | Concurrent amendment handling undefined | `Admin/Governance_Migration_Protocol.md` | Open | — | Major |
| GMP-007 | Amendment withdrawal procedure undefined | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |
| GMP-002 | Canonical Governance Ownership transfer not yet recorded in Charter | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |
| GMP-008 | Stale proposal expiration policy undefined | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |
| GMP-010 | No evidence-sufficiency gate between a directed approach and downstream reliance on it — grounded in CE-006; extended 2026-07-19 to cover deliberate subversion (source diversity, wrong-by-design classification flagged) | `Admin/Governance_Migration_Protocol.md` | Open | — | Major |
| GMP-011 | Track classification dispute resolution undefined — "when in doubt, Track B" covers uncertainty, not disagreement after a classification has been made | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |
| GMP-012 | No rollback or repeal doctrine for a ratified Track B amendment that later proves harmful | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |
| GMP-013 | Epistemic Quorum Doctrine (§VI) has no tooling or machine-readable metadata for `Automation/AUDIT_HARNESS.py` verification | `Admin/Governance_Migration_Protocol.md` | Open | — | Minor |

*GMP-004 highest-risk attack vector on Track B amendment process — depends on SEC-007a.*
*GMP-005 and GMP-009 are Resolved as of 2026-07-17 (Track A/Track B redefined by constitutional impact rather than document location, merged as one gap) and do not appear in this active index per Size Management Rule 2 — see `Governance_Migration_Protocol.md`'s own sidecar and Resolution Log. `Governance_Charter.md`'s EDL draft was formally classified Track A under that resolution and remains PROPOSED, NOT RATIFIED. GOV-013 was classified Track A under the same resolution but has since been ratified (confirmed against `Archive/Logs/Governance_Charter_Changelog.md`, v4.28) — removed from this file's Active Index accordingly; the Track A classification itself is unaffected by ratification status.*
*GMP-002's transfer remains explicitly gated on `Governance_Migration_Protocol.md` reaching Gate 4 / Provisional Specification maturity (currently 0/6 Spec Gates) — not yet eligible for closure regardless of the GMP-005/GMP-009 resolution.*

### Repository Structure

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| RS-001 | Non-markdown file type introduction procedure undefined | `Admin/Repository_Structure.md` | Open | — | Minor |
| RS-002 | Forge_flow.md casing outlier not yet corrected | `Admin/Repository_Structure.md` | Open | — | Minor |
| RS-003 | Archive/ directory not yet physically created | `Admin/Repository_Structure.md` | Open | — | Major |

### Precision

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| PR-001 | Precision ceiling not yet declared | `Architecture/Precision.md` | Open | — | Critical |
| PR-002 | Reference standard not established | `Architecture/Precision.md` | Open | — | Major |
| PR-003 | Traceable dimensional claims required at Specification | `Architecture/Precision.md` | Open | — | Major |
| PR-004 | Backlash and compliance characterization not performed | `Architecture/Precision.md` | Open | — | Major |
| PR-005 | GK-005 resolution confirmation pending | `Architecture/Precision.md` | Open | — | Minor |

*PR-001 Critical — blocks T1/T2 part claims; PR-004 is a prerequisite.*

### Environmental Constraints

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| ENV-001 | Site-specific climate parameter baseline not established — all climatic parameters are Placeholder | `Admin/Environmental_Constraints.md` | Open | — | Major |
| ENV-002 | Regulatory compliance framework for bootstrap site not assessed | `Admin/Environmental_Constraints.md` | Open | — | Major |
| ENV-003 | Jurisdiction conflict hierarchy undefined — cross-ref EC-010, GOV-010 | `Admin/Environmental_Constraints.md` | Open | — | Minor |
| ENV-004 | Ecological impact assessment protocol undefined | `Admin/Environmental_Constraints.md` | Open | — | Major |
| ENV-005 | Community engagement protocol undefined | `Admin/Environmental_Constraints.md` | Open | — | Major |
| ENV-006 | No-externalized-entropy doctrine not operationalized | `Admin/Environmental_Constraints.md` | Open | — | Major |
| ENV-009 | No site has been assessed against this file's constraints — all values are Placeholder | `Admin/Environmental_Constraints.md` | Open | — | Critical |
| ENV-010 | Upstream Facilities.md checklist reciprocity unverified — whether Facilities.md's Site Initialization Checklist actually mandates collection of this file's Category 1 parameters is unconfirmed | `Admin/Environmental_Constraints.md` | Open | — | Major |

*ENV-009 Critical — file is doctrine only until first site assessment replaces Placeholder values.*
*ENV-007 and ENV-008 are Resolved/Partially Addressed respectively as of 2026-07-06 and do not appear in this active index per Size Management Rule 2 — see Environmental_Constraints.md's own sidecar and Discovery.md's 2026-06-21 registration note.*

### Closed-Loop Feedstock

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| CLF-001 | Blending ratios and thermal stabilizer performance for mixed, un-refined polymer streams across multiple thermal cycles | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Major |
| CLF-002 | Minimal viable field assay protocols (spot tests, melt-flow, etc.) for copper/aluminum alloys from salvage | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Major |
| CLF-003 | Nozzle and die wear tolerances when processing high-variance, particulate-laden salvage feedstocks | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Critical |
| CLF-004 | Chemical footprint of electrolytic/electrorefining pathways undefined — local/organic acid sourcing vs. closed-loop acid reclamation not decided; cross-ref `Admin/Ethical_Constraints.md` §Toxic and Hazardous Material Handling, `Operations/Gate_03_Reduction.md` GR-003, PL-001/CE-003, `Challenges/Critical_Minerals.md` CM-002. Candidate pathway logged 2026-07-07 (on-site chlor-alkali electrolysis) — blocked pending CE-006 (`Architecture/Chemistry.md`, chlorine containment). | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Critical |
| CLF-006 | Recursive cascading contamination thresholds, bleed-off, and purge metrics — full doctrine ratified 2026-07-31 (owning file §7.1); numeric thresholds provisional pending instrumented-cycle validation | `Challenges/Closed_Loop_Feedstock.md` | In Progress | — | Critical |
| CLF-007 | PIR aggregation function undefined — four sub-vectors collapsed to a scalar with no stated operator; arithmetic mean would contradict the file's own single-fatal-dependency framing | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Major |
| CLF-008 | Downstream destination for degraded/bleed-off material and hazardous byproducts undefined — no link to full-reduction diversion or waste-output accumulation tracking | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Major |
| CLF-009 | Interface contract for characterization→fabrication data handoff — Material Certainty Manifest schema ratified 2026-07-31 (owning file §7.2); not yet physically deployed on any real batch | `Challenges/Closed_Loop_Feedstock.md` | In Progress | — | Minor |
| CLF-010 | FIR boundary conditions undefined — how donated virgin resin, reclaimed-but-unprocessed wire, and reused fasteners count toward salvaged vs. total mass is unspecified | `Challenges/Closed_Loop_Feedstock.md` | Open | — | Major |

*CLF-003 and CLF-006 are Critical — CLF-003 blocks sustained polymer extrusion operations; CLF-006 blocks safe recursive-loop operation.*
*CLF-004 is Critical — no electrolytic/electrorefining pathway may proceed without a chemical footprint decision. Its candidate pathway is further blocked by CE-006 pending a chlorine containment design.*
*ID collision history: originally registered `CF-001`–`CF-003` (collided with `Architecture/Cognitive_Frameworks.md`/`Operations/Electronics.md`); briefly renamed `FL-001`–`FL-004` by an intervening pass, which collided with `Architecture/Forge_flow.md`'s FL-001 (Blocking); settled on `CLF-` prefix, unique in this index as of this version.*

### Pending Corrections

| ID | Title | Files Affected | Status | Subtype | Priority |
|---|---|---|---|---|---|
| PC-001 | Verification Ref corrections | All 10 files corrected | Resolved | — | Major |
| PC-002 | Upstream reference corrections | All 7 files corrected | Resolved | — | Minor |
| PC-003 | New file cross-reference corrections | All 10 files corrected | Resolved | — | Minor |
| PC-004 | Stale name corrections | Both files corrected | Resolved | — | Minor |
| PC-005 | `Challenges/Closed_Loop_Feedstock.md` not registered in `Routing.md`, `Discovery.md`, or `Automation/AUDIT_HARNESS.py` | Closed_Loop_Feedstock.md | Resolved 2026-07-19 — independently re-verified directly against source: present in Routing.md (line 93, Explicit backlink, fixed 2026-07-06), Discovery.md (structure tree, "created 2026-07-06 ✓"), and AUDIT_HARNESS.py FILE_REGISTRY. Flagged possibly-stale since v4.20 (2026-07-12); confirmation finally done. | — | Major |
| PC-006 | Ethical Anchor field used a non-canonical backticked, `Admin/`-prefixed variant instead of the canonical plain-text string | Biofouling.md, Closed_Loop_Feedstock.md, Critical_Minerals.md, Emergence.md, Planned_Obsolescence.md, Waste.md, Water.md, Support_Raft.md (8 of the original 9) — **Energy_Scarcity.md excluded from this list, corrected**: that file was created same-day (2026-07-12), evidently after this sweep's fetch, so it was never actually part of the 9; PC-006's original file list was wrong to include it. Fixed independently 2026-07-19 — see that file's own Resolution Log. | Resolved 2026-07-12 (8 files); Energy_Scarcity.md separately resolved 2026-07-19 | — | Critical |

### Cognitive Salvage

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| GH-001 | Heuristic-to-deterministic translation fidelity undefined | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-002 | Statistical significance threshold for consensus aggregation undefined | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-003 | Adversarial poisoning of heuristic datasets undefined | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-004 | Optimal abstraction level for heuristic preservation undefined | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-005 | Human vs. autonomous intervention fraction undefined | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Minor |
| GH-006 | NOVEL promotion threshold undefined — CANDIDATE_NOVEL holds qualifying entries until resolved | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-007 | Puzzle fidelity drift undefined — silent pipeline poisoning risk if machinery revision diverges from puzzle engine | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-008 | Heuristic expiration doctrine undefined — validated_on_machinery_revision field exists; expiration logic does not | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-009 | Emergent heuristic conflict undefined — N² interaction scaling; two independently verified heuristics may fail catastrophically in combination | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Critical |
| GH-010 | Simulator overfitting undefined — pipeline may harvest simulator expertise rather than physical expertise | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-011 | Heuristic canonicalization layer undefined — variant sequences inflate consensus_run_count without adding evidential weight | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-012 | Discovery yield rate undefined — fraction of harvested heuristics that are genuinely novel; primary ROI signal for the layer | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Major |
| GH-013 | Conceptual salvage artifact storage mechanism undefined — no object schema exists for non-physical-input recovery (Conceptual Salvage Pipeline, provisional) | `Tests/Cognitive_Salvage_Layer.md` | Open | — | Minor (Blocking for the Conceptual Salvage Pipeline subsection specifically, not the file as a whole) |

*GH-001 and CSL-A06 are co-blocking: translation fidelity and simulation-to-physical fidelity are the two load-bearing assumptions for operational deployment.*
*GH-003 maps to Adversarial Battery Challenge Class 8 — route adversarial resistance requirements to Admin/Security_Protocols.md.*
*GH-009 Critical — interaction surface grows as N²; Interaction Volume doctrine required before knowledge base scales beyond ~20 promoted heuristics.*
*GH-006 hard gate: no heuristic may receive NOVEL status until GH-006 closes; CANDIDATE_NOVEL intermediate status holds qualifying entries.*
*GH-013 — registered 2026-07-12 alongside the file's new "Conceptual Salvage Pipeline" Body subsection, which is explicitly Exploration-within-Exploration and has not passed Gate 1. Do not treat GH-013's resolution as validating that subsection's doctrine — the subsection needs its own Gate 1 review independent of this unknown closing.*

### Hydrologic Resource Cascade

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| HR-UNK-001 | Hydraulic sorting effectiveness at Forge-scale unvalidated — particle separation efficiency across all zones uncharacterized | `Tests/Hydrologic_Resource_Cascade.md` | Open | — | Critical |
| HR-UNK-002 | Material quality and contaminant risk uncharacterized — flood sediment may contain heavy metals, pesticides, or industrial runoff | `Tests/Hydrologic_Resource_Cascade.md` | Open | — | Critical |

*HR-UNK-001 Critical — entire resource recovery premise rests on hydraulic sorting effectiveness.*
*HR-UNK-002 Critical — safety-critical; contaminated sediment zones may require remediation rather than resource extraction.*
*Additional HR unknowns (HR-003 through HR-010) are research questions in the file body; formal sidecar registration deferred to first audit pass.*
*Known discrepancy: Tests/Hydrologic_Resource_Cascade.md File State declares "Open Unknowns: 8," but only HR-UNK-001 and HR-UNK-002 carry formal sidecar entries as of 2026-06-28. Correct the File State field to 2 on next commit to that file, or register HR-003 through HR-008 formally to match the declared count.*

### Philosophical / Foundational

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|---|---|---|---|---|---|
| NT-010 | Maintenance energy normalization undefined — R metric assumes a common unit of "maintenance energy" across physical, informational, institutional, and cognitive substrates; normalization methodology undefined | `Admin/Nothingness_Theorem.md` | Open | Active | Minor |

*NT-001 through NT-009 are tracked in the Admin/Nothingness_Theorem.md internal unknowns table. They are not cross-module and are not registered here.*

### Cross-Module

| ID | Title | Owning Files | Status | Subtype | Priority |
|---|---|---|---|---|---|
| UNK-008 | Welding wire specification and qualification — ownership reassigned 2026-07-19 to `Architecture/Geck_forge_seed.md` (was incorrectly listed as `Gate_05_Separation_Thermal.md`, which explicitly disclaims it) | `Architecture/Geck_forge_seed.md` | Open | — | Major |
| UNK-009 | External root-of-trust — spans GOV-003, GOV-005, RIP-001, SEC-007a/SEC-007b | `Admin/Governance_Charter.md`, `Admin/Repository_Integrity_Protocol.md`, `Admin/Security_Protocols.md` | Open | — | Critical |

### Future / Deferred

| ID | Title | Owning File | Status | Subtype |
|---|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Admin/Auditor_Protocols.md` | Deferred (Leviathan milestone) | — |
| UNK-005 | Marine G.E.C.K. seed variant | `Architecture/Geck_forge_seed.md` | In Progress (stub added) | Active |
| UNK-001 | Discovery.md Unknowns.md entry | `Discovery.md` | In Progress | Active |
| RC-001 | Governance Drift | None yet | Candidate | — |
| RC-002 | Incentive Capture | None yet | Candidate | — |
| RC-003 | Information Decay | None yet | Candidate | — |
| RC-004 | Identity Continuity | None yet | Candidate | — |
| RC-005 | Coordination Failure | None yet | Candidate | — |
| RC-006 | Institutional Ossification | None yet | Candidate | — |
| RC-007 | Priority Escalation Saturation | `Admin/Auditor_Protocols.md` | Candidate | — |
| RC-008 | Long-Lived Unknown Accumulation | `Admin/Auditor_Protocols.md` | Candidate | — |
| RC-009 | Resolution Vehicle Persistence Without Progress | `Admin/Auditor_Protocols.md` | Candidate | — |

*RC-001 through RC-006 are Reflexive Challenge candidates — log against Challenges/ on next major architecture review.*
*RC-007 through RC-009 doctrine resides in Admin/Auditor_Protocols.md Unknowns Registry. Promote to Challenges/ alongside RC-001 through RC-006 on next major architecture review.*

---

## Active Disputes Registry

| ID | Title | Owning File | Positions | Risk | Status |
|---|---|---|---|---|---|
| CF-DS-001 | Centralized vs. distributed cognition | `Architecture/Cognitive_Frameworks.md` | Single executive AI vs. fleet consensus | High | **Resolved 2026-07-26 — scope-dependent hybrid** |
| CF-DS-002 | Human override authority scope | `Architecture/Cognitive_Frameworks.md` | Absolute override vs. bounded override (see `Admin/Ethical_Constraints.md`) | High | **Resolved 2026-07-26 — Bounded Override** |

*CF-DS-001 resolved as neither named extreme — Frameworks E and F apply at different decision scales per the new Authority Scope Boundary in `Architecture/Cognitive_Frameworks.md` §III, generalizing `Tests/Support_Raft.md`'s existing comms-blackout doctrine.*
*CF-DS-002 ratified directly by human governing authority — hard floors in `Admin/Ethical_Constraints.md` (Anti-Weaponization, Life Preservation, Cultural Sites) sit above the human governing authority's own direct order, not only above subordinate agents. Full doctrine in `Admin/Ethical_Constraints.md` v0.13. Per Size Management Rule 2, both entries will drop from this registry entirely on the next version pass; kept visible with Resolved status this pass since the resolution is new.*
*ENV-DS-001 (Bootstrap operating doctrine vs. Compliance-Maximizing Default) ratified by human governing authority 2026-07-17 and removed from this active registry per Size Management Rule 2 — see `Admin/Environmental_Constraints.md` Constraint Category 2 for the adopted text.*

---

## Expiry Watch

*Expiry Rule is active. Check this table at the opening of each audit cycle.*

**Tier 1 Axiom verification is the mandatory first step** — confirm axiom text in `Admin/Governance_Charter.md` matches prior committed version before proceeding. Any unratified change is a Constitutional violation.

**Epistemic Foundation integrity check is the mandatory second step** — confirm EF-0.0 through EF-0.8b text in `Admin/Auditor_Protocols.md` matches prior committed version. Any unratified modification = Integrity Violation → STATE_HOLD.

FL-001 and several EC entries have been In Progress since v1.1 — approaching two-cycle threshold. Flag for Full Stop Review trigger assessment at next audit opening if still unresolved.

GOV-003 In Progress — Repository_Integrity_Protocol.md is the executing resolution path. GOV-005 remains Critical with no fast resolution path. GOV-007 In Progress — Genesis Phase Protocol executing; full resolution depends on GOV-008. GOV-008 exit condition not yet met.

**RIP-001 Resolved** — Git release tag system (V0.6–V0.97, GPG-signed) fulfills prior-state archival at v0 scale. Discharged via Lessons Learned 2026-06-28. Full resolution detail in Admin/Repository_Integrity_Protocol.md sidecar.

**EN-001 Critical/Blocking** — no structural specification may be promoted without validated safety factors for salvaged materials.

**CF-001 In Progress/Blocking** — parameters defined (τ=50ms WDT). Remains Blocking until first hardware prototype validates at Measured confidence.

**AP Systemic Risk escalation** — Downgrade confirmed by human governing authority 2026-07-03 (Auditor_Protocols.md v0.15). AP-001, AP-002, AP-004, AP-005, AP-007 remain In Progress. AP-012 and AP-016 Resolved 2026-07-03 (v0.16) — no longer Critical Watch items.

### Critical Watch

| ID | Note |
|----|------|
| GOV-005 | Constitutional stability — no fast resolution path; requires operational cycles |
| SEC-007a | External root-of-trust, constitutional layer — architectural decision above repository level required; blocks SEC-007b |
| SEC-007b | External root-of-trust, physical implementation layer — blocked pending SEC-007a resolution |
| UNK-009 | External root-of-trust cross-module — spans GOV-003, GOV-005, RIP-001, SEC-007a/SEC-007b |
| EC-008 | Inferred authorization — softest point in permission model; interim default (no material alteration) in place; formal resolution required before operational deployment |
| EC-011 | Human governance adversary model — load-bearing assumption under "capability never outruns permission"; no protection if permission source is compromised |
| EC-012 | Epistemic spoofing via hardware/firmware tampering — every constraint in Ethical_Constraints.md assumes telemetry is honest; no doctrine addresses compromised sensor/firmware data |
| EV-003 | Battery thermal containment — no enclosed battery bank until resolved |
| PL-001 | Halogenated polymer contamination — no hot pyrolysis run before triage protocol validated |
| WW-005 | IFM detection — no powered machinery contact with raw urban salvage until screening validated |
| EN-001 | Validated safety factors for salvaged materials — blanket floor replaced with differentiated per-material interim table 2026-07-05; still no destructive test data; no structural specification promotion until resolved |
| CF-001 | Hardware watchdog — In Progress; Blocking until hardware prototype validates at Measured confidence |
| TH-003 | Atmospheric moisture yield — Blocking for Living Waters deployment |
| FA-001 | Site not confirmed — no hot operations until site physically assessed |
| ECN-002 | Operating cost baseline not established — blocks TR-001; depends on EV-001 |
| PR-001 | Precision ceiling not declared — blocks T1/T2 part claims; PR-004 prerequisite |
| EM-001 | Behavioral opacity detection threshold — depends on CF-001 hardware validation |
| EM-004 | Governance substrate integrity under emergent agent access — Critical; mirrors GOV-003, SEC-007a |
| WA-002 | Hazardous fraction identification reliability — safety-critical before mixed-waste operations |
| WA-004 | Negative-value waste fraction disposal — no owning file; mirrors GR-003 gap |
| CM-002 | Acid leach reagent recovery doctrine — no hydrometallurgical processing before closed-loop specified |
| CE-003 | Field polymer identification reliability — Critical; blocks first hot pyrolysis run |
| CE-006 | Chlorine gas containment for on-site acid synthesis — no chlor-alkali pathway may be adopted for CLF-004 until sealed-vessel/scrubbing design defined |
| TF-006 | Non-target insect capture — Ethical_Constraints escalation candidate; halt expansion if threshold cannot be bounded |
| SD-UNK-004 | Host geology fracturing threshold — no excavation without geomechanical assessment; parallels FA-001 |
| LW-UNK-001 | Volatile co-distillation in LW-001 — CRITICAL safety gap; blocks potable output claim |
| LW-UNK-003 | LW-003 lumen implosion — CRITICAL; 4.9 MPa net crush load at 500 m |
| GH-009 | Emergent heuristic conflict — N² interaction scaling; two independently verified heuristics may fail catastrophically in combination; Interaction Volume doctrine required before knowledge base scales |
| HR-UNK-002 | Hydrologic Resource Cascade material quality — flood sediment contaminant risk; safety-critical before any resource extraction operations |
| CLF-003 | Nozzle/die wear tolerances — blocks sustained polymer extrusion operations |
| CLF-004 | Electrolytic chemical footprint undefined — no electrorefining pathway before acid sourcing/reclamation decision made; candidate pathway further blocked by CE-006 |
| CLF-006 | Recursive contamination thresholds/bleed-off undefined — blocks safe recursive-loop operation |

### Blocking Watch

| ID | Note |
|----|------|
| GOV-008 | Minimum quorum — GOV-007 Genesis Phase exit condition not yet met |
| PL-002 | Reactor pressure control — no reactor fabrication before pressure relief specified |
| WW-004 | Mixed-species dust — interim mitigation (P100 mandatory); formal characterization required |

---
