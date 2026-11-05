# AUDIT_AGGREGATE — Admin/Security_Protocols.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Security_Protocols.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_06_Admin-Security_Protocols.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 10,893 | `f2a3c89159ab9de651ae74adacf254db5b300201` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_75_Admin-Security_Protocols.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 355ee03d | 3,647 | `12b985ff5551d126ade94fd85b980a1f0fe7ffeb` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | colliding prefix (X3) | Sidecar defines CF-006 inside Cognitive_Frameworks' prefix space with no Kit ID-Reference row disambiguating it | AUDIT_06 §Findings F1 | Standing-open | Kit Governance Sidecar ID Reference regeneration queued (X5); remedy (2) at issuance (namespace SEC-CF-006 or add a CF- row) | |
| A-F2 | F2 | WARNING | stale narration (X9) | Relationship section narrates SEC-008…012 registration and the SEC-007a/b split as pending; both were long since completed in Unknowns v5.71 and this file's own sidecar | AUDIT_06 §Findings F2 | Not re-tested | No enactment evidence located; pass B check 5 spot-clean but the Relationship bullets not re-derived | |
| A-F3 | F3 | NOTE | X7 date-stamp lag | Trailing Status block stamped "Current (2026-09-03)" predates the 2026-09-16 passes; content still accurate | AUDIT_06 §Findings F3 | Closed-by-ruling | PKC-002 (maintain, 2026-10-25) governs the trailing-Status class; the same block's live staleness is B-F1 (enacted) | |
| A-F4 | F4 | NOTE | naming consistency | Three sidecar/log passages credit ratification to "James" rather than the Human Governing Authority — reconciled as authentic by the Charter's own equation of name and role | AUDIT_06 §Findings F4 | Positive-record | n/a — recorded, not graded; no action urged at issuance | |
| A-F5 | F5 | WARNING | bare colliding IDs (PKC-003) | Bare EC-011/EC-004/CF-001 re-mentions at four named locations; EC-011 load-bearing (gates SEC-ASM-006 removal) | AUDIT_06 §Findings F5 | Asserted (enacted) | 2026-10-29 X3 retrofit on this file (8 qualifications per its Last Audit chain); re-verified holding by pass B check 6 | |
| B-F1 | F1 | WARNING | stale narration (X9) | Self-labeled "Current (2026-09-03)" Status block lists 10 open SEC IDs, omitting SEC-013 (registered 2026-10-28); the header (authoritative via the 2026-10-28 precedence line) correctly reads 11 | CAMPAIGN2_AUDIT_75 §Findings F1 | Enacted | MAINT-45 fix pass, commit bff6b3e1 (2026-11-03, per the MAINT-45 session record) | |
| B-C1 | (none) | NOTE | positive | Clean derivations: 11-parity exact (incl. SEC-013), Highest Risk High via SEC-007b with Priority-Critical correctly not mirrored, drift indicators (Trust Boundary guards, Phase 3 gating) intact | CAMPAIGN2_AUDIT_75 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) called this the cleanest file audited to that point; its citation findings were substantially absorbed by the 2026-10-29 X3 retrofit (8 qualifications), and the trailing-Status staleness it graded NOTE became B's one WARNING once SEC-013's registration made the stale block omit a live unknown.
- Pass B (10-31) verified the post-X3 state clean except that block; the MAINT-45 fix pass (2026-11-03, commit bff6b3e1) closed it. The remaining carried items are structural and corpus-wide: the CF-006 namespace question (A-F1) rides the X5 Kit ID-Reference regeneration.
- Checklist authority: count parity (three-way at 11) — pass B. Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
