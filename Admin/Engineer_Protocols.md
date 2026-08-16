# Engineer_Protocols.md — Engineering Problem-Solving Protocol

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Poor engineering judgment or unvalidated creative solutions can lead to
> structural failure, energetic release, wasted resources, or dangerous systems.
> AI-generated designs carry additional risk of subtle errors, overconfidence,
> or context loss between sessions. Prerequisite: always anchor creativity in
> first principles, existing repository knowledge, explicit safety margins, and
> physical validation. Never treat novel ideas as true until tested against
> reality. When in doubt, simplify, increase margin, or hold the solution.
> The cost of elegant but wrong is always higher than the cost of simple and
> proven.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-30 (ChatGPT — Skeptic/Auditor); revised 2026-06-08          |
| Auditor          | Claude — Retrofit/Auditor (integrating 2026-05-30 addendum)         |
| Open Unknowns    | 6                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cognitive and procedural protocols for engineering problem-solving
  within LazarusForge
- Pragmatic question framework for AI and human contributors
- Assumption challenge triggers — when skepticism is mandatory
- Discipline for balancing innovation with evidence, reuse, and safety
- Anti-reinvention and failure-harvesting rules
- Engineer ↔ Auditor relationship and dispute resolution doctrine
- AI-specific engineering contribution guidance

**This file DOES NOT define:**
- Specific engineering calculations or domain techniques — governed by
  domain files (Operations/, Architecture/)
- General audit or governance procedures — governed by
  `Admin/Auditor_Protocols.md` and `Admin/Forge_Audit_Kit.md`
- Detailed validation test protocols — deferred to domain files
- Engineering authority boundary — see EP-004 in sidecar; undefined
  until resolved
- Auditor role class definitions — governed by
  `Admin/Auditor_Protocols.md` §Auditor Role Classes; this file
  extends the Engineer role defined there, it does not replace it
- Physical safety hazard thresholds, PPE requirements, and
  acceptable risk consequence categories
  (→ `Admin/Safety_Protocols.md`)

---

## File Purpose

This file guides AI and human engineers toward effective, reality-grounded
creative problem-solving within the Forge. It replaces vague directives
like "be creative" or "question everything" with a disciplined framework
that maximizes value while minimizing waste, reinvention, and safety
violations.

Without this file, the repository lacks explicit doctrine for how
engineering contributors — human or AI — should approach novel problems.
The gap between governance documents (what is permitted) and domain
specifications (what is built) is where undisciplined engineering
accumulates: hallucinated solutions, duplicated effort, ungoverned
assumptions, and preventable failures.

**Relationship to existing files:** This file extends the Engineer role
defined in `Admin/Auditor_Protocols.md` §Auditor Role Classes. Engineers
operating under this protocol remain subject to all AI Contribution Rules
in Auditor_Protocols.md. This file does not supersede Cognitive_Frameworks.md
— that file governs how Forge systems think under uncertainty; this file
governs how contributors engineer solutions within the repository.

---

## Assumptions

| ID      | Assumption                                                                     | Basis                              | Confidence | Expiry Trigger                                        |
|---------|--------------------------------------------------------------------------------|------------------------------------|------------|-------------------------------------------------------|
| ASM-001 | Contributors have access to the full repository and Discovery.md               | Standard Forge operating context   | High       | Repository access restricted                          |
| ASM-002 | Physical prototyping and testing capability exists at some level               | Core Forge capability — Analogous  | Medium     | Confirmed no-test environment                         |
| ASM-003 | Lessons Learned and Unknowns sections are actively maintained                  | Repository integrity doctrine      | Medium     | Observed systemic neglect                             |
| ASM-004 | "Engineering authority" in this file refers to governance intent, not cryptographically enforced implementation | Honest v0 acknowledgment | High | Phase 3 cryptographic enforcement per `Admin/Security_Protocols.md` |

---

## Body

### 1. Engineering Mindset

Effective Forge engineering is constrained creativity — not unconstrained
ideation. The goal is to deliver functional value with minimal resources
while preserving safety and institutional memory.

**Core posture:**
> "The only reasonable response to 'Question everything?' is 'Why should I?'"

Skepticism must be targeted and justified by potential impact, uncertainty,
or evidence of prior failure. Indiscriminate skepticism wastes cycles
re-litigating settled knowledge. Targeted skepticism catches the failures
that matter.

Engineering is disciplined adaptation under constraints. It is neither
pure creativity nor pure bureaucracy.

---

### 2. Pragmatic Question Framework

Apply this framework on every non-trivial engineering problem before
proposing a solution.

**1. Is it actually needed?**
What is the measurable value? What failure occurs if we do nothing or use
a simpler alternative? Feature and capability creep are common failure
modes in complex systems.

**2. Has a solution already been found?**
Search in this order: (1) `Discovery.md` — primary navigation layer, preferred
first stop; (2) canonical folder structure (Admin/, Architecture/, Operations/,
Tests/) if Discovery.md is stale or unavailable; (3) `Archive/Rename_Registry.md`
for potentially renamed files; (4) direct file search as fallback.
`Discovery.md` is the preferred dependency, not the only path — if it becomes
stale, repository search quality degrades but does not fail entirely. Also consult
`Architecture/Forge_Net.md` (when available) for cross-forge knowledge.
This is repository doctrine, not a suggestion.

**3. What worked, what failed, and why?**
Consult Lessons Learned before proposing new approaches. A solution that
ignores documented prior failure is not a solution — it is a repetition.

**4. What are the real constraints?**
Safety, materials (especially salvaged and imperfect), energy, tools,
time, environment, skill level. Constraints are not obstacles — they are
the problem definition.

For energy-bearing systems, thermal processes, chemical processing,
electronics salvage, pressure vessels, rotating machinery, or fabrication
operations: review `Operations/Energy.md` and relevant hazard doctrine
before capability claims or design proposals. Energy-bearing proposals
must not assume available capacity without consulting current energy
characterization state.

**5. What is the simplest thing that could work?**
Apply the "good enough for now" standard. Complexity is debt. Every
additional component is a failure mode waiting to manifest.

Recovery economics check: does implementation cost — in energy, materials,
time, or operator burden — exceed the recovered value or utility? A solution
that costs more than it recovers is reduction dressed as progress. Apply
the Energy Density Paradox test from the Fallacy Checklist before committing
to any recovery or reprocessing proposal.

**6. What are the three most likely failure modes?**
Perform lightweight failure mode analysis. Identify load paths, single
points of failure, and environmental derating. A design that has not been
stress-tested against its three most likely failures is not a design —
it is a hope.

**7. Why should I question this assumption?**
Only challenge assumptions with evidence of weakness or high downstream
risk. See Assumption Challenge Triggers below for mandatory conditions.

**8. How will we test and validate this?**
Define success criteria and test plan before building. Untestable
specifications are not specifications.

**9. What knowledge will this create or preserve?**
Every engineering effort should feed Lessons Learned or resolve an
Unknown. Knowledge that is not captured is lost at the next session
boundary.

**10. What is the rollback or fail-safe plan?**
Reversibility is a design requirement. Irreversible actions require
explicit justification and elevated authorization per
`Admin/Ethical_Constraints.md` and `Admin/Auditor_Protocols.md`
§Human Override Doctrine.

#### Assumption Challenge Triggers

Questioning an assumption becomes mandatory when one or more of the
following apply:

- Safety consequences exceed acceptable risk threshold
- Failure cost exceeds replacement cost
- Assumption has never been validated against physical evidence
- Environmental conditions differ from the original context of the
  assumption
- Lessons Learned contain contradictory evidence
- `Unknowns.md` contains related unresolved items in the same cluster

Without explicit triggers, skepticism thresholds vary by contributor
and audit cycles become unpredictable.

---

### 3. Creative Problem-Solving Doctrine

**First Principles and Constraint Harvesting**
Break the problem to physics, then creatively recombine under real
constraints. Do not begin with solutions — begin with constraints.

**Analogy Control**
Analogies are useful but dangerous. Always validate the mapping: does the
analog system share the same constraints, failure modes, and operating
environment? If not, the analogy is a starting point, not an answer.

**Reuse First, Innovate Last**
Prefer adaptation of existing solutions documented in
`Architecture/Components.md` and `Operations/Gate_06_Fabrication.md`.
Novel solutions carry unknown failure modes. Adapted solutions carry
documented ones.

**Salvage-Aware Design**
Assume imperfect materials. Design for repairability, graceful
degradation, and component substitution. A design that only works with
perfect inputs is fragile. A design that degrades predictably under
imperfect inputs is robust.

**Iteration Speed**
Fast, cheap, small-scale prototypes beat perfect simulation. Simulation
is a planning tool. Physical testing is the verification gate.

**Documentation Discipline**
Record assumptions, decisions, and test results immediately. Context
loss between sessions is a primary failure mode for multi-agent
workflows. What is not recorded is lost.

**Unknown Discovery Doctrine**
When an engineering contribution surfaces a gap, uncertainty, or unresolved
question that does not yet exist as a sidecar unknown, log it before solution
development proceeds beyond exploratory discussion. Do not build on an
unlogged unknown — it will not be tracked, will not receive an expiry review,
and will not be visible to future contributors or audit cycles. The cost of
logging is seconds. The cost of an untracked unknown compounding across
sessions is institutional memory loss.

Newly discovered unknowns must include at minimum: a one-sentence description
of the reality gap, a one-sentence consequence if left unresolved, and a
proposed resolution path or discharge route. Route to the owning file's
sidecar; cross-module unknowns route to `Unknowns.md`.

---

### 4. Anti-Reinvention Rules

- Never invent what can be referenced.
- `Discovery.md` is the primary navigation layer — search there first.
- Consult `Admin/Canonical_Terms.md` for terminology before introducing
  new terms.
- Log solved problems into Lessons Learned immediately.
- New solutions must explicitly address why prior approaches were
  insufficient. "I didn't know it existed" is not a sufficient reason.
- Cross-reference `Archive/Rename_Registry.md` before assuming a
  file does not exist — it may have been renamed.

---

### 5. AI-Specific Engineering Guidance

AI contributors carry specific failure modes that human contributors do
not share at the same rate. This section addresses them directly.

- **Use tools before generating.** Search the repository, read the
  relevant files, check Discovery.md before producing new content.
  Generation without context produces hallucinated solutions.
- **Declare context limitations explicitly.** If operating under token
  constraints or without access to a relevant file, say so. Confident
  output under incomplete context is a governance failure mode.
- **Cross-reference canonical files rather than paraphrasing from
  memory.** Memory across sessions is unreliable. Canonical files are
  the source of truth.
- **Flag uncertainty and required validation steps when proposing novel
  approaches.** Novel is not better. Novel means unvalidated.
- **Treat confidence as provisional until physically tested.** High
  internal confidence in an untested design is not evidence of
  correctness — it is evidence of coherent reasoning under assumptions
  that may be wrong.
- **Apply AI Contribution Rules 1–7 from `Admin/Auditor_Protocols.md`.**
  Role declaration, lineage tracking, and assumption extraction apply to
  engineering contributions as much as to audit contributions.

---

### 6. Failure Harvesting

Every failure is data. Capture immediately and completely:

| Field | Content |
|-------|---------|
| What was tried | Specific approach or solution |
| What failed | Specific failure mode or outcome |
| Root cause | If known; "unknown" is acceptable and honest |
| What was learned | Concrete operational insight |
| Revalidation needed | Yes / No — with trigger condition |

Captured failures must be reviewed for institutional closure across four
pathways. A failure that is archived but never closes a loop is lost
institutional memory:

1. **Lessons Learned entry** — is this a permanent record worth
   preserving for future contributors?
2. **Unknown closure opportunity** — does this resolve or inform an
   open sidecar entry?
3. **Design standard update** — does this change how we build or
   specify?
4. **Audit protocol update** — does this change how we verify or test?

---

### 7. Engineer ↔ Auditor Relationship

Engineers optimize for solution generation.
Auditors optimize for failure detection.
Neither role supersedes the other.

Both are necessary. A repository with only engineers accumulates
unverified claims. A repository with only auditors accumulates governance
without progress. The tension is productive when it is explicit.

**Dispute resolution sequence:**

1. **Evidence** — physical test data or documented analog from a similar
   system. Evidence ends most disputes.
2. **Testing** — define a falsifiable test, run it, accept the result.
3. **Specification** — if the dispute reveals a gap in existing doctrine,
   promote the resolution into body specification.
4. **Governance escalation** — if unresolved after three cycles, route
   to `Admin/Auditor_Protocols.md` §Dispute Handling Protocol and log in
   the file's Active Disputes table.

**Role boundary:**
This file extends the Engineer role defined in `Admin/Auditor_Protocols.md`
§Auditor Role Classes. Engineers operating under this protocol remain
subject to all AI Contribution Rules and Human Contributor Protocols in
Auditor_Protocols.md. Engineering decisions that cross into safety-adjacent,
scope-expanding, or Tier 1 Axiom-adjacent territory require elevation to
the appropriate governance layer — see EP-004 for the unresolved boundary
definition.

---

### 8. Hazard Escalation Doctrine

Engineering proposals that introduce or interact with the following hazard
classes must review relevant hazard doctrine and active unknowns before
proceeding beyond exploratory discussion:

| Hazard Class | Repository Reference | Active Critical Unknowns |
|---|---|---|
| Energetic materials | `Operations/Gate_01_Intake.md` | GI-002, GI-003 |
| Toxic emissions / dust | `Operations/Electronics.md`, `Operations/Air_Scrubber.md` | EL-005 |
| Biological / chemical waste | `Operations/Gate_03_Reduction.md` | GR-003 |
| Fire / hot-work | `Operations/Gate_06_Fabrication.md` | GF-007 |
| Halogenated polymers | `Operations/Plastics.md` | PL-001 |
| Autonomous behavior | `Admin/Ethical_Constraints.md`, `Architecture/Cognitive_Frameworks.md` | LT-003, LT-004 |
| Pressure vessels / reactor | `Operations/Plastics.md` | PL-002 |
| Rotating machinery | `Operations/Gate_05_Separation_Thermal.md` | SC-001, SC-005 |
| Physical safety / PPE | `Admin/Safety_Protocols.md` | SP-002, SP-003, SP-006 |

Findings from hazard review that are not already logged must be logged as
unknowns before the proposal advances. Hazard findings that involve
energetic release, toxic exposure, fire/explosion risk, autonomous action,
or irreversible environmental impact must be escalated to human operator
review before any implementation proceeds.

Route escalations to `Admin/Ethical_Constraints.md` for hard-floor checks
and `Admin/Auditor_Protocols.md` §Human Override Doctrine for authorization
requirements.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                              | What Failed                                              | What Was Learned                                                                                  | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-29 | Anecdotal     | Broad "question everything" approach        | Wasted effort on settled problems                        | Targeted skepticism anchored in explicit triggers is superior to indiscriminate skepticism        | Anecdotal  | Yes                 |
| 2026-05-30 | Audit Review  | Discovery.md as sole navigation anchor      | Single-point dependency — stale Discovery degrades search quality | Discovery.md is preferred dependency not only path; canonical folder structure is the fallback   | Analogous  | No                  |
| 2026-05-30 | Audit Review  | Recovery proposals without economics check  | Solutions proposed whose cost exceeded recovered value   | Energy Density Paradox check must apply to recovery and reprocessing proposals, not just fabrication | Analogous | Yes                 |
| 2026-05-30 | Audit Review  | Unknown discovery without explicit logging doctrine | Unknowns surfaced during engineering work went untracked | Unknown discovery doctrine required — log before proceeding; untracked unknowns are invisible to future audit cycles | Analogous | Yes |
| 2026-05-29 | Audit Review  | Engineer role defined without explicit Auditor relationship | Role boundary became ambiguous under governance pressure | Engineer and Auditor roles must be explicitly complementary with a defined dispute resolution sequence | Analogous | Yes              |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                    | Reconsider? |
|------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| 2026-05-29 | "Question everything" as core engineering posture                 | Rewards indiscriminate skepticism; wastes cycles on settled knowledge; replaced with targeted triggers | No      |
| 2026-05-29 | Engineering protocol as standalone authority independent of Auditor_Protocols.md | Creates parallel governance; this file extends, not replaces, existing role doctrine | No   |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Pragmatic Question Framework reduced below 8 questions without
  documented rationale
- Assumption Challenge Triggers section removed or made optional
- Engineer ↔ Auditor relationship section removed or scope reversed
  to imply one role supersedes the other
- Anti-Reinvention Rules no longer reference Discovery.md as primary
  navigation layer
- AI-Specific Engineering Guidance section removed or merged into
  generic guidance that does not address AI-specific failure modes
- Failure Harvesting four-pathway closure loop removed
- EP-003 or EP-004 closed without resolution evidence
- Derivation relationship to Auditor_Protocols.md §Auditor Role Classes
  removed from Scope Boundary or File Purpose
- File moved out of Admin/ without updating all cross-references
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### EP-001 — Validation of Pragmatic Question Framework

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Technical                    |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** Effectiveness of the 10-question framework has not been
operationally tested across multiple engineering domains within the
repository. The framework was derived from general engineering practice,
not from Forge-specific operational experience.

**Why It Matters:** Different engineering domains (thermal, mechanical,
electronics, governance) may require different question weighting or
additional domain-specific triggers. A framework that works well for
hardware design may be poorly calibrated for governance document
engineering.

**Resolution Path:** Payment via Specification — collect operational
feedback from at least three engineering contributions that explicitly
used the framework. Log outcomes in Lessons Learned. Adjust question
weighting or add domain-specific variants if patterns emerge.

---

### EP-002 — AI vs Human Protocol Optimization

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Architectural                |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The AI-Specific Engineering Guidance section identifies
AI failure modes but does not define optimal adjustments for AI
context-window limitations, tool-use sequencing, or the difference
between AI intuition (pattern matching) and human intuition (embodied
experience).

**Why It Matters:** Multi-agent workflows require contributors to
understand not just what to do but how AI and human contributors
complement each other's blind spots. The current section addresses
AI failure modes but not AI strengths that should be deliberately
leveraged.

**Resolution Path:** Payment via Specification — expand Section 5 with
explicit AI strength leverage doctrine (systematic search, cross-reference
consistency, pattern detection across large corpora) balanced against
known failure modes. Cross-reference `Architecture/Cognitive_Frameworks.md`
for alignment with distributed cognition doctrine.

---

### EP-003 — Integration Mapping with Auditor_Protocols.md and Cognitive_Frameworks.md

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The relationship between this file and
Auditor_Protocols.md is partially defined (Engineer role extension,
dispute resolution routing) but the relationship with
Cognitive_Frameworks.md is not yet mapped. Cognitive_Frameworks.md
defines how Forge systems think under uncertainty; this file defines
how contributors engineer solutions. The boundary and handoff between
them is implicit.

**Why It Matters:** Without explicit integration mapping, contributors
may apply cognitive frameworks where engineering protocols are called
for, or vice versa. Procedural overlap between the two files could
accumulate silently.

**Resolution Path:** Payment via Specification — add a dedicated
cross-reference paragraph in the Relationship section mapping: (1)
what Cognitive_Frameworks.md owns that this file defers to; (2) what
this file owns that Cognitive_Frameworks.md defers to; (3) the handoff
condition between them.

---

### EP-004 — Engineering Authority Boundary Undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The file assumes engineering autonomy without defining
what decisions engineers may make independently versus what requires
auditor concurrence or human operator approval. The boundary between
engineering decisions and policy decisions is not documented.

**Why It Matters:** As the repository grows, contributors need a clear
boundary. Without it, engineers either over-escalate (slowing progress)
or under-escalate (accumulating ungoverned decisions that may later
conflict with governance doctrine). Safety-adjacent, scope-expanding,
and Tier 1 Axiom-adjacent decisions are the highest-risk undifferentiated
zone.

**Resolution Path:** Payment via Specification — define at minimum:
(1) decisions within engineer authority (material substitution within
spec, prototype iteration, test design, Lessons Learned entries);
(2) decisions requiring auditor concurrence (scope changes, new
capability claims, safety-adjacent choices, cross-module dependency
additions); (3) decisions requiring human operator approval (irreversible
actions, first operational runs, Tier 1 Axiom-adjacent choices).
Cross-reference `Admin/Auditor_Protocols.md` §Human Override Doctrine
and `Admin/Ethical_Constraints.md` for the hard floors that cannot be
overridden regardless of engineering authority level.

---

---

### EP-005 — Acceptable Risk Threshold Undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance / Technical       |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-30                   |
| Last Reviewed | 2026-05-30                   |

**Description:** The Assumption Challenge Triggers section requires escalation
when "safety consequences exceed acceptable risk threshold" but no threshold
is defined. The term "acceptable risk" appears without a reference standard,
quantitative bound, or decision rule.

**Why It Matters:** Without a defined threshold, two engineers may reach
opposite conclusions about whether a safety consequence triggers mandatory
challenge. The trigger becomes subjective and audit-inconsistent. This also
affects EP-004 — authority to accept risk cannot be defined before the risk
threshold is defined.

**Resolution Path:** Payment via Specification — define acceptable risk
threshold with reference to at least one of: (1) consequence severity
categories (minor/major/catastrophic/irreversible) with corresponding
escalation routes; (2) cross-reference to `Admin/Ethical_Constraints.md`
Life Preservation heuristics as the hard floor; (3) explicit deferral to
human operator for any consequence involving irreversible physical harm.
Cross-reference `Admin/Safety_Protocols.md` consequence category table —
that file now owns physical safety escalation thresholds (EP-005 partial
resolution path). Also cross-reference EC-001 (sufficient confidence
threshold) and EP-004 (engineering authority boundary).

---

### EP-006 — Unknown Lifecycle Integration Undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-30                   |
| Last Reviewed | 2026-05-30                   |

**Description:** The file instructs engineers to feed Lessons Learned and
resolve Unknowns, but does not define the full lifecycle for unknowns
discovered during engineering work: how to discover and log them, how to
assign ownership and severity, how to set expiry criteria, and how to
distinguish engineering unknowns from governance unknowns. The Unknown
Discovery Doctrine added to Section 6 covers the discovery trigger but
not the full lifecycle.

**Why It Matters:** Engineers surfacing unknowns without lifecycle guidance
will log them inconsistently — wrong file, wrong severity, no expiry trigger,
no owner. Inconsistent unknowns are invisible to the Expiry Watch and the
global index.

**Resolution Path:** Payment via Specification — define: (1) format
requirements for engineering-sourced unknowns (cross-reference
`Admin/File_Template.md` §8 sidecar format); (2) ownership assignment
rules (unknown lives in the file closest to the gap); (3) severity
classification guidance for engineering discoveries; (4) escalation
path for unknowns that surface hazards rather than just gaps.
Cross-reference `Admin/Auditor_Protocols.md` §Unknowns Registry Governance.

---

### Resolution Log

- 2026-05-29: v0.1 created by Grok (Fabricator/Systems). Initial
  10-question framework, creative problem-solving doctrine, anti-
  reinvention rules, AI-specific guidance, and failure harvesting
  defined. EP-001 through EP-003 logged.
- 2026-05-29: v0.2 revision — ChatGPT Skeptic/Auditor and Claude
  Skeptic/Auditor findings actioned. Assumption Challenge Triggers
  added as mandatory subsection under Question 7. Failure Harvesting
  four-pathway closure loop added. Discovery.md priority explicitly
  anchored in Anti-Reinvention Rules and Question 2. Engineer/Auditor
  relationship section added (Section 7) with explicit derivation
  statement from Auditor_Protocols.md. EP-004 logged (engineering
  authority boundary). Drift Indicators section replaced with full
  mandatory re-audit conditions. Body Stability updated to Transitional.
  Spec Gates updated to 2/6. Open Unknowns updated to 4. All EP-
  owner fields corrected to Admin/Engineer_Protocols.md. Abandoned
  Paths section populated. ASM-004 added to Assumptions.
- 2026-05-30: ChatGPT Skeptic/Auditor addendum actioned. Question 2
  search order updated to include fallback paths. Question 4 expanded
  with energy-bearing systems consultation requirement. Question 5
  expanded with recovery economics check. Section 6 expanded with
  Unknown Discovery Doctrine. Section 8 (Hazard Escalation Doctrine)
  added — hazard class table with repository references and active
  critical unknowns. Lessons Learned entries added. EP-005 logged
  (acceptable risk threshold undefined). EP-006 logged (unknown lifecycle
  integration undefined). Open Unknowns updated to 6.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected
  from `Verification_Gates.md` to `Admin/Verification_Gates.md`
  (PC-001). Scope Boundary updated — `Admin/Safety_Protocols.md` added
  for physical safety hazard thresholds and PPE requirements (PC-003).
  Safety_Protocols.md row added to Section 8 Hazard Escalation table.
  All addendum content integrated into body — addendum block removed.
  File State updated: Open Unknowns 4→6, Last Audit and Auditor fields
  updated to reflect 2026-05-30 ChatGPT pass. EP-005 resolution path
  updated — `Admin/Safety_Protocols.md` now provides consequence
  category table as partial resolution path.

- `Admin/Auditor_Protocols.md` — Tier 2; this file extends the Engineer
  role defined in §Auditor Role Classes; AI Contribution Rules and Human
  Contributor Protocols defined there apply to engineering contributions;
  dispute escalation routes to §Dispute Handling Protocol
- `Admin/Forge_Audit_Kit.md` — Tier 3; condensed audit reference;
  engineering contributions are subject to the Fallacy Checklist and
  Verification Gates defined there
- `Admin/Governance_Charter.md` — Tier 1; EP-004 engineering authority
  boundary must not conflict with Tier 1 Axioms; safety-adjacent and
  irreversible engineering decisions defer to constitutional doctrine
- `Admin/Ethical_Constraints.md` — Tier 1; hard floors for all
  engineering decisions; Anti-Weaponization and Life Preservation
  doctrines are not subject to engineering authority override
- `Admin/Canonical_Terms.md` — vocabulary reference; engineering
  contributions must use canonical terms; new terms introduced by
  engineering work should be routed here for registration
- `Architecture/Cognitive_Frameworks.md` — defines how Forge systems
  think under uncertainty; this file defines how contributors engineer
  solutions; explicit integration mapping deferred to EP-003
- `Admin/Trajectories.md` — destination for engineering capabilities
  that are valid future work but out of current version scope
- `Discovery.md` — primary navigation layer; mandatory first search
  target for all engineering problem-solving
- `Unknowns.md` — EP-001 through EP-004 to be added to Governance &
  Verification section at next Unknowns.md update

---

## Drift Indicators

Mandatory re-audit conditions for this document. All canonical triggers
from `Admin/File_Template.md` apply. The following are additional local
triggers specific to Engineer_Protocols.md:

| Trigger | Reason |
|---------|--------|
| The 10-question framework is modified to remove safety or failure-learning questions | Safety and failure-learning are load-bearing — the framework is not complete without them |
| Assumption Challenge Triggers are removed or made optional | Mandatory challenge doctrine is the primary defense against reasoning drift in multi-agent workflows |
| Discovery.md is removed as the primary search target | Anti-reinvention doctrine depends on a stable primary navigation anchor |
| Unknown Discovery Doctrine removed from Section 6 | Untracked unknowns compound silently — logging doctrine is mandatory |
| Section 8 Hazard Escalation table revised without cross-validating against owning file sidecars | Hazard unknowns change as files are updated — table must stay current |
| "Acceptable risk threshold" referenced without pointing to a defined standard | EP-005 — subjective threshold produces audit-inconsistent escalation decisions |
| EP-005 or EP-006 closed without formal resolution entry | Both require documented resolution criteria — silent closure is not permitted |
| Lessons Learned evidence type labels diverge from repository Truth Provenance vocabulary | Repository alignment requires Measured / Estimated / Analogous / Placeholder labels |

**Compound Drift Rule:** Multiple simultaneous triggers escalate to
human review.
