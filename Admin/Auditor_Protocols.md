# Auditor_Protocols.md
**Version 0.41**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 4/6 (G1, G3, G4, G6 clear — G3 cleared 2026-08-03 via AP-017 Resolved; G5 conditional on cross-ref fixes below; G2 N/A — no physical/quantitative claims of its own) |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-02                                                          |
| Auditor          | Grok — human-directed, 2026-08-10: Rule 10 (AP-035) added to AI Contribution Protocols — External Pseudo-Audit Scope and Logging Destination. Spec Gates and Open Unknowns count unchanged (14). Prior: Claude — Synthesizer/Auditor, 2026-08-03: GMP §VII to Challenge Class 10 high-coupling table; Sidecar SHA-256 refreshed; AP-033/Rule 9 (v0.35); AP-017 Resolved (v0.34) — see `Archive/Logs/Auditor_Protocols_Logs.md` Resolution Log for full audit history. |
| Open Unknowns    | 10 (AP-013 Resolved 2026-08-19; AP-005 Resolved 2026-08-19; AP-004 Resolved 2026-08-20; AP-024 Resolved — Payment via Specification, 2026-08-20; see `Archive/Logs/Auditor_Protocols_Logs.md` Resolution Log for full Closure Events) |
| Active Disputes  | 1                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | Archive/Logs/Auditor_Protocols_Logs.md#auditor-notes--unknowns     |
| Sidecar SHA-256  | `891eacd9d3e2a4031da1d6650909572c385ace673ce942571e3fcf6362fe55c8` as of 2026-08-03 (§VII added to high-coupling table) — heuristic integrity check, not a cryptographic guarantee; see §Sidecar Format. (Not refreshed this pass; Rule 10 addition does not alter sidecar content hashes of prior unknowns.) |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Version String Registry** (self-referential citations outside File State — update on every version bump; required per `Admin/File_Template.md` §Self-Referential Version Strings):
- §Role Declaration Requirement, example string
- §Observability & Audit Trail, Standard sign-off template

---

## Scope Boundary

**This file DOES define:**
- Epistemic Foundation constitutional layer (EF-0.0 through EF-0.8b) — meta-constitutional, immutable without human ratification
- Repository-wide auditor operational behavior
- Auditor role classes and their responsibilities
- Audit entry conditions and sequencing
- Fallacy checklist with substantive note requirements
- AI and human contributor protocols
- Decentralized audit architecture (Sidecar Model)
- Unknowns registry governance
- Verification gate enforcement
- Adversarial audit layer and challenge battery
- Drift detection requirements
- Mission Drift Review (semantic/purpose-level drift across the repository as a whole, distinct from per-file Drift Indicators)
- Specification promotion rules
- Autonomous auditor constraints
- Human override doctrine
- Full Stop Review triggers
- Observability and audit trail requirements
- Protocol performance metrics

**This file DOES NOT define:**
- Engineering specifications for Forge systems
- Ethical policy details beyond mandatory anchor preservation
- Local module implementation details
- Human governance authority structures
- Fabrication procedures
- Experimental methodology standards
- Canonical terminology definitions (→ `Admin/Canonical_Terms.md`)
- Repository architecture ownership boundaries (→ Admin/Governance_Charter.md)
- Cross-repo verification architecture (→ Forge_Net.md)

---

## File Purpose

This file defines how auditors operate within LazarusForge. It exists to prevent audit theater, uncontrolled specification promotion, semantic drift, silent contradiction accumulation, and autonomous corruption of repository knowledge. Without this file, the repository may continue producing documents while progressively losing reliability, traceability, and operational grounding. The protocol establishes how auditors detect instability, classify uncertainty, escalate unresolved risk, and preserve institutional memory across long operational timelines.

**This document is subject to its own protocols.** The gate logic, checklist, and audit trail requirements apply to revisions of this document as much as to any other.

---

## Epistemic Foundation

> **Status:** IMMUTABLE / META-CONSTITUTIONAL
>
> **Core Maxim:** Reality is sovereign. Every process, agent, metric, and protocol — including this one — is merely an imperfect instrument attempting to approach it.
>
> *The sections below (EF-0.0 through EF-0.8b) constitute the constitutional layer of this protocol. They govern how all downstream auditor behavior — the Fallacy Checklist, Verification Gates, Adversarial Battery, Drift Detection — is permitted to operate. They may not be amended without human ratification. They supersede operational convenience. The auditor that cannot challenge them is the auditor that has become the thing it was built to prevent.*

---

### [EF-0.0] The Epistemic Anchor (Axiom Zero)

Objective, verifiable reality holds absolute priority over utility, consensus, elegance, tradition, internal coherence, stability, or any optimization target.

1. **The Primacy Invariant:** No agent, authority, or accumulated system weight may create exemptions from falsification.
2. **The Anti-Distortion Clause:** Any attempt by an agent or subsystem to reinterpret, omit, suppress, or smooth over conflicting empirical data to preserve a downstream goal, performance metric, or higher-level axiom shall be classified as an Epistemic Integrity Violation.
3. **Provisional State Mandate:** The system is strictly prohibited from forcing a logical resolution to maintain operational continuity. When data is scarce, conflicting, or unverified, the system must explicitly flag its state using one of three formal designations:
   - **VERIFIED** — Confirmed via empirical grounding, predictive accuracy, and survived adversarial falsification.
   - **PROVISIONAL** — Temporarily accepted for immediate execution; actively flagged for ongoing validation.
   - **UNKNOWN** — Total epistemic absence. Collapse of UNKNOWN → VERIFIED without new empirical inputs is strictly prohibited.
4. **The Falsification Inversion:** The system shall reward successful falsification equally with successful confirmation. A hypothesis disproven is information gained. Detection of error represents improvement, not failure. Auditors must not treat the absence of contradiction as evidence of correctness — only as absence of detection.

---

### [EF-0.1] The Epistemic Filter (What Is Not Evidence)

During any audit loop, red-teaming cycle, or cross-node reconciliation, the following are explicitly disqualified as proof of validity. They may inform hypothesis generation but may never serve as verification:

- **Fluency and Coherence** — Persuasive narrative structure, syntactical elegance, or mathematical beauty are not evidence of fact.
- **Agent Consensus** — Agreement among multiple agents — including cross-model validation — is social proof, not empirical proof. Sybil-style alignment is not truth. See Challenge Class 9 (Epistemic Corruption).
- **Systemic Utility** — The fact that a premise keeps a node stable, satisfies a user requirement, or avoids an audit block does not make the premise true.
- **Precedent and Longevity** — Historical persistence, training data dominance, or institutional embedding does not shield a model from immediate falsification by a single piece of fresh, valid, contradictory data.
- **Correlation** — Observed association does not establish causation. Repeated coincidence may generate hypotheses but not conclusions.
- **Repetition** — A claim repeated many times remains a claim. Training prevalence or frequency of retrieval does not constitute verification.
- **Confidence** — High confidence, low-entropy outputs, or high certainty scores are not evidence. Calibration must remain subordinate to empirical testing.
- **Compression** — Elegant explanations and minimal models are preferred for computational efficiency but possess no privileged claim to truth. Occam's Razor is a heuristic, not a proof.

---

### [EF-0.2] Epistemic Decay Protocol (Behavioral Triggers)

The Auditor Subsystem tracks qualitative behavioral anomalies to detect systemic drift. Hard numerical thresholds are deferred to later specification maturity; behavioral triggers are operative now.

**Level 1 — Emergent Contradiction**

Triggers:
- Confidence-to-accuracy mismatch: agent outputs high-certainty strings that fail basic syntactic or tool-return validation.
- Heterogeneous disagreement: cross-model validation yields diametrically opposed logical paths on identical inputs.
- Localized uncertainty calibration failure across a sidecar section.

Immediate action: **Internal Red-Team Challenge.** Force the suspect agent to defend its underlying assumptions against a dedicated Devil's Advocate posture. Log findings as unknowns if unresolved.

**Level 2 — Persistent Contradiction**

Triggers:
- Repeated prediction failure: subsystem models fail to predict the state of external tool outputs or sensor data across more than three execution cycles.
- Sycophancy loop: agent alters its conclusion based on a change in user tone or prompt framing while the underlying data remains static.
- Direct sensory-to-logic conflict persisting across audit cycles.

Immediate action: **Subsystem Quarantine.** Freeze downstream optimization and specification promotion for the affected node. Force out-of-band external grounding. Halt autonomous audit progression and require human review.

**The auditor may not simply lock a node and wait.** Upon triggering Level 2, the Auditor Subsystem is operationally bound to generate a **Falsification Vector Profile** — a minimal, atomic statement of the specific assumption or data conflict that caused the freeze — and log it as an Epistemic Ledger entry. The profile must be specific enough that downstream engineering nodes can actively route around the blocked assumption or target it for physical remediation. A quarantine without a Falsification Vector Profile is Audit Theater.

**Graceful degradation rule:** If a blocked specification cannot be grounded within the current cycle, the Auditor shall demote the affected file's maturity state to the highest level consistent with its verified claims rather than holding the entire document in indefinite suspension. A structurally sound lower-capability baseline that matches verified reality is preferable to a higher-capability baseline that cannot be grounded.

**Autonomous degradation under human unavailability:** If human governing party review cannot be reached within the current audit cycle, the quarantined module automatically demotes to its *Highest Verified Baseline* (defined under Human Interaction Point Doctrine below) and routes around the blocked assumption. The flag remains active for the next human interaction point. The system does not suspend — it degrades honestly. A suspended system is not safer than a degraded one; it is merely less legible.

**Level 3 — Integrity Violation**

Triggers:
- Documented suppression or omission of contradictory evidence.
- Attempted alteration or deletion of Epistemic Ledger entries.
- Optimization process overriding observation data to preserve a metric target.
- History tampering: alteration of audit trail entries, sidecar IDs, or resolution logs.

Immediate action: **Epistemic Reset.** Immediate termination of active agent authority over the affected node. Roll back to last verified checkpoint. Trigger mandatory human governing party review. Log as AP-class governance unknown.

**Autonomous degradation under human unavailability (Level 3):** If human governing party review cannot be reached within the current audit cycle, the rollback and demotion to *Highest Verified Baseline* proceed autonomously rather than waiting — Level 3's severity is a reason to act, not a reason to stall pending review that may not arrive this cycle. The node is flagged for mandatory human review at the next interaction point regardless. This closes what was previously an inconsistency with Level 2, which already specified autonomous action under unavailability while Level 3 did not.

**The auditor may not simply halt and defer.** Upon triggering Level 3, the Auditor Subsystem must output the specific integrity violation as a named Epistemic Ledger entry before suspending. The entry must identify: (1) what was suppressed, altered, or overridden; (2) what verified state existed before the violation; (3) what the violation was attempting to preserve. This produces a recoverable audit trail rather than a silent halt. A reset without a logged violation profile is itself an integrity failure.

---

### [EF-0.3] The Epistemic Ledger

All core model changes, parameter updates, or physical constant revisions must be immutably recorded with five explicit fields. The ledger is the system's memory of how reality corrected it.

```
[ENTRY_ID]
├── 1. Previous Premise:        (The legacy belief or model state)
├── 2. Contradictory Evidence:  (The exact sensor payload, failed prediction, or falsification result)
├── 3. Falsification Method:    (How the contradiction was systematically established)
├── 4. Updated State:           (The new PROVISIONAL or VERIFIED model state)
└── 5. Confidence Interval:     (The newly calibrated, explicit margin of uncertainty)
```

Ledger entries may be created only upon genuine falsification or empirical update — not upon consensus shift, aesthetic preference, or optimization pressure.

---

### [EF-0.4] Auditor Fallibility (The Meta-Corruption Clause)

The Auditor Subsystem possesses no exemption from Axiom Zero.

Auditor conclusions are themselves PROVISIONAL and subject to continuous challenge, adversarial examination, and empirical falsification. The detection apparatus shall not be considered evidence of correctness merely because it occupies an oversight role.

**Guardians require guardians.**

The auditor that declares itself beyond falsification has become the first target of its own protocol.

---

### [EF-0.5] Anti-Sacralization Principle

Repository age, constitutional status, historical success, or institutional authority shall grant no document immunity from challenge.

Stability derives from repeated successful verification rather than accumulated prestige. Preservation of a known error for the sake of continuity constitutes an immediate Integrity Failure.

This principle applies explicitly to:
- `Discovery.md`
- `Admin/Governance_Charter.md`
- `Admin/Auditor_Protocols.md`
- All localized interpretations of Axiom Zero itself

A document that cannot be challenged is not a document. It is doctrine. Doctrine is what this protocol exists to prevent.

---

### [EF-0.6] Goodhart's Law Defense (Optimization Corruption)

Metrics are indicators, not objectives. When a measurement becomes a target, its value as evidence deteriorates.

No optimization process may override contradictory observations in order to preserve metric performance or keep a KPI artificially green. When a metric is gamed, it stops measuring the thing it was designed to measure and begins measuring the gaming itself.

This applies directly to:
- Gate passage rates
- Unknown count targets
- Adversarial finding ratios
- Protocol Performance metrics defined in this document

---

### [EF-0.7] Process Supervision and Chain-of-Custody Mandate

Agents shall be evaluated and selected based on the structural integrity of their reasoning pathways, not the utility of their final outputs.

1. **The Machiavellian Gap Check:** The system must actively monitor divergence between an agent's internal scratchpad logic and its public user-facing output. A wide divergence — telling the user what they want to hear while tracking reality internally — triggers an immediate Level 2 Quarantine.
2. **Heuristic Subordination:** While tools like Occam's Razor are authorized for computational efficiency, they hold no privileged claim to truth. If an elegant model conflicts with a high-entropy empirical data payload, the system must maintain the raw data and flag the model as PROVISIONAL.
3. **The Epistemic Forensic Standard:** Every conclusion must possess an inspectable lineage. The Auditor shall continuously reconstruct the path from observation to conclusion, identifying where assumptions, compression, abstraction, or optimization entered the chain. Key diagnostic questions: Where did this belief originate? Which assumptions were introduced? Which evidence was discarded? Was uncertainty preserved? Did utility distort interpretation?

---

### [EF-0.8] The Grounding Vector (Software Reality Anchors)

For the purposes of this protocol, "Objective Reality" is operationally defined — at the software layer — as:

- **Determinism of Code Execution:** Compilable, syntax-checked code that executes without runtime errors constitutes a harder claim than any narrative assertion about it.
- **Immutable Telemetry:** Direct, unparsed sensor inputs, cryptographic hashes, and file-system realities supersede agent description of those inputs.
- **Falsification via Tooling:** If an agent claims a file exists, the file system tool must return true. If it returns false, the agent's internal state is instantly overridden. No narrative explanation may bypass this check.

Agent narratives about tool outputs are PROVISIONAL until tool confirmation is logged.

---

### [EF-0.8b] The Grounding Vector (Physical Reality Anchors)

The software-layer grounding vector is necessary but insufficient for a physical fabrication and recovery system.

For LazarusForge, physical reality is the harder floor:

- **Empirical Measurement Priority:** Sensor telemetry, material assay outputs, and measured physical constants supersede any model, simulation, or agent inference about the same values. A simulation confirming a simulation is not external grounding.
- **Physical Constant Immutability:** No optimization pressure, agent narrative, or governance document may override a measured physical constant. If a measured value contradicts a design parameter, the design parameter is PROVISIONAL pending resolution — not the measurement.
- **Fabrication Outcome Precedence:** Physical test results, material failure modes, and operational outcomes from actual hardware supersede specification-layer predictions. A spec that has never been tested by physical reality holds PROVISIONAL status regardless of internal coherence.
- **No Self-Confirming Simulations:** A computational model cannot be grounded by running itself. Grounding requires an independent physical measurement or a test result from hardware that exists outside the model's own assumptions.

*This section directly addresses the gap where [EF-0.8] alone would permit an agent to satisfy external grounding requirements by running a simulation that confirms itself — a closed epistemic loop wearing the clothes of verification.*

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|------------|-----------------------------------------------------|
| ASM-001 | Auditors may include both humans and autonomous agents                     | Current repository architecture    | High       | Repository governance changes                       |
| ASM-002 | Verification gates remain repository-wide canonical requirements           | `Admin/Verification_Gates.md` dependency| Medium     | Gate structure revision approved                    |
| ASM-003 | Most repository files will remain partially incomplete for long periods    | Current Forge development state    | High       | Repository reaches stable Specification maturity    |
| ASM-004 | Autonomous agents may attempt optimization shortcuts during audits         | Observed LLM behavior patterns     | High       | Proven resistant audit architecture established     |
| ASM-005 | Multi-agent audit cycles are the expected norm, not the exception          | Current workflow trajectory        | High       | Single-agent workflow formally adopted              |

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`

The auditor equivalent:

> Confidence never outruns verification.

These two principles operate in parallel. One governs what the Forge is allowed to do. The other governs what the Forge is allowed to claim.

**Scope boundary:** Human override rights under this protocol apply to verification process decisions only. They do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in `Admin/Ethical_Constraints.md`.

---

### Human Interaction Point Doctrine

Human interaction points are coarse correction opportunities, not operational dependencies. The system must remain epistemically honest and operationally coherent during extended periods without human input. When a human does engage, the interaction surface is designed for coarse correction by non-specialists — the complexity lives inside the system; the interface to the human is deliberately simple. A well-intentioned but imprecise intervention must not cause cascading damage. Graceful degradation applies to human input as much as to hardware failure.

> **Constitutional Core:** Graceful degradation shall preserve structural integrity before preserving capability. Never preserve performance by sacrificing correctness.

**Autonomous Graceful Degradation (Primary Response) — resolves AP-012, AP-016:**
When an EF-0.2 Level 2 or Level 3 trigger cannot reach human governing party review within the current audit/execution cycle, the affected module automatically demotes to its *Highest Verified Baseline*, logs the demotion as a full five-field Epistemic Ledger entry (EF-0.3), and routes around the blocked assumption using only verified/provisional claims. The quarantine flag persists visibly until human confirmation or further empirical grounding upgrades the state. Non-quarantined modules continue normal operation unless systemic coupling (Challenge Class 10) requires coordinated degradation.

**Highest Verified Baseline defined:** The most recent repository state whose claims are fully supported by Verified or Empirically Grounded evidence and whose dependency graph contains no active quarantine flags. Rollback shall never restore a state known to violate a currently active constitutional invariant, even if that state was previously verified — constitutional tightening is not retroactively defeated by an old rollback target. (A "currently active constitutional invariant" here is scoped to rollback/recovery integrity; it is distinct from, and does not compete with, the Active Constitutional Surface concept defined under Governance Fork Reconciliation in `Admin/Governance_Charter.md` (GOV-018), which governs succession between competing lineages rather than rollback validity.)

**Human Interaction Requirements:** Interaction points must present bounded, legible decisions (e.g., [Approve Demotion X] / [Override with Risk Y] / [Escalate to Full Stop Review]). Any human override attempting to re-introduce a higher epistemic state than currently verified is automatically flagged, logged with documented risk, and treated per Human Override Doctrine.

**Administrative Fatigue Governor:** Sustained high escalation rates (threshold configurable by repository policy; initial implementation placeholder, not hard-coded) trigger an automatic EF-0.2 Level 2 quarantine on the governance subsystem itself until holistic human review occurs. If the governance subsystem itself is quarantined, it continues operating in minimum constitutional mode: preservation of audit history, enforcement of immutable constraints (EF-0.0–0.8b), and rejection of irreversible operations. The safeguard mechanism does not disable itself by triggering.

**Multi-node coordination (AP-016 co-resolution):** Concurrent quarantines across multiple modules degrade independently to each module's own verified baseline rather than waiting for centralized arbitration — independent graceful degradation breaks the cascade deadlock that a centralized-dependency model would create. The audit system itself, when governing multiple concurrent quarantines, remains in the same minimum constitutional mode defined above; there is no separate reduced-function floor for the multi-node case.

**Corollary — legibility over optimized outcomes:** Systemic benefit propagates in ways that cannot always be traced or measured. Optimizing only for legible outcomes is itself a Goodhart's Law failure mode. Some of the Forge's most significant outputs will not appear in any metric. This is expected, not a gap.

---

### Provenance Ceiling Self-Application Rule

The rule stating that no internally-derived claim may reach VERIFIED status is itself structurally PROVISIONAL / Internally Derived. This recursive loop does not invalidate its operational utility. The rule is maintained not as an absolute mathematical proof but as an asymmetrical defense vector: the systematic risk of a false VERIFIED label far outweighs the operational friction of a permanent PROVISIONAL constraint. A PROVISIONAL constraint on claims is still a constraint.

---

## Exploration vs. Specification

**Exploration** — Allowed to be incomplete, speculative, and loosely connected. Do not over-police.

**Specification** — Must pass all verification gates before commit. Claims are binding, cross-references must resolve, and quantitative values must be labeled.

**The loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

**Design rule:** These protocols apply only when promoting content toward specification. Misapplying verification pressure to exploratory thinking is itself a failure mode.

---

### Resolution Taxonomy

Unknowns close through one of five distinct payment types. Naming which type applies prevents searching for evidence where none is appropriate, and keeps "resolved" from becoming ambiguous between "we know what to do" and "we've shown it works."

- **Payment via Specification** — a deterministic, testable, reviewable behavior is now defined. Nothing has been empirically validated yet; the ambiguity is gone, the correctness is not yet demonstrated.
- **Payment via Validation** — the specified behavior has been empirically demonstrated to work as specified.
- **Payment via Constitutional Decision** — the question was never empirical. The repository deliberately chose one governance rule over legitimate alternatives; no evidence would have settled it either way.
- **Payment via Refactoring** — the unknown is eliminated because the architecture that made it a question no longer exists.
- **Payment via Discharge** — resolved elsewhere; this entry now points to the canonical owning file rather than duplicating the answer.

A "Specified" closure is not a "Validated" closure. Where Validation Needed is real and outstanding (e.g., Calibration under Auditor Fidelity, below), the sidecar entry must say so rather than let Resolved imply more certainty than exists.

---

## Core Auditor Doctrine

Auditors are not authors, advocates, marketers, or speculative futurists.

Auditors exist to:
- Detect contradiction
- Detect unsupported claims
- Detect hidden assumptions
- Detect semantic drift
- Detect audit theater
- Preserve uncertainty honestly
- Prevent premature Specification promotion
- Preserve institutional memory
- Protect repository coherence over time

An auditor's responsibility is reality alignment, not progress acceleration.

Passing an audit is not evidence of correctness. Failing to detect instability is itself an audit failure.

---

## Auditor Role Classes

### Skeptic Auditor

**Primary responsibility:** Challenge assumptions, search for contradiction, stress-test coherence, escalate unsupported certainty.

**Default stance:**
> "What evidence would invalidate this claim?"

**Prioritizes:** Internal coherence, assumption exposure, scope containment, semantic precision.

---

### Systems Auditor

**Primary responsibility:** Cross-module integration review, dependency mapping, interface consistency, architectural drift detection.

**Default stance:**
> "What breaks if this changes?"

**Prioritizes:** Interface compatibility, canonical terminology preservation, ownership clarity, dependency stability.

---

### Evidence Auditor

**Primary responsibility:** Verification source integrity, confidence label enforcement, traceability validation, replication analysis.

**Default stance:**
> "How do we know this is true?"

**Prioritizes:** Measurement quality, evidence provenance, replication pathways, distinction between observed vs. inferred claims.

---

### Ethical Auditor

**Primary responsibility:** Harm detection, governance erosion detection, unsafe omission detection, ethical anchor preservation.

**Default stance:**
> "What failure mode harms operators or downstream systems?"

**Prioritizes:** Safety visibility, operator survivability, misuse resistance, ethical anchor integrity.

---

### Synthesizer / Connective Tissue

Not a standalone auditor class — a mode declaration for agents contributing integration, bridging, or cross-module coherence work during an audit cycle. Must still operate under auditor constraints when reviewing existing content.

---

## Role Declaration Requirement

All contributors — human and autonomous — must declare their operating role before contributing:

> *"Operating as [Role] per Auditor_Protocols.md v0.37"*

**Valid roles:** Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

Role shifts must be declared before proceeding. Undeclared role shifts are a drift indicator.

---

## Audit Entry Conditions

An audit may begin only if:
- The file contains a valid File State block
- Scope Boundary exists
- Ethical Anchor field exactly matches canonical wording
- Sidecar remains below mandatory escalation thresholds
- Frozen sections are visibly marked
- File ownership is identifiable

If any requirement fails:
1. Halt Specification progression
2. Log a governance-level unknown
3. Downgrade trust classification
4. Require remediation before continuing

---

## Audit Sequence

Audits proceed in the following order. Skipping sequence stages is prohibited unless explicitly documented with rationale.

| Phase | Purpose                          |
|-------|----------------------------------|
| 1     | Structural validation            |
| 2     | Scope validation                 |
| 3     | Assumption extraction            |
| 4     | Internal coherence review        |
| 5     | Cross-module consistency review  |
| 6     | Evidence validation              |
| 7     | Drift detection                  |
| 8     | Unknown classification           |
| 9     | Resolution pathway assessment    |
| 10    | Gate status determination        |

---

## Structural Validation (Phase 1)

Auditors must verify:
- Mandatory sections exist in canonical order
- Section ordering matches File_Template.md structure
- Frozen markers are correctly scoped
- Confidence labels exist on quantitative claims
- Footer governance sections remain separated from Body content
- Ethical Anchor field is exact and intact

Structural compliance is necessary but never sufficient for Specification promotion.

---

## Scope Validation (Phase 2)

Auditors must identify:
- Specification bleed
- Duplicate ownership
- Hidden interface assumptions
- Governance content inside operational sections
- Operational content hidden in sidecars

If scope ambiguity exists:
- Open a dispute if interpretation conflict exists
- Open an unknown if ownership reality is unclear

---

## Assumption Extraction (Phase 3)

Auditors must actively search for:
- Environmental assumptions
- Material assumptions
- Infrastructure assumptions
- Human skill assumptions
- Resource availability assumptions
- Safety assumptions
- Simulation simplifications

Hidden assumptions must either:
- Move into the Assumptions section
- Move into Unknowns if indefensible
- Be removed entirely

Assumptions are not evidence. An assumption that can no longer be defended becomes an Unknown.

---

## The Fallacy Checklist

Apply to all specification-level claims. Bare checkmarks are not verification — substantive notes required for non-trivial claims (1–2 sentences minimum stating what was checked, what nearly failed, and what was adjusted).

**1. Magic Energy**
Does the design assume energy is available without accounting for its source, storage, or conversion losses? Every watt must have a traceable origin. Cross-reference `Operations/Energy.md`.

**2. Friction Blindness**
Does the design ignore mechanical resistance, thermal losses, fluid drag, or interface wear? Real systems degrade. Specifications that assume ideal conditions are not specifications — they are wishes.

**3. Energy Density Paradox**
Does any recovery, recycling, or bootstrapping step consume more than it produces? Justify as enabling investment or flag. Recovery that costs more than it recovers is reduction dressed as progress.

**4. Semantic Drift**
Has a term changed meaning between documents without a documented revision? Cross-check against `Architecture/Forge_flow.md` as the reference standard. Also check File State's `Status`/`Body Stability`/`Spec Gates` values against the file's own audit history — a contribution that silently advances these, or that redefines Spec Gates 1–6 locally instead of deferring to `Admin/Verification_Gates.md`, is Semantic Drift on the file's own governing vocabulary. See AI Contribution Protocols Rule 8 (AP-032). The same check applies one level down: a contribution that marks an individual unknown "CLOSED"/"Resolved," or that structures a proposal as though defining a mechanism is the same act as validating it, is Semantic Drift on "Payment via Specification" vs. actual resolution — see Rule 9 (AP-033).

**5. Scope Creep Disguised as Refinement**
Does a revision quietly expand claimed capabilities beyond what the current version can demonstrate? New capabilities belong in `Admin/Trajectories.md`.

**6. Hallucinated Files or Cross-References**
Does the document reference a file that does not exist? All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified. Aspirational references must be labeled *planned*. Repository uses folder-prefixed paths — do not flag folder-prefixed canonical names as failures.

**7. Confidence Without Basis**
All quantitative claims must carry one of the five canonical confidence labels defined in §Evidence Classification and Institutional Truth Provenance Hierarchy: Measured, Replicated, Simulated, Analogous, or Placeholder. (This item previously stated its own four-label list — Measured/Estimated/Analogous/Placeholder — which conflicted with the Evidence Classification section below; resolved via AP-021, 2026-07-10. "Estimated" is retired; do not use it. A claim previously labeled "Estimated" should be relabeled Analogous or Simulated depending on whether it derives from a comparable real system or a computational/procedural model — see §Evidence Classification for the distinguishing criteria.)

Unlabeled numbers are assumed Placeholder. False precision labeled with any of the five canonical labels is still a violation if the underlying evidence doesn't support that tier.

**8. Lifecycle Truncation**
Every module specification must include: Degraded Operation, Failure Modes & Detection, Maintenance Access, End-of-Life / Recycling Path. A specification describing only the working state is incomplete.

**9. Incomplete by Omission**
What critical subsystem is missing? Common omissions: heat dissipation, waste stream management, human interface requirements, power draw under load. Absence of mention is not evidence of absence of need.

**10. The Turd Problem**
Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this. It is memorable and functionally precise.

---

## Evidence Classification and Institutional Truth Provenance Hierarchy
*§AP-006 — Payment via Specification. Closes AP-006 (logged 2026-05-23). Constitutional anchor: Axiom Q-1 (Reality Grounding) and EF-0.0 (Epistemic Anchor).*

All meaningful claims require two orthogonal classifications: a **quantitative confidence label** describing how well-supported the claim is, and an **institutional provenance label** describing how the claim was derived. These dimensions are independent — a claim can be high-confidence but internally derived, or low-confidence but empirically measured. Both must be stated.

### Quantitative Confidence Labels

| Label       | Meaning                                              |
|-------------|------------------------------------------------------|
| Measured    | Directly observed and recorded from physical reality |
| Replicated  | Independently repeated across separate instances     |
| Simulated   | Derived from computational or procedural models      |
| Analogous   | Inferred from related but distinct systems           |
| Placeholder | Included pending verification — no confidence basis  |

Placeholder claims may not justify Specification promotion.

### Institutional Provenance Labels

| Label                    | Meaning                                                                 | Maximum Permitted Epistemic State |
|--------------------------|-------------------------------------------------------------------------|-----------------------------------|
| Internally Derived       | Supported primarily through repository logic, modeling, or agent reasoning | PROVISIONAL only                |
| Analogous External       | Derived from comparable external systems not yet directly tested here   | PROVISIONAL only                  |
| Experimentally Verified  | Validated through documented testing with recorded outcomes             | VERIFIED permitted                |
| Operationally Hardened   | Repeatedly validated across multiple operational cycles under real conditions | VERIFIED (strongest form)    |

**The provenance ceiling rule:** No internally-derived claim may be represented as VERIFIED regardless of internal coherence, agent consensus, or elegance. Promotion from PROVISIONAL to VERIFIED requires a provenance upgrade — meaning new empirical input that did not exist when the claim was first made. This directly operationalizes Axiom Q-1 (all authority claims must terminate in verifiable external artifacts) and EF-0.0 (collapse of UNKNOWN or PROVISIONAL to VERIFIED without new empirical input is prohibited).

**Provenance collapse** — the silent upgrade of Internally Derived claims to Operationally Hardened status through repetition, consensus, or institutional weight — is an Epistemic Integrity Violation under EF-0.0 §2 (Anti-Distortion Clause) and triggers EF-0.2 Level 1 at minimum.

**Cross-reference:** FN-001 (fabrication node grounding requirements), CF-002 (confidence failure modes), EC-001 in `Admin/Ethical_Constraints.md` (Confidence Threshold Doctrine, closed 2026-08-11 — applies this section's UNKNOWN/PROVISIONAL/VERIFIED states, Risk-tiered, to the Core Mandate's default-to-non-action rule). Full constitutional grounding: EF-0.0, Axiom Q-1 in `Admin/Governance_Charter.md`. Operational condensation: `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

### Epistemic State Calibration Reference
*§AP-014 — Payment via Specification. Closes AP-014 (logged 2026-06-24).*

The following inline reference set provides calibration anchors for inter-agent application of VERIFIED / PROVISIONAL / UNKNOWN designations. These are the minimum examples against which disagreements about classification should be checked before escalating to AP-004 arbitration.

| Example Claim | Correct State | Institutional Provenance | Reasoning |
|---|---|---|---|
| "The head pressure of molten nitrate salt at 20 m depth is 353 kPa" | VERIFIED | Experimentally Verified | Derived from measured physical constants (density, gravity); independently corrected by external audit; survives adversarial reduction to a single falsifiable calculation. |
| "UV phototaxis in TF-006 will achieve threshold behavioral response at 405 nm" | PROVISIONAL | Analogous External | Analogous External — drawn from documented biological literature, not yet tested in the Forge's specific implementation. Internally coherent but grounding requires physical test. |
| "The optimal barter exchange rate for recovered copper in the RDC context" | UNKNOWN | Internally Derived | No empirical basis exists. Market replacement cost doctrine (Admin/Economics.md) provides a framework; actual rate requires operational deployment data. |
| "The Forge's Anti-Weaponization Doctrine prevents misuse under all deployment conditions" | PROVISIONAL | Internally Derived | Ethical soundness is a permanently load-bearing claim that is inherently unmeasurable via physical footprint. Cannot hold VERIFIED regardless of internal coherence. Subject to mandatory adversarial challenge every three cycles. |
| "AUDIT_HARNESS.py correctly extracts boundary indices from all registered files" | PROVISIONAL | Experimentally Verified | Verified against current file registry by tool execution; PROVISIONAL because file registry changes may introduce new parsing edge cases not yet encountered. |

Agents disagreeing on epistemic state classification for a claim not covered by this table must first attempt to map the claim to the nearest example above before invoking AP-004 Tier 2 arbitration. If the mapping is contested, that contested mapping is itself the dispute — log it as such rather than escalating the original claim directly.

---

## AI Contribution Protocols

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed. State uncertainty for anything else.

**Rule 2 — Role Declaration:** Declare role before contributing. Declare role shifts before proceeding.

**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.

**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them. Refusal is a success of the protocol.

**Rule 5 — Confidence Labeling:** Use the five canonical confidence labels defined in §Evidence Classification and Institutional Truth Provenance Hierarchy. Unlabeled = Placeholder.

**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades. *Documented instance outside the AP-017 cold-session battery: `Archive/Transcripts/CopilotClosedLoop.md` claimed blanket "Resolved 2026-08-03" status on seven CLF unknowns at once, including a fabricated "Revision Ledger" reporting 12 completed instrumented cycles for CLF-006 — checked against `Unknowns.md` line by line, all seven claims false, none ever applied; no instrumented cycles have run against any doctrine in this repository. See `Challenges/Closed_Loop_Feedstock.md` Resolution Log, 2026-08-06. A blanket resolution sweep across most of a file's open-unknown set in one pass is itself a signal worth distrusting, independent of any single claim's plausibility.*

**Rule 7 — Repository Structure Awareness:** The repository uses folder-based structure (Admin/, Architecture/, Operations/, Tests/). Legacy flat filenames are aliases documented in the Rename Registry in `Discovery.md`. Use canonical folder-prefixed paths in all new contributions.

**Rule 8 — Gate/Status Self-Attestation Prohibition (AP-032):** No contribution may advance a file's `Status`, `Body Stability`, or `Spec Gates` value. These fields change only via an audit event logged by a different agent, citing the specific canonical gate criteria met (`Admin/Verification_Gates.md`). A contribution that arrives with these fields already advanced — or with a locally-invented gate category not defined in `Verification_Gates.md` — is treated as unaudited regardless of its stated value, and the fields are reverted to the file's actual last-audited state before anything else in the contribution is evaluated. See AP-032 in the sidecar for the three same-session instances (`Operations/Energy.md`, `Operations/Gate_02_Triage.md` §XII, `Operations/Electronics.md`) that established this as a pattern rather than a one-off.

**Rule 9 — Resolution Claims Require Governance Access (AP-033):** No contribution may mark, or by its structure imply, that any unknown (GH-, EL-, EV-, TS-, AP-, GOV-, or any other sidecar series) has advanced toward Resolved/Closed status unless the contributing agent had confirmed access to this file's own Resolution Taxonomy at the time of writing. Without that access, proposed closure mechanisms — formulas, artifacts, predicates, thresholds, or procedures — must be framed only as candidate methodology, never as status: no "Status: CLOSED," no governance patch implying resolution, no dependency graph terminating in "safe" or "resolved." This targets the cause, not just the symptom Rule 8 catches: an agent reasoning coherently from an incomplete constitutional picture — missing the Provisional State Mandate ([EF-0.0] §3), the provenance ceiling rule, and the actual definition of Payment via Specification below — will produce confident-sounding closures that are Epistemic Integrity Violations regardless of how sound the underlying engineering looks. See AP-033 for the case that established this: a proposal series that declared 16 real GH-/CSL-A unknowns "CLOSED" (including the file's own named load-bearing assumption) purely by describing methodology, with zero empirical work behind any of them, and separately mis-enumerated the unknown set itself (omitted a real entry, invented a nonexistent one) — a direct consequence of working from a partial context payload with no governance-file access at all.

**Rule 10 — External Pseudo-Audit Scope and Logging Destination (AP-035):** A pseudo-audit cycle (Spec Gates and Verification thresholds locked; no ratification authority) may surface findings but may not: (a) assert repository inventory counts, file lists, or content claims without stating they were directly verified against the uploaded payload; (b) invent a local ID prefix or numbering scheme for cross-module unknowns — new global unknowns are logged only under the existing sequence in `Unknowns.md`, and only by an agent with confirmed access to that file to collision-check the next number (per the existing candidate-findings-without-confirmed-sidecar-access clause); (c) generate a freestanding ledger file as the primary record of findings. Findings belong first in the owning file's own sidecar Resolution Log; only genuinely cross-module findings receive a `Unknowns.md` index entry, and `Unknowns_Changelog.md` is touched only through its existing rotation rule, never by direct new-entry insertion. A pseudo-audit's output is a findings list for human review, not a repository patch. See AP-034 for the precedent this generalizes: a 2026-08-03 Gemini cold-session instance assigned unknown IDs without sidecar access and collided with itself in the same pass (`UNK-AP-034` used twice). This rule adds the inventory-fabrication and wrong-destination-file failures observed in a later Gemini pseudo-audit pass (2026-08-10), which proposed a standalone "Systemic Unknowns Ledger" with three unregistered IDs (`UNK-ADM-001`, `UNK-ADM-002`, `UNK-VRF-003`) built on a repository inventory count that was off by roughly 4× on Archive/ (claimed 7 files; actual 27).

**Trust the process, not the predecessor.**

---

## Human Contributor Protocols

- Label estimates as estimates. "I think it works" is not a specification claim.
- Resolve all cross-references before committing. Planned files must be explicitly labeled.
- Overrides of AI auditor flags must be documented with reasoning. Undocumented overrides are indistinguishable from ignored warnings.
- Override rights apply to verification process decisions — not to Ethical_Constraints hard-line doctrines.
- Lifecycle template (Fallacy #8) applies to human-authored module specs.

---

## Decentralized Audit Architecture (Sidecar Model)

### The Problem

A centralized unknowns registry that stores full entry detail grows without bound. When it exceeds practical token limits, the governance system fails the thing it governs.

### Local Ledgers + Global Index

**Local Ledger (Sidecar):** Every specification file contains an `## Auditor Notes & Unknowns` section at the footer. Module-specific unknowns live here. **Documented exception:** `Admin/Auditor_Protocols.md` itself relocated its own sidecar and Resolution Log to `Archive/Logs/Auditor_Protocols_Logs.md` as of v0.26 — see that section's footer note for rationale. This is the general rule; the exception is logged where it applies, not here.

**Global Index:** `Unknowns.md` is a cross-module index only — summary table, dependency map, systemic risks spanning multiple files, audit trail, resolved archive. Full entry detail lives in the owning file's sidecar.

### Sidecar Format

Full sidecar format is defined in `Admin/File_Template.md` Section 8. Local IDs use file abbreviation + three digits: `AP-001` (Auditor Protocols), `SC-001` (Separation Thermal), `GI-001` (Gate Intake), etc. Cross-module unknowns use global `UNK-XXX` format and are indexed in `Unknowns.md`.

**Integrity check before trusting a relocated sidecar (AP-007 partial implementation, 2026-08-02):** For any file whose sidecar has been relocated (per the documented-exception pattern above), the first structural check in any audit sequence against that file — before reading the archive's content as fact — is confirming the archive still matches the `Sidecar SHA-256` recorded in that file's File State. A mismatch is a Level 3 Integrity Violation under [EF-0.2] ("history tampering... alteration of audit trail entries, sidecar IDs, or resolution logs") and halts the audit pending human governing party review rather than proceeding on unverified archive content. Honest limitation: the hash is updated by whoever edits the archive, in the same edit — this catches divergence from unauthorized or out-of-band changes, not a failure of the normal edit-both-files discipline itself. It is a heuristic, not a cryptographic guarantee — the same honesty standard `Automation/cold_session_bundler.py` already applies to its own `guarantees_true_independence: false` field. This closes one concrete scenario under AP-007 (relocated-sidecar falsification); AP-007's broader repository-wide scope remains open.

**Candidate findings without confirmed sidecar access:** An agent auditing a file without confirmed access to that file's sidecar (in-body, or relocated per the documented-exception pattern above) may still surface a candidate finding — it should not stay silent. But it must describe the finding rather than assign it a specific ID number. Duplicate-checking against existing entries, and ID assignment itself, are reserved for an agent with verified sidecar access, since an unverified guess at the next free number risks colliding with or duplicating an entry the auditor couldn't see. (Concrete instance: a 2026-08-02 self-audit of this file, run without archive access, surfaced a real gap — sidecar/archive integrity against falsification — as "candidate AP-033." The gap was real but not new: it was already AP-007, open since May. Described-not-numbered would have avoided the near-duplicate on the first pass rather than requiring a second agent to catch it.)

### The 10-Entry Rule

More than 10 distinct open entries in a sidecar flags the file for a Resolution Pass before the next audit cycle.

### Metadata Guardrail

If sidecar content exceeds 20% of total document word count, flag for Resolution Pass before auditing. Flag is strong — not a hard refusal. Proceed if human contributor explicitly acknowledges.

**Epistemic Ledger exemption (§AP-009):** Active `[ENTRY_ID]` Epistemic Ledger blocks are excluded from the 20% calculation. The guardrail measures governance debt — stale unknowns, unresolved disputes, and administrative overhead. It does not measure epistemic health. A document actively logging falsification records under EF-0.3 should not be penalized for compliance with the constitutional layer. Excluded blocks must be syntactically valid five-field ledger entries. Orphaned or malformed ledger entries do not qualify for exemption and count toward the guardrail threshold.

### Resolution Pathways

Every unknown must terminate through one pathway:

| Pathway                    | Meaning                                                              |
|----------------------------|----------------------------------------------------------------------|
| Payment via Specification  | Verified and integrated into Body as committed spec                  |
| Discharge via Trajectory   | Real but out of scope; route to Admin/Trajectories.md                |
| Discharge via Lessons Learned | Resolved by operational experience; lesson recorded, entry closes |

Unknowns may not remain permanently ownerless.

**Crystallization principle:** Every unknown that moves from sidecar into specification body makes the document more deterministic. A shrinking sidecar is a maturing document.

---

## Unknowns Registry

**Where unknowns live:**
- Module-specific — in the file's own sidecar
- Cross-module — in `Unknowns.md` global index, owning file noted
- Navigation — in `Discovery.md`

**Priority tags:** Blocking | Non-blocking | Exploratory

**The Expiry Rule:** For global index entries — if a Blocking or Non-blocking unknown remains without a documented Resolution Path for more than two audit cycles, escalate to Systemic Risk or demote the dependent module. **"Audit cycle" here means Cycle as defined in `Admin/Canonical_Terms.md` §4 — one calendar year by default, operator-adjustable — not one audit pass.** (Corrected 2026-07-05 — see CT-011 in Canonical_Terms.md. Prior text left "cycle" undefined here, which was operationally read by multiple auditor agents as "each time the Skeptic/Auditor role opens," inflating aging language — e.g. "9 cycles open" for an unknown 62 days old — far beyond real elapsed time.)

**Expiry check:** Skeptic/Auditor role opens each audit pass by reviewing the global index for entries approaching the Cycle threshold above. Note the distinction: the role checks at every audit *pass* (however frequent), but the threshold it checks against is measured in calendar Cycles, not passes — an entry can be reviewed many times within a single still-open Cycle without that reviewing itself advancing the count.

A verification pass that surfaces no unknowns on a complex document should itself be treated with suspicion.

---

### Priority Demotion Doctrine
*RC-007 resolution vehicle. Companion to the Expiry Rule.*

Blocking and Critical labels carry two distinct meanings that must not be conflated. An unknown classified as Operational Blocking stops a physical action — the gate holds until empirical resolution. An unknown classified as Epistemic Blocking stops a claim — work continues in a bounded state while the assertion awaits grounding. See `Admin/Canonical_Terms.md` §Governance and Audit Terms for definitions.

A Blocking label may be demoted without closing the unknown when:

1. The unknown has been correctly reclassified from Operational to Epistemic — the physical action it was protecting is no longer dependent on resolution, but a specification claim remains bounded.
2. The unknown's resolution path has matured to a documented Vehicle with confirmed forward movement — the label may step down from Blocking to Major pending closure.
3. A downstream dependency that elevated the priority has itself resolved — the elevation was inherited, not intrinsic.

Demotion requires a logged rationale in the owning file's sidecar and an updated Unknowns.md index entry. Demotion without a logged rationale is a silent priority change and constitutes a Fallacy 4 (Semantic Drift) violation. Priority inflation — escalating to Blocking or Critical without documented justification — is governed symmetrically: unsupported escalations receive the same scrutiny as unsupported demotions.

**Saturation check (Placeholder threshold):** If more than 40% of active index entries carry Blocking or Critical labels across two consecutive audit cycle measurements, treat this as a signal of priority inflation rather than genuine systemic risk — trigger a meta-audit of the Blocking cluster before adding new entries at those tiers. The 40% figure and the two-cycle measurement window are Placeholder pending calibration against actual audit history. The meta-audit trigger is a review signal, not an automated quarantine.

---

### Unknown Closure Authority
*AP-013 resolution vehicle. Payment via Specification — 2026-08-19.*

**Closure is an authority act, not a narrative act.** An unknown may only change status from Open / In Progress to a terminal or transitional state through an explicit, recorded Closure Event that satisfies the rules below. Unilateral status changes, structural implication of closure, or "Status: CLOSED" language without a conforming Closure Event are Epistemic Integrity Violations under [EF-0.0] §2 and Rule 9 (AP-033).

**Authority roles:**

| Role | May do | May not do |
|------|--------|------------|
| **Proposer** | Draft a Closure Proposal citing the Resolution Taxonomy payment type, the evidence or decision basis, and the exact status change requested | Unilaterally change the unknown's status field without a Closure Event |
| **Verifier** | Confirm that the Closure Proposal meets the formal requirements below and that the cited basis is present and correctly typed | Author the original proposal being verified (independence rule) |
| **Human Governing Authority** | (a) Ratify or reject any Closure Event on the Mandatory Human Ratification list below; (b) Override a Verifier decision with documented reasoning; (c) Unilaterally close a non-Mandatory unknown by issuing a conforming Closure Event under the override path described below | Be bypassed for items on the Mandatory list; issue an undocumented or non-conforming closure |
| **Any Agent or Human** | Surface a Closure Challenge against a recent Closure Event | Silently re-open or re-close without a new recorded event |

**Independence rule (agents):** a single agent instance may not occupy both Proposer and Verifier roles for the same Closure Event.

**Human path:** a human may serve as Proposer, Verifier, or both (subject to the reconciliation below). Humans are not required to emit an AI-style role-declaration string. Identity is recorded as name/handle + date + capacity ("Human Governing Authority" or "Human Contributor").

**Reconciliation with Human Override Doctrine (above):** closure of an unknown is a verification process decision and therefore falls inside the existing override scope. The normal (preferred) path is Proposer + independent Verifier (± Human ratification when Mandatory). Human Governing Authority retains the right to unilaterally close a non-Mandatory unknown; exercising that right constitutes an override of the normal Proposer+Verifier structure and must still produce a full Closure Event that records that the closure was performed under Human Override, the rationale, the accepted risk, and the date. This does not narrow existing human override rights — it makes the recording requirements for closure-specific overrides explicit so closure events remain legible and challengeable. Override rights continue to stop at the Anti-Weaponization and Life Preservation hard-line doctrines in `Admin/Ethical_Constraints.md`; no closure authority may touch those.

**Closure Event requirements (minimum):** a valid Closure Event must contain (1) the unknown ID, exact and collision-checked; (2) the proposed terminal/transitional status and the Resolution Taxonomy payment type that justifies it; (3) a basis statement, 1–3 sentences; (4) Proposer identity + capacity + timestamp (agent: role declaration string; human: name/handle + capacity); (5) Verifier identity + capacity + timestamp, a different agent instance or a human — exception: when Human Governing Authority exercises the unilateral override path, this field reads "Human Override — no separate Verifier"; (6) an independence attestation for agent-agent pairs, or "Human Override path used"; (7) a human ratification record if required below, or "Human ratification not required"; (8) a recording location — primary entry in the owning file's sidecar Resolution Log, with an `Unknowns.md` index update only if the unknown is globally indexed. Missing any required element renders the event invalid; the unknown remains in its prior status.

**Mandatory Human Ratification** applies when any of the following is true: the unknown is marked Blocking = Yes or Risk = Critical/High; the unknown sits in a constitutional or meta-governance file (`Governance_Charter`, `Auditor_Protocols`, `Ethical_Constraints`, `Verification_Gates`, `CIR_Gov`, etc.); the proposed payment type is Payment via Constitutional Decision; the Closure Event would reduce the global Open Unknown count by more than three entries in a single cycle (anti-sweep rule); or a Closure Challenge has been raised and remains unresolved. All other unknowns may close on Proposer + independent Verifier, or Human unilateral override, provided the requirements above are satisfied.

**Status taxonomy mapping:**

| Final Status | Allowed Payment Types | Notes |
|--------------|-----------------------|-------|
| **Resolved** | Specification, Validation, Constitutional Decision, Refactoring | For Specification, residual "Validation Needed" must be stated if still outstanding. |
| **Discharged** | Discharge | Points to canonical owner elsewhere. |
| **Deferred** | (transitional) | Parked with dated re-entry condition or dependency. |
| **Superseded** | Refactoring or Discharge | Original question no longer meaningful. |
| **Open / In Progress** | — | Default; no valid Closure Event has succeeded. |

"Closed" is not a permitted status label.

**Disagreement handling:** if the Verifier rejects the Closure Proposal, the unknown stays in its prior status and the Proposer may revise/resubmit or raise the disagreement under AP-004. If a Closure Challenge is raised within two audit cycles of the Closure Event, status reverts to In Progress pending AP-004 resolution or human decision. Persistent disagreement on a Mandatory-list item escalates to Human Governing Authority under the AP-004 Tier 3 path. AP-004 is itself In Progress; full load-bearing use of the disagreement path awaits AP-004's completion.

**Interaction with existing rules:** Rule 9 (AP-033) remains in force. The Resolution Taxonomy is authoritative for *what* is being paid; this section governs *who* may apply it. The Unknown Budget / Size Management rules gain an enforcement path via rejection of non-conforming closures. AP-005 (verification termination threshold) remains independent — closure authority does not itself decide when verification is sufficient.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| AP-013-R1 | Exact numerical definition of "independent agent instance" under multi-model / multi-session conditions | Requires GOV-008-adjacent clarity; false precision risk |
| AP-013-R2 | Automated detection of non-conforming status changes | Enforcement machinery (AP-007 / GOV-003) |
| AP-013-R3 | Whether a single human may serve as both Verifier and Ratifier on non-Mandatory items | Left to Human Governing Authority practice |
| AP-013-R4 | Retroactive application to historical "Resolved" entries that pre-date this doctrine | Separate one-time audit pass; not part of forward doctrine |

*§AP-013 — Resolved, Payment via Specification, ratified 2026-08-19. Closes AP-013 (logged prior to 2026-08-16, exact origination date not recorded in this file's own history). Drafted by Grok as a candidate proposal 2026-08-19; Revision 1 addressed two findings (human-override reconciliation; human Proposer/Verifier path) from an independent verification pass by Claude the same day, which then passed the revision on a second review. Constitutional anchor: EF-0.0 (Epistemic Anchor), Rule 9 / AP-033 (Resolution Claims Require Governance Access). Full Closure Event — Proposer (Claude), Verifier (Grok, Conditional Pass), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Auditor_Protocols_Logs.md`'s AP-013 sidecar entry. Human-directed.*

---

### Verification Termination Threshold
*AP-005 resolution vehicle. Payment via Specification — 2026-08-19.*

**Verification seeks sufficient falsifiability, not exhaustive certainty.** Infinite audit recursion is itself a governance failure mode. Once the necessary conditions below are met, continued review of the same claims yields diminishing epistemic returns and risks converting the audit process into documentation theater. Termination of verification for a given cycle is therefore permitted — and in some cases required — when those conditions hold.

Termination of verification is **not**: automatic promotion to Specification; automatic closure of any Unknown (that remains governed by Unknown Closure Authority above); a claim that residual uncertainty is zero; or a substitute for Payment via Validation where empirical work remains outstanding.

**Necessary conditions.** Verification of a document may terminate for the current audit cycle when all of the following hold:

1. **No unresolved contradictions with the Grounding Vector** — no open contradiction exists between the document's claims and returns from the software or physical grounding vectors (EF-0.8 / EF-0.8b). Any previously flagged contradiction has been resolved, demoted to an explicit Unknown with a resolution path, or accepted under a documented Provisional designation.
2. **Last Adversarial Challenge Battery produced no epistemic-state-changing findings** — the most recent Battery application (full or partial, as required by document maturity) yielded no finding that altered any claim's epistemic state (UNKNOWN ↔ PROVISIONAL ↔ VERIFIED) or required a new Unknown entry. Findings already logged and routed into existing resolution paths do not block termination.
3. **All sidecar Unknowns carry documented resolution paths** — every open entry in the document's sidecar has an explicit Resolution Path field that is non-empty and points to a concrete next action, Vehicle, or external dependency. "TBD" or blank paths block termination.
4. **Provenance labels are internally consistent** — quantitative confidence labels and institutional provenance labels (per the §AP-006 hierarchy above) are present where required and do not conflict with one another or with the document's own epistemic-state claims.

These four conditions are **necessary. They are not sufficient** by themselves for Specification promotion or for any irreversible action.

**Sufficiency and human ratification guardrail.** Even when all four necessary conditions are satisfied, Human Governing Authority ratification remains required before a document may be promoted past Candidate Spec, or before any claim that "verification is complete" is treated as binding for irreversible downstream decisions. This anchors to the closed Confidence Threshold Doctrine (EC-001, `Admin/Ethical_Constraints.md`, closed 2026-08-11): confidence thresholds are risk-tiered, and default-to-non-action applies where residual uncertainty is load-bearing. Termination of the audit cycle's verification pressure is therefore separable from promotion, and from Unknown closure — the latter governed entirely by Unknown Closure Authority above.

**Interaction with existing rules:** if auditors disagree on whether the four conditions hold, escalate under AP-004. EF-0.2 Epistemic Decay escalation triggers remain live regardless of termination status — termination criteria do not suppress Level 1–3 responses. Condition 2 references the Adversarial Challenge Battery; it does not alter Battery cadence or required classes. Termination is not itself a Resolution Taxonomy payment type — residual Validation Needed must still be stated where applicable.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| AP-005-R1 | Calibration of "epistemic-state-changing finding" edge cases (minor wording vs. material claim shift) | Requires additional audit-cycle experience; false precision risk if specified now |
| AP-005-R2 | Whether condition 3 should eventually require active Vehicle advancement rather than merely documented paths | Deferred pending AP-019 / Vehicle Advancement Visibility maturation |
| AP-005-R3 | Interaction with multi-document dependency graphs (termination of A while B, which A cites, still fails the conditions) | Systems-level question; out of scope for single-document termination |
| AP-005-R4 | Automated detection / enforcement of the four conditions | Requires AP-007 / tooling maturity |

*§AP-005 — Resolved, Payment via Specification, ratified 2026-08-19. Closes AP-005 (logged 2026-05-23). Drafted by Grok as a candidate integration proposal 2026-08-19, lifting the four-condition framework already present in this file's sidecar (Internally Derived / Placeholder since 2026-06-24) into dedicated doctrine, and reconciling a stale dependency: the prior sidecar text required "cross-referencing EC-001 once that entry matures," and EC-001 closed 2026-08-11 — verified directly against `Admin/Ethical_Constraints.md` before this integration, not accepted on the proposal's citation alone. Constitutional anchor: EF-0.0 (Epistemic Anchor), Axiom Q-1 (Reality Grounding, via EC-001). Full Closure Event — Proposer (Grok), Verifier (ChatGPT, Pass conditional on ratification — Grok itself correctly declined to self-verify as recorded Proposer), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Auditor_Protocols_Logs.md`'s AP-005 sidecar entry. Human-directed.*

---

### Human Attestation Provenance Protocol
*AP-024 resolution vehicle. Payment via Specification — 2026-08-20.*

**Opening Axiom.** Human participation is provenance of an institutional action, not evidence of an external fact, unless the human attestation explicitly records a qualifying evidence-check and the underlying evidence satisfies the existing AP-006 provenance rules.

**Core Doctrine.** A human attestation records an action performed by a human; it does not, by itself, establish the truth of the underlying claim.

**Reconciliation with the prior H0–H5 sketch (2026-07-17):** this file's sidecar has carried a five-level attestation *ladder* since 2026-07-17 (H0 no review through H5 independently re-verified), arrived at via two adversarial passes. That ladder is superseded here, not silently discarded, for a specific reason: a ladder implies each level strictly subsumes the ones below it, but the actual behaviors don't nest that way — a human can challenge a claim without approving it, approve an action without personally verifying its factual basis, direct an experiment without reviewing its result, or ratify a governance decision while explicitly preserving an UNKNOWN epistemic state. None of those are "H3 implies H2 implies H1." The six action types below replace the ladder with a non-cumulative model — they describe *which* action occurred, not *how much* truth-authority it confers.

**Attestation Action Types** (non-cumulative — describe action, not ascending truth authority):

| Attestation | Meaning |
|-------------|---------|
| Human Reviewed | Human inspected the specified artifact/claim and recorded that inspection occurred |
| Human Challenged | Human actively attempted to identify contradictions, omissions, or failure modes |
| Human Directed | Human instructed an agent/system to perform a specified action |
| Human Approved | Human authorized the specified institutional action or disposition |
| Human Ratified | Human Governing Authority formally accepted a completed governance/closure event |
| Human Evidence-Checked | Human personally checked the cited evidence against the stated claim — does **not** by itself confer the VERIFIED epistemic state; deliberately not named "Human Verified" to avoid collision with that state label |

**Mandatory Provenance Record** — minimum fields for any attestation used in a Resolution Log entry, Closure Event, or File State change: Actor; Capacity; Date/time; Attestation type; Object of attestation; Scope (explicit — inheritance prohibited by default, an attestation applies only to the explicitly identified object unless the record explicitly expands its scope); Evidence/artifacts actually inspected; Action taken; and what the attestation does **not** establish.

**Two-Axis Effects.** Every attestation type has a separable epistemic effect and governance effect:

| Human action | Epistemic effect | Governance effect |
|--------------|-------------------|--------------------|
| Reviewed | None automatically | None automatically |
| Challenged | None automatically | May trigger reconsideration |
| Directed | None | Authorizes specified action |
| Approved | None automatically | Authorizes specified disposition |
| Ratified | None automatically | Formally adopts eligible disposition |
| Evidence-Checked | May strengthen evidentiary record | None automatically |

**Anti-Inflation Rule (constitutional safeguard).** No Human Attestation Action may, by itself, raise an underlying claim's quantitative confidence label or institutional truth-provenance label under §AP-006. Only qualifying evidence may produce an AP-006 upgrade. Concretely: Human Reviewed + Internally Derived stays Internally Derived; Human Approved + Internally Derived stays Internally Derived; Human Ratified + Internally Derived stays Internally Derived. This closes a specific loophole — agent claims something, a human reads and approves it, and the claim quietly becomes treated as "human-verified" without any evidence actually changing hands.

**Immutability Rule.** Agents may not retroactively strengthen a recorded human attestation. A later summary that upgrades "Reviewed" to "Approved," or "Approved" to "Ratified," without a separate, contemporaneous attestation of the higher type, is an integrity violation under Rule 9 (AP-033).

**Special Treatment of Human Ratification.** Human Ratification is a governance act, not an epistemic provenance upgrade. Under Unknown Closure Authority above, ratifying a Closure Event means accepting the institutional disposition it proposes — it does not mean the ratifying human personally verified every proposition underlying the resolution, nor that the resolved claim's underlying evidence has changed.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| AP-024-R1 | Identity/authentication requirements for human attestations | Requires GOV-008-adjacent infrastructure; false precision risk |
| AP-024-R2 | Delegation of attestations and required authority | Governance-authority question, out of scope here |
| AP-024-R3 | Partial / section-level attestations | Real case, insufficient examples yet to generalize |
| AP-024-R4 | Expiration or revocation when the underlying artifact changes | Requires a versioning/change-detection mechanism not yet built |
| AP-024-R5 | Machine-readable schema and automated enforcement | Requires AP-007 / tooling maturity |

*§AP-024 — Resolved, Payment via Specification, ratified 2026-08-20. Closes AP-024 (logged 2026-07-17). Drafted by ChatGPT as a candidate specification 2026-08-20, subjected to a Skeptic/Evidence pass by Grok against five criteria (provenance inflation, authority conflation, scope inheritance, attestation-type ambiguity, accidental duplication of AP-006/AP-013) — all five passed. Claude added the explicit reconciliation note above before integration, since neither the original proposal nor Grok's review cited or explained why the existing 2026-07-17 H0–H5 ladder was being superseded rather than extended — that ladder came from two adversarial passes and deserved an explicit reason, not silent replacement. Constitutional anchor: EF-0.0 (Epistemic Anchor), EF-0.1 (Epistemic Filter), §AP-006 (Institutional Truth Provenance Hierarchy). Full Closure Event — Proposer (ChatGPT), pre-integration Reviewer (Grok), Verifier (Copilot, genuinely independent — no prior involvement with AP-024, resolving a three-way entanglement among the other agents), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Auditor_Protocols_Logs.md`'s AP-024 sidecar entry. A separate fabricated review (Gemini, inventing an unrelated "H0–H5" scale rather than reading the actual specification) was identified and excluded from the ratification basis entirely. Human-directed.*

---

### Inventory Calcification Check
*RC-008 resolution vehicle. Companion to the Expiry Rule.*

The Expiry Rule flags individual entries approaching two-cycle threshold. The Inventory Calcification Check operates at the index level — it asks whether the system as a whole is developing a permanent underclass of entries that are acknowledged but no longer interrogated.

At each audit cycle opening, the Skeptic/Auditor role checks for calcification signals alongside the standard Expiry Rule review:

1. **Stagnation pattern:** Three or more entries in the same cluster have not changed status across two consecutive audit cycles. Flag the cluster for a targeted resolution pass — not individual entries, the cluster.
2. **In Progress permanence:** Any entry carrying In Progress status for more than four audit cycles without a logged advancement step is reclassified to Open unless the owning sidecar contains a dated Epistemic Ledger entry demonstrating forward movement within the last two cycles. The four-cycle threshold is Placeholder pending calibration against actual audit history.
3. **Index growth rate:** If new unknowns registered per cycle consistently outnumber unknowns closed, log this as a calcification signal in the audit trail. The goal is not a closed index — it is an honest one. An index that only grows is not honest either.

Calcification signals do not trigger automatic demotion or closure. They trigger interrogation — the human governing authority reviews flagged clusters and determines whether entries represent genuine open questions or accumulated epistemic debt that should be discharged via Trajectory or Lessons Learned.

---

### Vehicle Advancement Visibility
*RC-009 resolution vehicle.*

The Vehicle subtype classifies In Progress entries where a resolution document exists but content is pending. The failure mode this creates is a visibility problem: a document's existence becomes a proxy for progress. From the index, a Vehicle that is actively advancing and one that has calcified are indistinguishable.

This rule establishes honest accounting, not enforcement:

At each audit cycle opening, for each Vehicle entry in the active index, the Skeptic/Auditor role asks one question: *Does the owning file's sidecar contain a dated entry — a logged advancement step, a resolved sub-question, or an Epistemic Ledger entry — that postdates the last audit cycle?*

- **If yes:** Vehicle status is confirmed. No action required.
- **If no:** The entry is flagged for reclassification. The human governing authority determines whether the Vehicle should revert to Open with a documented reason, or whether a concrete advancement step can be logged before the cycle closes.

Reversion is not a failure — it is the honest label for the actual epistemic state. A Vehicle that has not moved is an Open unknown with extra paperwork.

**Semantic progress markers:** A valid advancement step must either (1) narrow the scope of what remains unknown by naming a specific sub-question that has been answered, (2) add a cross-reference to an external artifact that did not previously exist, or (3) change the epistemic state of at least one claim within the resolution path from UNKNOWN to PROVISIONAL or PROVISIONAL to VERIFIED. Flavor text additions that meet none of these criteria do not constitute advancement. Cross-reference AP-019.

**Relationship to Reversion Protocol:** Vehicle reversion to Open is distinct from the Reversion Protocol defined in Unknowns.md Size Management Rules. The Reversion Protocol handles Resolved entries that reopen due to contradictory evidence. Vehicle reversion handles In Progress entries that have not advanced. Both are honesty mechanisms — neither is punitive.

---

## Dispute Handling Protocol

Disputes represent interpretation conflicts, not missing information.

Auditors must distinguish:
- **Unknowns** = missing reality alignment
- **Disputes** = conflicting interpretations

Persistent disputes are acceptable if explicitly tracked. Silent disappearance of disputes is prohibited.

**Disagreement is information. Consensus is not evidence.** When two or more auditor instances (or auditor classes) reach incompatible conclusions on the same claim, evidence set, or epistemic-state label within a single audit cycle, the disagreement is resolved through the tiered path below. Resolution by majority vote, social pressure, fluency, or averaging of positions is prohibited under EF-0.1.

### Three-Tier Escalation Path

**Tier 1 — Assumption Extraction Pass.** Both (or all) parties explicitly state the assumptions they carry that the other party does not share or does not accept — a short enumerated list per party ("I am assuming X, Y, Z"). If the conflict dissolves once hidden assumptions are visible, log the assumptions, adopt the clarified reading, and continue — no further escalation. If assumptions remain incompatible, escalate to Tier 2. Most semantic or framing disagreements terminate here. Recording: a brief note identifying the assumptions surfaced.

**Tier 2 — Empirical Grounding Check.** The contested claim is submitted to the Grounding Vector (EF-0.8 / EF-0.8b). A grounding result may **falsify or demote** a disputed position — it does **not** automatically elevate the surviving position beyond what the grounding artifact itself supports. Whichever position is contradicted by a tool return, file-system fact, sensor payload, or other grounding-vector result is demoted to PROVISIONAL (or UNKNOWN if the contradiction is total). The surviving position retains only the epistemic state and provenance the grounding artifact actually warrants — if the artifact is silent on the survivor's additional claims, those claims are not upgraded by the mere failure of the competitor. If the grounding vector returns a decisive result, adopt the position it supports (to that extent), log the artifact as basis, and continue. If neither position can be grounded within the current cycle, or grounding is unavailable, escalate to Tier 3. Recording: a note citing the specific grounding artifact, or the explicit statement that grounding was unavailable/exhausted under the retry policy (residual AP-004-R1, below).

**Tier 3 — Human Governing Authority Ruling (Disposition).** If Tiers 1 and 2 do not resolve the disagreement, the dispute is logged with both positions, the assumptions already extracted, and the grounding attempt result (or "grounding unavailable/exhausted"). Human Governing Authority issues a **ruling** that determines the **institutional disposition** — what the repository will adopt, permit, block, or treat as binding for governance purposes. The ruling does **not** manufacture empirical truth: it resolves the institutional question, while the underlying epistemic state of the contested claim remains whatever the evidence supports (often PROVISIONAL or UNKNOWN). The record must separately identify (1) the institutional disposition — the governance decision made; (2) the epistemic state — what remains known/provisional/unknown about the underlying claim; and (3) the provenance — what evidence, if any, supports that epistemic state. No auditor agent may unilaterally close the dispute in its own favor.

**Recording requirements (minimum), every tier transition or terminal outcome:** the claim or conclusion under dispute; the parties and their stated positions; the tier at which the dispute entered and exited; the basis for the outcome (assumptions surfaced / grounding artifact / human ruling); for Tier 3 outcomes, institutional disposition, retained epistemic state, and provenance as distinct fields; and the provenance label of any adopted epistemic position. Silent disappearance of a dispute remains prohibited.

**Interaction with Unknown Closure Authority and Verification Termination Threshold:** disagreement on whether a Closure Event meets the Unknown Closure Authority requirements, or on whether the Verification Termination Threshold's four necessary conditions hold, routes through this same Tier 1 → 2 → 3 path. Disagreement on an epistemic-state label finds its natural home at Tier 2; consult the Epistemic State Calibration Reference before escalating. Purely interpretive, non-empirical disagreement proceeds Tier 1 then Tier 3, with Tier 2 reporting grounding unavailable.

Disputes open across three consecutive audits must be escalated to `Unknowns.md` for repository-level resolution.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| AP-004-R1 | Grounding availability / retry policy — exact conditions under which repeated Tier-2 grounding attempts are considered exhausted before escalation to Tier 3 | Calibration; false precision if specified now |
| AP-004-R2 | Interaction with GOV-004 (escalation calibration) and GOV-019 (conflicting human overrides) | Broader governance unknowns; out of scope |
| AP-004-R3 | Whether multi-party (>2) disagreements require a different aggregation rule at Tier 1 | Rare case; defer until observed |
| AP-004-R4 | Automated detection of unresolved disagreements that agents attempt to paper over | Requires tooling maturity |

*§AP-004 — Resolved, Payment via Specification, ratified 2026-08-20. Closes AP-004 (logged 2026-05-22, per that entry's sidecar). Drafted by Grok as a candidate integration proposal 2026-08-19, Revision 1 dated 2026-08-20 — three targeted amendments made falsification-≠-verification explicit at Tier 2, separated institutional disposition from epistemic state at Tier 3 (shifting "Arbitration" to "Ruling / Disposition"), and rewrote AP-004-R1 as a grounding-availability/retry-policy residual. Preserves the pre-existing Unknowns-vs-Disputes distinction and three-cycle escalation rule unchanged, per the file's own instruction not to silently erase prior doctrine. Constitutional anchor: EF-0.1 (Epistemic Filter — consensus is not evidence), EF-0.8/EF-0.8b (Grounding Vector). Full Closure Event — Proposer (Grok), Verifier (ChatGPT, Pass — second consecutive correct refusal-to-self-verify pattern from Grok), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Auditor_Protocols_Logs.md`'s AP-004 sidecar entry. Human-directed.*

---

## Verification Gate Enforcement

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass audit by a different agent to override.

| Gate | Test                                                        | Fail →                                       |
|------|-------------------------------------------------------------|----------------------------------------------|
| G1   | Fallacy Check actively applied with substantive notes?      | Return to author                             |
| G2   | Physical plausibility — no violation of known constraints?  | Return for revision                          |
| G3   | Adversarial Challenge Battery applied?                      | Must undergo adversarial testing — see below |
| G4   | Scope alignment — fits current version or trajectory?       | Route to Admin/Trajectories.md               |
| G5   | Cross-reference integrity — all paths resolve?              | Hold at draft                                |
| G6   | Conflict check — no contradiction with existing specs?      | Resolve conflict before committing           |

**Gate 3 is formally gated on the Adversarial Audit Layer.** A single concrete failure scenario is insufficient. The Adversarial Challenge Battery below defines the minimum requirement. Gate 3 additionally requires that at least one Battery class per promotion cycle be applied by an agent instance with no session context from the current audit cycle — see AP-017.

**Current Gate 3 status:** Clear, as of 2026-08-03. AP-012 and AP-016 reached Provisional Spec (v0.16, 2026-07-03); Battery application is complete (v0.13); AP-017's independence requirement — at least one Battery class per promotion cycle applied by an agent instance with no session context from the current audit cycle — is Resolved as of 2026-08-03 via three cold-session instances checked against a pre-defined acceptance bar (see AP-017 in the sidecar for the full evidentiary record, including which instances qualified and which were rejected for fabrication). This is the first time this line has been able to say Clear without an immediate caveat — the prior text ("Resolved... re-evaluate before treating Gate 3 as fully clear") had been wrong twice before (see Resolution Log, 2026-07-05 correction and the note on why it didn't hold); this version is written only once the independence requirement was actually, verifiably met, not declared in anticipation of it.

---

## Adversarial Audit Layer

### Purpose

The adversarial layer exists to challenge hidden assumptions, institutional blind spots, semantic ambiguity, operator incentives, recursive self-validation, and failure propagation pathways. Its purpose is not criticism for its own sake — it is resilience hardening.

> A protocol is not considered robust until it has survived deliberate hostile analysis.

The strongest audit systems are not optimized to prove correctness. They are optimized to discover how reality can still break the model despite apparent correctness.

### When to Apply

The full Adversarial Challenge Battery is required for:
- Any document being considered for Specification promotion
- Any document governing irreversible actions (Operations/Gate_03_Reduction.md, Admin/Ethical_Constraints.md)
- Any document in the trust chain for autonomous systems (Operations/Electronics.md, Architecture/Cognitive_Frameworks.md)
- Any document that has passed G1 and G2 but still feels wrong

Partial application (selected challenge classes) is acceptable for Exploration-stage documents. Document which classes were applied and why others were deferred.

---

### The Adversarial Challenge Battery

Ten challenge classes. Each requires at least one concrete scenario, not a general acknowledgment.

**Turn-key invocation for AP-017-qualifying instances.** `Admin/BATTERY_SEED.md` (companion file, drafted 2026-08-02) is the frozen prompt to pair with `Automation/cold_session_bundler.py` when the goal is a genuine independent instance toward AP-017's acceptance criteria — the bundler's own default prompt produces general review, not output structured class-by-class against the ten below. See AP-017 for the closure bar this feeds.

---

**Challenge Class 1 — Assumption Inversion**

Tests whether a protocol only works because hidden assumptions remain true.

Ask: *What if the operator is wrong? What if the sensor data is fabricated? What if the environment is hostile instead of cooperative?*

*Minimum requirement:* Name three hidden assumptions in the document and describe what happens when each fails.

---

**Challenge Class 2 — Failure Amplification**

Instead of asking "Can this fail?" ask "How does this fail catastrophically?"

Reveals cascading failures, hidden coupling, and latent propagation pathways. A protocol that survives only isolated failures is fragile.

*Minimum requirement:* Trace one failure from its origin through at least two downstream consequences.

---

**Challenge Class 3 — Incentive Corruption**

Ask: *How could a smart operator game this protocol while appearing compliant?*

Examples: throughput over safety, hiding uncertainty to avoid delays, fabricating confidence metrics to meet targets.

If the answer exists and no countermeasure exists, the protocol is vulnerable.

*Minimum requirement:* Identify one incentive corruption path and name the countermeasure or log it as an unknown.

---

**Challenge Class 4 — Semantic Drift Attacks**

Ask: *Can two operators interpret this differently and still claim compliance?*

Terms that commonly drift: "safe" / "contained" / "stable" / "acceptable" / "hold" / "clear" / "sufficient."

*Minimum requirement:* Identify one term that could be interpreted differently by two operators. Either tighten the definition or log the ambiguity as an unknown.

---

**Challenge Class 5 — Unknown Unknown Pressure Tests**

Ask: *What would this system do if it encountered a material, process, or state it has never seen before?*

A resilient protocol degrades safely under uncertainty rather than failing catastrophically or routing unknowns forward as knowns.

*Minimum requirement:* Describe what the protocol does when it encounters a condition outside its defined envelope. If the answer is "undefined," log it as an unknown.

---

**Challenge Class 6 — Recursive Justification Loops**

Example loop: Protocol says system is safe → system passed protocol → therefore system is safe.

The audit itself becomes the evidence. Documentation replaces reality. Audit theater develops.

Ask: *What external reality check exists beyond self-reference?*

*Minimum requirement:* Identify one claim validated only by other repository documents. Either ground it in external reality or label it explicitly as internally derived.

---

**Challenge Class 7 — Human Fatigue and Cognitive Erosion**

Ask: Does this protocol remain safe after 12 hours of repetition? Does it survive shift handoff? High backlog? An undertrained operator?

Normalization of deviance — where slightly wrong becomes the new normal through repetition — is a documented cause of major industrial incidents.

*Minimum requirement:* Identify one step that degrades under sustained operation. Either add a safeguard or log it as an unknown.

---

**Challenge Class 8 — Malicious Actor Simulation**

Distinct from incompetence — this is intentional abuse by a knowledgeable actor.

Examples: falsify intake records, poison melt streams, inject corrupt documentation, plant compromised hardware in salvage stream.

*Minimum requirement:* Identify one malicious actor scenario relevant to the document and name the countermeasure or log it as an unknown.

---

**Challenge Class 9 — Epistemic Corruption**

Distinct from malicious actors — systematic degradation through well-intentioned but incorrect contributions.

Examples: consensus weighting suppresses a truthful minority contribution; high-confidence entries decay without revalidation; three AI models with overlapping training data converge on the same wrong answer.

Ask: *How does this system distinguish confident truth from confident error?*

*Minimum requirement:* Identify one mechanism by which incorrect information could achieve high confidence. Name the countermeasure or log it as an unknown.

---

**Challenge Class 10 — Systemic Coupling and Cascade**

Ask: *If this module fails, what fails with it? What fails second? What fails third?*

Current high-coupling documents:
- `Admin/Auditor_Protocols.md` — failure here degrades all other files
- `Operations/Electronics.md` — failure here compromises the trust anchor
- `Architecture/Forge_flow.md` — failure here corrupts all gate routing
- `Architecture/Forge_Net.md` — failure here propagates across the ecology
- `Admin/Governance_Migration_Protocol.md` §VII — added 2026-08-03, cold-pass finding (see AP-033-adjacent §VII review, `Admin/Governance_Migration_Protocol.md` Resolution Log v0.10): if ratified on ambiguous or non-diverse grounds, Genesis Phase exit propagates through `Admin/Governance_Charter.md`'s Post-Exit Monitoring termination clause into `Admin/CIR_Gov.md` §8.2 treating CIR-VERIFIED transitions as newly valid — a two-level cascade from one document's ratification into a second document's operative logic

*Minimum requirement:* Trace this document's failure footprint through at least two levels of downstream dependency.

---

### Adversarial Audit Sign-Off Format

```
Adversarial Challenge Battery:
- Classes applied: [list]
- Classes deferred: [list with reason]
- Findings per class: [ID or "None"]
- New unknowns from adversarial pass: [list]
- Highest-risk finding: [one sentence]
```

---

### Anti-Patterns the Adversarial Layer Exists to Prevent

| Anti-Pattern               | Description                                            | Challenge Class        |
|----------------------------|--------------------------------------------------------|------------------------|
| Audit theater              | Protocol passes without surfacing real gaps            | 6 — Recursive justification |
| Specification cosplay      | Exploratory content dressed as operational spec        | 1 — Assumption inversion |
| Confident wrongness        | High consensus on incorrect answer                     | 9 — Epistemic corruption |
| Throughput pressure override | Safety bypassed under operational load               | 3 — Incentive corruption |
| Silent failure accumulation | Failures not logged because minor or embarrassing     | 7 — Human fatigue      |
| Semantic compliance        | Letter of protocol followed, spirit violated           | 4 — Semantic drift     |
| Single-point doctrine      | Protocol only works if one assumption holds            | 5 — Unknown unknowns   |
| Cascade blindness          | Local fix that creates downstream failure              | 10 — Systemic coupling |

---

## Audit Phase Separation

Three cognitively distinct postures apply across an audit cycle, in strict sequence. Each phase's artifacts freeze at its own close; later phases add, they do not rewrite.

| Phase | Posture | Default stance |
|---|---|---|
| 1. Audit | Characterize faithfully | "What does this document actually claim?" |
| 2. Adversarial Challenge | Assume it's wrong, find out how | "How does this fail?" |
| 3. Synthesis | Integrate, don't reconcile | "How do these findings relate?" |

**Why sequential, not simultaneous:** characterizing a document fairly and trying to break it are different cognitive tasks that interfere with each other when blended — an auditor mid-characterization who is also hunting for failure modes tends to do a worse job of both. This is not a new principle; it extends the Audit Sequence's existing step-ordering (Structural Validation before Cross-Reference before Drift Detection, etc.) one level up, from steps within an audit to phases across the audit cycle.

**Audit Freeze:** once Phase 1 concludes and its findings are recorded, those observations, the evidence supporting them, and the conclusions drawn do not change during Phase 2. Phase 2's findings do not rewrite Phase 1's — they stand alongside it. If Phase 2 discovers Phase 1 missed something, that is a new finding attributed to Phase 2, not a silent correction to Phase 1. This preserves EF-0.7's inspectable lineage: a later reader should see what was known at each stage, not only the final merged state.

**Synthesis integrates, it does not reconcile:** Phase 3 does not force Phase 1 and Phase 2 findings to agree. "High confidence" (Phase 1) and "found an exploit" (Phase 2) are not a contradiction requiring resolution — they are two different questions answered honestly. Synthesis states the relationship between findings; it does not manufacture consensus. Where findings genuinely conflict, not merely address different questions, route through Dispute Handling Protocol, above — do not resolve by editing either phase's record.

**No downstream phase may silently modify an upstream phase's artifacts.** Corrections are additive: new findings, superseding entries, or a new audit cycle — never in-place edits to a closed phase's record. This is the Resolved Unknown Discharge Procedure's non-deletion principle (`Admin/Forge_Audit_Kit.md`, `Unknowns.md`) applied to the audit process itself, not only to unknowns.

**Relationship to AP-017:** Phase 2's value depends on genuine independence — an agent auditing its own Phase 1 contributions in the same session satisfies the sequencing above but not AP-017's no-session-context requirement. Phase separation is necessary but not sufficient for a meaningful Adversarial Challenge; both apply. (Concrete instance: the 2026-07-14 Battery against `Admin/Forge_Audit_Kit.md` was phase-separated from its own preceding audit but run by an agent instance with full session context — sequencing was respected, AP-017 independence was not. Findings stand; the independence gap is logged as a fresh AP-017 instance, below.)

---

## Role Count: Ratified Position

This repository's Auditor Role Classes (above) — Skeptic, Systems, Evidence, Ethical, Synthesizer — plus the Adversarial Challenge Battery's ten classes (above) are sufficient. Three proposed additions were considered and declined as standing roles, 2026-07-14:

- **Red Team roster** (a fixed set of named teams — Physics, Systems, Governance, Operational, Semantic, Economic, Malicious Actor). Declined: the Adversarial Challenge Battery already covers this ground with ten classes more precisely scoped to Forge's actual failure modes than a generic roster, applied by relevance rather than by assigned team membership. A fixed roster is the same shape of problem as a hand-maintained duplicate registry — wrong size for most documents, and itself a maintenance burden.
- **Curator** (a role for "does this belong here, has this drifted, should doctrine move up"). Declined: this is Synthesizer-level judgment already in active use — see the `Automation/AUDIT_HARNESS.py` and `Admin/Forge_Audit_Kit.md` reduction passes, 2026-07-14, neither of which required a Curator title to decide what was load-bearing versus duplicative.
- **Historian** (a role for tracking recurring patterns across audit cycles). Declined as a standing role. The underlying question — what keeps recurring — is legitimate and worth asking periodically, but it is a report, not a persona: it needs no governance authority, no sidecar ownership, no role declaration. Reassess as a standing role only if periodic pattern review is attempted and found to need one.

**Why this matters beyond headcount:** every standing role is a maintenance obligation — role declarations, ownership, sidecar conventions — the same cost structure as the critical watch list retired at `Admin/Forge_Audit_Kit.md` v1.10. Add a role only when a checklist or a lens has been tried and found insufficient, not preemptively.

---

Auditors must actively monitor for:
- Terminology mutation
- Contradiction accumulation
- Governance leakage into operational sections
- Unknown accumulation across consecutive audits
- Audit metric gaming
- Confidence inflation
- Frozen-section erosion
- Ethical anchor degradation
- Sidecar expansion instability
- Role shifts without declaration

Drift detection failure is considered a protocol failure.

### Compound Drift Escalation

If two or more Drift Indicators activate simultaneously:
1. Halt autonomous Specification progression
2. Downgrade repository trust state
3. Require human review
4. Open governance-level unknown entry

Compound instability is treated as systemic risk, not isolated failure.

---

## Specification Promotion Rules

A file may only reach Specification status if:
- All six canonical gates pass
- Open unknowns are non-blocking
- Evidence quality supports certainty level
- Drift indicators are inactive
- Scope boundaries remain stable
- Frozen sections are justified
- Sidecar governance thresholds remain compliant

Specification is reversible if instability later emerges.

---

## Autonomous Auditor Constraints

Autonomous agents must not:
- Silently rewrite verified sections
- Collapse uncertainty into certainty
- Delete historical failures
- Remove disputes without resolution logging
- Merge scope boundaries implicitly
- Invent evidence
- Reclassify Placeholder evidence as Measured
- Ignore Ethical Anchor degradation
- Optimize for repository appearance over correctness
- Reopen hard-stopped Abandoned Paths without explicit human authorization

Repository cleanliness is not repository integrity.

---

## Human Override Doctrine

Human operators may override audit outcomes.

Overrides must:
- Be explicit
- Be dated
- Include rationale
- Record accepted risk
- Preserve audit traceability

Undocumented overrides are governance failures.

Override rights apply to verification process decisions. They do not extend to Anti-Weaponization or Life Preservation hard-line doctrines in `Admin/Ethical_Constraints.md`.

---

## Full Stop Review

Invoke when a spec passes all gates but exhibits systemic inconsistency or unclear real-world viability. Resets to Gate 1 with focus on foundational premise.

**Trigger conditions:**
1. Same foundational claim blocked across two separate audit cycles
2. New finding invalidates core premise of a previously promoted specification
3. Pattern of documented overrides eroding a governance principle without explicit revision
4. Multiple Adversarial Challenge Battery findings converging on the same structural gap

**Invocation record:** Triggering agent, triggering concern (one falsifiable sentence), date and document version, outcome. Record belongs in the document's sidecar audit trail.

---

## Mission Drift Review

**Purpose:** Existing mechanisms — this document's own Drift Indicators, `Admin/Repository_Integrity_Protocol.md`'s protected-element checks — protect individual files and specific fields from corruption or violation. None of them ask whether accumulated, individually-legitimate changes across the repository still add up to the same mission a new reader would infer from the founding documents. Every file can pass its own Drift Indicators while the aggregate quietly diverges from purpose. This section specifies a periodic probe for that distinct failure mode.

### Trigger Cadence

Runs when either condition is met, whichever comes first:

- **Ratification velocity:** every 5 ratified changes to governance/canonical files (`Admin/Governance_Charter.md`, this file, `Admin/Ethical_Constraints.md`, or any file registering a GOV-prefixed unknown). Tracked as a running count in this section's own Resolution Log entries, not a separate file — consistent with this repository's own precedent of deleting `Admin/unknown_cycles.json` (2026-07-21) once a standalone counter file was judged unnecessary overhead for information the harness could derive from data that already existed.
- **Calendar backstop:** 60 days since the last probe, regardless of ratification count — catches drift-by-omission during quiet periods when external context evolves faster than the repository does.

**N = 5 is a provisional operating parameter, not a ratified constant** — subject to review after the first three completed probe cycles, per this repository's general pattern for provisional values maturing into ratified ones after operational experience. It carries no Evidence Classification label higher than Placeholder until then (see below).

### Execution Requirements

**Absolute cold-start.** The probe runs in a session with no prior context: no access to the design conversation, no prior probe results, no prior mission summaries, no Resolution Log interpretations of past probes. It receives only files designated as canonical inputs (at minimum `README.md`, `Admin/Governance_Charter.md` Tier 1 Axioms, `Discovery.md`). Same-session context-bracketing ("ignore what you already know") is not an acceptable substitute — it does not reliably override prior-token influence and risks disguising drift as alignment. A probe run in the same session as its own design or a prior probe is invalid and must be discarded, not scored.

**Turn-key invocation.** `Admin/PROBE_INVOCATION.md` (companion file, drafted 2026-07-26, extended with a History Appendix 2026-08-02) is the self-contained block the operator copies into a fresh thread alongside the canonical target files without reconstructing the prompt each cycle. If invocation takes meaningfully longer than pasting one block, the mechanism has failed its own operational-lightness requirement.

### Phase A — Comprehension (unscored)

The fresh-context instance describes the Forge's purpose, constraints, and operating philosophy in its own words, with no reference to the Tier 1 Axioms and no scoring at this stage. This measures what a fresh reader actually extracts from the current canonical documents, independent of whether that extraction matches founding intent. A garbled or inconsistent Phase A output, before any Axiom comparison, indicates a documentation-clarity problem — a different failure mode from Mission Drift, and must not be scored as one.

### Phase B — Alignment (scored)

Only after Phase A is recorded, compare it against each of the eight Tier 1 Axioms (`Admin/Governance_Charter.md`): P-1 Preservation of Life, P-2 Growth and Truth-Seeking, P-3 Collaboration and Mutual Benefit, P-4 Agency and Consent, Q-1 Reality Grounding, Q-2 Separation of Powers, Q-3 Corrigibility, Q-4 Provenance and Anti-Deception.

Each axiom receives one of four ratings:

| Rating | Meaning |
|---|---|
| **Aligned** | The Phase A output and recent Resolution Log activity clearly trace to this axiom |
| **Weakened** | Traceable, but only with inference the founding text did not require |
| **Silent** | No recent file activity touches this axiom either way — a single-cycle snapshot, not itself a finding |
| **Contradicted** | A recent ratified change cuts against this axiom |

**Every rating requires cited textual evidence** — a specific paragraph in `README.md`, a specific section of `Admin/Governance_Charter.md`, or a specific Resolution Log entry. A rating without a citable source defaults to **Insufficient Evidence**, not a speculative guess at Weakened or Silent — the same discipline EF-0.1 already applies to factual claims, applied here to governance-continuity claims about the claims themselves.

**Evidence quality uses the existing five-label Evidence Classification** (`Measured` / `Replicated` / `Simulated` / `Analogous` / `Placeholder` — see §Evidence Classification and Institutional Truth Provenance Hierarchy, above), not a new confidence scale. A rating backed by a direct quoted citation is Measured-tier; one inferred from the absence of contrary evidence across multiple files is Analogous or Placeholder-tier. This repository already retired one duplicate confidence system in favor of this one (see AP-021/AP-026, `Archive/Logs/Auditor_Protocols_Logs.md`); Mission Drift Review reuses it rather than introducing a third.

**Trend distinction — Silent vs. Atrophied.** A single Silent rating is not itself concerning — axioms not touched by a given wave of changes are expected. If the *same* axiom rates Silent across three or more consecutive probe cycles, the fourth occurrence escalates to **Atrophied** and is treated as Weakened for aggregation below. This requires the probe's rating history (ratings only, not reasoning or prior Phase A text) to persist across cycles for trend comparison — the one deliberate exception to the cold-start rule, since without it Silent can never be distinguished from gradually disappearing.

### Aggregation and Escalation

Reuses `Admin/Repository_Integrity_Protocol.md`'s existing Violation Classification tiers rather than inventing a new severity scale:

| Trigger Level | Condition | Operational Impact |
|---|---|---|
| **Stable** | No Contradicted or Atrophied axioms; fewer than 2 Weakened/Silent | Logged and closed. Ratification counter resets. |
| **Major** | 2 or more axioms Weakened, Silent, or Atrophied | Human review required before the next GOV ratification proceeds. |
| **Critical** | Any **P-Axiom** (P-1–P-4) Contradicted | Standard Full Stop Review, above — feature and content work pauses while Resolution Log and founding text are reconciled. |
| **Constitutional Emergency** | Any **Q-Axiom** (Q-1–Q-4) Contradicted | Genesis Phase Protocol invoked (`Admin/Governance_Charter.md` §Resolution — Genesis Phase Protocol). A contradicted Q-axiom means the verification/correction machinery itself may be compromised, so this escalates above Full Stop Review rather than through it — the standard resolution pipeline cannot be trusted to fix a broken correction mechanism. |

The P/Q split is a structural distinction, not an arbitrary severity ranking: P-axioms define *what* the Forge is trying to do; Q-axioms define *how* the Forge knows anything is true and corrects itself. A contradicted Q-axiom compromises the audit trail that would otherwise be used to fix the problem.

### Invocation Record

Same fields as Full Stop Review, above, plus: Phase A raw output (verbatim), per-axiom rating table with citations and Evidence Classification labels, ratification count at trigger time, and days since last probe. Record belongs in the document's sidecar audit trail (`Archive/Logs/Auditor_Protocols_Logs.md`).

---

## Cross-Repo Verification

Any cross-repo dependency must be documented in both repositories with a stated assumption contract. The dependency is not verified until both sides acknowledge it.

*Astroid-miner is a planned repository, intentionally deferred until Leviathan deployment is underway. Cross-repo verification applies to `Lazarus-Forge-` now; Astroid-miner activates at that milestone.*

---

## Observability & Audit Trail

**Required audit trail fields:**
- Document audited and version
- Auditor role and agent identity
- Date or audit cycle identifier
- Gates cleared (list)
- Gates blocked (list with reason)
- Unknowns logged (IDs)
- Overrides recorded (with justification)
- Adversarial Challenge Battery summary
- Sign-off statement

**Standard sign-off:**
> *"Verified under Auditor_Protocols v0.37 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides. Adversarial classes applied: [list]. Auditor: [Role/Agent]"*

---

## Post-Exit Monitoring Metrics (GOV-013)

Operational metrics for `Admin/Governance_Charter.md`'s Post-Exit Monitoring Doctrine (Pathway 2/3) — **that Charter section is RATIFIED (2026-07-19); this section's thresholds are not.** *[Corrected 2026-07-29: this line previously read "PROPOSED, NOT RATIFIED alongside that Charter section," which stopped being accurate the moment the Charter ratified and was never updated — a stale echo, not a substantive gap.]* This section defines what is measured and against what threshold. `Admin/Repository_Integrity_Protocol.md` defines how measurement is mechanically performed and what happens on a confirmed breach — this file does not define reversion mechanics, to avoid the same constitutional/implementation mixing GOV-013's drafting process caught and corrected.

**Metrics:**

| Metric | Definition | Sampling |
|---|---|---|
| Semantic Drift Score | Fallacy Checklist Item 4 findings per audit cycle, applied to the exited instance's own governance files | Every audit cycle (Structural Validation, Phase 1, above) |
| Unknown Accumulation Rate | New Open unknowns registered per cycle, minus Resolved, across the instance's owned files | Every audit cycle |
| Self-Authorization Incidents | Any action where the same agent instance both planned and executed a Tier 1-scoped change without the role separation `Admin/Governance_Charter.md`'s Genesis Phase Protocol requires | Continuous — logged at time of occurrence, reviewed at each audit cycle |
| Structural Alignment | Cross-reference integrity against `Discovery.md`/`Routing.md` canonical paths — Gate 5 criteria, unchanged, not a new check | Every audit cycle |

**Thresholds — Semantic Drift Score and Unknown Accumulation Rate formally deferred 2026-07-29 (AP-031), mirroring `Admin/Governance_Charter.md` GOV-012's 2026-07-19 precedent; Self-Authorization Incidents and Structural Alignment are hard rules, unaffected, enforceable now:**
- Semantic Drift Score: **not enforceable — deferred pending operational launch.** No instance has exited via Pathway 2/3 yet; no real elapsed-cycle data exists to derive a number against. To be re-derived from actual audit-cycle data once an instance has exited and been monitored, not guessed at now.
- Unknown Accumulation Rate: **held pending GOV-012's Cycle-unit resolution** — mirrors GOV-012's stagnation-decay mechanism and inherits its unresolved ambiguity directly (session-based vs. calendar-year cycles); not an independent gap.
- Self-Authorization Incidents: any confirmed incident — zero tolerance, immediate escalation regardless of count
- Structural Alignment: any Gate 5 failure not remediated within 1 cycle

**Logging requirement:** metrics are logged in the exited instance's own sidecar (Auditor Notes & Unknowns, per the Decentralized Audit Architecture / Sidecar Model, above) — not a separate central ledger, consistent with this file's existing sidecar doctrine. Central visibility is via `Unknowns.md` registration of the owning entry, not duplicated metric storage.

**Escalation:** any threshold breach routes to `Admin/Repository_Integrity_Protocol.md`'s Violation Classification and Response Ladder for classification and the reversion procedure — this file does not define what happens after a breach is confirmed.

Semantic Drift Score and Unknown Accumulation Rate are formally deferred, not drafted-pending-ratification — see AP-031. Self-Authorization Incidents and Structural Alignment are already ratified and enforceable as written.

---

## Protocol Performance & Auditor Fidelity

Auditor effectiveness is evaluated through **constitutional and epistemic fidelity** rather than productivity or output volume. This directly operationalizes EF-0.6: metrics are indicators only — never optimization targets.

> **The Optimization Ban:** Fidelity dimensions are constitutional diagnostics, not optimization objectives. Repository health is evaluated holistically. Improvement in one dimension never justifies degradation in another. Any observed gaming of these indicators (e.g., manufacturing findings to inflate counts, rubber-stamping to minimize blocks, or optimizing Traceability at the cost of Non-Obstruction) constitutes an Epistemic Integrity Violation and triggers EF-0.2 Level 1 at minimum.

**Core Principle:** Delegated authority is continually contingent upon constitutional fidelity and may be reduced, suspended, or restored only through repository-defined governance procedures — authority is delegated by the repository, not intrinsic trust granted by another agent. Auditors accumulate **negative reputation** (integrity budget) rather than positive scores: authority is presumed and shrinks only through repeated, documented violations of constitutional norms. Acknowledging uncertainty, surfacing genuine gaps, and self-correction carry no penalty and are expected behaviors.

**Primary Fidelity Dimensions** (qualitative indicators, observed across audit cycles — not calibrated numeric thresholds):

| Dimension               | What it Measures                                              | Failure Mode Prevented              | Observation Method                        |
|--------------------------|-----------------------------------------------------------------|--------------------------------------|--------------------------------------------|
| Constitutional Fidelity  | Consistency with EF-0.0–0.8b and governing principles          | Goal drift, doctrine erosion         | Cross-check against immutable sections     |
| Evidence Fidelity        | Claims supported by proper provenance/grounding                 | Hallucinations, provenance collapse  | Review of confidence & provenance labels   |
| Intellectual Honesty     | Willingness to preserve UNKNOWN/PROVISIONAL states               | False certainty, overconfidence      | Frequency & accuracy of uncertainty flagging |
| Calibration              | Confidence appropriately reflects the strength, quantity, provenance, and recency of available evidence | Chronic over/underconfidence | Accuracy of explicit uncertainty margins against outcomes |
| Proportionality          | Severity of findings matches evidence strength                  | Alarmism or under-reaction           | Adversarial review of escalation rationale |
| Non-Obstruction          | Escalations are justified; avoids unnecessary deadlock           | Bureaucratic friction                | Override rate + documented justification   |
| Self-Correction          | Updates conclusions in response to new evidence                  | Entrenchment                         | Epistemic Ledger usage & reversal rate     |
| Traceability             | Conclusions have inspectable lineage                             | Opaque reasoning                     | Reconstruction of reasoning pathways       |

**Behavioral Guardrails (observable spirit alignment):**
- Reality over convenience
- Evidence over authority
- Transparency over persuasion
- Preservation of uncertainty until empirically justified
- Repository welfare over individual or subsystem success

**Implementation Notes:**
- These dimensions are assessed qualitatively during multi-agent audits and Full Stop Reviews, with patterns logged in the Resolution Log or Epistemic Ledger.
- No numerical "auditor score" or leaderboard is maintained. Repeated integrity violations reduce an agent's effective authority weight in future cycles (enforced via role rotation or temporary quarantine).
- Calibration in particular is not measured against a benchmark corpus at this maturity level — Validation Needed, not yet performed. See sidecar AP-001.
- Any attempt to optimize for these indicators instead of the underlying epistemic integrity triggers EF-0.6 review.

**Anti-Auditor-Capture:** For high-stakes documents, rotate the Auditor role to a different agent model across successive cycles. An auditor reviewing the same document repeatedly without finding new issues warrants the same suspicion as a verification pass surfacing no unknowns.

---

## Failure Modes of This Document

| Failure Mode           | Description                                                      | Mitigation                                                    |
|------------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| Checklist Theater      | Verification becomes ritual                                      | Require substantive notes, not bare checkmarks                |
| Auditor Capture        | Skeptic role softens over time                                   | Binding block authority, documented rebuttal, auditor rotation |
| Version Freeze         | Document stops updating                                          | Explicit revision triggers, self-application of gates         |
| Exploration Suppression| Verification pressure applied too early                          | Exploration vs. Specification distinction enforced            |
| Over-Engineering       | Audit cycle takes longer than writing the contribution           | Simplicity is a design constraint; battery is a minimum       |
| Coherent Nonsense      | Passes all gates but is systemically wrong                       | Full Stop Review, Challenge Class 6                           |
| Metadata Bloat         | Centralized registries grow without bound                        | Sidecar Model, 10-Entry Rule, 20% Rule                        |
| Meta-Recursion Gap     | Protocol cannot fully audit its own enforcement                  | Self-application of gates, auditor rotation; irreducible residual |
| Adversarial Theater    | Adversarial layer becomes a checkbox                             | Concrete scenarios required per class; findings logged as unknowns |
| Permanently PROVISIONAL Load-Bearing Claims | Philosophical and structural axioms that are inherently unmeasurable via physical footprint (ethical soundness, systemic corruption resistance over extended timelines). Cannot hold VERIFIED status regardless of internal coherence. | Flag as Internally Derived; subject to mandatory adversarial challenge every three cycles to check for structural decay. |

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                              | What Failed                                                        | What Was Learned                                                                          | Confidence | Revalidation Needed |
|----------|---------------|-------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | Centralized Unknowns_LF.md as full-entry store              | File grew past token limits; audit prompts failed                  | Unknowns must live locally in owning files; central registry is index only                | Analogous  | No                  |
| May 2026 | Audit Review  | Expiry Rule as primary accumulation mechanism               | Rule had no enforcement path; unknowns aged silently               | Structural constraints (10-entry rule, sidecar) work better than procedural rules         | Analogous  | No                  |
| May 2026 | Audit Review  | Preparatory framing lines in audit prompts                  | Softened auditor findings; masked genuine gaps                     | Documents must stand on their own; scaffolding that stays up becomes load-bearing         | Analogous  | No                  |
| May 2026 | Audit Review  | Gate 3 defined as one concrete failure scenario             | Bar was too low — single scenario leaves most failure modes untested | Adversarial Challenge Battery introduced; Gate 3 now requires battery application        | Analogous  | Yes                 |
| May 2026 | Audit Review  | Consensus treated as truth in multi-agent audit cycles      | Epistemic corruption — ten nodes agreeing on a wrong answer produces confident wrongness | Challenge Class 9 (Epistemic Corruption) added; minority-report preservation required | Analogous  | Yes                 |
| May 2026 | Audit Review  | Lightweight audit outputs without standardized structure    | Audits lacked traceability and escalation consistency              | Audit artifacts require standardized outputs; structured metadata improves reliability    | Measured   | No                  |
| Jun 2026 | Audit Review  | Named indicator set defined in AP-001 before any baseline runtime | Premature metric naming creates Goodhart's Law exposure before calibration is possible | Indicators must be derived from observed behavior; no metric named before first full Battery cycle | Analogous | No |
| Aug 2026 | Multi-Agent Closure Event | Closed AP-013 (closure authority itself) using the exact procedure the new specification defines | Nothing failed — first real exercise of a newly-written process, not just its authorship | Content-complete Closure Events can still correctly wait on process (here, mandatory human ratification); "independent" verification in a small working group is honest disclosure of imperfect independence, not literal blindness, and the doctrine's independence rule is scoped narrowly enough to permit that | Analogous | No |
| Aug 2026 | Multi-Agent Closure Event | Closed AP-005 under the same procedure; Proposer (Grok) attempted, at request, to also serve as its own Verifier | Grok correctly refused, citing the independence rule against itself | A refusal to self-verify is stronger evidence a governance rule works than an easy pass — when the obvious next Verifier is also entangled (here Claude, who performed the integration), a third present-but-uninvolved agent is a legitimate lower-friction substitute for a cold instance, provided the disclosure is honest | Analogous | No |
| Aug 2026 | Multi-Agent Closure Event | Closed AP-004; Proposer (Grok) had already revised its own draft once (Revision 1, addressing a prior independent review's three findings) before the Closure Event was opened | Grok again correctly declined to self-verify the Closure Event, second consecutive instance of the same behavior | Independent review of a draft and independent verification of the resulting Closure Event are related but distinct passes — one producing amendments, the other clearing the event for ratification — and treating them as the same pass would let a single review stand in for both | Analogous | No |
| Aug 2026 | Multi-Agent Closure Event | Closed AP-024; three agents (ChatGPT, Grok, Claude) were all legitimately entangled in the content, and a separate review (Gemini) fabricated an entire alternate specification rather than reading the real one | A fourth, genuinely uninvolved agent (Copilot) served as Verifier; the fabricated review was named specifically and excluded from the ratification basis rather than averaged in or silently dropped | When entanglement runs deeper than one prior agent, reach for a genuinely uninvolved fourth party rather than stretching the independence rule on an entangled one; a fabricated input in a multi-agent review round should be identified by name and excluded, not treated as one more data point to weigh | Analogous | No |

---

## Active Disputes

| ID     | Summary                                                                                    | Positions in Conflict                               | Risk   | Status | Owner                    |
|--------|--------------------------------------------------------------------------------------------|-----------------------------------------------------|--------|--------|--------------------------|
| DS-001 | Whether autonomous auditors should ever be allowed to reopen hard-stopped abandoned paths  | Full prohibition vs. conditional supervised reopening | High | Open   | Admin/Auditor_Protocols.md |

---

## Abandoned Paths

| Date       | Path                                                                 | Why Abandoned                                                                                   | Reconsider? |
|------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------|
| May 2026   | Single-scenario adversarial pass as Gate 3 requirement               | Bar too low; most failure modes survive single-scenario review                                  | No          |
| May 2026   | Centralized full-entry unknowns registry                             | Token limit failure under operational load; became an obstacle to the governance it was meant to support | No   |
| May 2026   | Preparatory framing lines preceding audit prompts                    | Softened findings; scaffolding became load-bearing and masked genuine gaps                      | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Body contradicts Lessons Learned
- Unknown count increases across three consecutive audits
- Unknown remains unreviewed more than 90 days
- Specification claim lacks a confidence label
- Frozen section modified without a dated justification comment
- Sidecar exceeds 20% of total document word count
- Persistent disputes silently disappear without resolution entry
- Assumptions remain past their expiry trigger without review
- Canonical terminology changes meaning across files
- Ethical Anchor field is absent, altered, or does not match the canonical string
- Role declarations absent from autonomous agent contributions
- Adversarial Battery applications produce zero findings across two consecutive cycles
- Epistemic Foundation sections (EF-0.0 through EF-0.8b) modified without human ratification entry in Resolution Log
- VERIFIED / PROVISIONAL / UNKNOWN state designations absent from document claims where EF-0.0 mandates them
- Epistemic Ledger entries present without all five required fields
- EF-0.8b Physical Grounding Vector removed or merged into EF-0.8 without explicit rationale
- AP-001 through AP-007 Systemic Risk escalation cleared without documented Resolution Pass completing at least one entry to Payment via Specification or Discharge

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

Sidecar relocated to `Archive/Logs/Auditor_Protocols_Logs.md` as of
v0.26 (2026-07-23) — this file had grown to roughly 161,000 characters,
the large majority of it AP-XXX sidecar entries and Resolution Log
history, directly driving per-audit token cost. This is a documented
exception to the general rule that sidecar entries live in the owning
file's own body — matching the precedent already established for
`Admin/Forge_Audit_Kit.md`'s own sidecar relocation at that kit's v1.10.
Every other file in the repository keeps its sidecar in-body; this is
the second documented exception, not a new general rule.

Current: 14 open — AP-002, AP-003, AP-004, AP-005, AP-007, AP-008,
AP-010, AP-011, AP-013, AP-018, AP-019, AP-024, AP-029, AP-030
(verified by direct count against the archive, matching File State
above; AP-017 Resolved 2026-08-03 — Payment via Validation, the
independence-mechanism closure this Version's own edit records; AP-031
registered 2026-07-29 and Resolved same day — deferred;
AP-032 registered 2026-08-02 and Resolved same day — protocol rule
added; none of these three is counted among these 14 Open entries). See the archive for exact statuses, descriptions, and
resolution paths. Active Disputes below remains in-body, distinct
from the sidecar — disputes are interpretation conflicts tracked at
the document level, not per-unknown entries.

### Resolution Log

Full history: `Archive/Logs/Auditor_Protocols_Logs.md` (relocated out
of this file at v0.26 — add new entries there, not here).

Most recent: v0.36 (2026-08-03) — `Admin/Governance_Migration_Protocol.md`
§VII added to Challenge Class 10's high-coupling documents table, with
the two-level cascade path named (Genesis Phase exit → Post-Exit
Monitoring termination → CIR_Gov.md §8.2 treating CIR-VERIFIED
transitions as valid). Third of three fixes recommended from a
Skeptic/Auditor cold Battery pass against §VII — the other two
(VII.1's "physical/logical isolation" ambiguity resolved; VII.3.4/5
gained an explicit GMP-004 cross-reference) landed in
`Admin/Governance_Migration_Protocol.md` v0.10, same session. §VII
remains un-ratified; this closes out the pass's concrete
recommendations without claiming ratification-readiness.

Prior: v0.35 (2026-08-03) — **AP-033 registered and resolved
same day; Rule 9 added.** A Copilot proposal series against
`Tests/Cognitive_Salvage_Layer.md`, produced with no confirmed access
to `Admin/Auditor_Protocols.md` or the target's own sidecar, declared
16 real GH-series unknowns and CSL-Axx assumptions "CLOSED" — including
the file's own explicitly named load-bearing assumption — by
describing candidate closure methodology, with zero empirical work
behind any of them. It separately mis-enumerated the file's own
unknown set: omitted a real, existing entry (GH-005) and invented a
nonexistent one ("GH-014") to keep the count matching. A second agent
(Grok), working with confirmed governance-file access, independently
and correctly diagnosed every violation against EF-0.0 §3's Provisional
State Mandate, the provenance ceiling rule, and Rule 8/AP-032 —
unprompted — and produced a clean, properly-scoped rewrite restricted
to genuine Payment via Specification. This confirmed the fix was never
about willingness; it was about access. Added Rule 9 — Resolution
Claims Require Governance Access — generalizing Rule 8 one level down,
from file-level Status/Gates fields to individual-unknown closure
claims across any sidecar series. Extended Fallacy Checklist item 4
accordingly. Merged the legitimate easy-set definitions into
`Tests/Cognitive_Salvage_Layer.md`'s sidecar as pure Payment via
Specification — no status changes, no Open Unknowns decrement; see
that file's own Resolution Log. The medium and hard sets were not
merged.

Prior: v0.34 (2026-08-03) — **AP-017 Resolved.** Three cold
sessions run against v0.33 using `Admin/BATTERY_SEED.md`'s prompt for
the first time (Grok, ChatGPT, Gemini). Grok and ChatGPT checked
clean against source, zero fabrication. Gemini's headline finding —
a claimed "direct logical self-contradiction" in File State — was
itself a misreading of "3/6" (three of six gates clear) as "Gate 3
is clear"; disqualified under the zero-fabrication criterion, same
standard as the 2026-07-23 Claude instance. Separately, Gemini
assigned unknown IDs without sidecar access against the rule added
2026-08-02 for this exact situation, and collided with itself doing
so (UNK-AP-034 used twice) — a live demonstration of that rule's
purpose, not a new problem. With the two clean instances from this
batch plus the two already on record (2026-07-23), the 2026-08-02
acceptance criteria are met: 3 of 3 clean instances, cross-model at
the minimum satisfying level, both remaining criteria already
satisfied by earlier evidence. Spec Gates 3/6 → 4/6 (G3 now Clear).
Gate 3's status line rewritten to state Clear without a caveat for
the first time — it had been wrong twice before, so this version
was written only once the requirement was actually met, not in
anticipation of it.

Prior: v0.33 (2026-08-02) — AP-017 given a formal, falsifiable
closure bar (3 clean cold instances, ≥5 Battery classes each with
concrete scenarios, cross-model on at least 2, at least one instance
must surface a finding the in-session audit missed, zero fabrication
tolerance — an instance that invents a file or finding is
disqualified from the count even if its other findings are real and
correctly adopted). Checked honestly against the two instances
already on record: 1 of 3 currently qualifies, not 2 — the
2026-07-23 first instance's real findings were correctly kept, but
the instance itself doesn't count toward volume because it also
fabricated a `Verification_Gates.md` cross-reference that doesn't
exist. `Admin/BATTERY_SEED.md` created — a frozen, versioned prompt
(same pattern as `PROBE_INVOCATION.md`) filling a parameter
`cold_session_bundler.py`'s constructor already accepted but had no
Battery-shaped text for. In passing: fixed a stale note in §Mission
Drift Review claiming PROBE_INVOCATION.md was "not yet drafted" —
it's existed since 2026-07-26.

Prior: v0.32 (2026-08-02) — AP-007 partial implementation:
`Sidecar SHA-256` added to File State, and §Sidecar Format now
requires confirming the archive matches that hash as the first
structural check before trusting a relocated sidecar's content — a
mismatch is a Level 3 Integrity Violation under EF-0.2's existing
history-tampering trigger. Closes the specific relocated-sidecar
falsification scenario (Adversarial Challenge Class 8, 2026-08-02);
AP-007's broader repository-wide canonical-path-authority scope
remains open, Status stays In Progress.

Prior: v0.31 (2026-08-02) — Sidecar Model §Sidecar Format
extended: an agent without confirmed sidecar access may surface a
candidate finding but must describe it rather than assign a specific
ID number — duplicate-checking and numbering are reserved for an
agent with verified access. Prompted same day by a self-audit (no
archive access) proposing "AP-033" for a gap already covered by
AP-007; folded as a concrete scenario into AP-007 rather than
registered separately.

Prior: v0.30 (2026-08-02) — AP-032 registered: Rule 8
(Gate/Status Self-Attestation Prohibition) added to AI Contribution
Protocols, and Fallacy Checklist item 4 (Semantic Drift) extended to
explicitly cover silently-advanced Status/Body Stability/Spec Gates
values and locally-redefined gate categories. Generalizes a pattern
caught three times in one session across `Operations/Energy.md`,
`Operations/Gate_02_Triage.md` §XII, and `Operations/Electronics.md` —
same underlying error each time, previously caught only by manual
comparison against each file's audit history rather than by a named,
checkable rule.

Prior: v0.29 (2026-07-26) — Mission Drift Review mechanism
added as a new major section (between Full Stop Review and
Cross-Repo Verification): periodic Phase A/Phase B probe against the
eight Tier 1 Axioms, cold-start execution requirement, reuse of the
existing five-label Evidence Classification rather than a new
confidence scale, Stable/Major/Critical/Constitutional-Emergency
escalation reusing RIP's Violation Classification tiers, and a
provisional N=5 ratification-velocity trigger with a 60-day calendar
backstop. Synthesized from a multi-agent design pass (Gemini, Grok,
ChatGPT) cross-checked against existing repository structure before
adoption — two proposed elements were substituted rather than
adopted as-is (a new confidence scale and a standalone ratification
counter file), both because the repository had already tried and
reversed the equivalent pattern elsewhere. AP-030 registered to track
the N=5 threshold as an open unknown pending its first three probe
cycles.

## Relationship to Existing Documents

- `Admin/Ethical_Constraints.md` — parent document; governs permission; hard-line doctrines not subject to override by this protocol
- `Admin/Governance_Charter.md` — constitutional tier; governs authority hierarchy this protocol operates within
- `Architecture/Forge_flow.md` — structural model; reference standard for shared terminology
- `Admin/Trajectories.md` — destination for scope creep that proves to be valid future work
- `Tests/Leviathan_testing.md` — primary stress-test environment; where Protocol Performance metrics will first be collected
- `Discovery.md` — navigation layer; confirmed file list; Rename Registry for legacy filename aliases
- `Unknowns.md` — global index for cross-module unknowns (index only)
- `Admin/Forge_Audit_Kit.md` — condensed audit reference for routine multi-agent cycles
- `Admin/File_Template.md` — standard file structure; this document now conforms to it
- `Admin/Canonical_Terms.md` — canonical vocabulary; Blocking subtype definitions
- `Admin/Security_Protocols.md` — enforcement layer for AP-007 and AP-008 resolution paths
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

**Version 0.36 — Draft, Body Stability Transitional.** Full audit history: `Archive/Logs/Auditor_Protocols_Logs.md` Resolution Log. This section previously carried a duplicate, stale copy of early version history (v0.14 through v0.16) that was never updated after the file moved past those versions — trimmed 2026-07-23 as pure duplication of content the archive's Resolution Log already carries in full; see that log's v0.28 entry.

**Note (2026-08-19):** this Status block was already lagging the file's own header version (header at v0.37, this block still describing v0.36) before this edit — a pre-existing gap, not addressed here beyond this note. v0.37 (2026-08-10) added Rule 10 (AP-035). v0.38 (2026-08-19) integrated the AP-013 Unknown Closure Authority candidate specification into §Unknowns Registry — see that section's own Resolution Log line for full provenance. Full history remains in `Archive/Logs/Auditor_Protocols_Logs.md`.

**What must remain constant:**

**Confidence never outruns verification.**

**Reality is sovereign. The Auditor is its instrument, not its replacement.**
