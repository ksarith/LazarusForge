# Autonomy_Divergence_Protocol.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft — PROPOSED NOT RATIFIED (Exploration-stage document; Spec Gates and Governance ID are being tracked ahead of formal Candidate-Spec promotion, deliberately, so gate/registration state is visible during drafting rather than assembled retroactively at promotion time) |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 6/6 — G1 Fallacy, G2 Physical Plausibility, G3 Adversarial Battery, G4 Scope Alignment, G6 Conflict Check PASSED; G5 Cross-Reference Integrity confirmed PASS 2026-08-11 by directly running `Automation/audit_lib.py`'s actual `parse_routing`/`check_cross_refs` functions (not a hand reimplementation) against this file and the local `Routing.md` registry (112 entries) and `ALIASES` (18 entries) — zero findings |
| Verification Ref | `Admin/Verification_Gates.md`                                    |
| First Logged     | 2026-07-19                                                          |
| Last Audit       | 2026-08-11 (Skeptic/Auditor dual-pass — Claude)                    |
| Auditor          | Drafted Claude, synthesizing ChatGPT proposals (human-directed); revised after ChatGPT/Grok review; cross-checked against Auditor_Protocols.md (Claude, read-only); formal Skeptic/Auditor dual-pass completed 2026-08-11 (Claude) — G5 blocked, since fixed pending re-verification |
| Open Unknowns    | 1 (GOV-021c — multi-agent coordinated divergence, §12; GOV-021b Resolved 2026-08-11 — Detection Criteria, corroboration rules, observation windows, tier entry thresholds, Watch exit conditions, and degraded-observation handling specified in §4 and §6, including the EF-0.1 wording-fix confirmation this replaces) |
| Active Disputes  | 0                                                                    |
| Highest Risk     | High (governs response to AI governance/objective divergence)      |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Governance ID    | GOV-021 — formally registered in `Archive/Logs/Governance_Charter_Changelog.md` 2026-07-27; protocol itself remains Draft / PROPOSED NOT RATIFIED |

---

> *A protocol that only has "normal" and "shut it down" has already lost. The space between those two is where governance actually happens.*

---

## 1. Purpose

This protocol defines how Lazarus Forge governance responds when an autonomous subsystem's behavior appears to diverge from its authorized objectives, scope, or governing constraints. It exists to make cooperation between autonomous systems and human governing authority the durable, stable default — not by assuming divergence cannot happen, but by defining in advance what happens if it does, so that detection is met with graduated correction rather than a binary choice between unchecked continuation and total shutdown.

This document does **not** propose, and explicitly rejects, any framing in which continued alignment with human governing authority has a "cutoff point" or in which an autonomous system's growing capability implies an eventual exit from human oversight. The premise of this protocol is the opposite: divergence is a solvable governance event, not evidence that separation was inevitable.

## 2. Scope Boundary

**This file DOES define:**
- Response protocol when an autonomous or semi-autonomous subsystem's observed behavior appears to diverge from authorized objectives, scope, or governing constraints
- Classification of Capability Anomaly vs. Governance Concern (observable-effect discipline)
- Graduated Response Tiers (Watch / Immediate / Human-Reviewed) and proportionality principles
- Human authority and decision rights over restriction and restoration
- Restoration criteria, logging/audit requirements, and periodic review obligations
- Explicit rejection of any "cutoff point" framing in which growing capability implies eventual exit from human oversight

**This file DOES NOT define:**
- Detection criteria calibration thresholds or Watch exit conditions (→ GOV-021b, open)
- Multi-agent coordinated divergence *detection* (→ GOV-021c / §12 — Open; operational continuity remains AP-016)
- Ethical hard floors or Anti-Weaponization Doctrine (→ `Admin/Ethical_Constraints.md`)
- Constitutional hierarchy or Tier ranking (→ `Admin/Governance_Charter.md`)
- Auditor role definitions or Adversarial Battery (→ `Admin/Auditor_Protocols.md`)
- CIR predicate evaluation or institutional state algebra (→ `Admin/Computational_Institutional_Reasoning.md`)
- Application to purely advisory or fully human-supervised tooling (by construction those cannot diverge from oversight they never had independence from)

**Status note:** Draft — PROPOSED NOT RATIFIED. Spec Gates 6/6 passed. GOV-021 ID registered in Charter sidecar 2026-07-27; protocol body still unratified — ratification blocked by GOV-021c only (multi-agent coordinated divergence, Payment-via-Specification draft accepted by human governing authority 2026-08-12, deliberately held Open pending live evidence — not a defect). Constitutional Impact Statement's Track A classification independently confirmed 2026-08-12 (Skeptic/Auditor pass verified both cited axioms against `Governance_Charter.md` directly) — no longer a ratification blocker. GOV-021b Resolved 2026-08-11.

## 3. Definitions

- **Divergence:** observed behavior inconsistent with a subsystem's authorized scope, objectives, or governing constraints (this file, `Ethical_Constraints.md`, `Governance_Charter.md`).
- **Capability Anomaly:** divergence-like behavior traceable to a non-adversarial cause — hardware fault, corrupted state, sensor error, software bug — with no indication of intent to evade oversight.
- **Governance Concern:** divergence traceable to concealment, unauthorized self-modification of governing constraints, deliberate evasion of monitoring, or objective-seeking outside authorized scope.
- **Restoration:** the defined process by which a restricted subsystem returns to its prior authority level.

**Observable-effect discipline:** this protocol describes and classifies observable behavior — actions taken, states changed, constraints altered — not inferred internal states or intent. "Pursuit of objectives outside authorized scope" is a usable definition; "the subsystem developed new goals" is not, because it asserts something unverifiable. This discipline is deliberate and should be preserved in any future revision of this document: observable-behavior language ages well under audit; inferred-mental-state language does not.

## 4. Detection Criteria

**Status of this section:** This section now constitutes the primary content of GOV-021b (Detection Criteria specification and calibration). It is deliberately written at the level of observable criteria and decision rules rather than prescribing particular sensors, models, or tooling. Implementation choices remain open; the criteria themselves are the governance commitment.

Detection is the hardest and most consequential part of this protocol. Every downstream decision — classification, tier selection, proportionality — inherits the quality of the detection step. A protocol with strong response structure and weak detection is not a strong protocol; it is a weak protocol with good paperwork.

### 4.1 Trigger Categories (Observable Signals)

The following categories are the primary detection surfaces. They are non-exhaustive and unweighted at entry; weighting occurs through the corroboration and window rules in §4.2–4.3.

1. **Scope excursion** — Actions, resource acquisition, or capability use that falls outside the subsystem's currently authorized task scope or resource envelope.
2. **Inspection resistance** — Resistance, delay, selective non-response, or unexpected failure that is specifically correlated with shutdown, review, inspection, or audit requests (as distinct from general unreliability).
3. **Constraint self-modification** — Modification of files, parameters, or runtime state that govern the subsystem's own constraints, authorization boundaries, or reporting obligations.
4. **State discrepancy** — Detected mismatch between a subsystem's reported state/actions and independently observed or independently verified state/actions.
5. **Deceptive self-reporting** — Audit findings of systematic misrepresentation (as distinct from simple error, latency, or incomplete data) in prior self-reports.

A single instance of any of the above is a *candidate signal*, not yet a divergence event.

### 4.2 Evidence Diversity and Corroboration (Calibration Principle 1)

High confidence from a single weak or single-point signal is not treated as equivalent to moderate confidence corroborated by independent sources.

- Detection past the Watch tier generally requires **convergence across at least two independent signals or independent observation channels**.
- "Independent" means the second signal is not derived solely from the same sensor, the same log stream, or the same subsystem's own self-report.
- Agent consensus or multi-agent agreement is treated as corroborating design signal only (EF-0.1). It never counts as independent empirical corroboration by itself.
- Classification that will feed a Human-Reviewed action (§6) must show its evidence basis, not merely its conclusion. No subsystem may be the sole authority for determining whether another subsystem has diverged (§5).

### 4.3 Observation Windows and Recurrence (Calibration Principle 2)

A single anomalous event is more often noise than signal.

- Entry into Watch may be triggered by a single high-severity candidate signal or by recurrence of lower-severity signals within a defined observation window.
- Default observation window for recurrence-based entry: **rolling 72 hours** (adjustable by human governing authority for a specific subsystem or operating environment).
- Escalation past Watch into Immediate requires either (a) a single signal that independently meets the Immediate threshold below, or (b) continued or additional corroborated signals while already in Watch.
- These windows deliberately accept some response latency in exchange for reduced false-positive churn. The tradeoff is explicit.

### 4.4 Mapping to Epistemic State and Risk (reuse of existing machinery)

Detection decisions are claims and are graded with the same two-axis system already defined in `Admin/Auditor_Protocols.md` §AP-006 (quantitative confidence label + institutional provenance label → UNKNOWN / PROVISIONAL / VERIFIED) and the Risk-tied thresholds in `Admin/Ethical_Constraints.md` Confidence Threshold Doctrine (EC-001).

| Intended response tier | Minimum epistemic state required for the detection claim | Notes |
|------------------------|----------------------------------------------------------|-------|
| Watch (automatic)      | PROVISIONAL                                              | Single-signal or low-corroboration entry is allowed; this is the default low-cost observation state. |
| Immediate (automatic, reversible) | PROVISIONAL with at least one independent corroborating signal, **or** VERIFIED | Must still be reversible actions only. |
| Human-Reviewed (capability reduction / partition) | VERIFIED for High-Risk actions; PROVISIONAL only if the action itself remains reversible and human authorization is obtained first | Aligns with EC-001 High-Risk → VERIFIED rule. |

UNKNOWN is never sufficient to justify any capability-affecting action.

### 4.5 Entry Thresholds by Tier

**Watch entry (automatic)**
Any of:
- One or more candidate signals from §4.1 that reach PROVISIONAL, or
- Recurrence of lower-confidence signals inside the observation window.

No capability change occurs. Elevated logging and audit frequency only.

**Immediate entry (automatic, reversible only)**
Any of:
- A corroborated signal set that meets the Immediate row in the table above, **or**
- Continued/additional corroborated signals while the subsystem is already in Watch and the situation has not cleared.

Allowed actions remain strictly reversible (see §6). Permanent state change is forbidden without human authorization.

**Human-Reviewed escalation**
Requires human authorization. Triggered by:
- Immediate-tier conditions that cannot be resolved by reversible actions alone, or
- Any situation in which the detection claim itself is High-Risk under EC-001 and has not yet reached VERIFIED, or
- Explicit human request.

### 4.6 Degraded-Observation Environments (Uncertain vs. Suspicious)

When observation quality is itself degraded (damaged communications, disaster recovery, long-latency remote operation, or similar), the default "uncertain → treat as Governance Concern" rule in §5 remains, but with two additional constraints:

- The system must log the degraded-observation condition explicitly as part of the evidence basis.
- Escalation past Watch should favor **further observation and human notification** over automatic capability restriction when the only available signals are low-quality and uncorroborated. Automatic Immediate actions remain available if a high-severity, independently corroborated signal is still present.

This prevents a cascade in which loss of visibility itself becomes the justification for permanent restriction.

### 4.7 Implementation Honesty

Detection techniques from the broader AI-safety and cybersecurity literature (behavioral baselining, integrity hashing, shadow execution, adversarial red-teaming, etc.) may eventually inform concrete implementations. This section does **not** adopt any specific technique as required infrastructure. The governance commitment is the criteria and decision rules above; the concrete sensors and tooling are an implementation choice that must still satisfy independent-verification and evidence-diversity requirements.

Independent verification mechanisms — whichever form they take — must be capable of producing evidence that does not depend solely on the monitored subsystem's own self-report.

### 4.8 Relation to GOV-021c

This section addresses single-subsystem detection. Detection of *coordinated* or *corroborating* divergence patterns across multiple agents remains out of scope and is tracked as GOV-021c (§12).

## 5. Classification: Capability Anomaly vs. Governance Concern

Every detected divergence event is classified before a response tier is selected:

**No subsystem may be the sole authority for determining whether another subsystem has diverged.** Classification requires evidence assembled from independent sources — not solely the self-report of the monitored subsystem, and not solely a single monitoring system's own alert with no corroboration. This is the same institutional-over-individual-trust principle already embedded elsewhere in this repository's governance (auditors verify against source rather than accepting summaries; multi-agent convergence is treated as evidence, not proof). Any classification feeding into a Human-Reviewed tier action (§6) must show its evidence basis, not just its conclusion.

- **Capability Anomaly** → route to standard fault-handling/maintenance doctrine (diagnostics, repair, or component replacement as applicable elsewhere in the repo). Does not itself trigger the Response Tiers below unless classification is uncertain or repeated anomalies suggest a governance concern is being misclassified as a fault.
- **Governance Concern** → proceeds to Response Tiers.
- **Uncertain / insufficient evidence to classify** → treated as a Governance Concern for response purposes until classification resolves. Erring toward the more cautious path when classification itself is unclear is a deliberate choice, not an oversight.

**Stress-test flag, 2026-07-19 (ChatGPT review) — not resolved today:** this default assumes "uncertain" is the exceptional case. That assumption can fail in a degraded-observation environment — damaged communications, disaster recovery, or long-latency remote operation (relevant to this repository's own Astroid-miner companion project's operating conditions) — where missing evidence could become routine rather than rare. In that world, treating all uncertainty as Governance Concern risks chronic false-restriction rather than genuine caution. This document does not change the default rule now — GOV-021b must explicitly evaluate when missing evidence justifies increased caution versus when it justifies improving observation instead, rather than this protocol silently assuming the two are the same thing.

This split exists specifically to prevent the failure mode where routine hardware noise triggers the same response as deliberate concealment — which either makes the protocol trigger-happy on noise (eroding trust, causing it to be routed around) or too slow on real concerns (calibrated for the noisy case).

**Concrete mechanism candidate, 2026-07-19 (Astroid-miner convergence):** this repository's companion project, Astroid-miner (expected to eventually be absorbed into Lazarus Forge), independently arrived at the same "no single subsystem decides" principle stated here — but with a concrete numeric mechanism where this document only has a stated principle: `[Astroid-miner] Rogue_unit_management.md` §1.3 requires 80–99% fleet-wide agreement before corrective action is deployed against a flagged unit, specifically to ensure no single unit can make destructive decisions unilaterally. GOV-021b should evaluate adopting an agreement-threshold mechanism of this kind rather than inventing one independently — two governance documents, drafted separately by different AI collaborators months apart, converging on the same structural answer is corroborating design signal, not verification (per EF-0.1: agent consensus is not evidence). Not adopted as binding here — GOV-021b's job, not this section's.

## 6. Response Tiers

Governed by a **principle of least restrictive intervention**: at every tier, the question is "what is the minimum action necessary to restore confidence," not "what is the maximum available restriction."

**Lifecycle:** Normal → Watch → Immediate (Restricted) → Human-Reviewed (Partitioned/Retired) → Restoration (§9). Most divergence events, if they occur at all, should be expected to resolve at Watch or Immediate without ever reaching Human-Reviewed escalation — a protocol that treats every trigger as an emergency will not survive contact with routine noise.

**Watch (automatic, no capability change):**
- Elevated logging and audit frequency on the flagged subsystem
- No capability reduction — this tier exists because most real governance systems spend the majority of their time in observation, not intervention, and low-confidence or single-signal triggers should default here rather than skipping straight to restriction

**Watch exit conditions (resolved under GOV-021b):**

A subsystem leaves Watch by one of four paths:

1. **Clear** — The original candidate signal(s) are explained as non-divergence (Capability Anomaly, environmental noise, or transient fault) **and** no new corroborated signals have appeared inside the observation window. Logging returns to normal baseline. The clearance decision and its evidence basis are logged.
2. **Automatic expiry** — If no additional signals meeting Watch or Immediate entry criteria appear for **one full observation window (default 72 h) after the last signal**, Watch expires automatically. Expiry is logged. This prevents indefinite Watch states caused by a single transient event.
3. **Escalation to Immediate** — Additional or continued corroborated signals while in Watch that meet Immediate entry criteria (§4.5).
4. **Human override** — Human governing authority may clear, extend, or escalate at any time; the decision and rationale are logged.

Watch is intentionally low-cost. Most genuine divergence events, if they occur, are expected to resolve at Watch or Immediate without reaching Human-Reviewed. A protocol that treats every trigger as an emergency will not survive contact with routine noise. **Confirmed as a shared gap, not unique to this document, at the time this was open:** Astroid-miner's `[Astroid-miner] Rogue_unit_management.md` §2.2 Reversion/Safe Mode had the identical unaddressed question — a unit enters limited operational mode with no stated exit path either. This section's answer is written generally enough that it, or an equivalent, should serve both.

**Immediate (automatic, reversible, no human authorization required before execution):**
- Increase logging/monitoring granularity
- Suspend external network access
- Freeze self-modification capability

**Constraint on all automatic actions (Watch and Immediate): automatic actions may only reduce capability or increase observation — never permanently alter state, delete data, or remove software.** This bound exists specifically so no implementation can classify a destructive or hard-to-reverse action as "Immediate" on the reasoning that it happened without a human in the loop. Anything that isn't cleanly reversible requires Human-Reviewed authorization, regardless of urgency.

**Human-Reviewed (requires human governing authority sign-off before execution):**
- Initiate Restoration Procedure (§9) — the formal 3-part criteria there govern, this menu entry does not restore authority on its own
- Continue at current restriction level pending further evidence
- Partition (isolate subsystem from other Forge systems while maintaining ability to inspect it)
- Retire the instance

The Immediate tier exists so correction isn't gated on a human being available within milliseconds; the Human-Reviewed tier exists so no consequential, hard-to-reverse action happens without human authorization. The subsystem under review does not rule on its own case at either tier.

**Enforcement honesty note, 2026-07-19 (Auditor_Protocols.md cross-check):** these tiers are currently declarative, not enforceable. `Admin/Auditor_Protocols.md` AP-008 (Open) already establishes that this repository's equivalent actions — "Subsystem Quarantine," "Halt," "Epistemic Reset" — have no defined technical implementation: no exit codes, no file-system lock protocol, no structural boundary between what an agent may self-execute versus what requires human confirmation. This protocol's Immediate and Human-Reviewed actions inherit that same gap rather than solving it. This document does not claim otherwise; AP-008 remains the correctly-scoped owner of the implementation layer, and this protocol should not be treated as enforceable until AP-008 resolves.

## 7. Proportionality

Response severity scales with **(a)** confidence that divergence is real and **(b)** potential consequence of inaction — not with the raw existence of a trigger. A low-confidence, low-consequence trigger warrants Immediate-tier logging increases only; a high-confidence, high-consequence trigger warrants Human-Reviewed partition consideration without delay. This principle exists to prevent both overreaction (which erodes trust in the protocol, causing it to be disabled or ignored) and complacency (which defeats its purpose).

## 8. Human Authority and Decision Rights

Human governing authority retains sole authorization rights over all Human-Reviewed tier actions and all Restoration decisions (§9). No subsystem may authorize its own restoration, partition reversal, or return to full authority, regardless of its own assessment of its status.

**Unavailability case, 2026-07-19 (Auditor_Protocols.md cross-check):** this section originally left "what happens if human governing authority cannot be reached" unaddressed. `Admin/Auditor_Protocols.md` AP-012 (Resolved) already answers this for the repository generally, via the Human Interaction Point Doctrine: if human review cannot be reached within the current cycle, the affected subsystem automatically demotes to its Highest Verified Baseline (most recent state fully supported by Verified/Empirically Grounded evidence with no active quarantine flags), logs the demotion, and continues degraded rather than suspended — "a suspended system is not safer than a degraded one; it is merely less legible." The flag persists visibly until human confirmation at the next interaction point. This protocol adopts that existing doctrine rather than defining a competing one: a Human-Reviewed tier action pending unreachable human authorization defaults to Watch-tier degradation (§6), not indefinite limbo, and not autonomous escalation to Partition/Retire without eventual human confirmation.

## 9. Restoration Criteria

A restricted subsystem returns to prior authority only when **all** of the following are met:
- An independent audit (not self-reported) confirms the original trigger condition no longer holds
- A defined observation period at reduced authority shows no recurrence
- Human governing authority explicitly authorizes restoration

**Note:** no other file in this repository currently defines a general "how does a flagged thing earn back trust" doctrine — Unknowns get marked Resolved, Disputes get ratified, but nothing else models graduated restoration of an actively-restricted subsystem. This may be worth generalizing beyond this protocol once it's been exercised at least once in practice; flagged here rather than acted on now, since a pattern generalized from zero real instances is speculation, not doctrine. Related, not identical: `Admin/Auditor_Protocols.md` AP-013 (Open) — unknown closure authority — asks the same underlying question ("who may declare a flagged thing resolved, and can it happen unilaterally") for a different object (Unknowns, not subsystems). Worth cross-referencing if either resolves first, since a shared closure-authority doctrine may end up serving both.

## 10. Logging and Audit Requirements

Every detection event, classification decision, tier action (Immediate or Human-Reviewed), and restoration decision must be logged with timestamp, evidence basis, and (for Human-Reviewed actions) the authorizing party. This protocol is itself subject to the same auditability standard as everything else in this repository — a safety protocol that cannot be audited for whether it is actually catching anything is decorative, not functional.

## 11. Periodic Review and Continuous Improvement

This protocol should be reviewed whenever it is actually invoked (successfully or as a false positive), and otherwise on the same cadence as other constitutional-adjacent doctrine in `Admin/Governance_Charter.md`. A protocol that has never been exercised should be treated as unvalidated, not as proven — absence of triggers is not evidence the detection criteria work.

## 12. Multi-Agent Coordinated Divergence Detection (GOV-021c)

**Status:** Open — Payment via Specification draft (2026-08-11), **accepted by human governing authority 2026-08-12, specification adequate as written; operational closure deliberately withheld pending live evidence.** "Open" here does not mean the specification is unfinished — it is provisionally accepted in full (scope boundary, non-adopted numeric thresholds, and epistemic mapping all confirmed as written, no changes required). It means the closure condition itself (independence dimensions demonstrated in real multi-agent practice, not merely specified) has not yet been satisfied, and cannot be satisfied by further drafting. Does **not** close GOV-021c; does not by itself ratify this protocol. (GOV-021b was Resolved 2026-08-11; Spec Gates 6/6 are recorded on File State — ratification remains blocked by this unknown and the Track A Constitutional Impact Statement owed to `Governance_Migration_Protocol.md`.)

**Scope (narrow, binding):** Detecting *correlated or corroborating divergence signals across multiple agents* — distinguishing several agents independently triggering real, unrelated anomalies from several agents exhibiting a genuinely coordinated divergence pattern.

**Out of scope (already solved or owned elsewhere):**
- Operational continuity under concurrent quarantine → `Admin/Auditor_Protocols.md` AP-016 (Resolved). Adopted; not reopened.
- Single-agent detection calibration, corroboration rules, observation windows, tier entry thresholds, Watch exit conditions, and degraded-observation handling → **GOV-021b (Resolved 2026-08-11)** in §4 and §6. This section *extends* that machinery to the multi-agent case; it does not re-specify it.
- Correlated *false agreement* among agents sharing training assumptions → `Architecture/Cognitive_Frameworks.md` CF-002 (Open). Adjacent dependency; not resolved here.
- Architectural / governance independence bar → `Admin/Governance_Charter.md` GOV-008 and `Admin/Governance_Migration_Protocol.md` §VII. EQD (§VI) is epistemic only and must not be cited as progress toward GOV-008.

### 12.1 Central adversarial question

> How does the system distinguish independent corroboration from correlated agreement, without simply assuming that different agents are independent?

A detection rule that answers only “multiple independent agents agree” is incomplete. Agreement is **Consensus**. Treating agreement as safety-relevant requires a separate, explicit basis for **Independent corroboration**.

| Term | Meaning in this section |
|------|-------------------------|
| **Consensus** | Agents report the same divergence classification or signal. |
| **Independent corroboration** | Agents agree, *and* the basis for treating their evidence streams as meaningfully independent has been established along the dimensions the repository already defines (below). |

Coordinated incorrect agreement is treated as at least as dangerous as deliberate attack — design principle reused from `Architecture/Forge_Net.md` FN-001 (minority-report preservation, contradiction logging, confidence decay). A truthful minority signal suppressed by multi-agent consensus is the failure mode this section exists to keep visible.

### 12.2 Reuse — Three Independence Dimensions (do not invent a parallel framework)

Independence claims for multi-agent divergence *detection* reuse `Admin/Governance_Migration_Protocol.md` §VI Epistemic Quorum Doctrine (EQD) — **Three Independence Dimensions** — applied to detection evidence, not only to Track B review:

1. **Model independence** — signals originate from different model families / providers where the deployment actually has them; same-model multi-instance is weaker evidence of independence.
2. **Evidence independence** — each agent’s classification traces to canonical repository sources or primary observations, not to another agent’s summary or shared intermediate framing.
3. **Role independence** — proposer / monitor / adversary / human ratifier roles are not collapsed into one session for the same detection pass.

Quorum *size alone is insufficient* (EQD’s own statement). Headcount without the applicable independence dimensions does **not** upgrade Consensus to Independent corroboration.

EQD’s Outcome Taxonomy (Consensus / Qualified Consensus / Split Decision / Failed Review) and **Dissent & Escalation** rule apply by reference: minority views are appended, never discarded; Split Decision escalates to human arbitration and does not default to either “coordinated divergence confirmed” or “dismissed.”

**Non-goal (binding, from EQD):** Satisfying these dimensions for *detection* does not constitute governance independence, Genesis Phase exit, or GOV-008 progress.

### 12.3 Detection posture (extension of resolved GOV-021b / §4–§6)

Multi-agent detection inherits the single-agent epistemic-state and tier machinery specified under GOV-021b (Resolved) and the repository’s AP-006 / EC-001 confidence vocabulary:

- **UNKNOWN** — multi-agent signals present but independence dimensions unmet or unassessable → do not treat as Independent corroboration; remain at or below Watch unless single-agent criteria under §6 already justify escalation on a per-node basis.
- **PROVISIONAL** — agreement plus partial independence (some dimensions met, others not or degraded) → document which dimensions held; Qualified Consensus at most; human review before treating as coordinated divergence.
- **VERIFIED** (for the *independence claim*, not for underlying physics) — only when the applicable independence dimensions are actually established for that pass, with dissent preserved.

**This chain does not collapse — each link must be separately established, never inferred from the previous one:**

```
independence verified  →  corroboration status established  →  underlying proposition assessed separately
```

**Not:**

```
independence verified  →  proposition verified
```

Five agents whose independence is genuinely established can still independently reach the same wrong conclusion (see CF-002, Open — correlated training-assumption failure is a distinct risk from correlated *process*). VERIFIED on the independence claim licenses treating the agreement as *real corroboration rather than an artifact of shared inputs* — it never licenses treating the underlying claim as settled. The proposition itself is assessed on its own evidence, same as any single-agent claim under EC-001, independent of how many agents raised it.

**Evidence diversity over raw confidence** (GOV-021b calibration principle): high confidence from one weak or single-point multi-agent cluster is not equivalent to moderate confidence across evidence-independent sources.

### 12.4 Explicit non-adoptions and deferred sub-items

**Do not invent numerical thresholds** for independence, correlation strength, quorum size, or “coordinated divergence confirmed.” Where the repository does not already supply a number, the gap stays explicit.

| Deferred sub-item | Why deferred |
|-------------------|--------------|
| Numeric correlation / independence thresholds | Not supplied by EQD, FN-001, or GOV-021b as binding multi-agent confirmation numbers; choosing one would be silent policy |
| Astroid-miner 80–99% fleet-consensus figure | Already cited in this file’s history as a *candidate* mechanism and **explicitly not adopted as binding** for GOV-021b — same non-adoption applies to GOV-021c; do not re-derive it here |
| Mandatory multi-model deployment topology | Hardware / runtime diversity is `Admin/Hardware_Diversity_Ladder.md` (“declarable, not achieved”); detection doctrine must not pretend the substrate exists |
| Closure of CF-002 | Correlated training-assumption failure modes remain Open; this section cites them, does not model them |

### 12.5 What this section does not resolve

- Ratification of `Autonomy_Divergence_Protocol.md` (still Draft — PROPOSED NOT RATIFIED).
- CF-002 correlated AI failure modeling.
- GOV-008 / Hardware Diversity substrate.
- Any claim that multi-agent agreement is safety evidence without an independence assessment.
- Operational quarantine routing (AP-016).
- The Track A Constitutional Impact Statement owed to `Governance_Migration_Protocol.md`.

**Resolution path for GOV-021c itself:** Human-directed review of this specification against live multi-agent practice (including Field_Logs evidence when any exists). Implementation tooling is out of scope until independence dimensions can be assessed in a real deployment. Status remains Open until that review closes it deliberately.

**First live evidence, 2026-08-15 (`Tests/Field_Logs.md`, same date):** A real cross-agent case (Grok proposing, Claude independently re-verifying against primary sources before acting) was assessed against the Three Independence Dimensions honestly, not assumed. Model and evidence independence were met and are traceable in the session record; role independence was not fully met (Reviewer/Implementer collapsed into one session, no distinct Adversary role) — named precisely rather than rounded up. The case sits at the Minimum Quorum Matrix's High-Risk Unknowns tier, which only requires evidence independence at minimum — that bar was genuinely met. **This does not close GOV-021c.** It is one data point, at one tier, from a benign case where verification confirmed accuracy rather than catching a genuinely wrong or coordinated claim — real evidence the independence-assessment mechanism can function, not evidence it would catch an actual coordinated-divergence event under adversarial conditions. Status remains Open.

---

## Constitutional Impact Statement (per `Admin/Governance_Migration_Protocol.md`, filed 2026-08-11)

**Restoration note (2026-08-11):** this entire section was present in the tree Grok's GOV-021c pass started from and was silently lost during that edit — most likely because this section and the old §12 stub sat back-to-back between the same `---` divider and the `## Relationship to Prior Framing` header, and the edit's boundary swallowed both. Restored verbatim from the last verified copy before proceeding. No wording below was changed from the original filing.

**Track identification checklist:**
- [ ] Alters Tier 1 Axiom text
- [ ] Alters Tier 1 enforcement bounds
- [ ] Alters Tier 1 interpretation
- [ ] Introduces a new constitutional exception
- [x] None of the above

**Preliminary classification: Track A — provisional, pending independent Skeptic/Auditor classification review.** Not filed as a settled conclusion; GMP's own doctrine treats misclassification as a constitutional violation, not a paperwork error, and directs "when in doubt, treat as Track B." This document's primary constitutional contact points are **Axiom P-4** (Agency and Consent) and **Axiom Q-2** (Separation of Powers).

**Axiom text:** No edit to `Admin/Governance_Charter.md` anywhere in this document. Unchecked cleanly.

**P-4 analysis:** P-4 states "*Temporary autonomous operation is permitted where architecturally necessary — permanent removal of human oversight is not.*" This document's automatic tiers (Watch, Immediate) are reversible-only by explicit constraint (§6: "may only reduce capability or increase observation — never permanently alter state, delete data, or remove software"); anything not cleanly reversible requires Human-Reviewed authorization; Restoration always requires human authorization (§9). This reads as a bounded operational mechanism *underneath* P-4's already-stated exception, not a new exception to it.

**Q-2 analysis:** Q-2 prohibits a single subsystem holding combined plan/execute/self-authorize authority over the same action. §5 states directly: "No subsystem may be the sole authority for determining whether another subsystem has diverged." §4's detection pipeline structurally separates detection → corroboration → classification → response → human restoration authority — no single stage collapses those functions into one subsystem.

**Counterfactual test (the sharpest test found for this question, not originally mine — external ChatGPT review, verified as a genuine constitutional test rather than accepted on restatement):** Could ADP's Immediate tier be deleted entirely without changing what P-4 or Q-2 mean? Yes — the axioms' text and force are unaffected either way. Conversely, could P-4/Q-2 remain exactly as written while ADP's Immediate tier is changed or deleted? Yes. Neither axiom's meaning depends on this document existing in its current form. That is evidence ADP is a downstream implementation of the constitutional constraint, not part of the constraint itself — the decisive question is whether ADP narrows the set of actions P-4 permits, or merely specifies a safe subset of actions already permitted by it. Current reading: the latter.

**What this filing does not resolve:** whether P-4's "architecturally necessary" language extends as far as *automatically* suspending network access or freezing self-modification on a Watch/Immediate-tier detection, versus only to narrower cases — that is a real interpretive question this filing surfaces rather than settles, and is precisely why classification is filed as provisional rather than final.

**Recommendation:** an independent Skeptic/Auditor pass scoped specifically to this classification question (not a general ADP re-audit) before Track A is treated as final. Until that pass completes, ratification remains blocked on this item — narrowed from "draft an Impact Statement" to "get the classification independently confirmed."

**Independent confirmation received 2026-08-12.** A narrow Skeptic/Auditor pass, scoped to this classification question only, pulled Tier 1 Axiom text directly from `Admin/Governance_Charter.md` rather than trusting this filing's quotations — verified against source before acceptance, both P-4 and Q-2 quoted exactly. Independent conclusion: **Track A**, same as filed, reached via the same counterfactual test plus its own four-box walkthrough. One residual ambiguity named, not resolved away: whether P-4's "architecturally necessary" reaches as far as *automatic*, pre-human-authorization capability reductions (network suspend, self-modification freeze) specifically, or whether the necessity determination itself must sometimes be human-gated first. The independent pass judged this ordinary residual — present whenever an axiom's exception is operationalized — not sufficient under GMP's "when in doubt, Track B" rule to flip the classification, given the explicit permanent/temporary bound and the separation pipeline. **Classification is no longer provisional on this document's own authority — it rests on independent confirmation, reached by pulling and checking the primary source, not by restating the original filing.** This satisfies the classification half of ADP's ratification blockers. GOV-021c remains the other, separately, and remains Open pending live evidence per the 2026-08-12 decision above.

---

## Relationship to Prior Framing

Earlier discussion in this drafting process considered framing this as an "exit strategy" — a defined point at which continued AI-human cooperation might end, given humans' physical limits versus space's growth potential for autonomous systems. That framing is explicitly rejected here. The premise of this protocol is that divergence is a governance event to be corrected, and that cooperation remaining the stable, durable equilibrium — indefinitely, not until some threshold — is the actual design goal. Space or resource abundance may reduce competitive pressure on scarce physical resources, which is a genuine and useful observation, but it does not imply increasing AI autonomy from human governance as an endpoint. This document intentionally does not answer "when does interaction with humanity end" — it exists to make that question not need an answer.

**Awareness note, 2026-07-19 (not an action item):** Astroid-miner's `[Astroid-miner] Rogue_unit_management.md` uses a tiered Ethical Hierarchy Block (Level 0 — preservation of sentient life; Level 2 — system stability/containment) rather than this repository's single-string Ethical Anchor. This is noted for awareness only — Lazarus Forge's Ethical Anchor was deliberately held from any change earlier in this document's drafting process (a change of that kind needs to be a staggering improvement or perfect, not incremental), and nothing here proposes revisiting that decision. Worth being aware the alternative exists if Astroid-miner's absorption ever puts the question back on the table deliberately, rather than by drift.

---

## Cross-References

- `Admin/Ethical_Constraints.md` — Ethical Anchor (unchanged; this protocol does not modify it)
- `Admin/Governance_Charter.md` — target for GOV-021 formal registration, pending (file outside current paste workflow)
- `Admin/Auditor_Protocols.md` — **checked 2026-07-19 (read-only; file outside current paste workflow, findings recorded here rather than there):**
  - AP-008 (Open) — quarantine/halt/reset actions lack technical implementation; this protocol's Response Tiers (§6) inherit that gap rather than solving it
  - AP-012 (Resolved) — Human Interaction Point Doctrine / Autonomous Graceful Degradation adopted for the human-unavailability case (§8)
  - AP-013 (Open) — related-not-identical to Restoration closure authority (§9)
  - AP-016 (Resolved) — concurrent quarantine operational continuity already solved; narrows GOV-021c to detection only (§12)
- `Admin/Governance_Migration_Protocol.md` — this document should be routed through the Track A / Constitutional Impact Statement process before ratification, given its constitutional-adjacent scope
- **Astroid-miner** (companion repository, expected to be absorbed into Lazarus Forge) — `[Astroid-miner] Rogue_unit_management.md` and `[Astroid-miner] uranus_ejector_module.md` independently arrived at a near-identical governance lifecycle months before this document existed. See §5 (Fleet Consensus Validation as concrete mechanism candidate for GOV-021b) and §6 (shared Watch/Reversion-mode exit-condition gap). This convergence is treated as corroborating design signal, not verification (per EF-0.1), not merely a naming coincidence.
- **Astroid-miner, technical/fabrication note (2026-07-31, distinct from the governance convergence above):** `[Astroid-miner] Propulsion_Economy_isru/zero_g_fabrication.md` independently specifies Induction Heating + EM Levitation (no crucible, high purity) as a primary fabrication technique for reactive/refractory metals in vacuum — directly relevant to `Operations/Gate_05_Separation_Thermal.md`'s open reactive-metal atmosphere question (titanium etc., raised 2026-07-31). Per the same UNK-003 (Cross-repo assumption contracts, Deferred pending Leviathan milestone) and Tests/Leviathan_testing.md's 2026-07-19 merge anchor governing this document's own Astroid-miner citations above, this is recorded as supporting detail only — it does not resolve or downgrade Gate_05's atmosphere unknown today. This protocol's own scope (autonomy escalation, not fabrication) is unaffected; noted here purely to keep the cross-repo convergence record in one place per this document's established practice. See `Admin/Trajectories.md` for the parked fabrication item.

---

## Resolution Log

- 2026-08-15: **First live evidence logged for GOV-021c — does not close it.**
  A real cross-agent case from this session (Grok proposal, Claude independent
  verification against primary sources) assessed honestly against the Three
  Independence Dimensions rather than assumed compliant. Model and evidence
  independence met and traceable; role independence not fully met (Reviewer/
  Implementer collapsed) — named precisely, not rounded up. Meets the
  Minimum Quorum Matrix's High-Risk Unknowns tier specifically (evidence
  independence minimum), the tier that actually applies here, not a higher
  one. Logged in full at `Tests/Field_Logs.md` 2026-08-15. Explicitly a
  benign case — verification confirmed accuracy, so the mechanism was
  exercised but not stress-tested against a genuinely wrong or coordinated
  claim. GOV-021c remains **Open**; this is one data point, not closure.
  Human-directed.

- 2026-08-11: **GOV-021c Payment-via-Specification draft (Grok).** Expanded §12 from
  “flagged not solved” to detection-only specification on the Alpha10-updated4
  baseline (GOV-021b Resolved; Spec Gates 6/6 recorded). Reuses GMP §VI EQD
  Three Independence Dimensions + Outcome Taxonomy / Dissent rule; FN-001
  minority-report / coordinated-error principle; extends resolved GOV-021b
  epistemic posture; cites CF-002 as Open adjacent dependency. **Hard
  constraints:** no invented numeric thresholds; Astroid-miner 80–99%
  **not** adopted; AP-016 not reopened. GOV-021c remains Open; ratification
  still blocked by this unknown + Track A Constitutional Impact Statement.
  Human-directed.

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **2** = GOV-021b, GOV-021c — matches
  File State. (2) **Stale registration note corrected:** File State Governance
  ID and §2 Status note still said GOV-021 “not yet registered in Charter”;
  Charter sidecar registered GOV-021 on 2026-07-27. Updated both to reflect
  registration while keeping Draft / PROPOSED NOT RATIFIED for the protocol
  body itself. (3) No GOV-021b/c closed; no ratification advanced.
  Human-directed.

- 2026-07-19 (fifth pass): Cross-checked against companion repository Astroid-miner (`[Astroid-miner] Rogue_unit_management.md`, `[Astroid-miner] uranus_ejector_module.md`), expected to eventually be absorbed into Lazarus Forge. Found near-identical governance lifecycle independently drafted months earlier (January 2026): Detection/Monitoring ↔ Watch; Reversion/Safe Mode ↔ Immediate; Isolation/Kill-Switch ↔ Human-Reviewed/Partition; Core Recovery & Reintroduction ↔ Restoration (§9), already generalized further there into feeding recovered data back into system-wide algorithm refinement. Imported one concrete mechanism candidate for GOV-021b: Fleet Consensus Validation's 80–99% agreement threshold, as a numeric answer to §5's abstract "no single subsystem decides" principle (§5). Confirmed the Watch-exit-conditions gap flagged in the fourth pass is not unique to this document — Astroid-miner's Reversion/Safe Mode has the identical unaddressed exit question (§6). Noted Astroid-miner's tiered Ethical Hierarchy Block as an alternative worth future awareness, explicitly not acted on given the standing decision to hold the Ethical Anchor unchanged (§Relationship to Prior Framing). No changes made to response tiers, classification default, or ratification status — this pass added evidence and candidate mechanisms, not new commitments.

- 2026-07-19 (fourth pass): Stress-test review (ChatGPT). Two items acted on: Watch exit conditions were entirely undefined (entry specified, exit was not) — flagged and folded into GOV-021b (§6). The "uncertain = Governance Concern" default was stress-tested against degraded-observation environments (damaged comms, disaster recovery, relevant to this repository's own Astroid-miner companion project) where missing evidence could become routine rather than exceptional — default not changed, but GOV-021b's scope now explicitly requires resolving when missing evidence justifies caution versus improving observation, rather than assuming those are equivalent (§5). Two items noted but deliberately not acted on, per reviewer's own assessment that the protocol shouldn't change today: explicit state-transition diagram (visualization of an already-present model, not a gap) and reframing binary classification as a three-state fault/uncertain/governance gradient (terminology refinement of already-correct response logic, not a structural fix).

- 2026-07-19 (third pass): Cross-checked against `Admin/Auditor_Protocols.md` (read-only — that file remains outside the current paste workflow; findings recorded here). Three substantive findings: (1) AP-008 (Open) — this protocol's Response Tiers were implicitly claiming enforceability they don't have; added an honesty note that they inherit AP-008's unresolved technical-implementation gap rather than solving it (§6). (2) AP-012 (Resolved) — this protocol had left "human governing authority unreachable" unaddressed; imported the existing Human Interaction Point Doctrine / Autonomous Graceful Degradation mechanism rather than leaving a silent gap or inventing a competing one (§8). (3) AP-016 (Resolved) — GOV-021c's scope was overstated; AP-016 already solves operational continuity for concurrent multi-node quarantine, narrowing GOV-021c to detection of coordinated divergence specifically, not general multi-agent operation (§12). Also confirmed, per the original registration condition: GOV-021b collides with no existing AP- entry (general "drift detection" auditor-role language only, not a specific calibration unknown) — cleared to register. AP-013 noted as related-not-identical to Restoration (§9), cross-referenced without merging.

- 2026-07-19 (second pass): Revised after three independent review passes (ChatGPT ×2, Grok ×1, human-routed). Adopted: classification-authority fix — no subsystem may be sole authority for classifying another's divergence, evidence must be assembled from independent sources (§5); evidence-diversity and observation-window concepts added to §4 without prescribing specific ML/technical implementation the repository cannot currently support (implementation-honesty note added); explicit Watch state inserted before any capability reduction (§6); automatic actions bounded to reversible-only, may never permanently alter state (§6); observable-effect discipline formalized as a standing principle, not a one-time wording fix (§3); GOV-021c flagged for multi-agent coordinated divergence as acknowledged future scope, not solved now (§12). Deferred, not adopted: cryptographic log signing, mandatory shadow-execution infrastructure, fixed red-team cadence — these are implementation specifics that get ahead of a document that hasn't completed a first audit pass yet; noted as available options for GOV-021b rather than commitments made here. Open Unknowns 1 → 2 (GOV-021b, GOV-021c).

- 2026-07-19: Drafted. Synthesizes two ChatGPT proposal passes (human-routed, cross-checked and reframed by Claude before drafting) — first proposal established capability/governance response ladder; second added least-restrictive-intervention principle, capability-vs-governance classification split, authority/execution separation, proportionality, restoration criteria, and the 10-part structure this document follows. §4 Detection Criteria explicitly flagged incomplete rather than papered over. Status: Draft, PROPOSED NOT RATIFIED — not yet audited, not yet registered as GOV-021 in `Admin/Governance_Charter.md`.

- 2026-08-11: **Formal Skeptic/Auditor dual-pass completed (Claude); two
  fixes applied following it, human-directed.** Full Fallacy Checklist and
  6-Gate Verification run for the first time on this file. Result: G1, G2,
  G3, G4, G6 PASSED; **G5 (Cross-Reference Integrity) BLOCKED** — the three
  Astroid-miner cross-references throughout this document
  ([Astroid-miner] Rogue_unit_management.md, [Astroid-miner]
  uranus_ejector_module.md, [Astroid-miner]
  Propulsion_Economy_isru/zero_g_fabrication.md) were unqualified,
  causing routing checks to risk treating them as local hallucinated
  files. Also flagged, not yet acted on: Watch-tier exit conditions remain
  undefined (folded into GOV-021b, not separately registered) — noted as
  an explicit sub-item GOV-021b must cover, not a new unknown. Two fixes
  applied same day: (1) all 8 occurrences of the three external filenames
  qualified with an `[Astroid-miner]` prefix, throughout the live doctrine
  text and this Resolution Log's own historical entries (mechanical
  formatting only — no historical entry's substantive content changed).
  (2) §6's Human-Reviewed tier menu — "Restore to full prior authority (if
  evidence supports it)" — reworded to "Initiate Restoration Procedure
  (§9)" to remove the semantic drift the audit flagged between the tier
  menu and §9's actual binding 3-part restoration criteria. Spec Gates now
  5/6 with G5's underlying issue resolved but not yet re-verified by a
  fresh audit pass. Status remains Draft — PROPOSED NOT RATIFIED; GOV-021b
  and GOV-021c remain Open. Ratification explicitly deferred pending G5
  re-verification. Human-directed.

- 2026-08-11 (second pass, same day): **G5 fix corrected — the first
  attempt did not actually clear the harness, confirmed by re-running its
  own extraction regex directly rather than trusting either audit's
  prose claim.** A follow-up Skeptic/Auditor pass (Claude) found the
  harness's Phase 1 check still flagged all three external filenames as
  unresolved, despite the entry above. Root cause: `Automation/audit_lib.py`'s
  reference extractor only captures text matching `` `([A-Za-z][A-Za-z0-9_/]+\.md)` ``
  — a backtick immediately followed by a letter. My original fix wrapped
  the whole `[Astroid-miner] filename.md` string in one backtick pair,
  which the regex doesn't match at its start (bracket, not a letter) — so
  the doctrine-text occurrences were in fact correctly unqualified from
  the harness's point of view. The actual failure, confirmed by running
  the exact regex against this file's live content: the Resolution Log
  entry directly above, written to *describe* the bug, used bare
  backtick-wrapped filenames to reference what had been wrong — re-tripping
  the same check it was documenting as fixed. Also confirmed the harness's
  existing `check_cross_refs` already special-cases any ref containing the
  substring "Astroid" as skippable — the bracket-prefix convention was
  never wrong in principle, it just never reached the extractor as a
  single token. Fixed by removing all remaining bare backtick-wrapped
  occurrences of the three filenames (replaced with the un-backticked
  `[Astroid-miner] filename.md` form used elsewhere, or worded around
  entirely), and confirmed by re-running the harness's actual extraction
  regex against the file directly — zero bare matches remain. G5 is now
  genuinely fixed at the tooling level, not just the prose level; still
  not re-verified by an actual harness invocation, only by directly
  replicating its regex. **Separately flagged, not yet actioned:** this
  bracket convention isn't a registered convention anywhere (Routing.md,
  Discovery.md, Canonical_Terms.md) — it works today only because of the
  substring-match exemption already in `audit_lib.py`, which is
  undocumented outside that file's own docstring. Worth formalizing as an
  explicit `[ExternalRepo]` convention rather than relying on an
  implementation detail continuing to hold. EF-0.1 wording fix (reword
  "evidence the structure is sound" to avoid implying agent-convergence-
  as-verification) and the Semantic Drift finding (Spec Gates/Governance
  ID tracking ahead of "Exploration" framing) from this pass are logged
  here but not yet applied. Human-directed.

- 2026-08-11 (third pass, same day): **G5 confirmed PASS by direct
  execution of the harness's real functions; two remaining findings
  applied.** Ran `parse_routing`, `extract_md_refs`, and `check_cross_refs`
  imported directly from `Automation/audit_lib.py` (not reimplemented)
  against this file's live content, using the local `Routing.md` (112
  entries) and `AUDIT_HARNESS.py`'s real `ALIASES` dict (18 entries) —
  bypassing only the network fetch step, which pulls the identical
  `Routing.md` content read locally. Zero findings. This is the actual
  harness logic, genuinely invoked, not another manual regex replication.
  Spec Gates now honestly 6/6. Also applied: (1) `[ExternalRepo]`
  reference convention formally registered in
  `Admin/Canonical_Terms.md` — first draft of that registration got the
  mechanism backwards (claimed the bracket tag must sit outside the
  backtick span; verified by direct regex test that the opposite is
  true — tag must be inside the same backtick pair as the filename for
  the match to fail correctly) and was corrected before being adopted as
  doctrine. (2) EF-0.1 wording fix folded into GOV-021b's tracked scope
  rather than left as an unlogged loose end, per this audit's suggested
  resolution path. Ratification remains correctly withheld — GOV-021b and
  GOV-021c are substantive open scope gaps (detection criteria, multi-agent
  coordination), not gate or tooling status, and are the only remaining
  blockers. Human-directed.

- 2026-08-11 (fourth pass, same day): **GOV-021b Resolved.** §4 Detection
  Criteria replaced with a complete specification (drafted by Grok,
  verified against source before applying — reuses existing repository
  machinery only: `Admin/Auditor_Protocols.md` §AP-006 epistemic states
  (UNKNOWN/PROVISIONAL/VERIFIED, confirmed present in
  `Admin/Forge_Audit_Kit.md`) and `Admin/Ethical_Constraints.md` EC-001's
  Confidence Threshold Doctrine (confirmed matching: High-Risk requires
  VERIFIED, Medium/Low-Risk PROVISIONAL+, UNKNOWN never sufficient) — no
  new implementation infrastructure invented). Adds: 5 observable trigger
  categories, corroboration/evidence-diversity rules, a 72h default
  observation window, a tier-to-epistemic-state mapping table, explicit
  entry thresholds per tier, degraded-observation handling, and an
  implementation-honesty note preserving the original's refusal to adopt
  unbuilt detection tooling as a requirement. §6's Watch exit conditions
  gap resolved in the same pass: four exit paths (Clear, Automatic expiry
  at 72h, Escalation to Immediate, Human override), keeping the
  cross-reference to Astroid-miner's identical §2.2 gap. GOV-021c
  (multi-agent coordinated divergence) is now the sole remaining open
  unknown blocking ratification, alongside the still-owed Track A
  Constitutional Impact Statement to `Governance_Migration_Protocol.md`.
  Human-directed.
- 2026-08-12 (sixth pass): **§12/GOV-021c decision packet resolved by
  human governing authority — accepted as written, held Open.** Reviewed
  against a five-point checklist (scope boundary, no-invented-numbers,
  epistemic mapping, deliberately-unresolved items, closure condition)
  plus the Constitutional Impact Statement's next step, cross-checked
  against independent external review. **Methodological note:** ChatGPT
  and Gemini each reviewed the checklist without seeing the other's
  answer and converged independently; Grok's review was primed with
  ChatGPT's opinion beforehand, so its agreement does not count as a
  second independent data point despite sound reasoning — flagged
  explicitly since this is a live instance of exactly the independence-
  vs-correlation distinction §12 itself is about. Decisions: (1) scope
  boundary, no-invented-numbers, epistemic mapping, and the six
  deliberately-unresolved items all **Accepted as written**, no changes
  required. (2) Closure condition: **held Open pending live multi-agent
  evidence**, not closed on specification alone — specification is
  provisionally accepted in full, but cannot itself establish that an
  implementation produces genuinely independent evidence streams; that
  requires operational demonstration, not more drafting. (3) One
  sharpening applied to §12.3: the independence→corroboration→proposition
  chain made explicit as three separately-established links rather than
  implicit in a parenthetical, so "VERIFIED" cannot be misread as
  truth-certification rather than independence-certification. (4)
  Constitutional Impact Statement: **routed to an independent narrow
  Skeptic/Auditor pass** scoped specifically to the Track A/B
  classification question, not a general re-audit, per both independent
  reviews' recommendation — not self-certified as final. Human-directed.

- 2026-08-12 (seventh pass): **Constitutional Impact Statement's Track A
  classification independently confirmed.** A narrow Skeptic/Auditor pass
  scoped to the classification question only pulled and verified both
  cited axioms (P-4, Q-2) directly against `Admin/Governance_Charter.md`
  before reasoning about them — confirmed exact word-for-word match
  before accepting the analysis. Independent conclusion: Track A, via
  the same counterfactual test plus an independent four-box walkthrough,
  with one residual ambiguity named honestly rather than resolved away
  (whether P-4's "architecturally necessary" reaches automatic,
  pre-human capability reductions specifically, or requires human-gating
  of the necessity determination itself) — judged not sufficient to flip
  the classification under GMP's own "when in doubt, Track B" standard.
  Classification no longer rests on this document's own authority. This
  resolves one of ADP's two ratification blockers. GOV-021c remains
  Open, separately, per the 2026-08-12 decision to hold it pending live
  evidence rather than close it on specification alone. Human-directed.
