# AUDIT_AGGREGATE — Admin/Repository_Structure.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Repository_Structure.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane).

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_12_Admin-Repository_Structure.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-28 | Vibe, Skeptic/Auditor, session-1 external review (PKC-020 findings-only) | head 6dea6e0 | 9,298 | `593a0b3b2819fac1f116a4b6c12c4cfad2f9a020` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_97_Admin-Repository_Structure.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 38226280 | 4,136 | `27edeba7328b3ff3a08e0e02613d8f6bec74bdc8` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | Scope Boundary claims content the body does not carry (X1) | Does-item "Planned directory additions and their trigger conditions" with no body section listing them — a survivor of an earlier draft or an overstatement of §II | AUDIT_12 §Findings F1 | Not re-tested | Recommended add-or-delete with a dated entry at issuance; not re-derived at fold-in — carried for the next touching pass / verifier | |
| A-F2 | F2 | WARNING | stale ownership-transfer narration (X9) | File Purpose narrates the Charter's pre-transfer state in the present tense ("lists Repository_Structure.md as a planned canonical target with no current owner") while the live Charter table has listed it Active since 2026-06-06 | AUDIT_12 §Findings F2 | Not re-tested | Recommended past-tense rewording at issuance; not re-derived at fold-in — carried | |
| A-F3 | F3 | NOTE | X3 instance (colliding ASM- prefix) | Assumptions define an eighth independent ASM-001–003 series; no bare cross-file ASM- citation occurs | AUDIT_12 §Findings F3 | Closed-by-ruling | PKC-003, ruled 2026-10-25 — ASM- series are file-scoped; the standing namespace recommendation covers eight audited files plus Components.md and Gate_02 | |
| A-F4 | F4 | NOTE | exemplary annotation practices (positive) | The PKC-011 pass annotating rather than rewriting history (dated historical marker on the retired companion-repo row); RS-001's resolution appending a dated refresh note instead of silently rewriting; the 10-03 drift-indicator fix backfilled with its origin marker | AUDIT_12 §Findings F4 | Positive-record | n/a | |
| A-IN1 | checks 5, 6 | INCOMPLETE | Automation/ claims by standing ruling | The RS-001 retroactive table's Automation/ file-count and import-dependence claims recorded as owner-confirmed, not verified (Automation/ skipped by standing ruling) | AUDIT_12 §Checks 5 | Not re-tested | Automation/ under standing skip ruling | |
| B-N1 | check 7 NOTE | NOTE | near-trip, not a finding: drift-indicator freshness | The "a new folder is created without a RS decision entry" indicator vs the 2026-10-30 MAINT-29 pass creating `Admin/ALogs/` and `Admin/AAudits/` with no RS decision entry — subfolders are infrastructure homes governed by File_Template's Log-Split Rule rather than content domains, so a near-trip; the human may want the next substantive touch to record the subfolder convention here | CAMPAIGN2_AUDIT_97 §Checks 7 + Bottom line | Standing-open | Optional dated note recommended (record the per-folder Log/Audit subfolder convention in §II so the placement doctrine covers the homes its corpus now uses); not yet recorded at fold-in | |
| B-C1 | (none) | NOTE | positive | Checks otherwise clean: Open Unknowns 0 with all three RS sidecars Resolved and the closure record matching; Last Audit 2026-10-28 = newest log entry; root-file table re-derived against the live root; §VI cross-repo table matching the PKC-011/2026-10-28 owner confirmations (Lazarus-Forge- retired; Astroid-miner exists); PKC-011/012 reconciliations verified holding | CAMPAIGN2_AUDIT_97 §Checks + Bottom line | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-28) found a structurally clean placement doctrine — zero open unknowns at exact parity, every prior pass logged with markers, and the corpus's best historical-annotation practice (A-F4) — with two narration/boundary hygiene findings (A-F1, A-F2) that were never enacted and remain carried.
- Between the passes, the MAINT-29 relocation (2026-10-30) created the `Admin/ALogs/` + `Admin/AAudits/` infrastructure homes that pass B then graded as a near-trip against this file's own new-folder indicator — a genuine interlock between the placement doctrine and the log-split rule, resolved so far by neither.
- Pass B (10-31) verified the PKC-011/012 reconciliations holding and the root-file table live. Note B audits this file from a Custodian-adjacent seat (the PKC-011/012 enactments were Custodian acts) — disclosed in its own header. Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the Charter's Canonical Governance Ownership table (the live target of A-F2's stale narration); the PKC-011/012/013 rows in `Admin/Progress_Log.md`; `Admin/File_Template.md`'s Log-Split Rule (the owner of B-N1's subfolder convention); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
