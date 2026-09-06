# Architecture/Local_Governance_Framework.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
---

> *A node that can only govern itself has not yet met the communities it claims to serve.*
> *A community that cannot refuse has not yet been offered sovereignty.*

---

## File State

| Field | Value |
|---|---|
| **Status** | Exploration |
| **Architecture Subtype** | Institutional Interface |
| **Version** | v0.1-draft |
| **Last Updated** | 2026-09-06 |
| **Owner** | Architecture/ |
| **Verification Ref** | `Admin/Verification_Gates.md` |
| **Ethical Anchor** | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| **Spec Gates** | 0/6 |
| **Body Stability** | Volatile — first draft; no physical or institutional testing |
| **Open Unknowns** | See §Open Unknowns (LGF-001–LGF-007) |
| **Highest Risk** | Defining interface constraints on paper without enforceable standing or exit rights for the host community |

---

## Scope Boundary

**This file owns:**
- The minimum institutional interface between a Forge deployment (node) and its host community
- The design constraints that keep that interface from silently converting technical capability into unilateral authority or structural dependence
- The requirement that internal closure and resilience margins precede any externalization claim
- The rule that surplus disposition is a locally ratifiable and revisable decision; no disposition model is presumed by this framework
- Cross-references to the community-facing open unknowns already registered in Challenges/ (WS-004, WA-003, PO-004, ES-001, ES-002, and related)

**This file does not own:**
- Tier 1 Axioms, Human Override Doctrine, constitutional amendment rules, or repository governance → `Admin/Governance_Charter.md`
- Anti-Weaponization, Life Preservation, toxic-material hard floors → `Admin/Ethical_Constraints.md`
- Node-internal technical governance, watchdogs, multi-agent consensus → `Architecture/Cognitive_Frameworks.md`, `Admin/Auditor_Protocols.md`, `Admin/Verification_Gates.md`
- Specific surplus-routing mechanisms, economic models, or the detailed taxonomy of disposition ideologies → left to local decision and to domain files (`Challenges/Energy_Scarcity.md`, `Admin/Economics.md`, etc.)
- Concrete local institutional forms (councils, cooperatives, voting systems, informal-sector organizational structures) — those remain context-specific and downstream of this interface

**Layer relationship:**

```
Admin/Governance_Charter.md          (constitutional / repository authority & hard boundaries)
          │
          ▼
Architecture/Local_Governance_Framework.md   (institutional interface constraints)
          │
          ├── Challenges/Water.md
          ├── Challenges/Waste.md
          ├── Challenges/Planned_Obsolescence.md
          ├── Challenges/Energy_Scarcity.md
          └── other community-facing Challenges
                  │
                  ▼
          local deployment design
                  │
                  ▼
             Operations/
```

This framework does not create a new governance tier or parallel constitutional surface. It defines where the Forge does **not** possess unilateral authority over the host community.

---

## File Purpose

Multiple Challenges files assert community sovereignty, local capacity, informal-sector integration, and the need to consider externalizing surplus. None define the institutional interface that would make those claims operational without the repository choosing the community’s institutions for it.

This file supplies that missing middle layer:

1. A Forge node and its host community are distinct subjects.
2. Certain classes of decision that affect the community require local standing and cannot be decided unilaterally by the node or by repository-level authority.
3. Surplus disposition is a locally ratifiable and revisable decision; this framework presumes no particular disposition model.
4. Measured internal closure and resilience margins are prerequisites to any externalization claim.

Without this interface, “community sovereignty” remains moral language without institutional referent, and technical capability can silently become unilateral authority.

---

## Core Design Constraints

### LGF-P1 — Distinct Subjects
A Forge node and the host community are distinct subjects. The node does not absorb the community; the community does not absorb the node. Decision rights, information rights, and exit rights must be defined between them.

### LGF-P2 — Standing Before Benefit
No community-facing claim (surplus contribution, skill transfer, maintenance support, recovery services) may be treated as active doctrine until the host community has defined standing — the recognized capacity to accept, refuse, condition, or later withdraw from the arrangement.

### LGF-P3 — Internal Closure First
Measured internal power, material, and maintenance closure (including resilience margins and storage/buffer depth) is a prerequisite to any claim of surplus available for externalization. A generation or recovery figure is not a surplus figure until conversion losses, storage losses, maintenance energy, parasitic loads, and deferred-maintenance buffers have been subtracted and the residual remains positive under realistic duty cycles.

### LGF-P4 — Local, Revisable Disposition
Surplus disposition is a locally ratifiable and revisable decision. No disposition model is presumed by this framework. The Forge must not silently convert “surplus exists” into “the Forge is obligated to give it away.” Permanent one-way dependence is a failure mode, not a success condition.

### LGF-P5 — Reversibility and Non-Dependency
Arrangements that externalize capacity, knowledge, or material must be designed so that the host community can exit or reduce reliance without catastrophic loss of essential services. Creating structural dependence on the continued operation or goodwill of the node violates the sovereignty claims already present in the Challenges set.

### LGF-P6 — Pre-existing Institutions First
Where informal or formal local institutions already perform recovery, repair, energy, water, or waste functions, the default posture is interface and support rather than replacement. Displacement of existing capable actors requires explicit local justification and is presumptively disfavored.

### LGF-P7 — Subordination to Hard Floors
Nothing in this framework authorizes violation of Tier 1 Axioms, Anti-Weaponization, Life Preservation, toxic-material active-release prohibitions, or other hard floors in `Admin/Ethical_Constraints.md` and `Admin/Governance_Charter.md`. Local decision rights operate inside those boundaries, not around them.

---

## Decision-Rights Skeleton (Minimum Viable Interface)

The following classes of decision require host-community standing. Exact institutional form is left local and downstream.

| Decision Class | Node May Propose | Community Standing Required | Notes |
|---|---|---|---|
| Declaration that genuine surplus exists | Yes (with measured data) | Yes — acceptance of the claim | Prerequisite: LGF-P3 |
| Whether, how, and on what terms to externalize any surplus | Yes | Yes — including refusal | No model presumed (LGF-P4) |
| Terms, duration, and exit conditions of any externalization | Yes | Yes | Must be reversible (LGF-P5) |
| Community-facing maintenance or skill-transfer protocols | Yes | Yes | Links to WS-004, PO-004, WA-003 |
| Interface rules with pre-existing informal/formal local actors | Yes | Yes | Default: support, not displace (LGF-P6) |
| Acceptance of node-provided services that create ongoing dependence | Yes | Yes — with explicit exit path | |
| Changes to the above once in operation | Yes | Yes | |

Node-internal technical decisions (gate sequencing, safety interlocks, assay methods, etc.) remain outside this table unless they directly impose lasting community-facing obligations.

---

## Relationship to Existing Open Unknowns

This framework does not close the following; it supplies the institutional interface they have been missing:

- WS-004 — Community adoption and maintenance protocol (Water)
- WA-003 — Informal-sector integration doctrine (Waste)
- PO-004 — Community re-baselining skill-transfer standard (Planned Obsolescence)
- ES-001 — Community-facing energy surplus routing mechanism (Energy Scarcity)
- ES-002 — Economic legibility threshold for community-facing systems (Energy Scarcity)
- Related aspirations in Critical Minerals, Biofouling, and Return_To_Eden

Resolution of those unknowns should reference this framework for standing and decision-rights requirements rather than inventing parallel interface language.

---

## Open Unknowns

| ID | Description | Status | Risk |
|---|---|---|---|
| LGF-001 | Minimum viable standing definition — what concrete acts or recognitions constitute host-community standing for the decision classes above | Open | Major |
| LGF-002 | Conflict-resolution path when node technical constraints and community preferences cannot be reconciled inside hard floors | Open | Major |
| LGF-003 | Exit and non-dependency standards — measurable criteria that an arrangement has not created structural dependence | Open | Major |
| LGF-004 | Interface doctrine with pre-existing informal and formal local institutions (extends WA-003 and related) | Open | Major |
| LGF-005 | Record format for local disposition decisions so they remain legible and revisable across operator changes | Open | Minor |
| LGF-006 | Boundary cases — multi-node deployments, transient or non-geographic communities, and situations with no identifiable host community | Open | Major |
| LGF-007 | Relationship to multi-node or federated structures — does local standing survive upward coordination? | Open | Major |

*All LGF entries are new with this draft. Cross-registration in `Unknowns.md` and an Architecture scope-map entry required on adoption.*

---

## Drift Indicators

- Community-facing obligations are asserted as active doctrine without recorded local standing or ratification
- Surplus is declared and externalized before measured internal closure and resilience margins exist (violation of LGF-P3)
- Any particular surplus-disposition model is treated as background repository doctrine rather than a local, revisable choice
- Arrangements create ongoing dependence with no documented exit path
- Pre-existing local actors are displaced without explicit local justification
- This framework is cited to override Tier 1 Axioms or Ethical_Constraints hard floors
- This framework is treated as a new constitutional tier or parallel authority surface
- Open Unknowns count diverges from what is registered in `Unknowns.md`

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| — | Treating “share the surplus” (or any single disposition model) as settled moral background while leaving only the mechanism open | Converts a local interface decision into an unexamined obligation; precisely the pattern this framework exists to prevent | No |
| — | Defining detailed institutional forms (councils, co-ops, voting systems, etc.) at repository level | Would freeze context-specific design and violate the principle that local form remains local | No |
| — | Placing this document in Admin/ as a “Charter” | Would incorrectly present an institutional interface as repository-level governance authority | No |

---

## Resolution Log

- 2026-09-06: **v0.1-draft.** First articulation of the minimum institutional interface between a Forge deployment and its host community. Responds to the structural gap across the Challenges set (community-sovereignty language without institutional referent) and to the observation that surplus disposition was being treated as a background obligation rather than a local, revisable choice. Placement under Architecture/, naming as Framework, and reframing as interface constraints (not a new governance tier) per classification review. Human-directed; not yet ratified.

---

*This framework defines the minimum institutional interface required for the community-sovereignty claims already present in the Challenges set to become operational without the repository selecting the community’s institutions. It does not freeze local form. The obligation it names is to make standing, decision rights, reversibility, and non-dependency explicit — and to keep surplus disposition a local choice rather than a silent default.*
