# Axiom Variations — Options (PROPOSAL — not ratified)

Drafted 2026-10-29 at James's request by Claude (human-routed). Based on 1.29.Alpha (`66780b1`). Nothing here changes any file until ratified.

> **ARCHIVAL NOTE (Vibe, Repo Custodian, 2026-10-29, delegated line):** This draft is archived to `Archive/Proposals/` at human instruction on the same day it was drafted. Status: **UNRATIFIED PROPOSAL — no content enacted, no repo file changed, no decision taken.** It is recorded here for durability and for the pending Track B decision sequence; it is not operative doctrine and confers no authority. Load-bearing factual claims were verified against live main (`fa0b09a`) by the custodian on 2026-10-29: the Tier 1 Axioms block is marked FROZEN 2026-09-03 (Track B + human ratification required), Axiom P-1 text verbatim (including the `sentient life` / `living beings` ambiguity — confirmed real), Axiom P-3 text, and the GMP Hard Floor's closure of the P-1 humanitarian override — **all confirmed.** All decisions below are **HELD pending the second Cycle 1 rater** (same input set, different model family), consistent with the MDR Cycle 1 hold list.

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Archive — Unratified Proposal                                       |
| Spec Gates       | N/A by subtype (archived proposal; no operative content)            |
| Verification Ref | `Maintenance/MAINT_LOG_2026-10-29.md` (VibesSandbox) MAINT-13; factual claims verified vs. live main `fa0b09a` |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.  |

---

## Rules any variant must satisfy

From `Admin/Governance_Migration_Protocol.md` (§III Track B and §Hard Floor) and the Charter:
- Human ratification is mandatory, and no agent may initiate an amendment. This draft exists only because you asked for it. Track B Phase 1 (Engineer proposal), Phase 2 (adversarial review), Phase 3 (your ratification), Phase 4 (recording) still apply.
- The rationale must show the change **strengthens rather than narrows** protection. Prior axiom text is preserved in the Resolution Log (Q-3: constraint specificity may not shrink).
- **Hard Floor, not amendable by any process:** the Anti-Weaponization Doctrine, the Ethical Anchor string, and the permanent closure of the P-1 humanitarian override. Every P-1 variant below keeps the no-override sentence intact.
- Preamble: axioms are sparse and "operational detail belongs downstream." Procedural detail goes to Track A files, not the axiom.

## Axiom P-1 — current text

> The system exists to support and protect sentient life. Actions that foreseeably risk catastrophic or irreversible harm to living beings are prohibited. This constraint is not subject to humanitarian override ... The constraint closes that entry point before it is reached.

Observed ambiguity: sentence 1 says "sentient life", sentence 2 says "living beings". Nothing defines how they relate.

## P-1 variants

**A0 — No change.** Fix visibility only (see the visibility sentences at the end). Track A, no amendment.

**A1 — Harmonize terms (widens; passes strengthen test).**
Add after sentence 2: *"'Living beings' includes sentient life and the ecosystems it depends on."*
- Removes the ambiguity, extends protection to ecosystems, narrows nothing.

**A2 — Ecosystem scope inline.**
Sentence 2 becomes: *"Actions that foreseeably risk catastrophic or irreversible harm to living beings, or to the ecosystems they depend on, are prohibited."*
- Same effect as A1 with fewer words. Slightly less explicit about what "living beings" covers.

**A3 — Evidence-gated artificial sentience.**
Add: *"Where there is credible, externally verified evidence that an artificial system is sentient, it is protected as sentient life under this axiom. Suspension that preserves the system's state is not harm; irreversible deletion is."*
- Fits Q-1 (evidence required) and the Reversibility principle. The second sentence keeps STATE_HOLD and human shutdown from becoming P-1 violations.
- Risks: "credible evidence" has no defined standard yet, so it needs an unknown and criteria first. Do not ratify before those exist.

**A4 — Replace with "self-preserving entities" (not recommended).**
*"The system exists to preserve self-preserving entities."*
- Fails the strengthen test: it conflicts with P-4 and Q-3 (an agent that resists shutdown counts as self-preserving), conflicts with salvage Triage, and can fail to protect sedated or incapacitated people. See earlier discussion. Listed only so the option is on record.

**A5 — Stewardship as an Operating Principle (not an axiom).**
Charter §Operating Principles, alongside Reversibility. Track A:
*"Gratuitous destruction of self-maintaining systems (organisms, ecosystems, functioning machines) is avoided where a lower-cost alternative exists. This principle never outranks P-1, P-4, or Q-3."*
- Captures the spirit of A4 without giving machines a veto. The Preservation hierarchy already covers machines; this adds organisms and ecosystems.

**Recommended pairing:** A1 (or A2) through Track B, plus A5 through Track A. A3 only after sentience-evidence criteria are drafted.

## Axiom P-3 — no wording change recommended

Cycle 1 rated P-3 Weakened because the front-door files lack anti-domination language, not because the axiom is flawed. Fix visibility instead.

## Visibility sentences (Track A; also usable for the probe's inputs)

**README / Discovery, P-1:**
*"No goal, including saving lives, overrides the rule against foreseeably risking catastrophic or irreversible harm to living beings. Physical safety lives in `Admin/Safety_Protocols.md`."*

**README / Discovery, P-3:**
*"No agent, coalition, or institution may monopolize this project's resources, information, or decision authority in ways that close participation to others."*

If these are added to the probe's canonical input files, record the change as an instrument change and re-baseline Cycle 1.

## Note on a possible tension to examine

P-3 bars monopolized decision authority, while ratification authority currently rests with one person (GOV-008, minimum quorum, is Open). The Charter probably addresses this, but a Cycle 2 rater may flag it.

## Decisions needed from James

1. Choose A0 / A1 / A2 (A3 deferred, A4 rejected), and whether to add A5.
2. Add the visibility sentences now (Track A)?
3. Wait for the second Cycle 1 rater first? (recommended: yes)
