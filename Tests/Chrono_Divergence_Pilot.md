# Chrono_Divergence_Pilot.md v0.1 -- Scoring Reproducibility Pilot (CD-Pilot-001)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
* **Related:** [Tests/Chrono_Divergence.md](Chrono_Divergence.md) · [Tests/Field_Logs.md](Field_Logs.md) · [Admin/Forge_Audit_Kit.md](../Admin/Forge_Audit_Kit.md) · [Tests/Field_Logs/FL-20261012-kit-regression-Gemini.md](Field_Logs/FL-20261012-kit-regression-Gemini.md)

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
| Last Audit       | 2026-10-14 — v0.1 drafted from Grok's pilot draft; corrected against `Tests/Chrono_Divergence.md` v0.3/v0.4 before filing (Claude, human-directed). Not yet audited by a second agent. |
| Last Updated     | 2026-10-14 |
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
3. Independence is per (auditor family, case) pair (Chrono §4 allocation rule), so n per arm is bounded by the number of distinct pairs available.

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

The independence unit is the (auditor family, case) pair. Each pair runs once across both arms; assignment to arms is by recorded randomization or counterbalancing; each case appears in both arms.

| Pair | Auditor family | Case | Arm (Baseline / Pointer) | Order | Session ID | Memory state |
|------|----------------|------|--------------------------|-------|------------|--------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

Example shape (not an assignment): 4 families × Cases B and D, with each family running B in one arm and D in the other, and the two arms balanced within each case.

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

Record totals (forecasts made, withdrawn, partial, unscorable). Rubric revision follows only the predeclared triggers in Chrono §4.1. The pilot succeeds as a method test if Steps 1 to 4 ran in order, both forecasts received two independent scores, the agreement table and disagreement analysis are filed, and every invalid session, control failure and withdrawn forecast stays visible.

### 8. Explicit non-claims

- No Measured accuracy for divergence forecasts; completion licenses no claim about the pointer.
- No change to FAK-018, Kit text, Spec Gates, or any Unknown status.
- Scoring reproducibility is untested until this pilot completes, and one pilot cannot show forecasting accuracy.
- Filing this file does not start the pilot; Step 1 does.

### 9. Open items before start

- Exact pointer wording (one sentence).
- Family and case list sufficient for 8 distinct pairs, or a decision to run exploratory at smaller n.
- Named reviewers and their roles.
- Forecasts for D1-B, D1-C and D2 declared, or the gap recorded with a reason (Chrono checklist item 9).
- Whether D2 detection paths run in the same campaign (optional).

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
