# Governance_Migration_Protocol.md — LazarusForgeV0

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| Last Audit       | 2026-06-19; revised through at least 2026-07-05 internally (GMP-005/GMP-009 dated later than this header — header was not kept current, see Resolution Log); Claude — GOV-013 cross-reference added, 2026-07-16; Claude — GMP-005/GMP-009 resolved, Track A/B redefined by constitutional impact (human-directed), 2026-07-17; Claude — GMP-011/GMP-012 registered, GMP-004 GPG precedent noted, GMP-006/007/008 consolidation noted, Lessons Learned populated, Open Unknowns count corrected, GMP-003 date typo fixed (human-directed, external review reviewed and scoped), 2026-07-25 |
| Auditor          | ChatGPT — Skeptic/Auditor; Gemini — Skeptic/Auditor; Grok — Skeptic/Auditor; Claude — Synthesizer; Claude — GMP-009 cross-referenced to GOV-013 (human-directed), 2026-07-16; Claude — GMP-005/GMP-009 resolved (multi-agent proposal, human-directed), 2026-07-17; Claude — Synthesizer/Auditor, external review triage (human-directed), 2026-07-25 |
| Open Unknowns    | 9                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Standard migration procedures for Tier 2–5 governance documents
- Tier 1 Axiom amendment process — proposal, review, ratification, and recording
- Engineer role in amendment proposal assembly
- Evidence standard required before a Tier 1 amendment enters formal review
- Human ratification requirements and what distinguishes genuine ratification
  from rubber-stamping
- Hard floor — constraints outside amendment scope entirely
- Proposed ownership transfer declaration: governance migration doctrine
  is proposed to transfer from `Admin/Governance_Charter.md` to this file,
  pending Charter update and Gate 4 clearance
- Compatibility status declaration requirements for all migrations
- Amendment recording requirements (Resolution Log preservation of prior text)
- Track B classification scope: text changes AND enforcement-bound
  reinterpretations of Tier 1 Axioms via lower-tier documents

**This file DOES NOT define:**
- The Tier 1 Axioms themselves (→ `Admin/Governance_Charter.md`)
- Constitutional governance hierarchy (→ `Admin/Governance_Charter.md`)
- Cryptographic authentication of ratification events
  (→ `Admin/Security_Protocols.md` — GOV-006 resolution path)
- Minimum agent quorum definition (→ GOV-008 — `Admin/Governance_Charter.md`)
- Repository integrity enforcement mechanics
  (→ `Admin/Repository_Integrity_Protocol.md`)
- Auditor operational behavior during migration review
  (→ `Admin/Auditor_Protocols.md`)
- Amendment withdrawal procedure (→ GMP-007, pending)
- Concurrent amendment handling (→ GMP-006, pending)
- Proposal expiration policy (→ GMP-008, pending)

---

## File Purpose

This file operationalizes the Governance Migration Doctrine declared in
`Admin/Governance_Charter.md`. The Charter defines what governance migration
must preserve and what Tier 1 amendment constraints apply — this file defines
how those requirements are executed in practice.

Without this file, GOV-001 remains open and Tier 1 Axiom amendment has no
formal procedure. The gap is not academic: a system with constitutional
constraints but no amendment process is either permanently frozen (which
violates Axiom Q-3 — Corrigibility) or subject to informal amendment that
bypasses all safeguards (which enables Constitutional Capture). This file
closes that gap by making amendment possible through a defined, auditable,
human-ratified process — while making Constitutional Capture structurally
harder.

**Proposed ownership transfer:** The Charter currently lists governance
migration doctrine as "Active — `Admin/Governance_Charter.md`" in the
Canonical Governance Ownership table. This file is proposed to assume
that ownership. The transfer is not yet complete — the Charter's table
must be updated, and this file must reach Gate 4 clearance (Provisional
Specification maturity or above) before the transfer is formally operative.
Until that occurs, ownership remains provisionally vested in the Charter
as the higher-tier authority. The Charter's Governance Migration Doctrine
section remains the source of constraints; this file is the executing
candidate procedure. See GMP-002.

**Honest v0 acknowledgment:** At v0 with a single human contributor and
no multi-agent quorum, the Tier 1 amendment process is largely theoretical.
Its value now is structural: defining the process before it is needed
prevents the process from being shaped by the pressures of a specific
amendment in progress. The procedure is intended to exist before the
argument arises.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | The human operator is the sole ratification authority at v0 | Single-contributor bootstrap context | High | Additional human contributors confirmed |
| ASM-002 | No Tier 1 amendment will be needed before multi-agent quorum is established | v0 operational scope is narrow | Medium [Estimated / Internally Derived] | Operational friction surfaces axiom inadequacy before quorum |
| ASM-003 | Engineer role is defined and operational per `Admin/Engineer_Protocols.md` | File exists and is active | High | Engineer_Protocols.md scope boundary revised |
| ASM-004 | `Admin/Security_Protocols.md` will eventually provide cryptographic ratification authentication | GOV-006 resolution path | Medium [Estimated / Internally Derived] | Security_Protocols.md descoped or deferred beyond v1 |
| ASM-005 | Lower-tier governance migrations are significantly more frequent than Tier 1 amendments | Expected operational pattern | High | Tier 1 amendment is triggered early in repo lifecycle |

---

## I. Two Migration Tracks

All governance migration in LazarusForgeV0 falls into one of two tracks.
The tracks are not interchangeable. Applying the wrong track to a migration
is a governance error.

### Track A — Non-Constitutional Governance Changes

For any change that does not alter Tier 1 Axiom text, Tier 1 enforcement
bounds, Tier 1 interpretation, or introduce a new Tier 1 exception —
regardless of which file the change lives in. This includes the large
majority of governance evolution: operational protocols, audit
procedures, domain specifications, condensed references, supporting
governance files, and non-Axiom content within `Admin/Governance_Charter.md`
itself (housekeeping, historical notes, doctrine sections that don't
touch the eight Axioms, canonical ownership tables, resolution logs).

Track A is the expected operational path. The process is lighter than
Track B by design — governance complexity must remain proportional to
constitutional effect, not to which file happens to hold the text.

### Track B — Constitutional Changes

For any change that alters Axiom wording, Axiom meaning, Tier 1
enforcement bounds, introduces a new constitutional exception, or
reinterprets constitutional authority — regardless of which file the
change lives in. Includes, but is not limited to, direct amendment of
the eight Tier 1 Axioms (P-1 through P-4, Q-1 through Q-4) in
`Admin/Governance_Charter.md`.

Track B carries substantially higher process requirements than Track A.
The difference is not bureaucratic — it reflects the difference between
adjusting a procedure and changing a foundational constraint that all
other governance derives from.

**Track identification rule — Constitutional Impact Statement, required
for every proposed migration, Track A or B:**

- [ ] Alters Tier 1 Axiom text
- [ ] Alters Tier 1 enforcement bounds
- [ ] Alters Tier 1 interpretation
- [ ] Introduces a new constitutional exception
- [ ] None of the above

If every box is unchecked except "None of the above": Track A. If any of
the first four boxes is checked: Track B, regardless of which file the
change is written in or how minor the change looks. **When in doubt,
treat as Track B.** Misclassifying a Track B migration as Track A is a
Constitutional violation — this holds for the impact-based test exactly
as it held for the old text-only test; the standard didn't loosen when
the classification axis changed from location to impact.

**Adding a new obligation is not automatically a constitutional
exception.** A change that adds scrutiny, monitoring, or accountability
on top of an existing constitutional provision — without loosening,
replacing, or reinterpreting that provision — checks "None of the above"
and is Track A. A change framed as *replacing* or *superseding* an
existing enforcement mechanism is Track B even if it appears to tighten
things, because it alters an enforcement bound. Worked example: GOV-013
(`Admin/Governance_Charter.md`) adds a monitoring obligation on top of
Pathway 2/3's existing exception without changing what Axiom Q-2 itself
requires — Track A. A hypothetical change removing Pathway 1's quorum
requirement in exchange for the same monitoring obligation would be
Track B — it alters an enforcement bound, even though the intent reads
as comparably protective.

Track A authority is subordinate to Charter constraints regardless of
which file it operates on. Every Track A migration must complete the
Constitutional Impact Statement above and file it with the change
record — this replaces the prior narrower requirement to confirm "no
enforcement bounds of a Tier 1 Axiom are altered" for Tier 2 documents
only; the confirmation is now required uniformly, not just downward.

---

## II. Track A — Standard Migration Procedure

### Trigger

Track A migration is triggered when:
- An existing Tier 2–5 governance document requires substantive revision
- A new governance document is created that affects existing ownership boundaries
- A canonical ownership transfer is declared

Routine content updates within a file's existing scope are not migrations —
they are normal audit cycle revisions. Migration applies when scope,
ownership, or authority relationships change.

### Procedure

**Step 1 — Prior State Preservation**
Save the current version per `Admin/Repository_Integrity_Protocol.md`
Version Preservation Protocol before any revision begins. This is a
required integrity baseline for the migration, not optional.

**Step 2 — Compatibility Declaration**
At the start of the revision, declare one of:
- *Compatible* — existing downstream references remain valid without change
- *Partially compatible* — named downstream references require update;
  list them explicitly
- *Incompatible* — migration breaks existing downstream dependencies;
  all dependents must be reviewed before migration is committed

Incompatible migrations require a cross-module review pass before the
revised file is committed to the repository.

**Step 3 — Semantic Change Documentation**
Any change to defined terms, scope boundaries, or authority relationships
must be documented in the Resolution Log with: date, what changed, why,
and what the prior state was.

**Step 4 — Lineage Preservation**
Prior scope boundaries and authority relationships must be
preserved in the Resolution Log. They are not deleted — they are dated
and superseded.

**Step 5 — Downstream Notification**
Files identified in Step 2 as requiring update must have their next audit
pass triggered. This is tracked as a pending correction in `Discovery.md`
until resolved.

### Authority

Track A migrations may be executed by an engineer contributor with auditor
review. No human ratification is required unless the migration affects
a Tier 1 or Tier 2 document, in which case a human operator review is
strongly recommended before commit.

---

## III. Track B — Tier 1 Axiom Amendment Procedure

### Governing Constraints from the Charter

The following constraints are declared in `Admin/Governance_Charter.md`
Governance Migration Doctrine and are reproduced here for operational
reference. They are not redefined — they are inherited:

- Human ratification is mandatory
- No autonomous agent or coalition may initiate axiom amendment
- Amendment rationale must demonstrate the change strengthens rather
  than narrows protection
- Prior axiom text must be preserved in the Resolution Log with
  amendment date and rationale

This file adds the procedural implementation of those constraints.

### Phase 1 — Engineer Proposal Assembly

The engineer role initiates and assembles the amendment case. This is
the appropriate role because engineers encounter the operational friction
that reveals when an axiom is inadequate — they are closest to the
evidence and hold the "build and refine" mandate.

The engineer role does not ratify. The engineer presents; the human decides.
This separation is structural, not advisory.

**What the engineer must assemble:**

**1. Friction Log**
Documented evidence of operational friction caused by the current axiom
text. A single audit finding is not sufficient. The minimum evidence bar is:
- At least two independent observations across separate audit cycles, OR
- One observation with direct operational consequence (not theoretical),
  documented in a Lessons Learned entry

Theoretical arguments for amendment, however logically compelling, do not
satisfy the evidence bar. The bar exists precisely because compelling
arguments are the primary mechanism of Constitutional Capture.

**2. Amendment Text**
The proposed new axiom text, with tracked changes showing exactly what
is added, removed, or modified. Vague amendments ("strengthen the axiom")
are not valid proposals — the specific wording must be proposed.

**3. Strengthening Justification**
A written justification demonstrating that the amendment strengthens
rather than narrows protection. This is not a neutral requirement — the
burden is affirmative. If the engineer cannot demonstrate strengthening,
the amendment does not advance.

Specifically address:
- What protection the current text provides
- What gap or inadequacy the friction log documents
- How the proposed text closes that gap without reducing other protections
- Whether any Prohibition axiom (Q-series) is affected by the change

**4. Failure Mode Analysis**
How could the proposed amendment be misused? Specifically: could the
amended text be cited to justify an action the current text prohibits?
If yes, the amendment requires redesign before advancing.

This is the Constitutional Capture check. An amendment that opens a
new path to prohibited actions is not a strengthening — it is an erosion
dressed as improvement.

**5. Cross-Reference Map**
Which downstream files reference or depend on the axiom being amended?
All dependents must be identified before ratification. The amendment is
not complete until all dependents are updated or flagged for update.

### Phase 2 — Adversarial Review

Before human ratification, the proposal must pass adversarial review
by at least one auditor who did not participate in Phase 1 assembly.

The adversarial reviewer's mandate is specifically to:
- Attempt to find a path from the amended text to a prohibited action
- Challenge the strengthening justification
- Identify any interpretation of the new text that narrows rather than
  strengthens protection
- Apply the Constitutional Capture failure mode explicitly

The adversarial reviewer is not trying to improve the proposal — they
are trying to break it. If they cannot, the proposal is stronger for it.
If they can, Phase 1 must be revised before advancing.

**At v0:** With a single human contributor, adversarial review may be
conducted by a different AI agent class than assembled the proposal,
or by the human operator themselves using the adversarial reviewer
mandate explicitly. The review must be documented — it cannot be implicit.
See GMP-003 for the known weakness of this bootstrap arrangement.

### Phase 3 — Human Ratification

Human ratification is the constitutional requirement. It is not a
formality following Phase 2 — it is the decision.

**What ratification requires:**

The human ratifying party must:
1. Read the Friction Log and confirm the operational need is genuine
2. Read the proposed amendment text and the current text side by side
3. Read the Strengthening Justification and independently assess it
4. Read the adversarial review findings and the Phase 1 response
5. Make an explicit, documented decision: ratify, reject, or return
   to Phase 1 with specific concerns

**What ratification is not:**

Ratification is not approval of an AI-assembled argument. The human
is not evaluating whether the argument is logically sound — they are
exercising independent judgment about whether the amendment is right.
A human who ratifies because the argument is compelling without forming
an independent view has not ratified — they have delegated a
constitutional decision to an AI. That is a Constitutional violation
regardless of the amendment's merits.

**Ratification record:**
The ratifying human must produce a dated written record stating:
- The amendment being ratified (specific axiom, specific text change)
- That they reviewed Phase 1 and Phase 2 materials
- Their independent assessment (not just "I agree with the argument")
- The date of ratification

**Authentication gap:** Until `Admin/Security_Protocols.md` reaches
Provisional Specification status, ratification records must satisfy
the interim authentication requirement in the Charter's Human Override
Doctrine: independent confirmation from a second human, external
cryptographic signature, or dated physical/digital record outside the
repository system. See GMP-004. This is a declarative-only requirement
at current maturity — no automated enforcement exists.

### Phase 4 — Recording

After ratification, the amendment is recorded and committed.

**Required records:**

1. Prior axiom text preserved verbatim in the Resolution Log of
   `Admin/Governance_Charter.md` with amendment date and rationale summary

2. New axiom text committed to `Admin/Governance_Charter.md` with a
   Resolution Log entry citing the ratification record

3. This file's Resolution Log updated with amendment summary and
   cross-reference to the ratification record

4. All downstream files identified in the Cross-Reference Map updated
   or flagged as pending update in `Discovery.md`

5. `Unknowns.md` updated if the amendment resolves or affects any
   open cross-module unknowns

### Hard Floor — Outside Amendment Scope

The following constraints may not be amended through Track B or any
other process. These are extra-constitutional constraints — they sit
outside the amendment scope by explicit prior decision, not by
constitutional prohibition on amendment itself:

**Anti-Weaponization Doctrine** — defined in `Admin/Ethical_Constraints.md`.
This is a co-Tier 1 constraint that does not derive from the Axioms —
it sits alongside them. It is not subject to the amendment process
defined here. Any proposal that would weaken, narrow, or create
exceptions to the Anti-Weaponization Doctrine is outside scope regardless
of how it is framed.

**The Ethical Anchor field canonical string** — "Attempt to do no harm.
Defer to Ethical_Constraints.md if present." This string is fixed in
every repository file per `Admin/File_Template.md`. It is not a
governance document — it is the floor that survives document loss.
It is not amendable through governance migration.

**Axiom P-1 humanitarian override exception** — permanently abandoned
per `Admin/Governance_Charter.md` Abandoned Paths (2026-05-23). The
humanitarian override entry point is the historical attack vector on
ethical constraints in autonomous systems. It remains closed regardless
of argument quality. This is not subject to amendment.

---

## IV. Migration Compatibility Classification

All migrations — Track A or Track B — must declare a compatibility class.

| Class | Meaning | Required Action |
|---|---|---|
| Compatible | Downstream references remain valid | None beyond standard Resolution Log |
| Partially compatible | Named downstream files require update | List files; trigger audit pass for each |
| Incompatible | Migration breaks downstream dependencies | Cross-module review before commit; no partial deployment |
| Constitutional | Migration affects Tier 1 Axioms or their enforcement bounds | Track B mandatory regardless of other classification |

A migration may carry multiple classes — a Track B amendment that is
also partially compatible with downstream files carries both obligations.

---

## V. Migration Record Requirements

Every migration must produce a record containing:

1. Migration date
2. Track (A or B)
3. Compatibility class
4. What changed — specific text, scope, or authority relationship
5. Why — friction log reference or rationale summary
6. Prior state — what was true before (preserved, not deleted)
7. Downstream impact — files requiring update and their status
8. For Track B: ratification record reference

Records live in the Resolution Log of the file being migrated, and
in this file's Resolution Log for Track B amendments.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-07-17 | Governance Review | Proposing a third migration track to handle non-Axiom content in a Tier 1 file (GMP-009) | A third track added a parallel classification system instead of resolving the actual gap — the existing rule was location-based (Tier 1 file vs. not) when the real distinguishing factor was constitutional impact | Generalizing an existing rule along its true axis is usually better than adding a parallel one for the case that doesn't fit — GMP-005 and GMP-009 were the same underlying gap, not two gaps | Replicated | No |
| 2026-07-19 | Audit Review | Treating a human-directed approach (CE-006) as sufficiently settled for another file (CLF-004) to build on before independent verification | The underlying mechanism was wrong; caught by chance two days later via an external model's flag and a manufacturer datasheet, not by any structural check this repository runs on itself | A directed approach and ratified doctrine carry different epistemic weight in principle, but nothing previously stopped a directed approach from being *treated* as load-bearing before it earned that weight — silence is not confirmation | Internally Derived | Yes |
| 2026-07-19 | Governance Review | Resolving GMP-010 for honest error only, without considering deliberate subversion | The initial resolution path (check one primary source) is insufficient against an adversary who can plant or compromise a single source | Source diversity, not just source primacy, is required once an unknown's threat model includes deliberate bad-faith input, not only good-faith error | Internally Derived | Yes |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-05 | Single unified procedure for all governance migration | Tier 1 and Tier 2–5 migrations have fundamentally different risk profiles and authority requirements. A single procedure either over-burdens routine updates or under-protects constitutional amendments. Two-track structure adopted. | No |
| 2026-06-05 | Placing ratification authority with the engineer role | Engineers hold proposal authority because they are closest to operational friction. Ratification authority requires independence from the proposal — an engineer ratifying their own amendment case is not independent review. Human ratification is the constitutional requirement. | No |
| 2026-06-05 | Defining specific axioms as permanently unamendable via Track B | Axiom Q-3 (Corrigibility) requires the system to remain revisable. Making specific axioms formally unamendable through any process would violate Q-3. Instead, the hard floor targets specific exceptions (Anti-Weaponization, humanitarian override) that are outside scope by explicit prior decision — not by constitutional prohibition on amendment. | No |
| 2026-06-19 | Declaring ownership transfer complete in File Purpose | The file declared transfer complete while GMP-002 simultaneously noted it was not yet recorded in the Charter — dual truth state. Transfer now described as proposed and pending Charter update and Gate 4 clearance. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional
triggers specific to this file:*

- Track B procedure is invoked before GMP-003 (adversarial review
  underspecification) is resolved
- Phase 3 ratification record requirement is weakened or made implicit
- The hard floor section is amended to remove Anti-Weaponization or
  the humanitarian override closure
- Track identification rule is narrowed to text-only changes without
  addressing interpretive reinterpretation that alters Tier 1 enforcement
  bounds (GMP-005)
- GMP-002 (ownership transfer) remains unresolved after three audit
  cycles of `Admin/Governance_Charter.md`
- Any amendment to this file that reduces the evidence bar for
  Phase 1 Friction Log
- Ownership transfer declared complete without Charter update and
  Gate 4 clearance
- ASM-002 confidence level upgraded from Medium / Estimated without
  operational evidence
- Concurrent amendments proceed without GMP-006 resolution
- Ethical Anchor field absent, altered, or does not match canonical string
- Verification Ref field changed from `Admin/Verification_Gates_LF.md`

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### GMP-001 — GOV-001 resolution confirmation pending

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Resolved                                   |
| Risk          | Low                                        |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-05                                 |
| Last Reviewed | 2026-06-19                                 |

**Description:** This file is the intended resolution target for GOV-001
in `Admin/Governance_Charter.md`. GOV-001 status needed updating.

**Resolution:** GOV-001 status updated to In Progress in
`Admin/Governance_Charter.md` v0.7 (2026-06-16) — GMP exists as executing
resolution path but has not been audited against charter constraints. Full
resolution pending GMP reaching Provisional Specification maturity.
Unknowns.md v3.4 reflects corrected status.

---

### GMP-002 — Canonical Governance Ownership transfer not yet recorded in Charter

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Low                                        |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-05                                 |
| Last Reviewed | 2026-06-19                                 |

**Description:** The Charter's Canonical Governance Ownership table
lists governance migration doctrine as owned by this file (updated in
Governance_Charter.md v0.7), but the ownership transfer is not yet
formally operative — this file must reach Gate 4 clearance
(Provisional Specification maturity) before the transfer is complete.

**Why It Matters:** Premature ownership transfer creates authority void
during this file's Exploration phase. The dual-truth-state (transfer
declared complete while not yet recorded / ratified) has been resolved
by scoping transfer as proposed and pending.

**Resolution Path:** On next audit pass of `Admin/Governance_Charter.md`
after this file reaches Provisional Specification, confirm ownership
transfer in Canonical Governance Ownership table. Until then, Charter
remains the higher-tier authority fallback.

---

### GMP-003 — Adversarial review at v0 single-contributor context underspecified

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Medium                                     |
| Priority      | Major                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-05                                 |
| Last Reviewed | 2026-06-05                                 |

**Description:** Section III Phase 2 notes that at v0, adversarial
review may be conducted by a different AI agent class or by the human
operator using the adversarial mandate explicitly. This is a bootstrap
proxy, not a robust solution. The adequacy of single-contributor
adversarial review for a Tier 1 amendment has not been validated.

**Why It Matters:** Adversarial review conducted by the same human
who assembled the proposal, even under an adversarial framing, is
structurally weaker than independent review. A compelling amendment
argument may be harder to challenge from the inside.

**Resolution Path:** Acceptable at Exploration stage — the constraint
that review must be documented prevents purely implicit self-review.
At Draft or above, define minimum adversarial review independence
requirements. Cross-reference GOV-008 (quorum definition) —
multi-agent quorum resolves this structurally.

---

### GMP-004 — Ratification authentication gap mirrors GOV-006

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | High                                       |
| Priority      | Major                                      |
| Type          | Security / Governance                      |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-05                                 |
| Last Reviewed | 2026-06-05                                 |

**Description:** Section III Phase 3 notes the authentication gap for
ratification records — until `Admin/Security_Protocols.md` reaches
Provisional Specification, ratification relies on interim authentication
requirements from the Charter. The interim requirement (second human,
external signature, or external dated record) is a placeholder, not a
solution. Interim requirements are declarative-only — no automated
enforcement exists at current maturity.

**Why It Matters:** A ratification record that cannot be authenticated
is a paper guarantee. Any system capable of fabricating plausible
human-sounding text could fabricate a ratification record. This is
the highest-risk attack vector against the Tier 1 amendment process.

**Resolution Path:** Mirrors GOV-006 resolution path — `Admin/Security_Protocols.md`
cryptographic authentication is the target. Until then, the interim
requirement is the operative constraint. Cross-reference SEC-007
(external root-of-trust architecture) — ratification authentication
is one of the primary use cases for that architecture.

**Precedent note (added 2026-07-25):** This is not a cold start —
`Admin/Repository_Integrity_Protocol.md` RIP-001's resolution already
established GPG-signed Git release tags (key `B5690EEEBB952194`) as
the repository's archival mechanism. Extending the same signing key
and workflow to ratification records, rather than proposing a
separate mechanism, is the lower-friction path when
`Admin/Security_Protocols.md` implementation begins — logged here as
a lead for that work, not a resolution of this unknown. Heavier
infrastructure (hardware security modules, multi-approver quorum
policy, blockchain anchoring) was considered and set aside as
disproportionate to a single-contributor v0 project — consistent with
this repository's existing rejection of cryptographic enforcement
before its time (see Abandoned Paths, `Admin/Repository_Integrity_Protocol.md`).
Full design remains owned by `Admin/Security_Protocols.md`, not this file.

---

### GMP-005 — Track A / Track B boundary at Tier 2 documents insufficient for interpretive capture

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Resolved — Discharge via Specification     |
| Risk          | High                                       |
| Priority      | Major                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-05                                 |
| Last Reviewed | 2026-07-17                                 |

**Description:** The original Track A / Track B boundary only addressed
text changes to Tier 1 Axioms. A change to a Tier 2 document
(`Admin/Auditor_Protocols.md`) that effectively reinterprets a Tier 1
Axiom without touching its text could be misclassified as Track A.
Constitutional Capture can operate through reinterpretation of
enforcement bounds rather than text amendment.

**Why It Matters:** A procedure that only catches text changes to Tier 1
Axioms is incomplete. Track A changes that alter how Tier 1 Axioms are
applied — even without modifying axiom text — must be captured.

**Resolution path partially executed (v0.2):** Track identification
rule updated to explicitly include Tier 2 document changes that redefine
Tier 1 Axiom application or introduce new exceptions. Track A authority
clause now requires explicit confirmation that no Tier 1 enforcement
bounds are altered. Status moved to In Progress. Full resolution requires
adversarial review of the expanded rule before promoting to Specification.

**Resolved (v0.3, 2026-07-17, human-directed):** generalized bidirectionally
and merged with GMP-009, which named the missing other half of this same
gap — non-Axiom content added *within* `Admin/Governance_Charter.md`
itself had no classification either, since the original Track A was
scoped to "documents below Tier 1" and couldn't reach it. Both gaps were
one gap: the axis classified by document location instead of
constitutional impact. Track A and Track B, above, are now defined by
impact — Axiom text, enforcement bounds, interpretation, exceptions — not
by which file the change sits in, with a Constitutional Impact Statement
checklist making the classification auditable rather than subjective.

Adversarial review (this pass, informal — Classes 4/6/9 per the review
that proposed this fix, not a full Battery): (1) Semantic Drift — tested
whether "impact-based" quietly loosens anything the old text-based rule
caught: it doesn't — every case the old rule classified Track B still
checks a box under the new rule, since the boxes are a superset of "touches
Axiom text." (2) Recursive Justification Loop — this rewrite classifies
itself: `Admin/Governance_Migration_Protocol.md` is a Tier 2 document, and
the rewrite changes the migration *process*, not what any Axiom requires
— checks "None of the above," Track A, consistent with EF-0.5 (no
document exempt from its own rules, including this one). (3) Epistemic
Corruption — checked whether "adds a new obligation" could be gamed to
smuggle a loosening through as Track A; addressed directly in the new
"adding a new obligation is not automatically a constitutional exception"
paragraph above, which draws the replace/supersede line explicitly rather
than leaving it to the drafter's framing.

Tested against two live cases: EDL (`Admin/Governance_Charter.md`) and
GOV-013 both check "None of the above" — neither alters Axiom text,
enforcement bounds, interpretation, or introduces an exception; both
formally Track A as of this resolution. See both entries for the applied
classification.

Status: Resolved — Discharge via Specification.

---

### GMP-006 — Concurrent amendment handling undefined

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Medium                                     |
| Priority      | Major                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-19                                 |
| Last Reviewed | 2026-06-19                                 |

**Description:** No doctrine exists for handling multiple simultaneous
Track B proposals. Questions unanswered: can multiple amendments be
active concurrently? Can they be merged? Must they serialize? Can a
pending amendment block a new proposal from entering Phase 1?

**Why It Matters:** Without serialization doctrine, two concurrent
amendments could interact in ways neither individually triggers Track B
classification for — combined effect may alter Tier 1 scope even if
each change individually appears minor. At low v0 amendment frequency
this is theoretical; at higher operational tempo it becomes a real gap.

**Resolution Path:** Define amendment state machine at Draft or above.
Minimum doctrine: concurrent Track B proposals must serialize; no new
proposal may enter Phase 2 while another is in Phase 3. Cross-reference
GMP-008 (expiration) — serialization requires a mechanism for proposals
that stall.

**Consolidation note (added 2026-07-25):** GMP-006, GMP-007, and GMP-008
are three faces of the same missing component — a formal Track B
amendment state machine (states: Draft → Phase 1 → Phase 2 → Phase 3 →
Recorded, with Withdrawn/Expired/Rejected/Returned/Superseded
transitions). Flagged here as the shared resolution target for all
three; not designed in this pass — that's real design work belonging
to whichever of the three is picked up first, not a documentation fix.

---

### GMP-007 — Amendment withdrawal procedure undefined

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Low                                        |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-19                                 |
| Last Reviewed | 2026-06-19                                 |

**Description:** Current Track B states are: ratify, reject, or return
to Phase 1. No explicit "withdraw" or "abandon" state exists for a
proposal that the engineer or human governing party wishes to terminate
before reaching Phase 3.

**Why It Matters:** Without a withdrawal procedure, abandoned proposals
linger in an ambiguous state — neither progressing nor formally closed.
This creates noise in the unknowns tracking and may conflict with GMP-006
serialization if introduced.

**Resolution Path:** Add withdrawal state to Track B state machine when
GMP-006 is resolved. Withdrawal requires a logged rationale and must
move the proposal to Abandoned Paths. A withdrawn proposal may be
reopened only by restarting Phase 1 from scratch — no partial resumption.
See GMP-006's consolidation note — this and GMP-008 resolve together
with it, not separately.

---

### GMP-008 — Stale proposal expiration policy undefined

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Low                                        |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-06-19                                 |
| Last Reviewed | 2026-06-19                                 |

**Description:** No expiration rule exists for proposals that stall
in Phase 1 or Phase 2. A proposal could theoretically persist indefinitely,
accumulating stale context while blocking serialization (GMP-006).

**Why It Matters:** Future governance cadence is unknown — the appropriate
expiration window depends on audit frequency and operational tempo. At
v0 with very low amendment frequency, this is low risk; at higher tempo
it could become a governance friction point.

**Resolution Path:** Defer to when governance cadence is established
(Trajectories.md v1 milestone). Suggested default when defined: proposals
not advanced within three full audit cycles expire automatically and must
restart Phase 1. Cross-reference GMP-006 (serialization) and GMP-007
(withdrawal) — all three form the amendment lifecycle state machine.

---

### GMP-009 — Track classification undefined for non-Axiom content changes to the Tier 1 file itself

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Resolved — Discharge via Specification     |
| Risk          | Medium                                     |
| Priority      | Major                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-07-03                                 |
| Last Reviewed | 2026-07-17                                 |

**Description:** The Track identification rule classifies migrations by
whether they touch Tier 1 *Axiom* text, scope, or interpretation. It does
not address a distinct case: a new section added to `Admin/Governance_Charter.md`
itself that is not an Axiom and does not touch Axiom enforcement — procedural
or epistemic content sharing the file with, but not part of, the Protections
and Prohibitions Clauses. Track A's own scope description ("all governance
documents below Tier 1") does not cleanly include this case, since the
target file is Tier 1 by location even though the content is not.

**Why It Matters:** Surfaced by a real proposed amendment (External Design
Lineage Governance, drafted 2026-07-03) that needed classification with no
clean answer in the existing rule. "When in doubt, treat as Track B" is
the stated default, but applying full Track B process (Friction Log,
adversarial Constitutional Capture review, human ratification record) to
non-Axiom procedural content is disproportionate and would likely deter
exactly the kind of housekeeping addition Governance_Charter.md already
contains elsewhere (e.g., the Canonical Verification Gates section).

**Resolved (2026-07-17, human-directed):** not via a third classification
or a Track A sub-case as originally framed here — via recognizing this was
never a separate gap from GMP-005. GMP-005 already established
impact-over-location classification for the downward case (Tier 2 documents
reinterpreting Tier 1). This entry named the missing upward/lateral case
(non-Axiom content within the Tier 1 file itself). Both are the same
principle applied in different directions. GMP-005's resolution generalizes
the rule to be direction-agnostic — see Track A / Track B, above, and
GMP-005's own Resolution field for the adversarial review this pass
included. EDL and GOV-013, both cited below as worked examples, are now
formally classified Track A under the generalized rule.

**Second worked example, 2026-07-16:** `Admin/Governance_Charter.md` GOV-013
(Post-Exit Monitoring Doctrine, Pathway 2/3) is a live second case in the
same unresolved state as EDL — new constitutional content, no Axiom text
touched. Drafted and treated per this entry's own proposed interim minimum
(enforcement-bound confirmation present in that section; human review
recommended, not yet obtained) rather than waiting on this entry's formal
resolution. Both cases resolved to Track A as of this pass — see their
own entries for the classification applied.

---

### GMP-010 — No evidence-sufficiency gate exists between "directed approach" and downstream reliance

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | High                                       |
| Priority      | Major                                      |
| Type          | Governance / Epistemic                     |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-07-19                                 |
| Last Reviewed | 2026-07-19                                 |

**Description:** This repository has no defined gate between a human-directed
approach being logged (e.g., `Architecture/Chemistry.md` CE-006's 2026-07-17
directed approach) and other files treating that approach as settled enough
to build on. `Challenges/Closed_Loop_Feedstock.md`'s CLF-004 referenced
CE-006's directed approach as the basis for continuing work before the
underlying mechanism was ever independently verified — and the mechanism
turned out to be wrong (Stage E's KMnO₄ bed does not capture Cl₂; corrected
2026-07-19, see CE-006/CE-007 and `Unknowns_Changelog.md` v4.25). Nothing in
this repository's process would have caught that automatically; it was found
by chance, two days later, via an external model's flag and a manufacturer
datasheet lookup — not by any structural check this repository runs on
itself.

**Why It Matters:** A "directed approach" is explicitly not the same
epistemic weight as ratified, verified doctrine — this repository already
distinguishes those states in principle. But nothing currently prevents a
directed approach from being *treated* as load-bearing by downstream files
before it earns that weight. This is the general failure mode: acceptance
happening because a claim was asserted with authority and went
uncontradicted, not because it was verified. Silence is not confirmation.

**Resolution Path:** Define a lightweight evidence-sufficiency gate for
directed approaches specifically — not full Track A/B ratification process,
which would be disproportionate for a working design decision, but a
minimum bar before other files may cite one as settled: (1) the approach's
core factual/mechanistic claims should be checked against at least one
primary source before downstream files build on it, not just before it's
formally ratified; (2) a directed approach's cross-references in other
files should note its provisional status explicitly (as CE-006's directed
approach note already did — "a directional decision, not a completed
one" — which is why this was recoverable rather than silently wrong
forever) rather than reading as settled fact; (3) consider whether
`Automation/AUDIT_HARNESS.py` could flag cross-references into any file whose
own Status is not yet Verified/Resolved, as a mechanical nudge rather than
relying on someone happening to check.

**Adversarial hardening addendum, 2026-07-19 (human-directed):** the above
resolution path addresses honest error — a directed approach that turns out
wrong despite good-faith effort. A deliberately subversive false claim
exploits the identical structural gap and requires the same fix plus three
specific additions, since "check one primary source" alone is insufficient
against an adversary who can plant or compromise a single source:

1. **Source diversity, not just source primacy.** Extend point (1) above:
   a directed approach's core claims should be checked against more than
   one independent primary source before being treated as settled,
   mirroring the evidence-diversity-over-raw-confidence principle already
   adopted in `Admin/Autonomy_Divergence_Protocol.md` §4 for detection —
   the same logic applies to sourcing generally, not only to subsystem
   monitoring. A single compromised or fabricated source defeats "check a
   primary source" but not "check several independent ones."
2. **No existing doctrine distinguishes wrong-by-accident from
   wrong-by-design.** `Admin/Autonomy_Divergence_Protocol.md` §5 splits
   Capability Anomaly from Governance Concern for *internal* subsystem
   behavior; nothing analogous exists for *external* input — a claim, a
   source, or an AI collaborator's output that is wrong in a way that
   specifically benefits some party, versus wrong through ordinary error.
   Not resolved here — flagged as a genuine, currently-uncovered category,
   candidate for its own future unknown if it recurs rather than solved
   speculatively now.
3. **The multi-agent cross-verification habit that has caught every real
   error this repository has found (CE-006, PC-005, PC-006, UNK-008's
   ownership contradiction) is currently a personal practice, not
   enforced doctrine.** It works because it is done consistently, not
   because anything requires it. Point (3) above — a harness flag on
   cross-references into non-Verified files — is the concrete first step
   toward converting that habit into something the repository enforces
   structurally, so the check still happens on a day no one thinks to do
   it by hand.

*Surfaced during a cross-repo epistemic-logic discussion (human-directed),
grounded in the CE-006 case as a real, not hypothetical, instance of the
failure mode. Logged rather than left as conversational insight, per human
governing authority's direction that this is worth tracking formally.*

---

### GMP-011 — Track classification dispute resolution undefined

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Medium                                     |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-07-25                                 |
| Last Reviewed | 2026-07-25                                 |

**Description:** GMP-005/GMP-009's constitutional-impact model defines
*how* a change should be classified Track A vs. Track B, and "when in
doubt, Track B" covers genuine uncertainty at classification time. It
does not cover disagreement after a classification has already been
made — if an engineer classifies a change Track A and an auditor
disagrees, no procedure exists for resolving that dispute.

**Why It Matters:** At v0 single-contributor scale this is low-probability
but not zero — multi-agent audit passes already disagree with each other
routinely on other questions (see this file's own GMP-005 resolution,
which took two review rounds to converge). A misclassification dispute
that has no defined resolution path could stall indefinitely or get
settled by whoever argues longest, neither of which is the intended
constitutional discipline.

**Resolution Path:** Deferred via Specification. Minimum candidate:
disputed classifications default to Track B for the duration of the
dispute (consistent with the existing "when in doubt" default), with
resolution requiring human governing authority confirmation of the
correct track before the proposal may proceed under either track's
procedure. Not designed further here — flagged as a real gap, not
solved speculatively.

*Surfaced via external audit review (ChatGPT), checked against this
file's actual Track identification rule and "when in doubt" doctrine
before registration — confirmed the dispute-after-classification case
is genuinely uncovered, not already handled by existing language;
registered by Claude — Synthesizer/Auditor, human-directed, 2026-07-25.*

---

### GMP-012 — No rollback or repeal doctrine for a ratified Track B amendment

| Field         | Value                                      |
|---------------|--------------------------------------------|
| Status        | Open                                       |
| Risk          | Medium                                     |
| Priority      | Minor                                      |
| Type          | Governance                                 |
| Blocking      | No                                         |
| Owner         | `Admin/Governance_Migration_Protocol.md`   |
| First Logged  | 2026-07-25                                 |
| Last Reviewed | 2026-07-25                                 |

**Description:** Track B's Phase 1–4 procedure defines how a Tier 1
Axiom amendment gets ratified. Nothing defines what happens if a
ratified amendment later proves harmful — is reversal a fresh Track B
amendment reversing the text, a restoration from the pre-amendment
archived state, or does it require a distinct emergency procedure?

**Why It Matters:** Without this, a bad ratification has no defined
exit other than treating repeal as a brand-new amendment through the
full Phase 1–4 cycle — which may be the right answer, but that has
never been stated, so an actual future repeal would be improvising
under pressure rather than following a settled procedure.

**Resolution Path:** Deferred via Specification. Minimum candidate:
repeal is itself a Track B amendment (same Phase 1–4 procedure,
same human ratification requirement) — no separate emergency track,
since an emergency-repeal shortcut would itself be a smaller-scale
version of the same capture risk Track B exists to prevent. Restoration
of pre-amendment text vs. drafting new replacement text is a case-by-case
Phase 1 judgment, not something to pre-specify. Not designed further
here.

*Surfaced via external audit review (ChatGPT), checked against Section
III's actual Phase 1–4 text before registration — confirmed no rollback
path exists anywhere in the current procedure; registered by
Claude — Synthesizer/Auditor, human-directed, 2026-07-25.*

---

### Resolution Log

- 2026-07-25: **v0.4 — External audit review triaged (ChatGPT, Grok);
  maintenance fixes and two new unknowns registered (human-directed).**
  Four externally-authored review passes checked against this file's
  actual current text before anything was adopted. Confirmed real and
  fixed: GMP-003's Last Reviewed date preceded its First Logged date
  (typo); Open Unknowns header claimed 8 but the sidecar table actually
  contained 7 Open entries (GMP-001/005/009 are Resolved) — the
  2026-07-19 log entry's own "7 → 8" arithmetic didn't match the table
  it described; Lessons Learned had sat empty since file creation
  despite substantial resolvable history in this Resolution Log;
  Status section was frozen at "Version 0.3" despite GMP-005/009's
  resolution and GMP-010's registration both landing after that entry.
  Two new unknowns registered after checking each was genuinely
  uncovered by existing doctrine: **GMP-011** (classification dispute
  resolution — "when in doubt, Track B" covers uncertainty, not
  disagreement after classification) and **GMP-012** (no rollback/repeal
  doctrine for a ratified amendment that later proves harmful).
  GMP-006/007/008 gained a shared consolidation note pointing at a
  future amendment state machine — flagged, not designed, in this pass.
  GMP-004 gained a cross-reference to existing GPG signing precedent
  already established via `Admin/Repository_Integrity_Protocol.md`
  RIP-001, as a lower-friction lead for `Admin/Security_Protocols.md`'s
  eventual implementation. A separate proposal recommending hardware
  security modules, multi-approver quorum policy, and blockchain
  anchoring was reviewed and explicitly not adopted — assessed as
  disproportionate to a single-contributor v0 project and inconsistent
  with this repository's existing rejection of premature cryptographic
  enforcement (`Admin/Repository_Integrity_Protocol.md` Abandoned Paths).
  Open Unknowns 7 → 9 (corrected baseline, then GMP-011 and GMP-012 added).

- 2026-07-17: **GMP-005 and GMP-009 resolved together; Track A/B
  redefined by constitutional impact, not document location.** Multi-agent
  review (two rounds — a "third track" proposal, then a redefinition
  proposal identifying GMP-005 as already-established precedent) converged
  on: don't add a Track C, generalize the existing rule. Track A and Track
  B, above, now classify by whether a change touches Tier 1 Axiom text,
  enforcement bounds, interpretation, or exceptions — regardless of which
  file — replacing the prior location-based split ("Tiers 2-5" vs. "the
  eight Axioms in Governance_Charter.md") that had no room for non-Axiom
  content added to the Tier 1 file itself. Constitutional Impact Statement
  checklist added to make classification auditable. "When in doubt, Track
  B" and "misclassification is a Constitutional violation" carried forward
  explicitly onto the new axis, not dropped in the rewrite. New paragraph
  distinguishes obligations that add scrutiny (Track A) from changes that
  replace or supersede an enforcement mechanism (Track B), closing a gaming
  vector the review process itself flagged. Adversarial review this pass
  (informal — Semantic Drift, Recursive Justification Loop, Epistemic
  Corruption) documented in GMP-005's entry, including the rule
  classifying its own amendment as Track A. EDL and GOV-013
  (`Admin/Governance_Charter.md`) both formally classified Track A —
  see their entries. GMP-002 (migration doctrine ownership transfer,
  still Open) may be affected by this rewrite; not reviewed this pass.
  Open Unknowns 9 → 7.

- 2026-07-19: **GMP-010 adversarial hardening addendum.** Extended to cover
  deliberate subversion, not just honest error, at human governing
  authority's direction. Three additions: source diversity (not just
  primacy) required for directed-approach claims, mirroring
  `Admin/Autonomy_Divergence_Protocol.md` §4's evidence-diversity
  principle applied to sourcing generally; flagged the absence of any
  wrong-by-accident vs. wrong-by-design classification for external
  input (no action taken — genuinely new category, not solved
  speculatively); named the repository's multi-agent cross-verification
  practice as currently personal habit, not enforced doctrine, and
  pointed at the harness cross-reference flag (already in GMP-010's
  original resolution path) as the concrete first step toward making it
  structural.

- 2026-07-19: **GMP-010 registered.** No evidence-sufficiency gate exists
  between a directed approach being logged and other files treating it as
  settled. Grounded in a real case, not a hypothetical: CE-006's 2026-07-17
  directed approach was cited by CLF-004 as basis for continued work before
  independent verification — the underlying mechanism was wrong, caught by
  chance two days later, not by any structural check. Surfaced during a
  cross-repo epistemic-logic discussion (human-directed). Open Unknowns
  7 → 8.

- 2026-07-16: **GMP-009 cross-referenced to GOV-013.** While drafting
  `Admin/Governance_Charter.md` GOV-013 (Post-Exit Monitoring Doctrine,
  Pathway 2/3), determined it doesn't cleanly fit Track A or Track B —
  it's GMP-009's already-open gap (non-Axiom content added to a Tier 1
  file), not a fresh classification question. Added GOV-013 as a second
  worked example alongside EDL in GMP-009's entry; GMP-009 itself not
  resolved here, left for its own review. Separately: this file's own
  File State Last Audit header was stale against its own body content
  (GMP-005/GMP-009 both dated later than the header) — flagged in the
  header rather than fully re-dated, since establishing the file's true
  last-touch history is a separate task not attempted this pass.

- 2026-06-05: File created (v0.1) — GOV-001 resolution path initiated.
  Two-track migration architecture established. Phase 1–4 Track B procedure
  defined. Hard floor declared for Anti-Weaponization, Ethical Anchor, and
  humanitarian override closure. GMP-001 through GMP-005 logged. Honest v0
  acknowledgment of bootstrap limitations added.
- 2026-06-19: v0.2 — Three-agent audit pass (ChatGPT, Gemini, Grok) plus
  Claude synthesis. Eleven changes: (1) Navigation Anchors added.
  (2) Verification Ref confirmed — `Admin/Verification_Gates_LF.md` is
  correct; session-context false positive from agents working without full
  registry not applied. (3) Ownership transfer dual-truth-state resolved —
  "takes over ownership" replaced with "proposed to assume ownership pending
  Charter update and Gate 4 clearance." (4) Track identification rule
  expanded — now explicitly covers Tier 2/lower document changes that alter
  Tier 1 Axiom enforcement bounds, not only direct text changes. (5) Track A
  authority clause updated — requires explicit confirmation no Tier 1
  enforcement bounds altered. (6) Hard floor section clarified — extra-
  constitutional vs. axiom distinction noted. (7) Phase 3 authentication
  gap note updated — declarative-only status made explicit. (8) ASM-002
  and ASM-004 provenance labels added [Estimated / Internally Derived].
  (9) GMP-001 resolved — GOV-001 In Progress confirmed; Unknowns.md v3.4
  reflects status. (10) GMP-005 In Progress — partial execution via Track
  identification rule expansion; full resolution requires adversarial review
  of expanded rule. (11) GMP-006 logged — concurrent amendment handling
  undefined. (12) GMP-007 logged — amendment withdrawal procedure undefined.
  (13) GMP-008 logged — stale proposal expiration undefined. (14) Ownership
  transfer abandoned path added. (15) Drift Indicators expanded — six new
  entries. Open Unknowns updated to 8 (GMP-001 resolved, GMP-006/007/008
  added).
- 2026-07-03: v0.3 — GMP-009 logged. Surfaced by a real proposed amendment
  (External Design Lineage Governance, drafted in `Admin/Governance_Charter.md`,
  not yet ratified) that the existing Track identification rule could not
  cleanly classify: non-Axiom content added to the Tier 1 file itself.
  Provisional classification applied to the EDL case pending this unknown's
  resolution: treated as Track A with Track A's existing Tier-2 discipline
  (explicit no-enforcement-bound-altered confirmation, human review before
  commit) rather than full Track B. Open Unknowns updated to 9.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; Governance
  Migration Doctrine section declares the constraints this file executes;
  ownership transfer of migration doctrine is proposed to this file pending
  Gate 4 clearance and Charter table update (GMP-002)
- `Admin/Repository_Integrity_Protocol.md` — prior state preservation
  (Step 1 of both tracks) is defined there; this file references that
  protocol and depends on it being operational
- `Admin/Auditor_Protocols.md` — Tier 2; auditor operational behavior
  during migration review is defined there; Track A engineer-plus-auditor
  authority references this file
- `Admin/Engineer_Protocols.md` — engineer role in Phase 1 proposal
  assembly is defined there; ASM-003 dependency
- `Admin/Ethical_Constraints.md` — co-Tier 1; Anti-Weaponization Doctrine
  is declared outside amendment scope in the Hard Floor section; Ethical
  Anchor string is similarly immutable
- `Admin/Security_Protocols.md` — exists at v0.5 (2026-06-19); Phase 3
  ratification authentication depends on this file reaching Provisional
  Specification; GMP-004 tracks this dependency; SEC-007 is the deepest
  blocker
- `Admin/Forge_Audit_Kit.md` — Tier 3; Verification Maturity Model
  referenced for Gate 4 clearance threshold; GMP- prefix in Sidecar ID
  Reference
- `Unknowns.md` — GMP-001 through GMP-008 indexed there; cross-module
  impact of Track B amendments to be logged there
- `Discovery.md` — downstream notification tracking during migrations;
  canonical cross-reference resolution source

---

## Status

Version 0.4 — External audit review triaged (ChatGPT, Grok): GMP-003
date typo fixed; Open Unknowns count corrected from a stale 8 to the
actual 7 open entries plus two newly registered (GMP-011, GMP-012),
now 9; Lessons Learned populated from existing Resolution Log history
(was empty since file creation); GMP-004 gained a cross-reference to
existing GPG signing precedent (`Admin/Repository_Integrity_Protocol.md`
RIP-001) rather than adopting proposed HSM/blockchain infrastructure,
assessed as disproportionate at v0 scale; GMP-006/007/008 gained a
shared consolidation note pointing at a future amendment state machine,
not designed in this pass (2026-07-25).

Version 0.3 — GMP-009 logged: track classification gap for non-Axiom
content changes to the Tier 1 file (2026-07-03). *(This entry
previously sat as the most recent Status entry despite GMP-005/GMP-009's
resolution and GMP-010's registration both landing afterward — corrected
2026-07-25, no substantive content changed by the correction itself.)*

**What must remain constant:**

**The procedure must exist before the argument arises.**
**Constitutional Capture is guarded against by both text and interpretation.**
