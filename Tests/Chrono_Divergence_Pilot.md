# Chrono_Divergence_Pilot.md v0.4 -- Scoring Reproducibility Pilot (CD-Pilot-001)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
* **Related:** [Tests/Chrono_Divergence.md](Chrono_Divergence.md) · [Tests/Field_Logs.md](Field_Logs.md) · [Admin/Forge_Audit_Kit.md](../Admin/Forge_Audit_Kit.md) · `Tests/Field_Logs/FL-20261012-kit-regression-Gemini.md`

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | **Proposed** (pilot not started) |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Open Unknowns    | 0 (surfaces CD-001, owned by `Tests/Chrono_Divergence.md`; creates none) |
| Owner            | `Tests/Chrono_Divergence.md` |
| Last Audit       | 2026-10-15 — v0.4: preregistration template corrected after Claude review (single allocation table, hash scope, blank-as-not-ready, under-8-pairs consequence). Prior same day: template first added; editorial trim. Drafted by Grok, corrected by Claude; not yet audited by a second agent. History is in the Resolution Log. |
| Last Updated     | 2026-10-15 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Does:**

- Operationalize `Tests/Chrono_Divergence.md` §4.1: the order of steps, allocation, filing and scoring for the first scoring-reproducibility pilot.
- Record the pilot's preregistration inputs (allocation table, pointer wording, named reviewers) once they exist.

**Does not:**

- Copy or restate the frozen forecasts F1/F2, the scoring categories, the valid-session definition or the reviewer-agreement rules. These live in `Tests/Chrono_Divergence.md` §4 and §4.1, and this file points there so there is one source.
- Hold run evidence. Sessions are filed as Field_Logs (`Tests/Field_Logs/FL-YYYYMMDD-chrono-divergence-<slug>.md`, per Chrono Step F), not here.
- Claim the pointer works, that forecasts are accurate, or that scoring agreement generalizes beyond this pilot size.
- Change FAK-018 status, Kit text, Spec Gates, or any Unknown.

---

## File Purpose

Chrono_Divergence.md defines the protocol and the worked example. A pilot needs concrete, ordered, fillable steps. This file holds those steps so the protocol file does not grow into a run sheet, and so run evidence (Field_Logs) stays separate from protocol (here).

---

## Assumptions

1. The pilot claim is narrow: two independent reviewers can score the same frozen forecasts from the same filed evidence and produce documented agreement or fully recorded disagreement.
2. Only the preregistration record freezes F1/F2 (Chrono §3.3). Until it exists, the pilot is unstarted.
3. Sessions are counted per (auditor family, case) pair (Chrono §4 allocation rule), so n per arm is bounded by the number of distinct pairs available. A pair is not automatically an independent experimental unit: cross-arm exposure within a family is controlled by isolation, counterbalanced order and a carryover check.

---

## Body

### 1. Pilot claim

**Claim:** Two independent reviewers can score F1 and F2 from the same Field_Log evidence and produce documented agreement (exact category match, or fully recorded disagreement plus an optional labeled adjudicated score).

**Not the claim:** that the pointer works; that forecasts are accurate in general; that agreement generalizes beyond this pilot size. Completion licenses no accuracy statement about the pointer.

### 2. Sequence (hard order)

| Step | Action | Gate |
|------|--------|------|
| 0 | This file filed, registered, and linked from Chrono §4.1 | Done when registered |
| 1 | **Preregistration record** made: hash or commit of the Chrono forecast rows and §4 session controls, plus the filled allocation table (§4 below), exact pointer wording, and named reviewers | Must precede any data-collection session |
| 2 | Sessions run and filed as Field_Log(s), both arms | Needs 8 distinct (family, case) pairs for n=4 per arm; otherwise F1/F2 are Unscorable and results are reported as exploratory |
| 3 | Two named reviewers score F1 and F2 independently, before discussion | At least one reviewer did not write or audit the forecast or rubric text; any who did are labeled |
| 4 | Agreement table and disagreement analysis filed; any adjudicated score labeled as such | Completes the pilot |

Step 3 cannot begin before Steps 1 and 2.

### 3. Forecasts and rules (by reference)

F1 and F2 (claims, thresholds, withdraw conditions), the Hit / Partial / Miss / Unscorable / Withdrawn rules, the valid-session definition, baseline counting (the Gemini 0/2 is prior data, not counted), and the reviewer-agreement rules are in `Tests/Chrono_Divergence.md` §4 and §4.1. The preregistration record stores a hash of those rows; this file does not carry a second copy, so the two cannot drift apart.

### 4. Allocation (declared in the preregistration record)

The record states which design is used: within-family (default) or between-family (Chrono §4). Terms follow Chrono §4: allocation unit, observation unit, and the independence assumption that holds only under the stated controls.

The independence unit is the (auditor family, case) pair. Each pair runs once across both arms; assignment to arms is by recorded randomization or counterbalancing; each case appears in both arms.

**The filled allocation table lives only in §9.3.** This section states the rule; do not maintain a second copy of the table here.

Default design (Chrono §4, within-family): each family runs both arms on different cases, order counterbalanced (half baseline-first, half pointer-first), each case in both arms, every session isolated and run from the preregistered prompt verbatim. Example shape, not an assignment: 4 families × Cases B and D. Record isolation facts per session (memory state, new chat, no shared project or files). After the runs, report M1 by order position as the carryover check. The between-family alternative is in Chrono §4; use it only if isolation cannot be shown.

### 5. Arms and case material

| Arm | Kit variant | Target n (valid Stage 1) |
|-----|-------------|--------------------------|
| Baseline | Shipped Kit, reconciliation instruction in "How to Use" only | 4 |
| Pointer | One sentence added to the Audit Opening Checklist directing the auditor to the reconciliation check in "How to Use"; exact wording fixed in the preregistration record | 4 |

Cases B and D (or equivalent operator-held variants) are the planted-text design. Answer keys stay outside the repository. Cases A and C are optional and not needed for this pilot's claim. Per-session controls, memory-state recording and validity rules are in Chrono §4.

### 6. Filing

Each batch is filed as a Field_Log (`Status: Unreviewed`, with a row added to the `Tests/Field_Logs.md` index) holding: arm, family, case, controls table including memory state, the full Stage 1 report or a link, the Stage 2 result if run, a validity judgment with reason, and annotations (tool use, over-claims). The first Field_Log cites the preregistration record.

### 7. Scoring and acceptance

| Forecast | Outcome (R1) | Outcome (R2) | Exact agreement? | Disagreement category | Evidence cited |
|----------|--------------|--------------|------------------|-----------------------|----------------|
| F1 | | | | | |
| F2 | | | | | |

Record totals (forecasts made, withdrawn, partial, unscorable). Rubric revision follows only the predeclared triggers in Chrono §4.1.

Report three outcomes separately (Chrono §4.1):

| Outcome | What it establishes | Status for this pilot |
|---------|---------------------|-----------------------|
| Procedurally complete | Steps 1 to 4 ran in order; both forecasts received two independent scores; the agreement table and disagreement analysis are filed; every invalid session, control failure and withdrawn forecast stays visible | Minimum acceptance criterion |
| Scoring agreement observed | Reviewers assigned matching categories | A result to report, not a predetermined success; no percentage threshold |
| Rubric reliability supported | A larger, appropriately designed evaluation supports a stronger reproducibility claim | Not licensed by this pilot |

The pilot is procedurally complete even if the reviewers disagree on every score.

### 8. Explicit non-claims

- No Measured accuracy for divergence forecasts; completion licenses no claim about the pointer.
- No change to FAK-018, Kit text, Spec Gates, or any Unknown status.
- Scoring reproducibility is untested until this pilot completes, and one pilot cannot show forecasting accuracy.
- Filing this file does not start the pilot; Step 1 does.

### 9. Preregistration record (fill to start the pilot)

Until this section is completed and a content hash (or commit) of the frozen rows is recorded, the pilot remains **unstarted**. Fill in order; do not begin sessions until every required field has a value or an explicit deferral.

#### 9.1 Pointer wording (required)

Proposed (one sentence, for the Audit Opening Checklist):

> **Reconciliation:** Before relying on this kit, compare the Derived-from line with the live source versions (see “How to Use — Reconciliation check at audit start”).

Human may accept, edit, or replace. Once chosen, the exact sentence is frozen here and must match the Kit variant used in the Pointer arm.

**Frozen pointer text:** _[empty — fill before first session]_

#### 9.2 Design declaration (required)

| Field | Value |
|-------|-------|
| Design | Within-family (default) / Between-family (alternative) |
| Families planned | |
| Cases planned | (default: B and D or operator-held equivalents) |
| Target valid Stage-1 sessions per arm | 4 |
| Isolation method | (new chat / no shared project or files / memory-state recorded) |
| Order counterbalancing | (describe or “N/A if between-family”) |

#### 9.3 Allocation table (required — 8 distinct pairs for full n)

| Pair | Auditor family | Case | Arm | Order (1st/2nd) | Session ID | Memory state |
|------|----------------|------|-----|-----------------|------------|--------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

If fewer than 8 distinct pairs are available, mark the pilot **exploratory** and record the reduced n. Under Chrono §4 both F1 and F2 then score **Unscorable**, so the reviewers can only agree on Unscorable; that does not test Hit/Miss discrimination. Proceed only if the human accepts that limit.

#### 9.4 Reviewers (required)

| Role | Name / handle | Wrote or audited forecast/rubric text? |
|------|---------------|----------------------------------------|
| Reviewer 1 | | Yes / No |
| Reviewer 2 | | Yes / No |

At least one reviewer must be free of forecast/rubric authorship. Label any entanglement.

#### 9.5 Forecast coverage for remaining branches (Chrono checklist item 9)

| Branch | Forecast declared? | Reason if deferred |
|--------|--------------------|--------------------|
| D1-B (operator habit) | | |
| D1-C (accept low M1) | | |
| D2-A / D2-B (detection path) | | |

A blank reason means **not ready to start**. Checklist item 9 requires a recorded reason for any deferred branch; the human must write one (for example “Out of scope for scoring-reproducibility pilot; may be declared in a later map”). Do not treat silence as a decision.

#### 9.6 Freeze marker

| Field | Value |
|-------|-------|
| Preregistration completed date | |
| Content hash or commit of Chrono §4 F1/F2 rows + Chrono §4 session controls + this §9 (including allocation and design declaration) | |
| Linked from first test-start Field_Log | (FL-… ID) |

---

## Lessons Learned

- 2026-10-14: Grok's draft had the right sequence but copied the frozen forecasts, named the wrong bucket (Field_Logs holds evidence, not protocols), cited the wrong section for revision triggers, and proposed an allocation that violated its own independence rule. Corrected here by reference, not by copy.

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| -- | None | -- | -- | -- | -- |

---

## Auditor Notes & Unknowns

*No Unknowns of this file's own. CD-001 (scoring-rubric stability) is owned by `Tests/Chrono_Divergence.md`; this pilot is its resolution path.*

### Resolution Log

- 2026-10-15: **v0.4** after Claude review of the first preregistration template. Fixes: §4 no longer carries a second allocation table (points to §9.3 only); freeze hash scope expanded to Chrono §4 F1/F2 rows + session controls + this §9; blank forecast-coverage reason means not ready to start (no silent default); under-8-pairs consequence stated plainly (both forecasts Unscorable, Hit/Miss discrimination not tested); version bumped. Prior same day: §9 first expanded from open-items list into a fillable record; editorial trim of Last Audit cell. Pilot remains Proposed / not started until the record is filled and hashed. No Spec Gate or Unknown change. Human-directed.
- 2026-10-14: v0.3: §7 now reports three outcomes separately (procedurally complete / scoring agreement observed / rubric reliability supported) with completion as the only acceptance criterion; §4 requires the record to declare the design. Aligned to Chrono v0.6. Human-directed.
- 2026-10-14: v0.2: allocation section aligned to Chrono v0.5 (counterbalanced order, isolation requirements, carryover check by order position). Contamination affects what the reviewers score, not whether they agree, so the pilot claim is unchanged. Human-directed.
- 2026-10-14: v0.1 filed and registered (Proposed, pilot not started). Drafted by Grok; corrected against Chrono v0.3/v0.4 (forecast copy removed, bucket and cross-reference errors fixed, allocation rebuilt on distinct family-and-case pairs). Human-directed.

---

## Abandoned Paths

- Filing the pilot as a Field_Log: rejected 2026-10-14. Field_Logs is raw run evidence; a protocol there would blur the evidence/doctrine boundary `Field_Logs.md` states.
- Carrying a second copy of F1/F2 in this file: rejected 2026-10-14; two copies of text that freezes at preregistration can drift.

---

## Drift Indicators

- Forecast, scoring or reviewer text copied here instead of referenced.
- Allocation table filled with a (family, case) pair used in both arms.
- Scoring begun before a preregistration record exists.
- Run evidence added to this file instead of a Field_Log.
- Cross-references to Chrono sections that no longer exist after a Chrono renumbering.
