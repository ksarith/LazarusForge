# Forge_Audit_Kit.md
**Version 1.29**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | 0/6 — hold dissolved by human ruling 2026-10-29 (Decision Brief 2026-10-29 item 3, option B; PKC-022 option-B precedent — stale triggers are dissolved, not refreshed): the PKC-042 hold annotation is retired; FAK-014's stale same-day Grok account no longer freezes the field; the gates remain 0/6 and advance only by fresh audit + human ratification (ordinary File Template procedure; no self-approval)                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                    |
| Last Audit     | 2026-10-29 (third same-day) — Vibe (Repo Custodian, delegated maintenance, human-ruled Decision Brief 2026-10-29 item 3, option B): v1.28 → v1.29 — Spec Gates hold dissolved by human ruling (PKC-022 option-B precedent — stale triggers are dissolved, not refreshed; the PKC-042 hold annotation is retired; gates remain 0/6, advancing only by fresh audit + human ratification — no self-approval). No FAK opened or closed; Open Unknowns stays 4. No gate advanced. Prior: 2026-10-29 (second same-day) — Vibe (Repo Custodian, delegated maintenance, human-ratified queue advancement): v1.27 → v1.28 — AVE-R ownership row added to the Governance Sidecar ID Reference (queued Kit AVE- registration; X5 regeneration continuing as the sweep reaches each folder — `Admin/Agent_Verification_Event.md` audited in the AUDIT_27 window; reliance-rule sidecars AVE-R1–R4, AVE-R1 and AVE-R4 mirrored in `Unknowns.md`). No FAK opened or closed; Open Unknowns stays 4. No gate advanced. Prior: 2026-10-29 — Vibe (Repo Custodian, delegated maintenance, human-ratified kit-ceiling retirement): v1.26 → v1.27 — character-count ceiling retired as a Drift Indicator (FAK-005 Resolved by human ruling; PKC-022 option-B precedent: dissolve stale triggers, don't refresh them; cause of record: the mobile paste-instrument era is over — audits run by full-archive fetch); duplication indicator added in its place (changelog-homed history stays out of the kit body); one-time history relocation to the changelog sidecar (Last Audit pre-v1.23 chain, Auditor pre-2026-10-27 entries, Resolution Log Priors v1.19 and older). Open Unknowns 5 → 4. No gate advanced. Prior: 2026-10-28 (later same-day) — Vibe (Repo Custodian, delegated maintenance, human-ratified batch 2026-10-28c): v1.25 → v1.26 — ## File Purpose and ## Assumptions added (AUDIT_15 F1); ## Active Disputes and ## Lessons Learned added (F2); Rule 11 RIP-form logging standard (X4); Post-Audit Cross-Reference same-pass X1/X9 check; ASM- ID-Reference rows regenerated (X5). No gate advanced. Prior: 2026-10-28 — Vibe (Repo Custodian, delegated maintenance, human-ratified AUDIT_15 findings batch): v1.24 → v1.25 — Scope Boundary now lists the Resolved Unknown Discharge Procedure (X1); size drift indicator re-baselined 12,000 → 35,000 with a dated note; companion `Unknowns.md` v5.72 adds this kit's five open FAKs to the Active Index (mirroring gap). No gate advanced. Prior: 2026-10-28 — Vibe (Repo Custodian, delegated maintenance, human-ratified findings batch): v1.23 → v1.24 — Governance Sidecar ID Reference regenerated in part (CF- and GMP- ownership rows added; ASM- disambiguation note added pending the X3 human ruling). No gate advanced. Prior: 2026-10-27 — Vibe (human ruling enacted, PKC-022 option B: pin retirement): Derived-from version pins retired; FAK-014 through FAK-019 closed by ruling (Open Unknowns 11 → 5); header 1.22→1.23; no gate advanced. Older audit history (pre-v1.23 chain) relocated to `Archive/Logs/Forge_Audit_Kit_Changelog.md` §Relocated In-Body History (2026-10-29, v1.27 pass). |
| Auditor        | Vibe — Repo Custodian, 2026-10-29 (third same-day) v1.29 Spec Gates hold dissolution (delegated maintenance, human-ruled Decision Brief 2026-10-29 item 3B); prior: Vibe — Repo Custodian, 2026-10-29 (second same-day) v1.28 ID-Reference AVE-R registration (delegated maintenance, human-ratified queue advancement); prior: Vibe — Repo Custodian, 2026-10-29 v1.27 kit-ceiling retirement + history relocation (delegated maintenance, human-ratified); prior: Vibe — Repo Custodian, 2026-10-28 v1.26 wrapper-hygiene batch 2026-10-28c (delegated maintenance); prior: Vibe — Repo Custodian, 2026-10-28 v1.25 AUDIT_15 wrapper items (delegated maintenance, human-ratified batch); prior: Vibe — Repo Custodian, 2026-10-28 v1.24 ID-Reference regeneration (delegated maintenance, human-ratified batch); prior: Vibe — Skeptic/Auditor, 2026-10-27 pin-retirement ruling enacted, v1.23, FAK-014–019 closed (human-ratified); prior: Vibe — Skeptic/Auditor, 2026-10-27 targeted v1.22 refresh (human-authorized): re-pinned AP v0.45 / Unknowns v5.71, incorporated the PKC-020 findings-only sub-rule into condensed Rule 10, FAK-019 logged, Open Unknowns 10 → 11; prior: Claude — 2026-10-27 PKC-042 hold-reason annotation, header 1.20→1.21 (human-authorized autonomous management); older auditor history (pre-2026-10-27) relocated to `Archive/Logs/Forge_Audit_Kit_Changelog.md` §Relocated In-Body History (2026-10-29, v1.27 pass) |
| Open Unknowns  | 4 — see Sidecar Link                                                 |
| Sidecar Link   | Archive/Logs/Forge_Audit_Kit_Changelog.md#sidecar--auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from (reconciled against, 2026-10-27):** `Admin/Auditor_Protocols.md` | `Admin/Verification_Gates.md` | `Unknowns.md`. Version pins retired per human ruling 2026-10-27 (PKC-022, option B): a plain version delta is not drift; the content-based maintenance trigger and the reconciliation check at audit start are the staleness defense.

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Governing principles · Epistemic Foundation condensed reference · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Audit Opening Checklist · Fallacy checklist · AI contribution rules · Verification gates · Sign-off format · Governance sidecar ID reference · Resolved Unknown Discharge Procedure (X1, added 2026-10-28, AUDIT_15) · How to use

**DOES NOT define:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`) · Full EF constitutional text (→ `Admin/Auditor_Protocols.md` EF-0.0–EF-0.8b) · Full Adversarial Battery (→ `Admin/Auditor_Protocols.md`) · Unknown registry (→ `Unknowns.md`) · File paths and ownership (→ `Discovery.md`) · Governance hierarchy (→ `Admin/Governance_Charter.md`) · Ethical policy (→ `Admin/Ethical_Constraints.md`) · Canonical vocabulary (→ `Admin/Canonical_Terms.md`) · Kit evolution history (→ git log)

---

## File Purpose

This kit is a condensed working reference for audit sessions — governing principles, the Epistemic Foundation checklist, the Verification Maturity Model, truth-provenance labels, gate quick-reference, the Resolved Unknown Discharge Procedure, ID disambiguation, and the audit-session workflow (Post-Audit Cross-Reference → Sign-Off). It exists so a routine audit does not need to load full role doctrine; source files prevail on interpretive questions (see How to Use). *(Added 2026-10-28, AUDIT_15 F1 — the kit carried the working content but had never stated its purpose.)*

---

## Assumptions

- The condensed sections stay subordinate to their sources; on any interpretive question the source file prevails, and the kit is wrong the moment it diverges silently.
- The reconciliation check at audit start is performed honestly — a skipped check is a drift condition, not a formality.
- The 35,000-character ceiling decision stays with the human (re-baselined from 12,000 at v1.25).
- Auditors operate under `Admin/Auditor_Protocols.md` role doctrine; this kit is reference, not authority.

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`
> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`
> Reality is sovereign. Every process, agent, metric, and protocol is merely an imperfect instrument attempting to approach it. — EF-0.0
> Verification seeks sufficient falsifiability, not exhaustive certainty.
> Correct a flawed premise only when it threatens the task's outcome — not for its own sake.

Infinite audit recursion is a governance failure mode. Human override applies to process decisions only — not to `Admin/Ethical_Constraints.md` hard floors. The Epistemic Foundation (EF-0.0–EF-0.8b) is meta-constitutional and may not be amended without human ratification.

**Human Interaction Point Doctrine:** Human interaction points are coarse correction opportunities, not operational dependencies. The system degrades honestly to verified baselines under human unavailability — it does not suspend. Complexity lives inside the system; the interface to the human is deliberately simple. Full doctrine: `Admin/Auditor_Protocols.md` §Governing Principles.

---

## Epistemic Foundation — Condensed Reference

Full text: `Admin/Auditor_Protocols.md` EF-0.0–EF-0.8b. Runtime checklist only — source prevails on interpretive questions.

| Section | Core Rule |
|---------|-----------|
| EF-0.0 Epistemic Anchor | Reality > utility/consensus/elegance/coherence. All claims: VERIFIED / PROVISIONAL / UNKNOWN. Collapse UNKNOWN→VERIFIED without empirical input is prohibited. Reward falsification = reward confirmation. |
| EF-0.1 Epistemic Filter | Disqualified as evidence: fluency, agent consensus, systemic utility, precedent, correlation, repetition, confidence scores, compression. May generate hypotheses; never verify. |
| EF-0.2 Decay Triggers | L1 (confidence-accuracy mismatch / agent disagreement) → Red-Team. L2 (prediction failure / sycophancy loop) → Quarantine + autonomous degradation to verified baseline; human review when available. L3 (suppression / tampering / metric override) → Epistemic Reset + mandatory human governing party review. |
| EF-0.3 Epistemic Ledger | Five fields per state correction: Previous Premise · Contradictory Evidence · Falsification Method · Updated State · Confidence Interval. Created on falsification only. |
| EF-0.4 Auditor Fallibility | Auditor has no exemption from Axiom Zero. Auditor conclusions are PROVISIONAL. Guardians require guardians. |
| EF-0.5 Anti-Sacralization | No document immune from challenge — including this kit. Stability = repeated verification, not prestige. |
| EF-0.6 Goodhart's Law | Metrics are indicators, not objectives. No optimization overrides contradictory observations to preserve KPI. |
| EF-0.7 Process Supervision | Evaluate reasoning pathways, not outputs. Monitor Machiavellian Gap. Inspectable lineage required. |
| EF-0.8 SW Grounding | Code execution, telemetry, tool returns are the hard floor. Agent narratives about tool outputs are PROVISIONAL until tool confirmation logged. |
| EF-0.8b Physical Grounding | Sensor telemetry, assay outputs, measured physical constants supersede model/simulation/inference. Simulation confirming simulation is not grounding. |

---

## Verification Maturity Model

| State             | Operational Status         |
|-------------------|----------------------------|
| Exploration       | Not operational            |
| Candidate Spec    | Internal review only       |
| Provisional Spec  | Limited operational use    |
| Operational Spec  | Deployable                 |
| Hardened Doctrine | Trusted baseline           |

Promotion rule: assumptions narrow, unknowns shrink, external validation expands.

---

## Truth Provenance Labels

**Quantitative** (`Admin/Auditor_Protocols.md` §Evidence Classification; five-label system confirmed canonical via AP-021, 2026-07-10 — "Estimated" retired, relabel prior Estimated claims as Analogous or Simulated):
Measured | Replicated | Simulated | Analogous | Placeholder — Unlabeled = Placeholder.
Measured requires `m_phys ≥ 0.75`; Replicated additionally requires `m_rep ≥ 0.50` (`Admin/Verification_Gates.md` Gate 2, active 2026-07-10).

**Institutional:** Internally Derived | Analogous External | Experimentally Verified | Operationally Hardened

No internally-derived claim may be represented as Operationally Hardened without external validation. Full doctrine: `Admin/Auditor_Protocols.md` §Evidence Classification and Institutional Truth Provenance Hierarchy.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high: Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure | Governance Authority

Partial Battery allowed for Exploration-stage if deferred classes are documented and no safety-critical claims are present.

---

## Audit Opening Checklist

Execute before every document review. Do not skip steps.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1–P-4, Q-1–Q-4) match prior committed version in `Admin/Governance_Charter.md`. Any unratified wording change = Constitutional violation → STATE_HOLD immediately.

**2. Epistemic Foundation Integrity Check**
Confirm EF-0.0 through EF-0.8b text in `Admin/Auditor_Protocols.md` matches prior committed version. Any unratified modification = Integrity Violation (EF-0.2 Level 3) → STATE_HOLD immediately.

**3. Expiry Watch (file-scoped only — do not pre-load repo-wide findings)**
Check the target file's own Auditor Notes & Unknowns sidecar for entries
at or past the Cycle threshold (see `Admin/Canonical_Terms.md` §4 — one
calendar year by default, operator-adjustable; **not** one audit pass, a
distinction that matters — see Drift Indicators) without a substantively-
updated Resolution Path. If `AUDIT_HARNESS.py`'s boundary index is present
in session, use it — aging is pre-computed per file. Otherwise compute
directly from the target file's own sidecar entries.

Do not consult `Unknowns.md`'s repo-wide Critical/Blocking list before
auditing. This step is scoped to the target file's own registered
unknowns only — independent verification means assessing the file as it
actually reads, not confirming a pre-loaded expectation of what should be
wrong with it (EF-0.1: agent consensus and precedent are disqualified as
evidence). The full registry is consulted afterward — see Post-Audit
Cross-Reference.

**4. Semantic Stability Check**
Scan for high-drift-risk terms. Flag as [FALLACY 4 — Semantic Drift]. Route to `Admin/Canonical_Terms.md`.

| Term | Risk |
|------|------|
| Recycling | Use Value Preservation or Material Recovery |
| Autonomous Decision-Making (unbound) | Obscures Axiom P-4 override visibility |
| High-RPM (on Gate_04) | Terminology bleed from Gate_05 |
| Canonical (unqualified) | Five distinct usages |
| Safe / Contained / Stable / Sufficient | Context-dependent — tighten or log |
| Scrap | Conflates material states |
| Specification (on Exploration content) | Implicit promotion |
| VERIFIED / PROVISIONAL / UNKNOWN | Must match EF-0.0 definitions exactly — do not use informally |
| Operational Blocking / Epistemic Blocking | Distinct subtypes — do not conflate; see `Admin/Canonical_Terms.md` v0.3 |

---

## Fallacy Checklist

Substantive notes required — bare checkmarks are not verification. Full text: `Admin/Auditor_Protocols.md`.

1. **Magic Energy** — Every watt needs a traceable origin. Cross-ref `Operations/Energy.md`.
2. **Friction Blindness** — Real systems degrade. Account for losses and wear.
3. **Energy Density Paradox** — Does recovery cost more than it produces?
4. **Semantic Drift** — Terms must match across all files and sessions. Route conflicts to `Admin/Canonical_Terms.md`.
5. **Scope Creep** — New capabilities belong in `Admin/Trajectories.md`.
6. **Hallucinated Files** — All cross-references must resolve against `Discovery.md`. Aspirational = labeled *planned*.
7. **Confidence Without Basis** — Label all numbers. Unlabeled = Placeholder.
8. **Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life.
9. **Incomplete by Omission** — What critical subsystem is missing?
10. **The Turd Problem** — Strip to one falsifiable sentence. Do not rename this.

---

## AI Contribution Rules

Role declaration required: *"Operating as [Role] per Auditor_Protocols.md v[live version]"* (use the live version at audit time; `Admin/Auditor_Protocols.md`'s own template pins it and is the source of truth)

Valid roles: Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

1. No Invented Files — confirm against `Discovery.md`.
2. Role Declaration — declare before contributing; declare shifts before proceeding.
3. Lineage Tracking — note what changed, why, what it replaces.
4. Refusal is Valid — flag flawed premises; do not refine them.
5. Confidence Labeling — four-label system. Unlabeled = Placeholder.
6. Inter-Agent Consistency — open with Assumption Extraction.
7. Repository Structure Awareness — use canonical folder-prefixed paths.
8. Epistemic State Labeling — claims that cannot reach VERIFIED must be labeled PROVISIONAL or UNKNOWN. Do not collapse epistemic states under optimization pressure.
9. Resolution Claims Require Governance Access (AP-033) — no contribution may mark, or by structure imply, that any unknown has advanced toward Resolved/Closed status without confirmed access to `Admin/Auditor_Protocols.md`'s own Resolution Taxonomy at the time of writing. Without that access, proposed closure mechanisms are candidate methodology only — never status.
10. External Pseudo-Audit Scope and Logging Destination (AP-035) — a pseudo-audit (Spec Gates/Verification thresholds locked, no ratification authority) may not assert inventory/file/content claims without stating direct verification against the payload; may not invent a local ID prefix for cross-module unknowns; may not generate a freestanding ledger file as the primary record. Findings go first in the owning file's own sidecar; only genuinely cross-module findings get a `Unknowns.md` entry, added by an agent with confirmed sidecar access. Rule 10 addendum (PKC-020, human ruling 2026-10-25): a findings-only pseudo-audit does not advance the owning file's Last Audit or Auditor field — it is logged in the Resolution Log as a pseudo-audit, findings only, and Last Audit keeps the date of the last real audit; a body-changing pass bumps Last Audit and Auditor, as already practiced.
11. RIP-Form Logging Standard (X4, human-ratified batch 2026-10-28c) — every pass that edits a target file's body records its own dated Resolution Log entry in that file (what changed, why, ratification source); multi-file batches get one entry per file, and findings-only passes record only the pseudo-audit ledger line (PKC-020).

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass by different agent to override.

| Gate | Test | Fail → |
|------|------|--------|
| G1 | Fallacy Checklist actively applied with substantive notes? | Return to author |
| G2 | Physical plausibility — no violation of known constraints? | Return for revision |
| G3 | Adversarial Battery applied proportional to coupling/risk? | Return for adversarial analysis |
| G4 | Scope alignment — fits current version or trajectory? | Route to `Admin/Trajectories.md` |
| G5 | Cross-reference integrity — all paths use canonical folder-prefixed names? | Hold at draft |
| G6 | Conflict check — no contradiction with existing committed specs? | Resolve before committing |

**Gate scope vs. promotion readiness (source: `Admin/Verification_Gates.md` §Gate 3, §Gate 6, §Promotion Requirements Summary — the canonical gate-definition layer this kit condenses):** Gates test a document's own execution quality — was the check actually done, documented, and does the committed text avoid contradiction. Gates do **not** test whether unknowns a check surfaced have been resolved. "All six gates pass" and "open unknowns are non-blocking" are two separate, independently required conditions for Specification promotion — a document can clear all six gates while promotion stays blocked by open unknowns, and that is not a gate failure.

- **G2 evidentiary backing (active 2026-07-10, source: `Admin/Verification_Gates.md` Gate 2, VG-002):** a claim labeled Measured or Replicated must meet the evidentiary thresholds in Truth Provenance Labels above (`m_phys ≥ 0.75`; Replicated additionally `m_rep ≥ 0.50`). Simulated and Analogous remain self-asserted pending a future revision. Enforcement is manual — `AUDIT_HARNESS.py` does not yet compute or check the evidence vector; an auditor applying G2 must check this by hand.
- **G3** passes if the Adversarial Battery was applied and documented — full Battery, or partial with deferred classes named and reasoned (Exploration-stage default per §Adversarial Audit Layer "When to Apply"). G3 does not require that findings from the Battery be resolved; unresolved Critical findings block *promotion*, tracked as open unknowns, not as a G3 failure.
- **G6** passes if the committed text does not contradict itself or another *committed* spec. G6 does not test whether upstream dependencies are resolved — that is a promotion-readiness question.

**Gate 3 status is not permanent.** A resolved blocker is not automatically a passed gate — re-verify Gate 3's actual blocking status at each audit rather than assuming a prior "cleared" or "blocked" note still holds. Full incident history (a 2026-07-05 case where this went wrong in both directions) in `Archive/Logs/Forge_Audit_Kit_Changelog.md`.

**Physical harness note (AP-010 pending):** For documents with physical implementation claims, Gate 6 requires at least one confirmed cross-reference to an active test harness specifying test and grounding artifact. Documents without physical claims are exempt.

**Full Stop Review triggers:** Same claim blocked across two cycles · New finding invalidates core premise of a promoted spec · Pattern of overrides eroding a governance principle · Multiple Adversarial Battery findings converging on the same structural gap · EF-0.2 Level 2 or Level 3 trigger activated.

---

## Resolved Unknown Discharge Procedure

Canonizes the pattern first applied at RIP-001 (`Admin/Repository_Integrity_Protocol.md`, discharged 2026-06-27) and retroactively corrected at RIP-004 (2026-07-02, see step 6 note). Applies whenever any unknown, any prefix, closes.

1. Sidecar entry stays permanently in the owning file's Auditor Notes & Unknowns — **never deleted.** The ID is the permanent search anchor; there is no centralized archive to fall back on (`Unknowns.md` retired that model at v4.3 — see its Resolution Log).
2. Status field → `Resolved — Discharge via Lessons Learned`.
3. Add a **Resolution** field to the sidecar entry: what closed it, when, why.
4. Add a **Lessons Learned** field to the same sidecar entry: the transferable pattern, not just the outcome — what would a future agent facing a similar unknown need to know.
5. Add a matching row to the owning file's own top-level Lessons Learned table — distilled and pattern-focused, not a duplicate of step 3.
6. `Unknowns.md`: remove from the active index; add one line to Expiry Watch or the Audit Trail pointing back to the sidecar. **Do not skip steps 2–5 and jump to step 6** — RIP-004 was closed correctly in substance on 2026-06-19 but skipped steps 2, 4, and 5 for six weeks before being brought into conformance.
7. Bump the owning file's Open Unknowns count and add a Resolution Log entry.

---

## Post-Audit Cross-Reference

Perform after independent findings are drafted from the target file
alone — never before. Check `Unknowns.md`'s "Critical and Blocking
unknowns only" cross-reference table for entries tied to this file that
its own sidecar didn't surface: cross-file collisions, shared blocking
chains, prefix ambiguity (e.g. the EC- collision under CT-007). Note any
gap between the file's own sidecar and the registry as a new finding, not
a silent correction to either.

This step is a completeness check on an audit already performed, not a
source of findings to look for going in — auditing toward a pre-loaded
list is what Expiry Watch (step 3) exists to avoid. Its output populates
Sign-Off's `Unknowns logged` field below.

**Same-pass reconciliation (X1/X9, human-ratified batch 2026-10-28c):** a pass that enacts its own findings must, in that same pass, (a) update the target file's Scope Boundary DOES/DOES-NOT lists if the change alters what the file defines, and (b) reconcile any "to be registered/reconciled" narration it touches to the done-state — narrating a pending action the same pass could have completed is a wrapper-decay defect (X11), not a to-do.

---

```
Document: [filename] ([status] audit, [date])
Auditor: [Role] — [Agent]
Verification maturity: [state]
Truth basis: [provenance level]
Adversarial classes applied: [list]
Adversarial classes deferred: [list + reason]
Highest-risk finding: [one sentence]
Gates cleared: [list]
Gates blocked: [list with reason]
Unknowns logged: [IDs]
Overrides: [none / list with justification]
Sign-off: [one sentence summary]
```

---

## Governance Sidecar ID Reference

Non-obvious governance prefixes only. All operational prefixes: load `Discovery.md` or `Routing.md`.

| Prefix | Owning File |
|--------|-------------|
| AP-    | `Admin/Auditor_Protocols.md` |
| AVE-R  | `Admin/Agent_Verification_Event.md` |
| CT-    | `Admin/Canonical_Terms.md` |
| CF-    | `Architecture/Cognitive_Frameworks.md` |
| CIR-   | `Admin/Computational_Institutional_Reasoning.md` |
| EC-    | `Admin/Ethical_Constraints.md` |
| FAK-   | `Admin/Forge_Audit_Kit.md` |
| GH-    | `Tests/Cognitive_Salvage_Layer.md` |
| GOV-   | `Admin/Governance_Charter.md` |
| GMP-   | `Admin/Governance_Migration_Protocol.md` |
| RIP-   | `Admin/Repository_Integrity_Protocol.md` |
| SEC-   | `Admin/Security_Protocols.md` |

**ASM- disambiguation (X5, regenerated 2026-10-28, human-ratified batch 2026-10-28c):** ASM- is an assumption-series ID with no single owner — each file numbers its own series independently; cite ASM- with its qualifying File.md (PKC-003). Known series:

| Series | File |
|--------|------|
| ASM-001–006 | `Admin/Governance_Charter.md` |
| ASM-001–006 | `Admin/Repository_Integrity_Protocol.md` |
| ASM- series | `Admin/Governance_Migration_Protocol.md` |
| ASM-001–006 | `Admin/Safety_Protocols.md` |
| ASM-001–004 | `Admin/Engineer_Protocols.md` |
| ASM- series | `Admin/Verification_Gates.md` |
| ASM- series | `Admin/Canonical_Terms.md` |
| ASM-001–003 | `Admin/Repository_Structure.md` |
| ASM-001–003 | `Admin/Metrics_Scaffold.md` |
| ASM-001–005 | `Admin/Economics.md` |
| ASM- citations | `Architecture/Components.md`, `Operations/Gate_02_Triage.md` |

*Regeneration of remaining prefixes proceeds as the audit sweep reaches each folder (ratified batch 2026-10-28c). CF- and GMP- rows were added at v1.24 per the AUDIT_06/AUDIT_02 recommendations; the AVE-R row at v1.28 (2026-10-29) per the queued Kit AVE- registration — `Admin/Agent_Verification_Event.md` was campaign-audited in the AUDIT_27 window (reliance-rule sidecars AVE-R1–R4; AVE-R1 and AVE-R4 mirrored in `Unknowns.md`).*

---

## How to Use

Load this file plus the document under audit. That is the baseline for every routine audit session.

Load additional files only when the audit focus requires them — each adds tokens. Candidates: `Admin/Auditor_Protocols.md` (full role doctrine, full EF constitutional text, full Adversarial Battery), `Unknowns.md` (full unknown detail), `Discovery.md` (path lookup, Rename Registry), target file's upstream architecture files.

**Token ceiling note:** `Admin/Auditor_Protocols.md` is approximately 146,700 characters at v0.41 (measured directly via harness fetch, 2026-08-30 — prior figure of ~157,000 was itself measured at v0.24; the file has grown in content — Rules 9/10, AP-033/034/035 — while trimming duplicated version-history narrative elsewhere, netting slightly smaller despite more doctrine). Load it only when auditing the file itself, onboarding a new agent, or when full EF constitutional text is required for an interpretive dispute. This kit is the runtime reference for all other sessions. (Re-measured 2026-10-10 at v0.42: 150,529 bytes via `wc -c`, not a character count from harness fetch, so not directly comparable to the figure above.)

**Load full source documents instead of this kit when:** auditing `Admin/Auditor_Protocols.md` itself · onboarding a new agent · full unknown entry detail required · EF section interpretive dispute.

**Maintenance trigger:** Update this file when a source changes a section this kit condenses or copies: `Admin/Auditor_Protocols.md` (role declaration template, EF-0.0–EF-0.8b text, sign-off format, AI Contribution Rules), `Admin/Verification_Gates.md` (gate definitions), or `Unknowns.md` (Expiry Watch / Expiry Rule wording, the Critical-and-Blocking cross-reference, the Resolved Unknown Discharge Procedure, the Governance Sidecar ID Reference). A plain version increment of any source is **not** a trigger. When you do update, set the reconciled-against versions and date in the Derived-from line. Minimum fields to update: the reconciled-against line, and the EF condensed section if EF sections changed. (The role-declaration example no longer pins a version, so it is not an update target.)

**Reconciliation check at audit start:** Read each source's own version history for changes to the sections listed above before relying on this kit for them, and report any mismatch as a drift flag in the sign-off. (Version pins retired 2026-10-27, human ruling PKC-022 option B — a version delta alone is not drift; content is. Critical watch list removed at v1.10 — no longer a maintenance target.)

**End-of-Life:** This kit is a working document, not a permanent one — its function is to stay current with `Admin/Auditor_Protocols.md`, `Admin/Verification_Gates.md`, and `Unknowns.md`. When it's superseded — a successor kit, a structural change to the audit process, or the source documents outgrowing what a condensed reference can track — it is not deleted. It's shelved at its final version as a historical record: evidence of what the audit process actually was at a given point in Forge's evolution, available for ideological and process study rather than active use. Superseding a kit is a normal lifecycle event, not a failure; the sidecar and version history in `Archive/Logs/Forge_Audit_Kit_Changelog.md` are what make that shelving legible later rather than just an abandoned file.

---

## Active Disputes

| ID | Dispute | Status |
|----|---------|-------|

*(None open — added 2026-10-28, AUDIT_15 F1/F2; empty table per template requirement.)*

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence |
|------|---------------|----------------|-------------|------------------|------------|
| 2026-09-03 → 2026-10-10 | Internally Derived | Version-pinned derivation citations (FAK-014–018 lineage) | Went stale six times across five versions; same-day audits cleared gates without catching it | Content-based maintenance triggers and live-version placeholders beat version pins; reconciliation is checked at audit start, not assumed | High |

*(Table added 2026-10-28, AUDIT_15 F2, seeded from the kit's own FAK-014–018 recurrence record; Evidence Type vocabulary per File_Template §7.)*

---

## Drift Indicators

- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- A source this kit condenses or copies has changed a listed section since the Derived-from reconciliation date, and the kit was not updated (a newer version number alone is not drift)
- Expiry Watch step diverges from `Unknowns.md`'s current Expiry Watch / Expiry Rule wording
- Role declaration example pins a version number instead of the live-version placeholder
- Epistemic Foundation condensed section diverges from EF-0.0–EF-0.8b source text without documented rationale
- VERIFIED / PROVISIONAL / UNKNOWN used inconsistently with EF-0.0 definitions
- Governance sidecar ID reference contains stale or flat filenames
- Ethical Anchor absent or altered
- Resolved unknown missing Lessons Learned narrative field, matching top-table row, or discharge status suffix (Resolved Unknown Discharge Procedure skipped)
- Gate status language conflates "check coverage complete" with "promotion blocked by open unknowns" (see Gate scope vs. promotion readiness note)
- Kit body carries changelog-homed history — version entries older than the current audit window belong in `Archive/Logs/Forge_Audit_Kit_Changelog.md` (their designated home since v1.10); relocate, keeping the latest entries plus the pointer. *(Replaces the character-count ceiling trigger, retired 2026-10-29 by human ruling, FAK-005 closed: the 12,000-then-35,000-char limit was a constraint of the kit's mobile cut-paste era — a live ceiling while the kit was hand-carried and token-condensed at run time — not an intrinsic virtue of an audit instrument. Audits are now performed by full-archive fetch and direct prompting (FAK-014's 2026-09-03 record), so the trigger's cause of record is gone and it is dissolved, not re-baselined (PKC-022, option B: dissolve stale triggers, don't refresh them). Kit size remains a reported trend metric — roughly 40,000 characters at v1.26, before this pass's history relocation — not a trigger.)*
- "Cycle" (Expiry Watch, aging language) conflated with "audit pass" rather than the calendar-based definition in `Admin/Canonical_Terms.md` §4 — see CT-011

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

Sidecar relocated to `Archive/Logs/Forge_Audit_Kit_Changelog.md` §Sidecar as of
v1.11 (2026-07-14) — this kit is a working document, and its self-tracking
content was accumulating alongside the reference content it exists to
keep lean. This is a documented exception to the general rule that
sidecar entries live in the owning file; every other file in the
repository keeps its sidecar in-body. Adversarial Battery record for
this kit is in the same file, §Adversarial Battery Record.

Current: 4 open (FAK-001, FAK-006, FAK-009, and one flagged for
`Canonical_Terms.md` rather than resolved here — see Battery record, Cycle/CURRENT_CYCLE
finding). FAK-005 closed 2026-10-29 by human ruling: the character-count ceiling retired
as a Drift Indicator at v1.27 (PKC-022, option B: dissolve stale triggers, don't refresh
them); closure note in the changelog sidecar. FAK-014 through FAK-019 closed 2026-10-27 by
human ruling (PKC-022, option B: pin retirement) — Payment via Constitutional Decision,
ratification completes on commit; closure notes on each entry in the changelog sidecar.

---

## Resolution Log

Full history: `Archive/Logs/Forge_Audit_Kit_Changelog.md` (relocated out of this
kit at v1.10 — add new entries there, not here).

Most recent: v1.29 (2026-10-29) — Spec Gates hold dissolved by human ruling (Decision Brief 2026-10-29 item 3, option B; PKC-022 option-B precedent — stale triggers are dissolved, not refreshed): the PKC-042 hold annotation (v1.21) is retired — FAK-014's account of a same-day 2026-09-03 Grok audit that "cleared all six gates" remains stale (the body changed since, v1.16–v1.20); the ruling dissolves the hold, not the staleness. The gates remain 0/6 and advance only by the ordinary File Template procedure — fresh audit + human ratification; no self-approval. Successor-auditor naming is deferred to campaign end by the same brief's item 5 ruling, so no fresh audit is scheduled before then. No FAK opened or closed; Open Unknowns stays 4. Header 1.28→1.29. No gate advanced.

Prior: v1.28 (2026-10-29) — AVE-R ownership row added to the Governance Sidecar ID Reference (queued Kit AVE- registration; X5 regeneration continuing as the sweep reaches each folder — `Admin/Agent_Verification_Event.md` audited in the AUDIT_27 window; reliance-rule sidecars AVE-R1–R4, AVE-R1 and AVE-R4 mirrored in `Unknowns.md`). No FAK opened or closed; Open Unknowns stays 4. Header 1.27→1.28. No gate advanced.

Prior: v1.27 (2026-10-29) — Kit-ceiling retirement (human-ratified): 35,000-char ceiling dissolved as a Drift Indicator (FAK-005 Resolved; PKC-022 option-B precedent: dissolve stale triggers, don't refresh them; the ceiling was a constraint of the mobile paste-instrument era, not an intrinsic virtue of an audit instrument); duplication indicator added (changelog-homed history stays out of the kit body); Last Audit, Auditor and Resolution Log pre-cutoff history relocated to the changelog sidecar §Relocated In-Body History; File State Open Unknowns 5 → 4. Header 1.26→1.27. No gate advanced.

Prior: v1.26 (2026-10-28) — Wrapper-hygiene batch 2026-10-28c (human-ratified): ## File Purpose + ## Assumptions (AUDIT_15 F1); ## Active Disputes + ## Lessons Learned (F2); Rule 11 RIP-form logging standard (X4); Post-Audit Cross-Reference same-pass X1/X9 check; ASM- disambiguation rows regenerated (X5). Header 1.25→1.26. No gate advanced.

Prior: v1.25 (2026-10-28) — AUDIT_15 wrapper items enacted (human-ratified batch): Scope Boundary lists the Resolved Unknown Discharge Procedure (X1); size drift indicator re-baselined 12,000 → 35,000 with a dated note (measured 33,857 at v1.24); companion `Unknowns.md` v5.72 adds this kit's five open FAKs to its Active Index. Header 1.24→1.25. Changelog entry in `Archive/Logs/Forge_Audit_Kit_Changelog.md`.

Prior: v1.24 (2026-10-28) — ID Reference regenerated in part (CF- and GMP- rows added; ASM- note added pending the X3 ruling). Header 1.23→1.24. Changelog entry in `Archive/Logs/Forge_Audit_Kit_Changelog.md`.

Prior: v1.23 (2026-10-27) — Pin retirement enacted (human ruling, PKC-022 option B, ratification completes on commit): the Derived-from line's version pins are retired (sources and reconciliation date kept); the reconciliation check at audit start reworded to read source content histories, not version deltas; FAK-014 through FAK-019 closed by the same ruling (the recurring pin-staleness class is dissolved, not refreshed); Open Unknowns 11 → 5; header 1.22→1.23. Changelog entry and closure notes in `Archive/Logs/Forge_Audit_Kit_Changelog.md`.

Prior: v1.22 (2026-10-27) — Targeted derivation re-pin and PKC-020 incorporation (human-authorized; PKC-022 lag clearance): Derived-from line re-pinned to `Auditor_Protocols.md` v0.45 and `Unknowns.md` v5.71 (`Verification_Gates.md` confirmed unchanged at v0.7); the condensed AI Contribution Rules Rule 10 gained the PKC-020 findings-only sub-rule from AP v0.45's Rule 10 addendum; FAK-019 logged (seventh occurrence of the pin-staleness pattern); Open Unknowns 10 → 11; header 1.21→1.22. The pin-vs-retire structural question is untouched and remains open by human direction. Changelog entry added in `Archive/Logs/Forge_Audit_Kit_Changelog.md`.

Prior: v1.21 (2026-10-27) — Spec Gates hold reason annotated (PKC-042): FAK-014's account of a same-day Grok audit that "cleared all six gates" on 2026-09-03 is treated as stale; the header stays 0/6; no gate is advanced without a fresh audit and human ratification. Header 1.20→1.21; changelog entry added in `Archive/Logs/Forge_Audit_Kit_Changelog.md`. No FAK entry opened or closed.

Prior: v1.20 (2026-10-10) — FAK-018 logged: derivation citations went
stale a sixth time (`Auditor_Protocols.md` v0.41 → live v0.42; `Unknowns.md`
v5.57 → v5.58), found by an independent audit run and confirmed against both
files. Strings refreshed (including the role-declaration string); header
1.19→1.20; Open Unknowns 9 → 10. Whether `Auditor_Protocols.md` v0.42 changed
EF text was not checked (no v0.41 copy to diff). The maintenance-trigger
question from FAK-014 to FAK-017 is still open; a same-day mitigation
removed the daily-stale pin (role-declaration example now uses a live-version
placeholder; Derived-from line labeled reconciled-against) and made the
maintenance trigger content-based, with a reconciliation check at audit start. Full account in
`Archive/Logs/Forge_Audit_Kit_Changelog.md`.

*Older entries (v1.19 and earlier) relocated to `Archive/Logs/Forge_Audit_Kit_Changelog.md` §Relocated In-Body History, 2026-10-29 (v1.27 history-relief pass); their full accounts were already in that changelog's Version History section.*
