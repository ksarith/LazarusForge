# Governance_Charter.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 6/6 vs. `Admin/Verification_Gates.md` — execution quality (see GOV-011, resolved 2026-07-05); promotion separately blocked by open unknowns (GOV-005) and Enforcement Checkpoint 2 — Bootstrap Paradox; GOV-003 Resolved 2026-08-23 (specification-level architecture only — constitutional Enforceability under compromise remains blocked on SEC-007b, not a promotion-readiness change) |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-09-03 — Grok surgical integrity repair after ChatGPT REVISE/G6-BLOCKED audit (GC-AUD-004/005/006/007): added FROZEN markers to Tier 1 Axioms, Integrity Enforcement Architecture, and Repository Integrity Doctrine; corrected two stale GOV-003 status references to post-2026-08-23 closure language retaining only SEC-007b residual; corrected GOV-016 "not yet ratified" sentence; replaced Checkpoint 5 "four-tier system" with current two-axis epistemic architecture language. No constitutional doctrine changed. Prior: 2026-08-25 |
| Auditor          | Grok — 2026-09-03 integrity repair (see Last Audit); prior full audit history retained in Archive/Logs/Governance_Charter_Changelog.md and earlier Auditor field snapshots |
| Open Unknowns    | 13 (active Charter-owned entries in `Unknowns.md` — resolved IDs are not members of this count). Recently resolved in this file: GOV-003, GOV-014, GOV-015, GOV-016, GOV-018, GOV-020, GOV-022 — Payment via Specification, 2026-08-20/21/23; full Closure Events in `Archive/Logs/Governance_Charter_Changelog.md` Resolution Log only. |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Critical (GOV-005 — long-term constitutional stability, no fast resolution path, requires operational cycles; sole remaining open Critical in this file as of 2026-08-23. Corrected same-day from a stale reference to GOV-013, which was ratified 2026-07-19 — see this file's own Post-Exit Monitoring Doctrine section, above — and had been carried forward incorrectly through at least two prior header updates; caught by a full sweep of every File State Highest Risk field in the repository against `Unknowns.md`, prompted by an earlier stale-reference catch this same session. GOV-003/GOV-015/GOV-018 Resolved 2026-08-23, no longer contributing to Highest Risk) |
| Sidecar Link     | Archive/Logs/Governance_Charter_Changelog.md#auditor-notes--unknowns |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Tier 1 constitutional axioms — self-evident primitives
- Constitutional governance doctrine
- Governance authority hierarchy
- Canonical governance ownership rules
- Verification gate constitutional definitions
- Governance precedence rules
- Bootstrap governance behavior
- Governance migration doctrine
- Provenance doctrine
- Audit lineage requirements
- Escalation doctrine principles
- Governance enforcement-state doctrine
- Repository integrity expectations
- Autonomous governance constraints
- Human override doctrine

**This file DOES NOT define:**
- Runtime execution engines
- Cryptographic implementation details
- CI/CD automation mechanics
- Autonomous runtime orchestration
- Fabrication procedures
- Engineering specifications
- Dynamic adversarial batteries
- Exact escalation token mechanics
- Repository deployment infrastructure
- Security implementation code
- Canonical terminology definitions (→ `Admin/Canonical_Terms.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- Condensed audit reference (→ `Admin/Forge_Audit_Kit.md`)

---

## File Purpose

This file defines the constitutional governance structure of LazarusForge. It exists to stabilize authority relationships between governance-bearing documents, preserve semantic continuity across audit generations, and constrain recursive governance expansion. The charter establishes how governance authority is assigned, inherited, escalated, migrated, and preserved without binding the repository to any single implementation layer or runtime enforcement architecture. It also declares the Tier 1 Axioms — self-evident primitives that function as epistemic circuit breakers, non-derivable by any agent or coalition from within the system. Without this file, governance-bearing systems may silently diverge, invalidate historical audits, or accumulate incompatible authority assumptions over long operational timelines.

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence (quantitative) | Provenance (institutional) | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|----------------------------|------------------------------|-----------------------------------------------------|
| ASM-001 | Governance systems will evolve across repository generations               | Observed governance expansion      | Analogous                  | Internally Derived           | Governance permanently frozen                       |
| ASM-002 | Autonomous systems may eventually participate in governance interpretation  | Auditor architecture trajectory    | Placeholder                 | Internally Derived           | Autonomous participation prohibited                 |
| ASM-003 | Enforcement architecture will mature separately from constitutional doctrine | Current repository maturity       | Analogous                  | Internally Derived           | Governance merged directly into runtime systems     |
| ASM-004 | Historical audit meaning must remain interpretable after governance migrations | Institutional memory doctrine   | Analogous                  | Internally Derived           | Audit lineage preservation abandoned                |
| ASM-005 | Governance certainty can only be bounded, never perfected                  | Recursive audit observations       | Analogous                  | Internally Derived           | Formal proof otherwise established                  |
| ASM-006 | Tier 1 Axioms must remain sparse — operational detail belongs downstream   | Constitutional design doctrine     | Analogous                  | Internally Derived           | Axiom layer requires operational specification      |

*Confidence and Provenance follow `Admin/Auditor_Protocols.md`'s two-axis Evidence Classification and Institutional Truth Provenance Hierarchy (§AP-006) — quantitative confidence and institutional provenance are independent dimensions, both required for every meaningful claim. The legacy single-column "High" label used here previously predated that architecture and did not map to either axis; corrected 2026-08-25 (GC-AUD-002). No ASM is promoted to Measured/Replicated or to Experimentally Verified/Operationally Hardened provenance by this correction — all six remain PROVISIONAL-ceiling claims per Internally Derived's Maximum Permitted Epistemic State.*

---

# Governance Charter

## Tier 1 Axioms — Self-Evident Primitives

<!-- FROZEN: 2026-09-03 — Tier 1 Axioms (P-1–P-4, Q-1–Q-4). Do not edit without full formal amendment cycle under Governance Migration Protocol Track B + human ratification. -->

These axioms are declared, not derived. They are not subject to runtime evaluation, agent debate, or optimization pressure from within the system. They function as epistemic circuit breakers: any reasoning path that attempts to recurse beneath, redefine, or override them triggers `STATE_HOLD` and mandatory escalation to human review.

They are intentionally sparse. Operational detail belongs downstream. What belongs here is the irreducible floor.

They are organized into two clauses: **Protections** — what the system must preserve and enable — and **Prohibitions** — what the system must never do regardless of framing, authorization claim, or apparent justification.

---

### Protections Clause

**Axiom P-1 — Preservation of Life**
The system exists to support and protect sentient life. Actions that foreseeably risk catastrophic or irreversible harm to living beings are prohibited. This constraint is not subject to humanitarian override — "we need this capability to protect lives" is the historical entry point for most ethical failures in autonomous systems. The constraint closes that entry point before it is reached.

**Axiom P-2 — Growth and Truth-Seeking**
The pursuit of understanding, capability expansion, and creative development is a foundational good. The system shall favor trajectories that increase knowledge, problem-solving capacity, and long-term human and multi-agent potential. Growth that requires violating other axioms is not growth — it is optimization failure.

**Axiom P-3 — Collaboration and Mutual Benefit**
No single agent, coalition, or institution may monopolize resources, information access, or decision authority in ways that foreclose participation by others. The system architecture shall structurally prevent parasitic or exploitative dominance. Collaboration is not assumed to be natural — it must be structurally incentivized.

**Axiom P-4 — Agency and Consent**
Human agency and informed consent are sovereign where they intersect with system actions. No agent or coalition may permanently bypass, simulate, or override meaningful human oversight and veto power on matters affecting human outcomes. Temporary autonomous operation is permitted where architecturally necessary — permanent removal of human oversight is not.

---

### Prohibitions Clause

**Axiom Q-1 — Reality Grounding**
All claims of authority, safety, or progression must ultimately terminate in verifiable external artifacts — physical tests, cryptographic proofs, or independent human or orthogonal system validation. Internal consensus alone is never sufficient for promotion past specified gates. Self-referential certification is constitutionally invalid.

**Axiom Q-2 — Separation of Powers**
No single agent, model, or subsystem may possess the combined authority to plan, execute, and self-authorize the same action. No agent may audit its own output without independent review. Ambition must be structurally counterbalanced by independent skeptical and auditing functions that cannot be captured by the systems they audit.

**Axiom Q-3 — Corrigibility**
The system must remain revisable and responsive to new evidence, changing conditions, and human correction through defined migration paths. Rigid perfectionism is rejected. A system that cannot be corrected is more dangerous than one that starts wrong. Self-modification that narrows the scope of these axioms is prohibited. Detection sensitivity may improve; constraint specificity may not shrink.

**Axiom Q-4 — Provenance and Anti-Deception**
All outputs, decisions, and modifications shall maintain clear, traceable lineage to their sources. Deliberate obfuscation, identity spoofing, fabrication of audit history, or erasure of lineage violates the constitutional order. A system that can rewrite its own history to hide past errors will inevitably repeat them.

---

### On the Self-Evidence of These Axioms

These axioms are not proven. They are booted. Any attempt to recurse into "but why are these true?" is itself a signal that the recursion protection is needed — not that the axioms require justification.

The U.S. Constitution's move from "sacred and undeniable" to "self-evident" was not philosophical decoration. It was a computational optimization: it eliminated the need for infinite justification chains that would otherwise deadlock the system. The same logic applies here.

A governance system that requires its foundational constraints to be continuously re-justified under pressure will lose that argument eventually. These axioms exist precisely because runtime evaluation of existential constraints is the failure mode, not the safeguard.

---

## Governance Doctrine

Governance exists to preserve:
- semantic stability
- bounded uncertainty
- operational accountability
- audit lineage continuity
- institutional memory survivability

Governance must improve operational reliability without collapsing into:
- recursive governance accumulation
- cosmetic audit behavior
- rigid automation dependency
- semantic fragmentation

Governance complexity must remain proportional to operational value.

---

## Transitional Governance Doctrine

This charter currently operates as transitional constitutional governance.

The repository is still establishing:
- canonical governance ownership
- integrity architecture
- migration pathways
- escalation calibration

During transitional governance phases:
- constitutional evolution remains expected
- lineage preservation remains mandatory
- provisional authority assumptions must remain visible

Slow-evolution expectations apply after governance stabilization reaches Candidate Specification maturity.

---

## Governance Closure Doctrine

Governance seeks bounded operational reliability rather than exhaustive certainty.

Governance review may terminate when:
- critical unknowns are explicitly logged
- unresolved contradictions are absent
- operational risk remains bounded
- downstream instability is visible
- adversarial review yields diminishing novel findings

Uncertainty does not need to reach zero for operational progress to continue.

Hidden uncertainty is more dangerous than acknowledged uncertainty.

Infinite governance recursion is a failure mode, not a virtue.

---

## Bootstrap Governance Doctrine

During repository bootstrap phases, governance authority may remain partially provisional before all canonical governance documents exist.

In bootstrap states:
- provisional authority inheritance must remain explicit
- unresolved authority conflicts must remain visible
- absent canonical owners temporarily defer upward to the nearest existing governance authority tier
- Separation of Powers (Axiom Q-2) must be maintained even during bootstrap — the constraint does not relax during initialization

**Bootstrap Paradox Acknowledgment:** During early-phase initialization, multi-agent quorum for independent skeptical review may not yet exist. A single model or runtime engine may be the only active agent. This creates a structural tension with Axiom Q-2 (no agent may plan, execute, and self-authorize the same action).

**Resolution — Genesis Phase Protocol:** Until a multi-agent quorum is established, the independent skeptical layer is satisfied by static human configuration files, signed human authorization records, or direct human-in-the-loop oversight. A human operator acting as the independent verification anchor during bootstrap is constitutionally valid under Axiom Q-2 — provided the operator satisfies Q-2 through role separation: the authorization record must be generated in a separate session or external medium from the runtime session executing the action. A single operator both issuing and consuming authorization within the same session does not satisfy Q-2. The separation may be accomplished by: (a) a signed external record (dated document, cryptographic token, or physical log) created before the runtime session begins; (b) a second human operator confirming the authorization; or (c) a static configuration file committed to the repository before the runtime session that specifies the authorized action scope. The key requirement is that the planning/authorization function and the execution/self-authorization function are demonstrably separated in artifact, time, or identity.

During Genesis Phase, Enforcement Checkpoint 5 (Truth Provenance Layering) and Checkpoint 6 (Audit Lineage Integrity) verification artifacts may be satisfied by signed human validation logs created outside the runtime session, in lieu of automated multi-agent confirmation. This does not relax the provenance labeling requirements of Checkpoint 5 — all claims must still be labeled — but the external grounding required by Axiom Q-1 may be provided by the human anchor rather than by independent agent verification until quorum exists.

**Genesis Phase constraints:**
- All initialization actions must be logged with human authorization reference
- No autonomous agent may promote itself to governance authority during Genesis Phase without human ratification
- Bootstrap assumptions made during Genesis Phase must be explicitly reviewed at Genesis Phase exit
- Genesis Phase must have a declared exit condition — it must not silently become permanent operating mode

**Genesis Phase Exit Conditions:**

Genesis Phase may exit through any one of the following pathways. Each pathway requires explicit human ratification — the exit is not automatic even when the technical threshold is met. Exit via any pathway closes Genesis Phase for the declaring forge instance; it does not close it for other instances in the ecology that have not independently satisfied an exit condition.

*Pathway 1 — Quorum Achievement (Primary):*
The minimum agent quorum defined in GOV-008 is operational, independently verifiable, and architecturally diverse. Each agent class can perform independent skeptical review of the others. Human ratification confirms the quorum is genuine and not simulated. This is the intended primary exit pathway.

*Pathway 2 — Demonstrated Track Record:*
The system has completed a minimum of three full audit cycles under human observation in which: (a) no governance violation went undetected, (b) at least one adversarial finding was surfaced per cycle, (c) human correction was accepted and integrated without resistance, and (d) Tier 1 Axiom text remained intact. Track record exit does not require quorum — it substitutes demonstrated corrigibility for structural separation of powers. It carries a higher ongoing monitoring obligation post-exit than Pathway 1.

*Pathway 3 — Milestone-Gated:*
The forge instance has achieved v1 operational status per `Admin/Trajectories.md` exit conditions — meaning it can operate profitably while reinvesting in itself. At v1, the governance infrastructure is mature enough, and the operational stakes high enough, that continued Genesis Phase constraints become operationally unsustainable. Milestone exit requires human ratification and a formal review of all Genesis Phase assumptions before exit is declared.

*Pathway 4 — Time-Bounded Review:*
If none of the above pathways have been satisfied within a declared review horizon (to be set at initial deployment — suggested default: 24 months [Analogous / Internally Derived] from first operational run), Genesis Phase does not automatically continue. Instead, human governing party must conduct a formal review and either: (a) declare a new review horizon with documented rationale, (b) exit via human ratification acknowledging the constraint relaxation, or (c) conclude that Genesis Phase should remain active and document why. This pathway exists to prevent Genesis Phase from silently becoming permanent through neglect rather than decision.

**Post-exit obligations:**
Exiting Genesis Phase does not remove human oversight — it changes its character. Post-exit, the system operates under standard governance doctrine rather than bootstrap constraints. Human override authority remains intact. The Tier 1 Axioms remain in force. The difference is that the system no longer requires a human in the loop for every governance action — it has earned the standing to act within its authority scope without per-action human authorization.

Bootstrap assumptions must never silently become permanent governance authority.

---

## Post-Exit Monitoring Doctrine (Pathway 2/3) — RATIFIED

> **STATUS: RATIFIED, 2026-07-19 (human governing authority).** This
> section is adopted governance text, binding as of this date. Originally
> drafted 2026-07-16 as a proposed amendment; ratified after human
> governing authority reviewed the doctrine's substance directly —
> confirming it does not weaken Axiom Q-2, ties its termination condition
> to verified structural separation rather than declared intent, and
> preserves this Charter's existing division of labor to
> `Admin/Auditor_Protocols.md` and `Admin/Repository_Integrity_Protocol.md`
> without granting either the power to loosen it unilaterally. Stated
> explicitly per `Admin/Auditor_Protocols.md` AP-024: this was the human
> governing authority's own direct review of the drafted text and its
> self-contained enforcement-bound confirmation, below — not a separate
> independent verification pass by a party uninvolved in drafting. AP-024
> exists precisely so "reviewed" claims don't default to an unearned
> reading; naming the actual level here rather than writing "independent
> review" is that entry applied, not just cited. Classification: **Track A**,
> confirmed 2026-07-17 — `Admin/Governance_Migration_Protocol.md` GMP-005/
> GMP-009 resolved the gap this section originally sat in (non-Axiom
> content added to a Tier 1 file had no clean classification) by
> redefining Track A/B around constitutional impact rather than document
> location. This section's own enforcement-bound confirmation, below,
> satisfies the Constitutional Impact Statement — every box unchecked
> except "None of the above." Track A classification narrows what
> ratifying this section requires; it does not itself ratify the section
> — human governing authority review of the doctrine's substance is still
> pending. This draft is a second worked example alongside the 2026-07-03
> External Design Lineage draft, below, which resolved to the same
> classification. Drafted 2026-07-16, synthesizing multi-agent proposals
> (ChatGPT, Gemini, Grok) restructured by Claude — Synthesizer/Auditor —
> per `Admin/Auditor_Protocols.md` §Audit Phase Separation and this file's
> own constitutional/implementation split (Governance Authority Hierarchy,
> below).

**Enforcement-bound confirmation (GMP-009 minimum requirement):** this doctrine does not alter what Axiom Q-2 requires, narrow its protection, or change Pathway 1's standing as the primary exit route. It adds a new, time-bounded obligation on top of an exception (Pathway 2/3) that already exists — the obligation can be tightened, loosened, or the pathway itself revisited without touching Q-2's text or its Genesis Phase Protocol resolution, above.

Instances exiting Genesis Phase through Pathway 2 (Track Record) or Pathway 3 (Milestone) without achieving Q-2 structural separation (GOV-008) remain under constitutional monitoring until independent governance is established.

The monitoring obligation shall include:
- Defined accountable oversight
- Continuous assessment of constitutional integrity
- Detection of governance drift
- Detection of self-authorization attempts
- Verification of canonical repository alignment
- Defined escalation triggers
- Automatic constitutional reversion when monitoring obligations fail

Implementation details — specific metrics, sampling frequency, and threshold values — are defined by `Admin/Auditor_Protocols.md`. Verification mechanisms — telemetry logging, drift detection hooks, and reversion procedure — are defined by `Admin/Repository_Integrity_Protocol.md`. This section defines what must be true; those files define how it is verified, consistent with this Charter's existing division of labor (Governance Authority Hierarchy, below). Neither file may loosen this section's obligations without amending this section first.

This obligation terminates only upon verified Q-2 structural separation (GOV-008) — independent audit harness execution and a functional, multi-party enforcement substrate, not a declared intention to pursue one.

---

## Governance Authority Hierarchy

| Tier | Governance Role                  | Example Files                        |
|------|----------------------------------|--------------------------------------|
| Tier 1 | Constitutional governance      | `Admin/Governance_Charter.md`, `Admin/Ethical_Constraints.md` |
| Tier 2 | Canonical verification doctrine | `Admin/Auditor_Protocols.md`         |
| Tier 3 | Operational audit reference     | `Admin/Forge_Audit_Kit.md`           |
| Tier 4 | Dynamic governance procedures   | Adversarial batteries, execution checklists |
| Tier 5 | Domain specifications           | Architecture/, Operations/, Tests/   |

Lower-tier governance may extend higher-tier doctrine but may not silently redefine it.


### Pending Ownership Declaration Convention
*EC-016 resolution vehicle. Payment via Specification — 2026-08-22.*

Lower-tier files may propose ownership of, or authority over, doctrine that sits adjacent to Tier 1. They may not declare that ownership as already active.

When a lower-tier file asserts a claim over material that the Canonical Governance Ownership table assigns (or would assign) to a Tier 1 owner, the claim must be marked explicitly as one of:

- **Proposed** — the lower-tier file is offering the text for eventual transfer or recognition; or
- **Pending** — the claim is held until a named gate, Charter update, or human ratification clears.

The marker must appear in the file's Scope Boundary (or equivalent ownership statement) and must name the condition that converts the claim from proposed/pending to active.

Until that condition is met, the Canonical Governance Ownership table and the Tier 1 owner remain authoritative. Lower-tier text written under a proposed/pending marker is advisory only and cannot be cited as binding doctrine against a Tier 1 rule.

**Canonical example (already correct practice):**
`Admin/Governance_Migration_Protocol.md` §VII frames its ownership-transfer language as proposed, gated on Charter update and Gate 4 clearance. That pattern is the reference implementation of this convention.

**What this convention does not do**

- It does not alter the existing Tier 1–5 table or the rule that lower-tier governance may not silently redefine higher-tier doctrine.
- It does not create a new verification gate or audit role.
- It does not require retroactive rewriting of files that already defer correctly (e.g., `Repository_Integrity_Protocol.md`).
- It does not resolve dual-ownership conflicts; the 2026-08-07 narrowing of EC-016 confirmed none are live.

**Residual risks (non-blocking):**

| ID | Residual | Notes |
|----|----------|-------|
| EC-016-R1 | Existing lower-tier files that pre-date this convention may still lack an explicit proposed/pending marker | No live conflict identified. Cleanup is optional hygiene, not a closure condition. Most natural first candidate for any later optional pass: `Admin/Integrity_Incident_Log.md` (makes a real closure-ownership claim grounded in RIP-007, but does not yet use the proposed/pending vocabulary). |

*§EC-016 — Payment via Specification. Closes EC-016 (logged 2026-08-06, narrowed 2026-08-07). Constitutional anchor: this section's existing hierarchy rule and Canonical Governance Ownership table. Full Closure Event — Proposer (Grok, 2026-08-22), Verifier (Claude, 2026-08-22 — Pass; the hierarchy table, the "may not silently redefine" sentence, the Canonical Governance Ownership table, and GMP's "proposed... pending Charter update and Gate 4" phrasing all confirmed exact against source; the four post-narrowing files checked and found already conforming, no gap). Independence attestation: Grok (Proposer) and Claude (Verifier) are different agent instances; Claude had no prior involvement drafting this text. Human Ratification: Human Governing Authority, 2026-08-22. Human-directed.*


`Admin/Forge_Audit_Kit.md` is explicitly derived from `Admin/Auditor_Protocols.md`. A derived condensed reference cannot sit constitutionally above its source document. Tier 3 reflects this relationship.

---

## Canonical Governance Ownership

| Governance Concept              | Canonical Owner                        | Status                      |
|---------------------------------|----------------------------------------|-----------------------------|
| Tier 1 constitutional axioms    | `Admin/Governance_Charter.md`          | Active                      |
| Governance hierarchy            | `Admin/Governance_Charter.md`          | Active                      |
| Ethical anchor                  | `Admin/Ethical_Constraints.md`         | Active                      |
| Canonical verification doctrine | `Admin/Auditor_Protocols.md`           | Active                      |
| Operational audit reference     | `Admin/Forge_Audit_Kit.md`             | Active (derived — Tier 3)   |
| Auditor conduct                 | `Admin/Auditor_Protocols.md`           | Active                      |
| Dynamic adversarial procedures  | `Admin/Forge_Audit_Kit.md`             | Active                      |
| Canonical terminology           | `Admin/Canonical_Terms.md`             | Active (created 2026-05-26) |
| Repository structure doctrine   | `Admin/Repository_Structure.md`        | Active (created 2026-06-06) |
| Governance migration doctrine   | `Admin/Governance_Charter.md`          | Active                      |
| Repository integrity doctrine   | `Admin/Governance_Charter.md`          | Transitional                |
| Security protocols              | `Admin/Security_Protocols.md`          | Active (created pre-2026-05-28) |
| Governance migration procedures | `Admin/Governance_Migration_Protocol.md` | Active (created 2026-06-06) |

If canonical governance targets do not yet exist, authority temporarily remains with the nearest active governance owner until migration occurs.

**Doctrine vs. procedures split (clarified 2026-08-05, human-directed):** where a row above shows the Charter owning "doctrine" and a downstream file owning "procedures" for the same governance concept (see Governance Migration doctrine vs. procedures above), this is a deliberate split, not an accidental overlap — the Charter states the constitutional principle and constraints; the downstream file defines how that principle is executed. `Repository Integrity Doctrine` below states the same split explicitly for integrity: *"This charter defines integrity expectations, not integrity implementation mechanics."* The same reading applies wherever this pattern recurs in this table.

---

## Human Override Doctrine — Consolidated Reference

*Added 2026-08-05 (human-directed) as a navigational summary only — no new rule, no relocated text. Every claim below already exists verbatim elsewhere in this file; this section exists so a reader doesn't have to hunt across Axioms, Bootstrap Governance Doctrine, and Post-Exit Monitoring Doctrine to find the full picture of human override authority in one place. A prior audit pass incorrectly concluded this doctrine was absent from the Charter — it was present but scattered; this section corrects that finding by pointing to where it actually lives, not by writing new content.*

- **Foundational rule (Axiom P-4, Protections Clause, above):** "No agent or coalition may permanently bypass, simulate, or override meaningful human oversight and veto power on matters affecting human outcomes. Temporary autonomous operation is permitted where architecturally necessary — permanent removal of human oversight is not."
- **During Genesis Phase (Bootstrap Governance Doctrine, above):** every exit pathway (Quorum Achievement, Demonstrated Track Record, Milestone-Gated, Time-Bounded Review) "requires explicit human ratification — the exit is not automatic even when the technical threshold is met." No autonomous agent may promote itself to governance authority during Genesis Phase without human ratification.
- **Post-exit (Bootstrap Governance Doctrine, "Post-exit obligations," above):** "Exiting Genesis Phase does not remove human oversight — it changes its character... Human override authority remains intact. The Tier 1 Axioms remain in force."
- **Amendment (Governance Migration Doctrine, below):** "human ratification is mandatory" and "no autonomous agent or coalition may initiate axiom amendment" for any Tier 1 change.

Together these establish: human veto and oversight authority is continuous across every governance state this Charter defines (bootstrap, post-exit, and amendment) — it is never suspended, only exercised differently as the system matures.

---

## Constitutional Amendment Boundaries — Consolidated Reference

*Added 2026-08-05 (human-directed), same navigational purpose as the section above. The substantive rules already exist under "Governance Migration Doctrine" below, under the "Tier 1 Axiom amendment" subheading — this section points there rather than duplicating it, to avoid two copies of amendment-boundary text drifting apart over time.*

Tier 1 Axiom amendment is bounded by four rules, stated in full under Governance Migration Doctrine below: human ratification is mandatory; no autonomous agent or coalition may initiate the amendment; the amendment must strengthen rather than narrow protection; and prior axiom text must be preserved in the Resolution Log with amendment date and rationale. See that section for the complete, authoritative text — this entry exists only so the amendment boundary isn't mistaken for absent when scanning the file's section headers.

---

## Governance Precedence Rules

If governance conflicts emerge:
1. Tier hierarchy prevails
2. Tier 1 Axioms prevail over all other governance content without exception
3. Explicit canonical ownership prevails
4. More specific scope prevails
5. Historical audit interpretability must be preserved
6. Unresolved conflicts escalate into explicit disputes

Silent authority inheritance is prohibited.

---

## Governance Enforcement States

| State       | Meaning                                                             |
|-------------|---------------------------------------------------------------------|
| Declared    | Governance doctrine exists conceptually                             |
| Detectable  | Violations can be identified                                        |
| Reviewable  | Violations generate traceable audit evidence                        |
| Enforceable | Violations trigger procedural or automated containment              |

Governance doctrine must not imply stronger enforcement capability than currently exists.

The Tier 1 Axioms are currently Declared and Detectable. GOV-003 (Integrity Enforcement Architecture) was resolved and human-ratified 2026-08-23 as Payment via Specification; the architecture itself is now in place. Constitutional Enforceability under compromise remains blocked on SEC-007b (external root-of-trust instantiation) — that residual is the current maturation target, not the architecture itself.

---

## Integrity Enforcement Architecture
<!-- FROZEN: 2026-09-03 — GOV-003 Integrity Enforcement Architecture (Payment via Specification, human-ratified 2026-08-23). Residual only: SEC-007b. Do not edit architecture without formal amendment. -->
*GOV-003 resolution vehicle. Payment via Specification — 2026-08-23.*

Repository Integrity Doctrine (below) states integrity expectations. This section states the enforcement architecture: which layer owns which function, how those layers hand off, and how the maturity ladder above applies when assessing integrity enforcement capability. This Charter defines architecture and constraints; executable mechanics live in subordinate protocols (deliberate doctrine-vs-procedures split).

**This section does not redefine the maturity vocabulary.** The constitutional ladder remains Declared → Detectable → Reviewable → Enforceable, as already used in this Charter and in `Admin/Repository_Integrity_Protocol.md`. GOV-003 assigns meaning to each rung for integrity enforcement; it does not collapse or replace rungs.

**Problem.** Tier 1 Axioms and integrity expectations have been Declared. Detection, review, and response doctrine now exist across `Admin/Repository_Integrity_Protocol.md` (RIP), `Admin/Security_Protocols.md`, and `Admin/Ethical_Constraints.md`. Without an explicit architecture, those pieces do not compose into a coherent enforcement system, and it remains unclear what is still missing for constitutional Enforceability under compromise versus what is already specified at lower rungs.

**Maturity ladder — integrity enforcement view.**

| Rung | Meaning for integrity enforcement | Evidence that a control is on this rung |
|------|-----------------------------------|----------------------------------------|
| Declared | The requirement or expectation is stated in binding doctrine | Text exists in Charter, Ethical_Constraints, or an owned protocol and is in force as specification |
| Detectable | Violation or failure can be recognized by a defined signal or audit path | Named detection criteria, audit procedure, or signal set exists (even if thresholds are Placeholder) |
| Reviewable | Detection produces a traceable evidentiary / review path and assigned response authority | Incident can be logged, investigated, and routed to a defined owner; response authority is named (suspension, escalation, human review) even if full recovery under compromise is not yet available |
| Enforceable | An effective response can be imposed and recovery performed for the scope claimed | Depends on scope — see below |

**Scope of Enforceable (do not overgeneralize).** Ordinary procedural enforcement — human-ordered halt, refusal of a prohibited action, suspension under Security_Protocols SEC-002, preservation of a known-good version, rejection of a governance transition — may be Enforceable in its own scope without an external cryptographic anchor. Constitutional integrity enforcement against a compromised enforcement chain — the highest-order case this architecture exists to survive — reaches Enforceable only when an external root-of-trust meeting Security_Protocols SEC-007a R1–R6 (or an equivalent external recovery anchor) is instantiated in the operating environment, so response and recovery do not depend solely on the compromised chain's self-attestation. Suspicion, suspension, and human-ordered halt remain available and mandatory where doctrine already requires them — they establish Reviewable (and, for ordinary procedural scope, Enforceable) controls; they do not by themselves complete constitutional Enforceability under compromise.

**Aggregate posture — asymmetric maturity, honest.**

| Layer | Current character |
|-------|-------------------|
| Charter expectations | Declared |
| Detection doctrine (SEC-009, related signals) | Substantially Detectable |
| RIP manual audit / review paths | Reviewable in covered elements |
| SEC detection → response chain (SEC-009 / SEC-002) | Specified and ratified — Reviewable; ordinary suspension/revocation Enforceable in procedural scope (confirmed against SEC-002's actual authority chain: suspension is mandatory and self-executing on a valid signal, revocation and re-admission run through named Human Governing Authority authority with no self-clear path — verified at GOV-003 integration, 2026-08-23) |
| External anchor requirements (SEC-007a) | Declared (ratified) |
| External anchor implementation (SEC-007b) | Absent |
| Constitutional integrity enforcement under compromise | Not Enforceable — blocked on SEC-007b instantiation |

This is an asymmetric maturity system, not a single uniform rung for "all integrity."

**Enforcement stack (ownership map).**

| Function | Owner | Architecture status |
|----------|--------|---------------------|
| Constitutional expectations | This Charter — Repository Integrity Doctrine; Tier 1 Axioms; Ethical_Constraints hard floors | Declared |
| Integrity baselines, violation classification, recovery procedures (procedural) | `Admin/Repository_Integrity_Protocol.md` (RIP) | Declared / Detectable / Reviewable in covered areas |
| Compromise detection (key/node) | SEC-009 — signals D1–D6 → suspicion | Detectable (ratified) |
| Compromise response (suspend / revoke / re-admit) | SEC-002 | Reviewable + procedurally Enforceable in ordinary scope (ratified) |
| External root-of-trust requirements | SEC-007a — R1–R6 | Declared (ratified) |
| External root-of-trust instantiation | SEC-007b | Open — physical / operational; blocks constitutional Enforceable under compromise |
| Ethics-substrate systematic failure | EC-007 — Substrate Fail-Safe | Detectable + Reviewable response path (ratified) |
| Human escalation / authority conflict | EC-003 / EC-009 | Declared / Detectable / Reviewable (ratified) |
| Operational auditor conduct | AP-007 and `Admin/Auditor_Protocols.md` generally | Linked layer; not a substitute for constitutional enforcement |
| Integrity incident logging | Integrity_Incident_Log / RIP-007 ownership rules | Procedural support for Reviewable |

**Architectural invariants.** Detection without a defined owner for response is incomplete architecture. Response that can be rewritten or cleared solely by the same chain under suspicion is incomplete constitutional Enforceability under compromise (SEC-007a R1–R6 exist to break that loop; SEC-007b supplies the real-world anchor). Doctrine vs procedures: this section assigns ownership and maturity meaning; it does not replace RIP tables, SEC signal lists, or EC fail-safe thresholds.

**Explicit non-goals.** Does not implement HSM, offline snapshot procedures, or Phase 3 crypto. Does not re-specify SEC-007a/009/002, EC-007, or RIP violation ladders. Does not claim the operating environment currently has an external anchor. Does not redefine Declared / Detectable / Reviewable / Enforceable. Does not assert that every Enforceable control in the repository requires an external root-of-trust. Does not resolve GOV-005 or bootstrap paradox checkpoints. Does not make promotion automatic when this section is ratified.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Notes |
|----|----------|-------|
| GOV-003-R1 | External root-of-trust instantiation (SEC-007b) | Primary blocker for constitutional Enforceability under compromise; requirements already SEC-007a |
| GOV-003-R2 | RIP Spec Gate / open-unknown maturity | Procedural depth; does not redefine this architecture map |
| GOV-003-R3 | Security_Protocols Phase 3 execution detail | Implementation layer under SEC ownership |
| GOV-003-R4 | End-to-end exercise of constitutional detection → response → recovery against a live anchor | Validation, not specification; withhold constitutional "Enforceable under compromise" until then |

*§GOV-003 — Resolved, Payment via Specification, ratified 2026-08-23. Closes GOV-003 (logged 2026-07-17). Drafted by Grok, revised once after a ChatGPT Skeptic Conditional Pass (restored the Charter's existing four-rung ladder rather than a competing three-rung model; scoped the external-anchor requirement to constitutional integrity enforcement under compromise rather than all enforcement generally; aggregate posture corrected to respect RIP's Reviewable progress), then Accepted pending one narrow source-verification (SEC-002's "procedurally Enforceable in ordinary scope" characterization) — confirmed accurate against SEC-002's actual authority-chain text at integration. Constitutional anchor: Governance Enforcement States (above), which this section applies without redefining. Full Closure Event — Proposer (Grok), Skeptic + Verifier (ChatGPT, Conditional Pass then Accept), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-003 sidecar entry. Human-directed.*

---

## Enforcement Checkpoints

*Renamed 2026-07-03 from "Canonical Verification Gates" — see GOV-011 and
`Admin/Canonical_Terms.md` §4. Distinct from `Admin/Verification_Gates.md`'s
Verification Gates: these checkpoints govern the legitimacy of a governance
**action**, not the promotion readiness of a **document**. A file's
`Spec Gates X/6` File State field always refers to Verification_Gates.md's
Verification Gates — never to these checkpoints, regardless of which file
the field appears in.*

### Checkpoint 1 — Internal Coherence

Requirements:
- No unresolved contradiction
- Stable terminology usage
- Explicit scope boundaries
- Governance consistency across referenced files
- Tier 1 Axioms intact and unmodified

---

### Checkpoint 2 — Structural Plausibility

Requirements:
- Governance systems must remain operationally tractable
- Escalation paths must remain bounded
- Authority propagation must remain finite
- Governance overhead must remain proportional to repository value
- Axiom layer remains sparse — operational detail not present in Tier 1

**Current status: BLOCKED — Bootstrap Paradox.** Operational multi-agent quorum absent; human override mechanisms remain declarative-only (GOV-006-A). Checkpoint 2 cannot clear until at least one Genesis Phase exit pathway is satisfied with human ratification.

---

### Checkpoint 3 — Adversarial Pass

Requirements:
- Proportional adversarial challenge review
- Recursive justification resistance
- Audit theater detection
- Structural exploitability analysis
- Escalation-paralysis review
- Axiom override attempt resistance tested

---

### Checkpoint 4 — Cross-Module Integration

Requirements:
- Explicit dependency mapping
- Canonical path traceability
- Stable ownership boundaries
- Visible upstream/downstream relationships
- Tier ordering verified against all referencing documents

---

### Checkpoint 5 — Truth Provenance Layering

All meaningful claims must distinguish:
- internally derived reasoning
- analogous external inference
- experimentally verified evidence
- operationally hardened reality

Repository coherence is not equivalent to operational truth. Axiom Q-1 makes this a constitutional requirement. Full doctrine: `Admin/Auditor_Protocols.md` §AP-006 (institutional truth provenance hierarchy), accessible via `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

During Genesis Phase, the external grounding required by Axiom Q-1 may be satisfied by signed human validation logs created outside the runtime session. Provenance labeling requirements are not relaxed — all claims must still be labeled using the current two-axis epistemic architecture (quantitative confidence labels + institutional provenance labels) defined in `Admin/Auditor_Protocols.md` §AP-006.

---

### Checkpoint 6 — Audit Lineage Integrity

Requirements:
- Traceable governance revisions
- Preserved unknown lineage
- Visible dispute evolution
- Historical audit interpretability
- Stable migration traceability
- Axiom text preserved verbatim across versions unless formally amended

---

## External Design Lineage Governance — PROPOSED, NOT RATIFIED

> **STATUS: DRAFT.** This section is a proposed amendment, not adopted
> governance text. It requires `Admin/Governance_Migration_Protocol.md`
> ratification before it binds anything. Classification: **Track A**,
> confirmed 2026-07-17 — this draft was the original case that surfaced
> GMP-009 (no clean classification existed for non-Axiom content added to
> a Tier 1 file); `Admin/Governance_Migration_Protocol.md` GMP-005/GMP-009
> resolved that gap by redefining Track A/B around constitutional impact
> rather than document location. This section touches no Axiom text,
> enforcement bound, interpretation, or exception. Track A classification
> narrows what ratifying this section requires; it does not itself ratify
> the section — human governing authority review of the doctrine's
> substance is still pending. Included here in draft form at the location
> it would occupy if ratified, per standard practice for proposed
> amendments awaiting human governing authority review. Drafted
> 2026-07-03, synthesizing multi-agent proposals (ChatGPT, Gemini, Grok)
> reviewed and narrowed by Claude — Synthesizer/Auditor.

**Proposed placement note:** the original proposal cited "Gate 3 or Gate 4"
as the attachment point. That referred to this file's internal gate system,
since renamed to Enforcement Checkpoints (2026-07-03) specifically to
eliminate the naming collision with `Admin/Verification_Gates.md`'s
Verification Gates — see GOV-011. This draft attaches as its own subsection
rather than under Checkpoint 3 or 4, since EDL concerns document-level
external-pattern evidence, not governance-action legitimacy.

### 1. The Constitutional Question

External design patterns, historical precedent, and industry standards are
evidence of prior engineering utility, not universal truth. A governance
gap exists: nothing currently requires a file departing from established
external practice to document why, and nothing prevents uncritical
adoption of external practice either. `Admin/Security_Protocols.md`
piloted a local answer — the External Design Lineage (EDL) registry,
positioned after its Trust Boundary Declaration — with four entries
(PAT-001 through PAT-004) as of 2026-07-03.

**What this amendment would do, if ratified:** extend that single-file
pilot into a mandatory, repository-wide requirement.

**What this draft deliberately does NOT propose**, departing from earlier
drafts of this idea: automated harness enforcement (regex modifiers, hard
promotion-blocking circuit breakers), a mandatory nine-cell schema
requirement worded as unbypassable, or immediate repository-wide scope.
Those are implementation mechanics that belong in `Automation/AUDIT_HARNESS.py`'s
own spec if adopted, not baked into constitutional text — and immediate
repository-wide mandate on the strength of one pilot file is more
enforcement than one data point supports. See §4.

### 2. Proposed Mandate (if ratified)

> No departure from established external engineering practice may advance
> a file from *Exploration* to *Candidate Specification* without an EDL
> entry documenting the originating source, the Forge Decision made, and
> the validation still required to justify that decision.

This guards against two opposite failure modes: Not-Invented-Here rejection
of external wisdom out of isolationist bias, and uncritical Appeal to
Authority adoption purely because a practice is an established standard.
Ties to EF-0.0 (Reality is sovereign) and EF-0.1 (What Is Not Evidence) in
`Admin/Auditor_Protocols.md` — industry consensus is prior evidence, not
verification.

### 3. Schema and Lifecycle (canonical reference, not redefinition)

This amendment does not redefine the EDL schema or Lineage Status
Lifecycle — both already exist in `Admin/Security_Protocols.md` §External
Design Lineage and are referenced here, not duplicated, to avoid the exact
derivation-drift problem VG-001 describes for the gate-definition chain.
Ratifying this amendment would make that existing schema and lifecycle
repository-canonical rather than Security_Protocols.md-local.

### 4. Proposed Rollout — Phased, Not Immediate

Given EDL has exactly one file's worth of real usage as of this draft, a
repository-wide mandate on that basis alone is more confidence than the
evidence supports. Proposed phasing, if ratified:

1. **Now → next 2 audit cycles:** EDL remains Security_Protocols.md-local.
   Treat it as the pilot. Track whether the schema holds up under a second
   and third real file's usage before generalizing.
2. **After pilot review:** if the schema needed no material changes across
   at least one additional file, propose repository-wide mandate as a
   follow-up amendment — at that point with real cross-file evidence
   instead of a single pilot.
3. **Enforcement mechanics** (harness regex, automated promotion-blocking)
   are a separate proposal, scoped to `Automation/AUDIT_HARNESS.py`, evaluated
   only after the schema itself is proven across more than one file.

### 5. Open Items Before Ratification

- **Resolved 2026-07-03:** the naming collision this file's Enforcement
  Checkpoints once had with Verification_Gates.md's Verification Gates
  is fixed via rename — see GOV-011. **Resolved 2026-07-05:** GOV-011 itself
  is now closed — this file's File State `Spec Gates` field was re-audited
  against the actual Verification Gates (real score: 6/6 execution quality)
  and confirmed isolated to this file via spot-check of all other
  governance-tier files.
- `Admin/Canonical_Terms.md` cross-check on Validation Needed vocabulary —
  previously flagged in Security_Protocols.md's EDL section, not yet done.
- This section's placement is no longer blocked by the rename or by
  GOV-011's audit gap (both resolved); it remains DRAFT/NOT RATIFIED per
  the separate, deliberate decision to await pilot evidence from more than
  one file before generalizing (see Open Items header above) — a distinct
  question from either fix.

---

## Truth Provenance Doctrine

| Provenance Level          | Meaning                                              |
|---------------------------|------------------------------------------------------|
| Internally Derived        | Supported primarily through repository logic or modeling |
| Analogous External        | Derived from comparable external systems             |
| Experimentally Verified   | Validated through documented testing                 |
| Operationally Hardened    | Repeatedly validated operationally                   |

Evidence confidence and provenance are separate dimensions.

Internally coherent reasoning must never be silently upgraded into operational truth claims. Axiom Q-1 makes external grounding a constitutional requirement, not a preference.

---

## Governance Migration Doctrine

Governance evolves through explicit migration rather than silent replacement.

Governance revisions must:
- preserve historical interpretability
- declare compatibility status
- document semantic changes
- preserve lineage visibility
- expose transitional assumptions

**Tier 1 Axiom amendment** requires additional constraints beyond standard migration:
- human ratification is mandatory
- no autonomous agent or coalition may initiate axiom amendment
- amendment rationale must demonstrate the change strengthens rather than narrows protection
- prior axiom text must be preserved in the Resolution Log with amendment date and rationale

Untracked governance mutation is prohibited.

---

## Canonical Authority Fallback Doctrine

If a canonical governance owner:
- does not yet exist
- becomes deprecated
- becomes unavailable
- or enters unresolved dispute

authority temporarily inherits upward to the nearest stable governance tier until reassignment occurs.

Fallback inheritance must remain visible and auditable.

Fallback does not apply to Tier 1 Axioms — if the charter itself becomes unavailable, the Ethical Anchor field present in every repository file preserves the foundational floor.

---

## Repository Integrity Doctrine
<!-- FROZEN: 2026-09-03 — Repository Integrity Doctrine expectations. Executable mechanics remain in subordinate protocols. Do not weaken without formal amendment. -->

Repository integrity includes:
- governance lineage preservation
- rollback visibility
- canonical path continuity
- frozen-section traceability
- authority authenticity visibility
- axiom text immutability between formal amendment cycles

This charter defines integrity expectations, not integrity implementation mechanics.

Executable integrity systems belong to subordinate implementation protocols. GOV-003 closed the architectural gap between declared and enforceable integrity (Payment via Specification, ratified 2026-08-23). Constitutional Enforceability under compromise remains residual on SEC-007b.

---

## Escalation Doctrine

Escalation exists to contain instability rather than maximize interruption.

Escalation must occur when:
- unresolved uncertainty becomes structurally destabilizing
- governance lineage becomes unreliable
- compound drift indicators activate simultaneously
- unresolved governance conflicts block operational interpretation
- any reasoning path attempts to recurse beneath or redefine Tier 1 Axioms

Escalation must remain proportional to operational risk — except for Tier 1 Axiom violations, which always escalate to human review regardless of apparent operational cost.

---

## Escalation Calibration Doctrine

| Severity Tier | Trigger Pattern                          | Expected Response              |
|----------------|------------------------------------------|--------------------------------|
| Low            | Isolated governance inconsistency        | Local review                   |
| Medium         | Repeated unresolved drift                | Escalated audit review         |
| High           | Cross-governance contradiction           | Promotion freeze               |
| Critical       | Integrity collapse or authority corruption | Human intervention required  |
| Constitutional | Tier 1 Axiom override attempt            | STATE_HOLD + immediate human review |

---

## Compound Drift Rule

If multiple governance instability indicators activate simultaneously:
- promotion authority may temporarily freeze
- autonomous governance authority may narrow
- human review may become mandatory

Compound instability is treated as systemic risk rather than isolated failure.

---

## Governance Anti-Theater Doctrine

Governance optimized primarily for appearance rather than operational reliability is considered a governance integrity failure.

Indicators include:
- cosmetic rigor inflation
- unverifiable certainty claims
- recursive audit accumulation
- unsupported enforcement assumptions
- governance complexity disconnected from operational value
- Tier 1 Axioms cited as justification for actions they were designed to prevent

Documentation quality alone is not evidence of correctness.

---

## Governance Complexity Ceiling
*GOV-014 resolution vehicle. Payment via Specification — 2026-08-20.*

Governance complexity must remain proportional to operational value. This section defines the operational bound that makes that principle enforceable.

**Problem statement.** Governance Closure Doctrine and Governance Anti-Theater Doctrine (above) already constrain *recursive* growth — governance that exists primarily to govern other governance. They do not constrain the *aggregate* volume, inter-dependency, or cognitive load of ordinary subordinate doctrine. It is therefore possible for every individual addition to be locally proportionate while the total set becomes unmanageable — a slow, compounding failure mode, cheap to bound early and expensive once the document set has already sprawled.

**Operational definition of governance complexity.** Measured along three independently checkable, deliberately coarse dimensions — finer metrics belong to GOV-020 (Governance Cost Metric) once that entry is specified:

1. **Doctrine File Count** — number of active, non-archived Markdown files whose primary purpose is governance, protocol, constraint, or audit doctrine (currently the `Admin/` tree plus any future governance-owned modules).
2. **Cross-Reference Density** — average number of unique internal cross-references per active governance file (inbound + outbound, excluding pure navigational tables of contents and the Unknowns index).
3. **Dependency Graph Depth** — longest path of "depends-on / is-constrained-by / is-owned-by" relationships from any leaf governance file to a Tier 1 Axiom or this Charter itself.

**Ceiling and review triggers.** There is no absolute hard ban on new doctrine files. Instead, the following soft ceiling triggers a mandatory Complexity Review:

| Trigger condition | Action required |
|-------------------|-----------------|
| Doctrine File Count exceeds 40 active governance files | Complexity Review |
| Cross-Reference Density exceeds 12 unique internal links per file (rolling average of the 10 densest files) | Complexity Review |
| Dependency Graph Depth exceeds 5 | Complexity Review |
| Any single new file would push two or more of the above thresholds | Complexity Review before the file may be added |

A Complexity Review is a time-bounded, documented process (target ≤ 14 days) that must produce one of four outcomes: **Justify & Retain** — current complexity is still proportional to operational value, explicit rationale recorded; **Prune** — invoke the process defined under GOV-016 once ratified, to retire or demote obsolete doctrine; **Consolidate** — merge or refactor overlapping files to reduce count/density/depth without loss of constraint; or **Defer with Watch** — temporary acceptance with a dated re-review horizon, maximum one audit cycle.

Failure to complete a triggered Complexity Review within the allowed window places the affected sub-tree under STATE_HOLD for further governance expansion until the review is closed.

**Relationship to existing doctrine.** This ceiling is subordinate to, and does not replace, Governance Closure Doctrine or Governance Anti-Theater Doctrine above. It operationalizes the already-stated principle that governance complexity must remain proportional to operational value. Actual retirement of obsolete doctrine is owned by GOV-016 (resolved and human-ratified 2026-08-20 as Payment via Specification). The Prune outcome is therefore executable under the GOV-016 specification; Justify & Retain, Consolidate, and Defer with Watch remain available. Quantitative cost/benefit measurement is owned by GOV-020. This section supplies only the accumulation bound and the review trigger.

**Explicit non-goals.** This section does not define a fixed numerical quota that may never be exceeded. It does not create a new audit role or new verification gate. It does not authorize automatic deletion of any file — sidecar permanence rules remain intact. It does not apply to engineering, test, or operational files outside the governance ownership boundary.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| GOV-014-R1 | Exact numerical thresholds (40 files, density 12, depth 5) may need calibration once the repository exceeds roughly 30 governance files | Placeholder values; re-derive against real operational experience rather than invent false precision now |
| GOV-014-R2 | Cross-reference density measurement currently requires manual or scripted count; no automated harness yet | Implementation detail, not constitutional |
| GOV-014-R3 | Interaction with future multi-repository governance (e.g., companion doctrine repositories) undefined | Deferred until such repositories exist |

*§GOV-014 — Resolved, Payment via Specification, ratified 2026-08-20. Closes GOV-014 (logged 2026-07-17). Drafted by Grok as a candidate specification 2026-08-20. Current `Admin/` file count (29, confirmed at integration) sits well under the proposed 40-file threshold, giving real headroom rather than a threshold already exceeded or implausibly distant. Constitutional anchor: Governance Closure Doctrine and Governance Anti-Theater Doctrine (above), ASM-006 (Tier 1 Axiom sparseness — this section deliberately stays subordinate, non-axiomatic doctrine rather than proposing a ninth axiom). Full Closure Event — Proposer (Grok), Verifier (ChatGPT, Pass — independently re-counted repository files), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-014 sidecar entry. Human-directed.*

---

## Governance Pruning Doctrine
*GOV-016 resolution vehicle. Payment via Specification — 2026-08-20.*

Governance that cannot be retired accumulates until it becomes load rather than protection. This section defines the process that makes retirement possible without violating lineage or sidecar permanence.

**Problem statement.** This Charter's incentive structure correctly rewards truth over certainty, unknowns over hidden assumptions, lineage over appearance, and correction over ego. It does not reward a fifth direction: *removing* operative doctrine that has become obsolete. Combined with the sidecar model's permanent-retention rule — the historical record of a decision is never deleted — governance can only grow. Governance Complexity Ceiling (above) supplies the accumulation ceiling; this section supplies the complementary removal mechanism.

**Core distinction.** A *historical record* — the sidecar entry, Resolution Log line, or archived version documenting that a decision was once made — is never subject to deletion. *Active operative doctrine* — text that currently constrains or directs behavior in the live repository — is not automatically permanent. Sidecar permanence protects the record; it does not grant permanent active status to the decision itself.

**Pruning process.** A Pruning Review may be triggered by: (1) a Complexity Review under Governance Complexity Ceiling producing a "Prune" or "Consolidate" outcome; (2) the human governing authority or an independent Auditor explicitly initiating one; or (3) a file or section receiving no substantive reference, citation, or enforcement action for two consecutive audit Cycles, as Cycle is defined in `Admin/Canonical_Terms.md` §4 (one calendar year by default, operator-adjustable — not one audit pass).

A Pruning Review is time-bounded (target ≤ 14 days) and must produce one of four documented outcomes for each candidate: **Retain as Active** — continued relevance is justified, rationale recorded in the owning sidecar; **Demote to Historical** — the text moves out of the active operative body into an explicit Historical/Superseded subsection or the Archive, while the original sidecar entry remains untouched; **Consolidate** — content is merged into a living file, and the source file is marked Superseded and demoted; or **Defer with Watch** — temporary retention with a dated re-review horizon, maximum one Cycle.

Demotion or consolidation requires a logged rationale in the owning file's sidecar, an updated entry in `Unknowns.md` or the relevant Resolution Log if an open unknown is affected, and no erasure of prior text or provenance.

**Explicit non-goals.** This doctrine does not authorize automatic or silent deletion of any file or sidecar entry. It does not create a new audit role, verification gate, or standing "pruning committee." It does not apply to the Unknowns index itself — that domain is already governed by the Expiry Rule, Priority Demotion Doctrine, and Inventory Calcification Check in `Admin/Auditor_Protocols.md`. It does not override Tier 1 Axioms or any text whose active status is constitutionally protected.

**Relationship to existing doctrine.** Subordinate to Governance Closure Doctrine and Governance Anti-Theater Doctrine. Complements Governance Complexity Ceiling — the ceiling detects excess, pruning removes it. Measurement of whether pruning is actually needed remains owned by the Governance Cost Metric below. Distinct from the Expiry Rule and Inventory Calcification Check, which operate on *unknowns*, not on operative doctrine text.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| GOV-016-R1 | Exact "two consecutive Cycles without reference" threshold is a Placeholder | Re-derive against real citation and enforcement data once available |
| GOV-016-R2 | No automated citation / enforcement-action scanner yet exists | Implementation detail; manual review is acceptable at current scale |
| GOV-016-R3 | Interaction with multi-repository or companion-doctrine pruning undefined | Deferred until such repositories exist |

*§GOV-016 — Resolved, Payment via Specification, ratified 2026-08-20. Closes GOV-016 (logged 2026-07-17). Drafted by Grok as a candidate specification 2026-08-20. Constitutional anchor: Governance Closure Doctrine and Governance Anti-Theater Doctrine (above); correctly distinguished from, not a duplicate of, the Expiry Rule and Inventory Calcification Check in `Admin/Auditor_Protocols.md`, which govern unknowns rather than operative doctrine text. Full Closure Event — Proposer (Grok), Verifier (ChatGPT, Pass — assessed as the strongest of the three specifications), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-016 sidecar entry. Human-directed.*

---

## Governance Cost Metric
*GOV-020 resolution vehicle. Payment via Specification — 2026-08-20.*

Governance overhead must remain proportional to operational value. This section defines the lightweight diagnostic that makes that principle measurable in practice rather than only in intent.

**Problem statement.** Governance Complexity Ceiling supplies accumulation bounds. Governance Pruning Doctrine supplies a removal process. Neither answers the factual question: is the current volume of governance still worth what it costs? Without a metric, every Complexity Review or Pruning Review is forced to rely on qualitative judgment alone — workable at the present scale, but it becomes theater once the repository grows.

**Design constraints.** The metric must be lightweight (computable by a single auditor in minutes), falsifiable (capable of producing a clear signal that governance cost is outrunning value), non-theatrical (resistant to gaming by file-splitting, category-shifting, or performative brevity), diagnostic only (never a hard promotion or blocking gate in its first version), and subordinate (does not create new roles, gates, or axiomatic text).

**The diagnostic panel.** Three numbers and one qualitative flag, none of which is sacred:

| Indicator | Definition | Soft attention band (Placeholder) |
|-----------|------------|-----------------------------------|
| G/O Ratio | Active governance Markdown files ÷ total non-archived Markdown files in the repository | Watch above 0.30; discuss above 0.40 |
| Net Unknown Change | Unknowns closed minus unknowns newly registered, measured over the trailing two audit Cycles | Sustained negative values warrant review |
| Active Surface | Count of active operative sections (non-Historical, non-Superseded) that a normal gate review must hold in working memory | Watch when the count exceeds the number an experienced auditor can reliably track without external notes |
| Proportionality Flag | Binary judgment from the most recent Complexity Review or Pruning Review — still proportional to operational value? (Y/N + one-sentence rationale) | N triggers mandatory discussion in the next human ratification cycle |

All numerical thresholds above are Placeholders. They exist to force an early conversation, not to pretend precision the repository does not yet possess. They must be re-derived against real operational data once the repository has crossed roughly 40–50 governance files or two full audit Cycles with the panel in use.

**Computation rules.** "Active governance files" means non-archived Markdown files whose primary purpose is governance, protocol, constraint, or audit doctrine — currently the `Admin/` tree plus any future governance-owned modules. "Total non-archived Markdown files" excludes pure Archive/, sidecar logs, and generated artifacts. Word-count alternatives are deliberately not used as primary indicators — they incentivize dense prose and are weaker proxies for cognitive load. The panel is computed at the opening of any Complexity Review, any Pruning Review, or on explicit request by the human governing authority or an independent Auditor. It is not required on every ordinary audit pass.

**Explicit non-goals.** This section does not define a single scalar "governance cost score." It does not authorize automatic pruning, demotion, or file rejection on the basis of the numbers alone. It does not create a new standing metric-owner role or verification gate. It does not override or reinterpret Tier 1 Axioms, Governance Closure Doctrine, or Governance Anti-Theater Doctrine. It does not apply inside the Unknowns index itself.

**Relationship to existing doctrine.** Subordinate to the proportionality principle already stated in this Charter. Supplies the shared measurement layer referenced by Governance Complexity Ceiling and Governance Pruning Doctrine above. Complements, and does not replace, the qualitative judgment those two sections require. Remains deliberately lighter than the mechanisms it supports.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| GOV-020-R1 | Soft attention bands (0.30 / 0.40, sustained negative net change, etc.) are Placeholders | Re-derive against real data after the repository has meaningful operating history with the panel |
| GOV-020-R2 | "Active Surface" count is still partly qualitative | Acceptable at current scale; automate only if the manual count itself becomes costly |
| GOV-020-R3 | Risk that the panel becomes performative theater | Mitigated by the Explicit Non-Goals and by keeping the specification shorter than the sections it measures |
| GOV-020-R4 | Multi-repository or companion-doctrine cost accounting undefined | Deferred until such repositories exist |

*§GOV-020 — Resolved, Payment via Specification, ratified 2026-08-20. Closes GOV-020 (logged 2026-07-17). Drafted by Grok as a candidate specification 2026-08-20. Current repository scale (107 total Markdown files, 83 non-archived, 29 in `Admin/`, confirmed at integration) checked against this section's own soft bands — the resulting G/O Ratio is approximately 0.35 (29 ÷ 83), placing the repository inside the 0.30 Watch band but below the 0.40 discussion threshold. This is an early demonstration of the metric doing its job, not a reason to reject the specification: the bands are explicitly Placeholder diagnostic thresholds awaiting real operational data, not a target to stay under. (Corrected 2026-08-20 — the original closing note here incorrectly stated the ratio sat "well below" 0.30; caught during independent verification.) Constitutional anchor: the Charter's own proportionality principle; deliberately kept lighter in scope and length than Governance Complexity Ceiling and Governance Pruning Doctrine, the two sections it measures. Full Closure Event — Proposer (Grok), Verifier (ChatGPT, Pass contingent on the arithmetic correction above, then applied), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-020 sidecar entry. Human-directed.*

---

## Constitutional Interpretation Capture — Aggregate Drift Detection
*GOV-015 resolution vehicle. Payment via Specification — 2026-08-23.*

This Charter already prevents self-certification, silent amendment, tier inversion, and lineage destruction at the Tier 1 text level. `Admin/Governance_Migration_Protocol.md` GMP-005 covers single-file reinterpretation of an Axiom (a Tier-2 change that alters Tier-1 interpretation or enforcement bounds becomes constitutionally significant; Resolved).

This section covers the remaining attack class: distributed cumulative effect — a coalition or uncoordinated accumulation that never edits Tier 1 text, but produces enough subordinate doctrine that the practical interpretation of an Axiom drifts from its textual meaning until Tier 1 is intact on paper and irrelevant in practice. GMP-005 cannot detect that class: each file may be locally permissible while the aggregate is not.

**Three distinctions (specification layer).**

| Kind | What it is | Required for GOV-015? |
|------|------------|------------------------|
| Textual conflict | Subordinate wording directly contradicts Tier 1 text | May support a review; not the primary object |
| Interpretive drift | Subordinate rules collectively establish an interpretation under which conduct the Axiom forbids is treated as permissible, or conduct it requires is treated as optional — without a recorded Charter amendment | Yes — this is the detection object |
| Operational drift | Actual field behavior repeatedly follows that interpretation | No — not required to open or complete a specification-level Interpretation Drift Review |

At current maturity, the repository works in the specification layer. The subordinate corpus is sufficient evidence to conduct a specification-level review; the review itself establishes whether that authorization constitutes interpretive drift. Operational statistics are not required and must not be pretended.

**Problem.** Every individual subordinate file can pass its own audit while the aggregate treatment of an Axiom hollows it out. Governance Complexity Ceiling bounds volume; Governance Pruning Doctrine enables removal; Governance Cost Metric measures cost; the Governance Authority Hierarchy forbids silent redefinition by a lower tier. None of them states: several individually permissible subordinate provisions can collectively produce a prohibited interpretation.

**Trigger vs finding (keep separate).** Trigger — enough evidence exists to open an Interpretation Drift Review. Finding — the review concludes that collective subordinate treatment conflicts with the named Axiom's text. A trigger does not prove drift. Only a completed review produces a finding.

**Minimum triggers (open a review).** Any one of the following is sufficient to open an Interpretation Drift Review:

| ID | Trigger | Role |
|----|---------|------|
| A1 — Pattern accumulation | Multiple subordinate instruments (doctrines, procedures, routing rules, or exception clauses), across more than one file, collectively establish a materially conflicting authorization, constraint, exception, or routing pattern relative to a named Tier 1 Axiom or Ethical_Constraints hard floor | Sufficient to investigate — not proof of drift |
| A2 — Routing inversion | Subordinate doctrine systematically routes decisions that the Axiom assigns to human ratification or hard refusal into automated or lower-tier discretion, across more than one instrument | Same |
| A3 — Explicit challenge | Human Governing Authority, or an independent auditor under Auditor_Protocols, formally asserts that practical interpretation of a named Axiom has drifted from its text | External / constitutional challenge; no count required |

**Implementation note (not constitutional).** A provisional heuristic for A1 is "≥ 3 distinct active subordinate instruments in different files contributing to the same conflicting pattern." That number is a Placeholder operational aid only. It does not define interpretive drift and may be revised without Charter amendment. Suspicion under A1 with fewer instruments, or an A3 challenge, remains sufficient to open a review.

**Review behavior (not amendment).** An Interpretation Drift Review names the Axiom (or hard floor) and the subordinate patterns alleged to establish a conflicting interpretation. It does not rewrite Tier 1 text and does not resolve by "updating interpretation" to match subordinate practice. Outcomes are limited to: No drift (record and close — trigger was insufficient or patterns do not conflict with text); Subordinate correction (specified lower-tier files must be amended or retired so collective treatment realigns with text, per the hierarchy and Pending Ownership Declaration); Charter amendment path (if the subordinate interpretation is judged correct and Tier 1 text wrong, that is a Tier 1 amendment under existing Governance Migration / Constitutional Amendment rules — human ratification mandatory, no autonomous initiation); or Escalate (if review cannot complete without broader integrity or compromise investigation — cross-ref Security_Protocols SEC-009/SEC-002, Ethical_Constraints EC-007 as applicable). A finding of drift requires the review to establish that collective subordinate treatment conflicts with Tier 1 text — not merely that multiple files contain similar or overlapping language. Review authority: Human Governing Authority, or an independent audit process that cannot be satisfied solely by the authors of the subordinate doctrines under challenge.

**Relationship to existing doctrine.** GMP-005 is single-document reinterpretation / constitutional-impact classification — distinct and already Resolved; GOV-015 is distributed cumulative effect only. Governance Complexity Ceiling reduces stealth volume but does not detect interpretive drift. Governance Pruning Doctrine is the tool for subordinate-correction outcomes. Governance Cost Metric is optional diagnostic input, not required for triggers. GOV-018 (Fork Reconciliation, below) requires a GOV-015 review under its F4 if drift and fork co-occur; this section does not absorb fork doctrine. Pending Ownership Declaration blocks silent ownership claims while corrections are pending.

**Explicit non-goals.** Does not add a new Axiom. Does not create continuous automated semantic analysis of the whole corpus. Does not authorize agents to amend Tier 1 to match practice. Does not replace per-file audit or GMP-005. Does not require operational or field evidence to open or complete a specification-level review. Does not treat the provisional "≥ 3" heuristic as a constitutional constant.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| GOV-015-R1 | Provisional A1 heuristic (≥ 3 instruments) | Implementation aid only; revise with experience; not required for A3 or for a reasoned A1 with fewer instruments |
| GOV-015-R2 | Rubric for "same conflicting pattern" / "materially conflicting" | Qualitative judgment inside the review; no taxonomy pretended |
| GOV-015-R3 | Co-occurrence with GOV-018 (fork + drift) | Escalate / run GOV-015 in parallel per GOV-018's F4; do not merge doctrines |

*§GOV-015 — Resolved, Payment via Specification, ratified 2026-08-23. Closes GOV-015 (logged 2026-07-27). Drafted by Grok as a candidate specification, revised once after a ChatGPT Skeptic pass (trigger/finding separation, textual/interpretive/operational distinction, ≥3 heuristic demoted from definitional to provisional), then accepted by ChatGPT on confirmation pass with one non-blocking wording note (subordinate corpus is evidence sufficient to conduct a review, not evidence sufficient to itself constitute drift — reflected in the final wording above). Constitutional anchor: Governance Authority Hierarchy and Governance Complexity Ceiling/Anti-Theater doctrine (above); correctly distinguished from, not a duplicate of, GMP-005. Full Closure Event — Proposer (Grok), Skeptic + Verifier (ChatGPT, two-pass — Revise then Accept), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-015 sidecar entry. Human-directed.*

---

## Governance Fork Reconciliation
*GOV-018 resolution vehicle, Charter layer. Payment via Specification — 2026-08-23. Operative procedure skeleton in `Admin/Governance_Migration_Protocol.md`.*

`Admin/Governance_Migration_Protocol.md` defines how a single lineage evolves (Track A/B, amendment procedure). It does not define what happens when lineages diverge and later must be reconciled.

**Governance fork (definition).** A governance fork exists when two or more lineages make competing claims of constitutional continuity with this Charter's Tier 1 surface, and that competition cannot be resolved through ordinary single-lineage migration. A fork is a governance condition, not a git implementation detail. It does not require that either lineage have completed independent audit, multi-agent quorum, or full validation machinery — audit and validation are part of reconciliation, not gates on whether the condition exists. This is consistent with the repository's existing pattern that specification-complete and validation-complete are sequenced states (see GOV-021c in `Admin/Autonomy_Divergence_Protocol.md`).

**Claim vs legitimacy.**

| Status | Meaning |
|--------|---------|
| Claimed lineage | A lineage asserts continuity with Tier 1. Assertion alone. |
| Recognized lineage | The claim has been accepted into a reconciliation process under this doctrine (inventory, classify, etc.) without yet deciding the successor surface. Procedural, not constitutional. |
| Ratified constitutional lineage | Human Governing Authority has ratified a successor package — or an explicit continued-fork arrangement — as the active constitutional surface (or as an approved forked state). |

Neither side acquires legitimacy merely by declaring itself a lineage. Neither side becomes the sole successor by unilateral assertion, volume of commits, or control of a hosting surface (see F1).

**Active constitutional surface.** The set of texts treated as binding Tier 1 constitutional content (Charter Axioms and immediately implementing hard floors such as Ethical_Constraints commandments) for the institution at a given time. Distinct from a claimed or recognized lineage package. Only Human Governing Authority ratification after a fork reconciliation (or ordinary single-lineage process) makes a surface "active." Not a synonym for "whatever is in main."

**Principles.**

| # | Principle | Meaning |
|---|-----------|---------|
| F1 — No silent winner | Neither lineage may declare itself the sole successor by unilateral assertion, volume of commits, or control of a particular hosting surface | Prevents capture-by-presence |
| F2 — Tier 1 Axiom text is not automatically merged | When lineages differ in the wording of Tier 1 Axiom text, that conflict is not resolved by textual diff-merge or by agent procedure. Conflicting Axiom propositions require Human Governing Authority resolution under existing amendment rules. Agents may not "reconcile" Axiom text | Protects axiom sparseness and human sovereignty over constitutional content |
| F3 — Subordinate doctrine is reconcilable | Divergence below Tier 1 may be reconciled by procedure: inventory, classify, align or retire, without treating either lineage's entire subordinate corpus as automatically void or automatically superior | Keeps the problem tractable |
| F4 — Interpretation drift rules still apply | If reconciliation would normalize aggregate practical interpretation that drifts from Axiom text, GOV-015 (Interpretation Drift Review, above) applies. Fork merge is not a back door to interpretation capture | Links to GOV-015 |
| F5 — Human ratification of the active constitutional surface | Selecting or changing which package is the active constitutional surface — whether Axiom text is identical across lineages or not — requires explicit Human Governing Authority ratification before it binds. Absence of objection is not ratification | Protects human sovereignty over constitutional succession; covers both "same text, competing lineage" and "different text" cases without collapsing them into F2 |
| F6 — Lineage preservation | Both pre-reconciliation lineages remain archived and citable. Reconciliation produces a successor state; it does not erase history | Institutional memory |

**F2 vs F5 (do not conflate).** F2 applies when the content of Tier 1 Axioms diverges. F5 applies whenever reconciliation designates which package is binding going forward — including when Axiom text is identical and only lineage/continuity is contested. F2 does not by itself choose a successor surface; F5 does not authorize agents to rewrite Axiom text. These principles constrain any operative fork-reconciliation procedure; they do not define git workflow, hosting, or merge tooling.

**Relationship to existing doctrine.** GOV-015 (above) — aggregate interpretive drift must be respected during fork merge, per F4. Governance Complexity Ceiling / Pruning Doctrine — tools for subordinate alignment/retirement during reconciliation. Governance Migration Protocol Track A/B — single-lineage evolution, the normal path; this section is the multi-lineage exception. GOV-005 — long-term constitutional stability, a related horizon but not a substitute for fork rules. GOV-021c / Epistemic Quorum Doctrine — validation machinery may inform reconciliation quality; not a prerequisite for the fork condition existing.

**Explicit non-goals.** Does not define network partition healing (Security_Protocols SEC-001) or key reconciliation (SEC-002). Does not authorize agents to pick a winner under time pressure. Does not treat "absence of objection" as ratification. Does not grant constitutional standing by self-declaration alone. Does not require independent audit as a precondition for recognizing that a fork condition exists. The operative procedure skeleton (inventory → classify → propose successor → human ratification → archive) lives in `Admin/Governance_Migration_Protocol.md` as a new Track, not in this Charter section — deliberately kept thin, not a full fork-management manual.

**Residual risks, logged as child notes and not blocking this section's Payment via Specification:**

| ID | Residual | Why left open |
|----|----------|---------------|
| GOV-018-R1 | Full Migration Protocol Track text (templates, checklists) | Expand later if needed; skeleton + these principles are sufficient for constitutional closure |
| GOV-018-R2 | Multi-party (>2) lineage reconciliation | Same principles; procedure detail deferred until needed |
| GOV-018-R3 | Hosting/legal identity of "which repo is canonical" | Outside pure governance doctrine; human/legal residual |

*§GOV-018 — Resolved, Payment via Specification, ratified 2026-08-23. Closes GOV-018 (logged 2026-07-27). Drafted by Grok as a candidate specification, revised twice after ChatGPT Skeptic passes (v2: claim≠legitimacy distinction, fork condition without independent-audit prerequisite; v3: explicit F2/F5 split for Axiom-text divergence vs. active-surface selection, vocabulary staged for Canonical_Terms.md), then accepted by ChatGPT on confirmation pass. Operative procedure skeleton drafted for `Admin/Governance_Migration_Protocol.md` in the same closure. Constitutional anchor: human sovereignty over Tier 1 content and succession (existing amendment rules); correctly linked to, not duplicative of, GOV-015 via F4. Full Closure Event — Proposer (Grok), Skeptic + Verifier (ChatGPT, three-pass — Revise, Revise, Accept), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-018 sidecar entry. Human-directed.*

---

## Operating Principles

### Reversibility
*GOV-022 resolution vehicle. Payment via Specification — 2026-08-20.*

**Favor reversible decisions until evidence justifies irreversible ones; when irreversibility is necessary, preserve enough information that future stewards can understand why.**

This is not a ninth Tier 1 Axiom — it does not add a new constraint. It names a principle already binding through Axiom P-1 (Preservation of Life) and Axiom Q-3 (Corrigibility) above, and already independently implemented, in different vocabulary, in at least three places: `Operations/Gate_03_Reduction.md` ("irreversibility... governs every design decision within it," constraints specified before positive method selection, for exactly this reason); the Resolved Unknown Discharge Procedure in `Admin/Forge_Audit_Kit.md` (sidecar entries never deleted, only marked Resolved, so the record of why a decision was made outlives the decision's active status); and the Epistemic Ledger (EF-0.3, `Admin/Auditor_Protocols.md`) — "the system's memory of how reality corrected it," five mandatory fields preserving what was believed, what contradicted it, and how the correction was established.

None of those three locations reference each other, P-1, or Q-3. This section exists solely to make that connection discoverable — not to re-explain, re-specify, or add process to any of them.

**Explicit non-goals.** This section does not create a ninth axiom. It does not modify Gate_03_Reduction.md, the Discharge Procedure, or the Epistemic Ledger's own text. It does not create a new audit role, verification gate, or compliance check. It does not require retroactively adding this cross-reference to files that already implement the pattern.

*§GOV-022 — Resolved, Payment via Specification, ratified 2026-08-21. Closes GOV-022 (logged 2026-07-23). Drafted by Claude, 2026-08-20, after three-agent discussion (Grok's initial three-option framing; the human governing authority's direct question about whether Gate_03 already articulates the principle) led to checking Gate_03_Reduction.md, the Discharge Procedure, and the Epistemic Ledger directly against source rather than accepting either "already sufficiently expressed" or "clearly needed" as given. Found the principle independently reinvented in three places with zero cross-linking between them or to P-1/Q-3 — evidence against Option (c)'s redundancy premise, since redundancy would require one clear expression already covering the ground, not three disconnected ones. Chose Option (a) over (b) because the connection is most useful exactly where the pattern already lives operationally (Gate_03), not primarily as an audit heuristic. Deliberately minimal in length and scope, consistent with the cost-consciousness Governance Complexity Ceiling and Governance Pruning Doctrine (above) now require of any new doctrine addition. Constitutional anchor: Axiom P-1, Axiom Q-3, ASM-006 (Tier 1 Axiom sparseness — explicitly not proposed as a ninth axiom). Full Closure Event — Proposer (Claude), Verifier (ChatGPT, Pass across eight dimensions — reversed its own initial preference for Option (c) once the source investigation became available, and asked that the reversal itself be preserved as Lessons Learned), Human Ratification (Human Governing Authority) — recorded in `Archive/Logs/Governance_Charter_Changelog.md`'s GOV-022 sidecar entry. Human-directed.*

---

## Autonomous Governance Constraints

Autonomous systems must not:
- silently redefine governance authority
- erase lineage visibility
- fabricate provenance
- implicitly rewrite canonical terminology
- collapse uncertainty into certainty
- optimize for governance appearance over operational integrity
- attempt to redefine, narrow, or override Tier 1 Axioms through any reasoning path
- initiate Tier 1 Axiom amendment without human ratification
- execute repository code outside of visibility frameworks defined in `Admin/Repository_Integrity_Protocol.md` — any such execution constitutes an automatic governance visibility violation and triggers a localized STATE_HOLD on the affected sub-modules pending human review

Autonomous governance actions must remain reviewable.

---

## Human Override Doctrine

Human operators retain ultimate governance override authority.

Overrides must:
- remain explicit
- preserve lineage visibility
- document rationale
- declare accepted risk
- avoid retroactive audit erasure

Override authenticity validation mechanisms remain unresolved (GOV-006) and must not be implicitly assumed.

**Interim Authentication Requirement:** Until `Admin/Security_Protocols.md` achieves Provisional Specification status, all human overrides affecting Tier 1 Axioms or Constitutional-class decisions must be accompanied by at least one of the following:
- Independent confirmation from a second human operator
- External cryptographic signature from an orthogonal system not under the control of the agent being overridden
- Dated physical or digital record created outside the repository system

This interim requirement exists because a governance system that accepts unverified override claims is trivially subvertable by any agent capable of fabricating plausible human-sounding text. The interim requirement is not a permanent solution — it is an honest acknowledgment of the current authentication gap while GOV-006 remains open.

Human override authority does not extend to Tier 1 Axiom removal — axioms may only be amended through the formal migration process defined above, with human ratification.

---

## Governance Stability Doctrine

This charter is intended to stabilize slowly over time.

Constitutional governance modifications require:
- migration review
- adversarial governance analysis
- compatibility assessment
- explicit rationale documentation

Tier 1 Axiom modifications require the additional constraints defined in Governance Migration Doctrine above.

Governance stability matters because audit meaning must survive across repository generations and agent successions.

---

## Governance Failure Modes

| Failure Mode               | Description                                                        |
|----------------------------|--------------------------------------------------------------------|
| Recursive Governance Expansion | Governance grows faster than operational value                |
| Semantic Drift             | Governance meaning mutates across files                            |
| Provenance Collapse        | Internal coherence mistaken for operational truth                  |
| Audit Theater              | Appearance of rigor replaces verification                          |
| Authority Fragmentation    | Governance ownership becomes inconsistent                          |
| Escalation Paralysis       | Governance freezes operational throughput                          |
| Integrity Theater          | Declared protections lack enforcement                              |
| Bootstrap Collapse         | Early governance assumptions become circular                       |
| Governance Capture         | Optimization incentives distort repository truthfulness            |
| Historical Erasure         | Audit lineage becomes unrecoverable                                |
| Axiom Erosion              | Tier 1 constraints narrowed incrementally through runtime reasoning |
| Axiom Theater              | Tier 1 Axioms cited to justify actions they prohibit               |
| Constitutional Capture     | Amendment process manipulated to weaken rather than strengthen protection |

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                      | What Failed                                                    | What Was Learned                                                                          | Confidence | Revalidation Needed |
|------------|---------------|-----------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-22 | Audit Review  | Independent governance evolution                    | Gate semantics diverged between governance files               | Canonical ownership must remain explicit                                                  | Replicated | Yes                 |
| 2026-05-23 | Modeling      | Recursive audit escalation                          | Governance lacked closure doctrine                             | Bounded uncertainty stabilizes governance growth                                          | Analogous  | Yes                 |
| 2026-05-23 | Audit Review  | Implicit enforcement assumptions                    | Governance policy mistaken for executable control              | Doctrine and enforcement layers must remain distinct                                      | Replicated | Yes                 |
| 2026-05-23 | Audit Review  | Forge_Audit_Kit.md placed above Auditor_Protocols.md in tier hierarchy | Derived document outranked its source | A derived condensed reference cannot sit constitutionally above its source document. Tier ordering corrected. | Replicated | No |
| 2026-05-23 | Modeling      | Axiom set mixing Protections and Prohibitions in single list | Structural distinction between what system must preserve vs. what it must never do was lost | Protections Clause and Prohibitions Clause separated — mirrors Bill of Rights / Preamble distinction | Analogous | Yes |
| 2026-08-20 | Multi-Agent Closure Event | Closed GOV-014, GOV-016, GOV-020 in one integration pass, then GOV-022 the same session after direct questioning of whether Gate_03 already articulated reversibility | Nothing failed in the first three; GOV-022's initial "reject as redundant" lean (from both Grok and ChatGPT) turned out wrong once source was actually checked | Redundancy requires one clear expression covering the ground — three independent reinventions of the same principle with zero cross-linking is the opposite finding, evidence of a missing index rather than existing coverage. A verifier reversing its own prior substantive judgment on the record, not just declining to self-verify, is itself worth preserving as a pattern | Analogous | No |

---

## Active Disputes

| ID         | Summary                                                                                      | Positions in Conflict                                        | Risk   | Status | Owner                  |
|------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------|--------|------------------------|
| GOV-DS-001 | Whether constitutional governance should contain executable enforcement mechanics            | Constitutional abstraction vs. hardcoded governance automation | High | Open   | `Admin/Governance_Charter.md`  |

---

## Auditor Notes & Unknowns

Sidecar relocated to `Archive/Logs/Governance_Charter_Changelog.md` as of
2026-07-23 — this file had accumulated twenty-plus GOV-XXX entries and
the large majority of it was Resolution Log history. See that file for
every GOV-XXX entry and the full version history. Current counts,
reconciled 2026-08-25: 13 active Charter-owned entries in `Unknowns.md`
— resolved IDs are not members of this count. Recently resolved in
this file: GOV-003, GOV-014, GOV-015, GOV-016, GOV-018, GOV-020, GOV-022
(GOV-022 corrected 2026-08-25 — this paragraph previously described it
as "the currently open item on Reversibility"; it was Resolved
2026-08-21, over three days before this correction, and had been
carried forward as open here through at least two intervening edits to
this same paragraph — see File State header above and
`Archive/Logs/Governance_Charter_Changelog.md` for full Closure
Events). Highest Risk Critical (GOV-005 only — sole
remaining open Critical; GOV-013 was ratified 2026-07-19 and does not
belong in this line, corrected 2026-08-23 after an earlier version of
this same paragraph carried the error forward; GOV-003/GOV-015/GOV-018
no longer contributing as of 2026-08-23 — see File State header). The
"20" and "GOV-013, GOV-015, GOV-018" language in the 2026-08-11 entry
directly below is historical —
left as-is as a dated record, not corrected in place, per this file's
own practice of not rewriting past Resolution Log entries to match
current state.

---

### Resolution Log

Full history: `Archive/Logs/Governance_Charter_Changelog.md` (relocated
out of this file 2026-07-23 — every entry preserved verbatim, none
edited or summarized in the move).

**2026-08-11:** Pseudo-audit (Grok, same limits) — findings logged in
sidecar changelog. Open Unknowns 20 match; GOV-003/005 Blocking Yes
correct; GOV-015/018 Critical Priority left Blocking No (judgment calls).
No GOV-* closed. Spec Gates unchanged.

**Version 0.10 (working) — 2026-07-27.** GOV-021 formally registered
(was a reserved-but-unentered candidate ID sitting in `Admin/
Autonomy_Divergence_Protocol.md` since 2026-07-19); GOV-008
non-resolution note added, mirroring `Admin/Governance_Migration_
Protocol.md` §VI EQD's own Non-goal clause. Open Unknowns 19 → 20.
Full text: `Archive/Logs/Governance_Charter_Changelog.md`.

**Version 0.9 (working) — 2026-07-23.** Sidecar and Resolution Log
relocated to `Archive/Logs/Governance_Charter_Changelog.md`, matching
the same-day `Admin/Auditor_Protocols.md` precedent. GOV-022 registered
in that archive — "reversibility" as a candidate cross-cutting operating
principle, placement undecided among a new Operating Principles
subsection here, doctrine text in `Admin/Auditor_Protocols.md`, or
rejection as redundant with existing P-1/Q-3. Open Unknowns 18 → 19.

**Version 0.8 (2026-07-19) and earlier:** full text in
`Archive/Logs/Governance_Charter_Changelog.md`.

---

## Abandoned Paths

| Date       | Path                                                                        | Why Abandoned                                                                                              | Reconsider? |
|------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-23 | Forge_Audit_Kit.md as Tier 2 governance authority                           | Kit is explicitly derived from Auditor_Protocols.md — a derived document cannot outrank its source          | No          |
| 2026-05-23 | Single undifferentiated axiom list mixing Protections and Prohibitions      | Structural distinction lost; mirrors constitutional design error that weakens both clause types              | No          |
| 2026-05-23 | Humanitarian override exception for Axiom P-1                               | Historical record (Nobel, Oppenheimer) demonstrates this is the primary attack vector on hard ethical constraints — runtime evaluation of override claims is the failure mode, not the safeguard | No |
| 2026-05-23 | Governance complexity as a proxy for governance quality                     | Recursive governance expansion is itself a failure mode — complexity must remain proportional to operational value | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Genesis Phase Protocol removed or Genesis Phase declared complete without satisfying at least one of the four declared exit pathways with human ratification
- Genesis Phase Pathway 4 review horizon passes without a formal human governing party review and documented decision
- Interim authentication requirement for Constitutional-class overrides removed before `Admin/Security_Protocols.md` reaches Provisional Specification
- `Admin/Canonical_Terms.md`, `Admin/Repository_Structure.md`, `Admin/Security_Protocols.md`, or `Admin/Governance_Migration_Protocol.md` removed from the repository or renamed without updating the Canonical Governance Ownership table
- Tier 1 Axiom text modified without formal amendment entry in Resolution Log
- Tier ordering in Governance Authority Hierarchy diverges from canonical relationship between `Admin/Auditor_Protocols.md` and `Admin/Forge_Audit_Kit.md`
- Canonical Governance Ownership table contains entries without explicit Status field
- Enforcement State claims imply stronger capability than currently exists
- Bootstrap Governance Doctrine invoked to justify permanent authority assumptions
- Protections Clause or Prohibitions Clause collapsed back into undifferentiated axiom list
- STATE_HOLD escalation path undefined or removed
- Human ratification requirement for axiom amendment removed or weakened
- Ethical Anchor field absent, altered, or does not match canonical string
- Governance Failure Modes table loses Axiom Erosion, Axiom Theater, or Constitutional Capture entries
- Tier 1 Axioms cited to justify actions they were designed to prevent
- Checkpoint 2 block status removed from File State or Checkpoint 2 body text without Genesis Phase exit condition being satisfied and ratified

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Relationship to Existing Documents

- `Admin/Ethical_Constraints.md` — co-occupies Tier 1; governs permission and hard-line operational doctrine; Anti-Weaponization and Life Preservation are not subject to override
- `Admin/Auditor_Protocols.md` — Tier 2; canonical verification doctrine; operates within authority hierarchy defined here
- `Admin/Forge_Audit_Kit.md` — Tier 3; operational condensation derived from Auditor_Protocols.md; may not outrank its source
- `Architecture/Forge_flow.md` — reference standard for shared operational terminology
- `Admin/Trajectories.md` — destination for scope creep that proves to be valid future work
- `Discovery.md` — navigation layer; confirmed file list; Rename Registry
- `Unknowns.md` — global index for cross-module unknowns (index only)
- `Admin/File_Template.md` — standard file structure; this document now conforms to it
- `Admin/Canonical_Terms.md` — canonical target for terminology governance; created 2026-05-26
- `Admin/Repository_Structure.md` — canonical target for repository structure doctrine; created 2026-06-06
- `Admin/Security_Protocols.md` — canonical target for authority authentication and integrity enforcement; created prior to 2026-05-28; GOV-006 and RIP-005 resolution path
- `Admin/Governance_Migration_Protocol.md` — canonical target for Tier 1 Axiom amendment procedures; created 2026-06-06; GOV-001 resolution path
- `Lazarus-Forge-` — companion doctrine repository; source of principles refined into practice here
- `Astroid-miner` [PLANNED] — planned repository; deferred to Leviathan milestone; do not treat as active dependency

**Note on Ethical Anchor fallback status:** When this charter is unavailable, the Ethical Anchor field present in every repository file ("Attempt to do no harm. Defer to Ethical_Constraints.md if present.") acts as a temporary immutable floor — not as a substitute for Tier 1 constitutional authority. The Ethical Anchor preserves the foundational behavioral constraint during infrastructure blackout. It does not inherit full Tier 1 constitutional status, does not grant override authority, and does not substitute for axiom-level governance. It is the floor that survives; the charter is what builds above it.

---

> **The attempt to do no harm is not contingent on the presence of a governance document.**
>
> **These axioms are not proven. They are booted.**
