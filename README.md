# Lazarus Forge

> *The purpose of the Forge is not to make objects.*  
> *The purpose of the Forge is to preserve agency.*

Lazarus Forge is an open, salvage-first framework for turning discarded material, broken equipment, local resources, and accumulated knowledge back into useful capability. It is designed for communities that want to recover more value locally, depend less on fragile supply chains, and build systems that become more capable through documented experimentation.

It combines salvage-first engineering, local manufacturing, resilience, experimental testing, and unusually strict epistemic governance.

The Forge does not optimize for efficiency alone. Efficiency without resilience creates fragile systems. The Forge willingly sacrifices local speed and optimization when doing so increases **recoverability, redundancy, auditability, and graceful degradation.**

The deepest goal is this:

> *Build a civilization that forgets more slowly than it learns.*

---

## What can you do with it?

| If you are… | Start here |
|-------------|------------|
| 🔧 A builder | [`Architecture/Geck_forge_seed.md`](Architecture/Geck_forge_seed.md) |
| 🧪 An experimenter | [`Tests/Field_Logs.md`](Tests/Field_Logs.md) |
| 🧠 A systems thinker | [`Architecture/Forge_flow.md`](Architecture/Forge_flow.md) |
| 🔍 A skeptic | [`Admin/Auditor_Protocols.md`](Admin/Auditor_Protocols.md) |
| 🌎 A community organizer | [`Architecture/Facilities.md`](Architecture/Facilities.md) |
| 🤖 An AI researcher | [`Admin/Computational_Institutional_Reasoning.md`](Admin/Computational_Institutional_Reasoning.md) |
| 💡 Just curious | [`Discovery.md`](Discovery.md) |

---

## Three ways to participate

**Build something.**  
Try an existing protocol or adapt the architecture to your environment. Begin with the minimum viable seed or the Site Initialization Checklist.

**Bring evidence.**  
A failed experiment is useful. A measurement that contradicts the doctrine is especially useful. Log results in [`Tests/Field_Logs.md`](Tests/Field_Logs.md).

**Challenge the assumptions.**  
Find something that shouldn't work. Find a governance failure. Find a hidden assumption. Open an issue.

---

## Your first Forge experiment

You don't need a facility to participate.

1. Find one discarded object.
2. Identify the highest-value function, component, or material it contains.
3. Record what you think can be recovered.
4. Record what you were wrong about.
5. Estimate the energy and tools required.
6. Add the result to [`Tests/Field_Logs.md`](Tests/Field_Logs.md).

You have now contributed experimental evidence to the Forge.

---

## Don't Trust the Forge

The Forge is designed to be challenged.

If an experiment contradicts an assumption, that is a contribution — not a failure to follow the project.

The repository deliberately records unknowns, failed experiments, disagreement, uncertainty, and unresolved claims.

You do not have to agree with Lazarus Forge to participate in it.  
In fact, disagreement backed by evidence is one of the most useful forms of participation.

> The most valuable contribution may be a result that proves us wrong.

---

## Current status

**Alpha — active development**

The Forge currently has:

- a defined seven-gate operational architecture (architectural model
  complete; physical validation is a separate, ongoing question — see below);
- a formal governance and audit framework;
- a live registry of unresolved questions;
- experimental pathways covering material, water, biological, energy, and
  knowledge recovery;
- explicit separation between specified doctrine and experimentally
  validated capability.

**Not yet demonstrated:**

- physical validation of most gates at production scale;
- energy-independent or net-positive economics;
- autonomous operation without human oversight;
- self-replication;
- any off-world or interstellar capability. These appear in the long-term
  vision below as a research trajectory, not a current claim.

**What is real right now, at a glance:**

| Capability | State |
|---|---|
| Seven-gate operational architecture | Specified |
| Salvage-first doctrine | Specified |
| Governance and audit framework | Specified, in active use |
| Experimental pathways (material, water, biological, energy, knowledge) | Active / experimental |
| Physical gate validation at scale | Incomplete |
| Energy independence | Not demonstrated |
| Autonomous operation | Not demonstrated |
| Self-replication | Not demonstrated |
| Off-world / interstellar deployment | Research trajectory |

This table is a manual, human-facing orientation — a fast answer to "what's
actually real." It is distinct from `Automation/integrity_check.py --health`,
which mechanically checks repository consistency (metadata, cross-references,
active unknowns) and does not attempt to judge physical readiness; neither
replaces the other.

**Important:** much of the system remains experimental. An architectural
specification is not evidence that the corresponding physical capability
has been demonstrated. This distinction — specified versus demonstrated —
is load-bearing throughout the repository, not just in this section.

For the detailed development state, see [`Unknowns.md`](Unknowns.md) and [`Discovery.md`](Discovery.md).  
Primary remaining gaps include long-term constitutional stability (GOV-005), human override authentication (GOV-006), and the operational hardware unknowns tracked in `Unknowns.md`.

No claims of full automation, self-replication, or net-positive economics are made without measurement. All quantitative figures carry confidence levels per [`Admin/Auditor_Protocols.md`](Admin/Auditor_Protocols.md).

The system is incomplete. Incompleteness is honest.

---

## How to participate (details)

If this idea is useful, a GitHub star helps other people find it.

But the more valuable contribution is evidence.

Tell us what worked. Tell us what failed. Tell us where the assumptions break.

| Signal | Means | Where |
|--------|--------|--------|
| ⭐ Star | This is interesting or useful | GitHub star |
| 🐛 Issue | Something is wrong | GitHub Issues |
| 💡 Discussion | I have an idea | GitHub Discussions, or r/InnovativeAIChats |
| 🔬 Field data | I tried this in the real world | `Tests/Field_Logs.md` — see there for no-GitHub-required submission, or post in r/InnovativeAIChats |
| 🔧 Improvement | I improved the doctrine or code | See [`CONTRIBUTING.md`](CONTRIBUTING.md) |

Stars, bugs, ideas, evidence, and code changes are separate channels. Real-world observations — including failures — belong in `Tests/Field_Logs.md` and become part of the project's epistemic record when submitted with enough structure to be checked.

---

## The Problem

Modern industrial and recycling systems:

- Destroy functional components prematurely
- Are energy-intensive and often net-negative
- Depend on centralized, high-capital infrastructure
- Reinforce planned obsolescence rather than countering it
- Concentrate critical material supply chains in ways that create geopolitical leverage

As a result, vast amounts of usable mechanical and electromechanical value are permanently lost — and the communities closest to that loss have the least power to recover from it.

The Lazarus Forge exists to interrupt that pattern. At any scale, with whatever is on hand, anywhere in the world.

---

## The Doctrine of Preservation

The Forge operates on a strict, salvage-first hierarchy. Reduction — shredding, melting, downcycling — is an admission of failure. It is executed only when no higher-order value remains, and only under full accountability and thermodynamic tracking.

1. **Preserve Function** — Keep the component doing exactly what it was designed to do
2. **Preserve Assemblies** — Maintain the relationships between working components
3. **Preserve Components** — Salvage individual parts for alternative integration
4. **Preserve Materials** — Reclaim raw elements for fabrication
5. **Destroy** — Relinquish to entropy only when all higher-order value is exhausted

> A functioning component is more valuable than its raw material.  
> A functioning assembly is more valuable than its components.  
> A functioning system is more valuable than its parts.

---

## Recursive Architecture

Industrial manufacturing is linear: `Input → Process → Output`

The Forge is recursive. Knowledge is treated with the same conservation laws as matter.

```
[ Intake ]
     │
[ Triage ] ◄────────────────────────┐
     │                              │
┌────┴────┐                         │
[Repair] [Repurpose]                 │  (Continuous Lessons Learned)
└────┬────┘                         │
     │                              │
[ Reduction ]                       │
     │                              │
[ Fabrication ]                     │
     │                              │
[ Utilization ] ────────────────────┘
```

Every failure, every unknown component, and every kilowatt-hour spent is logged to ensure the system forgets more slowly than it learns. The primary viability metric at every scale:

> **Value recovered per kWh consumed**

Full flow logic is defined in [`Architecture/Forge_flow.md`](Architecture/Forge_flow.md).

---

## Portability — This Repository Is For Everyone

This repository is not for a specific location. It is designed to be forked, initialized, and deployed by any community anywhere in the world.

The **Reference Deployment Context (RDC)** provides a climate baseline for files that contain environment-sensitive values. The [`Architecture/Facilities.md`](Architecture/Facilities.md) **Site Initialization Checklist** (Section VII) surfaces every climate and site parameter that needs to be substituted for your deployment context — temperature range, humidity, wind loading, floor type, regulatory environment, primary salvage stream.

The doctrine is generic. The parameters are yours to supply. A builder in Lagos, Manila, or Reykjavik can run through the checklist and calibrate the entire repository to their local conditions. Nothing in the technical architecture assumes a particular geography, infrastructure level, or supply chain.

---

## Long-term vision

The Forge has a deliberately ambitious trajectory — from a local salvage loop to self-replicating and eventually off-world systems.

Those later stages are aspirational thresholds, not current capabilities.

**Each stage must earn the next through evidence.**

| Version | Threshold | Character |
|---------|-----------|-----------|
| v0 | Proof of persistence — the loop closes | Terrestrial, bootstrap-friendly, manual oversight |
| v1 | Energy independence demonstrated | Self-improving workshop; learning loops close |
| v2 | Self-replication demonstrated | Forge_Net; distributed knowledge; cross-validation |
| v3 | Autonomous operation demonstrated | Leviathan; harsh environments; sparse resources |
| v4 | Off-world deployment | Seed systems; minimal bootstrap packages |
| v5 | Interstellar propagation | Non-conquest expansion of adaptive, ethical fabrication capability |

Skipping versions on either axis is explicitly discouraged. Each threshold must be earned.

Full roadmap and exit conditions in [`Admin/Trajectories.md`](Admin/Trajectories.md).

---

## The Pressures That Shaped This

The Forge's architecture is the fossil record of the pressures that shaped it. The **Challenges/** directory is the problem layer — it answers *why* these capabilities exist by anchoring the technical architecture to the real-world conditions it was built to address.

Challenges are permanent. Solutions are temporary local answers.

**External Challenges** — pressures that exist independent of the Forge:

- `Challenges/Water.md` — Water scarcity and contamination. Clean water as a human right, not an optional capability. Living Waters initiative: atmospheric moisture recovery, stratification-based remediation, material-positive filtration
- `Challenges/Biofouling.md` — Biological colonization and corrosion as threats to long-duration autonomous hardware. Ultrasonic disruption, biomimetic surfaces, sacrificial anodes. No toxic antifoulants
- `Challenges/Waste.md` — Discretionary waste and the erosion of local repair capacity. The Forge as the system that makes self-reliance the path of least resistance
- `Challenges/Planned_Obsolescence.md` — Sealed enclosures, potted components, locked firmware as deliberate unrepairability. Logic-Zero re-baselining, thermal delamination, standardized geometry upcycling
- `Challenges/Critical_Minerals.md` — Rare earth and critical mineral supply chain concentration as a structural threat to technological sovereignty. The technosphere as the primary mine. Aggressive urban mining, centrifugal separation, selective induction melting for neodymium, cobalt, lithium, tantalum recovery
- `Challenges/Energy_Scarcity.md` — Energy poverty, grid fragility, and fossil-fuel dependency as a structural condition the Forge responds to, not merely an operational input it consumes. Distinguished explicitly from `Operations/Energy.md`, which answers how the Forge powers itself — this file answers why energy access is a Forge purpose. Community energy sovereignty objective

**Reflexive Challenges** — pressures created by the Forge's own capability:

- `Challenges/Emergence.md` — The only Challenge whose pressure is created by the Forge itself. Capability growth produces new failure modes, new governance demands, and new ethical surface area. The system must remain corrigible under its own success.

**Integration Challenges** — what success looks like when both external and reflexive pressures have been answered:

- `Challenges/Return_To_Eden.md` — The integration target. Closed-loop material and knowledge systems that increase local agency rather than extract it.
- `Challenges/Closed_Loop_Feedstock.md` — Solution-track counterpart. Operational pathways toward feedstock independence.

---

## Repository Map

### Operations (the seven gates)

- `Operations/Gate_01_Intake.md` — Safety screening and material acceptance. Where every physical cycle starts.
- `Operations/Gate_02_Triage.md` — Decision hierarchy: preserve function → assemblies → components → materials → destroy.
- `Operations/Gate_03_Reduction.md` — Controlled destruction only after higher-value paths are exhausted. Point-of-no-return doctrine.
- `Operations/Gate_04_Separation_Mechanical.md` — Mechanical separation of mixed streams.
- `Operations/Gate_05_Separation_Thermal.md` — Thermal and chemical separation pathways.
- `Operations/Gate_06_Fabrication.md` — Turning recovered materials and components into new capability.
- `Operations/Gate_07_Utilization.md` — Deployment, measurement, and feedback into the learning loop.

Supporting operational doctrine:

- `Operations/Energy.md` — How the Forge powers itself
- `Operations/Electronics.md` — Salvage and recovery of electronic systems
- `Operations/Plastics.md` — Polymer recovery and processing
- `Operations/Air_Scrubber.md` — Air quality and filtration systems
- `Operations/Woodworking.md` — Full timber processing chain

### Architecture

- `Architecture/Forge_flow.md` — Master decision flow and repository-wide vocabulary standard
- `Architecture/Facilities.md` — Physical environment constraints and Site Initialization Checklist
- `Architecture/Components.md` — Critical vs. useful component taxonomy
- `Architecture/Engineering.md` — Physical-world doctrine, first principles, Conservation of Complexity
- `Architecture/Mechanical_Structures.md` — Structural and kinematic engineering for salvaged-component machinery
- `Architecture/Thermal_Systems.md` — Thermodynamic laws as operating constraints
- `Architecture/Friction_Dynamics.md` — Fluid mechanics, aerodynamics, and tribology
- `Architecture/Chemistry.md` — Corrosion, galvanic series, polymer degradation, battery chemistry
- `Architecture/Cognitive_Frameworks.md` — How Forge systems think safely under uncertainty
- `Architecture/Forge_Net.md` — Decentralized network connecting Forge instances
- `Architecture/Geck_forge_seed.md` — Minimum viable seed for new deployments

### Governance & Philosophy

Governance is not an add-on. It is the infrastructure that prevents the system from drifting into entropy or weaponization.

- `Admin/Governance_Charter.md` — Constitutional governance. Eight Tier 1 Axioms
- `Admin/Ethical_Constraints.md` — Permission framework and Anti-Weaponization Doctrine
- `Admin/Auditor_Protocols.md` — Verification, hallucination filter, Epistemic Foundation (EF-0.0–EF-0.8b)
- `Admin/Computational_Institutional_Reasoning.md` — Verification algebra, epistemic debt dynamics
- `Admin/Engineer_Protocols.md` — Cognitive and procedural protocols for engineering contributors
- `Admin/Trajectories.md` — Full roadmap and exit conditions
- `Unknowns.md` — Live registry of unresolved questions
- `Discovery.md` — Context core and discovery log

### Tests & Evidence

- `Tests/Field_Logs.md` — Primary location for experimental results and failures
- Additional experimental pathways in the `Tests/` directory covering solar, water, biological, pyrolysis, cognitive salvage, and more

---

## Governance Architecture

The repository is treated as a governed knowledge system. The architecture was designed for a specific problem: how do you build a system that remains trustworthy under scale, drift, recursion, and agent succession — without assuming the agents involved will always remain well-intentioned?

The answer is institutional rather than behavioral:

- **Bounded authority** — no agent may plan, execute, and self-authorize the same action
- **Adversarial review** — no agent's output is trusted without hostile independent review
- **Provenance requirements** — all claims must trace to verifiable external sources
- **Visible uncertainty** — unknowns must remain visible, not buried
- **Amendment procedures** — the system can be corrected through defined paths
- **Escalation paths** — instability surfaces rather than accumulates silently

The Forge itself is subject to the same corrigibility standard it imposes on the agents operating within it.

---

## Multi-Agent Development

This project is developed through a structured multi-agent workflow. Different AI systems contribute in defined roles:

- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions
- **Systems/Auditor** — cross-module integration review, dependency mapping, drift detection
- **Evidence/Auditor** — verification source integrity, confidence label enforcement
- **Ethical/Auditor** — harm detection, governance erosion detection
- **Engineer** — translates concepts into operational specifications
- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence

All AI contributions are governed by `Admin/Auditor_Protocols.md`. Contributions pass through six verification gates before promotion from exploration to specification. Refusal of a bad premise is a first-class output.

---

## Leviathan

The Forge's assumptions are stress-tested in the **Leviathan framework** — a deep-ocean autonomous test environment designed to break what the system thinks it knows before any off-world deployment is attempted.

Leviathan is not a product. It is a filter.

Failure is expected. Adaptation is required. Learning is mandatory.

---

## The founding idea, taken seriously

Three developments that are not drift, but the founding idea applied more rigorously:

1. **The problem layer is now explicit.** Challenges/ files name the pressures the architecture answers.
2. **The same reduce-and-reintegrate logic applies beyond materials.** Water, biological byproducts, flood sediment, and discarded machinery wisdom are all treated as salvage streams.
3. **The system salvages its own claims to certainty the same way it salvages materials.** Nothing gets discarded without accounting — not scrap, not a failed hypothesis, not a resolved unknown that later turns out to have been closed too early. The Unknown Budget rule in `Unknowns.md` is the clearest expression of this.

None of this is drift away from the founding idea. It is the founding idea taken more seriously than a workshop floor alone could demand.

---

* **Context Core:** [Discovery.md](Discovery.md)  
* **Network Routing:** [Routing.md](Routing.md)
