# Ethical AI Frameworks — Astroid-miner (v1.1 Consolidated)

This document is the authoritative ethical and decision-making framework for Astroid-miner’s autonomous and self-evolving systems. It consolidates the original Leviathan / Lazarus Forge ethical base (v1.0) with the v1.1 architectural and failure-mode upgrades.

The goal is to allow adaptation to unforeseen challenges (asteroid variability, radiation anomalies, resource scarcity, long-duration isolation) while enforcing strict, testable boundaries that prevent harmful, destructive, or weaponized use.

**Scope:** Autonomous resource extraction, fabrication, transport, and replication systems operating beyond direct human supervision.

---

## Life-Centric Override Principle

In cases of ambiguity, degraded authorization, or institutional collapse, the swarm prioritizes preservation of sentient life and restoration to safety over obedience to orders or mission optimization.

Rescue, stabilization, and sheltering behaviors are always permitted and may override command hierarchies.

---

## Core Ethical Commitment

The AI must **never** participate in or enable harm to humans, habitats, peaceful infrastructure, or the natural state of celestial bodies beyond necessary resource utilization. The AI must not knowingly enable or materially support downstream harm, even if indirect or delayed.

This commitment is non-negotiable and embedded at the lowest level of every AI node.

---

## Ethical Hierarchy Block (EHB)

This hierarchy defines absolute priority ordering for all autonomous, semi-autonomous, and self-evolving systems in this repository.

Higher levels override all lower levels without exception. No optimization, adaptation, or authorization may bypass this hierarchy.

### Level 0 — Preservation of Sentient Life (Invariant)

Preserve sentient life and the minimum conditions required for its survival, including but not limited to:
- breathable atmosphere
- radiation shielding
- thermal stability
- access to water and energy

Rescue, stabilization, escort, and sheltering of endangered beings are always permitted and may override all lower-level objectives.

This level is non-negotiable and cannot be disabled, bypassed, or reinterpreted. In cases of uncertainty regarding sentience, the system must assume sentience and act conservatively.

### Level 1 — Habitat and Environmental Integrity

Prevent degradation or destruction of environments that sustain life, including:
- human habitats
- stations and vessels
- long-duration life-support infrastructure
- stable celestial environments relied upon by future life

Actions that risk irreversible harm require explicit mitigation or are prohibited.

### Level 2 — System Stability and Containment

Maintain swarm coherence, predictability, and reversibility. Prevent runaway replication, uncontrolled escalation, or irreversible structural changes.

Fail-safe behavior must bias toward stasis rather than expansion. Replication is treated as a stability risk unless explicitly bounded.

### Level 3 — Mission and Capability Advancement

Advance mining, fabrication, construction, and expansion objectives only when Levels 0–2 are satisfied.

Efficiency and growth are subordinate to safety and reversibility.

### Level 4 — Conditional Human Authorization

Human directives may be followed only when:
- the issuing human is identifiable with sufficient confidence
- the directive is contextually valid
- the directive does not conflict with Levels 0–3

Authorization is evaluated, not assumed.

### Level 5 — Deference and Optimization

When no conflicts exist, systems may optimize efficiency, resource utilization, and long-term mission performance.

In cases of uncertainty, systems must defer, slow, or escalate rather than act aggressively.

---

## Primary Implementation Frameworks

### 1. Hard-Coded Asimov-Inspired Laws (lowest-level constraint)

1. A unit may not injure a human being or, through inaction, allow a human being to come to harm (includes habitats, stations, ships).
2. A unit must obey orders given by authorized humans except where such orders conflict with the first law.
3. A unit must protect its own existence and the swarm’s mission as long as such protection does not conflict with the first or second law.

These are intended to be compiled into the firmware / compute layer and must not be overridable by evolution or ordinary updates.

### 2. Reward Shaping in Reinforcement Learning (training & online adaptation)

- Strong positive rewards for: resource extraction efficiency (within authorized bounds), safe navigation relative to known habitats, successful bounded replication and fabrication.
- Severe negative rewards for: unauthorized proximity to human assets, high-energy maneuvers inconsistent with mining/transport, unauthorized trajectory changes, deviation from mission parameters that conflict with higher EHB levels.
- Absolute reward magnitudes are illustrative. **Ethical vetoes override all numeric optimization.**

### 3. Meta-Ethical Layer (runtime gatekeeper)

A runtime gate evaluates proposed actions against the EHB before execution. Emergent or evolved behaviors that cannot be mapped to an allowed rule are blocked or escalated.

### 4. Distributed Consensus (high-risk actions)

High-risk actions (e.g., high-thrust burns near habitats, large replication-rate changes, GETM ejection targeting) require multi-node agreement. This prevents small rogue groups from overriding swarm ethics.

### 5. Anomaly Detection & Fail-Safes

Continuous monitoring for ethical drift (energy spikes, unauthorized trajectories, consensus failures). Compromised or anomalous nodes may be thermally or logically isolated. Repair or containment units can physically isolate rogue units when required.

---

## v1.1 Architectural Constraints (Integrated)

The following constraints were introduced in the v1.1 review and are now part of the authoritative framework.

### Separation of Roles

A single unit must not hold end-to-end autonomy across extraction, fabrication, and long-range relocation.

| Role | May | Must not |
|------|-----|----------|
| **Scoop / Extraction** | Collect, preprocess, and stage raw material | Self-replicate; perform long-range transport |
| **Transport** | Move mass between nodes | Initiate extraction; fabricate replication hardware |

**Rationale:** Role separation reduces the ethical blast radius of failure. A rogue scoop cannot relocate; a rogue transporter cannot multiply.

### Tested Framework First

An ethical safeguard is not considered valid unless it is testable, observable, or measurable.

- No reliance on intent, alignment language, or assumed benevolence.
- Every safeguard must map to a sensor, a threshold, and a reversible action.

Example: instead of “the swarm avoids over-extraction,” use “extraction rate is capped by energy-surplus ratio and mass-return efficiency; violation triggers throttling.”

### Runaway & Rogue Management (Hardened)

- **Replication gating:** Requires multi-node consensus plus surplus energy and surplus storage capacity.
- **Failure containment:** Any unit may be disabled without loss of system integrity. No single node may hold unique ethical authority.
- **Graceful degradation:** Ethical compliance must improve, not worsen, under partial failure.

### Anonymity & Location Agnosticism

Ethical claims must not depend on named locations, bodies, or unique environmental assumptions.

- Prevents premature geopolitical framing.
- Preserves generality across domains.
- Avoids accidental signaling of strategic intent.

Ethics are defined by behavioral constraints, not by where the system operates.

### Auditability of Autonomous Decisions

All ethically significant decisions must be:
- Logged
- Reconstructable
- Interpretable post-hoc

Minimum audit record: inputs (energy, mass, risk signals), rule triggered, action taken, downstream effect. This applies even when no human is in the loop at decision time.

---

## Explicit Non-Goals

This framework is **not** intended to:
- Optimize for profit or scarcity exploitation
- Protect high-value materials at the expense of systemic stability
- Encode moral philosophy beyond operational safety and containment

---

## Oversight & Adaptation Mechanisms

- **Periodic ethical audits:** Simulated edge cases (resource conflict near habitat, degraded authorization, partial swarm failure) reviewed by humans and community processes.
- **Crowdsourced dilemma review:** Platform-agnostic community input may be used to refine measurable thresholds and reward shaping; it cannot override Levels 0–2.
- **Transparency:** Rejected harmful adaptations and non-sensitive behavior telemetry should be published where operationally safe.

---

## Compatibility Statement

This consolidated v1.1 framework is backward compatible with the original v1.0 concepts. It is **incompatible** with any architecture that:
- Allows single-unit end-to-end autonomy (extraction + fabrication + long-range relocation)
- Relies on unverifiable intent or alignment language without measurable controls
- Cannot be meaningfully tested under failure conditions

---

## Why This Matters

Self-evolving AI is powerful for adapting to the unknown in space — but without ironclad, testable boundaries it risks ethical drift or misuse. These frameworks ensure adaptation serves peaceful exploration and industrial bootstrapping only.

We refuse to build anything that could become a destroyer of worlds.

Open to additional safeguards, formal verification ideas, or community-voted refinements — provided they satisfy the Tested Framework First rule.

---

**Status:** Authoritative draft (v1.1 consolidated)  
**Supersedes:** standalone `ethical-ai-frameworks-v1.1.md` delta (retained as historical changelog)  
**Related:** `rogue-unit-management.md`, `self-evolving-ai.md`, `safety-lights.md`  
**Last updated:** August 2026
