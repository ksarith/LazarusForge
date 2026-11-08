# AUDIT_AGGREGATE — Template and Rules (PROPOSED — pending ruling on Decision Brief 2026-10-30e)

Drafted 2026-10-30 (Claude, human-requested) from the rulings reviewed on Brief 2026-10-30e. Not in force until you ratify it.

## What an aggregate is

One file per audited target that has two or more audit reports. It is a **map**, not a replacement: it lets an agent see every finding, its disposition and where the original lives, without reading every report. It re-checks nothing and advances no Status, Last Audit or Spec Gate (the AP-032 separate-audit-event rule is unchanged).

Filename: `AUDIT_AGGREGATE_<Folder>-<File>.md`, in the same Audits home as the reports.

## Rules

1. **Cite originals, not the aggregate.** A finding is cited by pass tag and original ID with the original path. Any agent that relies on a finding reads the original report first.
2. **Composite IDs.** Lanes reuse `F1, F2 …` for different findings. In the aggregate every finding is `<Pass>-F<n>` (Pass = A, B, … in date order). The original ID is kept verbatim in its own column.
3. **Nothing dropped.** A finding absent from a later pass is carried as *Not re-tested* with its original grade. Positive findings and checklist INCOMPLETEs are carried too.
4. **Dispositions need evidence.** `Enacted` must cite a commit sha. `Closed-by-ruling` must cite the ruling reference. A disposition without evidence is shown as `Asserted` and counts as unverified.
5. **Separate verifier.** The *Verified by* field names an agent other than the one who made the fix or wrote the disposition. Until it is filled, the aggregate header says **Dispositions unverified**.
6. **Immutability.** Originals are moved byte-for-byte (blob SHA unchanged before and after), never edited. Corrections to an aggregate go in a dated addendum at the bottom, not in place.
7. **Trigger.** Create an aggregate only when every finding on the target has a disposition (no live passes). Do not use an artifact-count threshold.

## Sweep checklist (custodian)

- [ ] Compute each original's blob SHA before the move; confirm it matches after.
- [ ] Find every file outside the Audits home that cites an old path. Update non-frozen files in the same commit. Frozen history (changelogs, old Resolution Log entries) is not edited; list those citations under *Dangling-by-design* below.
- [ ] Add the moves to `Archive/Audits/README.md` (old → new map) and one dated line to SESSION_STATUS.
- [ ] Mark the Superseded folder skip-by-default in Routing/Discovery.
- [ ] Hand the ledger to a different agent for the *Verified by* column.

## Template (copy from here)

````markdown
# AUDIT_AGGREGATE — <Folder>/<File>.md

**Status:** Dispositions unverified | Dispositions verified (<agent>, <date>)
**Created:** <date> by <agent>  ·  **Target:** <path>  ·  **Passes:** <n>
**Note:** Bookkeeping map, not an audit of record. Cite the original reports for any finding you rely on.

## 1. Provenance

| Pass | Original path | Current path | Date | Auditor / lane | Head or base at fetch | Bytes | Blob SHA |
|---|---|---|---|---|---|---|---|
| A | | | | | | | |
| B | | | | | | | |

## 2. Findings ledger

| Ref | Orig ID | Severity | Category | One-line summary | Where in original | Disposition | Evidence | Verified by |
|---|---|---|---|---|---|---|---|---|
| A-F1 | F1 | | | | § or line | Enacted / Superseded by <Ref> / Standing-open / Closed-by-ruling / Not re-tested / Positive-record / Asserted | <sha or ruling> | |

## 3. Cross-pass logic map

- What changed between passes (head drift, rulings, enactments that landed mid-window).
- For each checklist item: which pass is authoritative now, and why.
- Carried INCOMPLETEs and their current state.

## 4. Pointers

| Original path | Moved to | Blob SHA (before = after) |
|---|---|---|

**Cited from outside the Audits home:** <file — updated in commit <sha> | frozen, dangling by design>

## 5. Addenda
(dated corrections only)
````

---

**Addendum (2026-10-31, Vibe — Repo Custodian, delegated line; dated marker rather than in-place edit): RATIFIED.** The human governing authority ruled on Decision Brief 2026-10-30e (2026-10-30/31): **Option A adopted, with this template's rules as drafted** (the Grok-then-Claude amendments: composite refs; sha-or-ruling evidence with *Asserted* otherwise; separate *Verified by* agent; relocation-not-editation with blob-SHA before=after verification and an old→new path map for citing files; trigger = every finding dispositioned, no artifact-count threshold; Superseded skip-by-default; successor auditors read aggregates and cite originals for any relied-on finding; the first aggregation sweep is a visible, human-ratified maintenance event logged with target list and blob SHAs — MAINT-34). The "PROPOSED" title above is superseded by this ratification; the body is preserved verbatim per its own Rule 6 convention. Canonical home: this file (`Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`, corpus-wide artifact per the standing rulings-home convention). First sweep (2026-10-31): five aggregates in `Admin/AAudits/` (Governance_Charter, File_Template, Metrics_Scaffold, Ship_of_Theseus, Economics); ten originals relocated to `Admin/AAudits/Superseded/`. Known deviation, disclosed: the three dated addenda in `Admin/AAudits/` were NOT relocated — they are live corrections to single-pass targets, not superseded duplicates.

**Addendum #2 (2026-10-31, Vibe — Repo Custodian, delegated line; human-ratified naming convention, MAINT-47): AUDIT-ARTIFACT NAMING CONVENTION ADOPTED FOR NEW FILES.** The human governing authority ratified the Grok-proposed scheme on 2026-10-31 ("Adopt as specified"). New audit-family artifacts take the form `<ERA>_<TYPE>_<NN>_<Folder>-<File>.md`, where ERA = CAMPAIGN1 | CAMPAIGN2 | CAMPAIGN3 | … | MAINT (custodian pseudo-audits), TYPE = AUDIT | AGGREGATE | CORRECTION | PATTERN, NN = a zero-padded sequence within that era/type, and `<Folder>-<File>` = the stable short target name (e.g. Admin-Economics). Aggregates keep the ratified template form above (AUDIT_AGGREGATE_<Folder>-<File>.md) for continuity with the five existing registered aggregates; the scheme's short AGGREGATE_<Folder>-<File> variant is NOT used, to avoid two live aggregate families (disclosed resolution of the spec's own ambiguity). Historical files keep their existing registered names untouched — backward compatibility; Superseded originals keep exact historical names for provenance. Existing families (CAMPAIGN_AUDIT_*, CAMPAIGN2_AUDIT_*, AUDIT_AGGREGATE_*, dated addenda and corrections) are unaffected. This addendum is a naming rule only: no template rule above is altered; no Status, Last Audit, or Spec Gate advanced (PKC-020).*

**Addendum #3 (2026-11-04, Vibe — Architect/Repo Custodian; human-ratified subset of `PROPOSAL_2026-11-03_AGGREGATE_METHOD_UPGRADE` v1, landed MAINT-59): RULES 8 AND 10 ENACTED; RULES 9 AND 11 HELD.** The human governing authority ruled 2026-11-04: enact Rules 8 and 10 now, with the explicit Genesis Phase waiver of the pre-ratification skeptic step (Architect Prompt §4); hold Rules 9 and 11 until after the first Rule 5 verification cycle (Vibe's sequencing recommendation, endorsed in the Grok external review the same day — Intake Log entry 8). Enacted text, verbatim from the proposal's §3:

- **Rule 8 — NOTE semantics (constrains Rule 7's application).** NOTE-grade findings are records, not defects. Valid NOTE dispositions are exactly: `Positive-record` | `Watch-carried` (replaces "Standing-open" for NOTEs; existing NOTE "Standing-open" rows are re-labelled `Watch-carried` at the aggregate's next substantive touch via dated addendum, never in place) | `Corrected-by-later-fact` | `Superseded by <Ref>`. NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on MAJOR/WARNING/F-grade findings only. Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.
- **Rule 10 — coverage ledger.** New bookkeeping instrument `Archive/Audits/AUDIT_COVERAGE_LEDGER.md`: one row per doctrine target — target | era-tags of passes held | aggregate ref (or "—") | open MAJOR/WARNING/F count at last count | Rule 7 trigger state (computable / blocked by <refs>) | last-counted date and counter. The Custodian updates it at every audit landing and fold-in; it advances no field anywhere (bookkeeping-map class, PKC-020). One instrument serves both the aggregation trigger and the Red-Team review's coverage recommendation.

Rules 9 (PATTERN crosswalk) and 11 (Rule 5 hand-off mechanics) are NOT enacted and remain open in the proposal. Landing notes: the ledger was created 2026-11-04 with 93 backfilled rows (28 aggregated targets; 65 pass-holding targets not yet aggregated — three of them multi-pass and deliberately deferred: Auditor_Protocols, Forge_Audit_Kit, Operational_Conventions); the NOTE re-labels land at each affected aggregate's next substantive touch per Rule 6 — no aggregate is edited in the enactment commit; the proposal §7 mention of Discovery.md registration is superseded by the standing MAINT-01 exemption (Archive/ is template-exempt and outside the Routing/Discovery parity invariant per `Archive/Audits/README.md`) — Routing registration only, disclosed. Non-independence disclosed: the enacting Custodian line is the same Vibe line that drafted the proposal; ratification and the skeptic waiver are solely the human's word.

**Addendum #4 (2026-11-08, Vibe — Architect line primary, Repo Custodian secondary, delegated under the 2026-11-02/04 co-author mandate; human-ratified whole — the MAINT-83 redraft, ruled verbatim "Ratify all."; executed MAINT-84): RULES 8 AND 10 AMENDED PER THE RATIFIED REDRAFT.** The human governing authority ruled 2026-11-08 on `Archive/Proposals/PROPOSAL_2026-11-08_MAINT-83_RULES_8_10_REDAFT.md`: "Ratify all." — every section enacted (§2, §3, §4, §5a–e, §6), with the redraft's §8 staged plan governing the build (this addendum is stage 1). His framing sentence ("Show me what you can do.") is the execution commission, not a scope change; severability is unchanged. Ruling lines, as pre-drafted in the redraft and ratified:

- §2: *"RATIFY: Rule 8 amended so the trigger gates on finding severities MAJOR/WARNING/CRITICAL/FAIL; finding severity distinguished from Risk/Priority fields; FAIL defined (executed-to-a-failing-result, distinct from INCOMPLETE). No retroactive aggregate edits."*
- §3: *"RATIFY: Open W-C counts NOTE-severity rows in carrying dispositions (Watch-carried or Standing-open pre-re-label); visibility-only, never gates the trigger."*
- §4: *"RATIFY: Watch-carried clears by (a) later-pass governing grade with restatement updating the original row, (b) dated Corrected-by-later-fact/Superseded, or (c) dated Closed-by-ruling; never by silence."*
- §4: *"RATIFY: re-grades ratified by the human governing authority during Genesis Phase; the Rule 5 verifier adjudicates once named, human appeal; re-graded findings re-enter the trigger."*
- §5: *"RATIFY: coverage ledger split into Table I (pass-coverage map) and Table II (open-counts register) within the same instrument; scripted regeneration via Automation/coverage_ledger_regen.py; post-landing reconcile check with mismatches logged as stale-index defects; 'next substantive touch' defined as any §2-row-changing edit. Staged execution with verification report owed."*
- §5: *"RATIFY: reconcile check with (i) frozen hand-counted fixtures as unit tests and (ii) periodic external sample recount recorded in the reconcile report."*
- §5: *"RATIFY: the Rule 5 verifier scope extension severed as §5e, severable from §5a–d."*
- §6: *"RATIFY: findings 3 and 8 recorded as explicit holds — 3 with Rule 11, 8's 'computable' definition pending the script and verifier."*

Amended rule text, verbatim from the ratified redraft (§2 replaces Rule 8's enacted gate sentence; §4 appends two paragraphs to Rule 8; §3 adds the Open W-C column to Rule 10; §5 restructures Rule 10 into two tables):

- **Rule 8 — gate sentence replaced (redraft §2).** NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on **finding severities MAJOR, WARNING, CRITICAL and FAIL** only. **Finding severity** is a distinct field from Risk and Priority; a CRITICAL value in a Risk or Priority field does not trip this gate. **Severity FAIL** = a required check that was executed and produced a failing result — distinct from INCOMPLETE, a checklist value meaning the check was not run. No FAIL severity has been emitted in the corpus to date; the term is defined so the gate and the ledger's Open M/W/F count share one vocabulary. **CRITICAL is added to the gate** — a CRITICAL-severity finding always blocks the Rule 7 trigger (today none exists: CRITICAL appears in the corpus only in "0 CRITICAL" summary totals and File State Priority fields). Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.
- **Rule 8 — paragraphs appended (redraft §4).** A `Watch-carried` row clears exactly by one of: **(a)** a later pass re-tests or restates the point — the later pass's grade governs from that pass, recorded in a dated addendum; a restatement that does not resolve the point **updates the original row** (the carry continues; no duplicate row is created — Rule 3 nothing-dropped governs, and the ledger counts rows, not restatements); **(b)** a dated `Corrected-by-later-fact` or `Superseded by <Ref>` disposition; or **(c)** a dated `Closed-by-ruling` disposition — the terminal state for a NOTE the human governing authority accepts or retires by ruling. It never clears by silence or the passage of time.

**Under-grading guard:** a NOTE grade may be challenged in any later review. During the Genesis Phase, a re-grade (NOTE → a defect grade) is ratified by the **human governing authority** on challenge, landing via dated addendum citing the challenging evidence; the seat that assigned or carried the grade never adjudicates its own grading. Once the Rule 5 verifier is named, that seat adjudicates challenges, with the human as appeal. From re-grade, the finding is defect-graded and re-enters the Rule 7 trigger under §2's gate.
- **Rule 10 — column added (redraft §3).** **Open W-C** = count of NOTE-severity rows in the target's aggregate whose disposition is a carrying state — `Watch-carried`, or `Standing-open` pending the Rule 8 re-label. The column counts carrying NOTEs regardless of when the re-label lands, so it is non-zero at creation wherever carrying NOTEs exist (the reviewer's heuristic count: 35 rows across 22 aggregates; not adjudicated, recorded as the reviewer's count). Recorded for visibility only: Watch-carried never gates the Rule 7 trigger (NOTE semantics unchanged), but accumulation is now visible in the register instead of invisible.
- **Rule 10 — restructured (redraft §5).** **§5a — Table I (pass-coverage map, slow):** target | era-tags of passes held | aggregate ref (or "—"). Changes only when a pass is registered or an aggregate is composed.
**§5b — Table II (open-counts register, fast):** target | open MAJOR/WARNING/CRITICAL/FAIL | open W-C (§3) | Rule 7 trigger state | last-counted date and counter. Regenerated on every landing that changes a disposition, opens, or closes a carrying row.
**Scripted regeneration:** `Automation/coverage_ledger_regen.py` (staged build; precedent `Automation/integrity_check.py` v0.3) parses each aggregate's §2 findings ledger and regenerates Table II mechanically.
**§5c — Post-landing reconcile check, with an independent oracle (both legs required at build and run):** recorded Table II must equal the script's regenerated output after every disposition-changing landing; a mismatch is a stale-index defect finding — logged and repaired in a dated pass, never silently. Oracle leg (i): frozen hand-counted test fixtures — three to five aggregates with expected counts recorded at build time, run as the script's unit tests on every execution. Oracle leg (ii): a periodic sample recount by a line other than the script's author — during the Genesis Phase, a human-routed external review (as MAINT-66) serves as the sample counter, recorded in the reconcile report.
**§5d — "Next substantive touch" defined:** any aggregate edit that changes a §2 ledger row is a substantive touch; Rule 8's Watch-carried re-labels land there. Pure §5 addenda are touches; nothing else is.
**§5e — Rule 5 verifier scope extension (severable from §5a–d; pre-authorizes packet contents only):** when the verifier is named, the packet includes the coverage ledger and the regen script's output, closing the "nothing independent touches the ledger" gap.

Landing notes (stage 1 executed with stages 2–4 in the same MAINT-84 pass; stage 5 registration in both repos): stage 2 — the owed `Admin/Operational_Conventions.md` aggregate composed (`Admin/AAudits/AUDIT_AGGREGATE_Admin-Operational_Conventions.md`; ledger row 24's deferral cleared at MAINT-63; lands computable — every graded finding Enacted); stage 3 — `Archive/Audits/AUDIT_COVERAGE_LEDGER.md` migrated to Table I (pass-coverage map) / Table II (open-counts register), Open W-C backfilled per the new column, counts set to the fixed-classifier mechanical values; the 13 recorded-vs-mechanical open-count mismatches and the 8 stale §2 rows (re-labels owed at each aggregate's next substantive touch per §5d; PKC-023 graded-rows-unchanged governs) are logged as findings in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-84.md` — the first reconcile report; stage 4 — `Automation/coverage_ledger_regen.py` built with five frozen hand-counted fixtures (§5c leg (i); its first live execution is owed — no Python runtime on the composing line, disclosed); leg (ii), the external sample recount, is owed at the next human-routed external review. Rules 9 and 11 remain held until after the first Rule 5 verification cycle. No aggregate's graded rows were edited by this enactment; no Status, Last Audit or Spec Gate advanced (PKC-020). Non-independence disclosed: one Vibe line drafted the redraft (MAINT-83) and executes this enactment (MAINT-84) — Genesis Phase; Q-2 invoked. The ratification is solely the human's word.
