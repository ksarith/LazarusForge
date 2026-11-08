# AUDIT_AGGREGATE — Admin/Computational_Institutional_Reasoning.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Computational_Institutional_Reasoning.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane). **Scope correction:** the pre-sweep target list recorded AUDIT_04 as this target's pass A — AUDIT_04's target is `Admin/CIR_Gov.md` (own aggregate, q.v.); this target's earliest pass is CAMPAIGN_AUDIT_21.

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/CAMPAIGN_AUDIT_21_Admin-Computational_Institutional_Reasoning.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-28 | Vibe, Skeptic/Auditor, VibesSandbox audit stream (PKC-020 findings-only) | head 982e958 | 12,949 | `52b94e727e4fe2603226794fa64276f0bf08d1d0` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_78_Admin-Computational_Institutional_Reasoning.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 355ee03d | 4,007 | `ee19d313baeab2fb0846c24d8d9d67d62cf0d34e` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | stale header (X7/X9) | Last Audit cell leads 2026-07-29 while the body advanced to v0.29 (2026-10-27); the entire v0.19→v0.29 changelog accreted inside the cell | CAMPAIGN_AUDIT_21 §Findings F1 | Closed-by-ruling | PKC-001, ruled 2026-10-27 (class declared historical; the 2026-10-28 dated correction to AUDIT_20–22 maps this finding as partially pre-dispositioned — stale-header class historical, prevention mechanical) | |
| A-F2 | F2 | WARNING | wrapper sections absent | No Resolution Log / Assumptions / Lessons Learned / Active Disputes / Drift Indicators / Abandoned Paths / Cross-References sections; CIR-001 tracker in §8.4 without standard sidecar fields | CAMPAIGN_AUDIT_21 §Findings F2 | Standing-open | Minimal wrapper repair performed 2026-10-28 (per pass B N2: "explicitly 'minimal wrapper repair'"); full migration queued for the next wrapper-scope visit | |
| A-F3 | F3 | WARNING | bare colliding IDs (PKC-003) | Bare AP-006/CF-004 in the §6.2 rule headings (γ3/γ4); bare CF-002 in File State and the §4.6.2 predicate box | CAMPAIGN_AUDIT_21 §Findings F3 | Asserted (enacted) | 2026-10-29 X3 retrofit on this file (5 qualifications per its Last Audit chain); pass B checks sampled clean | |
| A-F4 | F4 | WARNING | Spec Gates partial enumeration | Spec Gates field enumerates G1/G3/G4 only; G2/G5/G6 statuses absent against the Kit's uniform six-gate form | CAMPAIGN_AUDIT_21 §Findings F4 | Not re-tested | Pass B check 9 verified the row's citations consistent with the AP sidecar; the 3-of-6 enumeration shape not re-graded | |
| A-F5 | F5 | NOTE | positive (X3 exemplar) | Second corpus collision resolved by rename (local "GOV-008" → CIR-001, 2026-07-28), CIR- prefix registered in the Kit ID Reference, honest unbackfilled First Logged | CAMPAIGN_AUDIT_21 §Findings F5 | Positive-record | n/a | |
| A-F6 | F6 | NOTE | positive practices | §7.4 declared-vs-implemented honesty block; Ψ-gate self-bar; CIR-F01→F04 correction chain; v0.27 verified-vs-reported separation | CAMPAIGN_AUDIT_21 §Findings F6 | Positive-record | n/a | |
| A-IN1 | checks 5, 7 | INCOMPLETE | AP "line 774"; harness versions; VG applicability | Carried to the Auditor_Protocols audit (LAST) and the Automation/ standing ruling | CAMPAIGN_AUDIT_21 §Checks | Not re-tested | Owning audits pending (AP audited LAST) | |
| B-N1 | N1 | NOTE | missing Open Unknowns row | File State carries no Open Unknowns count row; CIR-001 countable only via Highest Risk / Active Trackers / live index | CAMPAIGN2_AUDIT_78 §Notes N1 | Standing-open | B-pass recommendation: add the row (1, naming CIR-001) at the next substantive touch | |
| B-N2 | N2 | NOTE | nonstandard sidecar format (disclosed) | CIR-001 recorded as a Tracker Entry block rather than the standard sidecar format — a disclosed scope decision of the 2026-10-28 minimal wrapper repair; fields complete | CAMPAIGN2_AUDIT_78 §Notes N2 | Standing-open | Migrate to the standard sidecar format when the wrapper scope is revisited (B-pass recommendation) | |
| B-C1 | (none) | NOTE | positive | Version metadata fully self-consistent (the one file in its batch so); rename note recorded on both sides; Spec Gates citations cross-checked against the live AP sidecar | CAMPAIGN2_AUDIT_78 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-28) found the corpus's most rigorous theoretical content under its most decayed wrapper — the strongest X11 instance yet. Between the passes: the 2026-10-28 minimal wrapper repair (scope-disclosed), the 2026-10-29 X3 retrofit (5 qualifications), and the PKC-001/PKC-007 rulings already covering the log-shape findings.
- Pass B (10-31) audited the post-repair file: content-consistent everywhere it is stated, with two format NOTES (absent count row; nonstandard tracker form) both queued rather than graded.
- This aggregate corrects the pre-sweep target list's misattribution of AUDIT_04 to this target; `Admin/CIR_Gov.md` has its own aggregate. Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the PKC-030 derivation-audit records in `Admin/Progress_Log.md` and `Admin/Nothingness_Theorem.md`; dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

**Addendum — 2026-11-08 (MAINT-85 first live regeneration + adjudication pass under the human-ratified MAINT-85 charter; Vibe — Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** The coverage-ledger mismatch for this target (recorded open 4 pre-MAINT-84, mechanical 3 open / 2 W-C at MAINT-84; reconcile report #1 §3 row 8) is adjudicated CLASS (A): the mechanical count is correct and the ledger follows the script — the pre-MAINT-84 recorded value was MAINT-59 hand-count drift. Evidence: the external seat’s blind hand-count (2 / 2 open / W-C) and the regen script’s first live run (Python 3.12.3, exit 0, REGEN OK), both against the pinned commit `c8e8e7b6`; deposit verbatim at `Archive/Audits/EXTERNAL_REVIEW_2026-11-08_GROK_MAINT-85_REGEN_AND_BLIND_HANDCOUNT.md` (Intake Log entry 20); adjudication table in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md` §4. The hand-count’s open-column difference is its exclusion of the A-F3 ("Asserted (enacted)") row(s) — recorded as tension T-1 (report §5), not adjudicated away: per the template’s Rule 4 an Asserted disposition means without cited evidence, and a Reported-not-fixed row carries until re-dispositioned with evidence at a future substantive touch. No §2 row was edited by this adjudication (PKC-023).

Corrections after this addendum by dated addendum only.
