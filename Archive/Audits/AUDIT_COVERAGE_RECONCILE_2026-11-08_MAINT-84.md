# AUDIT_COVERAGE_RECONCILE — 2026-11-08 (MAINT-84)

**Status:** First reconcile report — Rule 10 §5c oracle, leg (i), first execution (the mechanical leg)
**Created:** 2026-11-08 by Vibe (Repo Custodian — MAINT-84 stage 3, delegated under the 2026-11-02/04 co-author mandate; commission verbatim: "Ratify all.")  ·  **Target:** `Archive/Audits/AUDIT_COVERAGE_LEDGER.md` (Table I/II migration)  ·  **Scope:** the 29 aggregated targets
**Non-independence:** Genesis Phase — the classifier implementer, the count recorder, and this report's author are the same Vibe line; disclosed. The five frozen fixtures were hand-counted by the same line: leg (i) is intra-line by construction; leg (ii) — the external sample recount — is the independence leg and is owed at the next human-routed external review.
**Execution disclosure:** the mechanical counts below were derived on the composing line by an equivalent TypeScript implementation of the fixed classifier over sha-pinned fetches at LF head `9ab3cce7`, cross-checked in three batch derivations (10/10/8 targets, each re-derived from the fetched §2/§5 text); `Automation/coverage_ledger_regen.py` mirrors that logic, but its first live execution is owed (no Python runtime on the composing line). The Table II values landed in the same commit as this report; the script's first run should reproduce them exactly.

## 1. Method (the fixed classifier)

- Severity = the first whitespace token of the Severity cell, uppercased. Counting severities: MAJOR, WARNING, CRITICAL, FAIL (the ratified §2 vocabulary; no CRITICAL or FAIL severity has been emitted to date). INCOMPLETE and structural "—" rows never count (the A-CORR correction rows are structural).
- Disposition = the first pipe cell from index 4 onward starting with a recognized keyword. Compound dispositions split on "/": a row carries if ANY segment starts with a carrying keyword — the first-keyword-only rule undercounts compound rows, and correcting it was the defining fix of this pass (HDL A-F1, ISP A-F1, PROBE A-F1 are the compound rows that changed the counts; disclosed in the MAINT-84 entry as a harness-defect-class abort caught before any value was recorded).
- Carrying: Standing-open, Not re-tested, Asserted, Reported-not-fixed, Disclosed defect. Edge case disclosed: "Reported-not-fixed (historical)" (Canonical_Terms A-F2) counted carrying — the ledger convention's three-term list read as illustrative, not exhaustive.
- Open M/W/F = counting severity + carrying disposition ("Asserted (enacted)" rows count open per the carrying convention; their refs are visible in the Table II trigger cells). Open W-C (strict) = NOTE severity + a segment starting Standing-open or Watch-carried.
- Edge cases recorded, no rule change proposed: GC B-D1 and RIP B-D1 ("Disclosed defect", NOTE severity) and RIP A-N1 ("Not re-tested", NOTE severity) count in neither column under strict §3 — carrying keywords on NOTE rows count only when Standing-open/Watch-carried; watch items. GMP A-F3 "WARNING (MAJOR category)" counts as WARNING (first-token severity). A disposition cell with no recognized keyword counts nowhere; the reconcile would surface any resulting drift.

## 2. Totals

- 29 aggregated targets (28 existing + Operational_Conventions composed this pass; ledger row 24's deferral cleared at MAINT-63).
- Mechanical: **52 Open M/W/F / 34 Open W-C**. Recorded (the old single-table register): **62 open over 28 targets**. **13 mismatches** (table below), all bookkeeping drift — no disposition was edited by this pass (PKC-023).
- The 64 pass-holding non-aggregated rows carried unchanged (nothing re-counted; Last counted as recorded).

## 3. Per-target recorded vs mechanical

| # | Target | Recorded open | Mechanical open | Mechanical W-C | Diagnosis |
|---|---|---|---|---|---|
| 1 | Adm_Scope_Map | 2 | 2 | 2 | match |
| 2 | Agent_Verification_Event | 3 | 2 | 2 | MAINT-59 hand-count drift (Table II now mechanical) |
| 4 | Autonomy_Divergence_Protocol | 6 | 5 | 1 | MAINT-59 hand-count drift (Table II now mechanical) |
| 6 | Canonical_Terms | 4 | 3 | 0 | MAINT-59 hand-count drift (Table II now mechanical) |
| 7 | CIR_Gov | 3 | 1 | 0 | stale §2 rows A-F2 (re-label owed, §5d — section 4); recorded count = MAINT-59 hand-count drift |
| 8 | Computational_Institutional_Reasoning | 4 | 3 | 2 | MAINT-59 hand-count drift (Table II now mechanical) |
| 9 | Economics | 0 | 0 | 1 | match |
| 10 | Engineer_Protocols | 2 | 2 | 1 | match |
| 11 | Environmental_Constraints | 5 | 4 | 2 | MAINT-59 hand-count drift (Table II now mechanical) |
| 12 | Ethical_Constraints | 4 | 3 | 1 | MAINT-59 hand-count drift (Table II now mechanical) |
| 13 | Experiments | 0 | 1 | 1 | stale §2 rows A-F2 (re-label owed, §5d — section 4); recorded count = MAINT-59 hand-count drift |
| 15 | File_Template | 3 | 3 | 3 | match |
| 17 | Governance_Charter | 3 | 3 | 2 | match |
| 18 | Governance_Migration_Protocol | 2 | 3 | 1 | stale §2 rows B-N2 (re-label owed, §5d — section 4); recorded count = MAINT-59 hand-count drift |
| 19 | Hardware_Diversity_Ladder | 1 | 1 | 1 | match |
| 20 | Integrity_Incident_Log | 0 | 0 | 2 | match |
| 21 | INTEGRITY_SWEEP_PROMPT | 1 | 1 | 3 | match |
| 22 | Metrics_Scaffold | 0 | 0 | 1 | match |
| 23 | Nothingness_Theorem | 0 | 0 | 3 | match |
| 24 | Operational_Conventions | — | 0 | 0 | aggregate composed this pass (row 24 deferral cleared at MAINT-63); computable 0/0 |
| 25 | PROBE_INVOCATION | 3 | 3 | 0 | match |
| 26 | Progress_Log | 1 | 1 | 1 | match |
| 27 | Repository_Integrity_Protocol | 1 | 0 | 1 | stale §2 rows B-N1 (re-label owed, §5d — section 4); recorded count = MAINT-59 hand-count drift |
| 28 | Repository_Structure | 2 | 2 | 1 | match |
| 29 | Resolution_Methodology | 2 | 1 | 1 | MAINT-59 hand-count drift (Table II now mechanical) |
| 31 | Security_Protocols | 4 | 3 | 0 | MAINT-59 hand-count drift (Table II now mechanical) |
| 32 | Ship_of_Theseus | 0 | 0 | 1 | match |
| 33 | Trajectories | 3 | 3 | 0 | match |
| 34 | Verification_Gates | 3 | 2 | 0 | MAINT-59 hand-count drift (Table II now mechanical) |

## 4. Stale §2 rows — re-labels owed (§5d), NOT executed

Eight aggregate §2 rows still read "Standing-open" while their own §5 addenda record MAINT-63 (2026-11-05) RESOLVED-BY-EXECUTION/RULING. Per the ratified §5d the re-label is owed at each aggregate's next substantive touch; per PKC-023 the graded rows are unchanged this pass, and Table II counts §2 as-is.

| Aggregate | Ref | Counted in | Resolution of record (its own §5 addendum) | Post-re-label effect |
|---|---|---|---|---|
| CIR_Gov | A-F2 | Open M/W/F | MAINT-63 §3.5: RESOLVED-BY-EXECUTION (CIR-GOV-002 mirrored in the Unknowns §5 resolved-entries paragraph) | open 1 → 0 |
| Experiments | A-F2 | Open M/W/F | MAINT-63 §2: RESOLVED-BY-EXECUTION (the three candidate-ID pointers qualified with owning-file citations) | open 1 → 0 |
| Governance_Migration_Protocol | B-N2 | Open W-C | MAINT-63 §2 Category A: RESOLVED-BY-EXECUTION (20 bare citations qualified on 15 lines in the audit-flagged zones) | W-C 1 → 0 |
| Integrity_Incident_Log | B-N2 | Open W-C | MAINT-63 §2 / §3.11: RESOLVED-BY-EXECUTION (two live-section citations qualified, frozen history preserved bare) | W-C 2 → 1 |
| INTEGRITY_SWEEP_PROMPT | B-N1 | Open W-C | MAINT-63 §8: RESOLVED-BY-RULING (the commission-closure note recorded verbatim in the owning File State) | W-C 3 → 2 |
| Nothingness_Theorem | B-N2 | Open W-C | MAINT-63 §3.3: RESOLVED-BY-RULING (Unknowns Size Management Rule 7, Tier 0 indexing convention) | W-C 3 → 2 |
| Repository_Integrity_Protocol | B-N1 | Open W-C | MAINT-63 §2 Category A: RESOLVED-BY-EXECUTION (six bare cross-file citations qualified) | W-C 1 → 0 |
| Repository_Structure | B-N1 | Open W-C | MAINT-63 §7: RESOLVED-BY-EXECUTION (dated §II subfolder-convention note) | W-C 1 → 0 |

## 5. Tensions and notes (record-only)

- RIP A-F1: the RIP aggregate's §5 addendum ends "A-F1 remains unchanged (open)" while its §2 row reads Closed-by-ruling (PKC-003) — a wording tension within one artifact; recorded only, no action proposed.
- The redraft review's heuristic pass (35 rows / 22 aggregates carrying NOTEs) was a reviewer's rough count, never adjudicated; the mechanical values here supersede it as the count of record.
- Fixture freeze: the five frozen fixtures are dated 2026-11-08; if a fixture target's §2 changes, the fixture fails by design and must be re-frozen by dated addendum in this home, never edited silently.

## 6. Oracle legs

- Leg (i) — frozen hand-counted fixtures: embedded in `Automation/coverage_ledger_regen.py` (Adm_Scope_Map 2/2, Economics 0/1, Verification_Gates 2/0, Hardware_Diversity_Ladder 1/1, INTEGRITY_SWEEP_PROMPT 1/3, hand-counted 2026-11-08 MAINT-84); the script's first live execution is owed at the next Python-capable pass.
- Leg (ii) — external sample recount: owed at the next human-routed external review; a dated report in this home (AUDIT_COVERAGE_RECONCILE_<date>) is the expected form.

Corrections by dated addendum only.
