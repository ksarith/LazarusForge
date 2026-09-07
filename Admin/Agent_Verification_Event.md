# Agent Verification Event (AVE) — Schema & Reliance Rules

| Field            | Value |
|------------------|-------|
| Status           | Candidate / Exploration |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Owner            | `Admin/Agent_Verification_Event.md` (process schema); operational samples may land in `Tests/Field_Logs.md` |
| Last Updated     | 2026-09-07 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Purpose

Quantify **how much to rely on an agent’s checkable claims** without treating agent reputation as **claim confidence**.

AVE sits on the **node reliability / process** track only.

| Track | AVE role |
|-------|----------|
| **Node reliability** (agent-as-observer) | AVE outcomes update process reliability under verification |
| **Claim confidence** (DV-003 / evidence properties) | **Out of scope** — AVE must never multiply into epistemic confidence of a proposition |

Cross-reference: `Architecture/Forge_Net.md` §2.5.0 (claim confidence ≠ node reliability ≠ governance weight).

---

## Scope Boundary

**Does define:**

- Schema for a single verification event
- Claim classes eligible for cheap falsification
- Rolling reliability metrics (process only)
- Operational **reliance rules** (when to re-check source / quarantine a session)

**Does not define:**

- Cryptographic agent identity or Sybil resistance
- Automatic Unknown closure or File State edits from scores
- A global “trust score” used as access control or governance weight
- Replacement of Gate audits, RIP Phase 1 checks, or human ratification

---

## 1. Claim class (required before scoring)

| Class | Meaning | Typical check |
|-------|---------|----------------|
| **Inventory** | File/path/count/existence claims | `ls`, path resolve, Discovery map |
| **Quote** | “The file says …” | Open file; match span |
| **Structure** | “X gates on Y” / field/status relationships | Read owning section; compare |
| **Inference** | Design advice, priorities, closures | Ordinary review — **not** AVE-scored the same way |

Only **Inventory / Quote / Structure** enter reliability numerics by default. **Inference** may be logged as AVE with outcome `NotApplicable` or reviewed without scoring.

---

## 2. Agent Verification Event — record schema

One row (or block) per checkable claim that was actually verified by a party other than the claiming agent.

| Field | Required | Description |
|-------|----------|-------------|
| `ave_id` | Yes | Stable id for this event (e.g. AVE-YYYYMMDD-NNN) |
| `timestamp` | Yes | When verification completed |
| `claiming_agent` | Yes | Agent or role that made the claim (e.g. Gemini, Grok, Claude) |
| `session_ref` | Recommended | Session, zip, or thread id |
| `claim_class` | Yes | Inventory \| Quote \| Structure \| Inference |
| `claim_text` | Yes | Short verbatim or tight paraphrase of the claim |
| `claim_load_bearing` | Yes | Cosmetic \| LoadBearing \| ClosureBlocking |
| `verification_method` | Yes | What was done (e.g. `ls Architecture/`, read File_Template Ethical Anchor line) |
| `verifier` | Yes | Human or agent **other than** claiming_agent (or Human-directed script) |
| `outcome` | Yes | Pass \| Fail \| Partial |
| `severity_if_fail` | If Fail/Partial | Same scale as load-bearing, or upgraded if impact worse than claimed class |
| `doubled_down` | Yes | Yes \| No — claim defended after counter-evidence in-session |
| `would_have_affected` | Recommended | None \| Merge \| UnknownStatus \| FileState \| IncidentLog |
| `notes` | Optional | One to three sentences; no novel doctrine |
| `independent_of_speaker` | Yes | Yes if method does not take the claimer’s word as evidence |

**Hard rule:** The claiming agent must not be the sole `verifier` for events that update reliability metrics.

---

## 3. Rolling reliability metrics (process only)

Compute over a window of the last **k** scored events for that `claiming_agent` (default k = 20, or all if fewer), stratified by `claim_class` when volume allows.

| Metric | Definition | Use |
|--------|------------|-----|
| **Source-survival rate** | Pass / (Pass + Fail) among Inventory+Quote+Structure | Primary reliability signal |
| **Load-bearing fail rate** | Fails where claim_load_bearing ∈ {LoadBearing, ClosureBlocking} / such events | Danger signal |
| **Closure-contamination count** | Fails with would_have_affected ∈ {UnknownStatus, FileState, Merge} | How often uncaught error would have written governance state |
| **Contradiction-persistence count** | Events with doubled_down = Yes | Session-quarantine trigger |

**Partial** outcomes: count as Fail for survival rate unless notes document an agreed partial credit rule for that class.

**Do not** average Inference with Inventory. **Do not** publish a single scalar used as DV-003 input.

---

## 4. Reliance rules (operational)

These govern **scrutiny**, not belief.

| Rule | Trigger | Action |
|------|---------|--------|
| **R1 — Mandatory source-check** | Any ClosureBlocking claim, or LoadBearing Structure/Inventory claim from an agent with source-survival rate &lt; threshold (Placeholder: 0.8 over k≥5) | Verify against source before merge, Unknown status change, or File State edit |
| **R2 — Session quarantine** | One or more doubled_down = Yes on Fail in the same session | Treat further checkable claims from that agent in-session as **unverified until checked**; do not block unrelated agents |
| **R3 — Sampling relief** | Source-survival ≥ threshold over k≥10 and zero Closure-contamination in window | May reduce *spot-check rate* on Cosmetic Inventory only; **never** skip R1 triggers |
| **R4 — No confidence promotion** | Any reliability metric | **Forbidden** to increase claim confidence, promote Provisional→higher epistemic state, or satisfy DV-003 thresholds |

Thresholds above are **Placeholder** until calibrated against Field_Logs samples. Structure of rules is fixed; numbers are not.

---

## 5. Where to log

| Volume | Home |
|--------|------|
| Sparse / notable fails (Gemini folder claim, fabricated G5, etc.) | `Tests/Field_Logs.md` or session Progress_Log pointer |
| Routine batch | Optional table in Field_Logs or a future lightweight log under `Archive/Logs/` |
| Doctrine changes to this schema | This file’s Resolution Log |

No requirement that every chat sentence become an AVE — only claims that were **actually verified** (or that failed verification when checked).

---

## 6. Worked examples (illustrative)

**Example A — Inventory fail (Gemini)**  
- claim_class: Inventory  
- claim_text: “Architecture folder has only two files”  
- method: `ls Architecture/` → many files  
- outcome: Fail; load_bearing: LoadBearing; doubled_down: Yes  
- would_have_affected: Merge (if specs based on false inventory)  
- R2 applies for rest of session  

**Example B — Quote pass**  
- claim_class: Quote  
- claim_text: Ethical Anchor has no Admin/ prefix  
- method: read File_Template.md canonical string  
- outcome: Pass  
- updates source-survival only  

**Example C — Inference (not scored)**  
- claim_class: Inference  
- claim_text: “Expand Network Invariants next”  
- outcome: NotApplicable / review only  

---

## 7. Residuals

| ID | Residual |
|----|----------|
| AVE-R1 | Calibrate k and source-survival threshold against real multi-agent logs |
| AVE-R2 | Whether ClosureBlocking fails should auto-suggest Integrity_Incident_Log (process link, not automatic) |
| AVE-R3 | Machine-readable AVE table vs prose Field_Logs entries |
| AVE-R4 | Interaction with GOV-021 independence dimensions (complementary, not duplicate) |

---

## 8. Integration hooks

- `Architecture/Forge_Net.md` §2.5.0 — reliability track only  
- `Admin/Auditor_Protocols.md` — verification discipline; AVE does not replace Gates  
- `Tests/Field_Logs.md` — sample home for notable events  
- `Admin/Repository_Integrity_Protocol.md` — load-bearing false inventory may inform integrity review; AVE is not a RIP violation class by itself  

---

## Resolution Log

- 2026-09-07: **AVE schema drafted (Candidate).** Claim classes, event fields, rolling metrics, reliance rules R1–R4, explicit ban on feeding DV-003. Worked examples from recent session failure modes. No Unknowns index registration until Human decides ownership/promotion path. Drafted by Grok, human-directed.

---

## Abandoned Paths

- Single scalar “agent trust” used for access control or claim promotion — rejected (collides with §2.5.0 and Priority-1 Forge_Net fix).
- Claiming agent self-scoring into reliability metrics — rejected.
