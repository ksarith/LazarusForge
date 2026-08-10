# Cognitive_Salvage_Layer.md
**Version 0.4**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Draft                                                               |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-08-03                                                          |
| Auditor          | Claude — Synthesizer/Auditor, human-directed, 2026-08-03: corrective merge of a Copilot/Grok exchange — GH-004/GH-012/CSL-A03 gained complementary elaboration (Payment via Specification only, see AP-033 in Admin/Auditor_Protocols.md); GH-007/GH-008/GH-009/GH-011 left untouched, already better-specified than what was proposed; prior: Claude — Synthesizer/Auditor                                        |
| Open Unknowns    | 13                                                                  |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Cognitive Salvage Layer as a distinct architectural module within LazarusForgeV0
- The heuristic failure class that motivates human-in-the-loop integration
- The feedback loop architecture from physical scan to autonomous execution — covering both disassembly/triage and fabrication heuristics
- The Auditor Decision Tree for candidate heuristic verification (Stages 1–4)
- The six-status grading classification matrix including CANDIDATE_NOVEL
- The Heuristic Object schema for telemetry and logging
- Integration points with existing Forge modules including Gate_06_Fabrication.md
- The Leviathan emergency cognition connection
- GH-series unknowns governing heuristic governance architecture

**This file DOES NOT define:**
- Game design, player experience, or interface specifications
- Puzzle generation algorithms or procedural content systems
- Robotic arm kinematic models or IK solver implementations
- Finite element analysis methodology or FEA toolchain selection
- Forge_Net.md federated knowledge base architecture
- Auditor protocol operational behavior (→ `Admin/Auditor_Protocols.md`)
- Canonical terminology (→ `Admin/Canonical_Terms.md`)
- Leviathan deployment architecture (→ `Operations/Leviathan.md` — planned)
- Weld qualification standards or fabrication tolerance specifications (→ `Operations/Gate_06_Fabrication.md`)

---

## File Purpose

This file defines the **Cognitive Salvage Layer**: a human-in-the-loop heuristic harvesting pipeline that converts player-solved spatial and triage puzzles into verified, machine-executable protocols for the Lazarus Forge.

The layer exists to address a specific and underserved failure class: **heuristic failure**. This is distinct from sensor failure and mechanical failure. In a heuristic failure, the object is technically visible, the materials are technically identifiable, and the machine technically has the tools — yet the system does not know which bolt to remove first, which cut avoids structural collapse, which weld path routes around a stress concentration, which fixturing sequence stabilizes a non-standard geometry, or which joining order prevents distortion in mismatched salvaged components. These are problems humans solve extraordinarily well, and they appear on both sides of the Forge's operational flow: disassembly and fabrication alike.

The game interface is not the product. **The heuristic extraction pipeline is the product.**

This layer extends the Forge's core salvage-first doctrine from physical materials to human cognition itself:

> Human problem-solving effort is itself a salvageable resource.

Just as the Forge assumes that discarded materials contain unrealized value, the Cognitive Salvage Layer assumes that millions of hours of distributed human puzzle-solving contain recoverable operational knowledge — provided the extraction and verification pipeline is rigorous enough to separate genuine insight from game-engine artifact.

**Note on heuristic sources:** While the gamified puzzle interface is the primary harvesting mechanism described here, the verification pipeline is source-agnostic. Candidate heuristics could enter from players, operators, technicians, auditors, other Forge nodes, or autonomous model-generated proposals — all passing through the same four-stage verification funnel. The game is one harvesting mechanism, not the definition of the layer.

---

## Assumptions

| ID      | Assumption                                                                              | Basis                                | Confidence  | Expiry Trigger                                          |
|---------|-----------------------------------------------------------------------------------------|--------------------------------------|-------------|---------------------------------------------------------|
| CSL-A01 | Heuristic failures represent a meaningful fraction of Forge operational bottlenecks     | Analogous salvage system behavior    | Analogous   | Operational data from first Leviathan deployment cycles |
| CSL-A02 | Human spatial reasoning reliably surfaces solution paths that autonomous planning misses | Analogous (Foldit, protein folding)  | Analogous   | GH-001 resolution via empirical testing                 |
| CSL-A03 | A gamified interface can abstract real salvage geometry with sufficient fidelity         | Placeholder — no Forge-specific data | Placeholder | Stage 3 validation pass on first physical anomaly       |
| CSL-A04 | The Forge's existing Auditor Protocols are sufficient to gate heuristic promotion        | Internally Derived                   | PROVISIONAL | GH-003 (adversarial poisoning) resolution               |
| CSL-A05 | Players will not systematically attempt to poison the heuristic dataset                 | Placeholder — no deployment data     | Placeholder | GH-003 resolution                                       |
| CSL-A06 | Stage 3 high-fidelity simulation predicts physical outcomes with sufficient accuracy     | Placeholder — no Forge-specific data | Placeholder | First S2R delta measurement on promoted heuristic       |

CSL-A06 is load-bearing: the entire pipeline's safety guarantee rests on Stage 3 catching hazardous sequences. If simulation-to-physical fidelity is low, promoted heuristics may pass Stage 3 while failing in physical execution. This assumption requires empirical validation before any heuristic reaches Operational Spec status.

**CSL-A03 elaboration (Payment via Specification, added 2026-08-03 — human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** the expiry trigger above ("Stage 3 validation pass on first physical anomaly") elaborated as a concrete test: at the first physical anomaly that generates a puzzle, perform Stage 3 validation of the resulting heuristic and compare simulated versus measured physical profiles; if Δ_physical exceeds a Placeholder threshold ε, flag the puzzle physics model for redesign. Required artifact if adopted: a `Puzzle Fidelity Validation Log` recording anomaly_class, Δ_physical, and the redesign decision. This does not close CSL-A03 — it only states the test that will run when first-anomaly data exists, same as the existing expiry trigger already implies.

---

---

## Body

### The Heuristic Failure Class

Standard Forge operational flow assumes:

1. Material enters the system.
2. Sensors classify it.
3. Agents decide what to do.
4. Machinery executes.

This flow fails silently on a specific class of problem where the sensor and classification layers return valid data but the planning layer lacks the procedural knowledge to act optimally — or at all.

**Disassembly manifestations:**
- A structurally deformed hull section where standard disassembly sequence causes tool-pinching collapse.
- A biofouled assembly where cut order determines whether contamination spreads to clean components.
- A non-standard geometry where bolt removal priority is load-bearing and non-obvious.
- An edge-case material state (severe corrosion, fused joints, unexpected composites) outside the planning agent's training distribution.

**Fabrication manifestations:**
- A warped salvaged frame where weld path routing must avoid stress concentrations not evident from geometry alone.
- A non-standard component geometry requiring fixturing sequences that prevent distortion under clamp load.
- Mismatched salvaged materials where joining order determines whether thermal distortion propagates to structurally critical areas.
- A recovered assembly where repair sequence must preserve function in adjacent components that cannot be disassembled first.

These are not failures of sensing or execution. They are failures of procedural knowledge. Fabrication heuristic failures are in some respects more dangerous than disassembly failures: a bad disassembly sequence usually fails visibly and immediately; a bad fabrication sequence can produce a structurally compromised output that passes visual inspection and fails under load.

**Canonical Terms candidate:** *Heuristic Failure* as a first-class Forge failure class, distinct from Sensor Failure and Mechanical Failure. Registration proposed in `Admin/Canonical_Terms.md` as HF-001. Until registered, treat as PROVISIONAL vocabulary in this file only.

---

### Feedback Loop Architecture

The Cognitive Salvage Layer operates as a verification-gated pipeline from physical anomaly to autonomous execution update. The pipeline applies identically to disassembly and fabrication heuristics — the anomaly_class field in the Heuristic Object distinguishes them.

```
[Physical Salvage Scan / Fabrication Task]
              |
              |  Deformed geometry, unknown material composition,
              |  low-confidence triage or fabrication classification
              v
[Gamified Simulation Node]
              |
              |  Constraint-driven spatial puzzle; player explores
              |  solution space under abstracted physical rules
              v
[Heuristic Extraction]
              |
              |  Player action sequence captured as
              |  candidate Heuristic Object
              v
[Canonicalization Pass]  <- see GH-011
              |
              |  Normalize variant sequences to core heuristic;
              |  deduplicate evidence across player runs
              v
[Auditor Verification Pipeline]
              |
              +--- EXPLOIT -------> Archive: Engine Exploit Log
              +--- UNSAFE --------> Quarantine: Hazardous Sequence Log
              +--- SUBOPTIMAL ----> Archive: Low Priority
              +--- FEASIBLE ------> Queue for Execution
              +--- CANDIDATE_NOVEL> Pending threshold definition (GH-006)
              +--- NOVEL ---------> Immediate Promotion (threshold TBD)
                        |
                        v
              [Forge Knowledge Base]
                        |
                        v
              [Autonomous Execution]
              (Updated triage, fabrication,
               stratification, disassembly protocols)
```

The canonicalization pass is shown as a distinct stage but is currently undefined — see GH-011. Until GH-011 resolves, the pipeline proceeds directly from heuristic extraction to Stage 1 verification, accepting the accumulation of variant sequences as a known limitation.

**The critical distinction:** The player never directly teaches the Forge. The player generates candidate solutions. The Forge verifies them. That separation is what makes the pipeline safe to operate at scale.

---

### Core Data Streams

**Triage and Disassembly Path Logging**
Chronological sequence of player actions — where they cut, separate, unbolt, or manipulate a component and in what order. Sequence order is often the entire insight.

**Fabrication Path Logging**
Chronological sequence of construction actions — weld path routing, fixturing order, joint sequence, clamp placement and removal order. Sequence order in fabrication determines thermal distortion accumulation, residual stress distribution, and accessibility of subsequent operations.

**Volumetric and Geometric Manipulation**
How players rotate, align, and fit non-standard geometries into disassembly or fabrication configurations. Captures spatial reasoning that planning agents cannot derive from static geometry alone.

**Constraint Interactions**
Where players repeatedly fail, back up, or hit simulation limits. Failure clustering identifies structural stress points, biofouling traps, load-bearing sequences, and fabrication distortion patterns before physical tools ever contact the material. Failed attempts are data.

**Optimization Metrics**
Time, estimated tool wear, contamination risk exposure, distortion risk, and energy proxies for each solution path. Required for Stage 4 multi-dimensional efficiency grading.

---

### The Heuristic Object Schema

Every candidate solution path is serialized as a Heuristic Object before entering the Auditor pipeline.

```json
{
  "heuristic_id": "HS-XXXX",
  "anomaly_source": "[Scan ID and anomaly description]",
  "anomaly_class": "[Deformed geometry | Biofouled | Unknown composite |
                     Fabrication-weld | Fabrication-fixturing |
                     Fabrication-joint | ...]",
  "action_sequence": [
    {
      "action_type": "[CUT | SEPARATE | UNBOLT | WELD | FIXTURE | CLAMP | ...]",
      "target_component": "[component ID]",
      "parameters": {},
      "timestamp_sim_ms": null
    }
  ],
  "constraint_violations_logged": 0,
  "auditor_status": "PENDING_SIMULATION",
  "simulation_fidelity_version": "[engine version or hash]",
  "stage_outcomes": {
    "stage_1_abstraction": null,
    "stage_2_kinematic": null,
    "stage_3_physical_sim": null,
    "stage_4_efficiency": null
  },
  "metrics_delta": {
    "delta_t_seconds": null,
    "tool_wear_factor": null,
    "material_yield_value": null,
    "distortion_risk_delta": null
  },
  "candidate_novel_flag": false,
  "provenance": "Player_Swarm | Single_Player | Operator_Override | Technician | Forge_Node",
  "provenance_trust_tier": null,
  "session_count": 1,
  "consensus_run_count": 0,
  "validated_on_machinery_revision": null,
  "physical_grounding_ref": null,
  "failure_modes_observed": []
}
```

**Field notes:**

`action_sequence` — typed structure. Each entry specifies action type, target, parameters, and simulation timestamp. Supports kinematic replay in Stage 2 and canonicalization in GH-011.

`simulation_fidelity_version` — engine version or hash at time of capture. Required for GH-007 (puzzle fidelity drift) detection.

`metrics_delta` — replaces v0.1 `efficiency_delta`. Multi-dimensional object covering time, tool wear, material yield value, and distortion risk. Required for Stage 4 Pareto grading and CANDIDATE_NOVEL evaluation.

`candidate_novel_flag` — replaces v0.1 `novelty_flag`. Set true when Stage 4 identifies a heuristic that improves at least one metrics_delta dimension without degrading others below baseline. Does not constitute NOVEL promotion — GH-006 must close first.

`validated_on_machinery_revision` — machinery revision ID at time of physical validation. Required for GH-008 (heuristic expiration) tracking.

`provenance_trust_tier` — differentiates handling in the Auditor pipeline based on source reliability. Tier 1: Operator_Override with physical grounding. Tier 2: Technician or domain expert. Tier 3: Player_Swarm or Single_Player. Tier 4: Forge_Node (autonomous model-generated proposal). Higher-tier provenance may warrant reduced consensus_run_count requirements in GH-002 resolution — the threshold should be stratified by trust tier, not uniform. Null until provenance trust tier doctrine is formally defined.

`failure_modes_observed` — array populated from player constraint violations during simulation and from Stage 3 failure outcomes for paths that did not fully pass. Supports negative learning: a path that fails Stage 3 with a specific structural collapse mode provides information about the anomaly class even though it is not promoted. Empty array at submission; populated by Auditor pipeline during verification.

`physical_grounding_ref` — reference to the physical execution outcome record. Constitutes the EF-0.8b grounding artifact. Null until physical execution occurs; heuristics without this field remain PROVISIONAL regardless of Stage 3 outcome.

---

### Auditor Decision Tree

When a player submits a successful solution path, the Heuristic Object enters a four-stage verification pipeline. The Forge treats player inputs as untrusted, unverified candidate heuristics at all times.

```
[Player Solution Submitted]
              |
              v
+-----------------------------+
|  Stage 1: Abstraction &     |
|  Exploit Verification       |
+-------------+---------------+
              |
     Pass ----+----> Fail --> [Archive: Engine Exploit Log]
              |
              v
+-----------------------------+
|  Stage 2: Kinematic &       |
|  Collision Mapping          |
+-------------+---------------+
              |
     Pass ----+----> Fail --> [Archive: Kinematic Mismatch]
              |
              v
+-----------------------------+
|  Stage 3: Physical          |
|  Simulation & Stress Test   |
+-------------+---------------+
              |
     Pass ----+----> Fail --> [Archive: Material Failure /
              |                Hazardous Sequence]
              v
+-----------------------------+
|  Stage 4: Efficiency &      |
|  Yield Grading              |
+-------------+---------------+
              |
              v
     [Grading Classification]
     FEASIBLE | CANDIDATE_NOVEL | SUBOPTIMAL
              |
              v
     [Forge Knowledge Base]
```

---

### Stage 1 — Abstraction and Exploit Verification

The Auditor isolates the action sequence from the game engine's rendering and physics layer to confirm the player did not exploit simulation artifacts.

**Boundary Violations:** Did any object surfaces intersect or pass through one another in a way real-world matter cannot?

**Temporal Anomalies:** Did actions occur faster than real-world physical actuators or human reaction times allow within the simulation's stated parameters?

*Fail outcome:* Flag as EXPLOIT. Log the simulation defect to the puzzle engine bug registry. Discard the path.

*Archive value:* Exploit logs are a systematic record of simulation fidelity gaps. Cross-reference `simulation_fidelity_version` for version-specific exploit patterns (GH-007).

---

### Stage 2 — Kinematic and Collision Mapping

Human bodies have highly redundant degrees of freedom that standard 6-axis industrial robotic arms cannot replicate. This applies to both disassembly and fabrication — a weld path that a human hand can execute may require a robot to approach from an angle that causes chassis collision or reach limit violation.

**Actuator Emulation:** The Auditor replays the player's vector movements through an inverse kinematics model of the target Forge machinery.

**Tooling Clearance:** Does the physical tool geometry fit into the physical space the player utilized without chassis collision? For fabrication tasks, this includes torch angles, electrode access, and clamp arm geometry.

*Fail outcome:* Flag as KINEMATIC_MISMATCH. Archive the path. Use the failure data to adjust the puzzle's tool constraint model.

---

### Stage 3 — Physical Simulation and Stress Testing

Stage 3 subjects the candidate path to high-fidelity finite element analysis and rigid-body dynamic simulation.

**For disassembly paths:**
- Structural collapse under gravity if sequence is incorrect.
- Contamination and biofouling propagation vectors.
- Material state assumptions (tensile strength, ductility, joint integrity).

**For fabrication paths:**
- Thermal distortion accumulation across the weld or joining sequence.
- Residual stress distribution and potential stress concentration points.
- Fixturing adequacy — does the proposed clamp arrangement prevent distortion, or does it introduce new stress concentrations?
- Accessibility of subsequent operations — does the sequence close off access to later joints?

*Fail outcomes:* MATERIAL_FAILURE or HAZARDOUS_SEQUENCE.

*S2R Delta trigger (GH-003 partial mitigation):* If physical execution of a promoted heuristic encounters more than a defined variance threshold in expected torque, resistance, or thermal profile, the heuristic is immediately demoted to UNSAFE quarantine and the simulation model is flagged for recalibration. The specific variance threshold is Placeholder pending first physical execution data.

---

### Stage 4 — Efficiency and Yield Grading

A path that survives Stages 1–3 is physically feasible. Stage 4 determines its operational value using multi-dimensional grading against the current autonomous baseline.

**Delta-T:** Reduction in operational cycle time.

**Tool Wear Factor:** Does the path reduce tool wear relative to the autonomous baseline?

**Material Yield Value:** Does the sequence preserve high-value components and minimize fabrication waste? Cross-reference `Economics.md`.

**Distortion Risk Delta:** For fabrication paths — does the sequence reduce thermal distortion and residual stress relative to baseline?

**CANDIDATE_NOVEL evaluation — Pareto criterion (Placeholder):** A heuristic is flagged `candidate_novel_flag: true` when it improves at least one `metrics_delta` dimension without degrading any other below the autonomous baseline. The formal NOVEL promotion threshold remains undefined pending GH-006. Until GH-006 closes, all CANDIDATE_NOVEL entries are held at FEASIBLE disposition.

---

### Grading Classification Matrix

| Status Code      | Disposition               | Description                                                                                       |
|------------------|---------------------------|---------------------------------------------------------------------------------------------------|
| FEASIBLE         | Queue for Execution       | Physically valid. Performs equal to current autonomous baseline.                                   |
| CANDIDATE_NOVEL  | Hold — Pending Threshold  | Improves at least one metrics_delta dimension without degrading others. Held at FEASIBLE disposition until GH-006 resolves. |
| NOVEL            | Immediate Promotion       | Exceeds baseline per formal multi-dimensional threshold. **No heuristic may receive NOVEL status until GH-006 closes.** |
| SUBOPTIMAL       | Archive / Low Priority    | Physically valid but slower, higher tool wear, lower yield, or higher distortion than baseline.   |
| UNSAFE           | Quarantine                | Causes damage, collapse, contamination spread, or unacceptable fabrication distortion. Also triggered by S2R delta exceedance post-promotion. |
| EXPLOIT          | Scrub / Bug Log           | Relies on simulation inaccuracies. No physical insight recoverable without simulation repair.      |

---

### Integration Points

### Component_Triage_System.md / Gate_02_Triage.md
When triage confidence drops below threshold, the item is flagged and a puzzle instance generated.

### Gate_06_Fabrication.md
When the fabrication planning agent encounters a geometry, material combination, or repair scenario outside its procedural knowledge envelope, it flags the task and generates a fabrication puzzle instance. The anomaly_class field distinguishes fabrication from disassembly heuristics in the pipeline. Weld qualification standards and tolerance specifications remain owned by Gate_06_Fabrication.md.

### Admin/Auditor_Protocols.md
The Auditor Decision Tree operates under the full epistemic doctrine of `Admin/Auditor_Protocols.md`. Stage 3 results are PROVISIONAL pending physical grounding per EF-0.8b. UNSAFE and EXPLOIT classifications map to EF-0.2 Level 2 (Subsystem Quarantine).

### Forge_Net.md (planned)
NOVEL-classified Heuristic Objects federated as cognitive save states. Dormant until GH-006 resolves.

### Leviathan / Autonomous Swarm Operations

```
[Leviathan: Confidence Collapse on disassembly or fabrication task]
              |
              v
[Generate Puzzle Instance from anomaly scan]
              |
              v
[Human swarm explores solution space]
              |
              v
[Auditor pipeline verifies candidate paths]
              |
              v
[Verified heuristic returned to Leviathan]
              |
              v
[Autonomous execution resumes with updated knowledge]
```

### Admin/Security_Protocols.md
GH-003 adversarial resistance requirements route here: rate-limiting, honeypot anomaly injection, diversity sampling, session isolation.

---

### Conceptual Salvage Pipeline (Exploration)

*Status: Exploration within Exploration. This subsection is provisional — a proposed second pipeline, not yet a specified one. It has not passed Gate 1. Nothing here should be treated as active doctrine until GH-013 (below) is resolved and this subsection is promoted through the same Auditor Decision Tree the physical pipeline uses.*

Everything above this point in Body grades a *physical action* — a player disassembled, kinematically mapped, or fabricated something real, and the Auditor pipeline verifies the outcome against physical grounding. This subsection proposes a structurally different pipeline: recovering *verified knowledge and investigative pathways* generated by engaging seriously with a premise that was never physical at all — fiction, games, speculation, "what if" reasoning.

**Origin case (2026-07-12, James, via r/InnovativeAIChats / ChatGPT discussion):** A homebrewed illusion-power character, constrained at creation to "optical, not psychic" illusions, drove real investigation into optics, wavelength behavior, and eventually laser utility — none of which had anything to do with winning the game. The fictional premise (a superhero's illusion power) is discarded entirely. What survives is a real, independently verifiable knowledge trajectory: optics → EM spectrum → lasers → industrial cutting → Forge fabrication relevance.

**Why this is a different pipeline, not a variant of the existing one:**

| | Heuristic Failure Class (existing) | Conceptual Salvage (proposed) |
|---|---|---|
| Input | A physical action attempt on real material | An idea, premise, or question — physical or not |
| Stage 1 (Abstraction) | Verify the exploit/action makes physical sense | Separate fiction/premise from the genuine question it provoked |
| Stage 2 (Kinematic) | Map physical motion | *No physical motion exists to map — this stage has no equivalent* |
| Stage 3 (Simulation) | Stress-test in Forge simulator | *No simulator target exists — the "simulation" is whatever real-world verification method the question itself demands (literature, physics, existing Forge doctrine)* |
| Stage 4 (Grading) | Efficiency/yield metrics_delta | Some other metric — not yet defined; see GH-013 |
| Output | A Heuristic Object tied to a machinery revision | Some other artifact — not yet defined; see GH-013 |

The two right-column rows marked "no equivalent" are the actual reason this can't simply extend the existing schema. A Heuristic Object's entire structure (action_sequence, metrics_delta, simulation_fidelity_version, validated_on_machinery_revision) assumes physical grounding at every field. A conceptual salvage artifact has none of that to anchor to — it needs its own object shape, which has not been designed.

**Working principle (provisional, not yet ratified):** *Every idea is provisional feedstock. Cognitive salvage seeks not to preserve ideas intact, but to recover the verified knowledge, questions, and investigative paths they contain.* This extends the Forge's existing salvage-first doctrine (recover value from what looks like waste) into the cognitive domain, but it does not relax this file's evidence standards — the fiction is discarded specifically *because* only the independently verifiable knowledge it provoked is kept. A conceptual salvage pipeline that skipped verification would be indistinguishable from just believing things because they sound plausible, which is exactly the failure mode the Adversarial Challenge Battery exists to catch.

**What would need to exist before this is more than a provisional note:**
1. A storage/object schema for conceptual salvage artifacts, distinct from the Heuristic Object schema (GH-013, below).
2. A Stage-1-equivalent process for separating a premise's fiction from the genuine question it provoked, with an explicit test for "is this actually a verifiable question, or just an interesting-sounding claim."
3. A verification method to replace Stage 3's simulator — likely routing to existing Forge doctrine files, literature, or established physics/engineering knowledge rather than a Forge-specific simulation.
4. Explicit non-goals: this pipeline should not become a backdoor for unverified claims to enter the Forge's knowledge base under the appearance of having "passed a gate." Whatever gate structure it eventually gets must be at least as strict as the physical pipeline's, not weaker.

---

### Relationship to Existing Documents

- `Admin/Auditor_Protocols.md` — epistemic governance layer
- `Admin/Ethical_Constraints.md` — hard-line constraints apply
- `Admin/Canonical_Terms.md` — HF-001 (Heuristic Failure) registration proposed
- `Architecture/Forge_flow.md` — reference standard for shared terminology
- `Unknowns.md` — GH-series global index
- `Forge_Net.md` — planned; federation target for NOVEL Heuristic Objects
- `Operations/Leviathan.md` — planned; primary emergency cognition consumer
- `Operations/Gate_06_Fabrication.md` — fabrication integration point
- `Economics.md` — value retention weighting for Stage 4
- `Admin/Security_Protocols.md` — adversarial resistance requirements (GH-003)
- `Discovery.md` — registered at v0.1

### Core Invariant

**What must remain constant:**

**The player generates candidate solutions. The Forge verifies them. That distinction is what makes the pipeline safe.**

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                              | What Failed                                                    | What Was Learned                                                              | Confidence | Revalidation Needed |
|----------|---------------|---------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------|------------|---------------------|
| Jun 2026 | Audit Review  | Inline MUTABLE_HEURISTIC tagging            | Parallel vocabulary — Fallacy 4 risk                           | Epistemic state vocabulary must stay singular across the repository           | Analogous  | No                  |
| Jun 2026 | Audit Review  | 85% consensus threshold from synthesis      | No derivation; false-precision Measured claim                  | Threshold figures without derivation are Placeholder                          | Analogous  | No                  |
| Jun 2026 | Audit Review  | Single-dimension efficiency_delta           | Implied time-only grading; fabrication needs distortion dimension | Multi-dimensional metrics_delta required for Stage 4 Pareto grading        | Analogous  | No                  |
| Jun 2026 | Audit Review  | Pipeline scoped to disassembly only (v0.1)  | Fabrication failures same class; not surfaced by three external reviews | Fabrication failures more dangerous (silent structural failure); must be explicit | Analogous | No            |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### Epistemic State of This Document

Exploration stage. All claims PROVISIONAL / Internally Derived unless otherwise noted. Gate 1 passed this session. Gates 2–6 not yet attempted. CSL-A03, CSL-A05, and CSL-A06 are explicitly Placeholder.

### Gate 1 Audit Record

```
Adversarial Challenge Battery:
- Classes applied: 1 (partial), 3 (partial)
- Classes deferred: 2, 4, 5, 6, 7, 8, 9, 10 — Exploration stage;
  full Battery required at Candidate Spec
- Findings:
    Class 1: CSL-A06 added (simulation fidelity assumption was hidden);
             fabrication failure modes added; NOVEL hard constraint added
    Class 3: CANDIDATE_NOVEL intermediate status added; S2R delta trigger added
- New unknowns: GH-007 through GH-011 (surfaced by multi-agent review)
- Highest-risk finding: CSL-A06 — entire pipeline safety guarantee rests
  on Stage 3 fidelity; assumption was implicit in v0.1

Document: Cognitive_Salvage_Layer.md (Exploration audit, 2026-06-24)
Auditor: Synthesizer/Auditor — Claude
Verification maturity: Exploration
Truth basis: Internally Derived / Analogous External
Adversarial classes applied: 1 (partial), 3 (partial)
Adversarial classes deferred: 2-10 — deferred to Candidate Spec
Highest-risk finding: CSL-A06 simulation-to-physical fidelity implicit in v0.1
Gates cleared: G1, G2, G4, G5, G6
Gates blocked: G3 — full Battery required at Candidate Spec
Unknowns logged: GH-007, GH-008, GH-009, GH-010, GH-011
Overrides: none
Sign-off: v0.2 passes G1 at Exploration stage. Pipeline architecture
internally coherent and Forge-consistent. Five new unknowns logged.
Full Battery deferred to Candidate Spec. No specification-level claims promoted.
```

---

### GH-001 — Heuristic-to-deterministic translation fidelity undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Architectural / Epistemic        |
| Blocking      | Epistemic                        |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** Can player-derived heuristics be reliably translated into deterministic machine procedures? Applies to both disassembly and fabrication — fabrication heuristics (weld path intuition, fixturing feel) may be particularly resistant to decomposition into discrete replayable sequences.

**Resolution Path:** Payment via Specification — requires empirical testing on at least one physical anomaly with logged Stage 1–4 outcomes and post-execution verification. Candidate path: Stage 3 pass → synthetic trajectory → second human cohort validates in simulator → physical promotion. CSL-A02 and CSL-A06 both remain Placeholder until this resolves.

---

### GH-002 — Statistical significance threshold for consensus aggregation undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Governance / Epistemic           |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** How many independent player solutions for the same anomaly class are required before a heuristic pattern is considered statistically meaningful? consensus_run_count tracks this but no threshold is defined.

**Resolution Path:** Payment via Specification — define minimum independent run counts stratified by anomaly class complexity and risk level. Cross-reference EF-0.1 (consensus is not evidence) — threshold must be grounded in physical outcome verification, not run count alone.

---

### GH-003 — Adversarial poisoning of heuristic datasets undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Security / Governance            |
| Blocking      | Epistemic                        |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** Can adversarial players intentionally poison the heuristic dataset with paths designed to pass Stage 1–3 while encoding subtly unsafe sequences that manifest only in physical deployment? Maps to Adversarial Battery Challenge Class 8.

**Resolution Path:** Payment via Specification — adversarial resistance requirements including player session isolation, per-anomaly submission rate limiting, diversity sampling, honeypot anomalies, S2R delta post-execution monitoring, and rollback doctrine. Route to `Admin/Security_Protocols.md`.

---

### GH-004 — Optimal abstraction level for heuristic preservation undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Architectural                    |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-08-03                       |

**Description:** What abstraction level preserves useful human intuition while remaining computationally tractable? The typed action_sequence operates at operation level. Whether this is sufficient is untested.

**Resolution Path:** Payment via Specification — define abstraction hierarchy: Strategic (goal/sequence), Operational (current typed schema), Tactical (tool-path vectors). Store multiple levels when possible. GH-011 (canonicalization) partially addresses this.

**Canonicalization envelope (Payment via Specification, added 2026-08-03 — human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** independent of which abstraction hierarchy above is eventually adopted, any canonicalization pass needs a hard constraint on what it may alter: **allowed** — removal of redundant actions, normalization of syntactically equivalent sequences that produce identical Stage 3 outcomes; **forbidden** — removal or reordering of any action that alters Stage 3 outcomes (kinematic, stress, or metrics_delta results). Verification method (unexecuted): run Stage 3 on both the original and candidate canonicalized sequence, require identical outcomes within the same `simulation_fidelity_version`. This defines a testable envelope, not an abstraction level — it constrains GH-011's eventual implementation regardless of which hierarchy tier that implementation targets. Placeholder / Internally Derived. Does not resolve GH-004 or GH-011.

---

### GH-005 — Human vs. autonomous intervention fraction undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Low                              |
| Priority      | Minor                            |
| Type          | Operational                      |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** What fraction of edge-case triage and fabrication problems actually benefit from human heuristic intervention compared to extended autonomous planning time?

**Resolution Path:** Discharge via Trajectory if first Leviathan deployment data not available within current development phase.

---

### GH-006 — NOVEL promotion threshold undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Governance                       |
| Blocking      | Epistemic                        |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** NOVEL status requires a formal multi-dimensional threshold. No heuristic may receive NOVEL status until this resolves — enforced via CANDIDATE_NOVEL and hard constraint in Grading Matrix.

**Resolution Path:** Payment via Specification — define NOVEL threshold after first operational cycle data. Must be multi-dimensional (time, tool wear, material yield, distortion risk). Cross-reference `Economics.md`.

---

### GH-007 — Puzzle fidelity drift undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Architectural / Governance       |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** Over time the puzzle engine may diverge from actual Forge machinery. If physical tooling geometry changes but the puzzle engine still models old geometry, players optimize for a machine that no longer exists. This could silently poison the heuristic pipeline — promoted heuristics pass all four stages internally consistent with the simulation, while diverging from physical reality.

**Why It Matters:** Silent pipeline poisoning is the highest-severity failure mode for this architecture. A heuristic valid under engine version A may be KINEMATIC_MISMATCH or UNSAFE under physical machinery updated to version B.

**Resolution Path:** Payment via Specification — puzzle engine configuration hashes tied to machinery revision IDs. When machinery revision increments, all FEASIBLE and CANDIDATE_NOVEL heuristics for affected anomaly classes are demoted to PENDING_REVALIDATION and must pass Stage 2 kinematic mapping against the new machinery model before reinstatement. The `simulation_fidelity_version` and `validated_on_machinery_revision` schema fields support this.

**Trajectory note:** If the canonicalization layer (GH-011) matures into a dedicated subsystem, the fidelity drift detection logic may warrant its own file — `Architecture/Cognitive_Canonicalization.md` is a candidate home. Flag for Candidate Spec review.

*Surfaced by Gemini review, 2026-06-24.*

---

### GH-008 — Heuristic expiration doctrine undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Governance                       |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** Heuristics in the knowledge base are currently treated as persistent. A procedure valid on Spin Chamber revision SC-3 may be invalid on SC-4 if tooling geometry changed. The `validated_on_machinery_revision` field exists but no expiration doctrine governs what happens when the revision increments.

**Resolution Path:** Payment via Specification — when machinery revision increments, flag all heuristics whose `validated_on_machinery_revision` does not match current revision as PENDING_REVALIDATION for affected anomaly classes. Define revalidation pathway (Stage 2 kinematic re-run minimum; Stage 3 re-run if tooling geometry materially changed). Cross-reference GH-007.

*Surfaced by Gemini review, 2026-06-24.*

---

### GH-009 — Emergent heuristic conflict undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Critical                         |
| Priority      | Major                            |
| Type          | Architectural / Safety           |
| Blocking      | Epistemic                        |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** The current architecture evaluates heuristics independently. Two heuristics that each pass all four stages in isolation may interact catastrophically when applied in sequence. Example: Heuristic A changes load-bearing fastener removal order; Heuristic B changes fluid drain sequence. Applied together, the combined sequence creates a structural collapse scenario neither triggers individually.

**Why It Matters — elevated to Critical:** The interaction surface grows approximately as N² where N is the count of promoted heuristics. At 10 heuristics: 45 pairwise interactions. At 100: 4,950. At 1,000: 499,500. The risk scales faster than repository size. This is a hallmark of a future unmanageable problem if architectural countermeasures are not defined early. A Heuristic Dependency Graph or Heuristic Compatibility Matrix will likely be required to keep the interaction space tractable as the knowledge base matures.

**Resolution Path:** Payment via Specification — define a compositional verification pass using risk-stratified interaction testing: run full interaction matrix on high-risk anomaly classes (pressure vessels, load-bearing structures) initially; use sampling for lower-risk classes. Define Interaction Volume per heuristic (spatial and temporal envelope of tools and materials involved) — if a new heuristic's Interaction Volume overlaps with an existing one, Stage 3 simulation must run them concurrently before co-deployment is permitted. Resolution path must also define the scope boundary for what constitutes an overlapping sequence.

*Surfaced by Gemini review, 2026-06-24. Elevated to Critical 2026-06-24 — N² interaction scaling.*

---

### GH-010 — Simulator overfitting undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Architectural / Epistemic        |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** A player swarm may become experts at the game rather than experts at salvage. Over time participants discover scoring exploits, simulator biases, and reward hacks without realizing it. The pipeline begins harvesting simulator expertise instead of physical expertise. Distinct from GH-003 (adversarial poisoning) — GH-010 occurs accidentally through natural optimization behavior.

**Why It Matters:** Simulator overfitting produces a pipeline that appears healthy (high FEASIBLE rate, low EXPLOIT rate) while progressively degrading in physical relevance. The degradation is invisible until physical deployment reveals promoted heuristics performing worse than the autonomous baseline.

**Resolution Path:** Payment via Specification — define simulator diversity maintenance: periodic injection of novel anomaly classes to prevent player population over-specialization; monitoring of FEASIBLE-to-physical-outcome correlation rate as primary health signal; mandatory puzzle engine updates at defined intervals. Cross-reference GH-007 — fidelity drift and overfitting interact; a simulator that both drifts from physical reality and attracts overfitted players produces doubly degraded heuristics.

*Surfaced by Gemini review, 2026-06-24.*

---

### GH-011 — Heuristic canonicalization layer undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Architectural                    |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-06-24                       |

**Description:** Human solutions to the same core problem are noisy. One player executes A→B→C→D; another A→X→B→C→D where X is irrelevant. Without normalization, the knowledge base accumulates thousands of variants of the same insight. This inflates consensus_run_count without adding genuine evidential weight and makes GH-002 (statistical significance threshold) harder to evaluate meaningfully.

**Resolution Path:** Payment via Specification — define canonicalization algorithm: input is a set of Heuristic Objects for the same anomaly class; output is a Canonical Heuristic with confidence score derived from variant count and diversity. Canonical form operates at Strategic abstraction level (GH-004); variant sequences retained as evidence. This is a pre-Stage-1 pass — canonically identical variants are merged before entering the Auditor pipeline rather than passing through four stages independently.

*Surfaced by third-party architectural review, 2026-06-24.*

---

### GH-012 — Discovery yield rate undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Operational / Governance         |
| Blocking      | No                               |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                       |
| Last Reviewed | 2026-08-03                       |

**Description:** What percentage of harvested heuristics are genuinely novel? This is distinct from GH-005 (how often are humans needed). GH-005 asks how frequently the pipeline is invoked. GH-012 asks how often invocations produce new knowledge. A system might require human intervention frequently while producing very little novel knowledge, or rarely while producing extremely valuable breakthroughs. The ratio determines the actual return on investment of the layer and whether Cognitive Salvage functions as a high-value augmentation or an expensive edge-case handler. Without this metric, the pipeline cannot demonstrate its own effectiveness — a recursive justification problem (Adversarial Battery Challenge Class 6).

**Why It Matters:** If 100,000 player solutions produce 99,900 duplicates, 99 improvements, and 1 breakthrough, the economics and operational posture of the layer look entirely different than 100,000 solutions producing 5,000 useful improvements. That ratio also determines how aggressively the Leviathan emergency cognition pathway should be pursued versus alternative approaches. This unknown is the primary ROI signal for the entire layer.

**Resolution Path:** Payment via Specification — define a discovery yield rate metric as part of the AP-001 audit effectiveness metrics pass (once that entry matures). Minimum: track CANDIDATE_NOVEL rate as a fraction of total FEASIBLE completions per anomaly class, stratified by anomaly complexity. Cross-reference AP-001 (audit effectiveness metrics) — discovery yield rate is a candidate indicator for that entry's eventual indicator set, subject to EF-0.6 (must remain an indicator, not an optimization target). A pipeline optimized to maximize discovery yield rate rather than genuine novelty detection would produce exactly the epistemic corruption it was designed to prevent.

**Baseline ratio (Payment via Specification, added 2026-08-03 — human-directed, corrective merge from a Copilot/Grok exchange, see AP-033):** the simplest possible version of this metric, useful as a coarse baseline before the stratified CANDIDATE_NOVEL-rate version above matures: YieldRate = (heuristics graded FEASIBLE) / (total heuristic submissions), computed per `anomaly_class`. Required artifact if adopted: a `DiscoveryYieldReport` per deployment cycle (fields: anomaly_class, total_submissions, feasible_count, yield_rate, reporting_period). Placeholder / Internally Derived — no numerical target asserted, no collection has occurred. This is a coarser, earlier-available companion metric, not a replacement for the stratified version above.

*Surfaced by Gemini review, 2026-06-24.*

---

### GH-013 — Conceptual salvage artifact storage mechanism undefined

| Field         | Value                            |
|---------------|-----------------------------------|
| Status        | Open                             |
| Risk          | Low                               |
| Priority      | Minor                             |
| Type          | Architectural                     |
| Blocking      | Yes — blocks the Conceptual Salvage Pipeline subsection from advancing past Exploration-within-Exploration |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-07-12                       |
| Last Reviewed | 2026-07-12                       |

**Description:** The Conceptual Salvage Pipeline (Body, above) has no defined object schema, storage location, or data structure for the knowledge and investigative pathways it would recover. The existing Heuristic Object schema (`The Heuristic Object Schema`, Body) is built entirely around physical grounding fields — action_sequence, metrics_delta, simulation_fidelity_version, validated_on_machinery_revision — none of which have a meaningful value for an artifact that started as fiction or speculation and was never a physical action.

**Why It Matters:** Without a defined storage mechanism, the Conceptual Salvage Pipeline is a description of an idea, not a specified process — it cannot actually recover anything, because there's nowhere for a recovered pathway to go. This is the primary blocker for the entire subsection moving beyond provisional status. Risk is rated Low (this is an architectural gap, not a safety or integrity exposure), but Priority is Minor-but-Blocking specifically for this subsection's own advancement, not for the file as a whole.

**Resolution Path:** Not yet defined. Candidate questions to resolve before a schema can be proposed: Does this warrant its own object type analogous to but structurally distinct from the Heuristic Object, or a different mechanism entirely (e.g., routing directly into `Unknowns.md` as a differently-flavored entry, or a dedicated companion file)? What replaces `validated_on_machinery_revision` as the artifact's "is this still current" check, given there's no machinery to revise against? Does Canonical_Terms.md need a new term for this artifact type, distinct from "Heuristic"? This is deliberately left open rather than guessed at — same posture this file already took with GH-011 (canonicalization) before that unknown had enough real usage to design against.

---

### Resolution Log

- 2026-06-24: **v0.1 initial draft.** File created at Exploration stage. GH-001 through GH-006 registered. Inline compilation tags and LayerMD structure abandoned. File registered in Discovery.md and Unknowns.md.
- 2026-06-24: **v0.2 — Gate 1 pass.** Fabrication heuristics added throughout (Scope Boundary, File Purpose, Heuristic Failure Class, Core Data Streams, Stage 3, Integration Points). Heuristic Object schema updated: typed action_sequence, metrics_delta (replaces efficiency_delta), candidate_novel_flag (replaces novelty_flag), simulation_fidelity_version, validated_on_machinery_revision, physical_grounding_ref. CANDIDATE_NOVEL status added to Grading Matrix with Pareto criterion and GH-006 hard gate. CSL-A06 added (simulation-to-physical fidelity — load-bearing Placeholder). S2R delta trigger added to Stage 3. Canonicalization pass noted in pipeline. HF-001 Canonical Terms registration proposed. GH-007 through GH-011 registered. Gate 1 passed (G1, G2, G4, G5, G6 clear; G3 partial — full Battery deferred to Candidate Spec). Open Unknowns 6 → 11. Spec Gates 0/6 → 1/6. Unknowns.md requires update: GH-007 through GH-011 global index registration.
- 2026-06-24: **v0.3 — sidecar triage and schema polish.** GH-009 elevated to Critical (N² interaction scaling argument; resolution path hardened with Interaction Volume and risk-stratified testing). GH-007 Trajectory note added (Cognitive_Canonicalization.md candidate at Candidate Spec). GH-012 registered (discovery yield rate — primary ROI signal for layer; cross-reference AP-001). Schema: provenance_trust_tier subfield added (stratified trust tier for differentiated Auditor handling); failure_modes_observed array added (negative learning from Stage 3 failures and player constraint violations). Open Unknowns 11 → 12. Highest Risk remains High (GH-009 Critical elevates sidecar but file-level risk was already High). Unknowns.md requires update: GH-009 Critical elevation, GH-012 global index registration. AUDIT_HARNESS.py UNKNOWN_FIRST_CYCLE requires GH-012 at cycle 10.
- 2026-07-12 (first entry, same day): **Template-skeleton restructure, no content removed.** Added missing Navigation Anchors block (previously entirely absent). Wrapped the Heuristic Failure Class through Integration Points sections under a new `## Body` header. Folded "Relationship to Existing Documents" and the "What must remain constant" invariant into Body as subsections rather than leaving them as top-level non-canonical headers. Moved "Epistemic State of This Document" and "Gate 1 Audit Record" into `## Auditor Notes & Unknowns` as introductory subsections — they're audit-record content, which is what that section exists for. Dropped the standalone "## Status" header's version-summary line as a duplicate of this Resolution Log's own v0.3 entry above; kept its invariant statement in Body. Added an explicit (empty) Active Disputes section, matching File State's already-accurate "Active Disputes: 0". Reordered Abandoned Paths and Drift Indicators to the end of the file, after Auditor Notes & Unknowns, per template order — they previously sat before Lessons Learned.
- 2026-07-12 (second entry, same day): **v0.3.1 → v0.4 — Conceptual Salvage Pipeline added as a provisional Body subsection.** Origin: James's illusion-power RPG character example (optical-illusion constraint → optics study → wavelength curiosity → laser interest), discussed with ChatGPT and documented on r/InnovativeAIChats, 2026-07-12. Explicitly marked Exploration-within-Exploration and not yet Gate 1-reviewed — this is a proposed second pipeline (conceptual/idea salvage), structurally distinct from the existing physical Heuristic Failure Class pipeline, not a variant of it. A comparison table makes explicit which existing stages (Kinematic Mapping, Simulation) have no equivalent for non-physical input. The working principle ("every idea is provisional feedstock...") is recorded as provisional, not ratified doctrine. GH-013 registered for the storage/object-schema gap this subsection cannot resolve on its own — marked Blocking specifically for this subsection's advancement, not for the file as a whole. Open Unknowns 12 → 13. *(Correction, 2026-07-19: this entry originally said "Unknowns.md requires update: GH-013 global index registration (joins GH-007 through GH-012 already outstanding there)" — stale on arrival. GH-007 through GH-012 were already registered in `Unknowns.md` since v4.1 (2026-06-24), and GH-013 itself was registered the same day as this entry, per `Unknowns.md` v4.18. Nothing was actually outstanding.)*

---

- 2026-08-03: **Corrective merge — AP-033, human-directed.** A Copilot
  proposal series, produced with no confirmed access to this file's
  sidecar or `Admin/Auditor_Protocols.md`, declared 16 of this file's
  unknowns "CLOSED" purely by describing methodology, with zero
  empirical work behind any of them — including CSL-A06, this file's
  own named load-bearing assumption. It also mis-enumerated this
  file's own unknown set: never mentioned GH-005 (a real entry
  registered since v0.1), and invented a nonexistent "GH-014" to pad
  the count back to 13. None of that was merged — see AP-033 in
  `Admin/Auditor_Protocols.md`'s sidecar for the full account and the
  resulting Rule 9. A second agent (Grok), with confirmed access,
  correctly diagnosed every violation and produced a clean rewrite
  restricted to genuine Payment via Specification. Checked that
  rewrite against what this file already had before merging anything:
  three entries (GH-004, GH-012, CSL-A03) gained genuinely
  complementary elaboration — a canonicalization envelope constraint
  for GH-004, a simpler baseline yield ratio alongside GH-012's
  existing stratified metric, and a concrete Δ_physical test for
  CSL-A03's existing expiry trigger — all explicitly marked Placeholder
  / Internally Derived, none changing Status or Open Unknowns. Four
  entries (GH-007, GH-008, GH-009, GH-011) already had more specific,
  better-grounded resolution paths than the proposal series offered
  (GH-007 and GH-008 already tie to the real `simulation_fidelity_
  version`/`validated_on_machinery_revision` schema fields; GH-009
  already defines Interaction Volume, more concrete than a generic
  interaction matrix; GH-011 already specifies a pre-Stage-1 merge
  pass) — the proposal's versions of these would have been a downgrade
  if merged, so they weren't. CSL-A05's existing expiry trigger already
  matched the proposal exactly (dependent on GH-003) — nothing to add.
  Open Unknowns unchanged at 13. Status/Spec Gates unchanged
  (Exploration, 1/6).

## Abandoned Paths

| Date      | Path                                                     | Why Abandoned                                                              | Reconsider? |
|-----------|----------------------------------------------------------|----------------------------------------------------------------------------|-------------|
| Jun 2026  | Inline compilation tags (MUTABLE_HEURISTIC, UNCERTAINTY) | Parallel epistemic vocabulary — immediate Fallacy 4 drift risk             | No          |
| Jun 2026  | 85% consensus threshold                                  | Unlabeled Placeholder; false-precision Measured claim                      | Placeholder — see GH-002 |
| Jun 2026  | LayerMD structural template                              | Hallucinated framework; not consistent with File_Template.md               | No          |
| Jun 2026  | Flat action_sequence array (v0.1)                        | Insufficient for kinematic replay and canonicalization                     | No          |
| Jun 2026  | efficiency_delta single-dimension field (v0.1)           | Implied time-only grading; replaced with metrics_delta                     | No          |
| Jun 2026  | novelty_flag boolean (v0.1)                              | Risk of accidental NOVEL promotion; replaced with candidate_novel_flag     | No          |

---

## Drift Indicators

- Auditor Decision Tree stages modified without cross-referencing `Admin/Auditor_Protocols.md`
- NOVEL status assigned to any heuristic before GH-006 closes
- CANDIDATE_NOVEL used as a promotion pathway rather than a hold status
- Grading matrix status codes diverge from Auditor_Protocols.md epistemic state vocabulary
- Heuristic Object schema fields changed without version bump and migration note in Resolution Log
- Integration point references to planned files promoted from *planned* to confirmed without Discovery.md update
- GH-series unknowns closed without documented Resolution Path
- Physical test results logged without updating CSL-A02, CSL-A03, CSL-A06 confidence fields
- S2R delta threshold hardcoded without logged derivation
- Fabrication heuristic pipeline extended into weld qualification or tolerance specification (→ Gate_06_Fabrication.md)
- Leviathan integration section expanded into architecture specification before `Operations/Leviathan.md` exists
- Ethical Anchor field absent, altered, or not matching canonical string
- validated_on_machinery_revision not updated when Forge machinery revision increments
