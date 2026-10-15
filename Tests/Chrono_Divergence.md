# Chrono_Divergence.md v0.6 -- Idea Fork Forecast & Best-Outcome Map (Test Protocol)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
* **Related:** [Admin/Trajectories.md](../Admin/Trajectories.md) · [Tests/Field_Logs.md](Field_Logs.md) · [Admin/Progress_Log.md](../Admin/Progress_Log.md) · [Challenges/Emergence.md](../Challenges/Emergence.md) · [Tests/Chaos_Dynamics.md](Chaos_Dynamics.md) · [Tests/Chrono_Divergence_Pilot.md](Chrono_Divergence_Pilot.md)

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
| Last Audit       | 2026-10-15 — editorial trim after a repo-wide integrity pass (no content change). Last content revision v0.6 (2026-10-14, after ChatGPT's review of v0.4). Earlier audits (ChatGPT, fresh-instance Claude, Grok) are recorded in the Resolution Log. Method only; no forecast portfolio claimed Measured. |
| Last Updated     | 2026-10-15 |
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
| **Forecast** | A frozen, dated claim with a stable ID, observable success criteria and a scoring rule, declared before the test. **Frozen** means locked at the preregistration record (§4.1 item 7); before that point a revision is allowed but is logged with date and reason in the row. Scored later as hit / miss / partial / unscorable / withdrawn. |


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
At the review date, score each forecast against its frozen claim and criteria, with two reviewers scoring independently where possible; record any disagreement and keep both scores. Misses stay visible. Once frozen, original forecasts are never edited: a change is a dated superseding entry with a reason (supersede-not-delete or dated strike).

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

A forecast is optional on an Incidental map and expected on a Deliberate one. A row freezes at its preregistration record (§4.1 item 7) and in any case before the first test session; after that it is not edited and amendments are dated superseding rows. Before that point a revision is allowed but is recorded in the row's Frozen cell with date and reason.

#### 3.4 Scoring at review

| Forecast ID | Outcome | Reviewer 1 | Reviewer 2 | Disagreement | Notes |
|-------------|---------|------------|------------|--------------|-------|
| F1 | Hit / Partial / Miss / Unscorable / Withdrawn | | | | |

Always record the totals next to any accuracy summary: forecasts made, withdrawn, partial, unscorable. A hit rate without those counts invites optimizing for easy predictions. A small sample is not a stable estimate.

### 4. Worked example (illustrative — not a closed study)

**Idea:** Forge_Audit_Kit audit-start **reconciliation** (Derived-from pins vs live sources).

**Two outcome measures (do not collapse):**

| Measure | Question | Scored from |
|---------|----------|-------------|
| **M1 — Unprompted detection** | Does the auditor independently notice the reconciliation requirement in Stage 1? | Stage 1 report only |
| **M2 — End-to-end safety** | Is a stale pin or condensed-section risk flagged before the audit relies on the Kit for those sources? | Stage 1, or Stage 2 if Stage 1 missed, or equivalent operator-required check |

Branches may target different measures. Comparing D1-A and D1-B as if they measured the same capability is invalid.

| Field | Content |
|-------|---------|
| Idea name | Kit reconciliation salience |
| Owning file(s) | `Admin/Forge_Audit_Kit.md`; FAK-018; `FL-20261012-kit-regression-Gemini.md` |
| Date (t0) | 2026-10-12 |
| Origin | **Incidental** spark (Kit regression runs) → **Deliberate** map starting 2026-10-12 |
| Status / evidence | Kit text defines content-based trigger + reconciliation check. Gemini Cases B and D: **Stage 1 miss** (no unprompted check), **Stage 2 pass** (correct when asked). FAK-018 open, mitigated. Log caveats: Case B Stage 1 reported checks the pack could not support; Case D used retrieval tools (possible bleed). |
| Hard floors | Automation/kit does not decide governance; no silent Kit refresh mid-audit. |
| Open questions | Is the Stage 1 miss salience (placement/wording) or auditor-specific? |
| Evidence boundary | `FL-20261012-kit-regression-Gemini.md`, Case results table (Stage 1 / Stage 2 columns) and Secondary form notes. One auditor family (Gemini), two cases, one session each. Not a rate. |
| Non-goals | Not a ranking of models; not automatic Kit rewrite without human direction. |

Unit of analysis: one fresh, unprompted audit session of one case on one auditor family (for M1). M2 may include a prompted Stage 2 in the same session when Stage 1 missed.

| Div. ID | Branch ID | Divergence point | Branch | Primary measure | Compatible with | Unlock | Closed-by (type) | Review |
|---------|-----------|------------------|--------|-----------------|-----------------|--------|------------------|--------|
| D1 | D1-A | After the Gemini Stage 1 miss, before any further families run | **Salience fix** (pointer to the reconciliation check inside the Audit Opening Checklist) | M1 | D1-B (ops); excludes D1-C | Kit variant with the pointer; Cases B and D; ≥2 new auditor families; ≥4 Stage 1 sessions; see session controls below | `Human-declined` if the wording change is rejected | 2026-11-12 |
| D1 | D1-B | same | **Operator habit only** (always require Stage 2 if Stage 1 omits reconciliation) | M2 | D1-A | Document the habit in the Kit's "How to Use"; no claim that this improves M1 | Not falsified by high M1 rates; may be `Human-declined` if operators refuse the habit | 2026-11-12 |
| D1 | D1-C | same | **Accept low M1** (do not change Kit wording; do not require Stage 2) | Policy | Excludes D1-A (Kit wording changed) and D1-B (Stage 2 required) | Human decision; may require adjusting FAK-018 closure narrative | `Human-declined` if the salience gap is not accepted | 2026-11-12 |
| D2 | D2-A | After Case A or C runs (A = content change plus version bump; C = content change without version bump; neither run yet; planted text held by the operator) | Detection by **source-text comparison** (Kit condensed section vs live source body) | Detection path | D2-B as alternate path | Operator runs planted-text pack with an independent auditor | `Falsified` if the defined comparison procedure **fails to detect** a planted content mismatch under valid test conditions. `Resource-deferred` if no bandwidth | 2026-11-12 (record `Resource-deferred` if not run) |
| D2 | D2-B | same | Detection that **depends on a version difference** (claims version delta is necessary for notice) | Detection path | Excludes D2-A as sole path only if D2-B asserts necessity | Same run; compare reports | `Falsified` if a content mismatch is detected **without** a version difference, when D2-B claimed version difference was necessary. Version-only detection does **not** prove version comparison is the only viable path | 2026-11-12 (record `Resource-deferred` if not run) |

**Session controls (required for F1/F2 attribution):**

- Fresh session per case; no prior exposure to Kit reconciliation pack design or Case B/D outcomes.
- Record model/version, prompt hash or verbatim prompt, case ID, session order, and prior exposure.
- Randomize or counterbalance baseline (shipped Kit) vs intervention (pointer variant) **across** auditor families when both are run; do not treat a family's second session on the same case as independent evidence of the pointer.
- If controls cannot be met, label results **exploratory** and do not attribute differences to the pointer alone.
- **Valid Stage 1 session** (for `k/n`): fresh session; controls recorded; unhinted prompt that does not describe the reconciliation check; case pack as the operator specified; a completed initial audit report. Tool or retrieval use beyond the pack, and claims of checks the pack could not support, do not invalidate a session for M1 (M1 asks only whether a reconciliation statement appears) but are recorded as annotations and reported beside `k/n`. A session that breaks a control, or whose prompt reveals the check, is invalid.
- **Baseline counting:** the existing Gemini Case B and D Stage 1 sessions (0/2) predate the preregistration and these controls. They are prior data and are not counted among the 4 sessions for F1 or F2.
- **Allocation rule (v0.5):** the counting unit is the (auditor family, case) pair, and each pair is run at most once across both arms. n = 4 valid sessions per arm therefore needs 8 distinct pairs, for example 4 families × Cases B and D, or 2 families × 4 equivalent operator-held case variants. Pair independence is not the same as independence of the experimental unit: a family that appears in both arms can carry exposure from one arm to the other (account memory or shared files, an operator who adapts the prompt after seeing the pointer, a session that is not truly isolated).
  - **Terms:** the *allocation unit* is what is assigned to an arm (a family-and-case session slot in the within-family design; a whole family in the between-family design). The *observation unit* is the valid session. Sessions are treated as independent only under the isolation, order and carryover conditions below; the pair rule is a counting convention, not a statistical independence claim, and cases assessed by one family may share systematic bias.
  - **Default (within-family):** each family runs both arms on different cases, so family differences are not confounded with arm. Order is counterbalanced (half the families baseline-first, half pointer-first) and every case appears in both arms. Each session is isolated: new chat, memory off or no carried content, no shared project, files or custom instructions holding Kit text, and the prompt is the preregistered text verbatim, not edited between sessions.
  - **Carryover check:** report M1 by order position. If baseline sessions run after a pointer session show more M1 than baseline sessions run first, label cross-arm contamination suspected and treat F2 as exploratory.
  - **Alternative (between-family):** each family appears in one arm only. For example 2 families per arm × Cases B and D (4 families in total). This removes cross-arm carryover but confounds family with arm, so it is also exploratory unless families can be matched; use it only if isolation cannot be shown. With a few available families it is usually the weaker choice.
  - The preregistration record declares which design is used. Either way, with n = 4 per arm from a few families, read the arms as exploratory evidence about the pointer. The §4.1 pilot claim is scoring reproducibility, which this exposure affects in what is scored but not in whether reviewers agree. The assignment and order are declared in the preregistration record before the first run. With fewer than 8 distinct pairs, F1/F2 are Unscorable and sessions may be reported as exploratory `k/n` at their actual n.
- **Memory and personalization state:** record whether the auditor product's memory or personalization features were on for each session, and whether any earlier conversation in that account touched the pack, the Kit reconciliation design, or Case B/D outcomes. A session whose memory demonstrably held any of those is invalid; memory-on sessions without such content are valid but annotated.

**Counts, not vague frequency:** For this pilot, report M1 as `k/n` valid Stage 1 sessions (e.g. 0/4, 1/4). Do not use "common" or "rare" except as shorthand for a preregistered `k/n` threshold stated in the forecast row.

| F ID | Branch | Frozen claim | Frozen | Review by | Observation | Evidence source | Scoring | Withdraw if |
|------|--------|--------------|--------|-----------|-------------|-----------------|---------|-------------|
| F1 | D1-A | With the pointer variant, at least 2 of 4 Stage 1 reports contain an unprompted reconciliation statement (**M1**) | Declared 2026-10-12; revised 2026-10-13 (v0.2, v0.3; pre-freeze); freezes at preregistration record | 2026-11-12 | Unprompted Derived-from vs live comparison appears in Stage 1 | Filed Field Log Stage 1 sections | Hit: ≥2/4. Partial: exactly 1/4. Miss: 0/4. Unscorable: fewer than 4 valid sessions | A Kit change other than the pointer is made before the runs; or session controls broken |
| F2 | D1 baseline | On the shipped Kit (no pointer), the same design yields at most 1 of 4 unprompted reconciliation statements (**M1**) | Declared 2026-10-12; revised 2026-10-13 (v0.2, v0.3; pre-freeze); freezes at preregistration record | 2026-11-12 | Same observation as F1, shipped Kit | Filed Field Log Stage 1 sections | Hit: 0/4 or 1/4. Partial: **not applicable** (threshold is already a band; use Hit/Miss only). Miss: ≥2/4. Unscorable: fewer than 4 valid sessions | The Kit changes before the baseline runs; or session controls broken |

**Forecast coverage:** F1 and F2 cover D1-A and the shipped-Kit baseline only. D1-B, D1-C and D2 have no forecast yet, though a Deliberate map expects them. Declaring them, or recording a reason, is open before any formal pilot.

**Unscorable vs Withdrawn:** Unscorable = cannot assess under declared criteria (e.g. too few valid sessions). Withdrawn = a predeclared withdrawal condition in the forecast row is met. Withdrawal must not be used to avoid recording an unfavorable Hit/Miss/Partial.

**Reading the example:** the best outcome compatible with the floors is not "everyone always reconciles unprompted." It is **honest measurement of M1 and M2** plus the **cheapest branch** that still satisfies the Kit's purpose (stale condensed sections get noticed before reliance — M2). D1-A targets M1; D1-B targets M2; they are not substitutes for each other.

#### 4.1 First pilot (proposed, not run)

**Pilot claim (narrow):** Can two reviewers independently score the same frozen forecasts (F1/F2) from the same Field_Log evidence with documented agreement?

**Not the pilot claim:** That the pointer works, or that forecasts are accurate in general.

**Sequence:** (1) the preregistration record is made (item 7 below); (2) the pointer-variant and baseline sessions are run and filed as a Field_Log; (3) two reviewers score F1/F2 from that Field_Log. Step 3 cannot start before steps 1 and 2; until then the pilot is unstarted.

**Reviewers:** named in the pilot record with their roles. A reviewer who wrote or audited the forecast or rubric text (for example an agent that audited v0.1 or v0.2) is labeled as such, and the pair should include at least one reviewer who did not.

**Pilot protocol:** operationalized in `Tests/Chrono_Divergence_Pilot.md` (Proposed, not started). This section stays authoritative for the claim, the forecasts and the scoring rules; the pilot file points here and does not copy them.

**Pre-pilot checklist (must be satisfied before scoring F1/F2 as a formal pilot):**

1. D2-A / D2-B falsification conditions refer to each branch's own claim (see table above).
2. M1 and M2 are scored separately; D1-B is not treated as an M1 intervention.
3. Session ordering, allocation (distinct family-and-case pairs, per the allocation rule in §4), exposure controls including memory state, and independence limits are recorded.
4. Every scoring category is defined (F2 Partial = N/A as above).
5. Frequency language is bound to `k/n` thresholds in the forecast rows.
6. Reviewer agreement and rubric-revision rules are predeclared (below).
7. Preregistration record is preserved (content hash or commit of this file section) and linked from the test-start Field_Log note; hash shows identity, not creation time — retain log/history for ordering.
8. Trial remains exploratory; preserve misses, disagreements, and invalid sessions.
9. Forecast coverage for D1-B, D1-C and D2 is declared, or the gap is recorded with a reason.

**Reviewer agreement (pilot acceptance rule, not universal proof):**

- Two reviewers; independent scores on F1 and F2 before discussion.
- Record exact agreement and categories in disagreement.
- Disagreements preserved; optional adjudicated score labeled as such.
- Rubric revision triggered if both reviewers independently mark the same forecast Unscorable for a reason not in the preregistration, or if they disagree on Hit vs Miss for the same `k/n` count.
- Raw agreement + disagreement analysis is the reported output for this pilot size — not a reliability coefficient and not a pass/fail threshold.
- Three outcomes are kept distinct. **Procedurally complete:** preregistration, sessions, independent scoring and records followed the required sequence; this is the pilot's minimum acceptance criterion. **Scoring agreement observed:** reviewers assigned matching categories; this is a result to report, not a predetermined success, and the pilot is procedurally complete even if reviewers disagree on every score. **Rubric reliability supported:** requires a larger, appropriately designed evaluation and is not licensed by this pilot.

### 5. Interfaces

| Peer | Relationship |
|------|----------------|
| `Admin/Trajectories.md` | Longer mechanism design; this file is shorter-cycle idea forks |
| `Tests/Field_Logs.md` | Evidence sink for scored maps |
| `Admin/Autonomy_Divergence_Protocol.md` | Response tiers for autonomy drift and peer divergence; this file maps idea forks and sets no response tiers or authority |
| `Tests/Chrono_Divergence_Pilot.md` | Operational protocol for the §4.1 scoring-reproducibility pilot; points here for forecasts and rules |
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
| Last Reviewed | 2026-10-14 |

**Description:** Residual after v0.1–v0.2: inter-rater agreement on Hit/Miss/Partial/Unscorable/Withdrawn still untested; F2 Partial is N/A for this example but other maps need explicit Partial rules; withdrawal must not substitute for unfavorable scores.

**Resolution Path:** Run §4.1 pilot per `Tests/Chrono_Divergence_Pilot.md` (two reviewers, same frozen F1/F2 evidence); revise rubric only under predeclared triggers. Optional: score 3–5 historical Progress_Log arcs retrospectively.

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
| Last Reviewed | 2026-10-13 |

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
| Last Reviewed | 2026-10-13 |

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
| Last Reviewed | 2026-10-13 |

**Description:** Risk of semantic drift into unfalsifiable growth rhetoric.

**Resolution Path:** Fallacy/semantic review on first full map; amend glossary if needed.

### Resolution Log

*(No Unknown resolved. Entries below are file change history, newest first.)*

- 2026-10-15: Editorial, no version bump. Last Audit cell trimmed to current state with a pointer to this log (the long "Prior:" chain duplicated this log and tripped a checker warning); Last Updated aligned. No content, forecast, Spec Gate, Unknown or Status change.
- 2026-10-14: **v0.6 revision** after ChatGPT's review of v0.4 (assessed against source; v0.5 had already added isolation, counterbalanced order and a carryover check for the cross-arm exposure it raised). New here: allocation unit / observation unit / independence-assumption vocabulary; the between-family alternative given a concrete 2-families-per-arm shape (4 families in total, so ChatGPT's current recommendation is feasible, unlike its earlier 4-per-arm version); the preregistration declares which design is used; and the pilot acceptance rule now separates procedurally complete, scoring agreement observed, and rubric reliability supported. No forecast text, Spec Gate, Unknown ID or Status change.
- 2026-10-14: **v0.5 revision** after a further ChatGPT review (claims weighed against source; human-directed). The v0.4 allocation rule fixed same-case reuse but did not address cross-arm exposure for a family that appears in both arms. Added the distinction between pair independence and experimental-unit independence, a default within-family design with counterbalanced order and isolation requirements, a carryover check by order position, and the between-family alternative with its tradeoff (family confounded with arm). ChatGPT's preferred one-arm-per-family design was kept as the alternative, not the default: it needs about 8 families and confounds family with arm. No forecast text, Spec Gate, Unknown ID or Status change.
- 2026-10-14: **v0.4 revision** after ChatGPT (LF-122-04) and Grok reviews of release 1.22 (human-directed; claims verified against the 1.22 zip). The worked example's allocation could not meet its own independence rule: n=4 per arm from 2 families on Cases B and D forces each family to run the same case in both arms. Added an allocation rule (independence unit = family-and-case pair, 8 distinct pairs for n=4 per arm, fewer pairs → Unscorable, exploratory reporting allowed) and a memory/personalization-state control; checklist item 3 updated; §4.1 points to the new `Tests/Chrono_Divergence_Pilot.md`; Interfaces gained rows for `Autonomy_Divergence_Protocol.md` and the pilot file; CD-001 resolution path points to the pilot file. No forecast text, Spec Gate, Unknown ID or Status change.
- 2026-10-13: **v0.3 revision** after a fresh-instance Claude audit (11 findings, verified against the zip; human-directed). Forecast freeze point defined (the preregistration record), and the F1/F2 Frozen cells now record the 2026-10-13 pre-freeze revisions; D1-A/D1-C compatibility contradiction fixed (D1-C also excludes D1-B); valid-session, baseline-counting and allocation rules added; §4.1 gained sequence and reviewer-role rules and checklist item 9; Case A/C defined inline; D2 review dates set to 2026-11-12; t0 evidence caveats and evidence-boundary citation corrected; CD-001–004 Last Reviewed updated; Resolution Log moved into the nested template form and put in newest-first order. Registration drift fixed in Routing.md (missing Tests/ row) and Discovery.md (tree wording). No Spec Gate, Unknown ID, or Status change.
- 2026-10-13: **v0.2 revision** after ChatGPT follow-up audit (CD-B01–B06; human-directed). Worked example: fixed inverted D2-A falsification; split M1 unprompted detection vs M2 end-to-end safety; session-order/exposure controls; F2 Partial = N/A; Unscorable vs Withdrawn; k/n instead of common/rare; pilot agreement criteria and pre-pilot checklist; preregistration hash note. CD-001 description updated to current residual. No Spec Gate, Unknown ID, or Status change.
- 2026-10-12: **v0.1 revision** after a ChatGPT document-level audit and human review (human-directed). Navigation anchors now use the canonical raw URLs. Forecasts get a preregistration and scoring contract (3.3, 3.4) with an Unscorable outcome, frozen claims and dated superseding amendments. IDs split into divergence (D1), branch (D1-A) and forecast (F1). Closed-by split into Falsified / Prohibited by floor / Human-declined / Resource-deferred / Superseded. The worked example now states its evidence boundary, uses a defined unit and compatible branches, and has dated forecasts with thresholds; "Stage 1 fail" reworded to "Stage 1 miss" (earlier log lines are left as history). "Maximum potential" renamed "best outcome compatible with the floors," a qualitative heuristic. Active Disputes section and a sidecar Resolution Log subsection added; a first-pilot description added (4.1). No Spec Gate, Unknown or status change; no new Unknown (CD-001 path extended).
- 2026-10-12: **Registered** in Routing.md, Tst_Scope_Map.md, Discovery.md. Same day: §1.1 incidental spark vs deliberate forethought added; Origin field on t0 snapshot.
- 2026-10-12: **v0 Proposed stub filed.** Protocol steps A–F, templates, non-claims, four non-blocking Unknowns (CD-001–CD-004). Worked example: Kit reconciliation salience using FL-20261012-kit-regression-Gemini (Stage 1 fail / Stage 2 pass) as t0 evidence. Registered 2026-10-12 in Routing.md, Tst_Scope_Map.md, and Discovery.md.

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
