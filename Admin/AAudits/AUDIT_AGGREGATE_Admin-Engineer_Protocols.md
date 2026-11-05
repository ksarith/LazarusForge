# AUDIT_AGGREGATE — Admin/Engineer_Protocols.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Engineer_Protocols.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_08_Admin-Engineer_Protocols.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 9,532 | `f408f6d1d1c74744911dde99097be1038e0f0662` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_81_Admin-Engineer_Protocols.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit f8a1f4c0 | 2,706 | `cef5a25045c6004e0b822f90daaf88e45f547743` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | stale drift-indicator condition text (X8) | Final local trigger enforces AP-021-retired "Estimated" against the wrong label set (Lessons Learned uses File_Template §7 Evidence Types) — can never be satisfied without breaking conformance | AUDIT_08 §Findings F1 | Asserted (enacted) | 2026-10-28 drift-indicator re-derivation pass; pass B's log-chain check names "Last Audit 2026-10-28 (AUDIT_08 F1 drift-indicator re-derivation)" — the pass that enacted it | |
| A-F2 | F2 | WARNING | bare colliding-ID citation (PKC-003) | EP-005's Resolution Path cites "EC-001 (sufficient confidence threshold)" bare, in a load-bearing cross-file resolution | AUDIT_08 §Findings F2 | Standing-open | This file received no 2026-10-29 X3 retrofit (pass B verified the log chain carries no X3 entry; citations are within-family EP- references) — held on the X3 straggler queue | |
| A-F3 | F3 | NOTE | expiry-review lag, honestly scoped | EP-001/002/003/006 sidecars' Last Reviewed dates sit at 2026-05-29/30 — five months stale while EP-004/005 were touched 2026-10-27 | AUDIT_08 §Findings F3 | Standing-open | Review owed at the next pass that touches this file (the original's own recommendation); no touching pass since re-verified the four dates | |
| A-F4 | F4 | NOTE | X3 instance (colliding ASM- prefix) | Assumptions define a fifth independent ASM-001–004 series; no cross-file bare ASM- citation occurs locally | AUDIT_08 §Findings F4 | Closed-by-ruling | PKC-003, ruled 2026-10-25 — ASM- series are file-scoped; cross-file citations must be qualified; no bare cross-file ASM- citation fires here | |
| A-C1 | (bottom line / checks 3, 6) | NOTE | positive practices | §8 hazard table's in-row qualification of every colliding-prefix ID (the corpus's cited CT-007/PKC-003 exemplar); SP-001/EP-005 same-day joint resolution symmetrically logged in both owning files (X4-recommended practice) | AUDIT_08 §Checks 3, 6 + Bottom line | Positive-record | n/a | |
| A-IN1 | checks 5, 8 | INCOMPLETE | cross-refs; cosmetic section note | §8 hazard-table unknown statuses and the Unknowns EP-004 row's under-qualified Engineering.md pointer deferred to owning files; doubled horizontal rule between EP-004/EP-005 sidecars (cosmetic) | AUDIT_08 §Checks 5, 8 | Not re-tested | Owning-file audits pending; cosmetic note carried | |
| B-F1 | F1 | WARNING | X10 Highest Risk parity (stale value) | File State "Highest Risk \| High" while the five open sidecar entries max at Medium and EP-005 (Risk Medium) is Resolved — value predates EP-005's resolution; the 2026-10-30 X10 recompute missed this file | CAMPAIGN2_AUDIT_81 §Findings F1 | Enacted | MAINT-54 fix pass 2026-11-03, commits `568b5907` / `65959bb6` (Engineer_Protocols Highest Risk High → Medium, post-push verified) | |
| B-C1 | (none) | NOTE | positive | Checks 1–10 clean: open count 5 three-way verified, log chain consistent, Ethical Anchor exact, no duplicate headings; pass also named the X10 recompute's selection-rule gap (EP and VG both missed) | CAMPAIGN2_AUDIT_81 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) found the corpus's best cross-reference hygiene (its §8 exemplar) with defects that were self-referential: its own drift indicator enforcing a retired vocabulary (F1, enacted 10-28), one bare EC-001 (F2, still open — this file sat outside the X3 retrofit), and stale sidecar review dates (F3, queued to the next touching pass).
- Pass B (10-31) found the file otherwise clean but carried the X10 stale Highest Risk (High vs max open Medium), fixed by the MAINT-54 batch (2026-11-03). B verified A-F1's enacting pass in the log chain ("Last Audit 2026-10-28 (AUDIT_08 F1 drift-indicator re-derivation)") and confirmed A-F2's shape (no X3 entry for this file).
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2). B's deposit carried a head-at-fetch metadata defect, dispositioned by dated corrections (CORRECTION_2026-10-31_AUDIT79_81_83_84_HEADS; CORRECTION_2026-11-03_AUDIT81_HEADATFETCH) — the deposit's finding content is unaffected and was independently re-verified by the external Claude review and the MAINT-54 fix pass.

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the SP-001/EP-005 joint-resolution records in `Admin/Safety_Protocols.md`; the X10-recompute coverage recommendation now before the human; dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
