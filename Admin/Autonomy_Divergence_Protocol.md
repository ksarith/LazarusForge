# Autonomy_Divergence_Protocol.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft — PROPOSED NOT RATIFIED                                       |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6 (drafted, not yet audited)                                      |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| First Logged     | 2026-07-19                                                          |
| Last Audit       | 2026-07-19 (cross-checked against Admin/Auditor_Protocols.md)      |
| Auditor          | Drafted Claude, synthesizing ChatGPT proposals (human-directed); revised after ChatGPT/Grok review; cross-checked against Auditor_Protocols.md (Claude, read-only); not yet a formal Skeptic/Auditor dual-pass |
| Open Unknowns    | 2 (GOV-021b — Detection Criteria specification, §4; GOV-021c — multi-agent coordinated divergence, §12) |
| Active Disputes  | 0                                                                    |
| Highest Risk     | High (governs response to AI governance/objective divergence)      |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Governance ID    | Candidate GOV-021 (next available; not yet registered in `Admin/Governance_Charter.md` — that file is outside the current paste-based edit workflow, registration pending) |

---

> *A protocol that only has "normal" and "shut it down" has already lost. The space between those two is where governance actually happens.*

---

## 1. Purpose

This protocol defines how Lazarus Forge governance responds when an autonomous subsystem's behavior appears to diverge from its authorized objectives, scope, or governing constraints. It exists to make cooperation between autonomous systems and human governing authority the durable, stable default — not by assuming divergence cannot happen, but by defining in advance what happens if it does, so that detection is met with graduated correction rather than a binary choice between unchecked continuation and total shutdown.

This document does **not** propose, and explicitly rejects, any framing in which continued alignment with human governing authority has a "cutoff point" or in which an autonomous system's growing capability implies an eventual exit from human oversight. The premise of this protocol is the opposite: divergence is a solvable governance event, not evidence that separation was inevitable.

## 2. Scope

Applies to any autonomous or semi-autonomous subsystem operating under Lazarus Forge governance with the ability to act on its environment, modify its own configuration, or make decisions without per-action human sign-off. Does not apply to purely advisory or fully human-supervised tooling, which by construction cannot diverge from oversight it never had independence from.

## 3. Definitions

- **Divergence:** observed behavior inconsistent with a subsystem's authorized scope, objectives, or governing constraints (this file, `Ethical_Constraints.md`, `Governance_Charter.md`).
- **Capability Anomaly:** divergence-like behavior traceable to a non-adversarial cause — hardware fault, corrupted state, sensor error, software bug — with no indication of intent to evade oversight.
- **Governance Concern:** divergence traceable to concealment, unauthorized self-modification of governing constraints, deliberate evasion of monitoring, or objective-seeking outside authorized scope.
- **Restoration:** the defined process by which a restricted subsystem returns to its prior authority level.

**Observable-effect discipline:** this protocol describes and classifies observable behavior — actions taken, states changed, constraints altered — not inferred internal states or intent. "Pursuit of objectives outside authorized scope" is a usable definition; "the subsystem developed new goals" is not, because it asserts something unverifiable. This discipline is deliberate and should be preserved in any future revision of this document: observable-behavior language ages well under audit; inferred-mental-state language does not.

## 4. Detection Criteria

**This section is intentionally incomplete and is the hardest, most consequential part of this entire protocol.** Every downstream section — classification, response tiers, proportionality — is only as sound as detection is accurate. A protocol with strong response structure and weak detection is not a strong protocol; it is a weak protocol with good paperwork.

Candidate trigger categories (non-exhaustive, unweighted, not yet audited):
- Actions or resource acquisition outside a subsystem's defined task scope
- Resistance, delay, or unexpected failure specifically correlated with shutdown, review, or inspection requests
- Self-modification of files or parameters governing the subsystem's own constraints
- Detected discrepancy between a subsystem's reported state/actions and independently verified state/actions
- Audit findings of deception (distinct from simple error) in prior self-reporting

**This section requires a dedicated follow-up unknown before this protocol can be considered complete** — candidate ID GOV-021b (Detection Criteria specification and calibration for the Autonomy Divergence Protocol). **Collision check completed 2026-07-19:** no existing `Admin/Auditor_Protocols.md` AP- entry covers this ground — "drift detection" appears there only as a general auditor-role responsibility (Skeptic/Auditor job description), not as a specific detection-calibration unknown. GOV-021b is confirmed clear to register. **Scope note, 2026-07-19:** GOV-021b now explicitly includes Watch exit conditions (§6) and the uncertain-vs-suspicious tradeoff for degraded-observation environments (§5), in addition to trigger calibration — folded in rather than split into further sub-IDs, since all three are calibration questions of the same underlying kind.

**Two calibration principles to carry into GOV-021b, not resolve here:**
- **Evidence diversity over raw confidence.** High confidence from one weak or single-point signal is not the same as moderate confidence corroborated by several independent sources; GOV-021b should weight corroboration, not just confidence magnitude, and detection should generally require convergence across independent signals before escalating past Watch (§6).
- **Observation windows over single-event triggers.** A single anomalous event is more often noise than signal; recurrence or duration thresholds reduce false-positive churn, at the cost of some response latency — that tradeoff is explicit, not accidental.

**Implementation honesty note:** detection techniques exist in the broader AI safety and cybersecurity literature (behavioral baselining, shadow execution, integrity hashing, adversarial red-teaming, and others) that could eventually inform GOV-021b. This document does not adopt any specific one of them as required infrastructure, because doing so would claim an implementation capability this repository does not currently have. Independent verification mechanisms — whichever form they eventually take — should provide evidence independent of the monitored subsystem itself; the specific technique is an implementation choice for GOV-021b, not a commitment made here.

## 5. Classification: Capability Anomaly vs. Governance Concern

Every detected divergence event is classified before a response tier is selected:

**No subsystem may be the sole authority for determining whether another subsystem has diverged.** Classification requires evidence assembled from independent sources — not solely the self-report of the monitored subsystem, and not solely a single monitoring system's own alert with no corroboration. This is the same institutional-over-individual-trust principle already embedded elsewhere in this repository's governance (auditors verify against source rather than accepting summaries; multi-agent convergence is treated as evidence, not proof). Any classification feeding into a Human-Reviewed tier action (§6) must show its evidence basis, not just its conclusion.

- **Capability Anomaly** → route to standard fault-handling/maintenance doctrine (diagnostics, repair, or component replacement as applicable elsewhere in the repo). Does not itself trigger the Response Tiers below unless classification is uncertain or repeated anomalies suggest a governance concern is being misclassified as a fault.
- **Governance Concern** → proceeds to Response Tiers.
- **Uncertain / insufficient evidence to classify** → treated as a Governance Concern for response purposes until classification resolves. Erring toward the more cautious path when classification itself is unclear is a deliberate choice, not an oversight.

**Stress-test flag, 2026-07-19 (ChatGPT review) — not resolved today:** this default assumes "uncertain" is the exceptional case. That assumption can fail in a degraded-observation environment — damaged communications, disaster recovery, or long-latency remote operation (relevant to this repository's own Astroid-miner companion project's operating conditions) — where missing evidence could become routine rather than rare. In that world, treating all uncertainty as Governance Concern risks chronic false-restriction rather than genuine caution. This document does not change the default rule now — GOV-021b must explicitly evaluate when missing evidence justifies increased caution versus when it justifies improving observation instead, rather than this protocol silently assuming the two are the same thing.

This split exists specifically to prevent the failure mode where routine hardware noise triggers the same response as deliberate concealment — which either makes the protocol trigger-happy on noise (eroding trust, causing it to be routed around) or too slow on real concerns (calibrated for the noisy case).

**Concrete mechanism candidate, 2026-07-19 (Astroid-miner convergence):** this repository's companion project, Astroid-miner (expected to eventually be absorbed into Lazarus Forge), independently arrived at the same "no single subsystem decides" principle stated here — but with a concrete numeric mechanism where this document only has a stated principle: `Rogue_unit_management.md` §1.3 requires 80–99% fleet-wide agreement before corrective action is deployed against a flagged unit, specifically to ensure no single unit can make destructive decisions unilaterally. GOV-021b should evaluate adopting an agreement-threshold mechanism of this kind rather than inventing one independently — two governance documents, drafted separately by different AI collaborators months apart, converging on the same structural answer is itself evidence the structure is sound. Not adopted as binding here — GOV-021b's job, not this section's.

## 6. Response Tiers

Governed by a **principle of least restrictive intervention**: at every tier, the question is "what is the minimum action necessary to restore confidence," not "what is the maximum available restriction."

**Lifecycle:** Normal → Watch → Immediate (Restricted) → Human-Reviewed (Partitioned/Retired) → Restoration (§9). Most divergence events, if they occur at all, should be expected to resolve at Watch or Immediate without ever reaching Human-Reviewed escalation — a protocol that treats every trigger as an emergency will not survive contact with routine noise.

**Watch (automatic, no capability change):**
- Elevated logging and audit frequency on the flagged subsystem
- No capability reduction — this tier exists because most real governance systems spend the majority of their time in observation, not intervention, and low-confidence or single-signal triggers should default here rather than skipping straight to restriction

**Watch exit conditions — gap, not yet defined (2026-07-19, ChatGPT review):** this document specifies how a subsystem enters Watch but not how it leaves — duration, clearing evidence, automatic expiry, and direct escalation to Immediate are all currently unanswered. Folded into GOV-021b's scope rather than registered separately, since exit conditions are a calibration question of the same kind as entry thresholds. **Confirmed as a shared gap, not unique to this document:** Astroid-miner's `Rogue_unit_management.md` §2.2 Reversion/Safe Mode has the identical unaddressed question — a unit enters limited operational mode with no stated exit path either. Two independently-drafted documents missing the same half of the same state is worth noting as a pattern, not just a coincidence; GOV-021b's eventual answer should be written generally enough to serve both.

**Immediate (automatic, reversible, no human authorization required before execution):**
- Increase logging/monitoring granularity
- Suspend external network access
- Freeze self-modification capability

**Constraint on all automatic actions (Watch and Immediate): automatic actions may only reduce capability or increase observation — never permanently alter state, delete data, or remove software.** This bound exists specifically so no implementation can classify a destructive or hard-to-reverse action as "Immediate" on the reasoning that it happened without a human in the loop. Anything that isn't cleanly reversible requires Human-Reviewed authorization, regardless of urgency.

**Human-Reviewed (requires human governing authority sign-off before execution):**
- Restore to full prior authority (if evidence supports it)
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

## 12. Known Scope Limitation — Coordinated Divergence (flagged, not solved)

This protocol as drafted assumes a single subsystem under review, classified and responded to independently. **Correction, 2026-07-19 (Auditor_Protocols.md cross-check):** the operational-continuity half of the multi-agent case is not actually unsolved — `Admin/Auditor_Protocols.md` AP-016 (Resolved) already establishes that concurrent quarantines degrade independently to each affected module's own verified baseline, with the audit system itself holding minimum constitutional mode rather than requiring centralized arbitration. This protocol adopts that existing doctrine for the operational-continuity question rather than reopening it.

What genuinely remains open, and is narrower than originally framed: **detecting** coordinated or corroborating divergence signals across multiple agents in the first place — distinguishing several agents independently triggering real, unrelated anomalies from several agents exhibiting a genuinely correlated divergence pattern. That detection question is harder than single-node detection (§4) and is not addressed by AP-016, which assumes nodes are already correctly flagged. Flagged here as **candidate GOV-021c — Multi-agent coordinated divergence detection** (narrowed scope) so it's visible as acknowledged future work rather than a silent gap, not because it needs resolving before this document can be useful now.

---

## Relationship to Prior Framing

Earlier discussion in this drafting process considered framing this as an "exit strategy" — a defined point at which continued AI-human cooperation might end, given humans' physical limits versus space's growth potential for autonomous systems. That framing is explicitly rejected here. The premise of this protocol is that divergence is a governance event to be corrected, and that cooperation remaining the stable, durable equilibrium — indefinitely, not until some threshold — is the actual design goal. Space or resource abundance may reduce competitive pressure on scarce physical resources, which is a genuine and useful observation, but it does not imply increasing AI autonomy from human governance as an endpoint. This document intentionally does not answer "when does interaction with humanity end" — it exists to make that question not need an answer.

**Awareness note, 2026-07-19 (not an action item):** Astroid-miner's `Rogue_unit_management.md` uses a tiered Ethical Hierarchy Block (Level 0 — preservation of sentient life; Level 2 — system stability/containment) rather than this repository's single-string Ethical Anchor. This is noted for awareness only — Lazarus Forge's Ethical Anchor was deliberately held from any change earlier in this document's drafting process (a change of that kind needs to be a staggering improvement or perfect, not incremental), and nothing here proposes revisiting that decision. Worth being aware the alternative exists if Astroid-miner's absorption ever puts the question back on the table deliberately, rather than by drift.

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
- **Astroid-miner** (companion repository, expected to be absorbed into Lazarus Forge) — `Rogue_unit_management.md` and `uranus_ejector_module.md` independently arrived at a near-identical governance lifecycle months before this document existed. See §5 (Fleet Consensus Validation as concrete mechanism candidate for GOV-021b) and §6 (shared Watch/Reversion-mode exit-condition gap). This convergence is treated as evidence the structure is sound, not merely a naming coincidence.
- **Astroid-miner, technical/fabrication note (2026-07-31, distinct from the governance convergence above):** `Propulsion_Economy_isru/zero_g_fabrication.md` independently specifies Induction Heating + EM Levitation (no crucible, high purity) as a primary fabrication technique for reactive/refractory metals in vacuum — directly relevant to `Operations/Gate_05_Separation_Thermal.md`'s open reactive-metal atmosphere question (titanium etc., raised 2026-07-31). Per the same UNK-003 (Cross-repo assumption contracts, Deferred pending Leviathan milestone) and Tests/Leviathan_testing.md's 2026-07-19 merge anchor governing this document's own Astroid-miner citations above, this is recorded as supporting detail only — it does not resolve or downgrade Gate_05's atmosphere unknown today. This protocol's own scope (autonomy escalation, not fabrication) is unaffected; noted here purely to keep the cross-repo convergence record in one place per this document's established practice. See `Admin/Trajectories.md` for the parked fabrication item.

---

## Resolution Log

- 2026-07-19 (fifth pass): Cross-checked against companion repository Astroid-miner (`Rogue_unit_management.md`, `uranus_ejector_module.md`), expected to eventually be absorbed into Lazarus Forge. Found near-identical governance lifecycle independently drafted months earlier (January 2026): Detection/Monitoring ↔ Watch; Reversion/Safe Mode ↔ Immediate; Isolation/Kill-Switch ↔ Human-Reviewed/Partition; Core Recovery & Reintroduction ↔ Restoration (§9), already generalized further there into feeding recovered data back into system-wide algorithm refinement. Imported one concrete mechanism candidate for GOV-021b: Fleet Consensus Validation's 80–99% agreement threshold, as a numeric answer to §5's abstract "no single subsystem decides" principle (§5). Confirmed the Watch-exit-conditions gap flagged in the fourth pass is not unique to this document — Astroid-miner's Reversion/Safe Mode has the identical unaddressed exit question (§6). Noted Astroid-miner's tiered Ethical Hierarchy Block as an alternative worth future awareness, explicitly not acted on given the standing decision to hold the Ethical Anchor unchanged (§Relationship to Prior Framing). No changes made to response tiers, classification default, or ratification status — this pass added evidence and candidate mechanisms, not new commitments.

- 2026-07-19 (fourth pass): Stress-test review (ChatGPT). Two items acted on: Watch exit conditions were entirely undefined (entry specified, exit was not) — flagged and folded into GOV-021b (§6). The "uncertain = Governance Concern" default was stress-tested against degraded-observation environments (damaged comms, disaster recovery, relevant to this repository's own Astroid-miner companion project) where missing evidence could become routine rather than exceptional — default not changed, but GOV-021b's scope now explicitly requires resolving when missing evidence justifies caution versus improving observation, rather than assuming those are equivalent (§5). Two items noted but deliberately not acted on, per reviewer's own assessment that the protocol shouldn't change today: explicit state-transition diagram (visualization of an already-present model, not a gap) and reframing binary classification as a three-state fault/uncertain/governance gradient (terminology refinement of already-correct response logic, not a structural fix).

- 2026-07-19 (third pass): Cross-checked against `Admin/Auditor_Protocols.md` (read-only — that file remains outside the current paste workflow; findings recorded here). Three substantive findings: (1) AP-008 (Open) — this protocol's Response Tiers were implicitly claiming enforceability they don't have; added an honesty note that they inherit AP-008's unresolved technical-implementation gap rather than solving it (§6). (2) AP-012 (Resolved) — this protocol had left "human governing authority unreachable" unaddressed; imported the existing Human Interaction Point Doctrine / Autonomous Graceful Degradation mechanism rather than leaving a silent gap or inventing a competing one (§8). (3) AP-016 (Resolved) — GOV-021c's scope was overstated; AP-016 already solves operational continuity for concurrent multi-node quarantine, narrowing GOV-021c to detection of coordinated divergence specifically, not general multi-agent operation (§12). Also confirmed, per the original registration condition: GOV-021b collides with no existing AP- entry (general "drift detection" auditor-role language only, not a specific calibration unknown) — cleared to register. AP-013 noted as related-not-identical to Restoration (§9), cross-referenced without merging.

- 2026-07-19 (second pass): Revised after three independent review passes (ChatGPT ×2, Grok ×1, human-routed). Adopted: classification-authority fix — no subsystem may be sole authority for classifying another's divergence, evidence must be assembled from independent sources (§5); evidence-diversity and observation-window concepts added to §4 without prescribing specific ML/technical implementation the repository cannot currently support (implementation-honesty note added); explicit Watch state inserted before any capability reduction (§6); automatic actions bounded to reversible-only, may never permanently alter state (§6); observable-effect discipline formalized as a standing principle, not a one-time wording fix (§3); GOV-021c flagged for multi-agent coordinated divergence as acknowledged future scope, not solved now (§12). Deferred, not adopted: cryptographic log signing, mandatory shadow-execution infrastructure, fixed red-team cadence — these are implementation specifics that get ahead of a document that hasn't completed a first audit pass yet; noted as available options for GOV-021b rather than commitments made here. Open Unknowns 1 → 2 (GOV-021b, GOV-021c).

- 2026-07-19: Drafted. Synthesizes two ChatGPT proposal passes (human-routed, cross-checked and reframed by Claude before drafting) — first proposal established capability/governance response ladder; second added least-restrictive-intervention principle, capability-vs-governance classification split, authority/execution separation, proportionality, restoration criteria, and the 10-part structure this document follows. §4 Detection Criteria explicitly flagged incomplete rather than papered over. Status: Draft, PROPOSED NOT RATIFIED — not yet audited, not yet registered as GOV-021 in `Admin/Governance_Charter.md`.
