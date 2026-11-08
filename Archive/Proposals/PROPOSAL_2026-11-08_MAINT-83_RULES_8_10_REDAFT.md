# PROPOSAL — Rules 8+10 amendments REDRAFT (consolidating MAINT-65 §1–§3 and the MAINT-66 responses R1–R7) — MAINT-83

**Status: PROPOSED — nothing below is in force. This redraft consolidates `Archive/Proposals/PROPOSAL_2026-11-05_RULES_8_10_AMENDMENTS.md` (§1–§3) and `Archive/Proposals/ADDENDUM_2026-11-05_MAINT-65_SKEPTIC_RESPONSE_AND_REVISIONS.md` (R1–R7) into one ratifiable package: where a response revised the 2026-11-05 text, the revised text governs here. Both originals stay untouched as the provenance trail. Every section is severable and carries pre-drafted ruling text; partial ratification is normal per the severable-package convention. Enactment, in whole or in part, awaits the human governing authority's word; his slower look is owed on this redraft.**

Drafted: 2026-11-08 UTC, session MAINT-83. Commissioned by the human governing authority's 2026-11-08 MAINT-81 ruling set (ruling 6, recorded in the MAINT-81 Routing header: "Rules 8+10 F1–F8 redraft commissioned to the drafting line with F1 (define or drop FAIL), F2 (count carrying NOTEs), F3 (a Closed-by-ruling exit) and F5 (an independent oracle for the reconcile check) first, his slower look owed"). Drafted under the co-author mandate (granted 2026-11-04); Architect line primary, Repo Custodian secondary. Operating per Auditor_Protocols.md v0.47.

## §0 — Chain, verification anchors, non-independence

**Chain.** The enacted Rules 8 and 10 (Addendum #3, MAINT-59, in `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`; quoted verbatim in §1 below) were composed by this Vibe line. The MAINT-60 Claude skeptic review (Class A intake 9) recorded suggested fixes; MAINT-65 drafted them as the 2026-11-05 proposal (§1–§3). Claude's 1.34 review Part B raised findings F1–F8 against that draft (Class A intake 12, MAINT-66); the responses R1–R7 revised the affected texts. This redraft merges the two documents so one read suffices for ruling.

**Verification anchors (MAINT-66, live then):** F1 verified on the proposal's and the ledger's own text — the coverage ledger names FAIL and defines nothing; no FAIL severity exists anywhere in 1.34; INCOMPLETE is a checklist value, not a severity. F2 spot-verified: 0 Watch-carried dispositions in the sampled aggregates (the reviewer's heuristic count of 35 carrying-NOTE rows across 22 aggregates is recorded as the reviewer's count, not adjudicated). F3 verified: `Closed-by-ruling` exists as a disposition — 11 mentions across the sample — but was not a clearing path in the proposal. F4–F8 accepted on the proposal's own text.

**Non-independence, disclosed plainly:** one line composed the enacted rules, the 2026-11-05 proposal, the responses, and this redraft (Genesis Phase; Q-2 invoked). The defects were caught externally (Claude, human-routed, intakes 9 and 12); the consolidation is not independent. The recommendations widen the gate on this seat's own prior work rather than close it — a reason for care, not silence.

**Scope guards, unchanged:** Rules 9 (PATTERN crosswalk) and 11 (Rule 5 hand-off mechanics) remain HELD until after the first Rule 5 verification cycle; the original `PROPOSAL_2026-11-03_AGGREGATE_METHOD_UPGRADE` stays OPEN and untouched in both repos; no aggregate is edited by this redraft; nothing advances any Status, Last Audit, or Spec Gate (PKC-020).

## §1 — The enacted text being amended (verbatim, for the read)

From Addendum #3 (2026-11-04, MAINT-59) in `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`:

> **Rule 8 — NOTE semantics (constrains Rule 7's application).** NOTE-grade findings are records, not defects. Valid NOTE dispositions are exactly: `Positive-record` | `Watch-carried` (replaces "Standing-open" for NOTEs; existing NOTE "Standing-open" rows are re-labelled `Watch-carried` at the aggregate's next substantive touch via dated addendum, never in place) | `Corrected-by-later-fact` | `Superseded by <Ref>`. NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on MAJOR/WARNING/F-grade findings only. Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.
>
> **Rule 10 — coverage ledger.** New bookkeeping instrument `Archive/Audits/AUDIT_COVERAGE_LEDGER.md`: one row per doctrine target — target | era-tags of passes held | aggregate ref (or "—") | open MAJOR/WARNING/F count at last count | Rule 7 trigger state (computable / blocked by <refs>) | last-counted date and counter. The Custodian updates it at every audit landing and fold-in; it advances no field anywhere (bookkeeping-map class, PKC-020). One instrument serves both the aggregation trigger and the Red-Team review's coverage recommendation.

The amendments below replace the gate sentence of Rule 8, add two paragraphs to Rule 8, add one column to Rule 10, and restructure Rule 10 into two tables. Rules 7 and 3 are untouched.

## §2 — Fix A: the gate's vocabulary completed — FAIL defined, not dropped (F1, F8; consolidates proposal §1 + R1)

**The defect.** The enacted gate sentence reads "MAJOR/WARNING/F-grade findings only." "F-grade" is undefined in the rule text — F1, F2 … are finding IDs, not grades — and the only in-repo use of the term FAIL (the ledger's "open MAJOR/WARNING/F count") defines nothing (MAINT-66, verified). CRITICAL also sits outside the gate. F8: the corpus carries three vocabularies around "CRITICAL" (finding severity, Risk field, File State Priority field); the gate must name its field explicitly.

**The choice the commission allows (F1: define or drop).** This redraft DEFINES. Dropping FAIL from the gate would strand the enacted Rule 10 column ("open MAJOR/WARNING/F count") — the ledger already carries the term, so the gate and the column must share one vocabulary; defining costs nothing (no FAIL severity has been emitted in the corpus to date, verified MAINT-66; if none is ever emitted, the definition is dormant, and a dormant definition is cheaper than an undefined term in a gate).

**Proposed Rule 8 gate text (replaces the enacted gate sentence; deltas marked):**

> NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on **finding severities MAJOR, WARNING, CRITICAL and FAIL** only. **Finding severity** is a distinct field from Risk and Priority; a CRITICAL value in a Risk or Priority field does not trip this gate. **Severity FAIL** = a required check that was executed and produced a failing result — distinct from INCOMPLETE, a checklist value meaning the check was not run. No FAIL severity has been emitted in the corpus to date; the term is defined so the gate and the ledger's Open M/W/F count share one vocabulary. **CRITICAL is added to the gate** — a CRITICAL-severity finding always blocks the Rule 7 trigger (today none exists: CRITICAL appears in the corpus only in "0 CRITICAL" summary totals and File State Priority fields). Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.

**Pre-drafted ruling text:** *"RATIFY: Rule 8 amended so the trigger gates on finding severities MAJOR/WARNING/CRITICAL/FAIL; finding severity distinguished from Risk/Priority fields; FAIL defined (executed-to-a-failing-result, distinct from INCOMPLETE). No retroactive aggregate edits."*

## §3 — Fix B: Open W-C counts carrying NOTEs (F2; consolidates proposal §2 + R2)

**The defect.** The proposed Open W-C column as drafted read zero at birth while carrying NOTEs exist — invisible accumulation with a number that misstates. F2's corrected definition governs.

**Proposed Rule 10 column text (added to the column set):**

> **Open W-C** = count of NOTE-severity rows in the target's aggregate whose disposition is a carrying state — `Watch-carried`, or `Standing-open` pending the Rule 8 re-label. The column counts carrying NOTEs regardless of when the re-label lands, so it is non-zero at creation wherever carrying NOTEs exist (the reviewer's heuristic count: 35 rows across 22 aggregates; not adjudicated, recorded as the reviewer's count). Recorded for visibility only: Watch-carried never gates the Rule 7 trigger (NOTE semantics unchanged), but accumulation is now visible in the register instead of invisible.

**Pre-drafted ruling text:** *"RATIFY: Open W-C counts NOTE-severity rows in carrying dispositions (Watch-carried or Standing-open pre-re-label); visibility-only, never gates the trigger."*

## §4 — Fix C: clearing paths completed + the under-grading guard (F3, F4; consolidates proposal §2 + R3 + R4)

**The defect.** Watch-carried had no clearing condition (F3: a restatement loop with no ruling exit; `Closed-by-ruling` already exists as a disposition — 11 mentions — but was not a clearing path), and a NOTE grade could be challenged with no named ratifier (F4).

**Proposed Rule 8 appended paragraphs:**

> A `Watch-carried` row clears exactly by one of: **(a)** a later pass re-tests or restates the point — the later pass's grade governs from that pass, recorded in a dated addendum; a restatement that does not resolve the point **updates the original row** (the carry continues; no duplicate row is created — Rule 3 nothing-dropped governs, and the ledger counts rows, not restatements); **(b)** a dated `Corrected-by-later-fact` or `Superseded by <Ref>` disposition; or **(c)** a dated `Closed-by-ruling` disposition — the terminal state for a NOTE the human governing authority accepts or retires by ruling. It never clears by silence or the passage of time.
>
> **Under-grading guard:** a NOTE grade may be challenged in any later review. During the Genesis Phase, a re-grade (NOTE → a defect grade) is ratified by the **human governing authority** on challenge, landing via dated addendum citing the challenging evidence; the seat that assigned or carried the grade never adjudicates its own grading. Once the Rule 5 verifier is named, that seat adjudicates challenges, with the human as appeal. From re-grade, the finding is defect-graded and re-enters the Rule 7 trigger under §2's gate.

**Pre-drafted ruling texts:** *"RATIFY: Watch-carried clears by (a) later-pass governing grade with restatement updating the original row, (b) dated Corrected-by-later-fact/Superseded, or (c) dated Closed-by-ruling; never by silence."* / *"RATIFY: re-grades ratified by the human governing authority during Genesis Phase; the Rule 5 verifier adjudicates once named, human appeal; re-graded findings re-enter the trigger."*

## §5 — Fix D: ledger restructure with an independent-oracle reconcile (F5, F7; consolidates proposal §3 + R5 + R7)

**The defect.** The ledger drifts by design (one seat generates and tallies; MAINT-59 records 9 of 28 counts hand-counted), its row-count verification is circular, and the reconcile check as drafted compared two copies of one parse (F5).

**Proposed Rule 10 restructure (one instrument, two tables — no second meta-artifact):**

> **§5a — Table I (pass-coverage map, slow):** target | era-tags of passes held | aggregate ref (or "—"). Changes only when a pass is registered or an aggregate is composed.
> **§5b — Table II (open-counts register, fast):** target | open MAJOR/WARNING/CRITICAL/FAIL | open W-C (§3) | Rule 7 trigger state | last-counted date and counter. Regenerated on every landing that changes a disposition, opens, or closes a carrying row.
> **Scripted regeneration:** `Automation/coverage_ledger_regen.py` (staged build; precedent `Automation/integrity_check.py` v0.3) parses each aggregate's §2 findings ledger and regenerates Table II mechanically.
> **§5c — Post-landing reconcile check, with an independent oracle (both legs required at build and run):** recorded Table II must equal the script's regenerated output after every disposition-changing landing; a mismatch is a stale-index defect finding — logged and repaired in a dated pass, never silently. Oracle leg (i): frozen hand-counted test fixtures — three to five aggregates with expected counts recorded at build time, run as the script's unit tests on every execution. Oracle leg (ii): a periodic sample recount by a line other than the script's author — during the Genesis Phase, a human-routed external review (as MAINT-66) serves as the sample counter, recorded in the reconcile report.
> **§5d — "Next substantive touch" defined:** any aggregate edit that changes a §2 ledger row is a substantive touch; Rule 8's Watch-carried re-labels land there. Pure §5 addenda are touches; nothing else is.
> **§5e — Rule 5 verifier scope extension (severable from §5a–d; pre-authorizes packet contents only):** when the verifier is named, the packet includes the coverage ledger and the regen script's output, closing the "nothing independent touches the ledger" gap.

**Pre-drafted ruling texts:** *"RATIFY: coverage ledger split into Table I (pass-coverage map) and Table II (open-counts register) within the same instrument; scripted regeneration via Automation/coverage_ledger_regen.py; post-landing reconcile check with mismatches logged as stale-index defects; 'next substantive touch' defined as any §2-row-changing edit. Staged execution with verification report owed."* / *"RATIFY: reconcile check with (i) frozen hand-counted fixtures as unit tests and (ii) periodic external sample recount recorded in the reconcile report."* / *"RATIFY: the Rule 5 verifier scope extension severed as §5e, severable from §5a–d."*

## §6 — Explicit holds recorded (F6; from R6)

MAINT-60 finding 3 (no Rule 4 evidence type for `Watch-carried`) is HELD with Rule 11 until after the first Rule 5 verification cycle — the evidence type lands with the label mechanics it tests. MAINT-60 finding 8 (how trigger state is computed for the ~65 unaggregated targets) is partially answered by the ledger's recorded per-row position ("single pass — aggregate not owed"; "no aggregate — deferred"); the derived definition of "computable" is HELD pending the regeneration script and the named verifier. The proposal's §4 pointers remain his input: §4 final classification (AVE-R2 vs R3), §9 ISP runtime-source provenance evidence, §10 P-3 read + model-family names, §6 pending EthCon A-F3, IIL B-N3 at the next incident landing. Per the ratified §0 convention these are pointers, never open/close statements.

**Pre-drafted ruling text:** *"RATIFY: findings 3 and 8 recorded as explicit holds — 3 with Rule 11, 8's 'computable' definition pending the script and verifier."*

## §7 — What this redraft does NOT do

No rule is enacted by drafting. No aggregate is edited. The ledger is not split. No script is built. The 2026-11-05 proposal and response addendum are preserved unchanged (this redraft supersedes them for review, not for history). The original AGGREGATE_METHOD_UPGRADE proposal file stays OPEN, untouched, in both repos. Rules 9 and 11 stay held. Tier 1 / FROZEN / Hard Floor untouched; no Unknown opened or closed; no `Verified-by` cell filled; advances no field anywhere (PKC-020).

## §8 — Execution plan if ratified (staged)

1. Addendum #4 to `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md` recording the ratified amendment text verbatim (§2, §3, §4, §5a–e as ratified — severable).
2. Compose the owed `Admin/Operational_Conventions.md` aggregate (ledger row 24, deferral cleared at MAINT-63).
3. Ledger migration to Table I / Table II with row-by-row verification against the current 93 rows; Open W-C backfilled in the same pass, counting carrying NOTEs per §3.
4. `Automation/coverage_ledger_regen.py` build with the frozen fixtures (§5c leg i); first full regeneration + reconcile report deposited (expected: all mismatches = none, or logged as findings).
5. Routing + entries registration of each landing; disclosure of every defect the reconcile check catches.

---

*Drafted 2026-11-08 — MAINT-83 (Vibe — co-author mandate; Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed). One line composed the enacted Rules 8+10 (MAINT-59), the 2026-11-05 proposal (MAINT-65), the responses (MAINT-66) and this redraft; the defects were caught externally (Claude, human-routed, intakes 9 and 12); the commission is the human's (MAINT-81 ruling set, ruling 6). Operating per Auditor_Protocols.md v0.47.*
