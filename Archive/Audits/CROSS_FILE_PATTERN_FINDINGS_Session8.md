# CROSS_FILE_PATTERN_FINDINGS_Session8.md — Campaign 2, Tests/ + Challenges/ phases

**Issued:** 2026-10-30 · **Auditor:** Vibe (AI Auditor, Campaign 2) · **Scope:** CAMPAIGN2_AUDIT_35–62 (18 Tests reports, 10 Challenges reports) · **Head at fetch:** 4611f9f8dcdd9aeae4c099366806daaccf99f95f · **Corpus-wide artifact — Archive/Audits/ home per MAINT-29 convention. Findings-only (PKC-020): no audited file was modified.**

This document aggregates cross-file patterns visible only across the Tests/ (17 doctrine files + index) and Challenges/ (9 files + index) passes. Per-file evidence lives in the deposited reports (Tests/TAudits/, Challenges/CAudits/).

## X10 — Highest Risk parity — now four sub-shapes corpus-wide

1. **Value-miss (understatement, now Critical-grade):** Cognitive_Salvage_Layer (High vs GH-009 Critical), Pyrolysis_Cascade (High vs PYC-001/003/004 Critical), Solar_Descent (High vs SD-UNK-004 Critical). Tests repeats the MS/Thermal shape from Session 6, but with Critical understatements — worse, because the headers actively understate safety-relevant maxima.
2. **Field-format (sentence, no value):** Closed_Loop_Feedstock and Return_To_Eden (both name the right entries but carry no severity value); Local_Governance_Framework (Session 6) is the ancestor.
3. **Missing field / parity INCOMPLETE:** MAQT, Chrono_Divergence, Chrono_Divergence_Pilot, Admin_Governance_Teardown_POC, Quorum_Agent_Conduct_Protocol (Tests); the 7 Challenges Problem-Statement files by documented subtype design (no Highest Risk/Open Unknowns header fields at all). Positive counter-example: **Living_Waters is the corpus's first correctly stated Critical header** (Highest Risk Critical = max open Critical, with justification).
4. **Inherited map labels:** the Scope Maps faithfully repeat their owning files' understated "High" rows (CSL, Pyrolysis, Solar). The maps are not defective; the recompute batch must start at the owning files or the maps will re-inherit the error.

**Standing recommendation (extended):** a Highest-Risk recompute batch covering Architecture (MS, Thermal), Tests (CSL, Pyrolysis, Solar), and Challenges (CLF, RTE — which need value *assignment*, not recompute), followed by a Scope-Map row refresh.

## Aging — two folder clusters, opposite disciplines

- **Tests:** Living_Waters (all 9 at ~138d, incl. two Critical — the campaign's strongest aging finding), Support_Raft (~141d, incl. required-before-v1.0 SR-001), Trophic_Forge (~138d), Solar_Descent (~138d + 92d tier), Cognitive_Salvage_Layer (up to ~128d), Hydrologic (122–124d). Operations/ had zero tripped aging; Tests has the worst cluster so far.
- **Challenges:** Problem-Statement registrations at 2026-07-11/12 (~111d: BF, CM, PO, WS; ES at ~103–110d) and RTE's RE-UNK-001–005 at ~122d. **Notably, 7 of 9 Challenges files self-flag their own aging in Drift Indicators** — a discipline other folders lack. Exceptions: Closed_Loop_Feedstock's aged Criticals (CLF-003/004, ~115d) are NOT self-flagged, and Waste's indicator is stale (below).
- **Emergence discrepancy:** EM-004's indicator claims ">90 days" but visible registration dates give 74 days — indicator-clock mismatch, ruling needed.

**Standing recommendation:** an aging review batch, first candidates Living_Waters, Support_Raft, Return_To_Eden, then the Challenges Problem-Statement sets.

## X3 — retro completeness: in-whitelist stragglers found post-retrofit

The 2026-10-30 X3 Tests pass qualified citations but missed bare in-whitelist instances in operative text: Cognitive_Salvage_Layer (AP-033 line 607, AP-001 line 779), Leviathan_testing (CF-002 line 108), Multi_Agent_Quorum_Trial (GMP-004 line 132, GOV-008 line 558). Frozen-history exclusions were honored everywhere checked; the Challenges misses are zero (CLF's CT-011/AP-032 instances are all in frozen log history). **A completion sweep of Tests operative text is recommended** before the retro is declared closed. MAQT_Role_Cards_and_Cycle1_Task (GOV-008, GMP-004, EC-013) was NOT covered by the retro (PKC-038 non-canonical derived excerpt): coverage ruling + Ethical-Anchor exemption ruling both remain with the human.

## X8 — Scope-Map staleness (now 5 rows across two maps)

Tests map: MAQT row ("0 Open Unknowns (registered)" vs live 3 registered), Support_Raft row ("13 Open" vs corrected 12), QCC row (self-contradictory "0 registered" vs "R2/R5/R7 also indexed in `Unknowns.md`"). Challenges map: Emergence row (Status Exploration vs live Active), Return_To_Eden row (G4–G6 "cleared" vs PKC-042 stale-hold). Combined with Session 6's four Arc rows, the row-refresh recommendation now spans three maps. Positive: the Tests map's own PKC-041/PKC-031 correction log is exemplary.

## X11-adjacent — unlogged pass

Solar_Descent's Last Audit records a 2026-09-15 sibling scan (TMR over-attribution correction) with no corresponding Resolution Log entry (newest log entry 2026-08-11) — same shape as Governance_Charter's F1 (Session 4). If findings-only exemptions apply, the log entry convention still expects a record; ruling with the human.

## X9-adjacent — structural

Quorum_Agent_Conduct_Protocol: File State table with no `## File State` heading — invisible to heading-based tooling (this campaign's parser initially missed it; corrected before deposit). Same family as Forge_flow's unheaded sidecar table (Session 6).

## New sub-shape — drift-indicator decay

Waste's drift indicator cites WA-002 and WA-004 as "unreviewed past 90 days" — both are now Resolved (WA-004 via consolidation; WA-002 with R1 keeping it functionally blocking). Resolutions without indicator refresh produce indicators that erode the file's own early-warning value. Recommendation: indicator refresh added to the resolution checklist.

## Folder-level conventions requiring a human ruling

1. **Risk vocabulary divergence:** Challenges Problem-Statement files use Major/Minor (plus Critical), the rest of the corpus uses High/Medium/Low; Emergence uniquely carries dual Risk + Priority columns (and used them correctly on 2026-10-25 to fix EM-004's Critical mislabel). A corpus vocabulary ruling is recommended.
2. **Challenges numbered-heading convention** (`## 2. Scope Boundary`): documented in-map as a tooling trap; confirmed independently by this campaign's parser.
3. **Problem-Statement header field-set** (no Open Unknowns/Highest Risk/Spec Gates): documented as design; means header-vs-body count parity is formally INCOMPLETE for 7 files by construction. If the human wants parity checkable, a subtype field standard is needed.
4. **T1 Log-Split queue:** Persistent_Cognition_Candidates (~82KB) joins Forge_flow (~179KB), Auditor_Protocols (~157KB), Governance_Charter (~130KB). Split-order ruling still open.

## Positives worth preserving

- Living_Waters: first correct Critical header in the corpus.
- Emergence: dual-column Risk/Priority corrective (10-25) and same-day X3 supplemental straggler entry (10-30) — the retro-completeness standard other files should copy.
- Waste: WA-002-R1/R2/R3 resolution decomposition.
- Return_To_Eden: PKC-042 hold annotation resolving its own stale-gate self-contradiction.
- Challenges drift-indicator self-flagging discipline (with the Waste exception).
- Sidecar count parity: perfect in both folders where fields exist (13/13 where checkable in Tests; 6/6 in Challenges Solution-Track files).

## Standing recommendations register (cumulative)

1. Highest-Risk recompute batch (extended to Challenges value-assignment).
2. Aging review batch (Tests cluster first).
3. Scope-Map row-refresh batch (three maps).
4. X3 Tests completion sweep + RoleCards coverage/anchor rulings.
5. T1 Log-Split order ruling (four files queued).
6. Risk-vocabulary corpus ruling.
7. Drift-indicator refresh on resolution (new).
8. Out-of-whitelist bare-ID and X1 retroactivity rulings (carried from prior sessions).
