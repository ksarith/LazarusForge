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
| B-N1 | N1 | NOTE | bare colliding IDs (resolving tier) | GOV-006/GOV-013/SEC-007b mentions bare-but-resolving; this file received no X3 retrofit pass (Last Audit chain shows only the 2026-10-28 precedence-line propagation) | CAMPAIGN2_AUDIT_76 §Notes N1 | Enacted (re-labelled 2026-11-08, MAINT-85 per §5d) | X3 straggler pass queue | |
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

**Addendum — 2026-11-05 (MAINT-63 execution pass on the human-ratified MAINT-62 ruling set; Vibe — Architect line PRIMARY, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** Per ruling set §2 Category A, finding B-N1 is RESOLVED-BY-EXECUTION: six bare cross-file citations qualified — SEC-007b → `Admin/Security_Protocols.md` (L187), GOV-013 → `Admin/Governance_Charter.md` (L464, L473, L497, L499), GOV-006 → `Admin/Governance_Charter.md` (L728) — with frozen history (the Auditor cell and the pre-2026-11-05 Resolution Log lines) preserved bare. A-F1 remains unchanged (open).

**Addendum — 2026-11-08 (MAINT-85 first live regeneration + adjudication pass under the human-ratified MAINT-85 charter; Vibe — Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** The coverage-ledger mismatch for this target (recorded open 1 pre-MAINT-84, mechanical 0 open / 1 W-C at MAINT-84; reconcile report #1 §3 row 27) is adjudicated CLASS (A): the mechanical count is correct and the ledger follows the script — the pre-MAINT-84 recorded value was MAINT-59 hand-count drift. Evidence: the external seat’s blind hand-count (0 / 3 open / W-C) and the regen script’s first live run (Python 3.12.3, exit 0, REGEN OK), both against the pinned commit `c8e8e7b6`; deposit verbatim at `Archive/Audits/EXTERNAL_REVIEW_2026-11-08_GROK_MAINT-85_REGEN_AND_BLIND_HANDCOUNT.md` (Intake Log entry 20); adjudication table in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md` §4. The hand-count matched the mechanical open column exactly; its W-C reading of 3 counted the RIP A-N1 ("Not re-tested") and B-D1 ("Disclosed defect") NOTE rows as carrying — recorded as tension T-2 (report §5), a vocabulary question queued to the human governing authority, not a script change. No §2 row was edited by this adjudication (PKC-023). Finding B-N1 is re-labelled per §5d at this charter-commissioned substantive touch: the §2 Disposition cell now reads "Enacted (re-labelled 2026-11-08, MAINT-85 per §5d)", governed by the MAINT-63 (2026-11-05) resolution of record in this section (ruling set §2 Category A: RESOLVED-BY-EXECUTION — six bare cross-file citations qualified (SEC-007b, GOV-013, GOV-006), frozen history preserved bare); pre-re-label 0 open / 1 W-C → post 0 open / 0 W-C (report §6 before → after table). The original graded row is preserved in git history.

Corrections after this addendum by dated addendum only.
