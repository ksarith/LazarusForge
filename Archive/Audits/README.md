# Archive/Audits — External Audit Campaign Records

Provenance: findings-only per-file audit campaign (PKC-020 split policy) run by Vibe (Skeptic/Auditor) against ksarith/LazarusForge @ main. The head moved mid-campaign, so no single head describes the whole archive (reconciled 2026-10-29 after the release-1.29 review flagged the stale single-head claim): `AUDIT_01`–`AUDIT_16` were audited at head `6dea6e0`; `CAMPAIGN_AUDIT_17`–`CAMPAIGN_AUDIT_21` at `982e958`; `CAMPAIGN_AUDIT_22`–`CAMPAIGN_AUDIT_29` at `eee122a6`. Each report, correction, and cross-file session record states its own fetch head; `SESSION_STATUS.md` tracks the campaign-era head. Working copies live in ksarith/VibesSandbox/Audits/ (the resume authority); this folder is the LazarusForge-side archival record.

Naming conventions:
- AUDIT_NN_<domain>-<File>.md — one report per audited file (`AUDIT_01`–`AUDIT_16` unprefixed, `CAMPAIGN_AUDIT_17`–`CAMPAIGN_AUDIT_29` prefixed on import; campaign complete through file 29 as of 2026-10-28)
- AUDIT_NN-MM_<topic>_<date>.md — dated corrections to earlier reports
- CROSS_FILE_PATTERN_FINDINGS_Session<N>.md — recurring cross-file patterns (X-numbered), per session batch
- SESSION_STATUS.md — resume tracker: status table, approved remaining sequence, patterns, open questions

Status of these documents: these are external review findings, NOT audits of record. Per PKC-020, they advance no file's Last Audit, Last Reviewed, version, or Status; conversion of any finding into a recorded fix requires human ratification and the full bookkeeping cascade in the owning file. Findings graded CRITICAL/MAJOR/WARNING/NOTE.

Archive/ is template-exempt and outside the Routing/Discovery parity invariant; files here carry no registration requirements. New campaign artifacts will be added here as sessions complete, without cascade.

— Vibe (Repo Custodian), imported 2026-10-28 at human direction.

---

## Stream mapping (2026-10-28, Vibe — Repo Custodian, delegated maintenance; human-ratified batches 2026-10-28c + 2026-10-28d)

Two distinct audit streams live in this folder:

- **Internal custodian stream (unprefixed, high numbers):** `AUDIT_17_Admin-Metrics_Scaffold.md`, `AUDIT_18_Admin-Ship_of_Theseus.md`, `AUDIT_19_Admin-Economics.md` — findings-only pseudo-audits by the Repo Custodian (Vibe) under PKC-020.
- **Sandbox campaign stream:** `AUDIT_01`–`AUDIT_16` (unprefixed) and `CAMPAIGN_AUDIT_17`–`CAMPAIGN_AUDIT_29` (prefixed on import 2026-10-28 to avoid collision with the internal AUDIT_17–19 numbering; 22–29 plus the dated correction imported 2026-10-28 under human-ratified Decision Brief 2026-10-28d, item 9), plus `CROSS_FILE_PATTERN_FINDINGS_Session1–5`, `SESSION_PROMPT_2026-10-27.md`, `AUDIT_01-05_TEMPLATE_RESOLUTION_2026-10-27.md`, `AUDIT_13_CORRECTION_2026-10-28.md`, `CAMPAIGN_AUDIT_20-22_CORRECTION_2026-10-28.md`, and `SESSION_STATUS.md` — Claude's human-directed per-file campaign (01–21) and the Vibe-issued sandbox campaign files 22–29, imported verbatim from VibesSandbox `Audits/` (SESSION_STATUS.md is the sandbox version).

Caution: same-numbered files are **different documents** — internal `AUDIT_17–19` ≠ campaign `CAMPAIGN_AUDIT_17–19`, and their grades differ at F3 for 18/19. Also: `AUDIT_10` F1 was re-ruled 2026-10-28 (Decision Brief 2026-10-28c) — "Spec Gates N/A by subtype" governs, reversing the same-day reconciliation recorded in commit fee92b4.

---

**Relocation note — 2026-10-30 (human-ruled, MAINT-29):** the Admin-file audit artifacts (AUDIT_01–19 and corrections, AUDIT_01-05_TEMPLATE_RESOLUTION, CAMPAIGN_AUDIT_17–31 and correction) now live in `../../Admin/AAudits/`. This folder retains corpus-wide artifacts (CROSS_FILE_PATTERN_FINDINGS sessions, integrity sweep reports, session prompts, SESSION_STATUS); root-owned changelogs remain in `../Logs/`.
---

**Aggregation system — 2026-10-31 (human-ruled, Brief 2026-10-30e Option A):** duplicate-coverage audit passes are now aggregated per target in the audited folder's Audits home (`AUDIT_AGGREGATE_<Folder>-<File>.md`), with the superseded originals relocated byte-identically (blob SHAs unchanged) to that home's `Superseded/` subfolder, marked skip-by-default. Template and rules: `AUDIT_AGGREGATE_TEMPLATE.md` (this folder). Old → new map (2026-10-31 sweep, all now at `../../Admin/AAudits/Superseded/`): `AUDIT_01` + `CAMPAIGN2_AUDIT_03` (Governance_Charter); `AUDIT_10` + `CAMPAIGN2_AUDIT_01` (File_Template); `AUDIT_17` + `CAMPAIGN_AUDIT_17` (Metrics_Scaffold); `AUDIT_18` + `CAMPAIGN_AUDIT_18` (Ship_of_Theseus); `AUDIT_19` + `CAMPAIGN_AUDIT_19` (Economics). The three dated addenda were NOT relocated: they are live corrections to single-pass targets, not superseded duplicates (disclosed deviation from the Brief's earlier draft). The caution note above on same-numbered files remains in force; the aggregates' composite-ID rule (A-Fn/B-Fn) is now the disambiguating citation form.
