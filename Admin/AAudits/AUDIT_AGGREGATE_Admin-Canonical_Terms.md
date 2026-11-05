# AUDIT_AGGREGATE — Admin/Canonical_Terms.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Canonical_Terms.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_11_Admin-Canonical_Terms.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-27 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 12,379 | `6ea79ab75c0e69fe0492e290bdb430a4a58ef73f` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_77_Admin-Canonical_Terms.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 355ee03d | 3,748 | `5b6705dd7fde6f04c26ece1310e369c343fb8941` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | MAJOR | three-way count parity broken at the header (X10) | File State "Open Unknowns \| 9" vs sidecar non-Resolved 10 (CT-001–CT-010) vs Unknowns active index 10 — stale since a 2026-07-05 arithmetic slip (11→10, not 10→9) and repeated twice since without recounting | AUDIT_11 §Findings F1 | Enacted | 2026-10-28b delegated batch (corpus Highest-Risk recompute + count corrections), per AUDIT_26 F5's verified-adoption list; re-verified by pass B check 1: non-Resolved derived from source = 10 = File State, matching the live index | |
| A-F2 | F2 | WARNING | misplaced log entries + mislabeled Status diff headers | Two Resolution Log entries sit at the file bottom outside the log section; the Status history's v0.4 block carries a "Changes from v0.2:" header describing v0.3 changes | AUDIT_11 §Findings F2 | Reported-not-fixed (historical) | Placement defects left in place per the PKC-001/PKC-007 rulings' history discipline and the MAINT-44/45 session records (no relocation of frozen text); the file's own log discipline documents the shape | |
| A-F3 | F3 | WARNING | missing Version String Registry (X8-family) | File_Template §11 requires a registry for this file's self-referential version strings (Status headers, log version lines); its own 2026-07-05 header/Status desync is the exact failure mode the rule prevents | AUDIT_11 §Findings F3 | Standing-open | Registry still owed at the next substantive pass; no enactment located as of fold-in | |
| A-F4 | F4 | WARNING | self-violation of the file's own EC- guardrail | CT-005's Description cites bare EC-001 without the owning file, in the very file whose §5 guardrail forbids exactly that until CT-007's rename completes | AUDIT_11 §Findings F4 | Asserted (enacted) | 2026-10-29 X3 retrofit on this file (pass B's citation checks sampled clean); C2_77 check 6 spot-verified no dangling bare citations | |
| A-F5 | F5 | NOTE | X3 instance (colliding ASM- prefix) | Assumptions define a seventh independent ASM-001–004 series | AUDIT_11 §Findings F5 | Closed-by-ruling | PKC-003, ruled 2026-10-25 — ASM- series are file-scoped | |
| A-F6 | F6 | NOTE | exemplary self-correction practices | CT-007's escalated collision handling (ECN- rename registered in the Kit); CT-002's consolidation note catching a mutual mis-pointing Owner pair via integrity_check.py; the tested `[ExternalRepo]` backtick convention | AUDIT_11 §Findings F6 | Positive-record | n/a | |
| A-IN1 | checks 5, 9 | INCOMPLETE | cross-refs deferred | Auditor_Protocols v0.17 claim and AP-006 citations (AP audited LAST); ST-001/ST-002 status claims (Ship_of_Theseus); Tier placements vs live Charter hierarchy | AUDIT_11 §Checks 5, 9 | Not re-tested | Owning audits pending or read-only by human ruling | |
| B-F1 | F1 | WARNING | version bump with no recorded provenance | Header reads Version 0.13 while the Status current line, the PKC-039 table, and the whole Resolution Log stop at 0.12 (2026-10-28); the only post-v0.12 pass claims "Citation-form-only" — what 0.13 changed is unreconstructable from the file | CAMPAIGN2_AUDIT_77 §Findings F1 | Enacted | RECONSTRUCTED by MAINT-44 (2026-11-03, git-diff based reconstruction deposited); FIXED by MAINT-45, commit `72a61569` (Status line and PKC-039 table advanced to 0.13 in the same pass) | |
| B-C1 | (none) | NOTE | positive | Checks 1, 10, 11 clean: count parity 10 exact against live sidecars and index; Highest Risk High verified against CT-004 High and CT-007 escalated High (the 10-28 X10 recompute claim verified); Ethical Anchor exact; drift indicators untripped | CAMPAIGN2_AUDIT_77 §Clean derivations | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-27) found the anti-drift doctrine file drifting in exactly the ways it exists to prevent: a MAJOR count-parity break (F1, enacted 10-28b and re-verified by B), misplaced log entries (F2, left as historical record), a missing Version String Registry (F3, still owed), and one self-violating bare EC-001 (F4, X3-retrofitted 10-29).
- Pass B (10-31) verified A-F1's correction holding (10 = 10 = 10) and added the mirror-image defect: a version bump ahead of its own bookkeeping (F1, 0.13 with no recorded provenance) — the PKC-001 cascade-skip class occurring after the rule written to prevent it; reconstructed (MAINT-44) and repaired (MAINT-45, commit 72a61569) on 2026-11-03.
- This file defines the ID-prefix scheme the whole X3 retrofit depends on — its F1 pair (count off by one; version ahead of log) is the corpus's cleanest single-file illustration of both bookkeeping-decay directions. Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); AUDIT_26 F5's verified-delegated-adoption list (A-F1's enactment record); the MAINT-44 reconstruction and MAINT-45 fix-pass session records (B-F1); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
