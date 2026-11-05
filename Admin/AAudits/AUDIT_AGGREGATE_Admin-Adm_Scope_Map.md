# AUDIT_AGGREGATE — Admin/Adm_Scope_Map.md

**Status:** Dispositions unverified (Rule 5 separate-verifier hand-off pending — assign an agent other than the disposition writer)
**Created:** 2026-11-04 by Vibe (Repo Custodian — MAINT-58 tranche-2 aggregation sweep)  ·  **Target:** `Admin/Adm_Scope_Map.md`  ·  **Passes:** 2
**Non-independence:** Genesis Phase — pass depositors, disposition writer and this amalgamator are the same Vibe line; disclosed per MAINT-38 and the aggregate template.
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on. Rules per `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`. Originals not relocated (tranche-1 MAINT-47 precedent: fold only; relocation is a separate per-task lane). Target is an Active — Index file (per-folder scope-map exemption, Template Exemptions class 4); checks adapted to index class per the AUDIT_16 precedent.

## 1. Provenance

| Pass | Original path (at issuance) | Current path | Date | Auditor / lane | Head at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | `Admin/AAudits/CAMPAIGN_AUDIT_26_Admin-Adm_Scope_Map.md` | unchanged (live in `Admin/AAudits/`) | 2026-10-28 | Vibe, Skeptic/Auditor, VibesSandbox audit stream (PKC-020 findings-only) | head eee122a6 | 12,958 | `4bce16b6883f59629243532ffaefccbe47c42668` |
| B | `Admin/AAudits/CAMPAIGN2_AUDIT_96_Admin-Adm_Scope_Map.md` | unchanged | 2026-10-31 | Vibe (GLM 5.3), Skeptic/Auditor, Campaign 2 (PKC-020), non-independent Genesis Phase | commit 38226280 | 3,369 | `93404430df8c9b79a7cf746c48a667ec7828800d` |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | WARNING | Kit entry's Open Unknowns count stale (X8 — the index lagging its owning file, the map's own founding failure mode) | Kit entry reads "7 Open Unknowns" while Kit v1.25's File State reads 5 — PKC-022 (2026-10-27, option B) closed FAK-014..019 by pin retirement ("11 → 5"); the 10-28b recompute honestly scoped itself to Risk entries only | CAMPAIGN_AUDIT_26 §Findings F1 | Not re-tested | Recommended one-pass fix (7 → 5 with a PKC-022-citing dated note) queued for the delegated batch; the Kit row was not re-opened at fold-in — carried for verifier | |
| A-F2 | F2 | WARNING | AP entry's Spec Gates figure diverges from Discovery's snapshot (X10-class) | Map reads "AP · 4/6 · 10 Open Unknowns" vs Discovery's "5/6 (G1, G3, G4, G5, G6 clear)" — two navigation indexes disagree today; the map's own file-wins rule routes resolution to AP's File State | CAMPAIGN_AUDIT_26 §Findings F2 | Standing-open | Resolves at the Auditor_Protocols audit (LAST), which holds the divergence plus the map's "10 Open Unknowns" claim for AP | |
| A-F3 | F3 | NOTE | NT entry omits the Open Unknowns count | The Nothingness_Theorem entry carries no Open Unknowns field though NT holds 10 (NT-001–NT-010, three-way-verified at CA24); Tier 0 exempts gates, not unknowns | CAMPAIGN_AUDIT_26 §Findings F3 | Standing-open | Index-format polish queued at issuance (delegated batch); not re-verified at fold-in | |
| A-F4 | F4 | NOTE | CIR entry's Risk field carries an ID, not a value | "Risk: CIR-001" — the only entry whose Risk field is an unknown ID rather than a column-vocabulary value; shape inherited from Discovery's snapshot; the 10-28b recompute established the value convention for this column | CAMPAIGN_AUDIT_26 §Findings F4 | Standing-open | Index-format polish queued at issuance ("High (CIR-001)" or the owning file's value); not re-verified at fold-in | |
| A-F5 | F5 | NOTE | positives incl. verified delegated adoptions | Coverage complete (32/32) with the tier table recounted exact; five of five 2026-10-28/28b delegated adoptions independently verified against session fetches — CT 9→10 (= AUDIT_11 F1, cross-ref of this aggregate set), Trajectories Risk High (AUDIT_13 F5), SoT Risk High (AUDIT_18 F1), Economics Risk High (AUDIT_19 F1), CT Risk High citing CT-004/CT-007; EC's flagship 16→7 stale-count harvest; the AUDIT_16 Convention-7 carried check resolved clean | CAMPAIGN_AUDIT_26 §Findings F5 + Checklist | Positive-record | n/a | |
| A-IN1 | INCOMPLETEs | INCOMPLETE | carried checks | AP Spec Gates divergence (→ AP audit LAST); tier-table figures inherited from `Tests/Admin_Governance_Teardown_POC.md` (→ Tests/ sweep); the single unaccounted entry-addition date (git history); Security_Protocols entry recorded-as-reported | CAMPAIGN_AUDIT_26 §INCOMPLETEs carried forward | Not re-tested | Owning sweeps pending | |
| B-C1 | (none) | NOTE | positive | Checks clean: registration parity spot-checked live and exact on the rows opened this batch — AVE row "4 Open Unknowns (AVE-R1–R4…; R1 and R4 also indexed" matches live AVE including the honest disclosure of the R2/R3 index gap; ECO row "5 Open Unknowns (ECN-001/002/004/005/006) · Risk: High (ECN-002 — recomputed 2026-10-28)" matches live Economics and the index exactly | CAMPAIGN2_AUDIT_96 §Checks 5 + Bottom line | Positive-record | n/a | |

## 3. Cross-pass logic map

- Pass A (10-28) is itself the adoption record for five verified delegated enactments of other files' findings — this map is where the corpus's cross-file corrections became verifiable in one place. Its own defects are stale-index spots the 10-28b recompute honestly did not claim to cover (Kit count; AP gates), plus two format gaps (NT count; CIR Risk-as-ID).
- Pass B (10-31) spot-checked registration parity against live owners (AVE, Economics) and found the map matching exactly, including its honest disclosure of the AVE-R2/R3 index gap. Neither pass re-derived the rows A left queued (Kit, AP, NT, CIR format), so those remain carried.
- Index-class asymmetry disclosed: A graded the map against its owners; B graded the map's rows against the same owners live — the two passes' clean/finding split reflects which rows each opened, not a change in the map's health. Composite refs A-Fn/B-Fn are the only safe citation form (Template Rule 2).

## 4. Pointers

Originals are not relocated; both passes remain live at their deposit paths in `Admin/AAudits/`. **Cited from outside the Audits home:** `Routing.md` rows (registered at deposit); the verified-adoption records (AUDIT_11 F1, AUDIT_13 F5, AUDIT_18 F1, AUDIT_19 F1 in their aggregates and original passes); the AP-audit LAST inheritance set (A-F2); dated lines in `Archive/Audits/SESSION_STATUS.md` addenda and sandbox session records — frozen history, dangling by design.

## 5. Addenda

None. Corrections by dated addendum only.
