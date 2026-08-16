# Adm_Scope_Map.md — Admin/

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Index                                                      |
| Spec Gates       | N/A — this file is a cross-reference index, not a specification     |
| Open Unknowns    | 0 (surfaces existing unknowns from owning files; creates none)      |
| Owning Domain    | Admin/                                                               |
| Last Reviewed    | 2026-08-15                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md` if present. |

---

## Purpose

Pilot for a per-folder scope-map pattern, proposed 2026-08-07 as a fix for a known prior failure mode: an earlier version of `Discovery.md` (v0.93) tried to hold this same per-file Purpose/In-Scope/Out-of-Scope/Upstream/Downstream detail for the *entire* repository in one file, and outgrew itself. At that version's density (~17-20 lines/file) applied to today's repository size (77 files across six folders), a single combined file would run 1500+ lines on top of everything else `Discovery.md` already carries. This file exists to test whether splitting that same format one-file-per-folder keeps each piece small while preserving the actual payoff: juxtaposing every file's stated scope in one place so gaps between them become visible, the way the old file's "Cross-Module Unknowns — Attention Required" table did.

**This file does NOT** duplicate `Unknowns.md` — open items below point to unknowns already tracked there, not new ones. It does NOT replace each file's own authoritative Scope Boundary section — where this summary and a file's own text conflict, the file wins, same rule `Discovery.md` already states for its Maturity Snapshot.

---

## Scope Entries

### `Admin/Auditor_Protocols.md`
**Status:** Draft · 4/6 · 14 Open Unknowns · Risk: High
**Does:** Epistemic Foundation (EF-0.0-0.8b, meta-constitutional); auditor role classes; audit sequencing; Fallacy Checklist; Sidecar Model; Unknowns governance; verification gate enforcement; Adversarial Challenge Battery; Mission Drift Review; AI/human contributor protocols.
**Does not (arrow):** Canonical terminology (`Canonical_Terms.md`) - repository ownership boundaries (`Governance_Charter.md`) - cross-repo verification architecture (`Forge_Net.md`).

### `Admin/Autonomy_Divergence_Protocol.md`
**Status:** Draft — PROPOSED NOT RATIFIED · 0/6 · 2 Open Unknowns (GOV-021b, GOV-021c) · Risk: High
**Does:** Response protocol for observed divergence of autonomous/semi-autonomous subsystems; Capability Anomaly vs Governance Concern classification; graduated Response Tiers; restoration, logging, and review obligations. Explicitly rejects any "capability implies exit from oversight" framing.
**Does not (arrow):** Detection calibration / Watch exit conditions (GOV-021b) - coordinated multi-agent divergence (GOV-021c) - ethical hard floors (`Ethical_Constraints.md`) - Charter hierarchy - Auditor Protocols - CIR algebra. Normalized to DOES/DOES NOT template 2026-08-09.

### `Admin/BATTERY_SEED.md`
**Status:** Draft · N/A (prompt template) · 0 tracked here (see AP-017) · Risk: unlabeled in File State
**Does:** The frozen prompt block for a genuine AP-017-qualifying cold-session Adversarial Battery run; operator checklist; extra target-file list when auditing `Auditor_Protocols.md` itself.
**Does not (arrow):** AP-017's closure bar itself (`Archive/Logs/Auditor_Protocols_Logs.md`) - the Battery's ten class definitions (`Auditor_Protocols.md`) - `cold_session_bundler.py` mechanics.

### `Admin/CIR_Gov.md`
**Status:** Proposed — Not Ratified · 0/6 · 1 Open Unknown (CIR-GOV-001) · Risk: High (raised from Medium 2026-07-31)
**Does:** Formal epistemic state-transition kernel spec — predicate-gated admissibility, debt accounting, provenance ceilings — intended as a future layer *under* Charter authority.
**Does not, and must never claim:** Constitutional authority - satisfaction of Axiom Q-2 or GOV-008 - runtime execution (nothing in this repo implements it) - Genesis Phase exit.

### `Admin/Canonical_Terms.md`
**Status:** Draft · 0/6 · 9 Open Unknowns · Risk: Low
**Does:** Authoritative vocabulary mappings; conflict-resolution rules against other vocabulary sources; anti-drift guardrails and banned-term list.
**Does not (arrow):** Ethical policy (`Ethical_Constraints.md`) - operational routing semantics (`Architecture/Forge_flow.md` — authoritative on conflict) - governance tier authority (`Governance_Charter.md`) - Rename Registry (`Discovery.md`).

### `Admin/Computational_Institutional_Reasoning.md`
**Status:** Exploration · G4 cleared, G1 partial, G3 blocked (AP-012/AP-016) · Open Unknowns unclear from File State · Risk: CIR-001 (Physical Grounding Telemetry Mapping undefined)
**Does:** Formal algebraic Institutional State / Mutation model; Core Axioms and five theorems (Unknown Conservation, Governance Stability, Epistemic Debt Instability, Institutional Memory Dominance, Compiler Soundness); Verification Algebra and provenance ceilings; derivation of Axiom A3 / γ2 from Nothingness_Theorem without altering that file's Tier 0 status.
**Does not (arrow):** Charter hierarchy - Ethical hard floors - Auditor Protocols / Battery - Autonomy Divergence response tiers - runtime implementation - GOV-008 quorum - CIR_Gov packaging. Scope Boundary added 2026-08-09 (was the load-bearing gap flagged on Scope_Map creation).

### `Admin/Economics.md`
**Status:** Exploration · 0/6 · 5 Open Unknowns (ECN-001/002/004/005/006) · Risk: Medium
**Does:** Dynamic resource/procurement/surplus doctrine; market navigation; revenue model (TR-001 input); v1 profitability baseline; barter doctrine.
**Does not (arrow):** FRT doctrine/floor (`Trajectories.md`) - FRT logging (`Gate_07_Utilization.md`) - primary KPI (`Architecture/Forge_flow.md`) - energy cost model (`Operations/Energy.md`) - safety envelopes for commercial value streams (`Safety_Protocols.md`, `Operations/Plastics.md`, `Operations/Woodworking.md`).

### `Admin/Engineer_Protocols.md`
**Status:** Draft · 2/6 · 6 Open Unknowns · Risk: High
**Does:** Engineering problem-solving protocols; assumption-challenge triggers; anti-reinvention/failure-harvesting rules; Engineer-Auditor dispute resolution.
**Does not (arrow):** Domain-specific calculations (`Operations/`, `Architecture/`) - general audit procedure (`Auditor_Protocols.md`) - PPE/risk thresholds (`Safety_Protocols.md`).

### `Admin/Environmental_Constraints.md`
**Status:** Draft · 1/6 · 8 Open Unknowns · Risk: High
**Does:** Site-specific/regional environmental parameters; regulatory/climatic/ecological/jurisdictional constraints; degradation triggers.
**Does not (arrow):** Facility engineering specs (`Architecture/Facilities.md`) - site safety/PPE (`Safety_Protocols.md`) - jurisdiction conflict hierarchy (ENV-003 — confirmed cross-linked to `Ethical_Constraints.md` EC-010 in `Unknowns.md`, not a duplicate despite each file naming only its own ID locally).

### `Admin/Ethical_Constraints.md`
**Status:** Exploration · 0/6 · 16 Open Unknowns · Risk: High
**Does:** Pre-action authorization; ownership/legal rights recognition; Anti-Weaponization Doctrine (hard floor); life preservation; toxic material handling; cultural/sacred site recognition; refusal as first-class action; Pacifist Operating Posture.
**Does not (arrow):** Confidence threshold specifics (EC-001) - weaponization pattern-matching (EC-002) - escalation channel (EC-003, `Tests/Leviathan_testing.md`) - jurisdiction hierarchy (EC-010, see above) - Constitutional Governance Hierarchy naming convention (EC-016 — corrected 2026-08-07, see that entry's own note: the underlying doctrine already exists across `Governance_Charter.md`; this is a documentation-consolidation gap, not a live conflict).

### `Admin/Experiments.md`
**Status:** Draft · 0/6 · 0 Open Unknowns · Risk: Low
**Does:** Structured falsification records for PROVISIONAL claims; PROVISIONAL to VERIFIED promotion mechanism; pass/fail criteria for physical/sensor/assay/code grounding events.
**Does not (arrow):** Operational test system specs (`Tests/Living_Waters.md`, `Tests/Trophic_Forge.md`, `Tests/Solar_Descent.md`) - system-level validation (`Verification_Gates.md`).

### `Admin/File_Template.md`
**Status:** Exploration/Draft/Specification (template, all three by design) · 0/6 · Risk: Low/Medium/High (template)
**Does:** Defines the Scope Boundary pattern itself — "If content is not listed under DOES, it does not belong in the Body." The template every entry in this file is built from.

### `Admin/Forge_Audit_Kit.md`
**Status:** Draft · 0/6 · 5 Open Unknowns (see its own Sidecar Link) · Risk: unlabeled
**Does:** Condensed audit reference — Epistemic Foundation summary, Verification Maturity Model, Truth Provenance labels, Audit Opening Checklist, Fallacy Checklist, AI contribution rules.
**Does not (arrow):** Full auditor doctrine, full EF text, full Adversarial Battery (all `Auditor_Protocols.md`) - unknown registry (`Unknowns.md`) - file ownership (`Discovery.md`) - governance hierarchy (`Governance_Charter.md`).

### `Admin/Governance_Charter.md`
**Status:** Draft · 6/6 (execution quality; promotion separately blocked by GOV-003/GOV-005 + Enforcement Checkpoint 2) · 20 Open Unknowns · Risk: Critical
**Does:** Tier 1 constitutional axioms; governance authority hierarchy; canonical governance ownership; bootstrap/Genesis Phase doctrine; migration doctrine; human override doctrine.
**Does not (arrow):** Runtime execution, crypto implementation, CI/CD (out of scope entirely) - canonical terminology (`Canonical_Terms.md`) - auditor behavior (`Auditor_Protocols.md`) - condensed reference (`Forge_Audit_Kit.md`).
FLAG: Single most load-bearing file in the repository — six other files in this folder alone (`GMP`, `RIP`, `CIR_Gov`, `Hardware_Diversity_Ladder`, `Security_Protocols`, `Ethical_Constraints`) explicitly defer authority questions back to this one.

### `Admin/Governance_Migration_Protocol.md`
**Status:** Exploration · 0/6 · 10 Open Unknowns · Risk: High
**Does:** Tier 2-5 migration procedures; Tier 1 amendment process; Section VII Bootstrap Quorum Doctrine (GOV-008 candidate spec, extended 2026-08-06 VII.8, Class 9/Class 5 patches 2026-08-07).
**Does not (arrow):** Tier 1 Axioms themselves, constitutional hierarchy (`Governance_Charter.md`) - ratification crypto (`Security_Protocols.md`) - minimum agent quorum *definition* (owned by Charter, specified here) - integrity enforcement mechanics (`Repository_Integrity_Protocol.md`).
**Explicitly proposed, not claimed:** migration doctrine ownership transfer from `Governance_Charter.md` to this file — "pending Charter update and Gate 4 clearance." This is the pattern EC-016's correction pointed to as worth naming as a reusable convention.

### `Admin/Hardware_Diversity_Ladder.md`
**Status:** Draft — proposed implementation reference only · 0/6 · 0 Open Unknowns of its own · Risk: unlabeled
**Does:** Four-tier path from single-operator advisory to hardware-diverse governance quorum satisfying GOV-008; per-tier minimum config and advancement rules; cross-referenced to `Tests/Field_Logs.md`'s practical entry point (added 2026-08-06).
**Does not (arrow):** Whether Tier 1 suffices for Pathway 1 exit (`GMP` VII.6, open) - the governance-independence bar itself (`GMP` VII, `Governance_Charter.md` GOV-008) - TMR mechanisms (`Operations/Electronics.md`, reused not redefined).
**Explicit non-claim:** "records a path, not a status" — as of last audit, no second physical host exists anywhere in this repository's operating environment.

### `Admin/Nothingness_Theorem.md`
**Status:** Tier 0 — Philosophical Substrate, functionless by doctrine · N/A (Tier 0 exempt) · Risk: N/A
**Does:** Core Theorem (absolute nothingness is not an operational state); 8 Axioms; Ontological Spectrum and realization formalism; structural/topological constraints; category-error and rival-interpretation defenses; entropy/info-theoretic/lifecycle interpretations; cognitive/ethical/memetic corollaries.
**Does not (arrow):** Operational governance rules/predicates (→ CIR, which derives A3/γ2 without promoting this file) - Charter hierarchy - Ethical hard floors - Auditor / ADP protocols - any Spec-Gate-subject specification. Scope Boundary added 2026-08-09 for consistency; Tier 0 exemption unchanged.

### `Admin/PROBE_INVOCATION.md`
**Status:** Draft · N/A (prompt template) · 0 tracked here (see AP-030) · Risk: unlabeled
**Does:** The exact cold-start copy-paste block for one Mission Drift Review cycle; canonical input file list; required output structure.
**Does not (arrow):** Mechanism design/cadence/escalation rules, Invocation Record requirements (both `Auditor_Protocols.md`) - Axiom text (`Governance_Charter.md`).

### `Admin/Progress_Log.md`
**Status:** Active — Living Document · N/A (progression log) · 0 Open Unknowns · Risk: N/A
**Does:** Rolling, dated-heading lessons/continuity log — replaces `Unknowns.md`'s retired "What vX.X Means" section and `Discovery.md`'s removed 19-versions-stale "Attention Required" table (both 2026-08-09).
**Does not (arrow):** Duplicate `Unknowns.md`'s Active Index or any `*_Scope_Map.md`'s per-file content — references IDs, never restates full detail. Substitute for a per-file Resolution Log.
Note: created same day as this Scope_Map build's own findings were still fresh — exists specifically because two other files (this session's own Discovery.md and Unknowns.md work) had independently developed the same failure mode (stale narrative content trapped in structural index files) from opposite directions.

### `Admin/Resolution_Methodology.md`
**Status:** Active — Reference · N/A (named pattern reference, not a specification) · 0 Open Unknowns · Risk: Low
**Does:** Five citable resolution patterns demonstrated 2026-08-15 (dependency-hollowness check, reuse-before-invent, verify-before-accept, digital/equipment-gated split, scope-map stale-pointer pattern); intended as a short Admin-tier reference so the moves can be invoked by name rather than rediscovered.
**Does not (arrow):** Mandatory checklist or Spec Gate requirement · replacement for `Auditor_Protocols.md` / `Forge_Audit_Kit.md` · closure of evidence-gated unknowns by documentation alone · new process gates.

### `Admin/Repository_Integrity_Protocol.md`
**Status:** Draft · 2/6 · 9 Open Unknowns (RIP-001-011) · Risk: High
**Does:** Integrity baselines for protected elements; violation detection/classification/recovery; version preservation (Section 109 hash/line-count anchor rule — see RIP-011); registration latency between sidecars and `Unknowns.md`.
**Does not (arrow):** Crypto implementation (`Security_Protocols.md`) - constitutional doctrine, governance hierarchy (`Governance_Charter.md`) - auditor behavior (`Auditor_Protocols.md`) - Anti-Weaponization doctrine (`Ethical_Constraints.md`).

### `Admin/Repository_Structure.md`
**Status:** Exploration · 0/6 · 1 Open Unknown (RS-001 open; RS-002 resolved 2026-08-09 accepted outlier; RS-003 resolved 2026-08-09) · Risk: Low
**Does:** No-version-suffix filename convention; folder assignment doctrine; root-file doctrine; Archive/ directory doctrine; planned directory addition trigger conditions.
**Does not (arrow):** File content standards (`File_Template.md`) - governance hierarchy (`Governance_Charter.md`) - navigation/current file map - Rename Registry (`Archive/Rename_Registry.md`) - migration procedures (`GMP` Track A) - integrity enforcement (`Repository_Integrity_Protocol.md`).

### `Admin/Safety_Protocols.md`
**Status:** Exploration · 0/6 · 6 Open Unknowns · Risk: High
**Does:** Acceptable risk threshold doctrine; PPE by hazard class; hearing conservation; heat stress doctrine; operator impairment response; pre-operation safety checks; incident reporting.
**Does not (arrow):** Facility constraints (`Architecture/Facilities.md`) - Air Scrubber hardware specs (`Operations/Air_Scrubber.md`) - Anti-Weaponization/Life Preservation hard floors (`Ethical_Constraints.md` — explicitly distinguished as governance constraints, not operational safety) - legal/regulatory compliance (SP-005, human decision).

### `Admin/Security_Protocols.md`
**Status:** Draft · 0/6 · 13 Open Unknowns · Risk: High
**Does:** Multi-signature Human Override Verification crypto; code-signing (RIP Phase 3); node identity/key rotation; air-gapping and cryptographic fallback; trust-boundary declaration.
**Does not (arrow):** Component-level hardware infiltration prevention (`Operations/Electronics.md`) - constitutional doctrine (`Governance_Charter.md`) - auditor behavior (`Auditor_Protocols.md`) - minimum agent quorum definition (GOV-008, `Governance_Charter.md` — this file consumes that threshold as an input) - human-factors attack surface (pending, cross-refs `Safety_Protocols.md` and `Ethical_Constraints.md` EC-011).

### `Admin/Ship_of_Theseus.md`
**Status:** Exploration · 0/6 · 4 Open Unknowns · Risk: Medium
**Does:** Ship of Theseus paradox as repair-first legal/philosophical grounding; Grain system (provenance/identity continuity); right-to-repair defense; AI identity continuity doctrine (Derivative vs. Canonical, ST-003/CF-003).
**Does not (arrow):** Full triage workflow (`Operations/Gate_02_Triage.md`) - minimum seed spec (`Architecture/Geck_forge_seed.md`) - crypto state verification (`Security_Protocols.md`) - split-brain recovery (`Architecture/Cognitive_Frameworks.md`).

### `Admin/Trajectories.md`
**Status:** Exploration · 1/6 · 3 Open Unknowns · Risk: Medium
**Does:** v0 to v5 version trajectory; survival thresholds/exit conditions per version; FRT doctrine and floor (still Placeholder); revenue allocation framework; v0-v1 Trajectory Items registry.
**Does not (arrow):** Future-version component taxonomy (module docs, when active) - detailed economic model (`Economics.md`) - FRT logging procedure (`Operations/Gate_07_Utilization.md`) - component procurement (`Architecture/Geck_forge_seed.md`).

### `Admin/Verification_Gates.md`
**Status:** Draft · 2/6 · 0 Open Unknowns · Risk: High
**Does:** The six canonical verification gates for document promotion; pass criteria and evidence standards per gate; Full Stop Review triggers; gate enforcement rules.
**Does not (arrow):** Auditor role doctrine, sequencing, Adversarial Battery (all `Auditor_Protocols.md`) - condensed reference (`Forge_Audit_Kit.md`) - cryptographic enforcement (`Security_Protocols.md`) - ethical policy (`Ethical_Constraints.md`) - constitutional hierarchy (`Governance_Charter.md`).

---

## Gaps Exposed By Building This

This is the actual test of the format — what juxtaposing all 24 entries surfaced that reading any single file would not have:

1. ~~**`Computational_Institutional_Reasoning.md` has no Scope Boundary section at all.**~~ **Closed 2026-08-09.** Conforming DOES/DOES NOT Scope Boundary added. Was the single most consequential structural gap found on Scope_Map creation.

2. ~~**`Nothingness_Theorem.md` also has none.**~~ **Closed 2026-08-09.** Scope Boundary added for index consistency; Tier 0 / functionless-by-doctrine status explicitly preserved and restated in the boundary itself.

3. ~~**`Autonomy_Divergence_Protocol.md` uses a non-conforming narrative scope statement.**~~ **Closed 2026-08-09.** Normalized to standard DOES/DOES NOT template; prior narrative content preserved and expanded into explicit out-of-scope arrows.

4. **One apparent duplicate turned out not to be one:** `Environmental_Constraints.md`'s ENV-003 and `Ethical_Constraints.md`'s EC-010 both independently claim "jurisdiction conflict hierarchy" — checked directly against `Unknowns.md` rather than flagged on sight, and found already correctly cross-linked there. Neither file's own Scope Boundary text shows that link locally; it only becomes visible by checking the global index. Worth noting as a real limit of this file's method: per-file scope text alone will keep producing false-positive "duplicates" until `Unknowns.md` is also checked, not a substitute for it.

5. **`Governance_Charter.md` is a hub, not just a file** — six other files in this one folder explicitly defer to it by name in their own Out-of-Scope lists (GMP, RIP, CIR_Gov, Hardware_Diversity_Ladder, Security_Protocols, Ethical_Constraints). No single file's own Scope Boundary shows this concentration; only visible once every entry is read together. This matches, and gives independent visual confirmation of, EC-016's 2026-08-07 correction — the Charter genuinely is the hierarchy's real center, which is exactly why the "dual-ownership conflict" framing was wrong: everything already correctly points at one place.

Findings 1–3 (structural scope gaps) closed 2026-08-09. Findings 4–5 remain as method observations, not open defects.

---

## Resolution Log

- 2026-08-09: **Findings 1–3 closed.** Conforming Scope Boundary sections
  added to `Computational_Institutional_Reasoning.md` and
  `Nothingness_Theorem.md`; `Autonomy_Divergence_Protocol.md`'s narrative
  "## 2. Scope" normalized to the standard DOES/DOES NOT template. All
  three Adm_Scope_Map entries updated; Gaps Exposed section annotated.
  No new unknowns registered. Human-directed correction pass.

- 2026-08-07: **File created — pilot for the per-folder Scope_Map pattern**,
  proposed after review of an archived v0.93 `Discovery.md` that attempted
  the same per-file density across the whole repository at once and grew
  to 1300+ lines before being abandoned for that approach. All 24 Admin/
  files' Status/Spec Gates/Open Unknowns/Risk and Scope Boundary content
  extracted directly from source (Python-assisted bulk extraction,
  spot-verified) rather than reconstructed from memory. Three real
  structural gaps surfaced (two files with no Scope Boundary section,
  one non-conforming format) and one apparent duplicate was checked
  against `Unknowns.md` and found to be a false positive — both outcomes
  documented under Gaps Exposed above. No new unknowns registered.
  Human-directed.
