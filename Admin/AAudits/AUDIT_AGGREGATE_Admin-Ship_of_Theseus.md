# AUDIT_AGGREGATE — Admin/Ship_of_Theseus.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-10-31 by Vibe (Repo Custodian — delegated maintenance, Brief 2026-10-30e Option A, human-ruled; sweep = MAINT-34)  ·  **Target:** `Admin/Ship_of_Theseus.md`  ·  **Passes:** 3
**Updated:** 2026-10-31 by Vibe (Repo Custodian) — pass C folded in (MAINT-47, amalgamation tranche 1). Non-independent Genesis Phase: amalgamator and pass-C depositor are the same Vibe line.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`.

## 1. Provenance

| Pass | Original path (at issuance) | Current path (post-sweep) | Date | Auditor / lane | Head or base at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/AUDIT_18_Admin-Ship_of_Theseus.md` (custodian pseudo-audit; Archive/Audits until MAINT-29) | `Admin/AAudits/Superseded/AUDIT_18_Admin-Ship_of_Theseus.md` | 2026-10-28 | Vibe, Repo Custodian, delegated-maintenance pseudo-audit | base 8eb2949 | 7,713 | `7f83fc5a616b1578b5e91ee01d707de995a0936c` |
| B | `Admin/AAudits/CAMPAIGN_AUDIT_18_Admin-Ship_of_Theseus.md` | `Admin/AAudits/Superseded/CAMPAIGN_AUDIT_18_Admin-Ship_of_Theseus.md` | 2026-10-28 | Vibe, Skeptic/Auditor, VibesSandbox stream | head 982e958 | 9,215 | `1a795ea8671e9e177758512efdadcaab0393188f` |
| C | `Admin/AAudits/CAMPAIGN2_AUDIT_93_Admin-Ship_of_Theseus.md` | `Admin/AAudits/CAMPAIGN2_AUDIT_93_Admin-Ship_of_Theseus.md` (not relocated) | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 38226280 (target blob `36f6f807…`, 32,787 bytes) | 3,819 | `f57cd28539ac4b96e1687a9b73fdeecd8036076a` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | aging | All four ST entries past the 90-day Aging Rule (ST-001/002 177d, ST-003 142d, ST-004 124d) | AUDIT_18 §Findings F1 | Enacted | eee122a6ce (2026-10-28 Brief 2026-10-28b batch): live fetch 2026-10-31 shows all four sidecars read "Last Reviewed | 2026-10-28" | |
| A-F2 | F2 | WARNING | X10 value-parity | Header `Highest Risk | Medium` vs sidecar ST-004 `Risk | High` | AUDIT_18 §Findings F2 | Enacted | eee122a6ce: live File State reads `Highest Risk | High`; own Resolution Log 2026-10-28 entry records "F1/X10: … Medium → High" | |
| A-F3 | F3 | NOTE | X3 | ASM- series (ASM-001–004); within-folder collision continues | AUDIT_18 §Findings F3 | Standing-open | Within-folder X3 ruling open | |
| A-F4 | F4 | NOTE | positive | Healthiest full-schema posture: three-way parity, model PKC-027 hold, canonical anchors | AUDIT_18 §Findings F4 | Positive-record | n/a | |
| B-F1 | F1 | WARNING | X10 value-parity | Same defect as A-F2, independently found | CAMPAIGN_AUDIT_18 §Findings F1 | Enacted | eee122a6ce (same fix; own log entry names "AUDIT_18 (campaign) F1/F2 enacted") | |
| B-F2 | F2 | WARNING | bare citation (X3-family) | ST-004 body cites "AP-012" without owning-file qualifier, against the in-force PKC-003 rule | CAMPAIGN_AUDIT_18 §Findings F2 | Enacted | Live fetch 2026-10-31: the citation reads "`Admin/Auditor_Protocols.md` AP-012" — qualified; eee122a6ce log entry records F2 enacted | |
| B-F3 | F3 | WARNING | stale routing promise | ST-004 "Route to Security_Protocols.md" with no receiving tracker entry for four months | CAMPAIGN_AUDIT_18 §Findings F3 | Enacted | 9f374e7b31 (2026-10-28): SEC-013 reciprocal unknown registered in `Admin/Security_Protocols.md` ("cross-file reciprocal of Ship_of_Theseus.md ST-004"; brief-ID SEC-012→SEC-013 collision fix); verified in SP's live File State | |
| B-F4 | F4 | NOTE | X3 | Folder Designation ruling registered; within-folder collision and CT-007 still open | CAMPAIGN_AUDIT_18 §Findings F4 | Closed-by-ruling (partial) | CT §1 Folder Designation Characters registered (fee92b4, 2026-10-28); within-folder X3 ruling remains Standing-open (see A-F3) | |
| B-F5 | F5 | NOTE | positive | Model PKC-027 disposition; ST-004 adversarial finding; honest-empty tables | CAMPAIGN_AUDIT_18 §Findings F5 | Positive-record | n/a | |
| C-N1 | (none) | NOTE | positive / X10 control case | Clean pass: zero findings; header `Highest Risk | High` re-verified against live sidecar ST-004 `Risk | High` — the X10 pattern's control case, A-F2/B-F1 repairs holding | CAMPAIGN2_AUDIT_93 §Checks 1–11 | Positive-record | n/a | |
| C-N2 | (none) | NOTE | positive | Open-sidecar parity re-derived from live Unknowns.md v5.75: ST-001/002/003 In-Progress, ST-004 Open = File State 4 open; aging refreshes from eee122a6ce still holding | CAMPAIGN2_AUDIT_93 §Check 1 | Positive-record | n/a | |

## 3. Cross-pass logic map

- Both passes ran 2026-10-28 in the same fetch window; the 2028b enactment batch (eee122a6ce) landed after both were issued and resolved every WARNING from both lanes: aging (sidecar Last Reviewed refreshes), X10 (header → High), the bare AP-012 citation, and — via SEC-013 (9f374e7b31) — the unfulfilled routing promise, which only pass B had found.
- Checklist authority: pass B's 1–10 protocol (same head, deeper cross-reference work); pass A adds the custodian lane's independent parity/aging/X10 confirmation. Pass C (10-31) is the first clean full-protocol pass on this target and converts the X10 repair lineage into the corpus's control case: every A/B WARNING is Enacted with live re-verification, nothing new found.
- The 2026-10-29 X3 retrofit (f8e8212a78, Part 3/4) later touched the file again (4 further qualifications, Last Audit 2026-10-29) — post-dates passes A/B, recorded for continuity; pass C audited the post-retrofit state.
- Composite refs A-Fn/B-Fn/C-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

| Original path | Moved to | Blob SHA (before = after) |
|---|---|---|
| `Admin/AAudits/AUDIT_18_Admin-Ship_of_Theseus.md` | `Admin/AAudits/Superseded/AUDIT_18_Admin-Ship_of_Theseus.md` | `7f83fc5a…` |
| `Admin/AAudits/CAMPAIGN_AUDIT_18_Admin-Ship_of_Theseus.md` | `Admin/AAudits/Superseded/CAMPAIGN_AUDIT_18_Admin-Ship_of_Theseus.md` | `1a795ea8…` |

**Cited from outside the Audits home:** `Routing.md` — rows repointed in the sweep commit; `Archive/Audits/README.md` caution — updated in the sweep commit; `Archive/Audits/SESSION_STATUS.md` dated lines — frozen, dangling by design.

## 5. Addenda

- **2026-10-31 (MAINT-47, amalgamation tranche 1):** Pass C (`CAMPAIGN2_AUDIT_93_Admin-Ship_of_Theseus.md`) folded in by Vibe (Repo Custodian). Consolidation only per PKC-020 — no disposition, Status, supersession, or Verified-by column advanced; the Rule 5 separate-verifier hand-off remains pending. Non-independence disclosed: amalgamator and pass-C depositor are the same Vibe line (Genesis Phase).
