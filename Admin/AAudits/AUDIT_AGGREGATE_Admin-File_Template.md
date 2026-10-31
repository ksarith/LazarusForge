# AUDIT_AGGREGATE — Admin/File_Template.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-10-31 by Vibe (Repo Custodian — delegated maintenance, Brief 2026-10-30e Option A, human-ruled; sweep = MAINT-34)  ·  **Target:** `Admin/File_Template.md`  ·  **Passes:** 2
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`.

## 1. Provenance

| Pass | Original path (at issuance) | Current path (post-sweep) | Date | Auditor / lane | Head or base at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_10_Admin-File_Template.md` (issued to Archive/Audits/; relocated by MAINT-29) | `Admin/AAudits/Superseded/AUDIT_10_Admin-File_Template.md` | 2026-10-27 | Vibe, Skeptic/Auditor, VibesSandbox stream | head 6dea6e0 | 12,685 | `fc08cc55bcbd8c26fe86e17b41591cfe4d8c3ced` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_01_Admin-File_Template.md` | `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_01_Admin-File_Template.md` | 2026-10-30 | Vibe, Skeptic/Auditor, Campaign 2 (PKC-020) | head 0b476bdd | 4,858 | `27c07596781d94787f382d248023b84c402fb517` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | MAJOR | internal contradiction | Template Exemptions class 8 vs Challenges subtype doctrine disagree on Problem-Statement Spec Gates | AUDIT_10 §Findings F1 | Closed-by-ruling + Enacted | 2da669e28a (2026-10-28 re-rule: "Spec Gates N/A by subtype governs", superseding same-day fee92b4 reconciliation); Archive/Audits README caution note records it | |
| A-F2 | F2 | WARNING | schema drift | Challenges lean schema names Version/Owner fields the canonical §2 schema never defines | AUDIT_10 §Findings F2 | Standing-open | Front-door/registry family + Problem-Statement field standard sit in the deferred human-ruling queue | |
| A-F3 | F3 | WARNING | self-application gap | File_Template not on its own exemption list while not applying itself | AUDIT_10 §Findings F3 | Standing-open | B-N2 re-confirmed open at head 0b476bdd (2026-10-30) | |
| A-F4 | F4 | NOTE | positive | AP-029 removal enacted the right way (removal record kept visible) — anti-X8 | AUDIT_10 §Findings F4 | Positive-record | n/a | |
| A-F5 | F5 | NOTE | regrades | X2 = migration-pending; Aging-Rule staleness actionable; same-session cascade rules canonical | AUDIT_10 §Findings F5 | Positive-record (carried) | Grading conventions carried into SESSION_STATUS and later campaign phases | |
| B-F1 | F1 | WARNING | stale pointer (X8/X11) | Own Resolution Log cites `Archive/Audits/AUDIT_10_Admin-File_Template.md` — path stale across two substantive touches | CAMPAIGN2_AUDIT_01 §Findings F1 | Standing-open; dangling by design after this sweep | MAINT-29 defers inbound-pointer repair to the file's next substantive touch; the pointer is a dated ledger record and now resolves (after two hops) to `Admin/AAudits/Superseded/` | |
| B-N1 | N1 | NOTE | structure | Duplicated section headings are the template's documented self-model, not drift | CAMPAIGN2_AUDIT_01 §Findings N1 | Positive-record | n/a | |
| B-N2 | N2 | NOTE | exemption gap | Same substance as A-F3 | CAMPAIGN2_AUDIT_01 §Findings N2 | Standing-open | See A-F3 | |

## 3. Cross-pass logic map

- Pass A audited the pre-Pattern-A file (10-27); the file then gained Pattern A, the Log-Split Rule, Template Exemptions classes 10–11 and the seventh header entry (commits 263a94569d, 3d4b75a24e, 970282e221, 9aa7edf37a, 4683b7479d). Pass B audited the post-Pattern-A wrapper and called it the freshest, best-cascaded wrapper in the corpus.
- Checklist authority: header/log/scope integrity, exemption classes, Log-Split Rule — pass B (fresher head, verified against live tree). The meta-file's own MAJOR contradiction — pass A, resolved by the 10-28 re-rule (2da669e28a).
- A's INCOMPLETEs (AP-023/025/026 claims, Rename_Registry, Tooling_Inventory history) were deferred to owning-file audits, since issued (e.g. CAMPAIGN2_AUDIT_02 on Auditor_Protocols) — not re-verified in this ledger.

## 4. Pointers

| Original path | Moved to | Blob SHA (before = after) |
|---|---|---|
| `Admin/AAudits/AUDIT_10_Admin-File_Template.md` | `Admin/AAudits/Superseded/AUDIT_10_Admin-File_Template.md` | `fc08cc55…` |
| `Admin/AAudits/CAMPAIGN2_AUDIT_01_Admin-File_Template.md` | `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_01_Admin-File_Template.md` | `27c07596…` |

**Cited from outside the Audits home:** `Routing.md` — rows repointed in the sweep commit; `Admin/File_Template.md` own-log pointer to AUDIT_10 — frozen dated record, dangling by design; `Archive/Audits/SESSION_STATUS.md` dated lines — frozen, dangling by design.

## 5. Addenda
(none)

