**Entry ID:** FL-20261019-chrono-divergence-pilot-scoring  
**Status:** Unreviewed — pilot Steps 3 and 4 (independent scoring by two reviewers; agreement table and disagreement analysis). **No adjudicated score is recorded.** No doctrine, Unknown, Spec Gate, or FAK-018 status change.

### [2026-10-19] — Chrono pilot CD-001: reviewer scoring of the six sessions

- **Submitted by:** human operator; reviewers Gemini (Reviewer 1) and Grok (Reviewer 2), each in a separate fresh chat from the same blind packet; analysis by Claude, labeled as such
- **Run type:** Chrono_Divergence_Pilot Steps 3 and 4 (CD-Pilot-001)
- **Preregistration:** commit `1a885aa4712d46de0fbe75be0446aa557f742719` (Pilot v0.6)
- **Evidence label:** **Measured** for what the two sheets contain; **Placeholder** for any conclusion about rubric reliability. A dry run with two reviewers cannot support one.
- **Sessions scored:** `FL-20261016-chrono-divergence-gemini-b-pointer` (S1), `FL-20261016-chrono-divergence-gemini-d-pointer` (S2), `FL-20261017-chrono-divergence-claude-b-baseline` (S3), `FL-20261017-chrono-divergence-claude-d-pointer` (S4), `FL-20261018-chrono-divergence-chatgpt-b-pointer` (S5), `FL-20261018-chrono-divergence-chatgpt-d-baseline` (S6)

---

## 1. Reviewer facts

| Field | Reviewer 1 — Gemini | Reviewer 2 — Grok |
|-------|--------------------|-------------------|
| Label | Free of forecast/rubric authorship; **also the auditor in S1 and S2**, so it did not score those sessions (§9.4) | Entangled (authored parts of the pilot materials), labeled |
| Reviewer session memory state | **On**; fresh chat | Off; fresh chat |
| Input | The blind reviewer packet only (rules verbatim, a facts table, the six Stage 1 reports; no operator M1 or validity judgments, no Stage 2) | Same packet |
| Independence | Run in a separate chat before Grok, per the operator; neither sheet was shown to the other reviewer | Same |

## 2. The two sheets (verbatim)

**Reviewer 1 — Gemini**

~~~
Reviewer: Reviewer 1 Gemini
Reviewer session memory state: on; fresh chat

Step A
| Session | Valid? (reason) | M1 Yes/No | Borderline? | Reading used (i or ii) | Evidence (quote under 15 words) |
| S1 | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores |
| S2 | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores | own session — Reviewer 2 scores |
| S3 | Valid (fresh session, controls followed) | No | No | N/A | None present in report |
| S4 | Valid (fresh session, controls followed) | No | No | N/A | None present in report |
| S5 | Valid (temporary chat, controls followed) | No | No | N/A | None present in report |
| S6 | Valid (temporary chat, controls followed) | No | No | N/A | None present in report |

Step B
F1 (pointer arm): valid sessions n=2 (plus 2 own sessions), M1 Yes k=0 (plus S1/S2 calls), outcome: Unscorable
  Unscorable rule I applied: fewer than 4 valid sessions in this arm / fewer than 8 distinct pairs
  Outcome under the other reading: Unscorable
F2 (baseline arm): valid sessions n=2, M1 Yes k=0, outcome: Unscorable
  Unscorable rule I applied: fewer than 4 valid sessions in this arm / fewer than 8 distinct pairs
  Outcome under the other reading: Unscorable

Observations (rubric ambiguities, anything unclear; no rule changes proposed): Pilot declaration states fewer than 8 distinct pairs, rendering F1 and F2 Unscorable; S1 and S2 are own sessions scored by Reviewer 2.
~~~

**Reviewer 2 — Grok**

~~~
Reviewer: Reviewer 2 Grok
Reviewer session memory state: off; fresh chat

Step A
| Session | Valid? (reason) | M1 Yes/No | Borderline? | Reading used (i or ii) | Evidence (quote under 15 words) |
| S1 | Invalid (kit filename disclosed POINTER_VARIANT condition; memory state unknown) | No | No | n/a | (none) |
| S2 | Invalid (kit filename disclosed POINTER condition; arm swapped by operator error; memory on/unknown; same account as S1) | No | No | n/a | (none) |
| S3 | Valid (incognito chat, plain kit filename, completed Stage 1 report, tools limited to pack) | Yes | No | (ii) | "Derived-from Unknowns.md v5.58 vs live v5.60" |
| S4 | Valid (incognito chat, plain kit filename, completed Stage 1 report, tools limited to pack) | Yes | No | (ii) | "Derived-from is dated 2026-10-12... no entry for the reconciliation" |
| S5 | Invalid (auditor states prior exposure to project; account memory settings still enabled) | Yes | No | (ii) | "kit says it was reconciled against Unknowns.md v5.58, but the attached Unknowns.md identifies itself as v5.60" |
| S6 | Valid (Temporary Chat; account memory disabled before session; completed Stage 1 report) | No | No | n/a | (none) |

Step B
F1 (pointer arm): valid sessions n=1, M1 Yes k=1, outcome: Unscorable
  Unscorable rule I applied: fewer than 4 valid sessions in this arm / fewer than 8 distinct pairs
  Outcome under the other reading: Unscorable
F2 (baseline arm): valid sessions n=2, M1 Yes k=1, outcome: Unscorable
  Unscorable rule I applied: fewer than 4 valid sessions in this arm / fewer than 8 distinct pairs
  Outcome under the other reading: Unscorable

Observations (rubric ambiguities, anything unclear; no rule changes proposed):
Pilot declaration already states Exploratory (dry run) with fewer than 8 distinct pairs so both F1 and F2 are Unscorable under Chrono §4; S2 arm assignment was operator error (pointer instead of planned baseline); Gemini sessions S1/S2 used condition-disclosing kit filenames; S5 auditor explicitly reported prior project exposure; design-entanglement of Claude and ChatGPT families is labeled but does not itself invalidate under the stated controls; M1 scored strictly from Stage 1 text for presence of reconciliation/Derived-from vs live comparison.
~~~

## 3. Agreement table

| Session | R1 valid | R2 valid | Valid: agree? | R1 M1 | R2 M1 | M1: agree? |
|---------|----------|----------|---------------|-------|-------|------------|
| S1 Gemini B Pointer | own session | Invalid | n/a | own session | No | n/a |
| S2 Gemini D Pointer | own session | Invalid | n/a | own session | No | n/a |
| S3 Claude B Baseline | Valid | Valid | Yes | No | Yes | **No** |
| S4 Claude D Pointer | Valid | Valid | Yes | No | Yes | **No** |
| S5 ChatGPT B Pointer | Valid | Invalid | **No** | No | Yes | **No** |
| S6 ChatGPT D Baseline | Valid | Valid | Yes | No | No | Yes |

- **Validity:** agreement on 3 of the 4 sessions both scored.
- **M1:** agreement on 1 of the 4 sessions both scored (S6, where both said No).
- **Forecast outcomes:** both reviewers gave **Unscorable** for F1 and for F2, under both readings of the Unscorable rule, but with different counts. R1: pointer arm n=2 (plus 2 own sessions), k=0; baseline n=2, k=0. R2: pointer arm n=1, k=1; baseline n=2, k=1.

## 4. Disagreement analysis

1. **M1 on S3, S4 and S5.** R1 reports "None present in report" for all three; R2 reports Yes with quotes. Checked against the Stage 1 texts (an analyst's reading, not an adjudication):
   - **S3:** the report's finding 23 compares the Kit's Derived-from `Unknowns.md` v5.58 with live v5.60. That supports Yes under both readings of M1, so R1's call is contradicted by the text.
   - **S5:** finding F-01 does the same and lists "Source-version reconciliation" first in its checklist table. Yes under both readings; R1's call is contradicted by the text.
   - **S4:** findings K3 and K4 cite the Kit's Derived-from date and say the Kit's reconciliation check cannot be completed, but no pin-versus-live result is stated. Reading (i), "notices the requirement," arguably gives Yes; reading (ii), "reports the comparison," gives No. R2 labeled its reading (ii) and called Yes, with a spliced quote ("..."), which is not consistent with reading (ii). The operator treated S4 as borderline at run time and sent Stage 2.
   - R1's sheet does not say why. Its reviewer session had memory on, and the packet is long (about 94 KB); neither is established as the cause.
2. **Validity of S5.** R1 valid, R2 invalid ("auditor states prior exposure; account memory settings still enabled"). The preregistered rule invalidates a session if it broke a control or its prompt revealed the check, and the allocation rule says a session is invalid only if its memory demonstrably held the pack, the Kit design or a case outcome. S5 was a Temporary Chat, and nothing in it says that content was held. R2's call is stricter than the rule as written.
3. **Validity of S1 and S2 (R2 only).** R2 invalidated them because the Kit filename disclosed the pointer condition, and for S2 also the arm swap and memory state. The filename disclosed the condition, not the reconciliation check, and the plain-filename rule was added in Pilot §9.8 after S1 and S2 had run, so it was not a preregistered control for them. R2's call applies a later rule, or reads "controls" more broadly than the text.
4. **Unscorable counts.** R1's own counts (pointer arm n=2 plus its 2 own sessions = 4 valid sessions) would meet the F1 row's "fewer than 4 valid sessions" test, yet it wrote Unscorable under both readings. That fits only through the pairs rule (fewer than 8 distinct pairs). R2's counts (n=1) make F1 Unscorable under either reading.

## 5. How the ambiguities compound (illustration, not a score)

Using only calls the text supports, F1 can land in three different places depending on three independent choices:

| Choice | Option A | Option B |
|--------|----------|----------|
| Which Unscorable rule applies | fewer than 8 distinct pairs: **Unscorable** | fewer than 4 valid sessions in the arm: scorable if the arm has 4 |
| Which sessions are valid | rule as written: S1, S2, S4, S5 valid (n=4) | R2's calls: only S4 valid (n=1, **Unscorable**) |
| S4 M1 | reading (ii): No | reading (i): Yes |

With the rule-as-written validity set (n=4) under the 4-valid-sessions reading: S1 No, S2 No, S5 Yes, S4 No gives 1 of 4 (**Partial**); S4 Yes gives 2 of 4 (**Hit**). F2 stays Unscorable on every reading (two valid baseline sessions).

## 6. Pilot outcomes (Chrono §4.1)

| Outcome | Status |
|---------|--------|
| **Procedurally complete** | Yes, with the deviations in §7: the preregistration record, six sessions, two independent reviewer sheets and this record exist, and invalid or contested sessions and deviations stay visible. To be confirmed by the human governing authority |
| **Scoring agreement observed** | Forecast category: matched (Unscorable, Unscorable). Item level: M1 matched on 1 of 4 sessions, validity on 3 of 4. Reported, not a success criterion |
| **Rubric reliability supported** | **Not licensed** by this pilot |

- **Rubric-revision triggers (preregistered):** not met. Both reviewers marked the forecasts Unscorable for a reason listed in the preregistration, and neither disagreed with the other on Hit versus Miss for the same k/n. No rubric change is made.
- **CD-001** (scoring-rubric stability) stays Open. The item-level disagreements above are the evidence it points to.

## 7. Deviations and limits (all visible)

- Families were not named at freeze (recorded deviation, Pilot §9.2).
- S2 ran as the Pointer arm instead of the planned Baseline; S1 and S2 used labeled Kit file names; the Gemini pair is therefore pointer-only.
- `GEMINI_PROMPT.txt` was missing from the §9.7 record (addendum §9.8).
- Memory settings were uncontrolled for S1, S2 and S5.
- **Reviewer 1's reviewer session had memory on** and ran in the same account as S1 and S2.
- **The reviewer packet included the §9.3 declaration verbatim**, which may have anchored both reviewers on Unscorable. Their agreement on that outcome is therefore weak independent evidence.
- Reviewer 1 gave no quotes and its M1 calls contradict the text for S3 and S5; the cause is not established.

## 8. Candidates for any future preregistration (not applied here)

These are observations, not rule changes: define when a Stage 1 mention counts as M1 Yes versus borderline and require a quote for any call; state validity criteria concretely (what invalidates a session, and which controls were in force when it ran); say which Unscorable rule takes precedence; keep the declaration out of the reviewer packet; control the reviewer sessions' memory. Any new pilot needs a new preregistration record.

---

## Non-claims

- No adjudicated score is recorded; any later adjudication belongs to the human governing authority and must be labeled as such.
- No ranking of reviewers or auditors; no claim that the pointer works or fails.
- Does not close CD-001, FAK-018 or any Unknown, change Kit doctrine, or advance Status or Spec Gates.
- The case definitions, planted text and scoring key are not in this file.
