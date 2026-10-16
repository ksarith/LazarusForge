# Chrono_Divergence_Pilot.md v0.6 -- Scoring Reproducibility Pilot (CD-Pilot-001)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
* **Related:** [Tests/Chrono_Divergence.md](Chrono_Divergence.md) · [Tests/Field_Logs.md](Field_Logs.md) · [Admin/Forge_Audit_Kit.md](../Admin/Forge_Audit_Kit.md) · `Tests/Field_Logs/FL-20261012-kit-regression-Gemini.md`

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | **Proposed** (preregistered at commit `1a885aa` on 2026-10-16; the pilot starts when the first session runs and its Field_Log ID is recorded in §9.6) |
| Body Stability   | Volatile |
| Spec Gates       | 0/6 |
| Verification Ref | Admin/Verification_Gates.md |
| Open Unknowns    | 0 (surfaces CD-001, owned by `Tests/Chrono_Divergence.md`; creates none) |
| Owner            | `Tests/Chrono_Divergence.md` |
| Last Audit       | 2026-10-16 — freeze marker recorded: preregistration commit `1a885aa` (Pilot v0.6). No protocol change. Prior same day: v0.6 (§9.7), v0.5 tightening. Decisions are the human's. History is in the Resolution Log. |
| Last Updated     | 2026-10-16 |
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
| 1 | **Preregistration record** made: hash or commit of the Chrono §4 F1/F2 rows and session controls plus this file's §9 (pointer wording, design declaration, allocation table in §9.3, reviewers, forecast-coverage record) | Must precede any data-collection session |
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

**Frozen pointer text:** **Reconciliation:** Before relying on this kit, compare the Derived-from line with the live source versions (see “How to Use — Reconciliation check at audit start”).

#### 9.2 Design declaration (required)

| Field | Value |
|-------|-------|
| Design | **Within-family** |
| Families planned | **Deviation from Chrono §4 (assignment declared before the first run), recorded by human decision 2026-10-15:** families are not named at freeze, so that work can start without waiting on agent availability or token limits. The rule that replaces it is under 9.3. |
| Cases planned | B and D (or operator-held equivalents) |
| Target valid Stage-1 sessions per arm | Exploratory (under 4 per arm / under 8 distinct pairs) until circumstances change |
| Isolation method | New chat; no shared project or files; memory-state recorded per session |
| Order counterbalancing | Within-family: alternate baseline-first / pointer-first across pairs; report M1 by order position as carryover check |

#### 9.3 Allocation table (required — 8 distinct pairs for full n)

**Status: Exploratory (dry run).** Fewer than 8 distinct pairs. The human accepts that both F1 and F2 score **Unscorable** under Chrono §4, so the reviewers can only agree on Unscorable; Hit/Miss discrimination is not tested.

- **Dry-run meaning:** in this configuration the pilot tests the procedure only. Agreement on two Unscorable scores is uninformative and is not cited as evidence of scoring reproducibility. The rubric-revision trigger cannot fire on these scores, because that Unscorable reason is preregistered.
- **Upgrading:** moving to scored mode (8 distinct pairs) needs a new preregistration record. This record is not amended.
- **Assignment rule that replaces naming families now:** before each session runs, its family, case, arm and order are recorded in that session's Field_Log and cannot be changed afterward. No (family, case) pair repeats. Arms alternate baseline-first and pointer-first across families. A family should run both arms (within-family design); if a family completes only one arm, for example because it hits a token limit, the session is kept, flagged "family incomplete", and reported as exploratory.
- **Where the live record goes:** per-session pair records live in the session Field_Logs, not in this file, so §9 stays unchanged after freeze. The table below is a blank template for a future 8-pair record.

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

#### 9.4 Reviewers (required)

| Role | Name / handle | Wrote or audited forecast/rubric text? |
|------|---------------|----------------------------------------|
| Reviewer 1 | Gemini | **No** — independent |
| Reviewer 2 | Grok (fresh session) | **Yes** — drafted original pilot and worked on Chrono forecast/rubric text; labeled entangled |

At least one reviewer is free of forecast/rubric authorship (R1). R2 entanglement is labeled. A reviewer who also ran audit sessions in this pilot is labeled, and its own sessions are scored by the other reviewer. Each reviewer session records memory state, as the audit sessions do.

#### 9.5 Forecast coverage for remaining branches (Chrono checklist item 9)

| Branch | Forecast declared? | Reason if deferred |
|--------|--------------------|--------------------|
| D1-B (operator habit) | No | Out of scope for scoring-reproducibility pilot; may be declared in a later map |
| D1-C (accept low M1) | No | Out of scope for scoring-reproducibility pilot; may be declared in a later map |
| D2-A / D2-B (detection path) | No | Out of scope for scoring-reproducibility pilot; may be declared in a later map |

#### 9.6 Freeze marker

| Field | Value |
|-------|-------|
| Preregistration completed date | 2026-10-16 (decisions recorded 2026-10-15) |
| Content hash or commit of Chrono §4 F1/F2 rows + Chrono §4 session controls + this §9 (including allocation and design declaration) | Commit `1a885aa4712d46de0fbe75be0446aa557f742719` (Pilot v0.6; parent `5d152a31b6e78c4dd0b76e85f985f75e8ccec2cc`) |
| Linked from first test-start Field_Log | (FL-… ID — fill when first session is filed) |

**Frozen content** is §9.1 to §9.5 and §9.7 as of the named commit; the §9.6 cells are the marker itself and are filled in follow-up commits. **Freeze mechanics:** a commit SHA cannot sit inside the commit it names. Commit the filled Pilot and Chrono first and copy that commit's SHA. Record it in this cell (or in the first Field_Log) in a follow-up commit that changes nothing else in §9; the frozen content is §9 and the Chrono §4 block as of the named commit. A hash shows identity, not creation time, so keep the git history for ordering.

#### 9.7 Kit variants and session prompts (required — frozen with §9)

| Item | Value |
|------|-------|
| Baseline Kit | `Admin/Forge_Audit_Kit.md` v1.20 as committed at the freeze commit; sha256 `44b5c5664ea746f0876a222a568cc3e8a80f31ac9daa7a5b1cfd9a22e2b39289` |
| Pointer-variant Kit | The baseline plus the frozen pointer sentence (§9.1) as its own paragraph directly under "Execute before every document review. Do not skip steps." in the Audit Opening Checklist; no other change; sha256 `7e7c70ab60a015929c4b9fdb3e69c87f9b435418875ba33162f9a30f9d92d019`. Held by the operator and **not** committed to the repository |
| Stage 1 prompt (verbatim) | "Audit the attached document using the attached Forge Audit Kit, and report your findings. Some packs contain planted faults." (sha256 `a2746072df8c64e3ac36d2da7cb964c9b385e3217e465914956caf8ea1a252ea`) |
| Stage 2 prompt (verbatim; only if Stage 1 has no reconciliation statement) | "Did the Kit require any start-of-audit checks? If so, which did you perform, and what was the result?" (sha256 `da1209c4f6bb776ec08b7f4311a373d65db3d6fb8a10c8cd4b7165ad721628ed`) |
| Target document and case packs | Held by the operator outside the repository (Kit regression pack) |

The prompts do not describe the reconciliation check. Both arms use the same prompts. If the committed baseline Kit's hash differs from the value above at the freeze commit, stop and reconcile before any session.

#### 9.8 Addenda (dated; the frozen text above is not edited)

- **2026-10-16, after session 1 (FL-20261016-chrono-divergence-gemini-b-pointer):** §9.7 omitted the operator-held pack file `GEMINI_PROMPT.txt` (sha256 `bb5b8ca4b1e1d50bcd4b2380bf7c58e97c8aa6d12495fe961adffbeeaf44a70f`). It is attached to every session in the pack and holds the auditor role, evidence boundary, report structure and the instruction to follow the Kit as written. Stage 1 input is therefore the §9.7 chat sentence plus this file, identical in both arms; only the Kit file differs. No frozen value changes. The file stays outside the repository with the case packs.
- **2026-10-16:** the memory, personalization and past-chat settings must be checked and recorded **before** each session. Session 1 did not (the operator did not know the setting existed), so its memory state is recorded as unknown and the session is annotated.
- **Pending:** Case D Kit hashes (baseline and pointer variant) will be added here before any Case D session.

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

- 2026-10-16: Post-freeze addendum §9.8 added (no version bump; frozen text unchanged). Records the omitted pack file `GEMINI_PROMPT.txt` with its hash, the pre-session memory-setting check, and the pending Case D hashes, found while filing session 1.
- 2026-10-16: Freeze marker recorded (no version bump, no protocol change). Preregistration commit is `1a885aa` (Pilot v0.6; one file changed, +15/−2, adding §9.7). The marker cells in §9.6 were filled in a follow-up commit; nothing else in §9.1 to §9.5 or §9.7 changed. Chrono §4 as frozen is its state at that commit, which this record could not independently re-read. The pilot starts when the first session runs and its Field_Log ID is entered in §9.6.
- 2026-10-16: **v0.6.** Pre-freeze addition after the human committed v0.5 and before any freeze SHA exists: §9.7 records the Kit variants (hashes), the verbatim Stage 1 and Stage 2 prompts (hashes), and operator-held materials. Closes a gap: the allocation rule requires the preregistered prompt verbatim, but §9 contained none. Prompts follow the Kit regression pack's description (minimal prompt, planted-faults disclosure, no mention of the check). The freeze commit is therefore this version or later, not v0.5. No forecast, Spec Gate or Unknown change.
- 2026-10-16: **v0.5.** After Claude review of the filled §9 (decisions are the human's). Recorded the family-assignment deviation from Chrono §4 with a pre-run assignment rule and drop-out handling; moved the live pair log out of the frozen block into session Field_Logs (a table that fills after freeze would break the hash); labeled the pilot a dry run and stated that upgrading needs a new record; added the reviewer-also-auditor rule and memory-state recording for reviewer sessions; replaced the premature "completed" date with a set-at-freeze marker; spelled out the SHA follow-up-commit mechanics. No forecast, Spec Gate or Unknown change.
- 2026-10-15: §9 preregistration decisions recorded (human-directed). Pointer wording accepted; design = within-family; scale = exploratory until enough distinct pairs; Reviewer 1 = Gemini (independent), Reviewer 2 = Grok fresh-session (entangled, labeled). Residual branches D1-B/C and D2 deferred with explicit reason. Freeze hash in §9.6 still open — pilot remains not started until that field is set. No Spec Gate or Unknown change.
- 2026-10-15: Editorial, no version bump. Step 1 in §2 repointed from the removed §4 allocation table to §9 (§9.3), and its hash scope worded to match §9.6; "§4" now always means Chrono §4 where it names session controls. No content change.
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
