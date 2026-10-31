# AUDIT_AGGREGATE — Admin/Governance_Charter.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-10-31 by Vibe (Repo Custodian — delegated maintenance, Brief 2026-10-30e Option A, human-ruled; sweep = MAINT-34)  ·  **Target:** `Admin/Governance_Charter.md`  ·  **Passes:** 2
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`.

## 1. Provenance

| Pass | Original path (at issuance) | Current path (post-sweep) | Date | Auditor / lane | Head or base at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_01_Admin-Governance_Charter.md` (issued to Archive/Audits/; relocated by MAINT-29) | `Admin/AAudits/Superseded/AUDIT_01_Admin-Governance_Charter.md` | 2026-10-27 | Vibe, Skeptic/Auditor, VibesSandbox stream | head 6dea6e0 | 7,042 | `e4e57d87b2103c4bb0b1321e552b8f9e45f3e1f1` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_03_Admin-Governance_Charter.md` | `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_03_Admin-Governance_Charter.md` | 2026-10-30 | Vibe, Skeptic/Auditor, Campaign 2 (PKC-020) | head 0b476bdd | 6,674 | `a520034b0f425489940ed33b09a6111ddc4a8642` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | scope boundary | Deployment Localization Doctrine (added 2026-09-08) in neither Does nor Does-not | AUDIT_01 §Findings F1 | Enacted | 05bdb53912 (2026-10-28 Wrapper Hygiene Batch, ratified 2026-10-28c — commit message names AUDIT_01 F1; B pass check 4 verified) | |
| A-F2 | F2 | WARNING | bare colliding IDs | Bare EC- citations in Enforcement States table + GOV-007 sentence (CT-007/PKC-003) | AUDIT_01 §Findings F2 | Enacted | 5becc4d581 (2026-10-29 X3 retrofit Part 1/3, 38 qualifications; B pass check 6 verified sample) | |
| B-F1 | F1 | WARNING | skipped cascade (X11) | 2026-10-29 X3 retrofit has no Resolution Log entry in the relocated changelog | CAMPAIGN2_AUDIT_03 §Findings F1 | Standing-open | No changelog commit since 2026-10-28 except MAINT-29 relocation (cad087713c, byte-identical); backfill recommended at next substantive touch | |
| B-F2 | F2 | MAJOR | stale pointer (X8/X11) | File State Sidecar Link + 8+ body refs point at dead `Archive/Logs/` changelog path (target at `Admin/ALogs/` since 2026-10-30) | CAMPAIGN2_AUDIT_03 §Findings F2 | Standing-open | MAINT-29 follow-up family ("repaired at next substantive touch"); no substantive GC touch since | |
| B-F3 | F3 | WARNING | staleness (X8) | Six+ open GOV entries aged past the 90-day Aging Rule | CAMPAIGN2_AUDIT_03 §Findings F3 | Standing-open | Aging review batch deferred (human ruling queue) | |
| B-N1 | N1 | NOTE | resolving tier | Bare SEC-007a/b in GOV-003 closure prose — single-owner, not graded | CAMPAIGN2_AUDIT_03 §Findings N1 | Positive-record | n/a | |
| B-N2 | N2 | NOTE | complexity watch | Admin/ at 33 .md files vs 40-file soft ceiling | CAMPAIGN2_AUDIT_03 §Findings N2 | Standing-open | Watch item; no violation at fetch | |
| B-N3 | N3 | NOTE | log-split (T1) | ~130 KB exceeds T1 (≥100 KB); split due at next substantive touch, after Auditor_Protocols | CAMPAIGN2_AUDIT_03 §Findings N3 | Standing-open | T1 split queue (heaviest-first) | |
| A-C5 | checklist 5 | INCOMPLETE | cross-refs | EC co-Tier-1 and FA-001 status claims deferred to owning files | AUDIT_01 §Checks 5 | Not-re-tested | Owning-file audits since issued (Ethical_Constraints AUDIT_05/C2; Facilities R-phase); not re-verified in this ledger | |

## 3. Cross-pass logic map

- Pass A (10-27) audited the pre-repair state; both its WARNINGs were enacted on 10-28/10-29 (commits 05bdb53912, 5becc4d581) before pass B ran. Pass B audited the post-repair file at head 0b476bdd and found only relocation-era wrapper decay (dead Sidecar Link, missing X3 changelog cascade) and aging.
- Checklist authority: count parity (three-way at 13), anchor, FROZEN integrity, Highest Risk parity — pass B (fresher head, 11-check protocol). Scope Boundary — pass B confirmed A-F1's repair. Version/registry — both agree (narrative version log by design).
- The two lanes' F1/F2 IDs mean different things; composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

| Original path | Moved to | Blob SHA (before = after) |
|---|---|---|
| `Admin/AAudits/AUDIT_01_Admin-Governance_Charter.md` | `Admin/AAudits/Superseded/AUDIT_01_Admin-Governance_Charter.md` | `e4e57d87…` |
| `Admin/AAudits/CAMPAIGN2_AUDIT_03_Admin-Governance_Charter.md` | `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_03_Admin-Governance_Charter.md` | `a520034b…` |

**Cited from outside the Audits home:** `Routing.md` — rows repointed in the sweep commit; `Archive/Audits/SESSION_STATUS.md` dated lines and `Admin/ALogs/Governance_Charter_Changelog.md` dated entries — frozen history, dangling by design.

## 5. Addenda
(none)

