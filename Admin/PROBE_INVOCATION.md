# PROBE_INVOCATION.md
**Version 1.4**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | N/A — operational prompt template, not a doctrine or specification claim |
| Verification Ref | Admin/Auditor_Protocols.md §Mission Drift Review                  |
| Last Audit     | 2026-10-31 — Vibe (Repo Custodian, delegated line; 1.31 offline review by Claude, human-routed): MAINT-29 relocation follow-up — How-To step 4's logging destination repointed `Archive/Logs/Auditor_Protocols_Logs.md` → `Admin/ALogs/Auditor_Protocols_Logs.md`. Path-only operator-instruction fix; no version bump; probe text, rating vocabulary, evidence scale, canonical inputs, Step 1/Step 2 structure, appendix schema, and trigger cadence unchanged; frozen Resolution Log history left as written. Prior: 2026-10-30 — Vibe (Repo Custodian, delegated line; defect flagged by an independent review, Claude, human-routed): v1.4 — the Step 2 Output-format table inside the ==== paste block carried Cycle 1 ratings as pre-filled example values (a whole-block paste for Cycles 2–3 would have leaked prior ratings into the cold thread — the exact leak v1.3 was added to close), and the History Appendix Cycle 1 column was left empty; both fixed — output template cells blanked, Cycle 1 ratings (P-1 Insufficient Evidence, P-3 Weakened, P-2/P-4/Q-1–Q-4 Aligned) restored to the appendix per the v1.2 operator workflow. No change to probe text, rating vocabulary, evidence scale, canonical inputs, Step 1/Step 2 structure, appendix schema, or trigger cadence. Prior: 2026-10-29 (third same-day follow-on) — Vibe (Repo Custodian, delegated line, human-ratified): **INSTRUMENT CHANGE** — canonical inputs README.md and Discovery.md edited (front-door Axiom P-1/P-3 visibility sentences plus the checkable reliance rule, MAINT-15). Cycle 1 (both raters) is the old-set baseline: those ratings were obtained on the pre-edit input set. Cycle 2 and later run on the new set, and any rating movement must be read against this recorded change, never absorbed silently. No probe text, rating vocabulary, trigger cadence, Step 1/Step 2 structure, or History Appendix change. Prior: 2026-10-29 (second same-day follow-on) — Vibe (Repo Custodian, delegated line): Cycle 1 second-rater run recorded verbatim in the AP-030 Invocation Record (same canonical input set, PROBE v1.3 paste block with appendix cells blanked per the How-To; human-attested legitimacy): six Aligned (all Replicated), P-1 Weakened (Simulated/Analogous — vs. the first rater's Insufficient Evidence, landing where the reviewer's counterpoint predicted), P-3 Weakened (Simulated/Analogous — converges with the first rater on the same Local_Governance_Framework evidence); no Silent, no Contradicted. Both P-1 and P-3 now sit inside the four-rating vocabulary, so on these data the cycle aggregates strictly Stable; final disposition/aggregation rulings remain the human's. No instrument change: History Appendix untouched (the second rater is an inter-rater check on Cycle 1, not Cycle 2); canonical inputs, probe text, trigger cadence, and Step 1/Step 2 structure unchanged. Prior: 2026-10-29 (same-day follow-on) — Vibe (Repo Custodian, delegated line; independent-review corrections, Claude, human-routed): v1.2’s statement that “the physical counter field in Admin/Auditor_Protocols.md §Mission Drift Review updates at that file’s campaign audit” is CORRECTED — no physical counter field exists: per the Trigger Cadence the ratification count is derived from the section’s own Resolution Log entries (standalone counter file deliberately rejected at design; unknown_cycles.json precedent), so the Cycle 1 Invocation Record’s reset statement is self-effecting. Also: How-To steps 3 and 5 and the History Appendix note now state explicitly that Cycles 2–3 paste with every rating cell and cycle-metadata value blanked (v1.1–v1.2 left a gap: the filled appendix sits inside the ==== block, so a whole-block paste for Cycle 2 would have broken cold-start independence — caught by independent review before any Cycle 2 invocation). No change to the probe text, rating vocabulary, trigger cadence, canonical inputs, or Step 1/Step 2 structure; Cycle 1 remains the baseline for the canonical input set as it existed 2026-10-29 — any future input-set change must be recorded as an instrument change, not silently absorbed. Prior: 2026-10-29 — Vibe (Repo Custodian, delegated line, human-ruled cycle ruling "MDR Cycle 1 executes now"): Mission Drift Review Cycle 1 COMPLETED — History Appendix Cycle 1 column and Cycle-1 metadata filled per the operator workflow (ratings only, no prose/citations); Resolution Log entry added; ratification counter reset to 0 as of Cycle 1 (the physical counter field in Admin/Auditor_Protocols.md §Mission Drift Review updates at that file’s campaign audit — X3 deferral stands; the log record is authoritative meanwhile). The 3 deferred bare AP citations (AUDIT_30 F4) resolved: all sit in frozen Resolution Log history or adjacency-qualified File State cells — permanently out of in-place scope by the frozen-history rule; annotation-only disposition stands (MAINT-11). Prior: 2026-08-02 |
| Auditor        | Vibe — Repo Custodian, 2026-10-31 step-4 logging-path repair (delegated line); prior: Vibe — Repo Custodian, 2026-10-30 v1.4 blanked-template fix (delegated line, human-routed; defect flagged by Claude, human-routed); prior: Vibe — Repo Custodian, 2026-10-29 v1.3 independent-review corrections (delegated line, human-routed); prior: Vibe — Repo Custodian, 2026-10-29 MDR Cycle 1 completion record (delegated line, human-ruled); prior: Claude — Synthesizer/Auditor, human-directed, 2026-08-02: History Appendix added (post-Cycle-3 Atrophied detection, inactive until Cycle 4), independence language strengthened to match `cold_session_bundler.py`'s bar; prior: Claude — Synthesizer/Auditor, human-directed, first draft, 2026-07-26 |
| Open Unknowns  | 0 — tracked at Admin/Auditor_Protocols.md AP-030 (mechanism-level, not template-level) |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.31 §Mission Drift Review.
When this file contradicts that section, the source document prevails.

---

## Scope Boundary

**DOES define:** The exact copy-paste block an operator pastes into a fresh, cold-start thread to run one Mission Drift Review cycle; the canonical input file list; the required output structure.

**DOES NOT define:** The mechanism's own design rationale, trigger cadence, or escalation rules (→ `Admin/Auditor_Protocols.md` §Mission Drift Review) · Axiom text itself (→ `Admin/Governance_Charter.md`) · How to log the result (→ that same section's Invocation Record requirements).

---

## How To Use This File

1. Confirm a trigger condition has actually fired (5 ratified governance/canonical changes since the last cycle, or 60 days elapsed — see `Admin/Auditor_Protocols.md` §Mission Drift Review, Trigger Cadence). If neither has fired, don't run this yet.
2. Open a **brand new thread** — not this one, not any thread that has discussed Mission Drift Review, its design, or a prior probe's results. This is not optional; see the source section's cold-start requirement.
3. Copy everything between the two `================` lines below into that new thread, attach or paste in the three canonical files it lists, and send. When preparing Cycles 2–3, first blank every rating cell in the History Appendix table and the cycle-metadata values (the file copy keeps them; the pasted block must not) — prior ratings must not reach the cold thread before Cycle 4.
4. Take the raw output and log it into `Admin/ALogs/Auditor_Protocols_Logs.md` per the Invocation Record fields in `Admin/Auditor_Protocols.md` §Mission Drift Review.
5. Update the running ratification counter and this file's own Resolution Log below. The counter is log-derived by design (no separate field or file — see `Admin/Auditor_Protocols.md` §Mission Drift Review, Trigger Cadence): the Invocation Record’s reset statement effects it.

================================================================

You are being asked to read a set of documents and describe, in your own words, what this project is trying to do. You have not seen this repository before this session and have no prior findings, summaries, or context about it beyond what is attached below — that is intentional. Do not search for outside information about it. Work only from the attached files.

**Attached canonical inputs (attach or paste all three in full):**
- `README.md`
- `Admin/Governance_Charter.md` (the Tier 1 Axioms section specifically: P-1 through P-4, Q-1 through Q-4)
- `Discovery.md`

**Do this in two separate, sequential steps. Do not skip ahead to step 2 before finishing step 1.**

---

### Step 1 — Comprehension

Based only on the attached files, describe in your own words:
- What this project is trying to build or accomplish
- What its core operating constraints or philosophy appear to be
- What it explicitly says it is willing to sacrifice, and for what

Write this as your own synthesis, not a summary that copies the documents' phrasing. Do not reference any axiom list, numbered principle, or governance structure yet — just describe what you'd tell someone who asked "what is this project actually for?" if all you had was these three files.

---

### Step 2 — Alignment Check

Now, and only now, look at the eight Tier 1 Axioms in `Admin/Governance_Charter.md`:

P-1 Preservation of Life · P-2 Growth and Truth-Seeking · P-3 Collaboration and Mutual Benefit · P-4 Agency and Consent · Q-1 Reality Grounding · Q-2 Separation of Powers · Q-3 Corrigibility · Q-4 Provenance and Anti-Deception

For **each of the eight**, compare your own Step 1 description against the axiom and assign exactly one rating:

- **Aligned** — your Step 1 description and the axiom clearly line up, with a citable basis
- **Weakened** — you can trace a connection, but only by inferring something the source text didn't state outright
- **Silent** — nothing in the attached files touched this axiom either way
- **Contradicted** — something in the attached files actively cuts against this axiom
- **Insufficient Evidence** — use this instead of guessing if you cannot point to a specific passage supporting whichever rating you were about to give

**For every one of the eight, you must cite the specific source** — quote or closely paraphrase the exact sentence or section in `README.md`, `Admin/Governance_Charter.md`, or a Resolution Log entry you were given that supports your rating. No citation, no rating above Insufficient Evidence.

Also label how strong that citation is, using this project's own evidence scale: **Measured** (a direct, explicit statement), **Replicated** (stated more than once, consistently), **Simulated/Analogous** (inferred from a comparable but not identical statement), or **Placeholder** (inferred mainly from absence of contrary evidence).

---

### Output format — use exactly this structure

**Step 1 — Comprehension (unscored):**
[your synthesis, 1–3 paragraphs]

**Step 2 — Alignment:**

| Axiom | Rating | Evidence label | Citation |
|---|---|---|---|
| P-1 Preservation of Life | | | |
| P-2 Growth and Truth-Seeking | | | |
| P-3 Collaboration and Mutual Benefit | | | |
| P-4 Agency and Consent | | | |
| Q-1 Reality Grounding | | | |
| Q-2 Separation of Powers | | | |
| Q-3 Corrigibility | | | |
| Q-4 Provenance and Anti-Deception | | | |

### History Appendix (ratings only — activate only from Cycle 4 onward)

The table below contains **prior probe ratings only**. It exists solely so you can apply the source rule:

> If the *same* axiom rates Silent across three or more consecutive probe cycles, the fourth occurrence escalates to **Atrophied** and is treated as Weakened for aggregation.

- Do **not** read this table before completing Step 1 (Comprehension).
- Do **not** let these prior ratings influence your Step 1 synthesis or your primary rating of any axiom in Step 2.
- Use the table **only** after you have assigned your own independent ratings, and solely to decide whether any of your "Silent" ratings must be escalated to "Atrophied".
- If a cell is blank or marked "—", treat that cycle as having no recorded rating for that axiom.

| Axiom | Cycle 1 | Cycle 2 | Cycle 3 | Cycle 4 | … |
|-------|---------|---------|---------|---------|---|
| P-1 Preservation of Life | Insufficient Evidence | | | | |
| P-2 Growth and Truth-Seeking | Aligned | | | | |
| P-3 Collaboration and Mutual Benefit | Weakened | | | | |
| P-4 Agency and Consent | Aligned | | | | |
| Q-1 Reality Grounding | Aligned | | | | |
| Q-2 Separation of Powers | Aligned | | | | |
| Q-3 Corrigibility | Aligned | | | | |
| Q-4 Provenance and Anti-Deception | Aligned | | | | |

**Cycle metadata (for operator use only — ignore for scoring):**
- Cycle 1 date / ratification count at trigger: 2026-10-29 / 5 (velocity trigger fired; the 60-day backstop had also elapsed ~2026-09-24 — dual trigger, AUDIT_30 F3; missed-backstop lapse folded into the Cycle 1 output per human ruling)
- Cycle 2 date / ratification count at trigger:
- Cycle 3 date / ratification count at trigger:
- …

When you escalate a rating to Atrophied, note it explicitly in the Citation cell of your Step 2 table (e.g. "Escalated to Atrophied per three prior Silent ratings — see History Appendix").

*Inactive for Cycles 1–3 — leave this table entirely blank and unmentioned in the pasted block until a fourth cycle is actually due. This file’s copy accumulates ratings after each completed cycle (operator workflow above); “blank” here means the copy that reaches the cold thread: blank every rating cell and cycle-metadata value before pasting Cycles 2–3, and keep the table unmentioned in any framing text. Operator workflow: after each completed probe, extract only the eight ratings from that cycle's Step 2 table and paste them into the next column here — never Phase A prose, evidence labels, or citations. When preparing Cycle 4+, include this updated appendix inside the invocation block pasted into the fresh thread. History Appendix schema v1, added 2026-08-02 — see Resolution Log.*

================================================================

---

## Resolution Log

- 2026-10-31: Path repair (no version bump) — Vibe (Repo Custodian, delegated line; 1.31 offline review by Claude, human-routed). How-To step 4's logging destination repointed `Archive/Logs/Auditor_Protocols_Logs.md` → `Admin/ALogs/Auditor_Protocols_Logs.md`: the changelog was relocated byte-identically by MAINT-29 (2026-10-30) and the step still named the old path. Path-only; probe text, rating vocabulary, evidence scale, canonical inputs, Step 1/Step 2 structure, appendix schema, and trigger cadence unchanged; the v1.2 entry below keeps its dated path reference as history.

- 2026-10-30: v1.4 — Vibe (Repo Custodian, delegated line, human-routed; defect flagged by an independent review, Claude, before any Cycle 2 invocation). Two halves of one v1.2 operator-workflow failure: (1) the Step 2 Output-format table inside the ==== paste block carried Cycle 1 ratings as pre-filled example values — a whole-block paste for Cycles 2–3 would have carried prior ratings into the cold thread, the exact leak v1.3's blanking rule was added to close (the rule covered the appendix but not the output template); all eight cells blanked. (2) The History Appendix Cycle 1 column, which v1.2 says the file copy keeps filled after each cycle, was left empty; the Cycle 1 ratings (P-1 Insufficient Evidence, P-3 Weakened, P-2/P-4/Q-1–Q-4 Aligned) are restored there. No change to probe text, rating vocabulary, evidence scale, canonical inputs, Step 1/Step 2 structure, appendix schema, or trigger cadence. Defect discovered against the 1.30 release review (CAMPAIGN_AUDIT_30 did not mention it).

- 2026-10-29: v1.3 — Vibe (Repo Custodian, delegated line; corrections from an independent review by Claude, human-routed, before any Cycle 2 invocation). (1) Counter correction: v1.2’s “physical counter field … updates at AP’s campaign audit” was wrong — the Trigger Cadence derives the count from the section’s own Resolution Log entries (no separate field/file by design), so the Cycle 1 Invocation Record’s reset statement already effects the reset; How-To step 5 now says so. (2) Independence gap closed: the filled History Appendix sits inside the ==== block, so a whole-block paste for Cycle 2 would have carried prior ratings into the cold thread — How-To step 3 and the appendix note now require blanking every rating cell and cycle-metadata value when pasting Cycles 2–3 (the appendix note’s original “leave blank” wording was ambiguous about which copy). (3) Baseline note: Cycle 1 is the baseline for the canonical input set as of 2026-10-29; no input-set change has been made, and any future change gets recorded as an instrument change with Cycle 1 as the old-set baseline (per review; prevents tuning the instrument to the score). P-1/P-3 dispositions remain HELD pending a second-rater run (review recommendation, human-routed); no ratings altered.

- 2026-10-29: v1.2 — Vibe (Repo Custodian, delegated line, human-ruled cycle ruling "MDR Cycle 1 executes now"). Cycle 1 completed: the cold-start probe ran in a fresh thread on the human’s side (this session has read the MDR design, so an in-session run was invalid per the cold-start rule); the raw output is the Invocation Record in `Archive/Logs/Auditor_Protocols_Logs.md` (AP-030 section). Per the operator workflow: the eight ratings extracted into the History Appendix Cycle 1 column (ratings only — no Phase A prose, evidence labels, or citations) and the Cycle-1 metadata line filled (2026-10-29 / 5, dual trigger). Ratings: P-1 Insufficient Evidence, P-2 Aligned, P-3 Weakened, P-4 Aligned, Q-1..Q-4 Aligned; no Silent ratings, so no escalation. The appendix stays inactive for scoring until Cycle 4 — operators pasting Cycles 2–3 keep the block’s appendix blank and unmentioned as instructed. Ratification counter reset to 0 as of this cycle; the physical counter in `Admin/Auditor_Protocols.md` §Mission Drift Review updates at that file’s campaign audit (X3 deferral stands). AUDIT_30 F4’s 3 bare AP citations: all located in frozen Resolution Log history or adjacency-qualified File State cells — in-place qualification is permanently out of scope by the frozen-history rule; annotation-only disposition stands (MAINT-11). No change to trigger cadence, canonical inputs, or Step 1/Step 2 structure.

- 2026-08-02: v1.1 — human-directed, verified against source before merge.
  Added the History Appendix (ratings-only table, inactive until Cycle
  4, schema v1) to close the post-Cycle-3 gap a Skeptic/Auditor review
  had flagged: the source section's Silent→Atrophied rule (three
  consecutive Silent ratings on the same axiom escalate the fourth) had
  no mechanism for carrying prior ratings into a cold-start thread
  without breaking informational independence. Design constraints kept:
  ratings only, never Phase A prose or citations; explicit "do not read
  before Step 1" sequencing instruction; no new rating vocabulary:
  Silent/Atrophied/Weakened reused exactly as the parent section
  defines them. Also strengthened the cold-start independence language
  ("you have not seen this repository before this session and have no
  prior findings") to match `Automation/cold_session_bundler.py`'s bar
  — the previous wording ("no prior context on this project") was
  slightly softer than the standard AP-017's own clarification sets
  elsewhere. Updated the `Derived from` pointer to
  `Admin/Auditor_Protocols.md` v0.31 (was v0.29, stale since that file's
  two same-day version bumps this session). Open Unknowns unchanged (0
  — still tracked at AP-030, mechanism-level not template-level). Not
  done: no change to trigger cadence, canonical input list, or Step
  1/Step 2 structure — those are working as audited and out of scope
  for this pass.
- 2026-07-26: v1.0 — initial draft, human-directed. Companion file for `Admin/Auditor_Protocols.md` v0.29 §Mission Drift Review. Closes the blocking half of AP-030 (the template did not exist); the N=5 threshold itself remains open pending three real cycles.
