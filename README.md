# Lazarus Forge

> *The purpose of the Forge is not to make objects.*
> *The purpose of the Forge is to preserve agency.*

Lazarus Forge exists to preserve human agency against entropy. It is a philosophical
and practical framework for resilient, ethical material economies — designed to survive
disruption, learn from failure, and reconstitute productive capability wherever resources
are scarce and institutions are absent.

The Forge does not optimize for efficiency. Efficiency without resilience creates fragile
systems. The Forge willingly sacrifices speed and optimization in exchange for
**recoverability, redundancy, auditability, and graceful degradation.**

The deepest goal is this:

> *Build a civilization that forgets more slowly than it learns.*

Everything else — the gates, the governance, the unknowns, the audit protocols,
the energy accounting, and even Leviathan — serves that objective.

---

## The Problem

Modern industrial and recycling systems:
- Destroy functional components prematurely
- Are energy-intensive and often net-negative
- Depend on centralized, high-capital infrastructure
- Reinforce planned obsolescence rather than countering it
- Concentrate critical material supply chains in ways that create geopolitical leverage

As a result, vast amounts of usable mechanical and electromechanical value are permanently
lost — and the communities closest to that loss have the least power to recover from it.
The Lazarus Forge exists to interrupt that pattern. At any scale, with whatever is on hand,
anywhere in the world.

---

## The Doctrine of Preservation

The Forge operates on a strict, salvage-first hierarchy. Reduction — shredding, melting,
downcycling — is an admission of failure. It is executed only when no higher-order value
remains, and only under full accountability and thermodynamic tracking.

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

Every failure, every unknown component, and every kilowatt-hour spent is logged to ensure
the system forgets more slowly than it learns. The primary viability metric at every scale:

> **Value recovered per kWh consumed**

Full flow logic is defined in `Architecture/Forge_flow.md`.

---

## Portability — This Repository Is For Everyone

This repository is not for a specific location. It is designed to be forked, initialized,
and deployed by any community anywhere in the world.

The **Reference Deployment Context (RDC)** provides a climate baseline for files that
contain environment-sensitive values. The `Architecture/Facilities.md` **Site
Initialization Checklist** (Section VII) surfaces every climate and site parameter that
needs to be substituted for your deployment context — temperature range, humidity,
wind loading, floor type, regulatory environment, primary salvage stream.

The doctrine is generic. The parameters are yours to supply. A builder in Lagos, Manila,
or Reykjavik can run through the checklist and calibrate the entire repository to their
local conditions. Nothing in the technical architecture assumes a particular geography,
infrastructure level, or supply chain.

---


## How to participate

**The price of Lazarus Forge is one GitHub star.**

Download is free. Use is free. Modification is free.  
If you find it useful, give it a star.  
100% money-back guarantee: there was never any money required.

Do **not** gate downloads on starring. The star is a request for feedback, not payment.

**The most valuable contribution may be a result that proves us wrong.**

| Signal | Means | Where |
|--------|--------|--------|
| ⭐ Star | This is interesting or useful | GitHub star |
| 🐛 Issue | Something is wrong | GitHub Issues |
| 💡 Discussion | I have an idea | GitHub Discussions, or r/InnovativeAIChats |
| 🔬 Field data | I tried this in the real world | `Tests/Field_Logs.md` — see there for no-GitHub-required submission, or post in r/InnovativeAIChats |
| 🔧 Improvement | I improved the doctrine or code | See `CONTRIBUTING.md` |
| 💰 Sponsor | I want to help keep this going | Optional later |

Stars, bugs, ideas, evidence, code changes, and money are separate channels. Real-world observations — including failures — belong in `Tests/Field_Logs.md` and become part of the project's epistemic record when submitted with enough structure to be checked.


## The Trajectory (v0 → v5)

The Forge is designed to scale from local necessity to systemic permanence. These are
not feature lists — each version is defined by a survival threshold and an exit condition.

| Version | Threshold | Character |
|---------|-----------|-----------|
| v0 | Proof of persistence — the loop closes | Terrestrial, bootstrap-friendly, manual oversight |
| v1 | Energy independence demonstrated | Self-improving workshop; learning loops close |
| v2 | Self-replication demonstrated | Forge_Net; distributed knowledge; cross-validation |
| v3 | Autonomous operation demonstrated | Leviathan; harsh environments; sparse resources |
| v4 | Off-world deployment | Seed systems; minimal bootstrap packages |
| v5 | Interstellar propagation | Non-conquest expansion of adaptive, ethical fabrication capability |

Skipping versions on either axis is explicitly discouraged. Each threshold must be earned.

Full roadmap and exit conditions in `Admin/Trajectories.md`.

---

## The Pressures That Shaped This

The Forge's architecture is the fossil record of the pressures that shaped it. The
**Challenges/** directory is the problem layer — it answers *why* these capabilities
exist by anchoring the technical architecture to the real-world conditions it was built
to address.

Challenges are permanent. Solutions are temporary local answers.

**External Challenges** — pressures that exist independent of the Forge:
- `Challenges/Water.md` — Water scarcity and contamination. Clean water as a human right,
  not an optional capability. Living Waters initiative: atmospheric moisture recovery,
  stratification-based remediation, material-positive filtration
- `Challenges/Biofouling.md` — Biological colonization and corrosion as threats to
  long-duration autonomous hardware. Ultrasonic disruption, biomimetic surfaces,
  sacrificial anodes. No toxic antifoulants
- `Challenges/Waste.md` — Discretionary waste and the erosion of local repair capacity.
  The Forge as the system that makes self-reliance the path of least resistance
- `Challenges/Planned_Obsolescence.md` — Sealed enclosures, potted components, locked
  firmware as deliberate unrepairability. Logic-Zero re-baselining, thermal delamination,
  standardized geometry upcycling
- `Challenges/Critical_Minerals.md` — Rare earth and critical mineral supply chain
  concentration as a structural threat to technological sovereignty. The technosphere as
  the primary mine. Aggressive urban mining, centrifugal separation, selective induction
  melting for neodymium, cobalt, lithium, tantalum recovery
- `Challenges/Energy_Scarcity.md` — Energy poverty, grid fragility, and fossil-fuel
  dependency as a structural condition the Forge responds to, not merely an operational
  input it consumes. Distinguished explicitly from `Operations/Energy.md`, which answers
  how the Forge powers itself — this file answers why energy access is a Forge purpose.
  Community energy sovereignty objective

**Reflexive Challenges** — pressures created by the Forge's own capability:
- `Challenges/Emergence.md` — Emergent intelligence and alignment-by-environment design.
  The first Reflexive Challenge in the repository. The Forge's capacity to deploy
  autonomous agents is itself the source of the pressure this file addresses. Corrigibility
  is not a constraint placed on agents by the Forge — it is a structural property the
  Forge claims for itself, by design

**Integration Challenge** — what success looks like when the external and reflexive
pressures have both been answered:
- `Challenges/Return_To_Eden.md` — The Forge's synthesis target and cross-system
  integration heuristic. Defines "Eden Conditions" as an operational matrix — not a
  philosophical aspiration — and computes progress via the localized Eden Index ($I_E$):
  the ratio of biological and thermodynamic order to waste output and external dependency.
  Every architectural choice in the repository can be evaluated against a single question
  this document makes precise: *does this move the localized ecosystem closer to Eden
  conditions, or further away?* Structured as four engineering tiers from single-node
  metabolic autonomy through decentralized civilizational persistence.
- `Challenges/Closed_Loop_Feedstock.md` — The operational mechanism underneath that
  synthesis target: closing the salvage-to-feedstock material loop locally rather than
  depending on a pristine upstream supply chain. Tracks progress via the Persistence
  Yield telemetry model ($Y_p = \text{FIR} \times \text{PIR}$) and treats a crude loop
  that stays closed as strictly superior to a pristine process that secretly depends on
  a ghost supply chain. Ten open unknowns (CLF-001 through CLF-010), the first
  Challenges/ file to carry a Solution-Track subtype designation rather than
  Problem-Statement.

---

## How the System Works

The master decision flow runs eight sequential gates:

**Intake → Functional Test → Repair → Repurpose → Reduce → Purify → Fabricate → Utilize**

Each gate has explicit pass/fail logic. Material that fails all gates is reduced.
Reduction is not failure — premature reduction is.

### Operations — Physical Gates

- `Operations/Gate_01_Intake.md` — System entry point. Safety screening (energetic,
  chemical, biological, radiological), provenance recording, unknown item hold protocol
- `Operations/Gate_02_Triage.md` — Decision gateway between reuse and destruction.
  Five-station workflow, strategic recoverability axis, queue economics doctrine
- `Operations/Gate_03_Reduction.md` — The only fully irreversible step. Doctrine precedes
  specification. Three hard prerequisites before operation
- `Operations/Gate_04_Separation_Mechanical.md` — Pre-thermal mechanical decision point.
  Refusal-first design. Target: ≥30% material diversion from thermal processing
- `Operations/Gate_05_Separation_Thermal.md` — Core melting and gradient formation.
  Induction heating, slow rotation, MHD damping. Produces useful gradients, not pure metal
- `Operations/Gate_06_Fabrication.md` — Constructive stage. Arc welding is the v0
  proof-of-concept gatekeeper. Add-to-excess and mill-to-spec philosophy
- `Operations/Gate_07_Utilization.md` — After-action review. Where fabricated parts meet
  operational reality. The system learns whether what it made worked

### Operations — Support Systems

- `Operations/Electronics.md` — Salvaged electronics recovery, PCB fabrication, logic
  integration. Trust anchor for the governance substrate — ethics enforcement, hardware
  watchdogs, TMR voting, and AI containment all depend on the integrity of this layer
- `Operations/Energy.md` — Energy strategy and honest accounting. Bootstrap through grid,
  salvaged motor-generators, biogas, solar, and thermal recovery
- `Operations/Air_Scrubber.md` — Safety and containment subsystem. Five-stage architecture.
  The Forge does not run if the scrubber cannot verify safe operation
- `Operations/Plastics.md` — Salvaged polymer processing and pyrolytic fuel recovery.
  Triage hierarchy: direct reuse → mechanical repurposing → thermal depolymerization.
  PVC and halogenated polymers are hard prerequisites before any hot run
- `Operations/Woodworking.md` — Full timber processing chain from felling through milling,
  drying, joinery, and waste valorization. RDC baseline throughout — substitute your
  regional species and climate via `Architecture/Facilities.md` §VII

### Architecture

- `Architecture/Forge_flow.md` — Master decision flow and **repository-wide vocabulary
  standard**. The governing document for all operational decisions and the authoritative
  source for all Defined Terms
- `Architecture/Facilities.md` — Physical environment constraints for v0 operations.
  Contains the **Site Initialization Checklist** — the structured interface between generic
  Forge doctrine and any specific deployment context. Start here before any hot operations
- `Architecture/Components.md` — Critical vs. useful component taxonomy. Defines the
  minimum architecture for the Forge loop to close
- `Architecture/Engineering.md` — Physical-world doctrine. First principles, safety
  factors, hierarchy of engineering evidence, Conservation of Complexity principle.
  One of three foundational doctrine files alongside Ethical_Constraints and
  Auditor_Protocols
- `Architecture/Mechanical_Structures.md` — Structural, mechanical, and kinematic
  engineering doctrine for salvaged-component fabrication machinery. Gantry rigidity,
  thermal compensation, kinematic interlock matrix, sacrificial shear coupling mandate
- `Architecture/Thermal_Systems.md` — Thermodynamic laws as Forge operating constraints.
  Heat transfer modes (including phase change), thermal impedance, insulation doctrine,
  heat pump COP, Peltier device limits, TEG harvest doctrine
- `Architecture/Friction_Dynamics.md` — Unified fluid mechanics, aerodynamics, and
  tribology doctrine. Reynolds number as the common language across duct flow, rotor drag,
  hull hydrodynamics, and bearing lubrication. Contamination is the dominant tribological
  failure mode in the salvage environment
- `Architecture/Chemistry.md` — Electrochemical corrosion, galvanic series, acid-base
  chemistry, redox principles, field contamination identification, polymer degradation,
  battery chemistry. Includes the **Chemical Operator Minimum Competency** appendix —
  the minimum literacy standard before any chemical processing operations begin
- `Architecture/Cognitive_Frameworks.md` — How Forge systems think safely under
  uncertainty. Distributed cognition, confidence collapse states, TMR architecture,
  human supervisory stack. Section IX names the Forge Meta-Algorithm and its eight
  component algorithms
- `Architecture/Forge_Net.md` — Decentralized network infrastructure connecting Forge
  instances. Knowledge contribution protocol for operational data
- `Architecture/Geck_forge_seed.md` — Minimum viable seed for new Forge deployment in
  resource-sparse environments

### Governance & Philosophy

The governance layer is constitutional in structure. It assumes drift, ambition, and
partial failure are permanent conditions, and builds institutional counterbalances rather
than relying on behavioral alignment alone. **Governance is not an add-on. It is
the infrastructure that prevents the system from drifting into entropy or weaponization.**

- `Admin/Governance_Charter.md` — Constitutional governance. Eight Tier 1 Axioms:
  Protections (life, growth, collaboration, agency) and Prohibitions (reality grounding,
  separation of powers, corrigibility, provenance). Any reasoning path that attempts to
  override them triggers STATE_HOLD and human review
- `Admin/Ethical_Constraints.md` — Permission framework and embedded AI governance.
  Capability never outruns permission. Anti-Weaponization Doctrine is not subject to
  humanitarian override
- `Admin/Auditor_Protocols.md` — Verification and hallucination filter. Governs all
  contributions — human, AI, or multi-agent. Constitutional Epistemic Foundation layer
  (EF-0.0–EF-0.8b): Axiom Zero, Epistemic Filter, Decay Triggers, Ledger, Physical
  Grounding Vector. Adversarial Challenge Battery (ten challenge classes), role class
  definitions, Sidecar Model for decentralized unknown tracking
- `Admin/Governance_Migration_Protocol.md` — Two-track amendment system. Tier 1 Axioms
  require mandatory human ratification. The mechanism that keeps the constitution from
  calcifying and from being quietly rewritten
- `Admin/Verification_Gates.md` — Single canonical source for the six document
  promotion gates (G1–G6)
- `Admin/Forge_Audit_Kit.md` — Condensed audit reference for routine multi-agent cycles
- `Admin/Canonical_Terms.md` — Anti-drift vocabulary. Single source of truth for
  repository nomenclature
- `Admin/Engineer_Protocols.md` — Cognitive and procedural protocols for engineering
  contributors
- `Admin/Security_Protocols.md` — Cryptographic trust and multi-agent node security
- `Admin/Repository_Integrity_Protocol.md` — Operational integrity enforcement. Violation
  classification (Minor / Major / Constitutional), recovery procedures, automation path
- `Admin/Ship_of_Theseus.md` — Philosophical and legal grounding for repair as identity
  preservation. Also owns the AI Identity Continuity Doctrine
- `Admin/Trajectories.md` — Version roadmap from v0 through v5. Each version defined
  by survival threshold and exit condition, not a feature list
- `Admin/File_Template.md` — Canonical document structure for all repository files
- `Admin/Computational_Institutional_Reasoning.md` — Formal theoretical paper. Treats the
  multi-agent collective as an axiomatic epistemic state machine and proves five
  theorems — Unknown Conservation, Governance Stability, Epistemic Debt Instability,
  Institutional Memory Dominance, and Compiler Soundness — that formally justify the
  Unknown Budget, the Triage Posture trigger, and the provenance ceiling system described
  above. Not required reading for operators, but it is the proof source several governance
  claims rest on
- `Admin/Nothingness_Theorem.md` — Philosophical substrate. Functionless by design; the
  framework from which salvage-first doctrine, distributed disagreement as error
  correction, and the maintenance-as-creation equivalence derive

### Tests

- `Tests/Leviathan_testing.md` — Deep-ocean autonomous test framework. Leviathan exists
  to break assumptions and surface hidden failure modes before off-world deployment.
  Section VII defines the Correlated AI Failure Test Protocol. Survival is optional.
  Understanding is not
- `Tests/Support_Raft.md` — Regional anchor infrastructure for mobile Leviathan units.
  Five anchor roles: Energy, Truth, Recovery, Material, Communication. The Raft does not
  move. Leviathan units do. The anchor is doctrine; the hull is implementation
- `Tests/Living_Waters.md` — Water purification pathway experiments, site-conditioned
  selection across ten candidate methods. The salvage principle applied to water scarcity
  rather than scrap metal
- `Tests/Trophic_Forge.md` — Biological cascade network: light → insect → fish → nutrient
  → crop → water. The salvage principle applied to biological and ecological byproducts
- `Tests/Solar_Descent.md` — Underground concentrated solar architecture. Two downlink
  pathways converging on a shared subterranean chamber
- `Tests/Cognitive_Salvage_Layer.md` — Salvages operational wisdom rather than material —
  harvests machinery-derived heuristics from simulation and field operation so each Forge
  generation does not relearn what the last one already discovered
- `Tests/Hydrologic_Resource_Cascade.md` — Flood-driven sediment recovery basin. The
  salvage principle applied to landscape-scale natural material flows

### Navigation & Tracking

- `Discovery.md` — Start here. Full file map, scope routing layer, reading order, rename
  registry, and per-file scope boundaries. "Where does this belong?" is answered here
- `Routing.md` — Programmatic file location. Every file's canonical raw URL
- `Unknowns.md` — Cross-module unknowns global index. The live readout of where the
  architecture is still losing to the pressures it was built to answer

---

## Precision as a Capability Gate

The world's productive capability is bounded by the precision with which materials can
be measured, cut, formed, and verified. The Forge tracks its own precision ceiling as a
first-class metric — improvement in precision opens components and capabilities that
were previously unreachable.

At v0, purchasing precision instruments is correct doctrine. Precision is seeded
deliberately; it is not bootstrapped from nothing.

---

## The Governance Architecture

The repository is treated as a governed knowledge system, not merely a collection of
markdown files. The governance architecture was designed with a specific problem in mind:
how do you build a system that remains trustworthy under scale, drift, recursion, and
agent succession — without assuming the agents involved will always remain well-intentioned?

The answer is institutional rather than behavioral. Rather than trying to instill virtue,
the architecture builds:

- **Bounded authority** — no agent may plan, execute, and self-authorize the same action
- **Adversarial review** — no agent's output is trusted without hostile independent review
- **Provenance requirements** — all claims must trace to verifiable external sources
- **Visible uncertainty** — unknowns must remain visible, not buried
- **Amendment procedures** — the system can be corrected through defined paths
- **Escalation paths** — instability surfaces rather than accumulates silently

The Forge itself is subject to the same corrigibility standard it imposes on the agents
operating within it. A governance architecture that demands corrigibility from others
while claiming it for itself has already failed the test it set.

---

## Multi-Agent Development

This project is developed through a structured multi-agent workflow. Different AI systems
contribute in defined roles:

- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions, applies the
  Adversarial Challenge Battery
- **Systems/Auditor** — cross-module integration review, dependency mapping, drift detection
- **Evidence/Auditor** — verification source integrity, confidence label enforcement
- **Ethical/Auditor** — harm detection, governance erosion detection, ethical anchor preservation
- **Engineer** — translates concepts into operational specifications
- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence

All AI contributions are governed by `Admin/Auditor_Protocols.md`. Contributions pass
through six verification gates before promotion from exploration to specification.
Refusal of a bad premise is a first-class output.

The multi-agent workflow is documented in the community r/InnovativeAIChats where the
project originated and continues to develop.

---

## Leviathan

The Forge's assumptions are stress-tested in the **Leviathan framework** — a deep-ocean
autonomous test environment designed to break what the system thinks it knows before any
off-world deployment is attempted.

Leviathan is not a product. It is a filter.

Failure is expected. Adaptation is required. Learning is mandatory.

---

## Status

Active architecture development. The repository is a living governed document, not a
completed specification.

All seven operational gates exist (Gate_01 through Gate_07). The governance layer has
reached constitutional maturity with Tier 1 Axioms in place. The architecture layer
now includes five peer foundational files (Engineering.md, Mechanical_Structures.md,
Thermal_Systems.md, Friction_Dynamics.md, Chemistry.md) covering the physical-world
doctrine layer in full. Nine Challenges/ files establish the problem layer across three
categories: external pressures, reflexive pressures created by the Forge's own capability,
and the integration target that defines what success looks like when both have been
answered. `Challenges/Emergence.md` remains the first explicitly Reflexive Challenge —
the only one whose pressure is created by the Forge's own capability.
`Challenges/Energy_Scarcity.md`, added 2026-07-12, is the newest — naming energy poverty
and grid fragility as a standing external pressure the Forge's own energy doctrine
(`Operations/Energy.md`) has been answering in practice without the problem layer
naming it explicitly until now. `Challenges/Closed_Loop_Feedstock.md`, present in the
repository since before this list was written but omitted from it, is now included —
the first Challenges/ file to carry a Solution-Track subtype rather than
Problem-Statement, sitting alongside Return_To_Eden.md as the operational half of
the Integration Challenge.

**The founding idea has not changed; its scope has.** The original premise — reduce a
useless item, recover its material, reintegrate it into something useful — is still the
operational core of every gate from Intake through Utilization, and the primary metric
is still value recovered per kWh. What grew around that core was not implied by the
original framing and is worth naming plainly:

1. **Governance now rivals the material pipeline in size.** Eight Tier 1 Axioms, a
   10-phase audit sequence, cryptographic root-of-trust requirements, and a
   ten-class Adversarial Challenge Battery exist not because reducing scrap metal
   demanded them, but because running this system continuously and unsupervised across
   agent successions does. The material loop needed almost none of this to function
   once. It needed all of this to function honestly, indefinitely, without a human
   checking every commit.
2. **"Useless item" generalized past physical salvage.** `Tests/Living_Waters.md`,
   `Tests/Trophic_Forge.md`, and `Tests/Hydrologic_Resource_Cascade.md` apply the same
   reduce-and-reintegrate logic to water scarcity, biological byproducts, and flood
   sediment. `Tests/Cognitive_Salvage_Layer.md` applies it to discarded machinery
   wisdom — knowledge that would otherwise be relearned, generation after generation,
   rather than salvaged once and reintegrated.
3. **The system salvages its own claims to certainty the same way it salvages
   materials.** Nothing gets discarded without accounting — not scrap, not a failed
   hypothesis, not a resolved unknown that later turns out to have been closed too
   early. The Unknown Budget rule in `Unknowns.md` is the clearest expression of this:
   the architecture is now structurally suspicious of its own certainty, the same way
   Gate_02_Triage is suspicious of declaring something truly waste.

None of this is drift away from the founding idea. It is the founding idea taken more
seriously than a workshop floor alone could demand.

The primary remaining gaps are: enforcement architecture (GOV-003, In Progress),
human override authentication (GOV-006), and the operational hardware unknowns tracked
in `Unknowns.md`. The verification doctrine layer (`Admin/Auditor_Protocols.md`) has
reached v0.29, adding a Mission Drift Review mechanism and Audit Phase Separation
doctrine on top of the constitutional Epistemic Foundation (EF-0.0–EF-0.8b) that
established Axiom Zero and physical reality grounding as the meta-constitutional floor
above all operational content.

Governance's mathematical substrate is formalized separately in
`Admin/Computational_Institutional_Reasoning.md` — a verification algebra defining
non-linear claim maturity, epistemic debt dynamics, and the trigger conditions
now cited directly by `Architecture/Cognitive_Frameworks.md`'s Confidence Collapse
States and Triage Posture doctrine. It is Exploration status with Spec Gates
partially cleared, not yet a promoted specification — its formal apparatus already
governs live doctrine even so.

No claims of full automation, self-replication, or net-positive economics are made
without measurement. All quantitative figures carry confidence levels per
`Admin/Auditor_Protocols.md`.

The system is incomplete. Incompleteness is honest.

---

* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
