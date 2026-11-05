# AUDIT_AGGREGATE — Admin/Repository_Integrity_Protocol.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Repository_Integrity_Protocol.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_03_Admin-Repository_Integrity_Protocol.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 6,477 | `f2ce8681c93d99e5730e68e021319e5c70ba614f` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_76_Admin-Repository_Integrity_Protocol.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 355ee03d | 3,453 | `fe1ee2fde21a2e7f0803cfff0a4bde2ae6cd92ba` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | colliding prefix (X3 class) | This file's ASM-001–006 and the Charter's ASM-001–006 are independently defined with different content; the Kit's ID Reference lists neither ASM- series | AUDIT_03 §Findings F1 | Closed-by-ruling | PKC-003, ruled 2026-10-25 — assumptions stay file-scoped; cross-file citations must be qualified (`File.md ASM-NNN`); per-file prefixes to be considered at the next Canonical_Terms revision | |
| A-N1 | (check 5) | NOTE | stale narration | Discovery line "Archive directory to be added here when established" reads stale — Archive/ has existed in Discovery's tree since 2026-08-09 | AUDIT_03 §Checks 5 | Not re-tested | Line refresh not confirmed; not re-verified in this ledger | |
| A-IN1 | checks 4, 8 | INCOMPLETE | scope granularity; template conformance | §Lightweight Revision Anchors / §Protocol Validation absorbed only under umbrella Does items; File_Template conformance unresolved at issuance | AUDIT_03 §Checks 4, 8 | Not re-tested | Not re-verified in this ledger | |
| B-N1 | N1 | NOTE | bare colliding IDs (resolving tier) | GOV-006/GOV-013/SEC-007b mentions bare-but-resolving; this file received no X3 retrofit pass (Last Audit chain shows only the 2026-10-28 precedence-line propagation) | CAMPAIGN2_AUDIT_76 §Notes N1 | Standing-open | X3 straggler pass queue | |
| B-N2 | N2 | NOTE | version-history gap (ruled historical / PKC-002) | Status history begins at v0.5; v0.1–v0.4 and the unnumbered 2026-09-04/05 passes live in the Resolution Log only, explicitly held pending the maintain-or-retire ruling | CAMPAIGN2_AUDIT_76 §Notes N2 | Closed-by-ruling | PKC-002, ruled 2026-10-25 (maintain; formally closed 2026-10-28); finding graded "not re-litigated" | |
| B-D1 | (metadata defect) | NOTE | provenance-sha misreport | Deposit's head-at-fetch blob is the Metrics_Scaffold blob, not the RIP blob (live RIP blob at fetch: `d87e386d…`) | CAMPAIGN2_AUDIT_76 deposit header | Disclosed defect (carried per MAINT-41b) | Finding content unaffected — the deposit advanced no field (PKC-020); misreport is in the deposit's own metadata, not in the target; established by MAINT-44 deep verification (2026-10-31) | |
| B-C1 | (none) | NOTE | positive | Clean derivations: 5-parity exact three ways (RIP-002/005/006/007/009), Highest Risk High via RIP-005, drift indicators off, mirror-shape decay already backfilled 2026-10-23 and verified | CAMPAIGN2_AUDIT_76 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) found the corpus's cleanest file of its session, with one structural finding (the ASM- collision) that PKC-003 had already ruled (2026-10-25, pre-dating the pass). Pass B (10-31) confirmed the file healthy and added only straggler-tier citation notes plus its own metadata defect.
- Checklist authority: count parity (three-way at 5) — pass B. The ASM- namespace question is corpus-wide (see the Governance_Charter, Ethical_Constraints and other tranche-2 aggregates' X3 rows) and closed by PKC-003; the per-file-prefix refinement remains queued to the next Canonical_Terms revision.
- B-D1 follows the tranche-1 C-D1 precedent (Governance_Charter aggregate): a pass's own provenance defect is carried in the ledger as a disclosed defect, never silently.
- Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
