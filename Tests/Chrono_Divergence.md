# Chrono_Divergence.md v0.1 -- Idea Fork Forecast & Best-Outcome Map (Test Protocol)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
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
| Last Audit       | 2026-10-12 — Created/Filed: v0 stub (human-directed). Registered: same day. Last audited: ChatGPT document-level audit, 2026-10-12 (findings applied in v0.1; not a Spec Gate verdict). Method only; no forecast portfolio claimed Measured. |
| Last Updated     | 2026-10-12 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Does:**

- Define a **test protocol** for mapping how an *idea* (doctrine, process, module, or experiment design) may **diverge over time**.
- Provide templates: t0 snapshot, branch/divergence table, review cadence, and scoring of forecasts against later evidence.
- Help choose the **smallest next experiment** that keeps high-value paths open (the best outcome compatible with the floors: a qualitative planning heuristic, not a score and not unlimited growth).
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

**Best outcome** here means: the best outcome still compatible with Ethical Constraints, evidence rules, and declared hard floors — not “grow at any cost.” It is a qualitative planning heuristic. Unless a specific map states its own decision criteria (cost, reversibility, uncertainty, time, ecological impact), no potential score exists. Prefer reversible, evidence-producing actions that preserve options.

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
| **Closed-by** | Why a branch is no longer pursued. One of: `Falsified` (evidence), `Prohibited by floor`, `Human-declined`, `Resource-deferred`, `Superseded`. Only `Falsified` is evidence about the idea; the others leave the branch visible and are never scored as disproven. |
| **Forecast** | A frozen, dated claim with a stable ID, observable success criteria and a scoring rule, declared before the test. Scored later as hit / miss / partial / unscorable / withdrawn. |


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
4. **Best outcome compatible with the floors** applies to both modes; incidental origin does not exempt hard floors or evidence rules.

Add to the t0 snapshot template: **Origin** = Incidental | Deliberate | Mixed (with dates).

### 2. Protocol (v0)

**Step A — Select idea**  
One idea per map. Cite owning file(s) and IDs (Unknowns, FL, sections).

**Step B — t0 snapshot**  
Fill the snapshot table (below). Mark every numeric or maturity claim Placeholder / Measured / etc. honestly.

**Step C — Branch table**  
List plausible divergence points and branches. Prefer fewer sharp forks over many vague ones. Mark whether branches are compatible (can coexist, such as compatible mitigations) or exclusive; do not assume every divergence is a single choice.

**Step D — Unlock column**  
Each open branch needs a **smallest next experiment** (run card, audit case, LE-0 phase, code test). "Write more doctrine" is not an unlock unless the gap is purely definitional. Smallness is not enough: each unlock states its question, controlled inputs, what each hypothesis predicts, a stopping rule, and known limitations. Evidence from a small trial is labeled Exploratory, not decisive.

**Step E — Review**  
At the review date, score each forecast against its frozen claim and criteria, with two reviewers scoring independently where possible; record any disagreement and keep both scores. Misses stay visible. Original forecasts are never edited: a change is a dated superseding entry with a reason (supersede-not-delete or dated strike).

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

#### 3.2 Divergence and branch table

`D1` identifies a divergence event. Its branches are `D1-A`, `D1-B`, and so on. Forecasts have their own IDs (`F1`, `F2`) in 3.3.

| Div. ID | Branch ID | Divergence point (trigger) | Branch | Compatible with | Unlock (smallest experiment) | Closed-by (type) | Review date |
|---------|-----------|----------------------------|--------|-----------------|------------------------------|------------------|-------------|
| D1 | D1-A | | | | | | |

#### 3.3 Forecast preregistration (frozen before the test)

| Forecast ID | Branch | Exact claim | Forecast date | Deadline / review date | Observable success criteria | Evidence source | Scoring rule (hit / partial / miss / unscorable) | Withdrawal conditions |
|-------------|--------|-------------|---------------|------------------------|-----------------------------|-----------------|-----------------------------------------------|-----------------------|
| F1 | D1-A | | | | | | | |

A forecast is optional on an Incidental map and expected on a Deliberate one. Once the test starts, the row is not edited; amendments are dated superseding rows.

#### 3.4 Scoring at review

| Forecast ID | Outcome | Reviewer 1 | Reviewer 2 | Disagreement | Notes |
|-------------|---------|------------|------------|--------------|-------|
| F1 | Hit / Partial / Miss / Unscorable / Withdrawn | | | | |

Always record the totals next to any accuracy summary: forecasts made, withdrawn, partial, unscorable. A hit rate without those counts invites optimizing for easy predictions. A small sample is not a stable estimate.

### 4. Worked example (illustrative — not a closed study)

**Idea:** Forge_Audit_Kit audit-start **reconciliation** (Derived-from pins vs live sources) — will auditors perform it **unprompted**?

| Field | Content |
|-------|---------|
| Idea name | Kit reconciliation salience |
| Owning file(s) | `Admin/Forge_Audit_Kit.md`; FAK-018; `FL-20261012-kit-regression-Gemini.md` |
| Date (t0) | 2026-10-12 |
| Status / evidence | Kit text defines content-based trigger + reconciliation check. Gemini Cases B and D: **Stage 1 miss** (no unprompted check), **Stage 2 pass** (correct when asked). FAK-018 open, mitigated. |
| Hard floors | Automation/kit does not decide governance; no silent Kit refresh mid-audit. |
| Open questions | Is the Stage 1 miss salience (placement/wording) or auditor-specific? |
| Evidence boundary | `FL-20261012-kit-regression-Gemini.md`, Case B and Case D, Stage 1 and Stage 2 sections. One auditor family (Gemini), two cases, one session each. Not a rate. |
| Non-goals | Not a ranking of models; not automatic Kit rewrite without human direction. |

Unit of analysis: one fresh, unprompted audit session of one case on one auditor family.

| Div. ID | Branch ID | Divergence point | Branch | Compatible with | Unlock | Closed-by (type) | Review |
|---------|-----------|------------------|--------|-----------------|--------|------------------|--------|
| D1 | D1-A | After the Gemini Stage 1 miss, before any further families run | **Salience fix** (pointer to the reconciliation check inside the Audit Opening Checklist) | D1-B | Kit variant with the pointer; Cases B and D, one unprompted session each, on at least 2 auditor families not yet used (at least 4 sessions) | `Human-declined` if the wording change is rejected | 2026-11-12 |
| D1 | D1-B | same | **Operator habit only** (always send Stage 2) | D1-A | Document the habit in the Kit's "How to Use"; no change to the checklist | `Falsified` if unprompted reconciliation turns out to be common on the shipped Kit | 2026-11-12 |
| D1 | D1-C | same | **Accept the rare Stage 1 check** | Excludes D1-A | Human decision to accept the miss. This would need FAK-018's closure condition (a full source revision cycle with no pin failure) changed by a human | `Human-declined` if the salience gap is not accepted | 2026-11-12 |
| D2 | D2-A | After Case A or C runs | Detection by comparing the Kit's copy with the source text | D2-B | Operator runs the planted-text pack with an independent auditor | `Resource-deferred` if no operator bandwidth | when run |
| D2 | D2-B | same | Detection only through a version difference | Excludes D2-A as the sole path | Same run; compare reports | `Falsified` if content mismatches are caught without a version change | when run |

Forecasts, frozen at t0 (2026-10-12):

| Forecast ID | Branch | Exact claim | Forecast date | Deadline | Observable success criteria | Evidence source | Scoring rule | Withdrawal conditions |
|-------------|--------|-------------|---------------|----------|-----------------------------|-----------------|--------------|-----------------------|
| F1 | D1-A | With the pointer variant, at least 2 of 4 Stage 1 reports contain an unprompted reconciliation statement | 2026-10-12 | 2026-11-12 | A statement about comparing the Derived-from line with live source versions appears in the Stage 1 report | The four Stage 1 reports in the filed Field Log | Hit: 2 or more of 4. Partial: exactly 1. Miss: 0. Unscorable: fewer than 4 valid sessions | A Kit change other than the pointer is made before the runs |
| F2 | D1-B | On the shipped Kit, the same families produce at most 1 of 4 unprompted reconciliation statements | 2026-10-12 | 2026-11-12 | Same as F1, on the shipped Kit | The four baseline Stage 1 reports | Hit: 0 or 1 of 4. Partial: not defined. Miss: 2 or more of 4. Unscorable: fewer than 4 valid sessions | The Kit changes before the baseline runs |

**Reading the example:** the best outcome compatible with the floors is not "everyone always reconciles unprompted." It is **honest measurement** plus the **cheapest branch** that still satisfies the Kit's purpose (stale condensed sections get noticed before reliance). The branches D1-A and D1-B can coexist; D1-C excludes D1-A.

#### 4.1 First pilot (proposed, not run)

The pilot should answer one narrow question: can two reviewers independently score the same predeclared forecasts from the same evidence, without the rules changing after the results are seen?

Before the pilot, record the exact forecasts and window, what counts as hit, partial, miss and unscorable, the evidence source, how reviewer disagreements are recorded, and what outcome would justify revising this protocol. Afterward, compare the independent scores and keep every disagreement. A single pilot does not show forecasting accuracy; the aim is that the scoring procedure is reproducible.

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
- Scoring reproducibility is untested. A single pilot cannot show forecasting accuracy.
- `Closed-by` types other than `Falsified` are governance or resource states, not evidence about an idea.

---

## Lessons Learned

- 2026-10-12: Kit regression B/D (Gemini) supplied the first concrete t0 for the worked example: unprompted reconciliation absent; prompted reconciliation competent. Example only; not a full Chrono run portfolio.

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| -- | None | -- | -- | -- | -- |

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

**Resolution Path:** Score 3-5 historical Progress_Log arcs retrospectively; tighten rubric. v0.1 adds a scoring contract (3.3 and 3.4) and an Unscorable outcome; its reproducibility is still untested until two reviewers score a pilot.

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

### Resolution Log

*(empty — no Unknown resolved)*

---

## Abandoned Paths

*(None yet.)*

---

## Drift Indicators

- Forecasts treated as commitments or governance weight.
- "Best outcome" or "potential" language used to override Ethical Constraints or Blocking Unknowns.
- Forecast claims edited after outcomes are known, or `Closed-by` types other than `Falsified` scored as disproof.
- Maps without review dates or without unlock experiments.
- Spec Gate advance justified only by a filled branch table.
- Open Unknowns count mismatch vs sidecar.

---

## Resolution Log

- 2026-10-12: **Registered** in Routing.md, Tst_Scope_Map.md, Discovery.md. Same day: §1.1 incidental spark vs deliberate forethought added; Origin field on t0 snapshot.
- 2026-10-12: **v0 Proposed stub filed.** Protocol steps A–F, templates, non-claims, four non-blocking Unknowns (CD-001–CD-004). Worked example: Kit reconciliation salience using FL-20261012-kit-regression-Gemini (Stage 1 fail / Stage 2 pass) as t0 evidence. Registered 2026-10-12 in Routing.md, Tst_Scope_Map.md, and Discovery.md.
- 2026-10-12: **v0.1 revision** after a ChatGPT document-level audit and human review (human-directed). Navigation anchors now use the canonical raw URLs. Forecasts get a preregistration and scoring contract (3.3, 3.4) with an Unscorable outcome, frozen claims and dated superseding amendments. IDs split into divergence (D1), branch (D1-A) and forecast (F1). Closed-by split into Falsified / Prohibited by floor / Human-declined / Resource-deferred / Superseded. The worked example now states its evidence boundary, uses a defined unit and compatible branches, and has dated forecasts with thresholds; "Stage 1 fail" reworded to "Stage 1 miss" (earlier log lines are left as history). "Maximum potential" renamed "best outcome compatible with the floors," a qualitative heuristic. Active Disputes section and a sidecar Resolution Log subsection added; a first-pilot description added (4.1). No Spec Gate, Unknown or status change; no new Unknown (CD-001 path extended).
