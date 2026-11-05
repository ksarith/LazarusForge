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
