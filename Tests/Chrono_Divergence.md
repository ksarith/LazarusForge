# Chrono_Divergence.md — Idea Fork Forecast & Potential Map (Test Protocol)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](../Discovery.md)
* **Network Routing:** [Routing.md](../Routing.md)
* **Related:** [Admin/Trajectories.md](../Admin/Trajectories.md) · [Tests/Field_Logs.md](Field_Logs.md) · [Admin/Progress_Log.md](../Admin/Progress_Log.md) · [Challenges/Emergence.md](../Challenges/Emergence.md) · [Tests/Chaos_Dynamics.md](Chaos_Dynamics.md)

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | **Proposed** |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Open Unknowns    | 4 (sidecar below; all non-blocking) |
| Owner            | `Tests/Chrono_Divergence.md` |
| Last Audit       | 2026-10-12 — v0 Proposed stub filed (human-directed). Method only; no forecast portfolio claimed Measured. |
| Last Updated     | 2026-10-12 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Does:**

- Define a **test protocol** for mapping how an *idea* (doctrine, process, module, or experiment design) may **diverge over time**.
- Provide templates: t0 snapshot, branch/divergence table, review cadence, and scoring of forecasts against later evidence.
- Help choose the **smallest next experiment** that keeps high-value paths open (maximum *attainable* potential under constraints — not unlimited growth).
- Hold worked examples and Field_Log pointers when runs use this protocol.

**Does not:**

- Predict the future with authority, or treat forecasts as governance weight or claim confidence.
- Replace `Admin/Trajectories.md` (long-horizon mechanism design) or `Progress_Log.md` (what already happened).
- Use “quantum,” “superposition,” or similar language as physics claims — at most as informal metaphor for *unresolved exclusive choices*, and only if defined in-file as non-physical.
- Authorize Spec Gate promotion, Unknown closure, or physical work.
- Optimize for narrative coherence or hype; missed forecasts are evidence, not embarrassment.

---

## File Purpose

Ideas in the Forge fork: scope narrows or widens, metrics shift, authority boundaries move, implementations compete. Today that is visible only in retrospect (Resolution Logs, Progress_Log, audits). This file makes **forward branching** explicit and **falsifiable**: state the idea at t0, list plausible divergence points, name what would unlock or close each path, then score the map later.

**Maximum potential** here means: the best outcome still compatible with Ethical Constraints, evidence rules, and declared hard floors — not “grow at any cost.”

---

## Assumptions

1. An idea’s path is under-determined until evidence or a hard floor closes options.
2. Writing a branch down does not make it likely; it makes it **reviewable**.
3. The unit of progress is a **smallest experiment** (often a Field_Log), not a larger document.
4. Operators may be wrong about which branch matters; the protocol must record misses.

---

## Body

### 1. Operational definitions

| Term | Meaning in this file |
|------|----------------------|
| **Idea** | A named, citable claim-set or design (file section, protocol, Unknown cluster, experiment). |
| **t0 snapshot** | Dated description of the idea’s state: Status, open questions, constraints, evidence so far. |
| **Divergence point** | A decision or event after which two or more paths are no longer the same idea-in-practice (scope, metric, authority, implementation, or abandonment). |
| **Branch** | One coherent continuation from a divergence point. |
| **Unlock** | The smallest evidence-producing action that keeps a branch viable or advances it one epistemic step. |
| **Closed-by** | Floor, falsification, human decision, or resource limit that ends a branch. |
| **Forecast** | A dated claim that a divergence or unlock will occur by a review date — scored later as hit / miss / partial / withdrawn. |


### 1.1 Incidental spark vs deliberate forethought

Two different ways an idea enters the map. Mixing them confuses scoring.

| Mode | Meaning | How it should appear in a Chrono map |
|------|---------|--------------------------------------|
| **Incidental spark** | An idea or fork that **appeared without being chosen as a research target** — audit side-effect, Field_Log surprise, conversation residue, failed experiment’s byproduct. | Mark origin **Incidental**. t0 may be thin. Forecasts are optional; the first job is to *name* the fork so it is not lost. Unlock may be “decide whether to pursue.” |
| **Deliberate forethought** | An idea or fork **chosen in advance** for mapping — operator selects the idea, writes t0, and lists divergence points before further runs. | Mark origin **Deliberate**. Forecasts and review dates are expected. Unlocks should be pre-declared experiments. |

**Rules of thumb**

1. **Origin is not merit.** Incidental sparks can become the highest-value path; deliberate maps can be wrong.
2. **Do not retrofit prophecy.** If a path was incidental, do not later rewrite t0 as if it had been planned (progress notes may *add* a dated deliberate phase when pursuit begins).
3. **Promotion of mode.** Incidental → Deliberate is allowed when a human decides to run the full protocol on that idea; record the date of that decision in the snapshot.
4. **Maximum attainable potential** applies to both modes; incidental origin does not exempt hard floors or evidence rules.

Add to the t0 snapshot template: **Origin** = Incidental | Deliberate | Mixed (with dates).

### 2. Protocol (v0)

**Step A — Select idea**  
One idea per map. Cite owning file(s) and IDs (Unknowns, FL, sections).

**Step B — t0 snapshot**  
Fill the snapshot table (below). Mark every numeric or maturity claim Placeholder / Measured / etc. honestly.

**Step C — Branch table**  
List plausible divergence points and branches. Prefer fewer sharp forks over many vague ones.

**Step D — Unlock column**  
Each open branch needs a **smallest next experiment** (run card, audit case, LE-0 phase, code test). “Write more doctrine” is not an unlock unless the gap is purely definitional.

**Step E — Review**  
At the review date, score forecasts and update the map. Misses stay visible (supersede-not-delete or dated strike with reason).

**Step F — Field_Log**  
When the protocol is run for real, file `FL-YYYYMMDD-chrono-divergence-<slug>.md` and link it here or in the example section.

### 3. Templates

#### 3.1 t0 snapshot

| Field | Content |
|-------|---------|
| Idea name | |
| Owning file(s) | |
| Date (t0) | |
| Status / Spec Gates / evidence to date | |
| Hard floors that already constrain it | |
| Open Unknowns / residuals | |
| Explicit non-goals | |
| Origin | Incidental / Deliberate / Mixed (dates) |

#### 3.2 Branch / divergence table

| ID | Divergence point (trigger) | Branch | Unlock (smallest experiment) | Closed-by | Forecast (optional) | Review date |
|----|----------------------------|--------|------------------------------|-----------|---------------------|-------------|
| D1 | | | | | | |

#### 3.3 Forecast scoring (at review)

| Forecast ID | Claim | Outcome | Notes |
|-------------|-------|---------|-------|
| F1 | | Hit / Miss / Partial / Withdrawn | |

### 4. Worked example (illustrative — not a closed study)

**Idea:** Forge_Audit_Kit audit-start **reconciliation** (Derived-from pins vs live sources) — will auditors perform it **unprompted**?

| Field | Content |
|-------|---------|
| Idea name | Kit reconciliation salience |
| Owning file(s) | `Admin/Forge_Audit_Kit.md`; FAK-018; `FL-20261012-kit-regression-Gemini.md` |
| Date (t0) | 2026-10-12 |
| Status / evidence | Kit text defines content-based trigger + reconciliation check. Gemini Cases B and D: **Stage 1 fail** (no unprompted check), **Stage 2 pass** (correct when asked). FAK-018 open, mitigated. |
| Hard floors | Automation/kit does not decide governance; no silent Kit refresh mid-audit. |
| Open questions | Is Stage 1 failure salience (placement/wording) or auditor-specific? |
| Non-goals | Not a ranking of models; not automatic Kit rewrite without human direction. |

| ID | Divergence point | Branch | Unlock | Closed-by | Forecast (example) | Review |
|----|------------------|--------|--------|-----------|--------------------|--------|
| D1 | After ≥3 auditor families run Stage 1 | **A — Salience fix** (move reconciliation earlier / checklist item 0) | One Kit wording experiment + 2 fresh unprompted audits | Human rejects wording change | Partial: ≥1 unprompted reconciliation in next 3 runs | 2026-11-12 |
| D1 | same | **B — Prompt injection only** (operators always Stage-2) | Document operator habit in Kit “How to Use”; no body change | Evidence shows unprompted rate already high | Miss if Stage 1 stays rare and no doc change | 2026-11-12 |
| D1 | same | **C — Accept rare Stage 1** | Close FAK-018 as “mitigated; unprompted not required” with human note | Human refuses to accept salience gap | — | 2026-11-12 |
| D2 | Case A/C (content plant) run | Plant detection path vs version-only path | Operator runs Case A pack with independent auditor | Abandoned if no operator bandwidth | — | when run |

**Reading the example:** Maximum attainable potential is not “everyone always reconciles unprompted.” It is **honest measurement** plus the **cheapest branch** that still satisfies the Kit’s purpose (stale condensed sections get noticed before reliance).

### 5. Interfaces

| Peer | Relationship |
|------|----------------|
| `Admin/Trajectories.md` | Longer mechanism design; this file is shorter-cycle idea forks |
| `Tests/Field_Logs.md` | Evidence sink for scored maps |
| `Admin/Progress_Log.md` | May summarize completed chrono reviews; does not replace maps |
| CAP / AVE / MAQT | Point-in-time capability/reliability; may appear as unlocks on a branch |
| `Operations/*` | Domain ideas (e.g. Automotive floors) can be mapped; physical work still blocked by those files’ own floors |

### 6. Explicit non-claims

- No Measured accuracy for divergence forecasts until a review scores them.
- No claim that listing a branch makes it likely or approved.
- No quantum-mechanical model of ideas or organizations.
- Filing this stub does not change FAK-018, Kit text, or any Spec Gate.

---

## Lessons Learned

- 2026-10-12: Kit regression B/D (Gemini) supplied the first concrete t0 for the worked example: unprompted reconciliation absent; prompted reconciliation competent. Example only; not a full Chrono run portfolio.

---

## Auditor Notes & Unknowns

*All Open, non-blocking. Risk/Priority Placeholder severity for human confirmation.*

### CD-001 -- Forecast scoring rubric (hit / miss / partial) needs inter-rater stability

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Method |
| Blocking | No |
| Owner | `Tests/Chrono_Divergence.md` |
| First Logged | 2026-10-12 |
| Last Reviewed | 2026-10-12 |

**Description:** Partial credit rules for “divergence happened but different branch” are undefined.

**Resolution Path:** Score 3–5 historical Progress_Log arcs retrospectively; tighten rubric.

---

### CD-002 -- When a Chrono map should be mandatory vs optional

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Governance |
| Blocking | No |
| Owner | `Tests/Chrono_Divergence.md` |
| First Logged | 2026-10-12 |
| Last Reviewed | 2026-10-12 |

**Description:** Optional forever vs required for high-risk idea changes (e.g. new Operations domains).

**Resolution Path:** Human decision after 2–3 voluntary maps.

---

### CD-003 -- Relationship to Trajectories.md ownership boundaries

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Boundary |
| Blocking | No |
| Owner | `Tests/Chrono_Divergence.md` |
| First Logged | 2026-10-12 |
| Last Reviewed | 2026-10-12 |

**Description:** Avoid duplicate long-horizon design in both files.

**Resolution Path:** Short cross-link rule in both Resolution Logs after first real dual-use case.

---

### CD-004 -- Metaphor discipline (“potential,” informal physics language)

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low (Placeholder) |
| Priority | Minor (Placeholder) |
| Type | Semantic |
| Blocking | No |
| Owner | `Tests/Chrono_Divergence.md` |
| First Logged | 2026-10-12 |
| Last Reviewed | 2026-10-12 |

**Description:** Risk of semantic drift into unfalsifiable growth rhetoric.

**Resolution Path:** Fallacy/semantic review on first full map; amend glossary if needed.

---

## Abandoned Paths

*(None yet.)*

---

## Drift Indicators

- Forecasts treated as commitments or governance weight.
- “Maximum potential” used to override Ethical Constraints or Blocking Unknowns.
- Maps without review dates or without unlock experiments.
- Spec Gate advance justified only by a filled branch table.
- Open Unknowns count mismatch vs sidecar.

---

## Resolution Log

- 2026-10-12: **Registered** in Routing.md, Tst_Scope_Map.md, Discovery.md. Same day: §1.1 incidental spark vs deliberate forethought added; Origin field on t0 snapshot.
- 2026-10-12: **v0 Proposed stub filed.** Protocol steps A–F, templates, non-claims, four non-blocking Unknowns (CD-001–CD-004). Worked example: Kit reconciliation salience using FL-20261012-kit-regression-Gemini (Stage 1 fail / Stage 2 pass) as t0 evidence. Registered 2026-10-12 in Routing.md, Tst_Scope_Map.md, and Discovery.md.
