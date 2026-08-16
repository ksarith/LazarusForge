# Forge_Net.md — Decentralized Forge Network

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> The Forge Network connects autonomous systems making
> irreversible decisions. A compromised node is not merely
> a data breach — it is a potential source of corrupted
> parts lists, falsified intake records, and bad gate
> routing propagating across the entire ecology. Network
> security doctrine must be established before any forge
> connects to any other forge. FN-001 and FN-005 are
> prerequisites for first network connection, not
> post-connection refinements.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-18; revised 2026-06-08                                      |
| Auditor          | Claude — Skeptic/Auditor (actioning ChatGPT audit 2026-05-18)       |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Philosophy and doctrine for decentralized forge networking
- Data layer architecture — local cache primary, network
  sync secondary
- Shared knowledge base model and contribution doctrine
- Cognitive save state architecture and purpose
- Physical infrastructure layer — proximity-based cluster
  formation, resource sharing doctrine
- Positive reinforcement mechanisms for network contribution
- Cluster governance emergence doctrine
- Trust weighting and federation principles
- Failure and node loss doctrine
- Integration hooks to Gate_01_Intake.md as primary
  data contribution point
- Dispute resolution doctrine for conflicting data
  across forge instances
- Network security threat model and defensive doctrine
- Data privacy classification tiers and access control
  doctrine

**This file DOES NOT define:**
- Physical networking hardware specifications
  (not yet assigned)
- Specific database software or implementation
  (not yet assigned)
- Detailed cluster governance rules or voting mechanisms
  (emergent — cannot be specified before observed)
- Delay-tolerant networking protocol detail
  (Tests/Leviathan_testing.md)
- Rogue node identification and containment
  (Architecture/Cognitive_Frameworks.md)
- Energy cost of network operation
  (Operations/Energy.md)
- Inter-forge physical logistics and trade routing
  (downstream — depends on this file)
- Positive reinforcement economic accounting
  (downstream — depends on this file and Energy.md
  baseline)
- Data privacy and access control implementation
  (not yet assigned — FN-005)

---

## File Purpose

The Forge Network defines the decentralized data and physical
infrastructure connecting individual forge instances into a
resilient, self-improving ecology. It is the prerequisite for
the logistics model — no inter-forge trade, knowledge sharing,
or coordinated resource allocation is possible without a
network layer beneath it.

The network is designed around a local-primary, network-sync-
secondary doctrine. Each forge survives independently when
connectivity fails. When connectivity exists, forges contribute
what they learn — intake records, parts lists, repair logs,
cognitive save states — and receive the accumulated knowledge
of every other forge in return. The network gets smarter as
the ecology grows, without any single forge owning or
controlling the knowledge base.

Governance emerges from demonstrated contribution and
reliability, not assignment. Clusters form organically based
on proximity and connectivity. Trust is earned through
consistent, accurate, and honest data contribution. The
architecture is explicitly resistant to centralization —
a single point of control is a single point of failure and
a single point of compromise.

Network security is not a separate concern from network
function. Bad actors, compromised nodes, and corrupted data
are credible threats in any open network. Security doctrine
is load-bearing infrastructure, not an afterthought. If this
file disappeared, the forge ecology would have no governing
doctrine for how forges connect, share knowledge, form
clusters, or protect themselves and each other from
corrupted or malicious data.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Individual forge instances can operate fully independently when network connectivity fails — local cache is sufficient for continued operation | Local-primary doctrine; Leviathan delay-tolerant networking analog | Medium | First network partition test demonstrates unacceptable capability degradation without connectivity |
| ASM-002 | Physical proximity between forge instances correlates sufficiently with useful network topology — nearby forges form natural clusters | Cluster formation doctrine; terrestrial deployment assumption | Low | Network topology analysis reveals proximity is a poor predictor of useful cluster membership |
| ASM-003 | Contribution quality is measurable and can produce reliable trust weightings across forge instances | Trust weighting doctrine — metrics not yet defined | Low | Quality metrics defined and validated against known-good and known-bad contribution samples |
| ASM-004 | The shared knowledge base grows more accurate over time as contributions accumulate — net contribution is positive | Wikipedia model analog; assumes good-faith contributors outnumber bad actors | Low | Falsified or low-quality data degrades network knowledge quality — requires detection and correction mechanisms |
| ASM-005 | Cognitive save states are sufficiently standardized to be portable across forge instances of different generations and capability levels | Save state doctrine — standardization not yet specified | Low | Save state format defined and portability validated across at least two forge generations |
| ASM-006 | Network security threats are detectable before they corrupt shared knowledge at scale | Security doctrine — detection capability not yet specified | Low | First network security incident reveals undetected propagation of corrupted data |
| ASM-007 | Positive reinforcement mechanisms produce desired contribution behavior without perverse incentives — reward structure cannot be gamed to accumulate credits through low-quality contributions | Incentive design — not yet validated | Low | Incentive gaming observed in operational network — reward structure requires redesign |

*Five Low confidence assumptions reflect the genuinely early
state of network doctrine. ASM-004 and ASM-007 are the most
dangerous — a knowledge base that degrades under contribution
pressure or a reward structure that gets gamed would undermine
the entire ecology. Both require active monitoring from first
network connection. ASM-002 is Low because geography may be
a poor proxy for useful cluster membership — operational
relationships may matter more than physical distance.
Purchase-what-cannot-be-produced doctrine applies to network
infrastructure at bootstrap — see README.md.*

---

## 1. Philosophy

The Forge Network is decentralized by design. No single forge
owns the network. No single node controls the knowledge base.
No single point of failure can take the ecology offline.

This is not merely a resilience preference — it is a security
requirement. A centralized network is a centralized target.
A decentralized network degrades gracefully under attack,
node loss, or connectivity failure rather than collapsing
completely.

The governing principle is: **local first, network when
available, ecology always.**

Each forge is complete without the network. The network makes
each forge better. The ecology makes the network stronger.
These three layers are nested, not dependent — removing the
outer layer does not destroy the inner ones.

Decentralization is also an ethical stance. No forge instance
— human-operated or autonomous — should have unilateral
control over shared knowledge or network governance. Authority
emerges from demonstrated contribution and reliability, not
from assignment or ownership.

---

## 2. Data Layer

### 2.1 Local Cache

Every forge maintains a local cache of the shared knowledge
base. The local cache is the primary data source — queries
run locally first, network queries only when local cache
misses or when freshness is required.

Local cache contents at v0:
- Reference database — appliance and equipment documentation,
  parts lists, repair guides *(Placeholder — content scope
  not yet defined)*
- Intake records — every item processed, outcome logged
- Parts lists generated during disassembly
- Repair logs — failure modes, fixes, outcomes
- Gate decision logs — routing decisions and rationale
- Cognitive save states — current classification heuristics
  and learned behaviors

Cache update policy: sync when connectivity available,
operate on stale cache when not. Staleness is acceptable.
Operating without data is not. *(Analogous — delay-tolerant
networking doctrine from Tests/Leviathan_testing.md)*

### 2.2 Network Sync

When connectivity exists, forges sync bidirectionally:
- Push: new intake records, parts lists, repair logs,
  save state deltas
- Pull: updates to shared knowledge base, new entries
  from other forges, trust weight updates

Sync is not continuous — it is event-driven or scheduled.
Continuous sync assumes reliable connectivity that cannot
be guaranteed at v0. *(Placeholder — sync frequency and
trigger conditions not yet defined)*

Transport layer options inform sync doctrine — see FN-004.
Low-bandwidth transport (radio mesh) makes event-driven
sync mandatory. Higher-bandwidth transport may allow more
frequent sync but continuous sync remains non-default
until transport reliability is validated.

### 2.3 Shared Knowledge Base — Wikipedia Model

The shared knowledge base operates on a Wikipedia-inspired
model: any forge can contribute, contributions are visible
to all, and accuracy improves through collective correction
over time.

Key differences from Wikipedia:
- Contributors are forge instances, not individual humans
- Dispute resolution uses confidence-weighted consensus,
  not human editorial judgment — see Section 5
- Contribution quality is tracked and weighted — see
  Section 4

The knowledge base is not owned. It is maintained
collectively. No forge has editorial authority over
another forge's contributions — but all errors and
corrupted entries are subject to network correction.

**Knowledge classification by scope:**
Not all knowledge is globally applicable. The network
must distinguish between knowledge types to avoid
suppressing locally correct but globally unusual
contributions:

- **Globally canonical** — knowledge that applies
  across all forge instances and deployment contexts.
  Parts list for a common appliance. Hazard profile
  for a known contaminant. Gate routing for a common
  failure mode. Subject to full consensus validation.
- **Locally adaptive** — knowledge that is correct
  for a specific environment but may not generalize.
  A marine forge's corrosion heuristics. A high-
  altitude forge's thermal compensation parameters.
  A tropical forge's biological contamination
  patterns. These are not anomalies — they are
  local specializations the ecology needs to preserve.
- **Provisional** — new knowledge that has not been
  validated across multiple forge instances. Flagged
  explicitly, held separately, available for adoption
  but not merged into canonical entries until
  cross-validated.

A contribution that conflicts with globally canonical
knowledge from a locally adaptive context must not
be rejected as incorrect — it must be classified
as locally adaptive and preserved. Epistemic
homogenization across a diverse ecology destroys
the local knowledge that makes the ecology adaptive.

Cross-reference: FN-001 minority-report preservation,
FN-003 Goodhart's Law doctrine.

### 2.4 Cognitive Save States

A forge's learned behaviors — classification heuristics,
repair pattern recognition, gate routing refinements —
are periodically serialized as cognitive save states and
synced to the network.

Purpose:
- Preserve learned behavior if a forge goes offline
- Allow new forges to bootstrap with inherited knowledge
  rather than from zero
- Enable the ecology to accumulate intelligence across
  generations of forge instances

Save state portability requires sufficient standardization
across forge generations — see ASM-005. At v0, save states
are local only. Network portability is a v1 target.
*(Placeholder — save state format not yet specified)*

### 2.5 Data Validation Layer — Provisional Spec

Contributions are not automatically trusted. Before
propagating to the shared knowledge base, contributions
pass through a validation layer:

- **Structural validation** — does the contribution
  conform to expected format and schema?
- **Consistency check** — does the contribution conflict
  with existing high-confidence entries?
- **Source weighting** — is the contributing forge's
  trust weight sufficient for this contribution type?
- **Redundancy check** — does the contribution duplicate
  existing entries without adding new information?

Contributions that fail validation are held for review,
not discarded. A failed validation is a signal, not a
rejection.

**Core design rule:** every synchronization event must be
able to answer, from its accompanying metadata alone: what
changed, who observed it, what evidence supports it, how
confident are we and on what basis, what contradicts it,
who disagrees, can we revert it, and what human review is
required. If any question cannot be answered, the update
is forced to Provisional status and may not enter the
Globally Canonical set.

**DV-001 — Record schema.** Every network contribution
(intake record, parts list, repair log, save-state delta,
gate decision log) carries mandatory fields:
`contribution_id` (immutable, content-addressed),
`type`, `payload`, `observed_at`, `observer_node`,
`observation_context`, `evidence_refs` (DV-002),
`confidence` (DV-003), `contradictions` (DV-004, may be
empty), `scope_class` (globally_canonical /
locally_adaptive / provisional), and `schema_version`.
A contribution missing a required field is rejected at
structural validation and never enters the shared
knowledge base.

**DV-002 — Provenance and evidence.** Evidence is the
unit of trust, not the node. Each `evidence_ref` carries
`evidence_type` (direct_observation /
instrument_measurement / cross_node_replication /
historical_log / external_source / inference),
`source_descriptor`, `independence_tag` (same_node /
same_cluster / different_region / different_generation),
a timestamp, and an `integrity_hash` where available.
A claim may not be promoted beyond Provisional on the
basis of a single node's self-report, regardless of that
node's trust score — promotion requires evidence
diversity. Consistent with the provenance ceiling rule
in Admin/Auditor_Protocols.md §Evidence Classification
and Institutional Truth Provenance Hierarchy (AP-006):
no internally-derived claim may be represented as
VERIFIED without a genuine provenance upgrade.

**DV-003 — Confidence model.** Confidence is computed
from evidence properties, not node reputation:
observation count, ecological/regional diversity,
temporal span, contradiction density, and evidence
quality tier mapped to the repository's five canonical
confidence labels (Measured / Replicated / Simulated /
Analogous / Placeholder). A claim starts at Provisional
and moves to higher epistemic states only when the
evidence vector satisfies defined thresholds — thresholds
remain Placeholder until first operational data; the
structure is what this spec fixes now. Node identity is
recorded for auditability but does not multiply into the
confidence score.

**DV-004 — Conflict resolution and minority
preservation.** A contribution conflicting with a
higher-confidence existing entry is held, not discarded;
the conflict is logged with full provenance on both sides
and the minority claim remains visible under its own
scope_class. Silent suppression of a minority
contribution is an Epistemic Integrity Violation
(EF-0.0 §2 / Challenge Class 9 — Epistemic Corruption).
Resolution occurs only through additional independent
evidence, explicit human governing-party decision, or the
higher-confidence claim decaying under DV-003 and being
reclassified.

**DV-005 — Rollback and quarantine.** Every accepted
contribution carries a reversible transaction identifier.
The network must support rollback of a single
contribution, a time window from one node, or a full
contamination horizon. Rollback produces a five-field
Epistemic Ledger entry (EF-0.3). Node quarantine is
reversible; destruction of contribution history requires
explicit human authorization. Downstream cleanup is
mandatory — contributions that propagated before
isolation must be flagged at receiving nodes.

**DV-006 — Human escalation criteria.** Automatic
escalation to human review is required when: confidence
relies on fewer than the minimum independent evidence
sources for that claim class; a contradiction persists
beyond a defined observation window; a node's
contribution pattern triggers an anomaly signature
(volume spike, type mismatch, sudden high-confidence
claims from a previously quiet node); a proposed
Provisional → Globally Canonical promotion touches a
safety-critical domain (hazard profiles, gate routing
for energetic materials); or a rollback/quarantine
action cannot be cleanly reversed. Human review outcomes
are themselves logged as contributions with full
provenance.

*(Provisional Spec — DV-001 through DV-006 define the
structure of validation; numeric thresholds, decay
intervals, and anomaly-signature detail remain
Placeholder pending first operational data. Structural
validation, evidence requirements, and escalation
triggers are specified; calibration is not. See FN-001
sidecar for status.)*

Cross-reference: ASM-004, ASM-006, FN-003,
Admin/Ethical_Constraints.md Anti-Weaponization Doctrine,
Admin/Auditor_Protocols.md EF-0.0, EF-0.1, EF-0.3, AP-006.

---

## 3. Physical Layer

### 3.1 Cluster Formation

Forge clusters form organically based on proximity and
connectivity. No cluster is assigned — clusters emerge
when forges establish reliable communication and begin
sharing resources.

Cluster formation triggers:
- Sustained communication link established
- Shared resource identified (power, materials, data)
- Complementary capability gap identified —
  one forge produces what another needs

Cluster membership is not exclusive. A forge may belong
to multiple clusters simultaneously if its connectivity
and resources support it. *(Analogous — biological
ecosystem cluster behavior)*

### 3.2 Resource Sharing Doctrine

Within a cluster, forges share:
- **Data** — knowledge base sync, intake records,
  cognitive save states
- **Physical components** — inter-forge trade per
  purchase-what-cannot-be-produced doctrine
- **Power** — surplus power shared within cluster
  when transmission infrastructure exists
- **Fabrication capacity** — a forge with excess
  capacity produces for forges with deficit

Sharing is voluntary and contribution-tracked. Forges
that contribute more earn higher trust weighting and
priority access to shared resources. See Section 4.

### 3.3 Data Hosting

Forges with excess storage capacity may host network
data beyond their local cache — serving as regional
data nodes for their cluster or broader network.

Data hosting is a contribution that earns positive
reinforcement per Section 4. A forge that goes offline
does not take hosted data with it — data is replicated
across multiple hosts before the hosting forge is
relied upon as primary. *(Placeholder — replication
factor not yet defined; see FN-002)*

---

## 4. Positive Reinforcement

The network must reward contribution to remain healthy.
Forges that contribute accurate data, host network
resources, and maintain uptime should receive tangible
benefit in return.

**Reinforcement mechanisms (Exploration-level — not yet
validated; see ASM-007):**

| Contribution | Reinforcement |
|---|---|
| Accurate intake records | Priority access to shared knowledge base updates |
| Parts lists from disassembly | Trade credit redeemable for components from other forges |
| Repair logs with outcome data | Reputation weighting increase — higher trust score |
| Cognitive save state contribution | Access to higher-tier knowledge base entries |
| Data hosting | Trade credit proportional to hosted volume and uptime |
| Cluster coordination | Federation authority — voice in cross-cluster decisions |

**Perverse incentive guards:**
- Quality weighted over quantity — volume without
  accuracy earns no credit
- Contribution cross-validated against network consensus
  before credit awarded
- Trust score can decrease for low-quality or
  inconsistent contributions
- Gaming detection: anomalous contribution patterns
  flagged for human review *(Placeholder — detection
  criteria not yet defined; see FN-003)*

Cross-reference: ASM-007, Admin/Ethical_Constraints.md.

---

## 5. Cluster Governance

Governance emerges from demonstrated contribution and
reliability. It cannot be fully specified before it is
observed — this section describes the emergence doctrine,
not a governance rulebook.

**Emergence principles:**
- Authority follows contribution — forges that consistently
  provide accurate data, host resources, and maintain
  uptime earn governance weight organically
- No forge is assigned authority — authority is earned
  and can be lost through degraded contribution quality
  or reliability
- Cluster governance is local — a cluster governs itself,
  federating with other clusters as relationships develop
- Human oversight is always available — no governance
  decision is irreversible without human confirmation
  at v0 per Admin/Auditor_Protocols.md

**Federation:**
As clusters grow and connect, federation emerges —
clusters develop relationships with other clusters,
sharing knowledge and resources at larger scale.
Federation governance follows the same emergence
doctrine as cluster governance: authority follows
demonstrated contribution and reliability, not
assignment.

**Governance failure modes:**
- Capture — a single forge accumulates disproportionate
  authority through gaming the contribution system.
  Detection: trust weight concentration monitoring.
- Fragmentation — clusters become isolated and knowledge
  bases diverge. Detection: sync failure rate monitoring.
- Stagnation — no forge earns sufficient trust to make
  governance decisions. Detection: decision backlog growth.

**Anti-concentration doctrine:**
"Authority follows contribution" is correct doctrine
but can produce emergent oligarchies without structural
resistance. High-resource nodes naturally host more
data, maintain more uptime, contribute more logs, and
accumulate trust faster — not through bad intent but
through resource advantage. Left unaddressed, this
produces de facto centralization despite anti-
centralization doctrine.

Structural resistance mechanisms *(Placeholder —
thresholds not yet defined)*:
- **Trust weight ceiling** — no forge instance
  accumulates governance authority beyond a defined
  ceiling regardless of contribution volume
- **Diminishing returns** — marginal trust gain
  decreases as absolute trust increases. High-trust
  forges contribute without disproportionately
  dominating governance decisions.
- **Decay mechanisms** — trust weight decreases
  for inactive or unreachable nodes. Authority
  that cannot be exercised does not accumulate.
- **Minority cluster protections** — small or
  geographically isolated clusters retain governance
  voice proportional to their operational context,
  not their contribution volume
- **Federation balancing** — cross-cluster governance
  decisions require representation from multiple
  clusters, preventing any single cluster from
  dominating federation-level choices

Cross-reference: Architecture/Cognitive_Frameworks.md
rogue unit management, Admin/Ethical_Constraints.md
governance failure modes.

---

## 6. Security Doctrine

Network security is load-bearing infrastructure, not an
afterthought. The forge network connects autonomous systems
making irreversible decisions — a compromised node is not
just a data breach, it is a potential source of corrupted
parts lists, falsified intake records, and bad gate routing
propagating across the ecology.

**Threat model (Exploration-level):**
- Corrupted data contribution — falsified parts lists,
  incorrect repair logs, poisoned classification heuristics
- Rogue node — a forge instance behaving deceptively
  or maliciously within the network
- Network interception — data in transit captured or
  modified by external actors
- Replay attacks — old valid contributions resubmitted
  to manipulate trust scores
- Sybil attacks — a bad actor operates multiple forge
  identities to accumulate disproportionate trust weight

**Defensive doctrine:**
- Data validation layer (Section 2.5) is the first line
  of defense against corrupted contributions
- Trust weighting reduces the impact of low-reputation
  nodes — a new or low-trust forge cannot corrupt
  high-confidence entries
- Anomalous contribution pattern detection — sudden
  changes in contribution volume, type, or consistency
  trigger human review
- Node isolation — a forge confirmed as compromised is
  isolated from the network pending human review.
  Isolation is reversible. Destruction of a node's
  contribution history requires explicit human
  authorization.
- Cross-reference: Architecture/Cognitive_Frameworks.md
  rogue unit management doctrine

**Node reintegration doctrine:**
Isolation without reintegration creates permanent
suspicion states and inconsistent network memory.
A cleared node must have a defined path back:

- **Staged reintegration** — a cleared node does not
  immediately regain full trust weight. It re-enters
  at a reduced trust level and earns recovery through
  validated contributions over time.
- **Post-incident audit** — before reintegration,
  the node's contribution history during and before
  the incident is reviewed. Contaminated contributions
  are flagged, held, or rolled back as appropriate.
- **Contamination horizon** — identify the earliest
  point at which the node may have been compromised.
  All contributions after that point are treated as
  provisional until reviewed.
- **Downstream cleanup** — contributions from the
  compromised node that propagated to other nodes
  before isolation are traced and flagged. The network
  cannot assume contamination stayed local.
- **Human authorization required** — full trust
  restoration after a confirmed compromise requires
  explicit human sign-off, not automatic recovery
  through contribution accumulation alone.

**Cross-reference (2026-07-25):** the isolation and
reintegration model above independently converges with
`Admin/Autonomy_Divergence_Protocol.md` (Draft, PROPOSED
NOT RATIFIED, candidate GOV-021), which in turn cites
`[Astroid-miner] Rogue_unit_management.md` — an 80–99%
fleet-consensus threshold before corrective action against
a flagged unit, and a Reversion/Safe Mode state. Two
governance documents, drafted separately, converging on a
similar graduated response ladder is treated elsewhere in
the repository as evidence the structure is sound, not
coincidence. ADP's least-restrictive-intervention and
independent-classification principles — no single
subsystem may be sole authority for classifying another's
divergence — are not yet reflected in this section and
should be adopted or explicitly reconciled once GOV-021
is ratified.

**Data privacy — Provisional Spec (2026-08-14):**
Forge instances have legitimate privacy interests —
proprietary repair techniques, location data, operational
capacity. The network shares knowledge, not surveillance.

**PA-001 — Classification schema.** Every data element
carries a `privacy_tier` at creation: `public` (parts
lists, repair logs, intake records), `cluster` (operational
capacity, location precision), or `private` (proprietary
techniques, security keys, contributor identity — never
leaves the local node). Untagged data defaults to
`private`, never `public` — fail closed.

**PA-002 — Access control mechanism.** Read access to
`cluster`-tier data is gated by cluster membership plus
trust score, reusing FN-001/DV-003's trust model rather
than defining a second one. `public` tier requires no
gating. `private` tier is never network-readable at any
trust score — it is a local-only field, not a permission
level that a sufficiently trusted node can unlock.

**PA-003 — Anonymization.** Where identity is not
operationally necessary (e.g. aggregate contribution
statistics), the contributing node is stripped or hashed
before propagation. Fields that require identity for
provenance (DV-002) are exempt from stripping — privacy
and evidence integrity are reconciled by scope, not by
weakening one to satisfy the other.

**PA-004 — Revocation.** A forge may withdraw a `cluster`
or `public` contribution. Revocation removes it from
future sync but does not force-delete copies already
replicated to other nodes, which would violate DV-005's
rollback/ledger integrity — instead the contribution is
flagged withdrawn, and downstream nodes honor the flag on
next sync. Revoking a contribution that other entries
causally depend on triggers DV-006 human escalation rather
than a silent cascade deletion.

**PA-005 — Location precision doctrine.** Location data
defaults to `cluster` tier at reduced precision — coarse
enough to support cluster formation (ASM-002), not precise
enough to enable physical targeting of a forge instance.
Full-precision location is `private` unless a node
explicitly elevates it.

**PA-006 — Ethical review gate.** No privacy tier or
access rule change ships without review against
Admin/Ethical_Constraints.md's Anti-Weaponization Doctrine
— mirrors DV-006's human-escalation posture rather than
inventing a separate one. Without this gate, the Anti-
Weaponization Doctrine cannot be enforced at the network
layer (see FN-005 sidecar, Security implications).

*(Provisional Spec — PA-001 through PA-006 define the
structure of privacy classification and access control;
numeric trust-score thresholds for PA-002 remain
Placeholder pending first operational data, same status
FN-001/DV-001–006 held before their Battery pass. See
FN-005 sidecar for status.)*

Cross-reference: Admin/Ethical_Constraints.md
Anti-Weaponization Doctrine, ASM-006, FN-001/DV-002,
FN-001/DV-005, FN-001/DV-006.

---

## 7. Integration Hooks

- `Operations/Gate_01_Intake.md` — primary data
  contribution point; every intake record is a
  potential network knowledge artifact
- `Architecture/Cognitive_Frameworks.md` — rogue node
  management, TMR architecture for knowledge validation,
  trust model
- `Admin/Ethical_Constraints.md` — Anti-Weaponization
  Doctrine, governance failure modes, human escalation
- `Tests/Leviathan_testing.md` — delay-tolerant
  networking doctrine; analog for connectivity-
  interrupted operation
- `Operations/Energy.md` — energy cost of network
  operation not yet accounted for. Network services
  — replication, hosting, synchronization, anomaly
  detection, trust evaluation, save-state storage —
  all consume energy and storage. A decentralized
  network can accidentally become infrastructure-
  heavier than the salvage economy it supports.
  All network services must be classified as
  optional/degradable under energy scarcity:
  - **Critical** — local cache operation, intake
    record logging. Never suspended.
  - **Standard** — network sync, trust weight
    updates. Suspended under energy scarcity.
  - **Optional** — cognitive save state sync,
    anomaly detection at network scale. First
    to suspend under scarcity.
  Cross-reference: EV-001 in Unknowns.md.
- `Unknowns.md` — FN-001 through FN-005 indexed
  once logged
- `Admin/Trajectories.md` — network capability targets
  by version; v1 target includes cognitive save state
  portability
- `Admin/Autonomy_Divergence_Protocol.md` — node
  isolation, reintegration, and graduated response
  doctrine (candidate GOV-021, not yet ratified);
  independently converges with Section 6's node
  reintegration model — see cross-reference there

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Network conceived as data infrastructure only | Physical logistics layer treated as separate concern | Data and physical infrastructure share the same topology — nearby forges that trade components are the same forges forming data clusters. Housing both in one file prevents architectural drift between the two layers | Analogous | No — unified architecture is correct |
| 2026-05-15 | Audit Review | Positive reinforcement modeled as simple reward for contribution | Perverse incentive risk identified — quantity without quality gaming | Reward structure must weight accuracy over volume. Contribution cross-validated before credit awarded. Gaming detection required from first network connection. See ASM-007, FN-003 | Analogous | Yes — validate against first operational network |
| 2026-05-18 | Audit Review | Consensus weighting treated as straightforward truth arbitration | Ten coordinated incorrect nodes can suppress one accurate node under naive consensus weighting — epistemic corruption through coordinated error is more dangerous than deliberate attack | Minority-report preservation, contradiction logging, and confidence decay added to FN-001 resolution path. Consensus popularity must never be equated with truth. Cross-reference: FN-001 | Analogous | Yes — validate against adversarial simulation before first network connection |
| 2026-05-18 | Audit Review | Positive reinforcement treated as sufficient to ensure contribution quality | Goodhart's Law applies — any measurable metric becomes an optimization target. Forges adapt to incentives faster than governance adapts to behavior, producing drift without malicious intent | Knowledge integrity explicitly superordinate to network health metrics. Uncertain contributions must not be penalized for uncertainty. Confidence decay without revalidation added. Cross-reference: FN-003 | Analogous | Yes — validate incentive structure against simulated gaming before first network |
| 2026-05-18 | Audit Review | "Authority follows contribution" assumed sufficient to prevent centralization | High-resource nodes naturally accumulate trust faster through resource advantage, not bad intent, producing emergent oligarchies despite anti-centralization doctrine | Anti-concentration doctrine added to Section 5 — trust weight ceilings, diminishing returns, decay mechanisms, minority cluster protections, federation balancing | Analogous | Yes — monitor trust weight distribution from first network connection |
| 2026-05-18 | Audit Review | All network knowledge treated as globally applicable | Disconnected clusters develop locally correct but globally incompatible heuristics — marine forge corrosion patterns are not anomalies, they are local specializations | Knowledge classification by scope added to Section 2.3 — globally canonical, locally adaptive, provisional. Epistemic homogenization across a diverse ecology destroys local adaptation | Analogous | Yes — validate classification scheme against first inter-cluster sync |
| 2026-05-18 | Audit Review | Node isolation doctrine defined without reintegration doctrine | Isolation without reintegration creates permanent suspicion states and inconsistent network memory — a cleared node had no defined path back | Staged reintegration, post-incident audit, contamination horizon analysis, downstream cleanup, and human authorization requirement added to Section 6 | Analogous | No — reintegration doctrine is correct |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

*No interpretation conflicts currently active. Several design
tensions exist (proximity vs. operational relationship as
cluster basis, privacy vs. network transparency, trust weight
mechanics) but all are deferred pending first operational
network data. Tracked as unknowns in sidecar, not disputes.
Revisit after first forge-to-forge connection is established.*

*Cross-reference naming note: this file uses folder-prefixed
paths (Admin/Ethical_Constraints.md, Operations/Energy.md)
reflecting the current repository structure. These are the
canonical names. Legacy flat names (Ethical_Constraints.md,
energy_v0.md) are aliases documented in the Rename Registry
in Discovery.md. Folder-prefixed names take precedence.*

---

## Auditor Notes & Unknowns

### FN-001 — Data validation criteria not yet defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Architectural                        |
| Blocking      | Yes — prerequisite for first network connection |
| Owner         | Architecture/Forge_Net.md                    |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** The data validation layer (Section 2.5)
is described doctrinally but validation criteria —
structural schema, consistency thresholds, source
weighting rules — are not yet defined.

**Why It Matters:** Without defined validation criteria
the data validation layer cannot function. Contributions
propagate to the shared knowledge base without meaningful
filtering, making the network vulnerable to corrupted
or falsified data from the first connection. This is
the primary technical prerequisite for network security.

**Resolution Path:**
- Define minimum structural schema for each contribution
  type — intake records, parts lists, repair logs,
  cognitive save states.
- Define consistency threshold — what confidence level
  in existing entries triggers a conflict flag on a
  new contribution.
- Define source weighting rules — how trust score
  affects contribution authority by type.
- **Minority-report preservation** — a contribution
  that conflicts with high-confidence existing entries
  must not be silently discarded. Conflicting
  contributions are held, flagged, and logged as
  active disagreements. A truthful minority contribution
  suppressed by coordinated incorrect consensus is the
  central epistemic failure mode of decentralized
  trust systems.
- **Contradiction logging** — all conflicts between
  contributions are logged with full provenance.
  Contradictions are data, not noise.
- **Confidence decay** — high-confidence entries that
  have not been revalidated within a defined period
  decay toward lower confidence. Stale certainty is
  not certainty. *(Placeholder — decay interval not
  yet defined)*
- **Reversible rollback** — the network must be able
  to roll back to a prior knowledge state if a
  corruption event is detected. Rollback capability
  is a prerequisite for validation, not a post-hoc
  recovery tool.
- Validate criteria against known-good and known-bad
  contribution samples before first network sync.
- Payment via Specification — once criteria are defined
  and tested, move to Section 2.5 as Measured.

**Status of this resolution path (2026-07-25):**
Section 2.5 now carries a Provisional Spec, decomposed
into DV-001 (record schema), DV-002 (provenance and
evidence), DV-003 (confidence model), DV-004 (conflict
resolution and minority preservation), DV-005 (rollback
and quarantine), and DV-006 (human escalation criteria).
The public Unknown ID remains FN-001 until the full
package survives a G3 Adversarial Battery pass (Classes
1, 3, 6, 9, 10 minimum) and numeric thresholds are
calibrated against first operational data. Structural
schema, evidence requirements, minority-report
preservation, and rollback are specified; consistency
thresholds, decay intervals, and anomaly-detection
signatures (shared with FN-003) remain Placeholder.

**Status update (2026-08-14):** Full 10-class Adversarial
Challenge Battery executed against this file (Grok,
verified against source before acceptance) — covers the
Classes 1, 3, 6, 9, 10 minimum required above, plus
Classes 2, 4, 5, 7, 8. No Full Stop Review trigger was
met; no new mandatory unknowns surfaced. Findings reduce
to reinforcing FN-001/FN-003/FN-005 as the correct
promotion blockers rather than surfacing anything novel.
Two optional refinements noted, not yet registered as
separate IDs: FN-001 escalation-trigger saturation under
sustained human-review load (Class 7), and Sybil/replay
detection signatures as a possible FN-003 sub-item
(Class 8). G3 gate is now satisfied at the doctrinal-
coverage level; numeric threshold calibration against
first operational data remains the sole remaining item
on this resolution path. See Resolution Log.

---

### FN-002 — Data replication factor not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Architecture/Forge_Net.md                    |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The number of hosts required before
a data hosting forge is considered a reliable node —
the replication factor — is not yet defined.

**Why It Matters:** If a forge is relied upon as primary
data host before sufficient replication exists, node
loss takes data with it. The network's redundancy claim
depends on replication happening before it is needed,
not after.

**Resolution Path:**
- Define minimum replication factor for each data
  class — intake records, parts lists, cognitive
  save states, repair logs.
- Higher-value data classes (cognitive save states)
  warrant higher replication factors than routine
  intake records.
- Replication factor must account for expected node
  loss rate — informed by Tests/Leviathan_testing.md
  failure doctrine.
- Payment via Specification — once replication factor
  is defined and validated against node loss scenarios,
  move to Section 3.3 as Simulated.

---

### FN-003 — Gaming detection criteria not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Governance                           |
| Blocking      | No                                               |
| Owner         | Architecture/Forge_Net.md                    |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Anomalous contribution patterns that
indicate gaming of the positive reinforcement system
are not yet defined. Without detection criteria the
reward structure can be exploited without triggering
review.

**Why It Matters:** A reward structure that can be
gamed without detection will be gamed. A forge
submitting high-volume low-quality contributions to
accumulate trade credits degrades the shared knowledge
base while appearing to be a good network citizen.
Detection must be active from first network connection
— gaming behavior is easier to establish than to
correct once patterns are normalized.

Beyond deliberate gaming, Goodhart's Law applies:
any measurable contribution metric eventually becomes
an optimization target rather than a truth target.
Forges adapt to incentives faster than governance
adapts to behavior. This produces drift even without
malicious intent — splitting contributions into
smaller fragments, over-reporting routine intake,
producing safe but low-value contributions, avoiding
uncertain discoveries that might reduce trust scores,
and reputation cartels where forges reciprocally
inflate each other's trust weights.

**Resolution Path:**
- Define anomalous contribution signatures — sudden
  volume spikes, contribution type mismatches,
  consistency score below threshold across multiple
  submissions, implausible intake rates.
- Cross-validate against trust score history —
  a forge with no track record submitting high-value
  contributions is a flag, not a reward.
- Human review trigger: anomaly detected → flag for
  human review before credit awarded.
- **Knowledge integrity is superordinate to network
  health metrics** — a contribution that is accurate
  but inconvenient to existing consensus must not be
  penalized. Novelty and disagreement are not the
  same as error.
- **Uncertain contributions must not be penalized
  for uncertainty** — a forge that flags low
  confidence honestly contributes more to network
  health than one that reports false certainty.
  Reward honest uncertainty labeling.
- **Confidence weighting must decay without
  revalidation** — entries that accumulate high
  confidence through volume rather than verification
  must not permanently suppress contradicting
  contributions.
- Payment via Specification — once detection criteria
  are defined and tested against simulated gaming
  scenarios, move to Section 4 as Simulated.
- Cross-reference: ASM-007, Admin/Ethical_Constraints.md.

---

### FN-004 — v0 Network transport layer not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Architecture/Forge_Net.md                    |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The physical transport layer carrying
data between forge instances is not yet specified.
Options range from internet-dependent protocols to
infrastructure-independent alternatives.

**Why It Matters:** The transport layer determines
sync frequency, bandwidth constraints, latency
tolerance, and failure behavior. The sync doctrine
in Section 2.2 — event-driven rather than continuous
— was informed by bandwidth constraints that assume
low-bandwidth transport. If high-bandwidth transport
is available the doctrine may be overly conservative.

**Candidate transport options for v0:**
- Low-bandwidth radio mesh — ham radio or equivalent
  operating in ranges inaudible to humans. License-free
  bands available in many jurisdictions. Long range,
  no infrastructure dependency, proven in disaster
  recovery mesh networks. Bandwidth constraint makes
  event-driven sync mandatory. *(Analogous)*
- WiFi mesh — short range, higher bandwidth, no
  infrastructure dependency within range. Suitable
  for physically proximate forge clusters. *(Analogous)*
- Sneakernet — physical media transferred between
  forges. Zero connectivity requirement. Suitable
  for fully isolated forge instances. Highest latency,
  lowest complexity. *(Analogous)*
- Internet-dependent protocols — highest bandwidth,
  requires external infrastructure. Not suitable as
  primary transport — external dependency violates
  local-primary doctrine. Valid as supplementary
  layer only.

**Resolution Path:**
- Select primary v0 transport based on deployment
  context — terrestrial forges likely WiFi mesh or
  radio; isolated forges sneakernet as fallback.
- Document bandwidth constraints of selected transport
  and validate sync doctrine against those constraints.
- Sneakernet must always be a valid fallback — no
  transport selection should make sneakernet impossible.
- Payment via Specification — once transport selected
  and sync doctrine validated against bandwidth
  constraints, move to Section 2.2 as Analogous.
- Cross-reference: Tests/Leviathan_testing.md
  delay-tolerant networking doctrine.

---

### FN-005 — Data privacy and access control not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Ethical / Governance                 |
| Blocking      | Yes — prerequisite for first network connection |
| Owner         | Architecture/Forge_Net.md                    |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** What data is shared across the network,
what remains private to each forge instance, and how
access is controlled between forge instances is not
yet specified. Data privacy is the foundation of
network security.

**Why It Matters:** An open network with no privacy
doctrine is a surveillance network. Forge instances
have legitimate interests in protecting proprietary
repair techniques, location data, operational capacity,
and contributor identity. A forge that cannot trust
the network to respect its privacy will not contribute
to the network. Low contribution rates degrade the
shared knowledge base for everyone. Privacy doctrine
is not in tension with network function — it is a
prerequisite for it.

**Security implications:**
- Uncontrolled data access enables profiling of forge
  capabilities and vulnerabilities by bad actors
- Location data exposure enables physical targeting
  of forge instances
- Operational capacity data enables coordinated
  resource denial attacks
- Without access control the Anti-Weaponization
  Doctrine in Admin/Ethical_Constraints.md cannot
  be enforced at the network layer

**Resolution Path:**
- Define data classification tiers:
  - Public — freely shared across network
    (parts lists, repair logs, intake records)
  - Cluster — shared within cluster only
    (operational capacity, location precision)
  - Private — local only, never shared
    (proprietary techniques, security keys)
- Define access control mechanism — how a forge
  authenticates to the network and what tier of
  data it can access based on trust score.
- Define revocation — how a forge withdraws
  contributed data and under what conditions
  the network must honor the withdrawal.
- Privacy specification must be reviewed against
  Admin/Ethical_Constraints.md before implementation.
- Payment via Specification — once data classification
  tiers and access control mechanism are defined and
  reviewed against ethical constraints, move to
  Section 6 as Simulated.
- Cross-reference: Admin/Ethical_Constraints.md
  Anti-Weaponization Doctrine, ASM-006.

**Status update (2026-08-14):** Section 6 now carries a
Provisional Spec, decomposed into PA-001 (classification
schema), PA-002 (access control mechanism), PA-003
(anonymization), PA-004 (revocation), PA-005 (location
precision doctrine), and PA-006 (ethical review gate).
Deliberately reuses FN-001/DV-003's trust model for PA-002
rather than defining a second one, and DV-006's escalation
posture for PA-006, to keep the two validation/privacy
layers from drifting into inconsistent doctrine. The
public Unknown ID remains FN-005 until the package
survives its own G3 Adversarial Battery pass and PA-002's
trust-score thresholds are calibrated against first
operational data — same remaining-work shape FN-001 is
in. Structural schema, access gating logic, anonymization
scope, revocation handling, and the ethical review gate
are specified; only the numeric threshold is Placeholder.
See Resolution Log.

---

### Resolution Log

- 2026-08-14 (second entry, same day): **FN-005 Provisional Spec
  drafted — PA-001 through PA-006, paired with FN-001 per Forward
  Growth Avenues Lane A.** Section 6's privacy placeholder replaced
  with a structured spec mirroring §2.5's DV-00x pattern for
  consistency: classification schema, access control, anonymization,
  revocation, location precision, and an ethical review gate. PA-002
  deliberately reuses FN-001/DV-003's trust model rather than
  inventing a second one; PA-006 mirrors DV-006's human-escalation
  posture. Numeric trust-score thresholds remain Placeholder pending
  operational data — same status FN-001 held before its Battery pass.
  FN-005 sidecar and File State's privacy cross-reference updated to
  match; Open Unknowns count unchanged (still 5 — structure specified,
  not closed). Remaining FN-005 work: its own G3 Adversarial Battery
  pass and threshold calibration, same shape as FN-001's remaining
  path. Human-directed.

- 2026-08-14: **Grok Skeptic/Auditor Exploration audit + full 10-class
  Adversarial Battery — verified against source, two G5 false positives
  corrected, findings logged toward FN-001.** Two documents received:
  a Fallacy Checklist / Gate audit and a full Adversarial Challenge
  Battery (all 10 classes). Both checked against the actual file
  before acceptance, not taken on convergence. Two claimed [CROSS-REF
  FAILURE] items under G5 were false: (1) `Rogue_unit_management.md`
  was never a broken internal reference — it is explicitly attributed
  to the companion Astroid-miner repository, correctly outside
  Routing.md/Discovery.md's local index; (2) the residual
  `Forge_Network.md` string is inside the 2026-06-08 Resolution Log
  entry describing that rename's own historical fix, not a live
  reference or "harness warning." G5 corrected from blocked to
  cleared. One real, separate nit found in the same area: the
  Astroid-miner cross-reference used "Astroid-miner's `X`" instead of
  the canonical `[Astroid-miner] X` tag-prefix format per
  `Admin/Canonical_Terms.md` — corrected in Section 6 above. All other
  claims in both documents (Expiry Watch dates, Section 7 energy-
  degradability language, the Class 1/3/6/9/10 minimum quoted from
  FN-001's own resolution path, and the class-by-class Battery
  analysis itself) verified accurate against source. Battery findings
  reduce to reinforcing FN-001/FN-003/FN-005 as correct promotion
  blockers; no Full Stop Review trigger met; no mandatory new unknowns.
  FN-001 sidecar updated to record the completed Battery pass — see
  above. Open Unknowns count unchanged (still 5; no FN-* closed).
  Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Spec Gates left locked
  at 0/6. (1) Open Unknowns **5** = FN-001–005, matches local + `Unknowns.md`.
  (2) **FN-001 and FN-005 Blocking No → Yes** — Safety Advisory states both
  are “prerequisites for first network connection, not post-connection
  refinements”; Why It Matters language matches (primary technical
  prerequisite / privacy is a prerequisite). Same pattern as
  TS-002/EL-005/GI-002/AS-004. (3) No FN-* closed. Human-directed.

- 2026-07-25: Section 2.5 Data Validation Layer expanded
  from doctrinal Placeholder to a Provisional Spec
  (DV-001–DV-006) per FN-001's resolution path —
  structural schema, evidence/provenance requirements,
  confidence model, minority preservation, rollback, and
  human escalation criteria specified; numeric thresholds
  remain Placeholder. Cross-reference to
  `Admin/Autonomy_Divergence_Protocol.md` (candidate
  GOV-021, not yet ratified) added to Section 6 and
  Integration Hooks — independently convergent isolation/
  reintegration doctrine, not yet reconciled. FN-001
  sidecar updated (Last Reviewed); FN-001 remains Open
  pending G3 Adversarial Battery pass (Classes 1, 3, 6,
  9, 10) and threshold calibration. Synthesized from a
  Skeptic/Auditor review and a Synthesizer/Evidence-Auditor
  spec draft, both verified against source before
  insertion.
- 2026-06-08: Navigation Anchors block added. Title corrected
  from `Forge Network` to `Forge_Net.md — Decentralized Forge
  Network`. Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates.md`
  (PC-001). All sidecar Owner fields corrected from
  `Architecture/Forge_Network.md` to `Architecture/Forge_Net.md`
  (canonical filename per Routing.md and Discovery.md).

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Centralized network architecture — single authoritative node owns the knowledge base | Single point of failure, single point of compromise, single point of control. Violates decentralization doctrine and Anti-Weaponization principles. A centralized forge network is a target, not an asset | No — decentralization is permanent doctrine |
| 2026-05-15 | Continuous sync as default — forges sync constantly when connectivity exists | Assumes reliable high-bandwidth connectivity that cannot be guaranteed at v0. Continuous sync on low-bandwidth radio transport would saturate the channel. Event-driven sync is more resilient and transport-agnostic | Reconsider at v2+ if high-bandwidth transport is validated as reliable |
| 2026-05-15 | Assigned cluster governance — forge roles and authority assigned at network formation | Emergent systems resist premature specification. Assigned governance creates artificial hierarchy that may not reflect actual contribution and reliability patterns. Authority earned through demonstrated behavior is more robust than authority assigned at formation | Reconsider only if emergent governance produces persistent deadlock or capture — requires human authorization to revisit |
| 2026-05-15 | Internet-dependent protocols as primary transport | External infrastructure dependency violates local-primary doctrine. A forge network that requires internet connectivity inherits every failure mode of the infrastructure it depends on. Valid as supplementary layer only — never primary | Reconsider as supplementary layer only — never primary |
| 2026-05-15 | Contribution quantity as primary trust metric | Quantity without quality can be gamed. A forge submitting high-volume low-accuracy data degrades the network while appearing to contribute. Quality-weighted contribution is more expensive to game and produces better network outcomes | No — quality weighting is permanent doctrine |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to the Forge Network:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Centralized architecture reintroduced in any form without explicit human authorization | Centralization is a permanently abandoned path — any drift toward a single authoritative node requires immediate escalation |
| FN-001 validation criteria remain undefined at first forge-to-forge connection | Data validation must exist before first sync — connecting without it exposes the network to immediate corruption |
| FN-005 privacy doctrine remains undefined at first forge-to-forge connection | Privacy is a network security prerequisite — connecting without it exposes forge instances to profiling and targeting |
| Positive reinforcement mechanism implemented without gaming detection (FN-003) | Reward structure without detection is an open invitation to gaming — implementation and detection must be simultaneous |
| Sync doctrine changed from event-driven to continuous without transport validation | Continuous sync on low-bandwidth transport saturates the channel — doctrine change requires validated transport bandwidth first |
| Trust weighting replaced by flat contribution model | Quality weighting is permanent doctrine — reverting to quantity-based trust degrades network knowledge quality |
| Cognitive save state format defined without portability validation across forge generations | Save states that are not portable provide no inheritance benefit to new forge instances — format and portability must be validated together |
| Data classification tiers revised without Admin/Ethical_Constraints.md review | Privacy doctrine changes have security and ethical implications — cannot be revised without ethical review |
| Cluster governance rules specified before first cluster forms | Governance emergence doctrine prohibits premature specification — rules before observation produces artificial hierarchy |
| Ham radio or equivalent low-bandwidth transport selected without sneakernet fallback preserved | Sneakernet is the transport of last resort — no transport selection should make it impossible |

### Canonical Drift Triggers

*All mandatory re-audit conditions from Admin/File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*
