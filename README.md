# Lazarus Forge

> *The purpose of the Forge is not to make objects.*  
> *The purpose of the Forge is to preserve agency.*

LazarusForge is a scrappy open-source experiment in building useful, resilient systems from imperfect parts—without assuming the software is telling the truth.

It is part workshop, part experiment, part notebook.

We work with ordinary hardware, open tools, careful records, AI agents that are allowed to be wrong, and a deliberate refusal to hand-wave. The project assumes that software can be wrong, measurements can be misleading, agents can hallucinate, documentation can drift, and our own assumptions can fail. So instead of hiding those failures, we try to expose them, measure them, preserve the evidence, and improve one small step at a time.

AI is one of the things we are experimenting with. It is not the reason the project exists.

The deepest goal remains:

> *Build a civilization that forgets more slowly than it learns.*

---

## What this actually looks like

- Old or scavenged hardware when we have it.
- Markdown files and small Python scripts.
- Experiments that are allowed to fail.
- Explicit Unknowns that are not allowed to be buried.
- Agents that must declare roles and can be caught being wrong.
- Physical or mechanical checks preferred over software confidence.
- Everything logged, including the mistakes.

If the machine says one thing and the wire says another, believe the wire.

Three AI sessions on one computer are not three independent witnesses. We are still learning where that distinction actually matters.

---

## What LazarusForge is not

- A commercial AI product
- A claim that AI agents are trustworthy
- A finished autonomous system
- A promise of AGI
- A polished framework waiting for users
- A collection of benchmarks designed to make the project look good

It is an ongoing experiment.

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
A failed experiment is useful. A measurement that contradicts the doctrine is especially useful. Log results per [`Tests/Field_Logs.md`](Tests/Field_Logs.md)'s submission format (one file per entry under `Tests/Field_Logs/`, as of 2026-10-03).

**Challenge the assumptions.**  
Find something that shouldn't work. Find a governance failure. Find a hidden assumption. Open an issue.

You don't need a server farm. You don't need to understand the entire Forge.  
Read something. Find something wrong. Try to break an assumption.  
If you find the experiment interesting, one star is plenty.  
If you want to go further, bring a machine, a test, an uncomfortable question, or a better idea.

---

## Your first Forge experiment

You don't need a facility to participate.

1. Find one discarded object.
2. Identify the highest-value function, component, or material it contains.
3. Record what you think can be recovered and what you actually recover.
4. Log the result (success or failure) per [`Tests/Field_Logs.md`](Tests/Field_Logs.md).

That single cycle is already a real contribution.

---

## Things we got wrong

We keep a short public record of real mistakes and corrections so the project does not accidentally learn the wrong lesson from them. See [`Things_We_Got_Wrong.md`](Things_We_Got_Wrong.md).

---

## Current state (honest orientation)

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

This table is a manual, human-facing orientation — a fast answer to "what's actually real." It is distinct from `Automation/integrity_check.py --health`, which mechanically checks repository consistency (metadata, cross-references, active unknowns) and does not attempt to judge physical readiness; neither replaces the other.

**Important:** much of the system remains experimental. An architectural specification is not evidence that the corresponding physical capability has been demonstrated. This distinction — specified versus demonstrated — is load-bearing throughout the repository, not just in this section.

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
| 🔬 Field data | I tried this in the real world | `Tests/Field_Logs.md` — see there for the submission format and no-GitHub-required path, or post in r/InnovativeAIChats |
| 🔧 Improvement | I improved the doctrine or code | See [`CONTRIBUTING.md`](CONTRIBUTING.md) |

Stars, bugs, ideas, evidence, and code changes are separate channels. Real-world observations — including failures — belong under `Tests/Field_Logs/` (format and submission instructions in `Tests/Field_Logs.md`) and become part of the project's epistemic record when submitted with enough structure to be checked.

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
[ Fabrication ]                     │
     │                              │
[ Utilization ] ────────────────────┘
```

Every cycle feeds knowledge back into the next cycle. Failed experiments are not discarded; they become part of the permanent record.

---

## Seven Gates

Physical material moves through a controlled sequence of decision points. Each gate is a deliberate refusal to destroy value prematurely.

1. **Intake** — Safety screening and material acceptance
2. **Triage** — Preserve function → assemblies → components → materials → destroy
3. **Reduction** — Controlled destruction only after higher-value paths are exhausted
4. **Separation (Mechanical)** — Mechanical separation of mixed streams
5. **Separation (Thermal)** — Thermal and chemical separation pathways
6. **Fabrication** — Turning recovered materials and components into new capability
7. **Utilization** — Deployment, measurement, and feedback into the learning loop

Full operational doctrine lives in `Operations/`.

---

## Epistemic Governance

The Forge treats claims the same way it treats materials: nothing is discarded without accounting, and certainty is not assumed.

Core practices include:

- Explicit open Unknowns with a floor (the Unknown Budget)
- Evidence classification (Measured / Replicated / Simulated / Analogous / Placeholder)
- Verification gates before claims move from exploration to specification
- Agents that must declare roles and can be refused
- Preference for mechanical or physical checks over software confidence
- Append-only treatment of prior mistakes so the system does not quietly rewrite its own history

The same corrigibility standard the Forge imposes on agents is applied to the Forge itself.

See `Admin/` for the full governance and audit framework.

---

## Multi-Agent Development

This project is developed through a structured multi-agent workflow. Different AI systems contribute in defined roles (Skeptic, Auditor, Engineer, Synthesizer, and others). All AI contributions are governed by `Admin/Auditor_Protocols.md`. Refusal of a bad premise is a first-class output. Contributions pass through verification gates before promotion.

AI is a tool inside the experiment, not the experiment's purpose.

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
