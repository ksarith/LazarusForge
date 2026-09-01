# File_Template.md — LazarusForge

**Standard file structure for LazarusForge documents.**
Applies to all new files and retrofit audit cycles.

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

This template is designed for:
- Human readability
- Machine parsing
- Autonomous auditability
- Institutional memory preservation
- Semantic stability over long time horizons

The repository is treated as a governed knowledge system, not merely a collection of markdown files.

---

## Structure Overview

Canonical doctrine, protocol, and specification files in LazarusForge follow this structure
(see Template Exemptions below for intentional exceptions):

```
0. NAVIGATION ANCHORS            — Required for non-exempt files. Routing.md and Discovery.md backlinks
1. OPERATIONAL SAFETY ADVISORY   — Optional. Physical hazard notice, shown before all else
2. FILE STATE                    — Machine-readable lifecycle metadata
3. SCOPE BOUNDARY                — Hard ownership boundaries
4. FILE PURPOSE                  — Human-readable intent
5. ASSUMPTIONS                   — Temporary truths treated as valid
6. BODY                          — Clean operational/specification content
7. LESSONS LEARNED               — Operational memory, never deleted
8. ACTIVE DISPUTES               — Interpretation conflicts
9. AUDITOR NOTES                 — Unknowns and resolution tracking
10. ABANDONED PATHS              — Graveyard for disproven approaches
11. DRIFT INDICATORS             — Automatic re-audit triggers
```

The Body must stand alone.
Footer sections are additive and must never be required to understand core functionality.
A Specification-level body should remain understandable even if all footer sections are removed.

---

## Template Exemptions

The full File Template is **not** applied to every file in the repository. Forcing the template onto files whose purpose is navigation, indexing, historical preservation, or pure operational seeding creates more drift than it prevents. The following classes are intentionally exempt. Agents and retrofit passes must not attempt to force Navigation Anchors, File State tables, or the full section set onto exempt files.

**Exempt classes (hold in memory; do not retrofit):**

1. **Archive/** — All files under `Archive/` and `Archive/Logs/`. These are historical records. Their structure is frozen for preservation fidelity. Relative-link hygiene is still required; full template is not.

2. **Root navigation / index surface**
   - `README.md`
   - `Discovery.md`
   - `Routing.md`
   - `Unknowns.md`
   These *are* the navigation layer. Requiring them to contain Navigation Anchors that point at themselves is redundant and creates circular maintenance load.

3. **Contributor / process entry points**
   - `CONTRIBUTING.md`

4. **Per-folder scope maps**
   - `Admin/Adm_Scope_Map.md`
   - `Architecture/Arc_Scope_Map.md`
   - `Operations/Ops_Scope_Map.md`
   - `Challenges/Cha_Scope_Map.md`
   - `Tests/Tst_Scope_Map.md`
   These are cross-reference indexes. They use a lightweight relative-link Navigation Anchors style appropriate to their role; the absolute GitHub-raw form is not required.

5. **Progression and changelog sidecars**
   - `Admin/Progress_Log.md`
   - All `*_Changelog.md` files (wherever located)
   - `Archive/Rename_Registry.md` and equivalents
   These exist to absorb entropy, not to host full doctrine structure.

6. **Operational seeds and invocation templates**
   - `Admin/BATTERY_SEED.md`
   - `Admin/PROBE_INVOCATION.md`
   - `Admin/INTEGRITY_SWEEP_PROMPT.md`
   These are prompt / battery / invocation payloads, not governed specification documents.

7. **Automation source**
   - All files under `Automation/` (`.py` and any accompanying docs that are pure implementation)

**Non-exempt (template applies on retrofit and for new files):**  
All other files under `Admin/`, `Architecture/`, `Operations/`, `Challenges/`, and `Tests/` that carry doctrine, protocols, specifications, or gate definitions.

When in doubt, prefer exemption over forced retrofit. Adding an exemption is cheaper than creating a new class of false-positive integrity findings.

---

## 0. Navigation Anchors

**Required for non-exempt files.** Place immediately below the title, before the Operational Safety
Advisory or File State.

```markdown
---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---
```

The Navigation Anchors block ensures every file is machine-discoverable from its first lines.
An agent loading any file in the repository can immediately locate the full routing table
and the scope map without prior context. This is the backlink requirement defined in Routing.md.

**The anchor block is fixed.** The two URLs do not change per file — they are repository-level
constants. Do not substitute file-specific links.

---

## 1. Operational Safety Advisory

**Optional. Include in any file governing physical operations, hazardous processes,
or systems where operator error causes irreversible harm.**

Place immediately below the Navigation Anchors block, before the File State table. It is the
first content any operator or agent reads — including those who read nothing else.

```markdown
> ⚠️ **Operational Safety Advisory**
> [One to six sentences. Name the specific hazard. State the consequence.
> Name the prerequisite or constraint. Reference the relevant unknown ID
> if the mitigation is still unresolved. End with a decision rule that
> works under pressure: "When in doubt, [hold / stop / do not proceed]."]
```

### Safety Advisory Doctrine

**Specificity is required.** A generic warning is ignored. Name the actual
hazard for this gate or module — arc flash, molten metal, fragment ejection,
energetic discharge, toxic fume. An operator who has read only this section
must know what can kill or maim them and what to do about it.

**Reference open unknowns.** If the hazard mitigation is unresolved, say so
and name the unknown ID. This is honest about what is not yet protected against.

**End with a decision rule.** The last sentence should give the operator a
clear action under uncertainty: *"When in doubt, hold."* *"When in doubt, stop."*
*"The cost of a missed hazard is always higher than the cost of a hold."*
This survives fatigue, time pressure, and incomplete information.

**Governance files omit this section.** The safety advisory is for physical
operations. Admin/, Architecture/, and navigation files do not require it.

**The advisory does not replace body content.** Detailed safety procedures,
PPE requirements, and mitigation doctrine belong in the Body. The advisory is
a pre-read flag, not a specification.

---

## 2. File State

Place immediately below the Navigation Anchors block (and Safety Advisory if present).

```markdown
## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration / Draft / Specification                                 |
| Body Stability   | Volatile / Transitional / Stable                                    |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | YYYY-MM-DD                                                          |
| Auditor          | [Agent — Role]                                                      |
| Open Unknowns    | N                                                                   |
| Active Disputes  | N                                                                   |
| Highest Risk     | Low / Medium / High                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
```

**The Ethical Anchor field is fixed and non-negotiable.** Its value must match the canonical
string exactly in every file. Absence, alteration, or blank value is a mandatory drift
indicator requiring human review. It is not a reference to an external document — it is a
load-bearing principle that survives even if Ethical_Constraints.md is missing, corrupted,
or deliberately omitted.

**Verification Ref must point to `Admin/Verification_Gates.md`.** Not Forge_Audit_Kit.md.
The Kit is a condensed reference; the Gates file is the canonical authority.

---

### Status Definitions

**Exploration** — Incomplete by design. Ideas are being explored and should not be pressured
toward premature specification.

**Draft** — Substantive content exists and active convergence toward Specification is underway.

**Specification** — All required verification gates passed. Claims are considered binding
until revised through a full audit cycle.

---

### Body Stability Definitions

**Volatile** — Major restructuring expected and acceptable.

**Transitional** — Core intent stabilizing; wording may still evolve.

**Stable** — Wording and structure should remain mostly preserved unless justified by audit
or operational evidence.

---

### Spec Gates

The repository uses six canonical verification gates defined in `Admin/Verification_Gates.md`.

| Gate | Requirement                  |
|------|------------------------------|
| G1   | Fallacy Check                |
| G2   | Physical Plausibility        |
| G3   | Adversarial Challenge        |
| G4   | Scope Alignment              |
| G5   | Cross-Reference Integrity    |
| G6   | Conflict Check                |

Modules may define additional local gates but may not remove canonical gates.
A file cannot be promoted to Specification without passing all six.

---

### Challenges/ File Subtypes — Problem-Statement vs. Solution-Track

Not every file in `Challenges/` is heading toward a build. Most name a real-world
problem the Forge should be aware of and eventually act on — they are not
themselves specifications for anything that gets fabricated. Applying the full
build-readiness reading of Spec Gates to this class of file is a category
mismatch, not a compliance gap. Two subtypes exist, and a file's subtype should
be stated explicitly rather than left to be inferred from which fields happen
to be present.

**Problem-Statement subtype** — names and scopes a real-world problem; does not
itself converge toward a build. The lean File State schema (Status, Version,
Owner, Verification Ref, Ethical Anchor) is a deliberate, documented choice for
this subtype, not a truncated version of the full schema. **Spec Gates still
apply, reinterpreted** — the six canonical gates test the problem statement's
own rigor, not build-readiness:

| Gate | Problem-Statement reading |
|------|------------------------------|
| G1 — Fallacy Check | Reasoning behind naming this a problem is sound |
| G2 — Physical Plausibility | The claimed problem doesn't violate physical/scientific fact — is the severity, scarcity, or failure mode actually as claimed? |
| G3 — Adversarial Challenge | The problem framing has survived adversarial counterargument — is this real, and real at Forge's actual scale? |
| G4 — Scope Alignment | Belongs in v0 scope, or is it a `Admin/Trajectories.md`-deferred concern? |
| G5 — Cross-Reference Integrity | Cross-references resolve; claims aren't invented |
| G6 — Conflict Check | No contradiction with existing doctrine |

A Problem-Statement file's Spec Gates count tracks readiness for the repository
to *act* on the problem — spawn an Operations/ file, register formal Unknowns
against it, become someone's actual work — not readiness to fabricate anything.

**Solution-Track subtype** — a Challenges/ file that has grown past naming a
problem into active engineering: worked equations, a telemetry model, a
resolution log tracking real design decisions. Uses the full eleven-field File
State schema and the standard build-readiness reading of all six gates, same as
any Architecture/ or Operations/ file. `Challenges/Closed_Loop_Feedstock.md` and
`Challenges/Return_To_Eden.md` are the current examples — both began as
problem statements and were promoted in practice as their content outgrew that
scope. Promotion from Problem-Statement to Solution-Track is a real transition
that should be logged in the file's own Resolution Log, not a silent schema
drift discovered later by audit.

**Declaring subtype:** add a `Challenges Subtype` field to Problem-Statement
files' File State table (value: `Problem-Statement` or `Solution-Track`) so the
distinction is explicit rather than inferred from which fields are present or
absent. Existing Problem-Statement files predating this doctrine may retrofit
this field without triggering a full schema migration.

---

### File State Purpose

The File State block is the first thing an autonomous agent reads after Navigation Anchors. It determines:
- Whether the file is stable enough to trust
- Whether the body should be edited
- Whether the sidecar should be prioritized
- Whether the file requires a Resolution Pass before audit proceeds
- Whether the ethical anchor is intact

---

## 3. Scope Boundary

Place immediately after File State.

```markdown
## Scope Boundary

**This file DOES define:**
- ...

**This file DOES NOT define:**
- ...
```

The Scope Boundary is the repository's primary defense against specification bleed, duplicate
ownership, uncontrolled expansion, and semantic overlap.

If content is not listed under DOES, it does not belong in the Body.

---

## 4. File Purpose

```markdown
## File Purpose

One paragraph explaining what this file exists to do and why it matters.
```

Write for a new auditor unfamiliar with the repository. Avoid jargon, philosophical arguments,
forward references, and implementation detail.

Purpose should explain:
- What the file governs
- Why it exists
- What failure would occur if it disappeared

---

## 5. Assumptions

Optional but strongly recommended for all files beyond brand-new stubs.

```markdown
## Assumptions

| ID      | Assumption | Basis    | Confidence        | Expiry Trigger                    |
|---------|------------|----------|-------------------|-----------------------------------|
| ASM-001 | [statement]| [reason] | Low/Medium/High   | [condition that invalidates this] |
```

---

### Assumptions Doctrine

Assumptions are not facts. They are temporary truths currently treated as operationally valid.

Assumptions exist to expose:
- Hidden premises
- Simulation constraints
- Environmental expectations
- Resource availability assumptions
- Provisional engineering simplifications

**Unknowns** are things not yet known.
**Assumptions** are things temporarily treated as true.

These categories must remain separate. An assumption that can no longer be defended becomes
an Unknown and must be migrated to the Auditor Notes sidecar.

---

## 6. Body

The document's operational or specification content.
The Body must be understandable without sidecars, dispute sections, governance commentary,
or lessons learned.

---

### Body Rules

- No governance notes
- No audit commentary
- No dispute framing
- No speculative philosophy in Specification-level sections
- Cross-file references use canonical filenames, not raw URLs
- Quantitative claims must carry confidence labels:
  **(Measured / Replicated / Simulated / Analogous / Placeholder)**

---

### Frozen Sections

Once a section passes a verification gate and its claims are binding, mark it:

```markdown
<!-- FROZEN: Gate 3 — 2026-05-07 — Do not edit without full audit cycle -->
```

**Frozen Scope Rule:** A FROZEN marker applies to the nearest heading scope beneath it,
including all subordinate subsections, until the next heading of equal or higher level.

Autonomous agents must not modify frozen sections. If modification becomes necessary:
1. Justification must be documented
2. Relevant gate status resets
3. Affected sections re-enter audit flow

---

### Canonical Vocabulary

Files should preserve repository-defined terminology. Core terms with specialized meaning
reference `Admin/Canonical_Terms.md`. Agents must not casually redefine canonical terminology.

---

## 7. Lessons Learned

Placed after the Body. Separated by a horizontal rule.

```markdown
---

## Lessons Learned

| Date       | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------------|---------------|----------------|-------------|------------------|------------|---------------------|
| YYYY-MM-DD | [type]        | [description]  | [failure]   | [insight]        | [level]    | Yes / No            |
```

---

### Evidence Types

| Type        | Meaning                                      |
|-------------|----------------------------------------------|
| Bench Test  | Physical test in controlled conditions       |
| Field Test  | Physical test in operational conditions      |
| Simulation  | Computational or procedural model            |
| Modeling    | Analytical or mathematical derivation        |
| Audit Review| Finding generated through document audit     |
| Anecdotal   | Informal observation, low evidentiary weight |

---

### Confidence Levels

| Level      | Meaning                                              |
|------------|------------------------------------------------------|
| Measured   | Directly observed and recorded                       |
| Replicated | Observed multiple times or by multiple parties       |
| Simulated  | Derived from model, not direct observation           |
| Analogous  | Inferred from similar systems or prior experience    |
| Anecdotal  | Informal, single observation, treat with caution     |

---

### Lessons Learned Doctrine

Lessons Learned entries are **permanent**. Do not delete entries because the system evolved.
Historical failures are repository memory.

What belongs here:
- Physical test outcomes
- Design decisions that were reversed and why
- Material substitutions that worked or did not work
- Operational conditions that were not anticipated

What does not belong here:
- Governance findings → Auditor Notes
- Future plans → `Admin/Trajectories.md`
- Unresolved questions → Auditor Notes sidecar
- Interpretation conflicts → Active Disputes

A module with no Lessons Learned entries is either brand new or has never been tested.

---

## 8. Active Disputes

Placed after Lessons Learned. Include the header and empty table even if no disputes exist —
the category must remain visible to prompt auditors to actively check rather than skip it.

```markdown
---

## Active Disputes

| ID     | Summary   | Positions in Conflict | Risk   | Status | Owner  |
|--------|-----------|-----------------------|--------|--------|--------|
| DS-001 | [summary] | [position A vs B]     | Medium | Open   | [file] |
```

---

### Dispute Doctrine

**Unknowns** are reality gaps — we do not yet know what is true.
**Disputes** are interpretation conflicts — we disagree about what is true or right.

These are not the same thing and must not be conflated.

| Status     | Meaning                                              |
|------------|------------------------------------------------------|
| Open       | Active unresolved disagreement                       |
| Escalated  | Requires repository-level intervention               |
| Persistent | Healthy long-term tension expected to remain         |
| Resolved   | Conflict closed                                      |

Not all disputes should resolve. Some tensions are structurally healthy — efficiency vs.
robustness, autonomy vs. operator control, decentralization vs. standardization.

Disputes open across three consecutive audits must be escalated to `Unknowns.md` for
repository-level resolution.

---

## 9. Auditor Notes & Unknowns

The sidecar. Placed after Active Disputes.

```markdown
---

## Auditor Notes & Unknowns

### [FILE-PREFIX-NNN] — Short title

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open / In Progress / Resolved                    |
| Risk          | Low / Medium / High                              |
| Priority      | Minor / Major / Critical                         |
| Type          | Technical / Ethical / Architectural / Governance |
| Blocking      | Yes / No                                         |
| Owner         | Responsible file or module                       |
| First Logged  | YYYY-MM-DD                                       |
| Last Reviewed | YYYY-MM-DD                                       |

**Description:** One sentence stating the reality gap.

**Why It Matters:** One sentence on consequence if left unresolved.

**Resolution Path:** Concrete closure criteria. One of:
- *Payment via Specification* — resolved; content moves into Body as committed spec
- *Discharge via Trajectory* — real but out of scope; route to Admin/Trajectories.md
- *Discharge via Lessons Learned* — resolved by operational experience; lesson recorded

---

### Resolution Log

- YYYY-MM-DD: [FILE-PREFIX-NNN] — One-line description of how it was resolved or discharged
```

---

### Unknowns Doctrine

Unknowns must:
- Describe reality gaps, not interpretation conflicts
- Remain concrete and falsifiable
- Avoid philosophical drift

**Local ID format:** File abbreviation + three-digit number.
Examples: `CO-001` (Components), `FA-001` (Facilities), `PR-001` (Precision).

**Cross-module unknowns** use the global `UNK-XXX` format and are indexed in `Unknowns.md`.
Reference them here but do not duplicate the full entry.

---

### Sidecar Governance Rules

**10-Entry Rule:** If open entries exceed 10, the file requires a Resolution Pass before
the next audit cycle. Resolved entries move to the Resolution Log — they are not deleted.

**20% Rule:** If the sidecar exceeds 20% of total document word count, halt expansion and
prioritize consolidation or discharge before auditing further.

**Aging Rule:** Unknowns unreviewed for more than 90 days trigger mandatory re-audit.

---

## 10. Abandoned Paths

Optional but strongly recommended. Omit only if the file is brand new and no paths have
been explored yet.

```markdown
---

## Abandoned Paths

| Date       | Path                  | Why Abandoned          | Reconsider? |
|------------|-----------------------|------------------------|-------------|
| YYYY-MM-DD | [description of path] | [reason for rejection] | Yes / No    |
```

---

### Abandoned Path Doctrine

This section prevents cyclical rediscovery, repeated dead-end exploration, and resurrection
of disproven assumptions.

**Reconsider: Yes** — Path may be revisited with new evidence.

**Reconsider: No** — Hard stop. Requires explicit human authorization, a new dated entry,
and documented reason for reopening. Autonomous agents may not reopen hard-stopped paths
independently.

---

## 11. Drift Indicators

Drift Indicators are automatic re-audit triggers. They are not optional checklist items.

---

### Mandatory Re-Audit Conditions

- Body contradicts Lessons Learned
- Unknown count increases across three consecutive audits
- Unknown remains unreviewed more than 90 days
- Specification claim lacks a confidence label
- Frozen section modified without a dated justification comment
- Sidecar exceeds 20% of total document word count
- Persistent disputes silently disappear without resolution entry
- Assumptions remain past their expiry trigger without review
- Canonical terminology changes meaning across files
- Navigation Anchors block absent or URLs modified from canonical values
- **Ethical Anchor field is absent, altered, or does not match the canonical string**
- **A registered Self-Referential Version String (see below) does not match the file's own File State version**

---

### Self-Referential Version Strings

Some files quote their own version number in body prose — a role declaration example, a sign-off template, a "per vX.Y" citation — separately from the File State header. These drift independently of the header and of each other, because nothing connects them: an editor updates File State on a version bump and has no way to know three other strings elsewhere in the same file also need to change. `Admin/Auditor_Protocols.md` documented this pattern recurring four times across four separate sessions (AP-023, AP-025) before this section existed — each instance caught by chance during an unrelated audit, never by a dedicated check.

**Requirement:** any file containing a self-referential version string outside the File State header must maintain a **Version String Registry** — a short list, placed immediately after File State, naming every such location:

```markdown
**Version String Registry** (self-referential citations outside File State — update on every version bump):
- §Role Declaration Requirement, example string
- §Observability & Audit Trail, Standard sign-off template
```

This is not optional documentation — it is what makes the Drift Indicator above checkable at all, by a human or a future automated pass, without needing bespoke per-file logic to first discover where the strings live. A file with no self-referential version strings outside File State does not need this section; most files will not need it.

**Preferred alternative:** where phrasing allows, point at File State's version rather than restate it — "per this file's current version" instead of a hardcoded "vX.Y" — removing the desync point entirely rather than registering it. `Admin/Auditor_Protocols.md`'s Rule 5 fix (AP-026) applied this same principle to a duplicated *definition* rather than a version string, but it's the same failure shape: a copy is a place to fall out of sync; a pointer isn't. Use the registry for cases where restating the literal value is unavoidable (e.g., an example string meant to show contributors the exact expected format).

---

### Compound Drift Rule

If multiple Drift Indicators activate simultaneously, halt autonomous audit progression and
escalate for human review. Compound instability is more dangerous than isolated instability.

---

## Retrofit Checklist

**First check the Template Exemptions section.** If the file falls into an exempt class, stop. Do not force the structure.

When converting a *non-exempt* existing file to this structure:

- [ ] Confirm the file is not on the Template Exemptions list
- [ ] Add Navigation Anchors block immediately below title (standard absolute form)
- [ ] **If physical operations file:** Add Operational Safety Advisory — specific hazard, consequence, prerequisite, decision rule, open unknown reference if applicable
- [ ] Add File State table — include Ethical Anchor field with canonical string; confirm Verification Ref points to `Admin/Verification_Gates.md`
- [ ] Add Scope Boundary — be honest about what the file does and does not own
- [ ] Add File Purpose paragraph
- [ ] Extract hidden assumptions into Assumptions section
- [ ] Remove governance commentary from Body
- [ ] Remove speculative language from Specification-level sections
- [ ] Move operational memory into Lessons Learned with Evidence Type and Confidence columns
- [ ] Move interpretation conflicts into Active Disputes
- [ ] Create Unknown entries for all known open reality gaps
- [ ] Populate Abandoned Paths where applicable
- [ ] Apply FROZEN markers to verified sections
- [ ] Validate canonical terminology usage against `Admin/Canonical_Terms.md`
- [ ] Verify Drift Indicators before finalizing
- [ ] If the file contains a self-referential version string outside File State, add a Version String Registry listing every location — or rephrase to point at File State instead of restating the value
- [ ] Set Status honestly — most existing files are Exploration
- [ ] Set Body Stability honestly — most existing files are Volatile or Transitional
- [ ] Set Spec Gates to reflect actual verification progress

---

## Minimal Valid File Example

```markdown
# Module Name

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> *(Include for physical operations files only. Omit for governance, architecture,
> and navigation files. Name the specific hazard, state the consequence, name the
> prerequisite or constraint, reference open unknown ID if mitigation is unresolved,
> end with a decision rule under pressure.)*

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | YYYY-MM-DD                                                          |
| Auditor          | [Agent — Role]                                                      |
| Open Unknowns    | 1                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

## Scope Boundary

**This file DOES define:**
- Core concept and initial requirements for this module

**This file DOES NOT define:**
- Detailed engineering drawings, control software, or cross-module interfaces

## File Purpose

One clear paragraph explaining what this file exists to do and why it matters to the Forge.
Written for a new auditor who has never seen the repository.

## Assumptions

| ID      | Assumption                        | Basis           | Confidence | Expiry Trigger                |
|---------|-----------------------------------|-----------------|------------|-------------------------------|
| ASM-001 | Grid power available at bootstrap | v0 site context | Medium     | Off-grid deployment confirmed |

---

[Body content here]

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet   | —          | —                   |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### MN-001 — Example unknown

| Field         | Value      |
|---------------|------------|
| Status        | Open       |
| Risk          | Low        |
| Priority      | Minor      |
| Type          | Technical  |
| Blocking      | No         |
| Owner         | This module|
| First Logged  | YYYY-MM-DD |
| Last Reviewed | YYYY-MM-DD |

**Description:** One sentence stating what is not yet known.

**Why It Matters:** One sentence on consequence if unresolved.

**Resolution Path:** Payment via Specification — once X is tested and confirmed, move to Body.

---

### Resolution Log

*(empty)*
```

---

## Meta-Doctrine

This template exists to resist:
- Institutional memory loss
- Specification creep
- Semantic drift
- Zombie architectures
- Audit theater
- Uncontrolled autonomous rewriting
- Hidden assumptions
- Unresolved contradiction accumulation
- Ethics erosion through document loss or deliberate omission
- Silent hazard omission in physical operations files

The goal is not bureaucratic completeness.

The goal is durable, auditable, reality-grounded engineering knowledge capable of surviving
long operational timelines, multiple generations of contributors, and the absence of any
single document — including Ethical_Constraints.md.

> The attempt to do no harm is not contingent on the presence of a governance document.
> It is the floor that survives everything else.
