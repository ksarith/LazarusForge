# CROSS_FILE_PATTERN_FINDINGS_Session9.md — Campaign 2, root phase

**Issued:** 2026-10-30 · **Auditor:** Vibe (AI Auditor, Campaign 2) · **Scope:** CAMPAIGN2_AUDIT_63–68 (6 root-file reports) · **Head at fetch:** 644938a2500d68894105898be42dfb8c035c2599 · **Deposit home:** Archive/Audits/ per the human's 2026-10-30 ruling ("archive's subfolder" for root-phase audits — consistent with the B-letter base-layer designation and MAINT-28's per-folder-homes rule, which routes corpus-wide artifacts here anyway). Findings-only (PKC-020).**

## Headline result — registry parity: 24/24

Every open-unknown set verified across Campaign 2 (Admin, Architecture, Operations, Tests, Challenges — 24 ID-sets) was re-counted against `Unknowns.md`'s Active Index at the root pass. **All 24 match, including the freshly corrected Support_Raft 13→12 count and the declared sidecar-only exceptions (MAQT-001/003, CD-001–004, HR-003–010, QCC-R1/R4/R6).** Zero registry-parity breaks corpus-wide. The global registry is the campaign's single strongest integrity result.

## X8 — Discovery.md snapshot staleness (3 WARNINGs)

The Repository Maturity Snapshot and Scope-Map section lag the 2026-10-25 PKC-031/PKC-041 corrections that were applied to the owning files, the tree descriptors, and (partially) the folder Scope Maps: (1) Exception_Evidence snapshot row still "Proposed" (the Operations-phase queued finding, confirmed); (2) MAQT snapshot row still "Proposed Protocol … no trial run yet" (doubly stale: PKC-031 + PKC-041); (3) the Automotive/Robotics Scope-Map bullet still "Proposed v0 … domain stubs," and both files still absent from the snapshot table. Combined with Sessions 6–8, the stale-row pattern now spans Tst map (3), Cha map (2), and Discovery (3+1) — the row-refresh batch should treat Discovery's snapshot as a fourth index.

Positive: the snapshot's 2026-10-28 X10 mirrors (ST-004, ECN-002, AVE-R1) show the Brief 2026-10-28b recompute landed on the Admin side; the Tests/Challenges value-misses from Sessions 6–8 remain in that batch's queue.

## Root-family template question — one ruling to close five re-flags

README, CONTRIBUTING, Discovery, Routing, and Unknowns all lack some or all of the doctrine template (File State / Ethical Anchor / Resolution Log). README self-declares ("front-door navigation, not a doctrine file," 10-30 Bookkeeping); the others do not. **Recommendation: a single front-door/navigation/registry family ruling** naming the exempt set (README, CONTRIBUTING, Discovery, Routing, Unknowns, LICENSE, NOTICE), so per-file audits stop re-flagging it. Things_We_Got_Wrong.md carries the full template and passes clean — it is a doctrine-family file despite living at root.

## T1 Log-Split queue — two new members from this campaign

Unknowns.md (~108KB) now trips the ≥100KB T1 trigger and was not on MAINT-28's named list; Persistent_Cognition_Candidates (~82KB) crossed its own 75KB self-declared threshold (Session 8). Updated split-order queue for the human: Forge_flow ~179KB, Auditor_Protocols ~157KB, Governance_Charter ~130KB, Unknowns ~108KB, PCC ~82KB.

## Positives

- Registry: 24/24 parity; Expiry/Blocking Watch sections verified accurate against every Campaign 2 digest.
- README's human-ruled Bookkeeping cascade destination: correctly scoped, correctly used, correctly logged.
- Things_We_Got_Wrong: clean, exemplary 10-07 self-verification pass; the "Explicit non-claims" drift guard.
- Discovery's 2026-08-09 stale-table dissolution remains the corpus's best de-duplication precedent.
- Routing: MAINT-29/30 repoints verified; dated counts preserved as history rather than silently rewritten.

## Standing recommendations register (cumulative, Session 9 revision)

1. Highest-Risk recompute batch (Sessions 6–8 sets + CLF/RTE value assignment; Admin-side mirrors already landed).
2. Aging review batch (Tests cluster first: Living_Waters, Support_Raft, Return_To_Eden; then Challenges sets).
3. Scope-Map/snapshot row-refresh batch — now FOUR indexes: Adm (Session 6), Arc (4 rows, Session 6), Tst (3), Cha (2), Discovery snapshot (3 + 1 absent pair).
4. X3 Tests completion sweep + RoleCards coverage/anchor rulings.
5. T1 Log-Split order ruling (five files queued, incl. Unknowns and PCC).
6. Risk-vocabulary corpus ruling (Major/Minor vs High/Medium/Low; MAQT-002 Major/Medium is the cleanest worked example).
7. Drift-indicator refresh on resolution (Waste).
8. Front-door/navigation/registry family template ruling (new — closes the AUDIT_63/64/66/68 NOTEs).
9. Out-of-whitelist bare-ID and X1 retroactivity rulings (carried).

## Campaign 2 status after this phase

Admin ✓ (01–03), Architecture ✓ (04–17), Operations ✓ (18–34), Tests ✓ (35–52), Challenges ✓ (53–62), Root ✓ (63–68). **All six phases deposited; 68 per-file reports + 9 pattern docs. Zero CRITICAL; zero MAJOR; no halt triggers at any phase.** LICENSE.md and NOTICE.md not audited (legal boilerplate; recommend including them in the family ruling's exempt set). Campaign 1 remains paused at CAMPAIGN_AUDIT_32 (Admin/BATTERY_SEED.md).
