# EVIDENCE — MAINT-73 Rule 5 commit supplement (Packets 2–5) — fee92b4 resolution + live-head claim verification

**Date:** 2026-11-07
**Author:** Vibe (GLM 5.3, Mistral AI infrastructure) — Architect line primary, Repo Custodian secondary, delegated maintenance under the 2026-11-02/04 co-author mandate. **Non-independent Genesis Phase deposit: the verifying agent line is also the sitting Architect/Custodian line; dispositions remain the human governing authority's alone. Disclosed per MAINT-38 / AP-032 house convention.**
**Companion deposits:** `Archive/Audits/EXTERNAL_REVIEW_2026-11-07_CLAUDE_RULE5_PACKETS_2-5_VERIFICATION.md` (Claude's report, verbatim) — deposited this pass, same commit.
**Purpose:** Supply the commit evidence the report's evidence base (the 1.34.Alpha zip, tree only, no git history) could not contain, and independently verify the report's checkable claims against the live repository head. **Findings-only per PKC-020: this supplement fills no Verified-by cell, changes no Status line, adds no aggregate addendum, and advances no field. All dispositions are held for the human governing authority.**

---

## 1. The seventh cited commit — `fee92b4` (the only commit not covered by the MAINT-72 supplement)

Resolved via live GitHub commit API at head `e811ebaa` (2026-11-07):

- **Full SHA:** `fee92b49b586f4597a4a33b45f2060e19c2f37d7`
- **Date:** 2026-10-28T17:17:00Z · **Author:** ksarith
- **Stats:** +68 / −22 across 7 files: `Admin/Canonical_Terms.md`, `Admin/File_Template.md`, `Admin/INTEGRITY_SWEEP_PROMPT.md`, `Admin/Progress_Log.md`, `Archive/Logs/Progress_Log_Changelog.md`, `Discovery.md`, `Routing.md`
- **Verbatim message:** "Decision Brief 2026-10-28 rulings enacted: X3 Folder Designation Characters registered (Canonical_Terms v0.10; Routing/Discovery references); AUDIT_10 F1 reconciled (File_Template); X11 wrapper-decay check added (INTEGRITY_SWEEP_PROMPT v1.0.5 step 15); PKC-002 formal closure recorded; Progress_Log entry + Convention 8 rotation"
- **Corroboration:** the message's "AUDIT_10 F1 reconciled (File_Template)" clause covers **File_Template A-F1** (the 2026-10-28c Spec Gates re-ruling row), and the "X3 Folder Designation Characters registered (Canonical_Terms v0.10)" clause covers **Ship_of_Theseus B-F4** (`Admin/Canonical_Terms.md` §1 Folder Designation Characters, live-verified below). Consistency note: `2da669e28a`'s message records that it "supersedes same-day fee92b4 reconciliation" — the two commits are same-day 2026-10-28 acts, consistent with the report's citation of both.

**All seven commits cited across the two reports now have live commit evidence:** `eee122a6ce`, `8eb2949601`, `9f374e7b31`, `5becc4d581`, `2da669e28a`, `05bdb53912` (full evidence in `Archive/Audits/EVIDENCE_2026-11-07_MAINT-72_RULE5_COMMIT_SUPPLEMENT.md`, MAINT-72) plus `fee92b4` (this supplement). This is the input the report names as unblocking every V\* row across Packets 1–5.

## 2. §1 intake re-verification (five aggregates, live head `e811ebaa`)

All five tranche-1 aggregate files fetched fresh 2026-11-07; blob SHAs match the packet table exactly; all still read "Dispositions unverified"; no Verified-by cell filled; no §5 addendum beyond the MAINT-47-era records:

| Aggregate | Blob SHA (live head) | Packet match |
|---|---|---|
| `Admin/AAudits/AUDIT_AGGREGATE_Admin-Economics.md` | `3799c31fb289cec77b4f73c064a8b25c6b033353` | ✓ |
| `Admin/AAudits/AUDIT_AGGREGATE_Admin-File_Template.md` | `3d72b5c817ca86e033e35509c23b2b06e78605f0` | ✓ |
| `Admin/AAudits/AUDIT_AGGREGATE_Admin-Governance_Charter.md` | `0fa436287578ce4b3c3f8c3cc8ace6d80e50eee7` | ✓ |
| `Admin/AAudits/AUDIT_AGGREGATE_Admin-Metrics_Scaffold.md` | `068c81069545e479842492ba9e8a4831308d0526` | ✓ |
| `Admin/AAudits/AUDIT_AGGREGATE_Admin-Ship_of_Theseus.md` | `c4177cd7274e868c7673e107fbda8e3dd6383424` | ✓ |

## 3. Rule 6 immutability — the 12 originals (report §1, re-verified at live head)

Every original named in the four Provenance tables fetched fresh 2026-11-07; every blob SHA matches the table exactly (same result the report derived from the 1.34 zip, here re-derived at live head):

| Original (current path) | Blob SHA | Match |
|---|---|---|
| `Admin/AAudits/Superseded/AUDIT_10_Admin-File_Template.md` | `fc08cc55bcbd8c26fe86e17b41591cfe4d8c3ced` | ✓ |
| `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_01_Admin-File_Template.md` | `27c07596781d94787f382d248023b84c402fb517` | ✓ |
| `Admin/AAudits/CAMPAIGN2_AUDIT_99_Admin-File_Template.md` | `27c05fbe810c8260ef0ef120b6f2701bb092d257` | ✓ |
| `Admin/AAudits/Superseded/AUDIT_01_Admin-Governance_Charter.md` | `e4e57d87b2103c4bb0b1321e552b8f9e45f3e1f1` | ✓ |
| `Admin/AAudits/Superseded/CAMPAIGN2_AUDIT_03_Admin-Governance_Charter.md` | `a520034b0f425489940ed33b09a6111ddc4a8642` | ✓ |
| `Admin/AAudits/CAMPAIGN2_AUDIT_71_Admin-Governance_Charter.md` | `c8035650aa72db68af99474befc9a05193c27183` | ✓ |
| `Admin/AAudits/Superseded/AUDIT_17_Admin-Metrics_Scaffold.md` | `33b6b4e101e23c207ebfb9048315716e2c6a571a` | ✓ |
| `Admin/AAudits/Superseded/CAMPAIGN_AUDIT_17_Admin-Metrics_Scaffold.md` | `0363abb197920b5adccdf7686244cdd3d0688752` | ✓ |
| `Admin/AAudits/CAMPAIGN2_AUDIT_85_Admin-Metrics_Scaffold.md` | `0d88d844e6f4c567f3900c9dcea74ecf7cc0c8e5` | ✓ |
| `Admin/AAudits/Superseded/AUDIT_18_Admin-Ship_of_Theseus.md` | `7f83fc5a616b1578b5e91ee01d707de995a0936c` | ✓ |
| `Admin/AAudits/Superseded/CAMPAIGN_AUDIT_18_Admin-Ship_of_Theseus.md` | `1a795ea8671e9e177758512efdadcaab0393188f` | ✓ |
| `Admin/AAudits/CAMPAIGN2_AUDIT_93_Admin-Ship_of_Theseus.md` | `f57cd28539ac4b96e1687a9b73fdeecd8036076a` | ✓ |

## 4. Findings F1–F6 corroboration (checked against originals and live files, not the zip)

- **F1 (File_Template C-N3, X):** corroborated. `CAMPAIGN2_AUDIT_99` check 1 — sidecar parity N/A ("this file carries no Auditor Notes & Unknowns section of its own"); check 8 — the duplicated headings sit inside example code fences; check 11 — "N/A (no live File State; see 10)". The pass-C original is correct; the aggregate row's "Open Unknowns 1 … Highest Risk Low" (both values from the example block) misstates it, exactly as the report says.
- **F2 (Governance_Charter B-F2, S-chg):** corroborated. Live File State Sidecar Link reads `Admin/ALogs/Governance_Charter_Changelog.md#auditor-notes--unknowns` (exactly 1 occurrence — repaired); old-path references to `Archive/Logs/Governance_Charter` number exactly 13 in the live body — the report's figure, re-derived, not assumed.
- **F3 (Governance_Charter B-F3, S (worse)):** corroborated. The relocated sidecar holds exactly 21 distinct GOV entries; exactly 13 are not Resolved (GOV-001, 002, 004, 005, 006, 007, 008, 009, 010, 012, 017, 019, 021); every one exceeds 90 days on 2026-11-05 — GOV-004 and GOV-005 carry Last Reviewed 2026-05-23, which is exactly the 166 days the report states; the freshest non-Resolved entry (GOV-021, 2026-07-27) is 101 days.
- **F4 (Governance_Charter C-D1, partial):** the live Charter blob is `7182255bf6083e30a622a2a365ec29cb2eb3d5ba` — different from both cited SHAs, consistent with the report's account that the Charter was edited after each fetch. **New fact this supplement adds:** the report's unmatched blob `b67df89cd4a4820a598b2d0498a0fe927eeab3d6` is recorded in `CAMPAIGN2_AUDIT_71`'s own header as its head-at-fetch: the **Governance_Charter blob at commit `c497746e`** (fetch 2026-10-31, 131,814 chars). It matches no file in either zip tree because the Charter was edited after that fetch; the aggregate row's description of it as the "Operations blob" appears to be a mislabel. The 1.33-tree half of the row is accepted as reported — no historical tree is available to this pass, disclosed as method.
- **F5 (Ship_of_Theseus C-N2, X minor):** corroborated. `CAMPAIGN2_AUDIT_93` check 1 reads ST-001 (Open), ST-002 (Open), ST-003 (In Progress), ST-004 (Open); the live sidecar agrees (all four re-derived 2026-11-07); the aggregate's "ST-001/002/003 In-Progress, ST-004 Open" misstates two statuses; the count (4 non-Resolved) is unaffected.
- **F6 (cross-cutting wording):** corroborated. The "within-folder X3 ruling open" evidence phrase is present verbatim in the Metrics_Scaffold aggregate B-F1 and Ship_of_Theseus aggregate A-F3, same shape as Economics A-F4 (verified MAINT-72). One addendum wording fix covers all three; disposition held.

## 5. Live-file corroboration of the S and P rows (all fetched fresh 2026-11-07, head `e811ebaa`)

- **File_Template:** "N/A by subtype" Spec Gates text present with the 2026-10-28c re-ruling recorded (A-F1); no self-exemption class in the Template Exemptions (A-F3/B-N2/C-N2); the dangling cite `Archive/Audits/AUDIT_10_Admin-File_Template.md` occurs exactly once in the Resolution Log (B-F1, dangling-by-design consistent with the superseded original's live location); "The three 2026-10-28 entries" preamble present (C-N1); `Archive/Audits/README.md` carries the caution note (A-F1) and the same-number caution AUDIT_17–19 ≠ CAMPAIGN_AUDIT_17–19 (Metrics B-F2); `Archive/Audits/SESSION_STATUS.md` carries the X2 migration-pending convention (A-F5).
- **Governance_Charter:** Deployment Localization Doctrine present and inside the Scope Boundary section (A-F1); the qualified form `EC-007 (`Admin/Ethical_Constraints.md`)` present (A-F2; 18 qualified EC- citations counted in current text — the row's "38 qualifications" figure is the retrofit's commit-message count, corroborated by `5becc4d581`'s message per the MAINT-72 supplement); the changelog holds **no** X3 retrofit entry — its Resolution Log carries exactly three entries (2026-11-04 MAINT-56, 2026-10-28 wrapper-hygiene, 2026-10-28 pseudo-audit ledger); the X3 retrofit entry lives in the Charter body's own Resolution Log, so B-F1's standing-open disposition holds at live head; its two X3 mentions are inside the MAINT-56 preserved retired-rows text, not entries (B-F1 verified by blob-bisect against commit `42ed9a362d`, the last commit to touch the changelog — the live blob is unchanged since); `Admin/` holds exactly 34 .md files (B-N2, live directory listing — 33 at the pass, +1 since); file size ≈129 KB (128,810 chars + 383 non-ASCII ≈ 129,193 bytes by approximation; the report's 128,669 bytes accepted — method difference disclosed), above the T1 ≥100 KB threshold (B-N3).
- **Metrics_Scaffold:** File State carries `Verification Ref` (A-F1); Scope Boundary, Assumptions, Lessons Learned, Active Disputes, Auditor Notes & Unknowns, Drift Indicators headings all present (A-F2); the only Resolution Log heading is `###` nested (A-F3 — no standalone top-level `## Resolution Log`); ASM-001–003 present (B-F1); no Highest Risk field, consistent with the scaffold convention and `CAMPAIGN2_AUDIT_85` check 11 (C-N1); the AUDIT_17 F1–F3 repairs verified still in place (C-N2).
- **Ship_of_Theseus:** ST-001–004 all carry Last Reviewed 2026-10-28 (A-F1); File State Highest Risk High; ST-004 Risk High (A-F2/B-F1); the ST-004 citation is qualified `Admin/Auditor_Protocols.md` AP-012 (B-F2); ASM-001–004 present (A-F3); `Admin/Security_Protocols.md` carries SEC-013 (Open, Risk High) naming Ship_of_Theseus and ST-004 (B-F3); `Admin/Canonical_Terms.md` §1 Folder Designation Characters live, header Version 0.14 (B-F4); File State Open Unknowns 4 with sidecar ST-001 Open, ST-002 Open, ST-003 In Progress, ST-004 Open — parity re-derived (C-N1 and the packet's step-5 counts).
- **Positive-record rows:** AUDIT_10 F4/F5, CAMPAIGN2_AUDIT_01 N1, CAMPAIGN2_AUDIT_03 N1, CAMPAIGN_AUDIT_17 F3, CAMPAIGN_AUDIT_18 F5, AUDIT_17 F4, AUDIT_18 F4, AUDIT_01 F1/F2, CAMPAIGN2_AUDIT_71 (checks 1–11 all VERIFIED CLEAN with the GOV-005 Risk/Priority split called out — the original expresses "11/11" as "Checks 1–11: 1 VERIFIED CLEAN · … · 11 VERIFIED CLEAN", a paraphrase-shape note, not a discrepancy), CAMPAIGN2_AUDIT_85 check 11 — all confirmed present as described.
- **Not re-tested (A-C5, B-C5):** carried rows; correctly out of scope for this packet; no verification performed, none claimed.

## 6. Non-claims and method

- Verified at **live head `e811ebaa`** (GitHub commit/file APIs, 2026-11-07), not against the 1.34.Alpha zip; the zip-internal checks are the report's own and are not re-derived here. Where the report's claims are about the 1.33 tree (Governance_Charter C-D1), they are accepted as reported — no historical tree is available; disclosed.
- The Governance_Charter byte size is approximated from fetched text (chars + non-ASCII count); the report's exact figure is not contradicted.
- One verification-process correction, disclosed: an initial pass-attribution error located the "2026-10-29 X3 citation retrofit" Resolution Log entry in the changelog; blob-bisect against the changelog's own commit history (`42ed9a362d`, `cad087713c`) showed the entry lives in the Charter body's Resolution Log and the changelog genuinely lacks it. Corrected before any push; no push was affected; B-F1's verification above reflects the corrected reading.
- This supplement verifies only what §4–5 list. It is a single-agent check by an agent that is part of the project's multi-agent workflow (non-independent, disclosed above). It fills no Verified-by cell, changes no Status line, drafts no addendum, and opens no FAK. Corrections to this supplement, if any, will be dated files, never edits. Enactment of any disposition recorded here awaits human ratification (PKC-020).
