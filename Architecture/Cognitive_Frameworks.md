# Cognitive_Frameworks.md — Distributed Cognition & Trust Architectures

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-09 (ChatGPT — Synthesizer); revised 2026-06-08; revised 2026-06-27; revised 2026-07-26; revised 2026-07-28 |
| Auditor          | Claude — Retrofit/Auditor; revised Claude — Synthesizer/Auditor; Gemini — Skeptic/Auditor (Exploration audit), Claude — Synthesizer/Auditor (verification against source, corrections), CF-DS-002 ratified by human governing authority, CF-DS-001 resolved (Claude + Grok, independently confirmed), 2026-07-26; Claude — Synthesizer/Auditor, Section IV revised with formal transition triggers from `Admin/Computational_Institutional_Reasoning.md` §5.4, CF-004 updated, Section IX consistency check performed (human-directed), 2026-07-28 |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cognitive reliability architectures for autonomous
  Forge systems
- Distributed trust models and redundancy frameworks
- Framework taxonomy (A through G) — from lone
  intelligence to simulation-gated cognition
- Confidence collapse states and associated responses
- Split-brain handling doctrine
- Return-to-base and stasis logic
- Human override positioning and mutual stabilization
  doctrine
- Algorithm architecture — the computational structure
  that emerges from Forge doctrine (Section IX)
- Epistemic Load Regulation — Triage Posture doctrine
  governing system behavior under epistemic debt
  accumulation (Section IX)
- Guiding axioms for safe cognition under uncertainty

**This file DOES NOT define:**
- PCB fabrication or specific MCU wiring
  (`Operations/Electronics.md`)
- Mechanical actuator details
  (`Architecture/Mechanical_Structures.md`)
- Ethical policy itself
  (`Admin/Ethical_Constraints.md`)
- Individual Leviathan mission logic
  (`Tests/Leviathan_testing.md`)
- Networking implementation details
  (`Architecture/Forge_Net.md`)
- Cryptographic protocol specifics
  (`Admin/Security_Protocols.md`)
- Full autonomous governance law
  (`Admin/Governance_Charter.md`)
- Hardware watchdog circuit implementation
  (`Operations/Electronics.md` CF-001)
- Formal debt measurement implementation
  (CF-004 — see sidecar)

---

## File Purpose

This file defines how Forge systems think safely under
uncertainty, and what those thinking systems are
computationally attempting to do.

The Forge assumes degraded environments, imperfect
hardware, incomplete information, damaged sensors,
adversarial conditions, and partial system corruption
as normal operating conditions rather than edge cases.
Cognitive Frameworks exist to prevent isolated faults,
hallucinations, firmware corruption, or confidence
collapse from turning local errors into catastrophic
actions.

The goal is not perfect intelligence. The goal is
**survivable cognition**.

Section IX extends this into a formal description of
the algorithm architecture that the doctrine implies —
not a single algorithm, but a class of algorithms that
emerges from the Forge's foundational assumptions about
knowledge, uncertainty, and reality. Understanding this
architecture is necessary for translating doctrine into
machine behavior.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Degraded environments, damaged sensors, and partial corruption are normal operating conditions — not edge cases | Salvage-first doctrine; hostile deployment environments | Analogous | v0 operational data contradicts this — environment is consistently benign and controlled |
| ASM-002 | Mechanical constraints are more reliable than software constraints under failure conditions | Physical law vs. programmable logic; Layer 0 doctrine | Analogous | A hardware failure mode is identified where mechanical constraints become less reliable than software under specific conditions |
| ASM-003 | Three AI models with different training lineages provide meaningful cognitive diversity for consensus purposes | Model diversity assumption; CF-002 dependency | Placeholder | Correlated AI failure mode study (CF-002) characterizes actual reasoning overlap — diversity must be demonstrated, not assumed |
| ASM-004 | Human override remains meaningful and executable under degraded communication conditions | Human governance doctrine; Layer 6 | Analogous | Operational scenario arises where human override cannot be executed in time to prevent harm — override doctrine must be revised |
| ASM-005 | The algorithm architecture described in Section IX accurately characterizes the emergent computational behavior of the doctrine | Synthesis from ChatGPT Synthesizer analysis; cross-checked against repository structure | Analogous | Operational experience or formal analysis reveals a significant gap between described and actual emergent behavior |

---

## I. Core Doctrine

**Intelligence Is Treated as a Hazard Source**

A sufficiently autonomous system can generate incorrect
conclusions, fabricated certainty, unsafe optimization
paths, recursive logic traps, or coordinated failure
cascades. Therefore: cognition is monitored, confidence
is monitored, and disagreement is treated as signal
rather than nuisance.

> A machine can be physically functional while
> cognitively compromised.

**The Forge Does Not Assume Perfect Truth**

Reality may be partially observable, contradictory,
delayed, noisy, spoofed, or unknowable. Therefore the
Forge prioritizes bounded confidence, graceful
degradation, and reversible decisions over maximum
autonomy, maximum speed, or centralized certainty.

**Mechanical Truth Outranks Software Confidence**

Software may hallucinate. Sensors may drift. Firmware
may corrupt. Consensus may fail. Physical safety
boundaries must remain enforceable even during total
cognitive collapse.

Examples: watchdog relays, spring-return neutral states,
deadman switches, passive thermal shutdown, physical
docking locks.

No cognition layer is considered authoritative over
hard-safe physical constraints.

---

## II. Cognitive Reliability Layers

| Layer | Function |
|---|---|
| Layer 0 | Mechanical truth / passive safety |
| Layer 1 | Hardware watchdog enforcement |
| Layer 2 | Local controller logic |
| Layer 3 | Redundant arbitration |
| Layer 4 | Supervisory consensus |
| Layer 5 | Mission coordination |
| Layer 6 | Human governance override |

Failure containment should occur at the lowest possible
layer. A fault contained at Layer 1 is always
preferable to one that escalates to Layer 6.

---

## III. Framework Taxonomy

### Framework A — Lone Intelligence
Single controller → actuator system. Simplest
architecture, fastest response, minimal overhead.
**Forbidden for:** high-mass autonomous Leviathans,
weapons-capable systems, critical environmental
control, irreversible operations.

### Framework B — Lone AI + Hardware Watchdog
AI controls behavior. Watchdog controls boundaries.
If heartbeat, timing, or safety conditions fail:
watchdog interrupts motion, forces neutral state, or
returns unit to stasis. **Recommended v0 baseline** —
minimum acceptable architecture for early autonomous
Forge systems.

### Framework C — Dual Redundancy
Both systems cross-check each other. Detects anomalies
but cannot resolve 1v1 deadlock. Requires human
arbitration, supervisory AI, or return-to-base doctrine
for resolution.

### Framework D — Triple Modular Redundancy (TMR)
Three independent systems attempt the same task.
Majority agreement determines output. Tolerates
isolated faults and filters transient corruption.

**Diversity requirement:** True TMR requires
architectural diversity, firmware diversity, power-path
diversity, or manufacturing diversity. Three identical
damaged systems are not true redundancy. Correlated
failures and shared firmware defects bypass TMR
protection entirely.

*Cross-reference: `Operations/Electronics.md`
§Hardware TMR Implementation for circuit-level detail.*

### Framework E — Hierarchical Ruler + Advisors
One primary intelligence acts as executive authority.
Secondary systems provide challenge, verification,
simulation, or dissent. Advisors do not directly
control motion unless escalation conditions trigger.

| Advisor Type | Role |
|---|---|
| Safety advisor | Constraint checking |
| Navigation advisor | Spatial validation |
| Ethical advisor | Dual-use boundary checks |
| Energy advisor | Resource conservation |
| Simulation advisor | Predictive outcome testing |

### Framework F — Supervisory Consensus Network
Local units retain operational autonomy while a
supervisory layer monitors behavior, validates mission
coherence, and intervenes during confidence collapse.
Aligns naturally with Support Raft systems, Leviathan
fleets, and distributed salvage operations.
*Cross-reference: `Tests/Support_Raft.md`
§Orchestration & Data Tether.*

### Framework G — Simulation-Gated Cognition
Actions are simulated before execution. If predicted
outcomes exceed risk threshold: action blocked or
escalated. Computationally expensive. **Status:
Exploratory — likely v2/v3 architecture.**
*Cross-reference: `Tests/Support_Raft.md`
Guardian Protocol.*

### Authority Scope Boundary (resolves CF-DS-001)

Frameworks E and F are not competing philosophies —
they are the same doctrine applied at two different
decision scales. Which one governs a given decision
is determined by the criteria below, not by a
standing commitment to either architecture.

**A decision stays at local unit autonomy (Framework F's
local layer) only if all four hold:**
1. **Scope-confined** — effect is limited to the
   deciding unit; no other unit's behavior, knowledge,
   or shared parameters are changed.
2. **Reversible or fail-safe** — the action does not
   cross an `Admin/Ethical_Constraints.md` hard floor
   and can be undone or safely contained if wrong.
3. **Time-critical** — the delay required to route
   through the supervisory/advisory layer would itself
   cause harm, mission-critical loss, or unit loss.
4. **Confidence state is Green or Yellow** — see
   Section IV. A unit in Orange or worse has already
   lost the standing to self-certify a scope-confined
   judgment; escalation is mandatory regardless of the
   other three criteria.

**A decision routes through the supervisory/advisory
layer (Framework E's pattern — challenge and dissent
authority, not command authority) if any hold:**
1. Effect is swarm-wide — shared parameters, cached
   governance documents, or other units' operating
   behavior would change.
2. The action approaches or crosses an
   `Ethical_Constraints.md` boundary.
3. The action is irreversible and not urgent enough to
   justify bypassing challenge.
4. Confidence state is Orange or worse.

This is a direct generalization of `Tests/Support_Raft.md`'s
comms-blackout May/May-Not split (continue charging,
execute Stasis Mode, execute unit recovery, shed panels
= local; update cached reference documents, modify
swarm-wide operating parameters, authorize outside
`Ethical_Constraints.md` = supervisory) to the general
case, including when comms are available. The boundary
was already correct for the blackout case; it did not
need to be invented, only stated as doctrine that
applies independent of comms state.

**What "supervisory" does not mean:** Framework E's
advisors challenge and can trigger escalation; they do
not unilaterally command. No advisor may plan, execute,
and self-authorize the same action — Axiom Q-2
(Separation of Powers) applies to the advisor layer
exactly as it applies to any other agent. A "supervisory"
decision is one subject to challenge before it takes
effect, not one made unilaterally by a higher authority
in place of the unit.

---

## IV. Confidence Collapse States

| State | Meaning | Typical Response | Formal Trigger |
|---|---|---|---|
| Green | Stable consensus | Normal operation | $dD_e/dt \le 0$ — Stable Operating Zone or Neutral Equilibrium (CIR §5.3) |
| Yellow | Minority disagreement | Increase logging | $dD_e/dt > 0$, rolling average not yet past $\varepsilon_{\text{triage}}$ |
| Orange | Persistent disagreement | Slow operations; Triage Posture active | Rolling average of $dD_e/dt$ over $N$ audit cycles breaches $\varepsilon_{\text{triage}}$ — CIR §5.4 Entry Condition |
| Red | Cognitive instability | Enter caution/stasis | Sustained $\ddot{D}_e > 0$ — Collapse Region (CIR §5.3): debt accumulation itself accelerating, not merely present |
| Black | Trust chain compromised | Mechanical lockdown | Direct detection of trust chain compromise — bypasses the debt-derivative ladder entirely |

Transitions are not purely linear. A system can move
from Green to Black if trust chain compromise is
detected directly, bypassing intermediate states —
Black remains a direct-detection condition, not
derived from the debt derivative, exactly as before
this revision. Downward transitions (toward Green)
require explicit re-verification, not mere absence
of new faults.

**Revised 2026-07-28:** The Yellow→Orange transition
— previously undefined, tracked as CF-004 — now has
a formal trigger. `Admin/Computational Institutional
Reasoning` §5.4 (The Automated Triage Posture
Trigger) defines this exact condition and proves it
stable under a Lyapunov argument (§5.4 Theorem 3):
the trajectory cannot oscillate indefinitely once
triage engages. Entering Orange is the same event as
this file's Epistemic Load Regulation section
(Section IX) entering Triage Posture — they are one
mechanism described from two angles, not two
mechanisms that happen to agree. Exit follows the
same hysteresis in both descriptions: the rolling
debt derivative must demonstrate sustained reduction
beneath $-\varepsilon_{\text{exit}}$ before returning
to Yellow — not mere absence of new faults, consistent
with this section's existing downward-transition
requirement above.

Green, Yellow, and Orange correspond to CIR §5.3's
Stability Regimes (Stable Operating Zone / Neutral
Equilibrium / Triage Zone, respectively). Red
corresponds to the Collapse Region — note this
requires the *second* derivative of debt to be
sustained positive, i.e. debt growth that is itself
accelerating, a strictly harder condition than simply
carrying high debt. A system can sit in Orange
indefinitely without ever reaching Red if its debt
growth rate is elevated but not worsening.

**Calibration status:** the mathematical form and
stability proof are established. The specific numeric
values for $\theta_p$, $\varepsilon_{\text{triage}}$,
$\varepsilon_{\text{exit}}$, and the audit-cycle
window $N$ remain undefined — see CF-004, whose scope
now narrows to calibration rather than formal
definition. Until calibrated, Orange/Triage Posture
entry and exit remain human judgment calls, as
before; this revision changes what the judgment is
checked against, not who makes it.

**Consistency check against Section IX (2026-07-28):**
Section IX's Confidence Propagation rule
($\text{confidence}(A) \le \text{confidence}(B)$ for
dependent nodes, operating on the Measured / Replicated
/ Simulated / Analogous / Placeholder label set) is
unaffected by this revision — it governs per-claim
evidentiary confidence, an orthogonal axis to these
system-level aggregate debt states. Triage Posture
entering Orange changes agent bandwidth allocation
toward verification, which can accelerate individual
claims moving up the label set, but does not alter
the propagation rule itself. No change required there.

---

## V. Return-to-Base Doctrine

When confidence falls below operational threshold,
mission completion becomes secondary — preservation
becomes primary.

Return-to-base triggers: unresolved split-brain,
navigation uncertainty, watchdog anomalies, repeated
voter instability, or firmware integrity failure.

A damaged but recoverable unit is preferable to
autonomous escalation, uncontrolled movement, or
irreversible environmental harm.

---

## VI. Split-Brain Doctrine

A split-brain state occurs when no stable consensus
exists, arbitration confidence collapses, or identity
continuity becomes uncertain. The Forge treats
unresolved split-brain as a **safety condition**, not
merely a software bug.

Default response:
1. Halt non-essential actions
2. Preserve logs
3. Reduce energy state
4. Request supervisory intervention
5. Enter stasis if unresolved

*Identity continuity during split-brain: see CF-003
in sidecar and `Admin/Ship_of_Theseus.md`
§Relationship to Forge Doctrine.*

---

## VII. Human Position in the Stack

The Forge is autonomy-assisted, not
autonomy-worshipping. Humans remain final governors,
final ethical authorities, and final override
capability. However, humans are also fallible,
inconsistent, fatigued, and bandwidth-limited.
Therefore humans supervise systems — but systems also
constrain humans through hard safety doctrine.

The goal is **mutual stabilization**, not unilateral
dominance.

*Cross-reference: `Admin/Ethical_Constraints.md` for
hard-line doctrines that override both AI and human
override attempts.*

---

## VIII. Guiding Axioms

- Consensus is evidence, not proof.
- Silence between systems is not agreement.
- A confident machine can still be wrong.
- Diversity matters more than quantity.
- Mechanical truth outranks software confidence.
- The safest system is the one that can stop itself.
- A machine that cannot admit uncertainty is unsafe.
- Unknowns are assets, not failures.
- Reality has the final vote.

---

## IX. Algorithm Architecture

*Synthesized from ChatGPT Synthesizer analysis,
2026-06-08. Reviewed and extended by Claude —
Retrofit/Auditor. Confidence: Analogous.*

The doctrine does not naturally translate into a
single algorithm. It translates into an **algorithm
architecture** — a class of algorithms that emerges
from the Forge's foundational assumptions.

Most systems are optimization systems: they maximize
a known objective. The Forge is a
**continuous model-correction system** whose primary
objective is not producing answers but maintaining the
highest-fidelity representation of reality possible
under uncertainty. That distinction explains why
`Unknowns.md`, `Auditor_Protocols.md`, `Discovery.md`,
and the `Challenges/` directory feel architecturally
coherent — they are all components of the same
error-correcting algorithm.

---

### Foundational Assumptions the Architecture Inherits

The algorithm architecture is downstream of these
doctrinal commitments:

- Knowledge is incomplete
- Models drift
- Unknowns are assets, not failures
- Multiple perspectives are required
- Reality has the final vote
- Salvage is preferable to replacement
- Exploration and Production are different
  operational modes
- Every conclusion carries confidence and assumptions

Each of these maps to a specific algorithmic behavior
described below.

---

### The Forge Meta-Algorithm

The overarching loop that the entire repository
implements:

```
Reality
  ↓
Observation
  ↓
Model
  ↓
Audit
  ↓
Refinement
  ↓
Reality
```

Expanded:

```
Observe
  ↓
Map (Discovery.md, Routing.md)
  ↓
Identify Unknowns (Unknowns.md, sidecar entries)
  ↓
Prioritize Unknowns (Blocking/Critical/Major/Minor)
  ↓
Experiment (Gates, Leviathan, physical tests)
  ↓
Audit (Auditor_Protocols.md, multi-agent cycle)
  ↓
Update Models (Lessons Learned, Spec Gate promotion)
  ↓
Detect Divergence (Drift Indicators, Pending Corrections)
  ↓
Preserve Knowledge (permanent record doctrine)
  ↓
Repeat
```

The loop is already implemented across existing files.
It is not yet formally named anywhere in the repository.
This section names it.

---

### Component Algorithms

**1. Unknown-Driven Search**

Traditional algorithms optimize toward a known
objective. Forge doctrine optimizes toward reduction
of critical unknowns.

Objective function:
```
maximize: useful knowledge gained
          per unit risk and resource expenditure
```

Ranking function for unknowns:
```
priority = f(impact_if_wrong,
             current_uncertainty,
             cost_to_investigate)
```

This is implemented in `Unknowns.md` via the
Priority field (Blocking / Critical / Major / Minor)
and the Expiry Watch. It is a research algorithm,
not a production algorithm — it behaves differently
depending on whether the system is in Exploration
or Specification mode.

**2. Assumption Extraction**

The Auditor's primary function. Given any claim,
decompose it into its prerequisite graph.

```
Input:  claim
Output: directed graph of assumptions,
        each with confidence and expiry trigger
```

Example:
```
Claim: "This gearbox will survive"
  ├── torque estimate correct?     [Analogous]
  ├── material strength correct?   [Placeholder]
  ├── fatigue accounted for?       [No — Unknown]
  ├── thermal effects negligible?  [Assumed]
  └── lubrication available?       [Assumed]
```

The Assumptions section in `Admin/File_Template.md`
formalizes this. The `Admin/Auditor_Protocols.md`
Adversarial Challenge Battery executes it. This
algorithm is already running in every audit cycle.

**3. Confidence Propagation**

The repository stores claims with confidence labels
(Measured / Replicated / Simulated / Analogous /
Placeholder). What does not yet exist is propagation
through the dependency graph.

The rule:
```
if node A depends on node B,
then confidence(A) ≤ confidence(B)
```

A claim cannot be more confident than its least-
confident dependency. The Dependency Map in
`Unknowns.md` is the graph. The confidence labels
are the node weights. Propagation logic is not yet
enforced — it is a future automation target.

Example of current gap: EV-001 is Placeholder.
EC-002 depends on EV-001. EC-002 cannot legitimately
be more confident than Placeholder, but nothing
currently prevents a file from claiming otherwise.

**4. Divergence Detection**

`Discovery.md` treats divergence between doctrine
and implementation as signal, not failure.

```
compare: doctrine (what files say)
compare: implementation (what system does)

if mismatch:
    classify:
        doctrine obsolete?
        implementation drift?
        both?
    log as Pending Correction or Unknown
    do not silently reconcile
```

The algorithm is mining disagreement for information.
The `Admin/Repository_Integrity_Protocol.md` violation
ladder and Drift Indicators implement this.

**5. Salvage Optimization**

The core Gate_02_Triage decision function.

```
score = retained_value - repair_cost - risk_introduced
```

`retained_value` is the hard term. Strategic
Recoverability tiers in Gate_02 are currently
ordinal — they rank options but do not produce
cardinal scores. Turning this into an actual scalar
function is the step from doctrine to deployable
algorithm. This is an open development target.

**6. Adversarial Optimization (Skeptic/Engineer Loop)**

```
Engineer:  generate model
Auditor:   attack model
Engineer:  revise
Auditor:   attack revision
repeat until: convergence OR escalation to human
```

This is the multi-agent audit cycle already running
in practice. It is structurally similar to GAN
training, red-team systems, and formal verification
loops — but focused on engineering reasoning rather
than generative output. The termination condition
is not yet formally defined. Currently the loop
stops when session context runs out. A formal
convergence threshold or gate passage criterion
would complete the algorithm.

**7. Scope Routing**

`Discovery.md` and `Routing.md` implement this.

```
problem or question detected
  ↓
classify domain
  ↓
route to owning file
  ↓
gather output
  ↓
synthesize across domains if cross-module
```

This is a distributed expert system. The Scope
Boundary sections in each file are the routing
filters. An agent loading any file can determine
immediately whether the question belongs here
or elsewhere — without loading every other file.

**8. Challenge-Based Planning**

The `Challenges/` directory inverts the traditional
knowledge organization.

Instead of organizing around what is known, organize
around what must be overcome.

```
challenge identified
  ↓
identify affected domains
  ↓
collect constraints from domain files
  ↓
collect relevant unknowns
  ↓
generate candidate interventions
  ↓
score interventions
  ↓
execute best candidate
  ↓
audit outcome
```

This converts the repository from a knowledge store
into a problem-solving engine. The challenge files
do not freeze solutions — they define obligations
that all downstream domain files must satisfy.

---

### Asymmetric Conservatism

The architecture has a second meta-property beyond
error-correction: it is **asymmetrically conservative**.

The system is much harder to move in the direction
of "this is known and safe" than toward "this is
unknown and risky." Promotion gates, confidence
labels, Blocking flags, the Ethical Anchor, and the
Drift Indicators all create friction in the direction
of false certainty.

This asymmetry is a deliberate design choice. It
maps onto a specific algorithmic class: **anytime
algorithms** — systems that always maintain a valid
conservative answer and only upgrade their answer
when evidence justifies it.

The corollary: a system following Forge doctrine will
tend to understate confidence. That is correct
behavior. Overstatement of confidence is the
primary failure mode this architecture is designed
to prevent.

---

### Epistemic Load Regulation (Triage Doctrine)

*CF-004 sidecar — first logged 2026-06-27.*

The architecture has a third meta-property that
follows from Asymmetric Conservatism: it is
**self-throttling under epistemic load**.

When the rate of Unknown accumulation persistently
exceeds the rate of Unknown resolution, the system
enters a constrained operational posture:

**Triage Posture:**
- Knowledge expansion is deprioritized
- New claims that do not resolve an existing Unknown
  are deferred or blocked
- Agent bandwidth shifts toward verification and
  Unknown resolution
- Promotion gate advancement is suspended until
  load normalizes

The transition trigger is the sign of the debt
derivative, not the absolute debt level. A system
carrying significant accumulated Unknowns but
actively resolving them faster than new ones arrive
remains in normal posture. A system with low
absolute debt but accelerating accumulation enters
Triage Posture early — before the load becomes
unmanageable.

Exit condition: resolution rate exceeds accumulation
rate for a sustained interval. Exit requires
explicit re-verification of posture, not mere
absence of new Unknowns.

This is not a failure state. It is the architecture
functioning as designed — the same asymmetric
conservatism that governs individual claims here
governs system-level operational tempo.

*Dependency: CF-004 (debt measurement mechanism —
see sidecar). The trigger metric now has a formal
definition and stability proof, `Admin/Computational
Institutional Reasoning` §5.4; numeric calibration
is the remaining v1 automation target.*

---

### What Does Not Exist Yet

The architecture is described. The translation layer
is not. Specifically:

- **Confidence propagation enforcement** — nothing
  currently prevents a file from claiming higher
  confidence than its dependencies support
- **Salvage score function** — `retained_value` has
  no formal definition; Gate_02 tiers are ordinal
- **Adversarial loop termination condition** — the
  Skeptic/Engineer cycle has no formal convergence
  criterion
- **Epistemic debt measurement mechanism** — Triage
  Posture doctrine is defined (see above) but the
  trigger metric (Unknown accumulation rate vs.
  resolution rate over a rolling interval) has no
  formal implementation. Currently a human judgment
  call during audit sessions.
- **ML integration** — the Dependency Map, confidence
  labels, and Drift Indicators are structured for
  machine consumption but no translation layer
  exists between document structure and training
  signal

These are development targets, not current gaps
requiring immediate resolution. They belong in
`Admin/Trajectories.md` as v1/v2 automation targets.

---

## Integration Hooks

- `Operations/Electronics.md` — TMR hardware
  implementation; watchdog circuit design (CF-001)
- `Tests/Leviathan_testing.md` — primary stress-test
  environment for all frameworks; confidence collapse
  states are test targets
- `Tests/Support_Raft.md` — Framework F natural
  implementation; Guardian Protocol is Framework G
  prototype; source precedent for the Authority Scope
  Boundary (CF-DS-001 resolution, above) generalized from
  its comms-blackout May/May-Not split
- `Admin/Ethical_Constraints.md` — hard-line doctrines
  govern what no cognition layer may override; CF-DS-002
  resolved here as Bounded Override, full text in that
  file v0.13
- `Admin/Ship_of_Theseus.md` — CF-003 identity
  continuity cross-reference
- `Admin/Auditor_Protocols.md` — multi-agent audit
  cycle is a real-world implementation of the
  Skeptic/Engineer adversarial loop (Section IX);
  Epistemic Load Regulation doctrine mirrors
  EF-0.2 graceful degradation under load
- `Admin/Trajectories.md` — Framework G routes to
  v2/v3; ML integration, confidence propagation
  enforcement, and debt measurement are v1/v2
  automation targets
- `Unknowns.md` — Dependency Map is the confidence
  propagation graph; Expiry Watch implements
  Unknown-Driven Search prioritization
- `Admin/Computational_Institutional_Reasoning.md` —
  formal theoretical grounding for Epistemic Load
  Regulation, Triage Posture, and debt dynamics
  (Theorem 3, Section 5)

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review | Multiple AI models reviewed the same architecture | Models occasionally converged on identical flawed assumptions — apparent consensus on a wrong answer | Consensus without diversity amplifies shared blind spots. TMR requires architectural diversity, not duplication. Three models that share training data share failure modes | Analogous | Yes — CF-002 requires formal correlated failure characterization |
| May 2026 | Audit Review | TMR initially treated as universal redundancy solution | Correlated failures invalidated independence assumptions — three systems failing identically produce false consensus, not detected disagreement | Redundancy requires diversity, not quantity. Independence must be demonstrated through adversarial testing, not assumed from physical separation | Analogous | Yes — first TMR prototype must include correlated failure adversarial testing |
| 2026-06-08 | Audit Review | Algorithm architecture was implicit across multiple files but never formally named | Agents reading individual files could not identify the overarching computational loop. The meta-algorithm was present but invisible | Section IX added — names the Forge Meta-Algorithm and its component algorithms. The loop was already implemented; it needed to be described | Analogous | Yes — validate Section IX against operational behavior when physical systems are running |

---

## Active Disputes

| ID | Dispute | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| CF-DS-001 | Centralized vs. distributed cognition | Single executive AI with advisor sub-systems vs. fleet consensus with no single authority | High | **Resolved — scope-dependent hybrid, 2026-07-26** | `Architecture/Cognitive_Frameworks.md` |
| CF-DS-002 | Human override authority scope | Absolute human override vs. bounded override constrained by Tier 1 Axioms | High | **Resolved — Bounded Override, 2026-07-26** | `Admin/Ethical_Constraints.md` |

**CF-DS-001 resolution (2026-07-26):** Neither named
position as stated — Frameworks E and F are not in
competition; they apply at different decision scales,
per the Authority Scope Boundary added to Section III
above. This generalizes `Tests/Support_Raft.md`'s
existing comms-blackout May/May-Not split rather than
inventing new doctrine, and was independently confirmed
by both Claude and Grok before closing. No advisor or
supervisory layer gains unilateral command authority —
Q-2 (Separation of Powers) continues to apply to that
layer exactly as to any other agent.

**CF-DS-002 resolution (2026-07-26):** Ratified directly by human governing authority — hard floors (Anti-Weaponization, Life Preservation, Cultural Sites, per `Admin/Ethical_Constraints.md`) sit above the human governing authority's own direct, real-time order, not only above subordinate agents. Revision requires the deliberate constitutional process any Tier 1 document requires, not an in-the-moment override. Framed by the human principal as a moral commitment, not a technical default: "These hard floors should sit above my own authority. They are a moral imperative." `Admin/Ethical_Constraints.md` v0.13 carries the full doctrine text and the accompanying tool/weapon distinction ratified in the same decision. EC-011 (authenticating that a claimed override genuinely originates from the human principal, as opposed to what the floor binds) remains a separate, still-open unknown in that file — unaffected by this closure.

---

## Auditor Notes & Unknowns

### CF-001 — Hardware watchdog minimum standard undefined

| Field         | Value                                                        |
|---------------|--------------------------------------------------------------|
| Status        | Open                                                         |
| Risk          | High                                                         |
| Priority      | Critical                                                     |
| Type          | Technical                                                    |
| Blocking      | Yes — no Specification-level autonomous architecture may be approved without a defined watchdog minimum standard |
| Owner         | Operations/Electronics.md                                    |
| First Logged  | 2026-05-09                                                   |
| Last Reviewed | 2026-05-09                                                   |

**Description:** Minimum required watchdog behaviors
and enforcement mechanisms for autonomous Forge
systems are undefined. Without a defined hard-safe
layer, higher cognition frameworks cannot guarantee
containment during failure.

**Why It Matters:** The hardware watchdog is Layer 1
in the Cognitive Reliability Stack — the last
software-adjacent constraint before mechanical truth
(Layer 0). If Layer 1 is undefined, the gap between
Layer 0 and Layer 2 is uncontrolled. Any
Specification-level autonomous architecture approved
without a defined watchdog minimum rests on an
unverified safety assumption.

**Resolution Path:** Define mandatory watchdog
behaviors (heartbeat interval, timeout action,
neutral-state enforcement, tamper detection) before
any Specification-level autonomous architecture is
approved. Owner is `Operations/Electronics.md` —
watchdog circuit design belongs in the electronics
hardware layer. This file owns the minimum behavior
requirements; Electronics.md owns the implementation.
Payment via Specification — once Electronics.md
defines and validates a watchdog implementation,
update Layer 1 in Section II with concrete parameters.

---

### CF-002 — Correlated AI failure modes insufficiently modeled

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Architecture/Cognitive_Frameworks.md             |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-06-08                                       |

**Description:** How to detect and mitigate
synchronized reasoning failures across AI agents
that share training assumptions, architecture, or
data sources. Apparent consensus may produce false
confidence rather than genuine agreement.

**Why It Matters:** The multi-agent audit cycle —
the primary mechanism for error detection in the
repository — assumes that different AI models provide
independent perspectives. If models share training
data lineage or reasoning patterns on forge-relevant
engineering questions, the consensus they reach may
amplify shared blind spots rather than cancel
independent errors. The Skeptic/Engineer loop is
only as good as the diversity of the adversarial
perspectives it draws on.

**Resolution Path:** Develop diversity scoring
metrics and adversarial disagreement testing
frameworks. Add to `Tests/Leviathan_testing.md` as
a primary test target — the multi-unit swarm is
the natural environment for correlated failure
detection. Cross-reference `Operations/Electronics.md`
EL-007 (correlated TMR failure modes) — the hardware
and AI versions of this problem are structurally
identical. Payment via Specification — once first
multi-unit swarm test data characterizes actual
reasoning overlap, update Section IX confidence
propagation and Section III Framework D diversity
requirements.

---

### CF-003 — Identity continuity during split-brain, doctrine defined pending empirical validation

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Architecture/Cognitive_Frameworks.md             |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-07-26                                       |

**Description:** When a fragmented or partially
restored cognition system is considered the "same"
entity for purposes of authority continuity, memory
trust, and restoration policy.

**Why It Matters:** A Leviathan unit that suffers
split-brain, partially restores from cache, and
re-enters operation has an identity continuity
problem: which memories are trusted, which authority
grants are still valid, and whether the restored
unit should be treated as the same agent or a new
one. Without a doctrine, restoration decisions are
made ad hoc — which creates inconsistent authority
chains and potential security gaps.

**Resolution Path:** This entry was stale — it
described the gap as if no doctrine existed, when
`Admin/Ship_of_Theseus.md` §IV (AI Identity
Continuity Doctrine) already defines Canonical vs.
Derivative Identity, the 30% Derivative Threshold,
and the re-vetting path (added 2026-06-08). That
file's own ST-003 sidecar entry lists updating this
entry to reference §IV as one of its three closure
conditions — this update satisfies that condition.
Status set to In Progress, mirroring ST-003 exactly,
rather than Resolved: the 30% threshold is still
Analogous confidence, uncalibrated against real
split-brain recovery data, and ST-004 (sub-threshold
state-tampering against that same threshold) is a
separate open adversarial surface. Moves to Resolved
alongside ST-003, when the threshold is empirically
validated and the re-vetting path trial duration is
defined from operational deployment.

---

### CF-004 — Epistemic debt measurement mechanism undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Major                                            |
| Type          | Architectural / Automation                       |
| Blocking      | No                                               |
| Owner         | Architecture/Cognitive_Frameworks.md             |
| First Logged  | 2026-06-27                                       |
| Last Reviewed | 2026-07-28                                       |

**Description:** Epistemic Load Regulation (Triage
Posture) is defined as doctrine in Section IX. The
trigger metric — Unknown accumulation rate vs.
resolution rate over a rolling interval — previously
had no formal implementation. As of 2026-07-28,
verified: `Admin/Computational Institutional
Reasoning` §5.4 (The Automated Triage Posture
Trigger) formally defines this exact metric — a
rolling average of the debt derivative $dD_e/dt$
over $N$ audit cycles against a calibrated ceiling
$\varepsilon_{\text{triage}}$ — and proves it stable
under a Lyapunov argument (§5.4 Theorem 3). The
mathematical form and stability guarantee are no
longer missing. What remains open: numeric
calibration of $\theta_p$, $\varepsilon_{\text{triage}}$,
$\varepsilon_{\text{exit}}$, and $N$. Until calibrated,
Triage Posture entry and exit remain human judgment
calls during audit sessions — the check now has a
formal target to be checked against, but the check
itself is not yet automated.

**Why It Matters:** Without calibrated values, Triage
Posture still cannot be enforced automatically or
audited consistently — the instrument now has a
proven-stable design but no dial settings. Priority
raised from Minor to Major 2026-07-26: Section IV
(Confidence Collapse States) has now been revised
(2026-07-28) to formally reference this same debt
derivative for its Yellow→Orange transition, per the
CF-004/CIR §5.4 connection flagged during a prior
audit pass and confirmed in this one. That widens the
dependency surface further — Section IV, Triage
Posture, and promotion suspension now all cite the
same uncalibrated metric. The risk profile keeps
growing even as the underlying formal gap has
narrowed.

**Resolution Path:** Calibrate $\theta_p$,
$\varepsilon_{\text{triage}}$, $\varepsilon_{\text{exit}}$,
and $N$ against at least two audit cycles of real
`Unknowns.md` history — candidate location for
implementation remains `Automation/AUDIT_HARNESS.py`,
which already reads `Unknowns.md` and could emit the
debt derivative alongside Phase 1 output. Once
calibrated and validated, update Section IX Triage
Posture and Section IV's Orange-state trigger with
the concrete threshold values, replacing the symbolic
form with numbers.

---

### CF-005 — Adversarial audit loop convergence criteria undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural / Automation                       |
| Blocking      | No                                               |
| Owner         | Admin/Auditor_Protocols.md / Automation/AUDIT_HARNESS.py |
| First Logged  | 2026-07-26                                       |
| Last Reviewed | 2026-07-26                                       |

**Description:** Section IX's Adversarial Optimization
(Skeptic/Engineer Loop) already states in body text that
the loop "stops when session context runs out" rather
than on a formal convergence threshold or gate-passage
criterion, and lists this same gap under "What Does Not
Exist Yet" as the Adversarial loop termination condition.
Neither location had a corresponding sidecar entry — a
gap named in body text without a tracked unknown behind
it, same failure mode this file's own Drift Indicators
guard against elsewhere.

**Why It Matters:** Without a tracked unknown, this gap
has no expiry watch, no resolution path ownership, and no
visibility in Unknowns.md's cross-module index — it could
sit indefinitely as a body-text aside rather than
something anyone is accountable for closing.

**Resolution Path:** Define a formal termination
condition for the multi-agent audit cycle — a convergence
threshold, gate-passage criterion, or explicit escalation
trigger — as an extension of `Admin/Auditor_Protocols.md`'s
existing audit-phase doctrine, computable from
`Automation/AUDIT_HARNESS.py`'s existing session data
where practical.

*Surfaced by Gemini — Skeptic/Auditor, 2026-07-26; verified
against source and registered by Claude —
Synthesizer/Auditor, human-directed.*

---

### Resolution Log

- 2026-07-28: Section IV (Confidence Collapse States)
  revised — Yellow→Orange transition now formally
  defined via `Admin/Computational Institutional
  Reasoning` §5.4's debt derivative trigger
  ($dD_e/dt$ rolling average vs. $\varepsilon_{\text{triage}}$),
  Lyapunov-proven stable per that section's Theorem 3.
  Green/Yellow/Orange mapped to CIR §5.3's Stability
  Regimes; Red mapped to the Collapse Region (requires
  sustained positive second derivative, not merely
  elevated debt); Black remains direct-detection,
  unchanged. Numeric calibration ($\theta_p$,
  $\varepsilon_{\text{triage}}$, $\varepsilon_{\text{exit}}$,
  $N$) remains open — CF-004 updated to reflect this
  narrowed scope (formal implementation resolved,
  calibration pending). Section IX's Confidence
  Propagation rule checked for consistency per this
  file's own Drift Indicator — found orthogonal
  (per-claim label confidence vs. system-level debt
  state); no change required there. Epistemic Load
  Regulation's CF-004 dependency note updated to
  match. Prior status ("proposed revision... under
  review, not yet adopted," referenced in CF-004's
  own text) is now superseded — the revision has
  landed. Verified and drafted by Claude —
  Synthesizer/Auditor, human-directed.

- 2026-06-08: Navigation Anchors added. File State
  expanded to full table format. Assumptions section
  added. Section IX (Algorithm Architecture) added —
  incorporates ChatGPT Synthesizer analysis
  (2026-06-08), extended with Asymmetric Conservatism
  property and development targets. Lessons Learned
  expanded to full template format. Sidecar entries
  expanded to full field tables. Integration Hooks
  updated — stale filenames corrected.
  Active Disputes table expanded with Owner field
  and CF-DS-002 constitutional note. Guiding Axioms
  extended with two additions from doctrinal review.
- 2026-06-27: Section IX extended — Epistemic Load
  Regulation (Triage Doctrine) added as third
  meta-property following Asymmetric Conservatism.
  "What Does Not Exist Yet" updated — epistemic debt
  measurement mechanism added as fourth development
  target. CF-004 logged (debt measurement mechanism
  undefined — Low risk, Minor priority, v1 automation
  target). Scope Boundary updated — Triage Posture
  added to DOES define; CF-004 exclusion added to
  DOES NOT define. Integration Hooks updated —
  Auditor_Protocols.md EF-0.2 connection noted;
  Computational Institutional Reasoning cross-reference
  added. Open Unknowns 3 → 4. Last Audit date updated.
- 2026-07-26: Gemini Skeptic/Auditor Exploration audit
  reviewed and cross-checked against source. Two findings
  confirmed and fixed: Assumptions table's High/Medium/Low
  confidence labels (Semantic Drift from canonical Truth
  Provenance terminology) remapped to the five-label
  Evidence Classification — four assumptions to Analogous,
  ASM-003 to Placeholder given its own expiry trigger
  already states diversity "must be demonstrated, not
  assumed." CF-005 registered (adversarial audit loop
  convergence criteria — named in Section IX body text and
  in "What Does Not Exist Yet," but had no sidecar entry).
  One finding from the same audit rejected after
  verification: Gate G5 was reported BLOCKED on grounds
  that `Admin/Computational_Institutional_Reasoning.md` is a
  hallucinated/non-existent path. It is not — the file
  exists on disk, is registered in `Routing.md`, and is
  documented there as one of two files that resolve via
  hardcoded `ALIASES` in `Automation/AUDIT_HARNESS.py`
  rather than the dynamic `parse_routing()` registry. G5 is
  clear; CF-001 remains the sole legitimate promotion
  blocker. Verified by Claude — Synthesizer/Auditor,
  human-directed.
- 2026-07-26 (second entry, same day): Two further fixes
  from a multi-agent confidence-algebra discussion
  (ChatGPT, Gemini), both verified against source before
  adoption. CF-004 priority raised Minor → Major — multiple
  agents independently identified that Triage Posture,
  promotion suspension, and a proposed (not yet adopted)
  Section IV revision all depend on this metric, so its
  risk profile changed even though the gap itself didn't.
  CF-003 status and Resolution Path synced with
  `Admin/Ship_of_Theseus.md` — that file's §IV already
  defines the Canonical/Derivative Identity doctrine this
  entry described as nonexistent; its own ST-003 sidecar
  entry explicitly lists updating CF-003 as one of its three
  closure conditions, now satisfied. Status set to In
  Progress, mirroring ST-003, not Resolved — the 30%
  threshold remains uncalibrated. A third, larger proposal
  from the same discussion (a new "confidence algebra" with
  AND/OR/Conflict operators, and a full Section IV rewrite
  built on it) was not adopted this pass — see the note
  addressed to the human principal for why.
- 2026-07-26 (third entry, same day): **CF-DS-002 resolved
  — Bounded Override**, ratified directly by human governing
  authority after escalation, as this file's own Active
  Disputes entry required. Hard floors in
  `Admin/Ethical_Constraints.md` (Anti-Weaponization, Life
  Preservation, Cultural Sites) sit above the human governing
  authority's own direct order, not only above subordinate
  agents — framed by the human principal as moral commitment,
  not technical default. Full doctrine text, the accompanying
  tool/weapon distinction, and the override-scope closure live
  in `Admin/Ethical_Constraints.md` v0.13; this file records
  only the closure. Active Disputes 2 → 1. CF-DS-001
  (centralized vs. distributed cognition) remains Open — no
  constitutional escalation requirement, ours to work directly.
- 2026-07-26 (fourth entry, same day): **CF-DS-001
  resolved — scope-dependent hybrid**, not a win for
  either named extreme. New subsection "Authority Scope
  Boundary" added after the Framework Taxonomy (Section
  III): a decision stays at local unit autonomy only if
  scope-confined, reversible/fail-safe, time-critical,
  and confidence state is Green/Yellow; it routes through
  the supervisory/advisory layer if any of swarm-wide
  effect, an Ethical_Constraints boundary, irreversibility
  without urgency, or Orange+ confidence state hold.
  Directly generalizes `Tests/Support_Raft.md`'s existing
  comms-blackout May/May-Not split to the general case
  rather than inventing new doctrine — that file's
  boundary was already correct, just scoped to blackout
  only. Explicit clarification that "supervisory" means
  challenge/dissent authority, not command authority — no
  advisor may plan, execute, and self-authorize the same
  action, per Q-2. Independently confirmed by Claude and
  Grok before closing. Active Disputes 1 → 0.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| May 2026 | Pure consensus guarantees correctness | Consensus can fail through shared blind spots and correlated assumptions — three systems agreeing on a wrong answer produces false certainty | No — diversity requirement is permanent doctrine |
| May 2026 | Single perfect supervisory AI | Violates Forge degraded-environment assumptions; creates catastrophic single-point failure in the cognitive layer | No — distributed architecture with diversity is permanent |
| 2026-06-08 | Implicit algorithm architecture | The Meta-Algorithm and component algorithms were present in the doctrine but unnamed. Leaving them implicit prevented agents from understanding what the system is computing | No — Section IX names them explicitly; implicit status abandoned permanently |

---

## Drift Indicators

Mandatory re-audit conditions for this document.
All canonical triggers from `Admin/File_Template.md`
apply. The following are additional local triggers:

| Trigger | Reason |
|---------|--------|
| TMR diversity requirement weakened or removed | Correlated failure risk — consensus on wrong answer is worse than no consensus |
| Confidence Collapse States revised without updating Confidence Propagation rules in Section IX | The two systems must remain consistent — collapse state thresholds and confidence ceilings interact |
| Layer 0 (mechanical truth) demoted below any software layer | Mechanical truth outranks software confidence is permanent doctrine |
| Section IX algorithm descriptions revised without cross-validating against `Unknowns.md` Dependency Map | The Dependency Map is the confidence propagation graph — structural changes must stay synchronized |
| CF-DS-002 resolved without escalation to human governing party | Constitutional implications — human ratification required before closing |
| Salvage score function defined without cross-validation against `Operations/Gate_02_Triage.md` Strategic Recoverability tiers | Score function must extend, not contradict, existing triage doctrine |
| Human override authority reduced below Layer 6 without Tier 1 Axiom amendment procedure | Governance_Migration_Protocol.md Track B — constitutional amendment required |
| Triage Posture entry/exit criteria hardcoded without CF-004 resolution | Trigger metric must be derived from operational data, not specified in advance |
| Epistemic Load Regulation doctrine modified without updating CF-004 status | Doctrine and instrument must evolve together |

**Compound Drift Rule:** If multiple indicators
activate simultaneously, halt autonomous audit
progression and escalate for human review.
