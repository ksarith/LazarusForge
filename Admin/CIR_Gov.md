# CIR_Gov.md — Computational Institutional Reasoning v2.0

*Admin/CIR_Gov.md*

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## Operational Safety Advisory

None. This is a governance/epistemics document with no physical hazard surface.

---

## File State

| Field | Value |
|-------|-------|
| Status | **Proposed — Not Ratified** |
| Body Stability | Volatile |
| Spec Gates | 0/6 |
| Verification Ref | `Admin/Verification_Gates.md` |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Highest Risk | High — while unratified and GOV-008 remains Open, the misreading risk (treating this as operational) is real, not theoretical; raised from Medium 2026-07-31 per Skeptic/Auditor review. See §Binding Status below. |
| Last Audit | 2026-07-31 |
| Auditor | Grok — drafted CIR v2.0 architecture (Parts 0–8) and Nothingness-bridge/naming recommendations; Claude — Synthesizer, verified cross-references against `Governance_Charter.md`, `Nothingness_Theorem.md`, and `Unknowns.md` GOV-008 status before filing; human-directed, 2026-07-31; Grok — Skeptic/Auditor pass on this file (same-session as original drafting — human noted this is a "cognitive purity" limitation, a fresh instance would have been preferable and is a lesson for future review cycles), produced candidate Checkpoint mapping and f(n)/s(n) definitions; Claude — Synthesizer, independently verified all six Checkpoint names/numbers and the Checkpoint 2/4 gap characterization against `Governance_Charter.md` source before integrating (not just accepting the same-session review's claims), human-directed, 2026-07-31 |
| Open Unknowns | 1 (CIR-GOV-001 — predicate/Checkpoint mapping, candidate table now supplied; two genuine gaps documented at Checkpoints 2 and 4. Separately, this file's Binding Status also depends on GOV-008, but GOV-008 itself is tracked and owned by `Governance_Charter.md`, not counted here.) |
| Active Disputes | 0 |
| Sidecar Link | #resolution-log |

---

## Scope Boundary

**This file owns:** a formal, algebra-based specification for an epistemic state-transition kernel — predicate-gated admissibility, typed unknowns with debt accounting, provenance ceilings, and a deterministic triage posture — intended as a future implementation layer *under* `Admin/Governance_Charter.md`'s constitutional authority.

**This file does not own and must never claim:**
- Constitutional authority. `Governance_Charter.md`'s Tier-1 Axioms (P-1–P-4, Q-1–Q-4) remain supreme; nothing here amends, overrides, or reinterprets them.
- Satisfaction of Axiom Q-2 (Separation of Powers) or GOV-008 (minimum agent/hardware quorum). See §Binding Status.
- Runtime execution. No harness, evaluator, or automation in this repository currently implements any part of this document. It is specification only.
- Genesis Phase exit. Adopting this document does not clear Enforcement Checkpoint 2 or resolve the Bootstrap Paradox.

---

## File Purpose

CIR v2.0 is a candidate epistemic governance kernel for LazarusForge — a machine-checkable way to gate proposed state mutations through predicate logic rather than narrative judgment alone. It elevates predicates (`Γ`) to the primary admissibility mechanism, separates epistemic quality (`Q`) from admissibility (`A_adm`), treats provenance as a hard ceiling rather than a soft score, gives unknowns explicit weighted-graph semantics with debt accounting, and defines a deterministic state-transition kernel (`σ`) with a graded, debt-bounded triage posture.

It is preserved here in full, as drafted, because the ideology and architecture are sound and worth keeping intact even though it cannot yet be adopted as operational doctrine. See §Binding Status for exactly why, and §Relationship to Governance_Charter.md for how it is meant to eventually connect.

---

## Binding Status — Read This Before Anything Else in This Document

**CIR v2.0 is not currently operational, and its central structural claim is not currently true of this repository.**

The kernel's core promise is *agent-independent state transitions* — Part 0.1, Principle 7: "Agent identity cannot influence admissibility." Part 1, Axiom A4 states the same thing. This is meant to structurally implement `Governance_Charter.md` Axiom Q-2 (Separation of Powers): *"No single agent, model, or subsystem may possess the combined authority to plan, execute, and self-authorize the same action."*

That promise depends entirely on a real, ratified multi-agent quorum existing to evaluate the `Γ` predicates independently of whichever agent proposed a given state mutation. **That quorum does not exist.** `GOV-008` (Minimum hardware and agent quorum for bootstrap compliance, owned by `Governance_Charter.md`) is confirmed, as of 2026-07-31, to be an **Open** unknown with no agent-class taxonomy, no minimum counts, no diversity criteria, and no hardware requirements defined anywhere in the repository. Enforcement Checkpoint 2 (Structural Plausibility) remains **BLOCKED — Bootstrap Paradox** for exactly this reason.

If this kernel were switched on today, the entity evaluating `γ_grounding`, `γ_provenance`, `γ_conflict`, `γ_unknown`, and `γ_challenge` on a proposed mutation would, in the overwhelming majority of real sessions, be the same single agent that proposed the mutation. That is not the Separation of Powers this document describes — it is the exact Bootstrap Paradox `Governance_Charter.md` already named, acknowledged, and fenced off with the Genesis Phase Protocol. Running CIR v2.0's kernel under those conditions would not implement Q-2; it would produce the appearance of predicate-gated rigor while the actual gate was a single agent auditing itself.

**This is why the file is filed as Proposed — Not Ratified rather than adopted.** The architecture is worth preserving exactly as designed. It should not be read, cited, or built against as if it already governs anything.

**Sequencing implication:** `GOV-008` should be drafted and ratified first, as pure Charter-layer work independent of this document. Only once a real quorum exists does adopting CIR v2.0's kernel become more than a specification — at that point Principle 7 / Axiom A4 become true statements about the system rather than aspirational ones, and Part 8's runtime evaluator becomes something that could actually be implemented against a real multi-agent audit harness.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expires When |
|----|-----------|-------|------------|---------------|
| ASM-CIR-001 | A deterministic predicate kernel is a good target architecture for LazarusForge's eventual governance automation | Aligns with existing Verification Gates (G1–G6), Auditor Protocols' Adversarial Battery, and the repo's general preference for falsifiable, evidence-graded doctrine over narrative judgment | Medium — Analogous to existing gate structures, not yet tested as a unified kernel | A working reference implementation is built and run against real state mutations |
| ASM-CIR-002 | The five `Γ` predicates (grounding, provenance, conflict, unknown, challenge) are a complete and non-redundant set for constitutional-class admissibility decisions | Internal design choice by the drafting agent; not independently derived from `Governance_Charter.md`'s own six Enforcement Checkpoints | **Low, and understated by "confidence" framing alone** — the candidate mapping (§Predicate ↔ Checkpoint Mapping) confirms this is an open design-completeness risk, not just an unverified assumption: Checkpoints 2 (Structural Plausibility) and 4 (Cross-Module Integration) have **no** corresponding predicate at all | Either new predicates are added for Checkpoints 2 and 4, or those Checkpoints are explicitly declared out of CIR's runtime scope and left to the Charter/Auditor layer |
| ASM-CIR-003 | GOV-008, once ratified, will produce a quorum shape compatible with what CIR's Part 8 runtime evaluator assumes (independently reachable, responsive agent instances capable of predicate evaluation) | Speculative — GOV-008 is currently unratified; its eventual concrete form is unknown | Low | GOV-008 is ratified and its quorum definition is checked against CIR's runtime assumptions |

---

## Body

### PART 0 — Constitutional Architecture

#### 0.1 Constitutional Principles (Immutable Within This Document's Own Frame)

These principles are immutable *within CIR v2.0 itself* — i.e., changing them would mean drafting a different kernel, not amending this one. They are **not** constitutionally immutable for LazarusForge as a whole; that authority remains solely with `Governance_Charter.md`'s Tier-1 Axioms until and unless this document is ratified and placed under that authority per §Relationship to Governance_Charter.md.

1. **Predicate supremacy** — All institutional decisions are gated by constitutional predicates.
2. **External grounding** — Reality enters only through authenticated grounding interfaces.
3. **Typed unknowns** — All representational deficits must be structurally represented.
4. **Provenance ceilings** — Provenance determines admissibility ceilings, not evidence.
5. **Contradiction zeroing** — Contradictions collapse admissibility categorically.
6. **Debt-bounded evolution** — Epistemic debt must remain below a constitutional threshold.
7. **Agent-independent state transitions** — Agent identity cannot influence admissibility. *(See §Binding Status — not currently true of this repository.)*
8. **Deterministic state machine** — All transitions follow a deterministic constitutional kernel.

#### 0.2 Implementation Parameters (Tunable)

These may be adjusted via build configuration or automated calibration without violating the principles above, once this document carries operational authority.

- `ε` — coordinate floor
- `W` — weight vector for geometric maturity
- `Ψ_class` — provenance ceilings by class
- `θ_p` — promotion threshold
- `Δ_max` — triage debt threshold
- `d(n)` — dependency weights
- challenge difficulty / decay scales
- grounding interface sampling rates / frequencies

---

### PART 1 — Epistemic Substrate Axioms (A1–A5)

**A1 — External Grounding via Formal Interfaces**
Reality enters the institution only through authenticated grounding interfaces. No other epistemic channel is admissible.

**A2 — Finite Representation and Typed Unknowns**
All representational deficits must be expressed as typed unknown nodes `v_u` with explicit lifecycle and directed edges.

**A3 — Explicit Epistemic Accounting**
Unknowns must influence maturity, debt, and predicate evaluation.

**A4 — Agent-Independent State, Agent-Dependent Provenance**
Agent identity cannot influence admissibility. Agent reputation may influence provenance confidence `P(n)` only as bounded metadata. *(See §Binding Status.)*

**A5 — Predicate-Ordered Governance Precedence**
All state transitions must satisfy all constitutional predicates. UNKNOWN STATE is a predicate failure.

**A6 — Non-Zero Representational Floor (Nothingness Bridge)**
No admissible institutional state may claim or implement absolute representational zero. Every node carries `E(n) ≥ ε > 0`.

*Provenance of A6:* this axiom is a deliberately minimal, non-bloating import from `Admin/Nothingness_Theorem.md` — specifically its Core Theorem: *"Pure absence cannot be thought about without ceasing to be pure absence — the act of conceiving 'nothing' initializes it as a concept, granting it E > 0 and collapsing the zero state permanently."* Only this positivity principle is imported, not the full theorem. It justifies the strict positivity of the Coordinate Floor Constraint (§2.1) and the maturity/debt functions below — preventing division-by-zero pathologies and "optimize unknowns to zero" attacks, where a state mutation tries to claim complete certainty by definitional fiat rather than by satisfying the grounding and provenance gates. `Nothingness_Theorem.md` itself remains Tier 0, functionless by its own doctrine, and unaffected by this reference — this is the same kind of operationalization relationship it already has with `Computational_Institutional_Reasoning.md`'s Axiom A3 and Rule γ2, not a new precedent.

**Corollary (Unknown Conservation), 2026-07-31:** For any admissible institutional state, the measure of unresolved typed unknowns is bounded away from zero. Absolute representational closure is not a reachable state. This is the formal link A6 provides to `Unknowns.md`'s own Unknown Budget rule — the Charter-layer doctrine that an honest non-empty unknown index is a design goal, not a defect to be optimized away. Neither document requires the other to hold; they independently arrive at the same structural conclusion via different reasoning (A6 via the Nothingness Theorem's positivity argument, `Unknowns.md` via operational audit discipline).

---

### PART 2 — Verification Algebra

#### 2.1 Verification State Vector

```
V(n) = [E(n), R(n), C(n), P(n), S(n)]ᵀ
```

- `E` — Evidence completeness
- `R` — Reproducibility
- `C` — Cross-domain consistency
- `P` — Provenance confidence
- `S` — Physical grounding

**Coordinate Floor Constraint**

```
vᵢ ∈ [ε, 1],  ε ∈ (0, e_min)
```

#### 2.2 Unknown-Edge Semantics

Let `u(n)` be the number of unknown edges.

```
U(n) = 1 / (1 + u(n))
```

Unknowns also propagate epistemic debt:

```
δ(n) = d(n) · max(0, θ_p − M(n))
```

#### 2.3 Categorical Gates

**Physical Grounding Gate**

```
Φ(n) = 0  if n ∈ V_phys and S(n) = ε
     = 1  otherwise
```

**Provenance Ceiling Gate**

```
Ψ(n) = Ψ_class(n)
```

*Clarification:* `Ψ` is an **upper bound**, not a target. A node's provenance class caps how much maturity it may claim (`M(n) ≤ Ψ(n)`); it is not a score to be maximized. Higher provenance confidence `P(n)` does not raise the ceiling itself — it can only help a node approach the ceiling its class already permits. Conflating "higher provenance" with "higher ceiling" inverts the gate's purpose.

**Contradiction Gate**

```
Ξ(n) = 0  if c(n) > 0
     = 1  if c(n) = 0
```

**Adversarial Challenge Gate**

```
A(n) = [f(n) / (f(n)+1)] · [1 / (1+s(n))]
```

*See §2.3.1 immediately below for definitions of `f(n)` and `s(n)` — this gate is otherwise under-specified.*

##### 2.3.1 Adversarial Challenge Parameters

These two quantities complete the Adversarial Challenge Gate.

**`f(n)` — Challenge Frequency / Exposure Count**

`f(n) ∈ ℕ₀` — the number of distinct, recorded adversarial challenges raised against node `n` within the current audit window.

- Incremented each time an independent skeptic, auditor, or adversarial battery produces a non-trivial challenge logged against `n`. "Non-trivial" means the challenge introduces new critical pressure or a new attack angle — not a restatement of an already-open unknown or already-recorded contradiction.
- Decays according to the statutory challenge-decay scale (§0.2) so ancient challenges don't permanently inflate confidence.
- `f(n) = 0` means the node has never been adversarially tested in the current window.
- Interpretation: `f(n)/(f(n)+1)` is a soft saturation function. At `f=0` the factor is 0 — no adversarial exposure means the gate contribution collapses. As `f` grows the factor approaches 1 — repeated exposure and survival raises confidence.

**`s(n)` — Active Sinking / Unresolved Challenge Load**

`s(n) ∈ ℕ₀` — the number of currently open, unresolved adversarial challenges still actively "sinking" the node — raised but not yet answered, withdrawn, or converted into a typed unknown or contradiction.

- `s(n) > 0` means at least one live challenge remains unanswered.
- `s(n) = 0` means every previously raised challenge has been closed (answered, absorbed as an unknown, or shown invalid).
- A challenge moves from `f` (historical exposure) into `s` (active load) when first logged, and stays in `s` until dispositioned.
- Interpretation: `1/(1+s(n))` is a hard penalty. Any open challenge strictly reduces the gate value; only `s(n)=0` gives a factor of 1.

**Combined behavior:** a node never challenged fails the gate (no exposure to prove robustness against); a node challenged and fully resolved passes, with strength increasing as `f` grows; any node with an open, unresolved challenge fails regardless of past success — adversarial robustness is a live property, not a permanent credential.

**Conversion rule:** an open challenge resolves into either a typed unknown (moves the pressure into `U(n)`/debt accounting) or a logged contradiction (`c(n)`) — it does not simply vanish. This keeps the challenge mechanism from being gamed by declaring a challenge "closed" without it landing somewhere else in the algebra.

Suggested statutory defaults (§0.2, pending calibration): challenge window length of 1 full audit cycle; linear or exponential decay rate for `f`; minimum non-trivial threshold defined by `Auditor_Protocols.md`'s adversarial battery.

#### 2.4 Epistemic Quality vs Admissibility

**Epistemic Quality**

```
Q(n) = exp(Wᵀ · ln V(n)) · U(n)
```

**Admissibility**

```
A_adm(n) = Φ(n) · Ψ(n) · Ξ(n) · A(n)
```

**Full Maturity**

```
M(n) = A_adm(n) · Q(n)
```

---

### PART 3 — Predicate Layer (Primary Governance Mechanism)

```
Γ = { γ_grounding, γ_provenance, γ_conflict, γ_unknown, γ_challenge }
```

**Predicate Definitions**

```
γ_grounding(n)  = 1 if Φ(n) = 1,  else 0
γ_provenance(n) = 1 if M(n) ≤ Ψ(n),  else 0
γ_conflict(n)   = 1 if c(n) = 0,  else 0
γ_unknown(n)    = 1 if E(n) ≥ e_min and R(n) ≠ undefined,  else 0
γ_challenge(n)  = 1 if s(n) = 0,  else 0   (see §2.3.1 for definitions of f(n), s(n))
```

---

### PART 4 — Verification Classification Matrix

- **UNKNOWN STATE** — `E(n) < e_min ∨ R(n) = undefined ⟹ γ_unknown(n) = 0`
- **CONFLICT STATE** — `c(n) > 0 ⟹ γ_conflict(n) = 0`
- **PROVENANCE CEILING STATE** — `M(n) > Ψ(n) ⟹ γ_provenance(n) = 0`
- **UNGROUNDED PHYSICAL CLAIM** — `n ∈ V_phys, S(n) = ε ⟹ γ_grounding(n) = 0`
- **VERIFIED STATE** — `∀γ ∈ Γ: γ(n) = 1`

---

### PART 5 — Institutional State-Transition System

#### 5.1 Institutional State

```
I_t = (G_t, Δ_e, Γ, Θ)
```

#### 5.2 Transition Kernel

```
σ(I_t, ΔI) = I_{t+1}  if ∀γ ∈ Γ: γ(ΔI) = 1
           = I_t      otherwise
```

This is the constitutional core of CIR v2.0 — and the component most directly gated by §Binding Status. `σ` is only "deterministic and agent-independent" in the sense the document claims once the `Γ` predicates are actually evaluated by an independent quorum rather than by the proposing agent.

---

### PART 6 — Triage Posture (Debt-Bounded Stabilization)

#### 6.1 Debt Definition

```
δ(n) = d(n) · max(0, θ_p − M(n))
Δ_e  = Σₙ δ(n)
```

#### 6.2 Triage Activation

Triage triggers if any predicate fails, **or**

```
Δ_e > Δ_max
```

#### 6.3 Triage Actions

- HALT_GENERATION
- SATURATE_VERIFICATION
- LINEAGE_RECONSTRUCTION
- CEILING_ENFORCEMENT
- GROUNDING_REVALIDATION
- CONTRADICTION_RESOLUTION
- UNKNOWN_REDUCTION
- DEBT_RECOMPUTATION

#### 6.4 Exit Conditions

```
∀γ ∈ Γ: γ(n) = 1   and   Δ_e ≤ Δ_max
```

#### 6.5 Debt Aging / Resolution Credit

As originally specified, `δ(n)` only accumulates — nothing in Parts 6.1–6.4 reduces debt when the underlying unknown that caused it is actually resolved. In a long-lived institutional graph this produces **permanent triage lock-in**: a node that earned debt from a since-resolved unknown stays debt-burdened indefinitely, and `Δ_e` only ever grows toward `Δ_max`, never away from it.

**Rule:** when a typed unknown contributing to `δ(n)` is formally resolved (Payment via Specification, Trajectory discharge, Vehicle assignment, or equivalent per this repository's Resolution Taxonomy), recompute `δ(n)` against the node's current `M(n)` rather than treating the debt as a permanent historical charge:

```
δ(n) ← d(n) · max(0, θ_p − M(n))   [recomputed, not accumulated]
```

This is DEBT_RECOMPUTATION (§6.3) applied as a standing rule after any unknown resolution affecting `n`, not only as a triage-invoked action. Debt is a *current state* function of `M(n)`, not a ledger of historical failures — an unknown that is genuinely resolved must be able to lower `Δ_e`, or the triage posture becomes a one-way ratchet that eventually halts generation on nodes that are actually fine now.

---

### PART 7 — Constitutional Guarantees (Aspirational Pending §Binding Status)

CIR v2.0, once actually operational under a ratified GOV-008 quorum, is designed to guarantee:

- lineage safety
- physical realism
- contradiction-free evolution
- uncertainty containment
- adversarial robustness
- debt-bounded epistemic growth
- agent-independent governance
- deterministic state transitions

None of these are currently guaranteed by this repository. They are the design targets this specification is meant to eventually deliver.

---

### PART 8 — Runtime Protocol Layer (Operational Specification, Not Yet Implemented)

#### 8.1 Runtime Evaluator Execution Loop

The evaluation engine processes every proposed state mutation `ΔI` through a deterministic pipeline prior to committing to the global state tree `I_{t+1}`.

1. **Ingress Vector Ingestion** — Assemble state vector `V(n) = [E(n), R(n), C(n), P(n), S(n)]ᵀ`.
2. **Coordinate Floor Truncation** — Enforce minimum precision floor: `vᵢ ← max(vᵢ, ε)`.
3. **Scalar Gate Evaluation** — Compute categorical gate limits `Φ(n), Ψ(n), Ξ(n), A(n)`.
4. **Maturity & Quality Computation** — Evaluate `Q(n)`, `A_adm(n)`, `M(n)`.
5. **Predicate Suite Execution** — Evaluate truth values across `Γ`.
6. **Kernel State Transition:**
   - If `∀γ ∈ Γ: γ(ΔI) = 1` ⟹ `I_{t+1} = σ(I_t, ΔI)`.
   - If `∃γ ∈ Γ: ¬γ(ΔI)` ⟹ `HALT_MUTATION`, trigger Triage Posture.

#### Predicate DAG (Directed Acyclic Graph Topology)

The predicate pipeline is executed in topological order for early short-circuit evaluation:

```
                     [ State Ingress ΔI ]
                              │
                              ▼
                  [ γ_unknown Validation ]
                  (E(n) ≥ e_min & R(n) ≠ ⊥)
                              │
            ┌─────────────────┴─────────────────┐
            ▼                                   ▼
  [ γ_grounding Gate ]                 [ γ_provenance Gate ]
  (Φ(n) == 1)                          (M(n) ≤ Ψ(n))
            │                                   │
            └─────────────────┬─────────────────┘
                              ▼
                    [ γ_conflict Gate ]
                    (c(n) == 0)
                              │
                              ▼
                   [ γ_challenge Gate ]
                   (s(n) == 0)
                              │
                              ▼
                   [ Deterministic Transition ]
                   σ(I_t, ΔI) ──► I_{t+1}
```

#### Verification State & Action Matrix

| State | Predicate Failure Profile | State Outcome | Automated Triage Action |
|---|---|---|---|
| **VERIFIED** | None (`∀γ = 1`) | State Transition Accepted | COMMIT_STATE |
| **UNKNOWN** | `γ_unknown = 0` | Incomplete Representation | UNKNOWN_REDUCTION |
| **UNGROUNDED** | `γ_grounding = 0` | Physical Floor Default | GROUNDING_REVALIDATION |
| **CEILING EXCEEDED** | `γ_provenance = 0` | Admissibility Overreach | CEILING_ENFORCEMENT |
| **CONFLICT** | `γ_conflict = 0` | Contradiction Detected | CONTRADICTION_RESOLUTION |
| **CHALLENGED** | `γ_challenge = 0` | Active Adversarial Sinking | SATURATE_VERIFICATION |

**No component of this Part is wired to any harness, evaluator, or automation in this repository.** It is a specification for what a future implementation should do, not a description of anything currently running.

#### 8.2 Genesis-Mode / Single-Agent Degradation (Required Behavior, Not Yet Implemented)

Part 8.1's execution loop implicitly assumes the `Γ` predicates are evaluated by an evaluator independent of whichever agent proposed `ΔI`. §Binding Status already establishes that no such independent evaluator currently exists in this repository — `GOV-008`'s quorum is Open. This subsection specifies what the runtime **must** do about that fact once it is implemented, rather than leaving the gap implicit.

**Rule:** if the runtime detects that fewer than the `GOV-008` minimum independent evaluators are live and reachable, the kernel **must not** issue a `VERIFIED` transition under any circumstance, regardless of how the `Γ` predicates individually evaluate. It must instead:

1. Refuse to commit the state transition (`σ` returns `I_t`, not `I_{t+1}`).
2. Escalate to the human-anchor / Genesis Phase Protocol defined in `Admin/Governance_Charter.md`, following the same role-separation rules that protocol already requires (authorization record generated in a separate session or external medium from the runtime session executing the action).
3. Log the degraded-mode transition attempt explicitly — a Genesis-mode refusal is not silent, it is a recorded event.

**Hard constraint:** self-evaluation of any `γ` by the same agent that proposed `ΔI` is constitutionally invalid under this kernel, full stop — it does not produce a degraded-but-usable VERIFIED state, it produces no VERIFIED state at all. There is no "single-agent VERIFIED with a caveat." A predicate evaluated by the proposing agent has not been evaluated for the purposes of this kernel.

This is why, as of 2026-07-31, every single-agent session working with this repository — including the one that drafted this document — operates in Genesis-Mode with respect to CIR v2.0's own kernel. Nothing in this repository has ever issued a CIR-VERIFIED transition, and nothing should, until `GOV-008` is ratified.

**8.2.1 Elaboration on refuse/escalate/log (candidate, 2026-08-06, human-directed):** an independent multi-agent thread (Grok/Copilot) drafted a parallel "Genesis-Mode Escalation Protocol" covering this same refuse/escalate/log sequence, without loading this section or `Admin/Governance_Migration_Protocol.md` §VII.5 (which already states quorum loss triggers automatic re-entry to Genesis-Phase-equivalent restricted mode). That draft's core structure — halt, escalate, human decides — is not new; it restates the rule above. Three specific refinements from that thread were not previously present here and are folded in as elaboration, not replacement:

- **Concurrent ΔI handling:** each degraded-mode transition attempt is logged independently (item 3 above already requires this); multiple simultaneously-refused `ΔI`s do not block or merge with one another.
- **Human decision paths, made explicit:** the human anchor's decision on a refused `ΔI` is one of three outcomes — reject permanently; return for revision (no VERIFIED status, re-evaluation required on resubmission); or authorize degraded-mode execution as an emergency-continuity exception. A degraded-mode execution under the third path still produces no VERIFIED state (per the Hard constraint above), must not update any maturity or provenance ceiling, and must not be cited as precedent for any future VERIFIED transition or future degraded-mode authorization — routine or repeated use of this path is itself a Track B drift signal per `Governance_Migration_Protocol.md`'s drift-indicator doctrine.
- **Re-entry after a prior Pathway 1 exit:** if a repository that previously satisfied `GOV-008` and exited Genesis Phase later fails a quorum check again, it re-enters Genesis-Mode degradation under this same rule. The prior exit is suspended, not revoked, and resuming VERIFIED transitions requires a fresh human confirmation — it does not inherit the earlier ratification.

This elaboration changes nothing about the Hard constraint, the refuse/escalate/log sequence, or this file's Binding Status — it makes three previously-implicit consequences explicit.

---

### PART 9 — Proposed Directory Boundary Split (Not Yet Executed)

If and when this document is ratified, the drafting recommendation is to partition it into two files under `Admin/`:

**`Admin/Constitutional_Core.md` (Immutable, pending ratification)**
Contents: Part 0.1 (Constitutional Principles), Part 1 (Axioms A1–A6), Part 2 (Verification Algebra), Part 3 (Predicate Definitions), Part 5 (Kernel Transition Logic).
Governance Boundary: Invariant across build variations. Requires full manual consensus ratification to modify — same bar as `Governance_Charter.md` Tier-1 Axioms.

**`Admin/Statutory_Parameters.md` (Tunable, pending ratification)**
Contents: Part 0.2 (Implementation Parameters: `ε`, `W`, `Ψ_class`, `θ_p`, `Δ_max`, `d(n)`), interface sampling frequency thresholds, challenge decay scales.
Governance Boundary: Tunable via build configuration or automated calibration runs without violating constitutional guarantees.

This split is **not executed** — this single file preserves the whole architecture intact until ratification makes the split meaningful. Splitting an unratified document into "immutable" and "tunable" files would be a category error: nothing here is binding yet, so nothing is truly immutable yet either.

---

## Relationship to Governance_Charter.md

CIR v2.0 does not merge with `Governance_Charter.md` and should not. The two operate at different layers:

| Dimension | CIR v2.0 (this file) | Governance_Charter.md |
|-----------|----------------------|------------------------|
| Primary job | Epistemic state machine + predicate governance for knowledge claims | Constitutional authority hierarchy + Tier-1 axioms for institutional power and legitimacy |
| What it gates | State mutations `ΔI` via `Γ` predicates | Governance actions and authority claims via Enforcement Checkpoints + Tier-1 Axioms |
| Scope boundary | Explicitly operational/runtime (Part 8), algebra, DAG, debt, triage | Explicitly does *not* define runtime engines or execution mechanics |
| Amendment regime | Full manual consensus ratification (once adopted) | Human ratification + formal migration, prior text preserved in Resolution Log |

**Where they already align, by design, not by accident:**
- External grounding as non-negotiable — CIR A1 / `γ_grounding` ↔ Charter Axiom Q-1.
- Provenance as ceilings, not evidence weight — CIR `Ψ` / `γ_provenance` ↔ Charter Checkpoint 5 (Truth Provenance Layering).
- Rejection of self-authorization, demand for independent review — CIR agent-independent transitions + predicate supremacy ↔ Charter Axiom Q-2 + Genesis Phase Protocol.
- Typed unknowns / explicit uncertainty rather than collapse — CIR `γ_unknown` + debt accounting ↔ Charter's "hidden uncertainty is more dangerous than acknowledged uncertainty" stance and `Unknowns.md`'s own Unknown Budget rules.
- Deterministic, auditable transitions; no silent mutation.
- Immutable constitutional floor vs. tunable parameters, in both documents independently.

**Where merging would actively harm both documents** (unchanged from the original drafting agent's analysis, verified sound): it would force the Charter to absorb runtime algebra it explicitly disclaims owning; it would collapse the Constitutional/Statutory split CIR needs and the Tier hierarchy the Charter needs; it would put a functioning evaluation engine *inside* a still-bootstrapping constitution, worsening rather than resolving the Bootstrap Paradox; and the two documents' amendment regimes would conflict if combined into one file.

**Recommended eventual relationship, once ratifiable:** CIR v2.0 becomes a Tier-2/Tier-3 epistemic governance substrate implementing several of the Charter's higher-level requirements, under the Charter's authority. Its predicates would reference the Charter's Q-1/Q-2/Q-4 as non-negotiable outer bounds they must never violate, and its triage posture would escalate to the Charter's Genesis Phase / Human Override / Escalation doctrines for anything beyond automated containment. None of this is active today.

---

## Lessons Learned

- (None yet — this document has no operational history.)

---

## Active Disputes

- (None currently open.)

---

## Auditor Notes / Unknowns

### CIR-GOV-001 — Predicate-to-Checkpoint mapping incomplete

| Field | Value |
|-------|-------|
| Status | Open — candidate mapping supplied, gaps documented |
| Risk | Low |
| Priority | Minor |
| Type | Technical / Governance |
| Blocking | No — does not block anything while this file is unratified |
| Owner | `Admin/CIR_Gov.md` |
| First Logged | 2026-07-31 |
| Last Reviewed | 2026-07-31 |

**Description:** CIR v2.0 defines five `Γ` predicates. `Governance_Charter.md` defines six Enforcement Checkpoints (verified against source 2026-07-31: 1 Internal Coherence, 2 Structural Plausibility, 3 Adversarial Pass, 4 Cross-Module Integration, 5 Truth Provenance Layering, 6 Audit Lineage Integrity). A candidate mapping now exists — see table below — and confirms this is a genuine design-completeness gap, not merely an unverified assumption: **two Checkpoints have no corresponding predicate at all.**

**Candidate Predicate ↔ Enforcement Checkpoint Mapping (Candidate / Unreviewed):**

| CIR Predicate (`Γ`) | Primary Checkpoint | Secondary / Supporting | Coverage Notes | Gap / Open Question |
|---|---|---|---|---|
| `γ_unknown` | 1 — Internal Coherence | 6 — Audit Lineage Integrity | Forces explicit representation of incompleteness (`E ≥ e_min`, `R ≠ ⊥`); prevents "silent unknown" being treated as coherent | Does Internal Coherence also require terminology stability / scope-boundary clarity that `γ_unknown` doesn't address? |
| `γ_grounding` | 5 — Truth Provenance Layering | 1 — Internal Coherence | Directly implements Axiom Q-1 and the four-tier provenance hierarchy; blocks physical claims sitting only at the coordinate floor (`S = ε`) | Checkpoint 5 also demands *labeling* of every claim; `γ_grounding` only gates physical nodes, doesn't yet enforce provenance labels on non-physical claims |
| `γ_provenance` | 5 — Truth Provenance Layering | 2 — Structural Plausibility | Enforces provenance as a hard ceiling (`M(n) ≤ Ψ_class(n)`) | The ceiling logic is clear; the `Ψ_class` taxonomy itself is still statutory and undefined |
| `γ_conflict` | 1 — Internal Coherence | 3 — Adversarial Pass | Categorical zeroing of contradictions (`c(n)=0`) | Checkpoint 3 also tests recursive-justification resistance and audit-theater detection — `γ_conflict` only catches explicit logical contradiction |
| `γ_challenge` | 3 — Adversarial Pass | 6 — Audit Lineage Integrity | Requires active adversarial sinking pressure to clear (`s(n)=0`); closest runtime analogue to a live adversarial battery | Gate strength depends entirely on `f(n)`/`s(n)` definitions — see §2.3.1 |
| *(none)* | **2 — Structural Plausibility** | — | **No direct predicate.** Tractability, bounded escalation, finite authority propagation, sparse axiom layer are meta-properties of the governance system itself, not of a single mutation `ΔI` | Explicit gap — no predicate can currently fail a mutation for "this would make the overall system structurally implausible" |
| *(none)* | **4 — Cross-Module Integration** | — | **No direct predicate.** Dependency mapping, ownership boundaries, upstream/downstream stability are repository-level, not single-mutation concerns | Explicit gap — could be partially addressed by a future `γ_lineage` or by requiring an explicit dependency vector checked against the ownership table |

**Coverage summary:** Checkpoint 1 (Strong: `γ_unknown`+`γ_conflict`) · Checkpoint 2 (**Gap**) · Checkpoint 3 (Moderate, depends on `s(n)` definition) · Checkpoint 4 (**Gap**) · Checkpoint 5 (Strong: `γ_grounding`+`γ_provenance`) · Checkpoint 6 (Weak-to-moderate, partial via `γ_unknown`/`γ_challenge`).

**Resolution Path:** the two genuine gaps (Checkpoints 2 and 4) are acceptable while this document remains unratified, but any future ratification discussion must either (a) add one or more new predicates for them, or (b) explicitly declare those Checkpoints outside the runtime kernel's scope, enforced only by the higher-tier Charter/Auditor layer instead. This must be an explicit decision at ratification time, not a silent omission carried forward.

---

## Abandoned Paths

- (None — this is a first draft, not a revision of a prior rejected approach.)

---

## Resolution Log

- 2026-08-06: **§8.2.1 added — elaboration on refuse/escalate/log, reconciled from an independent multi-agent thread.** A Grok/Copilot thread drafted a parallel "Genesis-Mode Escalation Protocol" without loading this section or `Governance_Migration_Protocol.md` §VII.5 (which already specifies automatic re-entry to Genesis-Phase-equivalent restricted mode on quorum loss). Its core halt/escalate/human-decides structure restated §8.2's existing rule rather than adding to it. Three genuinely new refinements — concurrent-ΔI logging, an explicit three-path human decision structure (reject / return for revision / degraded-mode exception with an explicit anti-precedent clause), and a re-entry-after-prior-Pathway-1-exit rule — were folded in as §8.2.1, framed as elaboration of the Hard constraint and refuse/escalate/log sequence, not a replacement. Binding Status, the Hard constraint, and this file's Status (Proposed — Not Ratified) are unchanged. See `Governance_Migration_Protocol.md` §VII.8 for the companion registry/runtime-gate reconciliation from the same thread. Operating as Synthesizer, human-directed.

- 2026-07-31: **Skeptic/Auditor review pass integrated (six substantive additions).** Grok reviewed the filed document — same session as original drafting, a limitation the human governing authority explicitly flagged ("should have started a new instance to maximize cognitive purity... lesson for the future"). Given that, every factual claim in the review was independently re-verified against source before integration rather than accepted on the reviewing agent's authority: confirmed all six `Governance_Charter.md` Enforcement Checkpoint names/numbers exactly, and confirmed the Checkpoint 2 (Structural Plausibility) and Checkpoint 4 (Cross-Module Integration) "no corresponding predicate" gap claims against the Checkpoints' actual requirement text. Six changes integrated: (1) candidate Predicate↔Checkpoint mapping table replacing CIR-GOV-001's prior bare description, status updated to "candidate mapping supplied, gaps documented"; (2) new §8.2 Genesis-Mode/Single-Agent Degradation, making explicit that self-evaluation of any γ by the proposing agent is constitutionally invalid under this kernel — not a lesser passing grade, no VERIFIED state at all; (3) new §2.3.1 defining f(n) and s(n) for the previously under-specified Adversarial Challenge Gate; (4) new §6.5 Debt Aging/Resolution Credit, closing the permanent-triage-lock-in gap where resolved unknowns never reduced accumulated debt; (5) Unknown Conservation corollary added under A6, formally linking the Nothingness bridge to `Unknowns.md`'s Unknown Budget rule; (6) γ_provenance ceiling-vs-target inversion warning added inline. Also: Highest Risk raised Medium→High, ASM-CIR-002 reframed from a confidence rating to a documented design-completeness gap (Checkpoints 2/4 have zero predicate coverage), Open Unknowns field corrected to describe CIR-GOV-001 (this file's own tracked item) rather than conflating it with the separately-owned GOV-008 dependency. Declined to integrate: worked micro-examples (3 test vectors) — genuinely useful but lower priority than the structural gaps above; left as a future refinement, not filed as a new unknown. Operating as Synthesizer per Auditor_Protocols.md v0.29, human-directed.

- 2026-07-31: Filed as a new document, `Admin/CIR_Gov.md`, preserving the full CIR v2.0 architecture (Parts 0–8) as drafted, plus a minimal Nothingness Theorem positivity bridge (Axiom A6) per the drafting agent's own "selective inclusion, not full merge" recommendation. Explicitly filed **Proposed — Not Ratified**, with a §Binding Status section placed immediately after File Purpose (before the algebra) stating plainly that the kernel's central "agent-independent transitions" claim is not currently true of this repository, because GOV-008 (verified against `Unknowns.md` and `Governance_Charter.md` before filing: Open, no concrete specification, Checkpoint 2 BLOCKED — Bootstrap Paradox) has no ratified quorum for the `Γ` predicates to be evaluated by. Sequencing recommendation recorded: GOV-008 first, CIR v2.0 adoption second. Registered CIR-GOV-001 (predicate-to-Checkpoint mapping gap) as the one open item tracked against this file. Human governing authority directed the filing with the explicit goal of preserving the ideology intact even while unratified, rather than either discarding it or quietly treating it as live. Operating as Synthesizer per Auditor_Protocols.md v0.29, human-directed.
