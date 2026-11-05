# AUDIT_AGGREGATE — Admin/Verification_Gates.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Verification_Gates.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_09_Admin-Verification_Gates.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 9,104 | `15af2efc87ae5eb030ebd997e9bd4794167752dc` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_83_Admin-Verification_Gates.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit f8a1f4c0 | 3,495 | `1426f9111f46a2972a4858b22afc8ecb87d41a90` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | bare colliding-ID citations (PKC-003) | Three bare cross-reference instances: AP-007/GOV-003/RIP-001 in VG-001's Resolution; bare GOV-011 in the 2026-07-03 disambiguation note; bare RIP-004 in VG-001's Lessons Learned | AUDIT_09 §Findings F1 | Asserted (enacted) | 2026-10-29 X3 retrofit on this file (2 qualifications per its Last Audit chain); pass B's log-chain check verified the X3 entry and sampled citations clean | |
| A-F2 | F2 | WARNING | vocabulary conflation (X8-family) | 2026-07-03 Lessons Learned row's Confidence value reads "Operationally Hardened" — a Kit institutional label used where File_Template §7 Confidence Levels belong | AUDIT_09 §Findings F2 | Not re-tested | Pass B's checks did not re-derive the Lessons Learned vocabulary; carried for verifier at the next touching pass | |
| A-F3 | F3 | NOTE | X3 instance (colliding ASM- prefix) | Assumptions define a sixth independent ASM-001–004 series; no bare cross-file ASM- citation occurs | AUDIT_09 §Findings F3 | Closed-by-ruling | PKC-003, ruled 2026-10-25 — ASM- series are file-scoped | |
| A-F4 | F4 | NOTE | positive practices | Trailing Status block's explicit precedence rule ("the File State header is authoritative if this block and it ever disagree") neutralizing X7; Gate 2's correct "Estimated"-retired handling (the X8 counter-example done right) | AUDIT_09 §Findings F4 | Positive-record | n/a (the precedence line was additionally propagated into GMP's Status block by the 2026-10-28 delegated batch, observed live at CA29) | |
| A-IN1 | check 5 | INCOMPLETE | AP sync deferred | Gate definitions vs `Admin/Auditor_Protocols.md` §Verification Gate Enforcement deliberately deferred — AP sequenced LAST; also the 2026-08-09 Rename Registry row and AP-029 claims deferred | AUDIT_09 §Checks 5 | Not re-tested | Owning audit (Auditor_Protocols, LAST) pending | |
| B-F1 | F1 | WARNING | stale cross-claim in the index (file-wins rule) | Unknowns.md's FAK-009 row claims "VG-001 itself remains unresolved in `Admin/Verification_Gates.md`" while VG-001's live sidecar reads Resolved — Discharge via Lessons Learned, with a dedicated resolving body section | CAMPAIGN2_AUDIT_83 §Findings F1 | Enacted | MAINT-54 fix batch, commit `817cfb48` (FAK-009 row's VG-001 parenthetical corrected against the live sidecar) | |
| B-F2 | F2 | WARNING | X10 Highest Risk parity (stale value) | "Highest Risk \| High" with Open Unknowns 0 — nothing open to mirror; Resolution_Methodology (the zero-unknown control) correctly reads Low; the 2026-10-30 X10 recompute missed this file | CAMPAIGN2_AUDIT_83 §Findings F2 | Enacted | MAINT-54 fix batch, commits `54761b65` / `62740060` (VG Highest Risk recomputed post-resolution) | |
| B-C1 | (none) | NOTE | positive | Checks otherwise clean: open count 0 three-way verified, Spec Gates 6/6 consistent with the 2026-09-03 promotion record, X3 retrofit entry in the log chain, Ethical Anchor exact | CAMPAIGN2_AUDIT_83 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) found a tight, self-aware governance file — zero open unknowns at exact parity, the corpus's X8 counter-example done right — with citation/vocabulary hygiene findings only. The 2026-10-29 X3 retrofit resolved A-F1 (2 qualifications, verified in B's log-chain check); A-F2's Confidence-cell label was not part of X3's scope and is carried.
- Pass B (10-31) audited the post-X3 file: both of its findings are stale wrapper values pointing the wrong way (the index's stale claim about this file; this file's stale Highest Risk about nothing), both fixed by the MAINT-54 batch (2026-11-03). B also confirmed the X10 recompute's selection-rule gap (EP and VG both missed) — now before the human.
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2). B's deposit carried a head-at-fetch metadata defect, corrected by CORRECTION_2026-10-31_AUDIT79_81_83_84_HEADS (provenance metadata only; findings unaffected).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the FAK-009 row in `Admin/Unknowns.md` (corrected by MAINT-54); the X10-recompute coverage recommendation before the human; dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
