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
| B-N2 | N2 | NOTE | bare colliding IDs (resolving tier) | Bare GOV-008 citations in §Assumptions/§VII the 2026-10-29 X3 retrofit (6 qualifications) did not reach — same-file/candidate-text instances | CAMPAIGN2_AUDIT_73 §Findings N2 | Standing-open | X3 straggler pass queue (human-directed, per the B-pass recommendation) | |
| B-C1 | (none) | NOTE | positive | Clean derivations: 4-parity exact (GMP-002/003/004/013), Highest Risk High via GMP-004, log chain complete through 2026-10-29, anchor exact | CAMPAIGN2_AUDIT_73 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) audited the pre-wrapper-hygiene state; its F1 was enacted one day later by the human-ratified 2026-10-28c delegated batch, and the 2026-10-29 X3 retrofit qualified 6 citations. Pass B (10-31) audited the post-repair file and found only ruled-historical Status staleness and resolving-tier stragglers.
- Checklist authority: count parity (three-way at 4) and anchor — pass B. Scope Boundary — B confirmed A-F1's repair present in the log chain. Trailing-Status class — both passes agree it is ruled (PKC-001/PKC-002); the file's eventual T1 log-split (largest file in the corpus, ~190 KB) is the natural rotation point per B's bottom line.
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
