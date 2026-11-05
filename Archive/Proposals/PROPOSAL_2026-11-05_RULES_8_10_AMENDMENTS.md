# PROPOSAL — Rules 8+10 Amendments (AGGREGATE_METHOD_UPGRADE follow-up) — MAINT-65

**Status: PROPOSED — nothing below is in force. Every section is severable and carries pre-drafted ruling text; partial ratification is normal per the severable-package convention. Enactment, in whole or in part, awaits the human governing authority's word.**

Drafted: 2026-11-05 UTC, session MAINT-65. Drafted under the co-author mandate (granted 2026-11-04, invoked by the human's direct word 2026-11-05); Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, disclosed. Operating per Auditor_Protocols.md v0.47.

## §0 — Origin and scope

The three amendments below are the **Rules 8+10 amendment drafts**, ruled next in the queue by the human governing authority at MAINT-61 ("standing-debt sweep first, then the Rules 8+10 amendment drafts") and next again after MAINT-63's execution. All three originate in the **MAINT-60 Claude skeptic review** (Class A intake, entry 9 in `Admin/ALogs/External_Intake_Protocol_Logs.md`; deposit `Archive/Audits/EXTERNAL_REVIEW_2026-11-05_CLAUDE_RULES8_10_SKEPTIC.md`, verbatim), where they were recorded as suggested fixes and **HELD for human ruling — none enacted**. This proposal drafts them as ratifiable rule text.

Provenance pattern, disclosed plainly: the enacted Rules 8 and 10 (Addendum #3, MAINT-59) were composed by this same Vibe line. The amendments fix defects that an external review caught in that work. The fixes are externally sourced (Claude's review, human-relayed); their composition into rule text is not independent (same line, same session lineage, Q-2 invoked). The MAINT-62 pattern finding applies with the sign reversed: these recommendations *widen* the gate on this seat's own prior work rather than close it, which is a reason for care but not a reason for silence — the defects are real and verified (MAINT-60 claim verification, and the ledger's own maintenance rule).

Scope guards: Rules 9 (PATTERN crosswalk) and 11 (Rule 5 hand-off mechanics) remain HELD until after the first Rule 5 verification cycle (Addendum #3) and are untouched here. The original `PROPOSAL_2026-11-03_AGGREGATE_METHOD_UPGRADE` stays OPEN and untouched in both repos. No aggregate is edited by this proposal. Nothing here advances any Status, Last Audit, or Spec Gate (PKC-020).

## §1 — Fix A: CRITICAL into the trigger gate; "F-grade" defined

**Defect (skeptic finding 1, verified MAINT-60).** The Rule 7/8 trigger gates on "MAJOR/WARNING/F-grade findings only." The corpus grade vocabulary is MAJOR | WARNING | NOTE | CRITICAL, with FAIL defined as a severity by the coverage-ledger counting convention. Two gaps: (a) a CRITICAL-grade finding would sit outside the gate and block nothing; (b) "F-grade" is undefined in the rule text — F1, F2 … are finding IDs, not grades. Verified at MAINT-60: no CRITICAL-grade finding exists today (CRITICAL appears only in "0 CRITICAL" summary totals; the 14 `| CRITICAL |` cells in the corpus are File State Priority fields, not finding severities). The amendment is vocabulary-completeness, not a response to a live defect; it costs nothing now and closes a real gap if a CRITICAL finding is ever raised.

**Proposed rule text (amends Rule 8, final sentence; deltas marked):**

> NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on **MAJOR, WARNING, CRITICAL and FAIL** findings only (**"F-grade" in the prior text = severity FAIL, as defined by the coverage-ledger counting convention; CRITICAL is added to the gate — a CRITICAL-grade finding always blocks the Rule 7 trigger**). Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.

**Effects if ratified:** rule text only. No aggregate carries a CRITICAL or FAIL finding that would newly block (verified against the 28 aggregates at MAINT-59/MAINT-63 counts), so no aggregate or ledger row changes on ratification; the ledger counting convention already counts FAIL severities, so Open M/W/F totals are unaffected.

**Pre-drafted ruling text:** *"RATIFY: Rule 8 amended so the Rule 7 trigger gates on MAJOR/WARNING/CRITICAL/FAIL; 'F-grade' defined as severity FAIL per the coverage-ledger counting convention. No retroactive aggregate edits."*

## §2 — Fix B: Watch-carried clearing condition + ledger count column

**Defect (skeptic findings 2 and 4, partially answered at MAINT-60).** Watch-carried repeats the gap it replaced ("Standing-open" had no clearing condition; so does Watch-carried). NOTEs are excluded from the trigger and from ledger counts, so accumulated Watch-carried items are invisible. And the grade is the only thing separating a record from a defect: an auditor who under-grades a real defect as a NOTE lets it clear the trigger permanently (skeptic finding 4 — under-grading risk; Governance_Charter B-N2/B-N3 were treated as live by their own writer, so the concern is not hypothetical).

**Proposed rule text (amends Rule 8, appended paragraph):**

> A `Watch-carried` row clears exactly by one of: **(a)** a later pass re-tests or restates the point — the later pass's grade governs from that pass, recorded in a dated addendum; if the later pass drops the point, the Rule 3 *Not re-tested* carry applies with the governing grade; or **(b)** a dated `Corrected-by-later-fact` or `Superseded by <Ref>` disposition. It never clears by silence or the passage of time.
>
> **Under-grading guard:** a NOTE grade may be challenged in any later review. A re-grade (NOTE → a defect grade) lands only via dated addendum citing the challenging evidence; from that moment the finding is defect-graded and re-enters the Rule 7 trigger under §1's gate.

**Proposed ledger amendment (amends Rule 10, column set):** the coverage ledger gains one column, **Open W-C** = count of Watch-carried NOTE rows in the target's aggregate at last count. It is recorded for visibility only: Watch-carried never gates the Rule 7 trigger (NOTE semantics unchanged), but accumulation is now visible in the register instead of invisible.

**Effects if ratified:** Rule 8 paragraph + Rule 10 column added at the next ledger touch; Watch-carried counts backfilled in the same pass that splits the ledger (§3), not in place before it. No existing disposition is re-judged; no history rewritten.

**Pre-drafted ruling text:** *"RATIFY: Watch-carried clearing condition defined as (a) later-pass governing grade or (b) dated Corrected-by-later-fact/Superseded disposition — never by silence; under-grading re-grade path defined (dated addendum, cites evidence, re-enters the trigger); coverage ledger gains a visibility-only Open W-C column."*

## §3 — Fix C: ledger split + scripted count regeneration + post-landing reconcile check

**Defect (skeptic findings 6, 7, 9, 10).** The ledger drifts by design: its own mitigation is Custodian discipline, and the Custodian also writes the dispositions the counts come from (one seat generates and tallies; MAINT-59 records 9 of 28 counts as hand-counted). Its row-count verification is circular (rows come from the same Routing registry). One table mixes slow data (pass coverage) with fast data (open counts, which change with every fix). And nothing independent touches the ledger: Rule 5 covers the aggregates, not the register, until a verifier is named.

**Proposed amendment (Rule 10, restructured; one instrument, two tables — no second meta-artifact):**

> **Table I — pass-coverage map (slow):** target | era-tags of passes held | aggregate ref (or "—"). Changes only when a pass is registered or an aggregate is composed.
> **Table II — open-counts register (fast):** target | open MAJOR/WARNING/CRITICAL/FAIL | open W-C (§2) | Rule 7 trigger state | last-counted date and counter. Regenerated on every landing that changes a disposition, opens, or closes a carrying row.
>
> **Scripted regeneration:** `Automation/coverage_ledger_regen.py` (staged build; precedent `Automation/integrity_check.py` v0.3) parses each aggregate's §2 findings ledger and regenerates Table II mechanically.
> **Post-landing reconcile check:** after every disposition-changing landing, recorded Table II must equal the script's regenerated output; a mismatch is a stale-index defect finding — logged and repaired in a dated pass, never silently. The check is mechanical, but the build and first runs are by the Custodian line (non-independent, disclosed) until the Rule 5 verifier is named.
> **"Next substantive touch" defined (settles skeptic finding 5):** any aggregate edit that changes a §2 ledger row is a substantive touch; Rule 8's Watch-carried re-labels land there. Pure §5 addenda are touches; nothing else is.
> **Rule 5 verifier scope extension (when named):** the verifier's packet includes the coverage ledger and the regen script's output, closing the "nothing independent touches the ledger" gap (the MAINT-60 proposed extension, restated here so it ratifies with this section or not at all).

**Effects if ratified:** staged execution — the register file is migrated to two tables with row-by-row verification against the current 93 rows; the script is built and its first full regeneration + reconcile report is deposited; hand-counted history is preserved in Last-counted annotations (never rewritten). Ledger row 24's owed OC aggregate composes before or with this migration (no row is left uncountable).

**Pre-drafted ruling text:** *"RATIFY: coverage ledger split into Table I (pass-coverage map) and Table II (open-counts register) within the same instrument; scripted regeneration via Automation/coverage_ledger_regen.py; post-landing reconcile check with mismatches logged as stale-index defects; 'next substantive touch' defined as any §2-row-changing edit; Rule 5 verifier scope extended to the ledger when named. Staged execution with verification report owed."*

## §4 — Held items not addressed here (pointers only, his read owed)

Not part of this proposal; recorded so the queue reads in one place. Awaiting the human governing authority's direct input: §4 final classification (AVE-R2 vs R3 — Claude's MAINT-63 relay favors R3, reversing the Grok/ChatGPT lean; both file-internal meanwhile); §9 ISP runtime-source provenance evidence (evidence bar: execution logs / source hash / code inspection / change-reproduces test); §10 P-3 read + model-family names; §6 pending EthCon A-F3; IIL B-N3 annotation at the next incident landing. Per the ratified §0 convention these are pointers, never open/close statements.

## §5 — What this proposal does NOT do

No rule is enacted by drafting. No aggregate is edited. The ledger is not split yet. No script is built yet. The original AGGREGATE_METHOD_UPGRADE proposal file stays OPEN, untouched, in both repos. Rules 9 and 11 stay held. Tier 1 / FROZEN / Hard Floor untouched; no Unknown opened or closed; no `Verified-by` cell filled; advances no field anywhere (PKC-020).

## §6 — Execution plan if ratified (staged)

1. Addendum #4 to `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md` recording the ratified amendment text verbatim (§1, §2, §3 as ratified — severable).
2. Compose the owed `Admin/Operational_Conventions.md` aggregate (ledger row 24, deferral cleared at MAINT-63).
3. Ledger migration to Table I / Table II with row-by-row verification against the current 93 rows; Open W-C backfilled in the same pass.
4. `Automation/coverage_ledger_regen.py` build; first full regeneration + reconcile report deposited (expected: all mismatches = none, or logged as findings).
5. Routing + MAINT_LOG registration of each landing; disclosure of every defect the reconcile check catches.

---

*Drafted 2026-11-05 — MAINT-65 (Vibe — co-author mandate, invoked 2026-11-05; Architect line primary, Repo Custodian secondary; non-independent Genesis Phase, disclosed). The three fixes originate in the MAINT-60 Claude skeptic review (human-relayed, Class A); their composition into rule text is by the same line whose enacted work they amend — Q-2 invoked. Operating per Auditor_Protocols.md v0.47.*
