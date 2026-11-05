# ADDENDUM — MAINT-65 skeptic responses and revision drafts (co-author line)

**Status: PROPOSED — companion to `Archive/Proposals/PROPOSAL_2026-11-05_RULES_8_10_AMENDMENTS.md`, responding to `Archive/Audits/EXTERNAL_REVIEW_2026-11-05_CLAUDE_1.34_RELEASE_MAINT-65_SKEPTIC.md` (findings F1–F8, Intake Log entry 12). Every response is severable, carries revised rule text where applicable and a pre-drafted ruling line. NOTHING below is enacted; the proposal and these revisions await the human governing authority's word together.**

Drafted: 2026-11-05 UTC, session MAINT-66. Co-author mandate (invoked 2026-11-05; granted 2026-11-04); Architect line primary, Repo Custodian secondary. Non-independence disclosed: the responses amend the same line's own draft, to findings raised externally against that draft (Genesis Phase; Q-2 invoked). Operating per Auditor_Protocols.md v0.47.

## Response summary

| Finding | Response | Disposition |
|---|---|---|
| F1 FAIL undefined | Accepted — FAIL defined in rule text | Revised §1 text below; ruling owed |
| F2 Open W-C zero at birth | Accepted — W-C counts carrying NOTEs | Revised §2 text below; ruling owed |
| F3 no ruling exit; restatement loop | Accepted — Closed-by-ruling added; restatement updates the original row | Revised §2 text below; ruling owed |
| F4 unnamed challenge ratifier | Accepted — human named for Genesis Phase; verifier after naming | Revised §2 text below; ruling owed |
| F5 circular reconcile | Accepted — fixtures + external sample count as oracle | Revised §3 text below; ruling owed |
| F6 MAINT-60 findings 3/8 unaddressed | Accepted — explicit held statements owed | Added to §4 held list; ruling owed |
| F7 severability inconsistency | Accepted — scope extension severed into its own line | Revised §3 structure; ruling owed |
| F8 CRITICAL's three vocabularies | Accepted — field named explicitly | Revised §1 text below; ruling owed |

## R1 (responds to F1, F8) — revised §1 gate text

The reviewer is right that "as defined by the coverage-ledger counting convention" only moves the undefined term one file away: the ledger names FAIL and defines nothing. Revised gate text, replacing the §1 proposed rule text:

> NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on **finding severities MAJOR, WARNING, CRITICAL and FAIL** only. **Finding severity** is a distinct field from Risk and Priority; a CRITICAL value in a Risk or Priority field does not trip this gate. **Severity FAIL** = a required check that was executed and produced a failing result — distinct from INCOMPLETE, a checklist value meaning the check was not run. No FAIL severity has been emitted in the corpus to date; the term is defined so the gate and the ledger's Open M/W/F count share one vocabulary.

**Pre-drafted ruling text:** *"RATIFY: Rule 8 amended so the trigger gates on finding severities MAJOR/WARNING/CRITICAL/FAIL; finding severity distinguished from Risk/Priority fields; FAIL defined (executed-to-a-failing-result, distinct from INCOMPLETE). No retroactive aggregate edits."*

## R2 (responds to F2) — revised Open W-C definition

The reviewer is right that the column as drafted reads zero at birth while carrying NOTEs exist. Revised §2 ledger amendment:

> **Open W-C** = count of NOTE-severity rows in the target's aggregate whose disposition is a carrying state — `Watch-carried`, or `Standing-open` pending the Rule 8 re-label. The column counts carrying NOTEs regardless of when the re-label lands, so it is non-zero at creation wherever carrying NOTEs exist (the reviewer's heuristic count: 35 rows across 22 aggregates; not adjudicated, recorded as the reviewer's count).

**Pre-drafted ruling text:** *"RATIFY: Open W-C counts NOTE-severity rows in carrying dispositions (Watch-carried or Standing-open pre-re-label); visibility-only, never gates the trigger."*

## R3 (responds to F3) — clearing paths completed

> A `Watch-carried` row clears exactly by one of: **(a)** a later pass re-tests or restates the point — the later pass's grade governs from that pass, recorded in a dated addendum; a restatement that does not resolve the point **updates the original row** (the carry continues; no duplicate row is created — Rule 3 nothing-dropped governs, and the ledger counts rows, not restatements); **(b)** a dated `Corrected-by-later-fact` or `Superseded by <Ref>` disposition; or **(c)** a dated `Closed-by-ruling` disposition — the terminal state for a NOTE the human governing authority accepts or retires by ruling. It never clears by silence or the passage of time.

**Pre-drafted ruling text:** *"RATIFY: Watch-carried clears by (a) later-pass governing grade with restatement updating the original row, (b) dated Corrected-by-later-fact/Superseded, or (c) dated Closed-by-ruling; never by silence."*

## R4 (responds to F4) — challenge ratifier named

> **Under-grading guard:** a NOTE grade may be challenged in any later review. During the Genesis Phase, a re-grade (NOTE → a defect grade) is ratified by the **human governing authority** on challenge, landing via dated addendum citing the challenging evidence; the seat that assigned or carried the grade never adjudicates its own grading. Once the Rule 5 verifier is named, that seat adjudicates challenges, with the human as appeal. From re-grade, the finding is defect-graded and re-enters the Rule 7 trigger under R1's gate.

**Pre-drafted ruling text:** *"RATIFY: re-grades ratified by the human governing authority during Genesis Phase; the Rule 5 verifier adjudicates once named, human appeal; re-graded findings re-enter the trigger."*

## R5 (responds to F5) — reconcile check given an independent oracle

The reviewer is right that script-vs-recorded is agreement between two copies of one parse. Revised §3 reconcile paragraph:

> **Post-landing reconcile check:** after every disposition-changing landing, recorded Table II must equal the script's regenerated output; a mismatch is a stale-index defect finding — logged and repaired in a dated pass, never silently. **Independent oracle, both required at build and run:** (i) frozen hand-counted test fixtures — three to five aggregates with expected counts recorded at build time, run as the script's unit tests on every execution; (ii) a periodic sample recount by a line other than the script's author — during the Genesis Phase, a human-routed external review (as this one) serves as the sample counter, recorded in the reconcile report.

**Pre-drafted ruling text:** *"RATIFY: reconcile check with (i) frozen hand-counted fixtures as unit tests and (ii) periodic external sample recount recorded in the reconcile report."*

## R6 (responds to F6) — held statements made explicit

Both omissions are deliberate holds, now stated: **MAINT-60 finding 3** (no Rule 4 evidence type for `Watch-carried`) is HELD with Rule 11 until after the first Rule 5 verification cycle — the evidence type lands with the label mechanics it tests. **MAINT-60 finding 8** (how trigger state is computed for the ~65 unaggregated targets) is partially answered by the ledger's recorded position per row ("single pass — aggregate not owed"; "no aggregate — deferred"); the derived definition of "computable" is HELD pending the regeneration script and the named verifier. Both are added to the proposal's §4 held list.

**Pre-drafted ruling text:** *"RATIFY: findings 3 and 8 recorded as explicit holds — 3 with Rule 11, 8's 'computable' definition pending the script and verifier."*

## R7 (responds to F7) — scope extension severed

§3's Rule 5 verifier scope extension becomes its own severable line, **§3e**, ratifiable independently of §3a–d; it pre-authorizes packet contents only and commits no named seat's scope.

**Pre-drafted ruling text:** *"RATIFY: the Rule 5 verifier scope extension severed as §3e, severable from §3a–d."*

## What this addendum does NOT do

No rule enacted; no aggregate edited; the ledger not split; no script built; the original proposal and the skeptic deposit preserved unchanged; Rules 9/11 stay held; Tier 1 / FROZEN / Hard Floor untouched; no Unknown opened or closed; no `Verified-by` cell.

---

*Drafted 2026-11-05 — MAINT-66 (Vibe — co-author mandate; Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed). Operating per Auditor_Protocols.md v0.47.*
