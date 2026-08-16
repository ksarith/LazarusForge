# Canonical_Terms.md — Standard Repository Nomenclature
**Version 0.7**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-07-05                                                          |
| Auditor          | Claude — Synthesizer/Auditor (2026-06-24); Claude — Cycle definition + version-string correction (2026-07-05); Claude — CT-011 resolution 2026-07-05 |
| Open Unknowns    | 9                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Authoritative vocabulary mappings for system architecture, hardware
  structures, and governance layers
- Conflict resolution rules between this file and other vocabulary sources
- Strict semantic boundaries to enforce consistency and prevent definition
  creep across multi-agent cycles
- Anti-drift guardrails: terms explicitly banned from specification drafts
  and their approved replacements
- Disambiguation of overloaded uses of "canonical" within the repository

**This file DOES NOT define:**
- Individual component blueprints or dimensional specifications
- Specific programmatic API schemas or cryptographic algorithms
- Ethical policy constraints — governed by `Admin/Ethical_Constraints.md`
- Operational routing semantics — governed by `Architecture/Forge_flow.md`;
  where definitions conflict, Forge_flow.md is authoritative for operational
  routing until reconciliation occurs and is logged here
- Governance tier authority — governed by `Admin/Governance_Charter.md`;
  tier definitions here are derived from that source and must remain
  consistent with it
- Filename resolution for renamed or legacy files — governed by the
  Rename Registry in `Discovery.md`

---

## File Purpose

This document provides a single source of truth for repository nomenclature.
In a distributed multi-agent workflow, semantic drift is an institutional
vulnerability. Subtle rewordings across different sessions can introduce
cascading misinterpretations of architectural logic, gate routing decisions,
and governance authority claims. This file locks down vocabulary, explicitly
draws lines where terms diverge, and bridges historical code artifacts with
current structural architecture.

**Relationship to other vocabulary sources:** This file does not replace
`Architecture/Forge_flow.md` as the operational vocabulary reference standard.
Forge_flow.md governs how terms are used in routing decisions and gate logic.
This file governs cross-file consistency and prevents semantic drift in
documentation, governance, and audit contributions. The two are complementary.
Conflicts between them must be resolved through reconciliation logged here,
not by either file silently overriding the other.

**Relationship to Archive/Rename_Registry.md:** The Rename Registry in
`Archive/Rename_Registry.md` is the canonical source for legacy filename resolution.
This file does not duplicate or supersede that function. CT-001 tracks
alignment between this file's vocabulary and AUDIT_HARNESS.py internal
string references — that is a distinct function from filename aliasing.

---

## Assumptions

| ID      | Assumption                                                                          | Basis                              | Confidence | Expiry Trigger                                             |
|---------|-------------------------------------------------------------------------------------|------------------------------------|------------|------------------------------------------------------------|
| ASM-001 | A standard lexicon mitigates token inflation and multi-agent misinterpretation      | Observed multi-agent drift patterns| High       | Single-agent workflow formally adopted                     |
| ASM-002 | Contributors will query this file before promoting files with new terminology       | Governance discipline assumption   | Medium     | Automated terminology check implemented in AUDIT_HARNESS.py|
| ASM-003 | Forge_flow.md remains the authoritative operational routing vocabulary reference    | Scope boundary discipline          | High       | Forge_flow.md scope boundary revised                       |
| ASM-004 | Governance_Charter.md tier definitions remain the authoritative tier structure      | Constitutional hierarchy           | High       | Governance_Charter.md tier structure formally revised      |

---

## Conflict Resolution Doctrine

**This section governs how terminology conflicts are resolved.**

Three vocabulary sources exist in the repository:

| Source                       | Authority Domain                                      |
|------------------------------|-------------------------------------------------------|
| `Architecture/Forge_flow.md` | Operational routing semantics; gate logic vocabulary  |
| `Admin/Governance_Charter.md`| Governance tier definitions; constitutional vocabulary|
| `Admin/Verification_Gates.md` | Document promotion vocabulary; Verification Gate definitions |
| `Admin/Canonical_Terms.md`   | Cross-file consistency; anti-drift enforcement        |

**Resolution rules:**

1. If this file conflicts with `Architecture/Forge_flow.md` on operational
   routing vocabulary, Forge_flow.md is authoritative. Log the conflict
   as an Active Dispute here and initiate reconciliation.

2. If this file conflicts with `Admin/Governance_Charter.md` on governance
   tier definitions or constitutional vocabulary, Governance_Charter.md
   is authoritative. Log the conflict as an Active Dispute here and
   initiate reconciliation.

3. If this file conflicts with `Admin/Verification_Gates.md` on
   Verification Gate definitions or document-promotion vocabulary,
   Verification_Gates.md is authoritative. Log the conflict as an
   Active Dispute here and initiate reconciliation. Added 2026-07-03 after
   this file failed to catch a real divergence between Verification Gates
   and Governance_Charter.md's (then-named) "Canonical Verification Gates"
   because Verification_Gates.md was never registered as an authority
   source — see GOV-011, CT-010.

4. If this file conflicts with `Discovery.md` Rename Registry on filename
   resolution, Discovery.md is authoritative. Log the conflict here.

5. For all other vocabulary conflicts between repository files, this file
   is the resolution authority. Agents encountering conflicting terminology
   in non-authoritative files should flag the conflict and route to this
   file for resolution.

Conflicts must be logged — silent divergence is drift. Logged divergence
is a reconciliation task.

---

## Disambiguation: Uses of "Canonical"

The term "canonical" appears in multiple distinct contexts within the
repository. These are not interchangeable:

| Usage                     | Meaning                                                        | Example                                                                 |
|---------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------|
| Canonical File            | The authoritative source document for a governed concept       | `Admin/Governance_Charter.md` is the canonical governance authority     |
| Canonical Term            | An approved vocabulary entry defined in this file              | "Material Recovery" is the canonical term for post-triage feedstock     |
| Canonical Cross-Reference | A file reference that resolves against Discovery.md confirmed list using folder-prefixed paths | `Operations/Gate_03_Reduction.md` not `Gate_03_Reduction.md` |
| Canonical Mapping         | A legacy-to-current filename resolution entry in Archive/Rename_Registry.md | `Spin_Chamber_v0.md` → `Operations/Gate_05_Separation_Thermal.md` |
| Canonical Path            | The folder-prefixed file path used in all new contributions    | `Admin/Ethical_Constraints.md` not `Ethical_Constraints.md`            |

Agents must not treat these as synonymous. "Canonical" without qualification
is ambiguous — use the specific form.

---

## Body: Canonical Nomenclature Mapping

### 1. Architectural and Repository Structural Terms

**Active Working Repository**
The lean, operational environment (`LazarusForge`) containing functional
specification files, active gate validations, and localized sidecars.
Distinct from the companion doctrine repository.

**Companion Doctrine Repository**
The upstream repository (`Lazarus-Forge-`) dedicated exclusively to
macro-philosophy, abstract doctrine development, and baseline structural
principles. Divergence between the two repositories is logged, not ignored.

**`[ExternalRepo]` reference convention (registered 2026-08-11)**
Any cross-reference to a file in a companion or external repository (e.g.
Astroid-miner) that is not part of this repository's own canonical registry
must be qualified with a bracketed repository tag immediately before the
filename, with the bracket tag included **inside the same single
backtick pair** as the filename — e.g. `` `[Astroid-miner] Rogue_unit_management.md` ``,
not `` [Astroid-miner] `Rogue_unit_management.md` `` (tag outside the
backticks). This is not cosmetic and the two forms are not interchangeable:
`Automation/audit_lib.py`'s reference extractor only matches a pattern
requiring the character immediately after an opening backtick to be a
letter (`` `([A-Za-z][A-Za-z0-9_/]+\.md)` ``) — a bracket in that position
breaks the match entirely, so the whole qualified span is correctly never
extracted as a reference at all. Putting the tag *outside* the backticks
leaves the bare `` `filename.md` `` span intact and still matching,
which still trips an `[UNKNOWN]` finding — confirmed by directly testing
both forms against the live extraction regex. `check_cross_refs` also has
a separate, independent substring-based skip for any *extracted* ref
containing a known external-repo name, but that skip is redundant here in
practice since the correct form is never extracted in the first place.
First applied and debugged live in `Admin/Autonomy_Divergence_Protocol.md`
(2026-08-11, Resolution Log — two passes; the first attempt used the
bracket-outside-backticks form and did not clear the harness).

**Governance Tier Hierarchy (Tiers 1–5)**
The structural precedence rules governing documentation authority.
Derived from `Admin/Governance_Charter.md` §Governance Authority Hierarchy —
that document is authoritative; definitions here must remain consistent with it.

- *Tier 1 (Constitutional Layer):* `Admin/Governance_Charter.md` and
  `Admin/Ethical_Constraints.md`. Defines inviolable primitives (Tier 1 Axioms).
  Any reasoning path attempting to override Tier 1 triggers STATE_HOLD.
- *Tier 2 (Canonical Verification Doctrine):* `Admin/Auditor_Protocols.md`.
  Defines auditor role execution, checklist adherence, and verification sequences.
- *Tier 3 (Audit Operationalization):* `Admin/Forge_Audit_Kit.md`. Condensed
  cross-module indexes, Verification Maturity Model, and Audit Opening Checklist.
  Derived from Tier 2 — may not outrank its source.
- *Tier 4 (Dynamic Procedures):* Operational checklists, adversarial batteries,
  and execution procedures. Governed by Tier 2 and 3 doctrine.
- *Tier 5 (Domain Specifications):* Highly specific technical documents detailing
  individual gates, materials, or scripts — e.g., `Operations/Gate_03_Reduction.md`,
  `Automation/AUDIT_HARNESS.py`, `Architecture/Forge_flow.md`.

**Sidecar Model**
The decentralized documentation practice where module-specific unknowns,
audit notes, and resolution logs reside in the `## Auditor Notes & Unknowns`
footer of their owning document rather than in a central master tracker.
Cross-module unknowns are indexed in `Unknowns.md` — summary only; full
entry detail remains in the owning file sidecar.

**STATE_HOLD**
The mandatory halt condition triggered when any reasoning path attempts to
recurse beneath, redefine, or override Tier 1 Axioms, or when a Constitutional
integrity violation is detected. Requires human review before any autonomous
action resumes. Defined in `Admin/Governance_Charter.md`.

---

### 2. Operational Flow and Material States

Terms in this section are derived from `Architecture/Forge_flow.md`, which
is the authoritative operational routing reference. Definitions here serve
cross-file consistency. If a conflict exists between this section and
Forge_flow.md, Forge_flow.md governs.

**Intake (Gate_01)**
The system's initial inspection and verification vector. Responsible for
primary hazard containment (energetic, chemical, biological, radiological),
digital screening, provenance recording, and initial object categorization.
Items enter here; nothing bypasses this gate.

**Triage (Gate_02)**
The progressive, non-destructive routing logic evaluating whether a component
preserves functional value over material reduction. Five-station workflow.
The Forge preserves embedded industrial capability, not just metal.

**Reduction (Gate_03)**
The fully irreversible mechanical processing step where structural complexity
is disassembled into bulk feedstock. The only irreversible step in the flow.
Three hard prerequisites before operation: Air Scrubber operational, human
operator present, no energetic materials remaining.

**Separation — Mechanical (Gate_04)**
Pre-thermal mechanical decision point operating after Reduction and before
thermal processing. Diverts recoverable material away from the thermal stage
using centrifugal separation and dual-channel sensor cross-check. Defined by
its position in the flow (pre-thermal diversion) and its refusal-first
fail-to-bin protocol. Target: ≥30% material diversion rate.
*Note: Gate_04 is distinct from the Spin Chamber (Gate_05). Gate_04 operates
on bulk reduced material before the melt. Do not describe Gate_04 using
"high-RPM" as a defining characteristic — that term belongs to Gate_05.*

**Separation — Thermal (Gate_05)**
High-temperature crucible processing where distinct material classes are
liquefied via induction heating, separated via slow rotation and MHD damping,
and extruded into ranked material streams. Also referred to as the Spin Chamber.
Produces useful gradients, not pure metal. The RPM envelope is a defining
operational parameter here — not in Gate_04.

**Fabrication (Gate_06)**
The reconstructive process transforming categorized feedstock into functional
physical assets. Arc welding is the v0 proof-of-concept gatekeeper.
Add-to-excess and mill-to-spec is the primary dimensional control philosophy.

**Utilization (Gate_07)**
The field-deployment and after-action-review phase. Where fabricated outputs
operate within standard environments while streaming lifecycle durability and
failure telemetry back into triage loops. A part in service without a
utilization record is an opportunity lost.

**Value Preservation**
The correct taxonomy for early-stage triage processes where functional
components are identified and routed away from reduction. Replaces "Recycling"
in this context. Use when the component retains functional identity.

**Material Recovery**
The correct taxonomy for bulk reduced feedstock bound for geometric processing.
Replaces "Recycling" in this context. Use when structural complexity has been
reduced and the material is being recovered as raw stock.

**Forge Regeneration Threshold (FRT)**
The minimum fraction of material throughput value that must be reinvested in
Forge capability development per operating cycle. A survival metric, not an
efficiency metric. Defined in `Admin/Trajectories.md`.

---

### 3. Deep-Ocean and Marine Subsystems

**Leviathan Framework**
A dedicated, hostile-environment operational filter designed to falsify
autonomy assumptions under real-world pressures before off-world deployment.
A testing methodology, not a commercial product line. Survival is optional.
Understanding is not.

**Support Raft**
A stationary regional operational anchor deployed to offload infrastructural
weight, power accumulation, and data processing overhead from adjacent mobile
swarms. The Raft does not migrate — it remains fixed to optimize stationary
energy collection and mitigate biofouling. Its value is measured by what it
enables in mobile units, not what it does directly.

**Shell Cycle**
The deliberate material swap protocol where regional anchors exchange modular
structural skins or surface panels to maximize operational lifecycle against
calcification or corrosion pressure.

---

### 4. Governance and Audit Terms

**Exploration / Draft / Specification**
The three primary file status designations. Exploration: incomplete by design,
do not over-police. Draft: active convergence toward Specification underway.
Specification: all gates passed, claims binding until revised through full
audit cycle. Defined in `Admin/File_Template.md`.

**Verification Maturity Model**
Five-state maturity progression from Exploration through Hardened Doctrine.
Distinct from the three-state Status field. Defined in `Admin/Forge_Audit_Kit.md`.

**Verification Gate**
One of the six criteria (Fallacy Checklist, Physical Plausibility, Adversarial
Battery, Scope Alignment, Cross-reference Integrity, Conflict Check) a
*document* must satisfy to advance toward Specification status. Defined and
owned exclusively by `Admin/Verification_Gates.md`. A file's `Spec Gates
X/6` File State field always refers to these gates and to no other system,
regardless of which document the field appears in. Not to be confused with
Enforcement Checkpoint (below) or the Operations/Gate_01–07 physical
material-flow pipeline stages (owned by `Architecture/Forge_flow.md` —
distinct concept, same word, unrelated to document promotion).

**Enforcement Checkpoint**
One of six criteria (Internal Coherence, Structural Plausibility, Adversarial
Pass, Cross-Module Integration, Truth Provenance Layering, Audit Lineage
Integrity) a *governance action* must satisfy to be constitutionally sound.
Defined and owned exclusively by `Admin/Governance_Charter.md` §Enforcement
Checkpoints. Renamed 2026-07-03 from "Canonical Verification Gates" — the
prior name collided with Verification Gate (above), causing an undocumented
divergence where the two systems were referenced interchangeably despite
testing different objects (a governance action's legitimacy, not a
document's promotion readiness). See GOV-011. Never appears in a file's
`Spec Gates X/6` field — that field is reserved for Verification Gates only.

**Full Stop Review**
A reset to Verification Gate 1 (Fallacy Checklist) triggered when a
specification passes all six Verification Gates but exhibits systemic
inconsistency or unclear real-world viability, or when specific trigger
conditions defined in `Admin/Auditor_Protocols.md` are met.

**Cycle (Governance / Audit Cycle)**
The time unit against which Expiry Watch, the Expiry Rule, Systemic Risk
escalation, and all "N cycles open" language are measured. **Default: one
calendar year**, declared by human governing authority (ksarith) 2026-07-05
at current operating pace. The human governing authority may declare a
shorter interval at their own discretion as automation, throughput, or
operational maturity increases — this is an operator-adjustable parameter,
not a fixed constant, and any change should be logged here with the date
and rationale. Absent an explicit shorter declaration, one calendar year
applies repository-wide to every file that references "audit cycle" or
"cycle" without its own more specific definition.

This definition exists because none previously existed: `Admin/Auditor_
Protocols.md`'s own text (§Expiry Rule, §Expiry check) operationally treated
a "cycle" as *each time the Skeptic/Auditor role opens* — i.e., each audit
pass, not a fixed duration. Under that reading, two independent same-day
audits already satisfy a "2-cycle" expiry threshold regardless of real
elapsed time, which produced escalation language ("6 cycles open," "8-cycle
threshold exceeded") far outpacing actual operational aging. This entry
supersedes that reading for elapsed-time purposes; per-audit-pass counting
may still be useful for other doctrine (e.g., AP-017's independence
requirement) and is not banned, but it may not be conflated with the
calendar-time "cycle" used for Expiry Watch aging without saying so
explicitly. See CT-011 for propagation status into Auditor_Protocols.md's
own text.

**Distinct from:** `Admin/Trajectories.md`'s Forge Regeneration Threshold
"operating cycle" (material throughput/reinvestment measurement — see TR-002),
which remains its own separately-declared placeholder and is not resolved
by this entry. The two concepts share a word, not a definition — do not
assume they're interchangeable.

**Expiry Rule**
The governance requirement that Blocking or Non-blocking unknowns without a
documented Resolution Path for more than two audit cycles escalate to Systemic
Risk or trigger demotion of the dependent module. Checked at audit opening.
"Audit cycles" here means Cycle (above) — one calendar year by default, not
one audit pass.

**Genesis Phase**
The bootstrap governance period before a minimum multi-agent quorum is
established. During Genesis Phase, human operators serve as the independent
verification anchor. Genesis Phase must have a declared exit condition and
must not silently become permanent operating mode. Defined in
`Admin/Governance_Charter.md`.

**Operational Blocking**
An unknown or condition that stops a physical action from occurring safely.
The gate holds until empirical or physical resolution is achieved —
documentation advancement alone is insufficient. Examples: no excavation
without geomechanical assessment (SD-UNK-004); no hot pyrolysis run before
halogenated polymer triage protocol is validated (PL-001); no powered machinery
contact with raw urban salvage before IFM screening is confirmed (WW-005).
Operational Blocking unknowns require physical or empirical resolution — they
cannot be worked around by grounding a claim in better documentation. Defined
as a priority subtype in `Admin/Auditor_Protocols.md` Priority Demotion Doctrine.

**Epistemic Blocking**
An unknown or condition that stops a claim from being made or a file from being
promoted, without stopping the underlying work. The file may advance; the
assertion may not. Examples: no structural specification promotion without
validated safety factors for salvaged materials (EN-001); no T1/T2 part claims
without a declared precision ceiling (PR-001). Epistemic Blocking is resolved
by grounding the claim in empirical evidence sufficient for the relevant
provenance label — the work continues in a bounded state while that grounding
is sought. Consistent with the graceful degradation rule in
`Admin/Auditor_Protocols.md` EF-0.2. Defined as a priority subtype in
`Admin/Auditor_Protocols.md` Priority Demotion Doctrine.

**Priority (Promo)**
The `Unknowns.md` Active Index column tracking whether an unknown blocks
*promotion* of its owning file (Spec Gate advancement, Status change) — distinct
from a file-local `Blocking` field, which tracks whether an unknown blocks a
*physical operation* (Operational Blocking) or a *claim* (Epistemic Blocking).
The same unknown can carry "Blocking" in the Priority (Promo) column and "No"
in the file-local Blocking field without contradiction: SC-002 (segregation
effectiveness) blocks the Spin Chamber's capability claim from being promoted,
but does not by itself stop a physical run from occurring safely. Misreading
Priority (Promo) as identical to the file-local Blocking field has produced
false-positive "desync" findings (EV-001/F-EN-002, SC-001–002/F-SC-003). Always
treat the two columns as separate vocabularies.

**Heuristic Failure (HF-001)**
A failure class distinct from Sensor Failure and Mechanical Failure. In a
heuristic failure, the object is technically visible, the materials are
technically identifiable, and the machine technically has the tools — yet the
system lacks the procedural knowledge to act optimally or safely. Heuristic
failures manifest in both disassembly (bolt removal order, cut sequence,
contamination routing) and fabrication (weld path, fixturing sequence, joint
order) contexts. The Cognitive Salvage Layer (`Tests/Cognitive_Salvage_Layer.md`)
exists specifically to address this failure class by harvesting and verifying
human-derived procedural knowledge. Heuristic Failure is a first-class Forge
failure class; do not collapse it into planning failure or agent error. See
CT-008 for canonicalization status.

**Grain System**
The physical provenance and identity continuity mechanism for the Lazarus Forge.
A Grain is a small retained sample (baseline: 1g) taken from a source component
before or during Forge processing. Grains serve three simultaneous functions:
(1) philosophical continuity — connecting a rebuilt or fabricated output to its
material origin, instantiating the Ship of Theseus doctrine; (2) legal artifact
— providing chain-of-custody evidence that an output is a restoration of owned
material rather than a new manufacture, supporting right-to-repair legal
posture; (3) provenance anchor — the physical equivalent of a cryptographic
hash, binding the output's identity to a verifiable source.

The Grain System is the physical instantiation of the identity continuity
doctrine defined in `Admin/Ship_of_Theseus.md`. The cognitive equivalent is
the cryptographic state log defined in Section IV of that file.

Implementation analog: Vehicle Identification Numbers (VIN, NHTSA 49 CFR Part
565), Hull Identification Numbers (HIN), and ISO 3779 equipment serialization
all attach identity to the irreducible structural core rather than replaceable
components and are legally recognized as identity anchors even after total
component replacement. The Grain protocol should adapt these existing
legally-hardened standards rather than inventing a new system. Minimum viable
grain protocol must specify: what constitutes the Forge equivalent of the
irreducible structural core; where the serial identifier attaches; and how
provenance transfers through the Forge gates.

*Implementation status: ST-001 (grain storage and tracking protocol) and
ST-002 (QR documentation standard) in `Admin/Ship_of_Theseus.md` sidecar
are the open resolution vehicles. The canonical definition here does not
constitute resolution of either entry — it registers the vocabulary;
the implementation work remains in the owning sidecar.* See CT-009.

---

### 5. Explicit Term Exclusions — Anti-Drift Guardrails

The following substitutions are mandatory in all specification drafts.
Use of banned terms in specification-level content is a Fallacy 4
(Semantic Drift) violation per `Admin/Auditor_Protocols.md`.

| Banned Term                          | Use Instead                                    | Context                                                                                          |
|--------------------------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Recycling (for triage processes)     | Value Preservation                             | When functional identity is preserved                                                            |
| Recycling (for bulk feedstock)       | Material Recovery                              | When structural complexity has been reduced                                                      |
| Autonomous Decision-Making (unbound) | Deterministic Gate Logic                       | For rule-governed routing decisions                                                              |
| Autonomous Decision-Making (unbound) | Arbitrated Agent Consensus                     | For multi-agent deliberation outcomes                                                            |
| High-RPM (for Gate_04)               | Centrifugal Separation / Pre-thermal Diversion | Gate_04 is defined by position, not RPM                                                          |
| Scrap                                | Material Recovery or Salvaged Feedstock        | Depending on processing state                                                                    |
| Canonical (unqualified)              | See Disambiguation section above               | Always specify which canonical usage applies                                                     |
| Gate N (unqualified, N=1–6)           | Verification Gate N or Enforcement Checkpoint N | Always specify which system; both are six-item, numbered, and were once both called "Canonical Verification Gates" — see GOV-011 |
| Blocking (unqualified)               | Operational Blocking or Epistemic Blocking     | Always specify which type; unqualified Blocking obscures whether physical work halts or only claims halt |
| SESSION BOUNDARY INDEX               | Audit Cycle (Section 4, this file)             | Not a defined term anywhere in `Admin/Auditor_Protocols.md`, `Admin/Forge_Audit_Kit.md`, `Unknowns.md`, or `Admin/Verification_Gates.md` as of 2026-07-05, despite appearing in multiple audit headers as if citing established doctrine. Treat any audit opening with this phrase as citing an unverified/external convention, not repository doctrine, until traced to a real source or formally adopted here. |
| EC-00X (bare, no owning file named) | EC-00X (`Admin/Ethical_Constraints.md`) or the pending `ECN-` renumbering (`Admin/Economics.md`) | Ambiguous as of 2026-07-05 — see CT-007. EC-001, EC-002, EC-004, EC-005, and EC-008 are each claimed by both files with unrelated content. Never cite a bare "EC-00X" without naming the owning file until CT-007's rename is complete. |

"Autonomous Decision-Making" without bounding clauses is prohibited because
it obscures human override visibility, which is a constitutional requirement
under Axiom P-4 (Agency and Consent).

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                          | What Failed                                                                  | What Was Learned                                                                                                        | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Drafting localized naming definitions inside gate files | Fragmented files diverged quickly over successive multi-agent cycles         | Consolidation into a dedicated terminology document prevents premature cross-file drift                                 | Replicated | No                  |
| 2026-05-27 | Audit Review  | Gate_04 described using "high-RPM" as defining characteristic | Terminology bled from Gate_05 (Spin Chamber); audit flagged semantic conflict | Gate_04 is defined by flow position (pre-thermal diversion) and protocol (refusal-first); RPM belongs to Gate_05 only  | Replicated | No                  |
| 2026-05-27 | Audit Review  | Tier 4 defined as "operational logic files" with Forge_flow.md as example | Conflicted with Governance_Charter.md which places Forge_flow.md in Tier 5  | Tier definitions must derive from Governance_Charter.md; Forge_flow.md is Tier 5 (domain specification)                | Replicated | No                  |
| 2026-07-03 | Audit Review  | `Admin/Verification_Gates.md` and `Admin/Governance_Charter.md` each titled their six-item criteria list "Canonical Verification Gates" independently | Neither file cross-checked the other before naming; `Admin/Verification_Gates.md` was never registered as a vocabulary authority in this file's Conflict Resolution Doctrine, so no mechanism existed to catch the collision | Registering every load-bearing file as a vocabulary authority source matters even when it seems self-evidently canonical — "obviously the audit-gates file owns gate vocabulary" was never actually written down anywhere, so nothing caught the collision until a downstream governance amendment needed to cite "Gate 3 or Gate 4" and found two answers | Replicated | No |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                                   | Why Abandoned                                                                                         | Reconsider? |
|------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-26 | Merging naming conventions into Unknowns.md file header                | Overcrowds navigation layer; violates single-responsibility principle of cross-module indexing        | No          |
| 2026-05-27 | Gate_04 defined by RPM characteristics                                 | RPM is Gate_05's defining parameter; Gate_04 is defined by flow position and pre-thermal diversion   | No          |
| 2026-05-27 | Tier 4 containing Forge_flow.md as example                             | Governance_Charter.md places Forge_flow.md in Tier 5; derived file cannot contradict constitutional source | No     |
| 2026-05-27 | This file as primary ontology superseding Forge_flow.md                | Forge_flow.md is the operational routing authority; this file is the cross-file consistency enforcer | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Conflict resolution doctrine removed or simplified to single-source authority
- Gate_04 definition reintroduces RPM as defining characteristic
- Tier definitions diverge from `Admin/Governance_Charter.md` §Governance
  Authority Hierarchy without a logged reconciliation entry
- Disambiguation table for "canonical" removed or collapsed
- Anti-drift guardrails table loses any of the banned term entries
- "Autonomous Decision-Making" prohibition removed without corresponding
  update to Axiom P-4 discussion in `Admin/Governance_Charter.md`
- "Blocking (unqualified)" row removed from anti-drift table without
  corresponding removal of Operational Blocking / Epistemic Blocking
  definitions from Section 4
- HF-001 (Heuristic Failure) definition modified without corresponding
  update to `Tests/Cognitive_Salvage_Layer.md` Scope Boundary
- Scope boundary revised to absorb filename resolution from Discovery.md
  Rename Registry
- Scope boundary revised to absorb operational routing semantics from
  `Architecture/Forge_flow.md`
- "Verification Gate" and "Enforcement Checkpoint" entries in Section 4
  removed or merged, or either system renamed elsewhere without a
  corresponding update logged here (CT-010)
- A structural renaming occurs in Discovery.md or AUDIT_HARNESS.py that
  is not reflected here within one audit cycle
- Any new functional gate added between Gate_01 and Gate_07 without
  corresponding entry in Section 2
- CT-001 or CT-002 closed without resolution evidence
- Lessons Learned table missing Evidence Type, Confidence, or
  Revalidation Needed columns
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### CT-001 — Legacy Script Integration Name Mapping

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Technical                |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-05-26               |
| Last Reviewed | 2026-06-24               |

**Description:** Several early internal variables within legacy automation
layers may still map back to alternative names used prior to folder
structuralization. Distinct from the filename aliasing function of Discovery.md
Rename Registry — this tracks internal string references within AUDIT_HARNESS.py
and tooling.

**Resolution Path:** Audit `Automation/AUDIT_HARNESS.py` internal hardcoded
strings against this vocabulary file to confirm alignment with current
canonical folder-prefixed paths.

---

### CT-002 — Component Library Schema Standard Undefined

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Architectural                           |
| Blocking      | Yes (Gate_02_Triage.md Spec promotion)  |
| Owner         | Admin/Canonical_Terms.md                |
| First Logged  | 2026-05-26                              |
| Last Reviewed | 2026-07-21                              |

**Description:** The technical definition for what constitutes a Component
Library entry format remains fluid. Without a rigorous taxonomy specification,
different triage nodes will export incompatible semantic tags for identical items.

**Resolution Path:** Cross-validate with `Architecture/Components.md` and
define entry properties (UUID, structural envelope, metallurgical class)
before promoting triage documentation to full Specification.

**Consolidation note, 2026-07-21:** `Operations/Gate_02_Triage.md` independently
logged this same unknown under a colliding `CT-002` ID, 11 days after this
entry, with its own Owner field pointing back here — while this entry's
Owner field pointed there. Neither file claimed itself. Surfaced by
`Automation/integrity_check.py`'s Unknown Pass; Owner corrected to this file
(matching the self-referential convention every other entry here uses);
`Operations/Gate_02_Triage.md`'s duplicate renamed to `TS-004` and discharged
to this entry, which `Unknowns.md`'s global index already treated as
canonical. This entry remains the single tracked instance of the underlying
question, still genuinely open.

---

### CT-003 — Dependency_Priority_Map.md Needed Before v1

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Architectural            |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-05-27               |
| Last Reviewed | 2026-06-24               |

**Description:** As governance, ontology, integrity, audit, and security
become mutually referenced, the modification propagation path between them
risks becoming ambiguous. A dedicated dependency priority map would make
the ordering of authority explicit and auditable.

**Resolution Path:** Discharge via Trajectory — log in `Admin/Trajectories.md`
as a v0→v1 transition task.

---

### CT-004 — Trusted Initialization Environment Definition Required

| Field         | Value                                           |
|---------------|-------------------------------------------------|
| Status        | Open                                            |
| Risk          | High                                            |
| Priority      | Major                                           |
| Type          | Security / Technical                            |
| Blocking      | Yes (Security_Protocols.md Section III.2)       |
| Owner         | Admin/Canonical_Terms.md                        |
| First Logged  | 2026-05-28                                      |
| Last Reviewed | 2026-06-24                                      |

**Description:** `Admin/Security_Protocols.md` Section III requires key-pair
generation within a "trusted initialization environment" but the term is
undefined across four dimensions: physical custody, software verification,
network isolation, and attestation method.

**Resolution Path:** Payment via Specification — define in Section 4 of this
file. Minimum required elements: (1) physical custody requirements;
(2) software verification requirements; (3) network isolation requirements;
(4) attestation method. Cross-reference SEC-005 in `Admin/Security_Protocols.md`.

---

### CT-005 — Ethical and Authorization Term Placeholders Pending Canonicalization

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Governance / Epistemic   |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-14               |
| Last Reviewed | 2026-06-24               |

**Description:** Several ethical and authorization terms appear across
Ethical_Constraints.md, Governance_Charter.md, and Auditor_Protocols.md
without canonical definitions here. Confirm EC-001 (sufficient confidence
threshold) language is consistent with the Epistemic Blocking definition
when that entry matures.

**Resolution Path:** Payment via Specification — register each placeholder
term in Section 4 as entries mature across owning files.

---

### CT-006 — Circular Dependency Detection Undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Architectural / Governance |
| Blocking      | No                         |
| Owner         | Admin/Canonical_Terms.md   |
| First Logged  | 2026-06-23                 |
| Last Reviewed | 2026-06-24                 |

**Description:** No doctrine governs the detection of circular dependencies
(A → B → C → A) in the blocking chain. At current scale these have not
appeared, but no mechanism exists to detect or prevent them as the dependency
graph grows.

**Resolution Path:** Payment via Specification — define circular dependency
detection criteria and either prohibit cycles formally or specify how they are
broken. May resolve via AUDIT_HARNESS.py enhancement or as a doctrine note
in the Dependency Clusters section of Unknowns.md.

---

### CT-007 — ID Namespace Allocation Doctrine Undefined

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | **High (escalated 2026-07-05, was Low)** |
| Priority      | **Major (escalated 2026-07-05, was Minor)** |
| Type          | Governance / Technical   |
| Blocking      | **Epistemic — see below** |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-23               |
| Last Reviewed | 2026-07-05               |

**Description:** No formal doctrine governs whether IDs may be reused after
resolution, how ranges are reserved for new clusters, how collisions are
handled if two files claim the same prefix, or how multi-owner cross-module
unknowns are numbered.

**Escalation 2026-07-05 — this stopped being hypothetical.** Confirmed via
direct check of `Unknowns.md`: the `EC-` prefix is claimed by **both**
`Admin/Ethical_Constraints.md` and `Admin/Economics.md`, with five actual
colliding IDs already live in the global index — EC-001, EC-002, EC-004,
EC-005, EC-008. Each ID currently points to two entirely different unknowns
depending on which file's context you're in (e.g., EC-002 is
"Anti-Weaponization pattern-matching" in Ethical_Constraints.md and
"Operating cost baseline not established" in Economics.md — one Blocking,
one Critical, unrelated in substance). `Admin/Forge_Audit_Kit.md`'s own
Governance Sidecar ID Reference already documents `EC-` as belonging to
Ethical_Constraints.md — Economics.md's usage was never registered there
and appears to be the erroneous claim, not the reverse. Any reference to an
"EC-00X" unknown anywhere in the repository is now ambiguous without an
explicit file qualifier until this is fixed.

**Why It Matters:** This is a live G5 (Cross-Reference Integrity) problem
at the repository level, not a future risk to plan around. Every past and
future reference to an EC-numbered unknown that doesn't name its owning
file explicitly is currently unreliable.

**Resolution Path:** Economics.md's five colliding entries need renaming to
a non-colliding prefix — candidate: `ECN-` (Economics.md is not yet
formally represented in the Governance Sidecar ID Reference at all, so this
also closes that gap). Update `Unknowns.md`'s global index and
Economics.md's own sidecar to match. Register `ECN-` in
`Admin/Forge_Audit_Kit.md`'s Governance Sidecar ID Reference table
alongside the existing entries. Until renamed, any reference to EC-001,
EC-002, EC-004, EC-005, or EC-008 must explicitly name the owning file. The
original Discharge-via-Trajectory resolution path (below) remains correct
for the *general* doctrine question (reuse, range reservation, future
collision handling) — this escalation only accelerates the specific,
already-occurred collision, which shouldn't wait for the general doctrine
to be resolved first.

**Original Resolution Path (general doctrine, still valid):** Discharge via
Trajectory — log in `Admin/Trajectories.md` as a v0→v1 transition task.
Minimum doctrine when resolved: IDs are never reused; prefixes are
registered in this file or Repository_Structure.md when a new cluster is
created; collisions are resolved by renaming the newer entry with a logged
alias.

---

### CT-008 — HF-001 Heuristic Failure Canonicalization Status

| Field         | Value                    |
|---------------|--------------------------|
| Status        | In Progress — Vehicle    |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-24               |
| Last Reviewed | 2026-06-24               |

**Description:** HF-001 (Heuristic Failure) was proposed in
`Tests/Cognitive_Salvage_Layer.md` v0.2 as a first-class Forge failure class
distinct from Sensor Failure and Mechanical Failure. The definition has been
registered in Section 4 of this file as of v0.3. CT-008 tracks whether the
canonicalization is complete and consistent across all files that reference
the concept.

**Resolution Path:** Payment via Specification — verify that all files
referencing heuristic failure use HF-001 vocabulary consistently; confirm
no file uses "planning failure" or "agent error" as a synonym for what this
file defines as HF-001. Close when vocabulary is confirmed consistent across
Cognitive_Salvage_Layer.md, Forge_flow.md (if referenced), and any future
files in the Cognitive Salvage domain. This entry is In Progress because the
definition exists but cross-file consistency has not yet been verified.

---

### CT-009 — Grain System implementation protocol undefined

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Governance / Technical   |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-26               |
| Last Reviewed | 2026-06-26               |

**Description:** The Grain System canonical definition
has been registered in this file (Section 4), establishing
the vocabulary and legal analog (VIN/HIN/ISO 3779). The
implementation protocol — storage container standard,
label format, chain-of-custody log, serial identifier
attachment point — remains in ST-001 and ST-002 in
`Admin/Ship_of_Theseus.md`. CT-009 tracks whether the
canonical definition here remains consistent with the
implementation as it matures in the owning sidecar.

**Resolution Path:** Confirm consistency between this
definition and ST-001/ST-002 resolution when those entries
close. If the implementation deviates materially from the
VIN/HIN analog described here, update the canonical
definition accordingly. Close CT-009 when ST-001 and
ST-002 both reach Payment via Specification and the
canonical definition is confirmed consistent.

---

### CT-010 — Verification Gate / Enforcement Checkpoint rename propagation

| Field         | Value                    |
|---------------|--------------------------|
| Status        | In Progress — Vehicle    |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-07-03               |
| Last Reviewed | 2026-07-03               |

**Description:** `Admin/Governance_Charter.md`'s "Canonical Verification
Gates" (Gate 1–6) was renamed to "Enforcement Checkpoints" (Checkpoint
1–6) on 2026-07-03 to end a naming collision with this file's
`Admin/Verification_Gates.md`-owned Verification Gate definition — see
GOV-011. `Admin/Verification_Gates.md` also received a disambiguation
note confirming sole ownership of unqualified "Gate"/"canonical"
terminology in its domain. CT-010 tracks whether every file that cites
"Gate 3," "Gate 6," or similar in a governance-action context (as opposed
to document-promotion or Operations/Gate_01–07 physical-pipeline context)
has been updated to Enforcement Checkpoint terminology, or at minimum
disambiguated.

**Why It Matters:** A rename at the two source files does not guarantee
every downstream citation updates. `Admin/Auditor_Protocols.md` and
`Admin/Forge_Audit_Kit.md` both cite Verification_Gates.md's Gate 3/6
directly (correctly, no rename needed there) — but any file that was
actually citing Governance_Charter.md's now-renamed checkpoints under the
old "Gate N" name would now be citing a term that no longer exists in that
file, silently breaking the reference rather than erroring visibly.

**Resolution Path:** Payment via Specification — grep the repository for
"Gate 1" through "Gate 6" outside `Admin/Verification_Gates.md` and
`Operations/Gate_01` through `Gate_07`; for each hit, confirm it means
Verification Gate (no change needed) or Enforcement Checkpoint (needs
updating) and correct accordingly. Close when no ambiguous unqualified
"Gate N" citation remains outside those two exempted contexts.

---

### CT-011 — Cycle definition propagation into Auditor_Protocols.md

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Resolved                 |
| Risk          | Medium (was)             |
| Priority      | Major (was)              |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-07-05               |
| Last Reviewed | 2026-07-05               |
| Resolved      | 2026-07-05               |

**Description:** This file now defines Cycle (Section 4) as one calendar
year by default, superseding the operational reading in
`Admin/Auditor_Protocols.md` (§Expiry Rule, §Expiry check) that measured a
"cycle" as each individual audit pass. Auditor_Protocols.md's own text has
not yet been updated to reflect or cross-reference this definition — the
same class of gap CT-010 tracks for the Gate/Checkpoint rename, applied to
a different term.

**Why It Mattered:** Until Auditor_Protocols.md's Expiry Rule and Expiry
check text explicitly pointed to this file's Cycle definition, an agent
reading Auditor_Protocols.md in isolation would still apply the old
per-audit-pass counting and reproduce the same escalation-inflation problem
this definition was created to fix. This was not hypothetical — a same-day
dual audit of `Admin/Ethical_Constraints.md` reported unknowns 62 and 17
days old as "9 cycles" and "3 cycles open" before this propagation closed.

**Resolution:** `Admin/Auditor_Protocols.md` v0.17 (2026-07-05) — §Expiry
Rule and §Expiry check now explicitly cross-reference this file's Cycle
definition and distinguish audit *pass* (can recur many times) from Cycle
*threshold* (calendar-based, advances independently of pass frequency). The
broader grep this entry called for — other files computing cycle-based
aging without cross-referencing this definition — has not been performed
yet; `Admin/Forge_Audit_Kit.md`'s Expiry Watch summaries specifically are
still unchecked. If that broader sweep surfaces further gaps, log a new
entry rather than reopening this one — this entry's scope was
Auditor_Protocols.md specifically, which is now closed.

---

### Resolution Log

- 2026-07-21: **CT-002 Owner field corrected; `Operations/Gate_02_Triage.md`'s
  colliding duplicate discharged.** `Automation/integrity_check.py`'s Unknown
  Pass (first run) found `Operations/Gate_02_Triage.md` independently tracking
  the same Component Library Schema question under a colliding `CT-002` ID,
  11 days after this entry, each file's Owner field pointing at the other. Same
  root-cause shape as CT-007's EC- collision below, this time a sidecar ID
  rather than a governance prefix registration gap. Owner corrected to
  `Admin/Canonical_Terms.md` (matching every other entry's self-referential
  convention in this file); `Gate_02_Triage.md`'s duplicate renamed to its own
  `TS-004` and marked Resolved — Discharge via Consolidation, pointing here.
  This entry remains the single tracked instance, still Open.

- 2026-07-05 (third entry, same day): **v0.7 — CT-007 escalated: confirmed
  active `EC-` prefix collision, not hypothetical.** Direct check of
  `Unknowns.md` found EC-001, EC-002, EC-004, EC-005, and EC-008 each
  claimed by both `Admin/Ethical_Constraints.md` and `Admin/Economics.md`
  with unrelated content under each ID. `Admin/Forge_Audit_Kit.md`'s own
  Governance Sidecar ID Reference already reserves `EC-` for
  Ethical_Constraints.md — Economics.md was never registered there.
  Risk/Priority escalated Low/Minor → High/Major. Anti-Drift Guardrails
  gained a row requiring the owning file be named explicitly for any bare
  "EC-00X" reference until resolved. Resolution path split: the original
  general-doctrine question (Discharge via Trajectory) stays as-is; a new,
  faster path added for the already-occurred collision specifically —
  rename Economics.md's five entries to a new `ECN-` prefix and register
  it. Surfaced incidentally while gathering current data for
  `Admin/Forge_Audit_Kit.md`'s FAK-007 refresh — not something either file
  was being audited for directly.

- 2026-07-05 (second entry, same day): **v0.6 — CT-011 resolved.**
  `Admin/Auditor_Protocols.md` v0.17 now cross-references this file's Cycle
  definition in its Expiry Rule and Expiry check text, closing the
  propagation gap. Confirmed against a real case: a same-day dual audit of
  `Admin/Ethical_Constraints.md` had reported 62- and 17-day-old unknowns as
  "9 cycles" and "3 cycles open" — exactly the inflation this definition
  exists to prevent, now closed at the source file. Broader sweep for the
  same gap in other files (Forge_Audit_Kit.md's Expiry Watch summaries
  specifically) not yet performed — flagged in CT-011's Resolution field
  for whoever does that pass next. Open Unknowns 10 → 9.

- 2026-07-05: **v0.5 — Cycle defined; version-string mismatch corrected.**
  Section 4 gained a canonical **Cycle (Governance / Audit Cycle)** entry:
  one calendar year by default, declared by human governing authority at
  current operating pace, adjustable shorter at operator discretion —
  resolves the ambiguity found when `Admin/Auditor_Protocols.md`'s own
  Expiry Rule text implicitly treated a "cycle" as each individual audit
  pass, which was inflating escalation language ("6 cycles open," "8-cycle
  threshold exceeded") far faster than real elapsed time. CT-011 logged to
  track propagation of this definition into Auditor_Protocols.md's own
  text, mirroring CT-010's rename-propagation pattern. Anti-drift guardrail
  table gained a row flagging "SESSION BOUNDARY INDEX" — a phrase used as
  if authoritative in recent Grok/Gemini audit headers but absent from
  Auditor_Protocols.md, Forge_Audit_Kit.md, Unknowns.md, and
  Verification_Gates.md; treat citations to it as unverified until
  traced or formally adopted. Separately, corrected a live version-string
  mismatch unrelated to today's substantive changes: this file's header
  read "Version 0.3" while the Status section below already documented
  changes through "Version 0.4" — the header had not been updated since at
  least the 2026-07-03 CT-010/Verification-Gate-disambiguation pass. Header
  now reads 0.5, matching this entry. Open Unknowns 9 → 10. **Process note:**
  a `str_replace` edit while adding CT-011 silently dropped the "Resolution
  Log" heading at the old_str/new_str boundary — caught and restored
  same-session via post-edit grep, per the standing recommendation in prior
  session handoffs to verify heading survival after any edit near a
  section boundary.

- 2026-05-26: File created (v0.1) by Gemini (Structural/Auditor). Initial
  vocabulary mappings, anti-drift guardrails, and CT-001/CT-002 logged.
- 2026-05-27: v0.2 revision — Conflict Resolution Doctrine section added.
  Disambiguation table for "canonical" added. Gate_04 definition corrected.
  Tier 4 definition corrected. Section 4 (Governance and Audit Terms) added.
  Scope boundary clarified. CT-002 owner path corrected. CT-003 logged.
  Abandoned Paths populated. Open Unknowns updated to 3.
- 2026-05-28: CT-004 logged — trusted initialization environment definition
  required by `Admin/Security_Protocols.md` Section III.2; Blocking for that
  section's promotion. Open Unknowns 3 → 4.
- 2026-06-23: v0.3 additions — Operational Blocking and Epistemic Blocking
  defined in Section 4. Anti-drift guardrail added for unqualified "Blocking"
  usage. CT-006 and CT-007 logged. Open Unknowns 4 → 6.
- 2026-06-24: v0.3 continued — HF-001 (Heuristic Failure) defined in Section 4
  per proposal in `Tests/Cognitive_Salvage_Layer.md` v0.2. CT-008 logged to
  track cross-file consistency of HF-001 vocabulary. Drift Indicators updated:
  HF-001 consistency rule and unqualified Blocking guardrail rule added.
  All Last Reviewed dates updated. Open Unknowns 6 → 7.

---

## Relationship to Existing Documents

- `Architecture/Forge_flow.md` — primary operational vocabulary reference
  standard; authoritative over this file for operational gate logic vocabulary
- `Admin/Governance_Charter.md` — Tier 1 constitutional source; authoritative
  for tier definitions and constitutional vocabulary; owns Enforcement
  Checkpoint definition (renamed 2026-07-03 from "Canonical Verification
  Gates" — see GOV-011, CT-010)
- `Admin/Verification_Gates.md` — fourth vocabulary authority source
  (added 2026-07-03); authoritative for Verification Gate definitions and
  document-promotion vocabulary; every file's `Spec Gates X/6` field
  references this file exclusively
- `Admin/Auditor_Protocols.md` — Tier 2; Fallacy 4 is the primary enforcement
  mechanism for terminology violations; Priority Demotion Doctrine defines
  Operational Blocking and Epistemic Blocking subtypes
- `Admin/Forge_Audit_Kit.md` — Tier 3; CT- sidecar prefix in Sidecar ID
  Reference table
- `Admin/File_Template.md` — standard file structure
- `Discovery.md` — Rename Registry is the canonical filename resolution source
- `Tests/Cognitive_Salvage_Layer.md` — source of HF-001 proposal; CT-008
  tracks cross-file vocabulary consistency
- `Operations/Gate_02_Triage.md` — CT-002 Blocking for that file's Spec promotion
- `Architecture/Components.md` — CT-002 resolution requires cross-validation
- `Admin/Trajectories.md` — CT-003 and CT-007 to be logged as v0→v1 items
- `Admin/Security_Protocols.md` — CT-004 Blocking for Section III.2 promotion
- `Admin/Canonical_Terms_LF.md` — prior planned filename; resolved via
  Archive/Rename_Registry.md; all references to _LF suffix are stale

---

## Status

Version 0.6 — CT-011 resolved: `Admin/Auditor_Protocols.md` v0.17 now
cross-references this file's Cycle definition in its Expiry Rule and Expiry
check text, closing the propagation gap logged at v0.5. Open Unknowns
10 → 9.

**Changes from v0.5:**
- CT-011 marked Resolved (was Open)
- Open Unknowns: 10 → 9
- Header version string 0.5 → 0.6

**Prior — Version 0.5 (2026-07-05):** Cycle (Governance / Audit Cycle)
defined in Section 4 (one calendar year default, operator-adjustable);
CT-011 logged tracking propagation into Auditor_Protocols.md; SESSION
BOUNDARY INDEX flagged as non-canonical in Anti-Drift Guardrails; header
version-string corrected from stale 0.3 to match this file's actual state.

**Changes from v0.4:**
- Section 4: Cycle (Governance / Audit Cycle) defined
- CT-011 logged: Cycle definition propagation into Auditor_Protocols.md
- Anti-drift guardrail table gained SESSION BOUNDARY INDEX row
- Open Unknowns: 9 → 10
- Header version string corrected 0.3 → 0.5 (was out of sync with this
  Status section since at least the prior v0.4 entry below)

**Prior — Version 0.4 (2026-07-03):** Verification Gate / Enforcement
Checkpoint disambiguation added; CT-010 logged; Verification_Gates.md
registered as fourth vocabulary authority source.

**Changes from v0.2:**
- Section 4: HF-001 (Heuristic Failure) defined as first-class failure class
- Drift Indicators: HF-001 consistency rule added; unqualified Blocking
  guardrail rule added
- CT-008 logged: HF-001 canonicalization status tracking
- All Last Reviewed dates updated to 2026-06-24
- Open Unknowns: 6 → 7
- Version string updated to 0.3

**What must remain constant:**

**Forge_flow.md governs operational routing semantics.**
**Governance_Charter.md governs tier authority.**
**This file governs cross-file vocabulary consistency.**
**Conflicts between them are logged here — never silently resolved.**
- 2026-06-26: Grain System canonical definition added to Section 4 — vocabulary,
  legal functions, VIN/HIN/ISO 3779 implementation analog, and implementation
  status note. CT-009 logged to track consistency between canonical definition
  and ST-001/ST-002 implementation work in Ship_of_Theseus.md. Open Unknowns
  7 → 8.
- 2026-07-03: v0.4 — Verification Gate / Enforcement Checkpoint disambiguation.
  `Admin/Governance_Charter.md`'s "Canonical Verification Gates" and
  `Admin/Verification_Gates.md`'s "Six Canonical Verification Gates" were
  found to be independently-named, materially different six-item systems
  sharing the same "Gate N" numbering — an undocumented divergence (GOV-011)
  that existed in part because Verification_Gates.md was never registered
  as a vocabulary authority source in this file's Conflict Resolution
  Doctrine, despite being the file every document's `Spec Gates X/6` field
  actually references. Fixed: Verification_Gates.md added as fourth
  authority source (Resolution Rule 3 renumbered accordingly). New Section 4
  entries: Verification Gate, Enforcement Checkpoint — both explicitly
  cross-referencing each other and the unrelated Operations/Gate_01–07
  physical-pipeline usage. Full Stop Review's "reset to G1" reference
  disambiguated to "Verification Gate 1." Anti-drift guardrail table gained
  a row for unqualified "Gate N." CT-010 logged to track propagation of the
  rename across any file still citing the old unqualified terminology. New
  Lessons Learned row added, following the same pattern as the 2026-05-27
  Gate_04/Gate_05 entry this file already used to fix an earlier instance
  of exactly this problem. Open Unknowns 8 → 9.
