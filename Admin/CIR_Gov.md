# CIR_Gov.md — Computational Institutional Reasoning v2.0

*Admin/CIR_Gov.md*

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

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
| Verification Ref | `Admin/Verification_Gates_LF.md` |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Highest Risk | Medium — this document has no runtime authority; the risk is *misreading* it as operational rather than any hazard in its content. See §Binding Status below. |
| Last Audit | 2026-07-31 |
| Auditor | Grok — drafted CIR v2.0 architecture (Parts 0–8) and Nothingness-bridge/naming recommendations; Claude — Synthesizer, verified cross-references against `Governance_Charter.md`, `Nothingness_Theorem.md`, and `Unknowns.md` GOV-008 status before filing; human-directed, 2026-07-31 |
| Open Unknowns | 1 (GOV-008 dependency — see §Binding Status; tracked in `Unknowns.md`, owned by `Governance_Charter.md`, not by this file) |
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

CIR v2.0 is a candidate epistemic governance kernel for LazarusForgeV0 — a machine-checkable way to gate proposed state mutations through predicate logic rather than narrative judgment alone. It elevates predicates (`Γ`) to the primary admissibility mechanism, separates epistemic quality (`Q`) from admissibility (`A_adm`), treats provenance as a hard ceiling rather than a soft score, gives unknowns explicit weighted-graph semantics with debt accounting, and defines a deterministic state-transition kernel (`σ`) with a graded, debt-bounded triage posture.

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
| ASM-CIR-001 | A deterministic predicate kernel is a good target architecture for LazarusForgeV0's eventual governance automation | Aligns with existing Verification Gates (G1–G6), Auditor Protocols' Adversarial Battery, and the repo's general preference for falsifiable, evidence-graded doctrine over narrative judgment | Medium — Analogous to existing gate structures, not yet tested as a unified kernel | A working reference implementation is built and run against real state mutations |
| ASM-CIR-002 | The five `Γ` predicates (grounding, provenance, conflict, unknown, challenge) are a complete and non-redundant set for constitutional-class admissibility decisions | Internal design choice by the drafting agent; not independently derived from `Governance_Charter.md`'s own six Enforcement Checkpoints | Low — Placeholder pending mapping exercise (see §Relationship to Governance_Charter.md) | A formal mapping between CIR's five predicates and the Charter's six Checkpoints is completed and reviewed |
| ASM-CIR-003 | GOV-008, once ratified, will produce a quorum shape compatible with what CIR's Part 8 runtime evaluator assumes (independently reachable, responsive agent instances capable of predicate evaluation) | Speculative — GOV-008 is currently unratified; its eventual concrete form is unknown | Low | GOV-008 is ratified and its quorum definition is checked against CIR's runtime assumptions |

---

## Body

### PART 0 — Constitutional Architecture

#### 0.1 Constitutional Principles (Immutable Within This Document's Own Frame)

These principles are immutable *within CIR v2.0 itself* — i.e., changing them would mean drafting a different kernel, not amending this one. They are **not** constitutionally immutable for LazarusForgeV0 as a whole; that authority remains solely with `Governance_Charter.md`'s Tier-1 Axioms until and unless this document is ratified and placed under that authority per §Relationship to Governance_Charter.md.

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

**Contradiction Gate**

```
Ξ(n) = 0  if c(n) > 0
     = 1  if c(n) = 0
```

**Adversarial Challenge Gate**

```
A(n) = [f(n) / (f(n)+1)] · [1 / (1+s(n))]
```

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
γ_challenge(n)  = 1 if s(n) = 0,  else 0
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
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Technical / Governance |
| Blocking | No — does not block anything while this file is unratified |
| Owner | `Admin/CIR_Gov.md` |
| First Logged | 2026-07-31 |
| Last Reviewed | 2026-07-31 |

**Description:** CIR v2.0 defines five `Γ` predicates. `Governance_Charter.md` defines six Enforcement Checkpoints. No formal mapping between the two exists yet — it is asserted informally in §Relationship to Governance_Charter.md that some predicates correspond to some Checkpoints, but a rigorous one-to-one (or documented many-to-many) mapping has not been produced or reviewed.

**Resolution Path:** Before this document could be seriously considered for ratification, produce an explicit mapping table (`γ_x ↔ Checkpoint N`) and identify any Charter Checkpoint with no corresponding CIR predicate, or any CIR predicate with no corresponding Checkpoint — either gap needs an explicit decision, not silent omission.

---

## Abandoned Paths

- (None — this is a first draft, not a revision of a prior rejected approach.)

---

## Resolution Log

- 2026-07-31: Filed as a new document, `Admin/CIR_Gov.md`, preserving the full CIR v2.0 architecture (Parts 0–8) as drafted, plus a minimal Nothingness Theorem positivity bridge (Axiom A6) per the drafting agent's own "selective inclusion, not full merge" recommendation. Explicitly filed **Proposed — Not Ratified**, with a §Binding Status section placed immediately after File Purpose (before the algebra) stating plainly that the kernel's central "agent-independent transitions" claim is not currently true of this repository, because GOV-008 (verified against `Unknowns.md` and `Governance_Charter.md` before filing: Open, no concrete specification, Checkpoint 2 BLOCKED — Bootstrap Paradox) has no ratified quorum for the `Γ` predicates to be evaluated by. Sequencing recommendation recorded: GOV-008 first, CIR v2.0 adoption second. Registered CIR-GOV-001 (predicate-to-Checkpoint mapping gap) as the one open item tracked against this file. Human governing authority directed the filing with the explicit goal of preserving the ideology intact even while unratified, rather than either discarding it or quietly treating it as live. Operating as Synthesizer per Auditor_Protocols.md v0.29, human-directed.
