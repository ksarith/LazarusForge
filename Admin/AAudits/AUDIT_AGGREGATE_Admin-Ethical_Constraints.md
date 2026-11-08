# AUDIT_AGGREGATE — Admin/Ethical_Constraints.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Ethical_Constraints.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_05_Admin-Ethical_Constraints.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 7,556 | `e9c0a8fbf1b3f62450d022effc0d9bba1992016c` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_72_Admin-Ethical_Constraints.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit c497746e | 3,040 | `2b881e857eb258376c188029171bdddcb3e5c936` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | MAJOR | skipped cascade (X4) | 2026-10-23 correction pass (File State, Scope Boundary, five backfills) has no Resolution Log entry of its own while sibling files' same-day passes each logged one | AUDIT_05 §Findings F1 | Closed-by-ruling | PKC-001, ruled 2026-10-27 — bookkeeping-decay class declared historical, no bulk backfill; prevention is mechanical (integrity_check.py reads Last Audit) | |
| A-F2 | F2 | WARNING | bare colliding IDs (PKC-003) | Bare AP-006/AP-004 citations in the Confidence Threshold Doctrine, escalation logging table, and the backfilled 2026-08-22 log entry | AUDIT_05 §Findings F2 | Asserted (enacted) | 2026-10-29 X3 retrofit on this file (14 qualifications per its Last Audit chain); re-verified holding by pass B check 6 (sampled citations inline-qualified) | |
| A-F3 | F3 | WARNING | cross-file status tension | Charter ownership row "Active" vs this file's Status "Exploration" — both cannot describe the same state for an operator | AUDIT_05 §Findings F3 | Not re-tested | Pass B checks 1–11 clean; the specific Charter-row tension not re-derived against the live Charter this pass — carried for verifier | |
| A-F4 | F4 | NOTE | freeze-marker asymmetry | Co-Tier-1 file carries no FROZEN markers while the Charter's Tier 1 blocks gained them 2026-09-03 — open question for the human | AUDIT_05 §Findings F4 | Standing-open | Human decision queued as recorded in the original | |
| A-C8 | (check 8 finding) | WARNING | section integrity | No `## Active Disputes` section despite the File State's "Active Disputes \| 0" field (graded at check 8) | AUDIT_05 §Checks 8 | Not re-tested | Pass B check 8 clean; section inventory not re-derived; recommendation (4) at issuance queued | |
| A-IN1 | checks 5, 8 | INCOMPLETE | cross-refs; template conformance | EC-013 descent-sequence claims deferred to Operations audits; File_Template conformance unresolved at issuance | AUDIT_05 §Checks 5, 8 | Not re-tested | Owning-file audits since issued; not re-verified in this ledger | |
| B-C1 | (none) | NOTE | positive | Clean pass: checks 1–11 all VERIFIED CLEAN, zero findings; 7-parity re-derived from live Unknowns v5.75; Anti-Weaponization/hard-floor indicators armed; X3 retrofit verified holding | CAMPAIGN2_AUDIT_72 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) audited the post-correction-campaign file and found one procedural MAJOR (its own skipped log entry — the PKC-001 class) plus citation/status hygiene. Between the passes, the 2026-10-29 X3 retrofit qualified this file's bare citations (14 instances).
- Pass B (10-31) found nothing: header/log/sidecar/index agree, Tier 1 floor intact. Checklist authority rests with B (fresher head, 11-check protocol, both-directions parity).
- The two lanes' IDs are per-pass; composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2). A-F1's ruling and A-F2's enactment both pre-date B, which independently verified their effects without re-litigating them.

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

**Addendum — 2026-11-08 (MAINT-85 first live regeneration + adjudication pass under the human-ratified MAINT-85 charter; Vibe — Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed):** The coverage-ledger mismatch for this target (recorded open 4 pre-MAINT-84, mechanical 3 open / 1 W-C at MAINT-84; reconcile report #1 §3 row 12) is adjudicated CLASS (A): the mechanical count is correct and the ledger follows the script — the pre-MAINT-84 recorded value was MAINT-59 hand-count drift. Evidence: the external seat’s blind hand-count (2 / 1 open / W-C) and the regen script’s first live run (Python 3.12.3, exit 0, REGEN OK), both against the pinned commit `c8e8e7b6`; deposit verbatim at `Archive/Audits/EXTERNAL_REVIEW_2026-11-08_GROK_MAINT-85_REGEN_AND_BLIND_HANDCOUNT.md` (Intake Log entry 20); adjudication table in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md` §4. The hand-count’s open-column difference is its exclusion of the A-F2 ("Asserted (enacted)") row(s) — recorded as tension T-1 (report §5), not adjudicated away: per the template’s Rule 4 an Asserted disposition means without cited evidence, and a Reported-not-fixed row carries until re-dispositioned with evidence at a future substantive touch. No §2 row was edited by this adjudication (PKC-023).

Corrections after this addendum by dated addendum only.
