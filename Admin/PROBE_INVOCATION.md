# PROBE_INVOCATION.md
**Version 1.0**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | N/A — operational prompt template, not a doctrine or specification claim |
| Verification Ref | Admin/Auditor_Protocols.md §Mission Drift Review                  |
| Last Audit     | 2026-07-26                                                          |
| Auditor        | Claude — Synthesizer/Auditor, human-directed, first draft, 2026-07-26 |
| Open Unknowns  | 0 — tracked at Admin/Auditor_Protocols.md AP-030 (mechanism-level, not template-level) |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.29 §Mission Drift Review.
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

You are being asked to read a set of documents and describe, in your own words, what this project is trying to do. You have no prior context on this project beyond what is attached below — that is intentional. Do not search for outside information about it. Work only from the attached files.

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

================================================================

---

## Resolution Log

- 2026-07-26: v1.0 — initial draft, human-directed. Companion file for `Admin/Auditor_Protocols.md` v0.29 §Mission Drift Review. Closes the blocking half of AP-030 (the template did not exist); the N=5 threshold itself remains open pending three real cycles.
