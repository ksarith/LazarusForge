# Forge_Audit_Kit.md
**Version 1.14**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                    |
| Last Audit     | 2026-07-28                                                          |
| Auditor        | Claude — Synthesizer; Claude — v1.10 reduction + Expiry Watch redesign (human-directed); Claude — self-audit + v1.11 (FAK-010/011/012, First Battery) — 2026-07-14; Claude — v1.12 Verification Gates trim (human-directed), derivation versions corrected, 2026-07-17; Claude — v1.13 Pragmatic Accuracy principle added (human-directed), 2026-07-26; Claude — v1.14 CIR- prefix registered, FAK-013 stale changelog path corrected (human-directed), 2026-07-28 |
| Open Unknowns  | 5 — see Sidecar Link                                                |
| Sidecar Link   | Archive/Logs/Forge_Audit_Kit_Changelog.md#sidecar--auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.24 | `Admin/Verification_Gates_LF.md` v0.7 | `Unknowns.md` v4.21

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Governing principles · Epistemic Foundation condensed reference · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Audit Opening Checklist · Fallacy checklist · AI contribution rules · Verification gates · Sign-off format · Governance sidecar ID reference · How to use

**DOES NOT define:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`) · Full EF constitutional text (→ `Admin/Auditor_Protocols.md` EF-0.0–EF-0.8b) · Full Adversarial Battery (→ `Admin/Auditor_Protocols.md`) · Unknown registry (→ `Unknowns.md`) · File paths and ownership (→ `Discovery.md`) · Governance hierarchy (→ `Admin/Governance_Charter.md`) · Ethical policy (→ `Admin/Ethical_Constraints.md`) · Canonical vocabulary (→ `Admin/Canonical_Terms.md`) · Kit evolution history (→ git log)

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
Measured requires `m_phys ≥ 0.75`; Replicated additionally requires `m_rep ≥ 0.50` (`Admin/Verification_Gates_LF.md` Gate 2, active 2026-07-10).

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

Role declaration required: *"Operating as [Role] per Auditor_Protocols.md v0.24"*

Valid roles: Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

1. No Invented Files — confirm against `Discovery.md`.
2. Role Declaration — declare before contributing; declare shifts before proceeding.
3. Lineage Tracking — note what changed, why, what it replaces.
4. Refusal is Valid — flag flawed premises; do not refine them.
5. Confidence Labeling — four-label system. Unlabeled = Placeholder.
6. Inter-Agent Consistency — open with Assumption Extraction.
7. Repository Structure Awareness — use canonical folder-prefixed paths.
8. Epistemic State Labeling — claims that cannot reach VERIFIED must be labeled PROVISIONAL or UNKNOWN. Do not collapse epistemic states under optimization pressure.

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

**Gate scope vs. promotion readiness (source: `Admin/Verification_Gates_LF.md` §Gate 3, §Gate 6, §Promotion Requirements Summary — the canonical gate-definition layer this kit condenses):** Gates test a document's own execution quality — was the check actually done, documented, and does the committed text avoid contradiction. Gates do **not** test whether unknowns a check surfaced have been resolved. "All six gates pass" and "open unknowns are non-blocking" are two separate, independently required conditions for Specification promotion — a document can clear all six gates while promotion stays blocked by open unknowns, and that is not a gate failure.

- **G2 evidentiary backing (active 2026-07-10, source: `Admin/Verification_Gates_LF.md` Gate 2, VG-002):** a claim labeled Measured or Replicated must meet the evidentiary thresholds in Truth Provenance Labels above (`m_phys ≥ 0.75`; Replicated additionally `m_rep ≥ 0.50`). Simulated and Analogous remain self-asserted pending a future revision. Enforcement is manual — `AUDIT_HARNESS.py` does not yet compute or check the evidence vector; an auditor applying G2 must check this by hand.
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
| CT-    | `Admin/Canonical_Terms.md` |
| CIR-   | `Admin/Computational Institutional Reasoning` |
| EC-    | `Admin/Ethical_Constraints.md` |
| FAK-   | `Admin/Forge_Audit_Kit.md` |
| GH-    | `Tests/Cognitive_Salvage_Layer.md` |
| GOV-   | `Admin/Governance_Charter.md` |
| RIP-   | `Admin/Repository_Integrity_Protocol.md` |
| SEC-   | `Admin/Security_Protocols.md` |

---

## How to Use

Load this file plus the document under audit. That is the baseline for every routine audit session.

Load additional files only when the audit focus requires them — each adds tokens. Candidates: `Admin/Auditor_Protocols.md` (full role doctrine, full EF constitutional text, full Adversarial Battery), `Unknowns.md` (full unknown detail), `Discovery.md` (path lookup, Rename Registry), target file's upstream architecture files.

**Token ceiling note:** `Admin/Auditor_Protocols.md` is approximately 157,000 characters at v0.24 (measured directly via harness fetch, 2026-07-21 — prior figure of ~100,000 was stale, likely last checked before AP-018 through AP-024 were added). Load it only when auditing the file itself, onboarding a new agent, or when full EF constitutional text is required for an interpretive dispute. This kit is the runtime reference for all other sessions.

**Load full source documents instead of this kit when:** auditing `Admin/Auditor_Protocols.md` itself · onboarding a new agent · full unknown entry detail required · EF section interpretive dispute.

**Maintenance trigger:** Update this file when `Admin/Auditor_Protocols.md` is revised OR when `Unknowns.md` version increments. Minimum fields to update: derivation version strings, role declaration version string, EF condensed section if EF sections changed. (Critical watch list removed at v1.10 — no longer a maintenance target.)

**End-of-Life:** This kit is a working document, not a permanent one — its function is to stay current with `Admin/Auditor_Protocols.md`, `Admin/Verification_Gates_LF.md`, and `Unknowns.md`. When it's superseded — a successor kit, a structural change to the audit process, or the source documents outgrowing what a condensed reference can track — it is not deleted. It's shelved at its final version as a historical record: evidence of what the audit process actually was at a given point in Forge's evolution, available for ideological and process study rather than active use. Superseding a kit is a normal lifecycle event, not a failure; the sidecar and version history in `Archive/Logs/Forge_Audit_Kit_Changelog.md` are what make that shelving legible later rather than just an abandoned file.

---

## Drift Indicators

- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- Derivation statement references a superseded version of `Admin/Auditor_Protocols.md` or `Unknowns.md`
- Expiry Watch not updated at `Unknowns.md` version increment
- Role declaration version string does not match current `Admin/Auditor_Protocols.md` version
- Epistemic Foundation condensed section diverges from EF-0.0–EF-0.8b source text without documented rationale
- VERIFIED / PROVISIONAL / UNKNOWN used inconsistently with EF-0.0 definitions
- Governance sidecar ID reference contains stale or flat filenames
- Ethical Anchor absent or altered
- Resolved unknown missing Lessons Learned narrative field, matching top-table row, or discharge status suffix (Resolved Unknown Discharge Procedure skipped)
- Gate status language conflates "check coverage complete" with "promotion blocked by open unknowns" (see Gate scope vs. promotion readiness note)
- Kit character count exceeds 12,000 — flag for reduction pass
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

Current: 5 open (FAK-001, FAK-005, FAK-006, FAK-009, and one flagged for
`Canonical_Terms.md` rather than resolved here — see Battery record,
Cycle/CURRENT_CYCLE finding).

---

## Resolution Log

Full history: `Archive/Logs/Forge_Audit_Kit_Changelog.md` (relocated out of this
kit at v1.10 — add new entries there, not here).

Most recent: v1.13 (2026-07-26) — Governing Principles gained a fifth
line: "Correct a flawed premise only when it threatens the task's
outcome — not for its own sake." Names explicitly what "Infinite audit
recursion is a governance failure mode" (below it) already gestured at
without stating as a standalone principle. Sourced from a cross-agent
prompt-design discussion (Grok/Gemini/ChatGPT), adapted rather than
adopted wholesale — see `Admin/Auditor_Protocols.md` v0.29 Resolution
Log for the same discussion's larger output (Mission Drift Review) and
why its proposed evidence-tag scheme was declined as a duplicate
vocabulary.
