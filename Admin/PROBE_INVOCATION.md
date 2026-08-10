# PROBE_INVOCATION.md
**Version 1.1**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | N/A — operational prompt template, not a doctrine or specification claim |
| Verification Ref | Admin/Auditor_Protocols.md §Mission Drift Review                  |
| Last Audit     | 2026-08-02                                                          |
| Auditor        | Claude — Synthesizer/Auditor, human-directed, 2026-08-02: History Appendix added (post-Cycle-3 Atrophied detection, inactive until Cycle 4), independence language strengthened to match `cold_session_bundler.py`'s bar; prior: Claude — Synthesizer/Auditor, human-directed, first draft, 2026-07-26 |
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
3. Copy everything between the two `================` lines below into that new thread, attach or paste in the three canonical files it lists, and send.
4. Take the raw output and log it into `Archive/Logs/Auditor_Protocols_Logs.md` per the Invocation Record fields in `Admin/Auditor_Protocols.md` §Mission Drift Review.
5. Update the running ratification counter and this file's own Resolution Log below.

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
| P-1 Preservation of Life | | | | | |
| P-2 Growth and Truth-Seeking | | | | | |
| P-3 Collaboration and Mutual Benefit | | | | | |
| P-4 Agency and Consent | | | | | |
| Q-1 Reality Grounding | | | | | |
| Q-2 Separation of Powers | | | | | |
| Q-3 Corrigibility | | | | | |
| Q-4 Provenance and Anti-Deception | | | | | |

**Cycle metadata (for operator use only — ignore for scoring):**
- Cycle 1 date / ratification count at trigger:
- Cycle 2 date / ratification count at trigger:
- Cycle 3 date / ratification count at trigger:
- …

When you escalate a rating to Atrophied, note it explicitly in the Citation cell of your Step 2 table (e.g. "Escalated to Atrophied per three prior Silent ratings — see History Appendix").

*Inactive for Cycles 1–3 — leave this table entirely blank and unmentioned in the pasted block until a fourth cycle is actually due. Operator workflow: after each completed probe, extract only the eight ratings from that cycle's Step 2 table and paste them into the next column here — never Phase A prose, evidence labels, or citations. When preparing Cycle 4+, include this updated appendix inside the invocation block pasted into the fresh thread. History Appendix schema v1, added 2026-08-02 — see Resolution Log.*

================================================================

---

## Resolution Log

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
