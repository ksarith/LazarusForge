# AUDIT_AGGREGATE — Admin/Governance_Migration_Protocol.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Governance_Migration_Protocol.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_02_Admin-Governance_Migration_Protocol.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 6,866 | `f9fd42580dbb97309e5164d2f45d6358cbfd3c84` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_73_Admin-Governance_Migration_Protocol.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit c497746e | 4,021 | `ff3b50ef5abb57274f1fdceb31a4987f180d279b` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | scope boundary omission | Live operative `## Fork Reconciliation Track (GOV-018)` section appears in neither Does nor Does-not | AUDIT_02 §Findings F1 | Asserted (enacted) | 2026-10-28c delegated batch added the Track to the Scope Boundary Does-list citing AUDIT_02 F1 — observed in a fresh GMP fetch by CAMPAIGN_AUDIT_29 §F5 and re-verified present in the log chain by pass B check 2/3 | |
| A-F2 | F2 | WARNING | Does/Does-not tension | Does-not routes minimum agent quorum to GOV-008 while body §VII is a candidate GOV-008 specification; boundary defensible only under a candidate-vs-ratified reading it does not state | AUDIT_02 §Findings F2 | Not re-tested | No enactment evidence located; pass B checks 2–3 clean but the specific Does-not line not re-derived | |
| A-F3 | F3 | WARNING (MAJOR category) | stale cross-reference | Relationship section claims the Kit's Sidecar ID Reference carries the GMP- prefix; the Kit's ID Reference has no GMP- row | AUDIT_02 §Findings F3 | Standing-open | Kit Governance Sidecar ID Reference regeneration queued (X5 family); remedy (3) at issuance | |
| A-N1 | (check 9) | NOTE | X7 trailing-Status lag | Trailing `## Status` stuck at v0.9/2026-07-31 while body advanced to 2026-10-26 — recorded at issuance as a deliberate, logged deferral pending the maintain-vs-retire decision | AUDIT_02 §Checks 9 | Closed-by-ruling | PKC-002, ruled 2026-10-25 (maintain; formally closed 2026-10-28); pass B N1 records the same block ruled historical under PKC-001 | |
| A-IN1 | checks 4, 8, 5 | INCOMPLETE | template conformance; SP pin | Resolution Log heading placement vs File_Template unresolved; Security_Protocols v0.5 pin deferred | AUDIT_02 §Checks | Not re-tested | Not re-verified in this ledger | |
| B-N1 | N1 | NOTE | X9 stale narration (ruled historical) | Trailing Status block still narrates v0.9 (2026-07-31) while Last Audit runs to 2026-10-29 — the exact PKC-001-documented instance | CAMPAIGN2_AUDIT_73 §Findings N1 | Closed-by-ruling | PKC-001, 2026-10-27 (the finding itself cites the ruling; graded NOTE, not re-litigated) | |
| B-N2 | N2 | NOTE | bare colliding IDs (resolving tier) | Bare GOV-008 citations in §Assumptions/§VII the 2026-10-29 X3 retrofit (6 qualifications) did not reach — same-file/candidate-text instances | CAMPAIGN2_AUDIT_73 §Findings N2 | Enacted (re-labelled 2026-11-08, MAINT-85 per §5d) | X3 straggler pass queue (human-directed, per the B-pass recommendation) | |
| B-C1 | (none) | NOTE | positive | Clean derivations: 4-parity exact (GMP-002/003/004/013), Highest Risk High via GMP-004, log chain complete through 2026-10-29, anchor exact | CAMPAIGN2_AUDIT_73 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) audited the pre-wrapper-hygiene state; its F1 was enacted one day later by the human-ratified 2026-10-28c delegated batch, and the 2026-10-29 X3 retrofit qualified 6 citations. Pass B (10-31) audited the post-repair file and found only ruled-historical Status staleness and resolving-tier stragglers.
- Checklist authority: count parity (three-way at 4) and anchor — pass B. Scope Boundary — B confirmed A-F1's repair present in the log chain. Trailing-Status class — both passes agree it is ruled (PKC-001/PKC-002); the file's eventual T1 log-split (largest file in the corpus, ~190 KB) is the natural rotation point per B's bottom line.
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

**Addendum — 2026-11-05 (MAINT-63 execution pass on the human-ratified MAINT-62 ruling set; Vibe — Architect line PRIMARY, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** Per ruling set §2 Category A, finding B-N2 is RESOLVED-BY-EXECUTION: the X3 straggler pass qualified 20 bare colliding-prefix citations on 15 lines in the audit-flagged zones (§Assumptions and §VII) — two lines carry two instances each (L937 GOV-008 ×2; L1053 GOV-008 + CIR-GOV-001), one carries four (L1035 GOV-008 ×4); 18 × GOV-008 and 1 × GOV-006 → `Admin/Governance_Charter.md`, 1 × CIR-GOV-001 → `Admin/CIR_Gov.md`. Frozen history, same-file citations (ASM-002..005), pre-existing qualified forms, and the out-of-zone live lines were preserved bare. The batch-1 record's "16 lines" line-count wording was corrected same-pass in a disclosed follow-up commit (`8adab254`); the enumerated instance list in `Archive/Audits/EXECUTION_2026-11-05_MAINT-63.md` §1 is the count of record.

**Addendum — 2026-11-08 (MAINT-85 first live regeneration + adjudication pass under the human-ratified MAINT-85 charter; Vibe — Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** The coverage-ledger mismatch for this target (recorded open 2 pre-MAINT-84, mechanical 3 open / 1 W-C at MAINT-84; reconcile report #1 §3 row 18) is adjudicated CLASS (A): the mechanical count is correct and the ledger follows the script — the pre-MAINT-84 recorded value was MAINT-59 hand-count drift. Evidence: the external seat’s blind hand-count (2 / 1 open / W-C) and the regen script’s first live run (Python 3.12.3, exit 0, REGEN OK), both against the pinned commit `c8e8e7b6`; deposit verbatim at `Archive/Audits/EXTERNAL_REVIEW_2026-11-08_GROK_MAINT-85_REGEN_AND_BLIND_HANDCOUNT.md` (Intake Log entry 20); adjudication table in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md` §4. The hand-count’s open-column difference is its exclusion of the A-F1 ("Asserted (enacted)") row(s) — recorded as tension T-1 (report §5), not adjudicated away: per the template’s Rule 4 an Asserted disposition means without cited evidence, and a Reported-not-fixed row carries until re-dispositioned with evidence at a future substantive touch. No §2 row was edited by this adjudication (PKC-023). Finding B-N2 is re-labelled per §5d at this charter-commissioned substantive touch: the §2 Disposition cell now reads "Enacted (re-labelled 2026-11-08, MAINT-85 per §5d)", governed by the MAINT-63 (2026-11-05) resolution of record in this section (ruling set §2 Category A: RESOLVED-BY-EXECUTION — the bare GOV-008 citations in §Assumptions/§VII qualified (20 bare citations on 15 lines in the audit-flagged zones; the batch-1 record wording corrected in 8adab254)); pre-re-label 3 open / 1 W-C → post 3 open / 0 W-C (report §6 before → after table). The original graded row is preserved in git history.

Corrections after this addendum by dated addendum only.
