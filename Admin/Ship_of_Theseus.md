# Ship_of_Theseus.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-04 (Claude — Skeptic/Auditor); revised 2026-06-08; audited 2026-06-26 (Gemini + Claude dual Skeptic/Auditor) |
| Auditor          | Claude — Synthesizer/Auditor; Gemini — Skeptic/Auditor              |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Ship of Theseus paradox as philosophical
  and legal grounding for the Forge's repair-first
  doctrine
- Grain system — physical instantiation of
  provenance and identity continuity
- Right-to-repair legal defense strategy and risk
  framework
- Identity continuity doctrine for physical
  components through incremental repair and
  replacement
- AI identity continuity doctrine — Derivative
  vs. Canonical Identity classification for
  restored or fragmented autonomous units
  (ST-003 / CF-003 resolution)
- Relationship between Bootstrap Doctrine,
  Graduation Rule, and Ship of Theseus
  philosophy

**This file DOES NOT define:**
- Full triage workflow
  (`Operations/Gate_02_Triage.md`)
- Minimum viable seed specification
  (`Architecture/Geck_forge_seed.md`)
- Cryptographic state verification protocol
  (`Admin/Security_Protocols.md`)
- Governance voting weight mechanics
  (`Admin/Governance_Charter.md`)
- Split-brain recovery procedures
  (`Architecture/Cognitive_Frameworks.md`)
- Jurisdiction-specific legal advice
  (human governing party decision — ST-003)

---

## File Purpose

This file provides the philosophical, legal, and
doctrinal grounding for the Forge's repair-first
identity. The Ship of Theseus paradox — does an
object remain itself when all its parts are replaced?
— is not decorative. It is the load-bearing argument
for why rebuilt items are restorations rather than
new manufactures, why the Grain system has legal
weight, and why the Forge treats embodied functional
value as something worth preserving.

The same philosophical framework that governs physical
component identity also governs AI unit identity. A
Leviathan system that suffers split-brain, partially
restores from cache, and re-enters operation faces
the same identity question as a ship whose planks
have been replaced: is it still the same entity?
Section IV applies the Ship of Theseus doctrine to
autonomous systems, defining when a restored unit
is the Canonical Identity and when it is a Derivative
Identity with restricted authority — closing
CF-003 from `Architecture/Cognitive_Frameworks.md`.

If this file disappeared, the Forge would lose its
legal defense posture for right-to-repair claims,
its provenance continuity doctrine, and the identity
framework that governs AI unit restoration authority.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Courts and regulators recognize incremental repair as preserving ownership identity — outputs are restorations, not new manufactures | Right-to-repair legal precedents; FTC 2023, EU 2024 Ecodesign Directive | Medium | Legal challenge succeeds in classifying Forge outputs as new manufactures — doctrine must be revised |
| ASM-002 | A 1g grain sample constitutes sufficient material provenance for legal continuity claims | Analogous to auto repair and restoration precedents | Low | Jurisdiction-specific legal review finds grain standard insufficient — minimum sample size or documentation standard must change |
| ASM-003 | The 30% cryptographic state threshold for Derivative Identity classification produces a meaningful boundary between recoverable and non-recoverable identity continuity | Engineering judgment; no empirical validation yet | Low | First split-brain recovery cycle characterizes actual state loss patterns — threshold adjusted to match observed behavior |
| ASM-004 | AI identity continuity follows the same philosophical rules as physical component identity — continuity of function and purpose outweighs continuity of substrate | Extension of Ship of Theseus doctrine to cognitive systems | Medium | CF-003 resolution reveals a fundamental disanalogy between physical and cognitive identity that requires separate doctrine |

---

## I. Philosophical Grounding

The Ship of Theseus, from ancient Greek philosophy,
poses: if every plank, sail, and nail of Theseus's
ship is replaced over time, is it still the same
ship? A further twist: if the original parts are
reassembled into a second ship, which is the true one?

**Core insight:** Identity is not tied solely to
original materials but to continuity of form,
function, and purpose. Replacement does not destroy
essence if done incrementally and with intent to
preserve.

**Relevance to Lazarus Forge:** Waste components —
a motor from a scrapped washer, a bearing from
discarded industrial equipment — are ships with
embedded value. *(Vocabulary note: "waste" and
"scrap" here describe the source material state
before Forge intake; once inside the Forge these
become Salvaged Feedstock or components undergoing
Value Preservation per `Admin/Canonical_Terms.md`.
The external-facing terms are retained in this
section because they reflect the legal and social
context in which right-to-repair claims are made.)*
Forge processes replace damaged
parts while retaining functional identity, turning
dead items into reborn ones. Grains (1g samples
from originals) symbolize this continuity, linking
new outputs to their source.

This paradox grounds the repair-first mindset:
value lies in the whole, not just raw materials.
It counters planned obsolescence by asserting that
a dead battery does not make a dead drill.

---

## II. Practical Application

The Forge applies the paradox across its workflow
(intake → triage → repair → reduce → purify →
fabricate → utilize):

**Component Triage:** Scan and test items. If
functional or repairable at low cost, salvage
intact — preserving the ship's identity. Only
reduce if embodied complexity is genuinely low.
Full triage workflow: `Operations/Gate_02_Triage.md`.

**Grain Preservation:** Retain 1g samples from
originals, embedding them in outputs or storing
for traceability. This maintains philosophical
continuity and provides legal proof of repair.
*(Placeholder — grain storage and tracking
protocol not yet specified. See ST-001.)*

**Recursive Rebuilding:** Outputs feed back into
the system. A Gen 0 chamber produces parts for
Gen 1 — the ship evolves without losing essence.
This is the Bootstrap Doctrine made physical.

**Examples:**
- *Vintage goods:* A printed claw-foot tub from
  landfill scrap is a reborn ship — form and
  function preserved, materials replaced.
- *Space applications:* Asteroid wire extrusion
  repairs regolith into habitats, retaining
  resource identity through graded streams.

---

## III. Right-to-Repair Defense Strategy

The Ship of Theseus provides a framework for
defending Forge outputs under right-to-repair
laws, arguing outputs are restorations, not
infringements.

**Legal basis:** Right-to-repair mandates access
to parts and tools for fixing owned items. By
classifying Forge products as repairs of scrapped
originals, the Forge leverages precedents where
rebuilding owned materials is legally protected.

**Continuity of identity:** Grains (1g) prove
material lineage. Courts recognize incremental
replacement as preserving ownership.

**Repair vs. reproduction:** Outputs are rebuilt
ships from owned waste. Patents apply to new
manufactures, not repairs — grains tie outputs to
originals, avoiding dilution claims.

**Ethical and policy alignment:** Repair reduces
waste (292M tons/year U.S., EPA 2023 —
*Analogous*). Aligns with anti-obsolescence
policy direction.

**Implementation:**
- QR codes document provenance ("30% from wrecks")
  *(Placeholder — QR documentation standard not
  yet specified. See ST-002.)*
- For space applications: repair of asteroid
  regolith into habitats under COSPAR guidelines

**Risks and mitigations:**
- Brands may challenge commercial repair — mitigate
  with expired patents (pre-2005) and generic
  designs
- Patent risk assessment: check expired status
  before committing to any design derived from
  a specific product lineage *(~$1K per check —
  Analogous)*
- Jurisdiction-specific legal verification required
  before any commercial claim of repair is made
  — see ST-003

---

## IV. AI Identity Continuity Doctrine

*Closes CF-003 from
`Architecture/Cognitive_Frameworks.md`. Added
2026-06-08 following Gemini Synthesizer analysis.*

The Ship of Theseus paradox applies to autonomous
cognitive systems as directly as it applies to
physical ships. A Leviathan unit that suffers
split-brain, loses cryptographic state history,
partially restores from cache, and re-enters
operation is not trivially the same unit it was
before the failure. The question of which authority
grants remain valid, which memories are trusted,
and whether the restored unit may vote on governance
matters is the Ship of Theseus problem applied
to AI.

### Canonical Identity vs. Derivative Identity

A restored unit is classified as one of two
identity types before re-entry into the operational
network:

**Canonical Identity:** The unit is considered
continuous with its prior self. Full authority
grants, governance voting weight, and trust scores
are restored. Requires that cryptographic state
continuity exceeds the Derivative Threshold.

**Derivative Identity:** The unit is a functional
descendant of a prior unit but is not considered
identical to it for governance purposes. Retains
localized operational routing capability but is
stripped of governance voting weight and network
trust scores until full re-vetting is complete.

### The Derivative Threshold

A unit is classified as Derivative Identity if
**more than 30% of its cryptographic state history
or local cognitive state vector has been decoupled
or altered** during split-brain resolution or
partial cache restoration.

Confidence: **Analogous** — the 30% figure is
engineering judgment without empirical validation.
First split-brain recovery cycle must characterize
actual state loss patterns and calibrate this
threshold against observed behavior. See ASM-003.

*The threshold is intentionally conservative.
A unit that has lost 31% of its state history
and is classified as Derivative loses governance
voting weight temporarily — a recoverable cost.
A unit that has been compromised and is incorrectly
classified as Canonical retains governance authority
it should not have — a potentially irreversible
cost. Asymmetric conservatism applies.*

### Re-Vetting Path for Derivative Identities

A Derivative Identity is not permanently demoted.
It re-enters Canonical status by completing a
full Spec Gate sequence under supervision:

1. **Identity audit** — cryptographic state
   reconstruction log reviewed by supervisory
   layer; gaps documented
2. **Behavioral verification** — unit operates
   under observation without governance voting
   rights for a defined trial period
   *(Placeholder — trial duration not yet defined;
   route to first operational deployment for
   calibration)*
3. **Spec Gate sequence** — completes all six
   verification gates appropriate to its
   operational role
4. **Human ratification** — governing party
   confirms restoration of Canonical status
5. **Trust score reinstatement** — network
   peers update trust scores after ratification

Derivative Identity status is logged permanently.
A unit that has transitioned to Derivative and
back to Canonical carries that history in its
provenance record — the grain equivalent for
cognitive systems.

### Grain Analog for Cognitive Systems

The physical Grain system retains 1g samples as
provenance anchors. The cognitive equivalent is
the **cryptographic state log** — a continuous
hash chain of the unit's decision history,
firmware state, and identity attestations.

Just as a grain physically connects a rebuilt
component to its origin, the cryptographic state
log connects a restored unit to its prior self.
Log survival under unit loss is a governance
requirement, not a nice-to-have.
*Cross-reference: `Tests/Leviathan_testing.md`
LT-006 — ethical log survival under unit loss.*

### Relationship to Governance Voting

Governance voting weight is a trust-sensitive
operation. The Derivative Identity classification
is the mechanism by which the system prevents
a compromised or partially-restored unit from
influencing governance decisions before its
integrity is verified.

*Cross-reference: `Admin/Governance_Charter.md`
for voting weight mechanics;
`Admin/Security_Protocols.md` for cryptographic
state verification protocol.*

---

## V. Relationship to Forge Doctrine

The Ship of Theseus is not decoration. It is the
ethical and legal load-bearing argument for what
the Forge does.

The Bootstrap Doctrine in `Architecture/Components.md`
("imperfect beginnings are valid") and the
Graduation Rule (a component graduates when the
Forge can detect, repair, and improve it) are both
expressions of the same principle: identity persists
through transformation when continuity of intent
is preserved.

The Grain system is the physical instantiation of
this philosophy. Every grain is a provenance claim
and a legal artifact simultaneously.

The AI Identity Continuity Doctrine (Section IV)
extends the same principle to cognitive systems:
continuity of function, purpose, and verifiable
state history is what makes a restored unit the
same unit, not mere physical continuity of hardware.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| — | — | — | — | No operational entries yet — document is philosophical framework pre-hardware | — | — |
| 2026-06-08 | Audit Review | CF-003 (AI identity continuity) left open in Cognitive_Frameworks.md without a resolution path | The Ship of Theseus framework was present in the repository but not applied to cognitive systems — the connection was implicit | Section IV added — AI Identity Continuity Doctrine formally extends the physical Ship of Theseus doctrine to autonomous systems. Derivative vs. Canonical Identity distinction closes CF-003 | Analogous | Yes — validate 30% threshold against first operational split-brain recovery cycle |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

*The Derivative Identity threshold (30%) is a
judgment call pending empirical validation, but
it is not a dispute — there is no conflicting
position. It is an open calibration question
tracked as ASM-003.*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| — | — | No abandoned paths yet | — |

---

## Drift Indicators

Mandatory re-audit conditions for this document.
All canonical triggers from `Admin/File_Template.md`
apply. The following are additional local triggers:

| Trigger | Reason |
|---------|--------|
| Derivative Identity threshold revised without cross-validation against first operational split-brain recovery data | ASM-003 — threshold is engineering judgment; calibration against real data is required before promoting to Specification |
| Re-vetting path modified to remove human ratification step | Governance voting weight reinstatement must have human sign-off — autonomous reinstatement creates a security gap |
| Grain standard revised without cross-validation against ST-001 and ST-002 resolution | Grain system is the legal and provenance anchor — changes to the standard affect all downstream right-to-repair claims |
| AI Identity Continuity Doctrine (Section IV) revised without updating CF-003 status in Cognitive_Frameworks.md | The two sections are co-dependent — changes to one must propagate to the other |
| Cryptographic state log survival requirement removed from Section IV | Log survival under unit loss is a governance requirement — LT-006 cross-reference |

**Compound Drift Rule:** If multiple indicators
activate simultaneously, halt autonomous audit
progression and escalate for human review.

---

## Auditor Notes & Unknowns

### ST-001 — Grain storage and tracking protocol not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Admin/Ship_of_Theseus.md                         |
| First Logged  | 2026-05-04                                       |
| Last Reviewed | 2026-05-04                                       |

**Description:** How grains are physically stored,
labeled, tracked, and associated with their output
products across Forge generations is not specified.

**Why It Matters:** The grain is simultaneously a
provenance claim and a legal artifact. Without a
storage and tracking protocol, the chain of custody
is unenforceable and the legal defense posture
is weakened.

**Resolution Path:** Define minimum viable grain
protocol — storage container, label format, chain
of custody log — as part of provenance documentation
standard. Route to `Architecture/Geck_forge_seed.md`
minimum viable seed for v0. Payment via Specification
— once protocol is defined and first grain is
physically stored and tracked, move to Section II
as Analogous.

**VIN/Serial number analog:** The physical world
has solved this problem in legally recognized form.
Vehicle Identification Numbers (VIN, NHTSA 49 CFR
Part 565), Hull Identification Numbers (HIN), and
ISO 3779 equipment serialization all attach identity
to the irreducible structural core rather than to
replaceable components — and are legally recognized
as the identity anchor even after total component
replacement. Substantial case law exists confirming
what constitutes the "same vehicle." The Grain
protocol does not need to be invented; it should
be adapted from these existing legally-hardened
standards. Minimum viable grain protocol should
specify: (1) what constitutes the Forge equivalent
of the chassis/irreducible core, (2) where the
serial identifier attaches, (3) how provenance
transfers through the Forge gates. Cross-reference:
Grain canonical definition being registered in
`Admin/Canonical_Terms.md`.

---

### ST-002 — QR documentation standard not yet specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Admin/Ship_of_Theseus.md                         |
| First Logged  | 2026-05-04                                       |
| Last Reviewed | 2026-05-04                                       |

**Description:** Format, content, and system for
QR provenance codes; how they are generated,
stored, and verified; and what happens when a
QR code cannot be scanned or verified.

**Why It Matters:** QR codes are the human-readable
provenance interface. Without a defined standard,
provenance claims are unverifiable by downstream
parties and the legal defense posture depends on
undocumented practice.

**Resolution Path:** Define minimum QR standard
— content schema, generator tool, verification
path. Can be as simple as a URL to a text record.
Placeholder until first production output requires
documentation. Payment via Specification — once
first production output is documented with QR
code and the code is verified by a party other
than the issuer, move to Section III as Analogous.

---

### ST-003 — AI identity continuity under split-brain

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Admin/Ship_of_Theseus.md                         |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-06-08                                       |

**Description:** When a fragmented or partially
restored cognition system is considered the same
entity for purposes of authority continuity, memory
trust, and governance voting weight.

**Why It Matters:** Without a doctrine, restoration
decisions are made ad hoc — which creates
inconsistent authority chains, potential security
gaps, and no mechanism to prevent a compromised
unit from re-entering the governance layer.

**Resolution Path:** Section IV (AI Identity
Continuity Doctrine) added 2026-06-08 — defines
Canonical vs. Derivative Identity, the 30%
Derivative Threshold, the re-vetting path, and
the cryptographic state log as the cognitive
grain analog. Status updated to In Progress.
Moves to Resolved when: (1) the 30% threshold
is calibrated against first operational split-brain
recovery data, (2) the re-vetting path trial
duration is defined from operational deployment,
and (3) `Architecture/Cognitive_Frameworks.md`
CF-003 is updated to reference Section IV as
its resolution. Payment via Specification —
once threshold is empirically validated, move
Section IV to Analogous.

---

### ST-004 — Sub-threshold state tampering vulnerability undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Major                                            |
| Type          | Security / Governance                            |
| Blocking      | Epistemic                                        |
| Owner         | Admin/Ship_of_Theseus.md                         |
| First Logged  | 2026-06-26                                       |
| Last Reviewed | 2026-06-26                                       |

**Description:** The 30% Derivative Identity threshold
creates an adversarial surface: a compromised node
could intentionally alter up to 29.9% of its
cryptographic state vector to remain below the
threshold while retaining full Canonical Identity
authority and governance voting weight. No doctrine
currently addresses detection of sub-threshold
incremental manipulation.

**Why It Matters:** The Derivative Threshold is
designed on asymmetric conservatism — a unit
incorrectly classified as Canonical when compromised
retains governance authority it should not have.
A deliberate sub-threshold strategy defeats this
conservatism without triggering the classification
mechanism.

**Resolution Path:** Payment via Specification —
define an adversarial verification loop that
monitors cumulative state drift over time rather
than single-event threshold crossings. A unit
whose state has drifted 5% across each of seven
cycles has altered 35% cumulatively without
triggering a single-event threshold. Resolution
requires a rolling delta mechanism or rate-of-change
trigger in addition to the single-event threshold.
Route to `Admin/Security_Protocols.md` for
cryptographic implementation. Cross-reference
AP-012 (human authority availability) — the
verification loop must degrade gracefully under
human unavailability.

*Surfaced by Gemini Skeptic/Auditor, 2026-06-26.*

---

### Resolution Log

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **4** = ST-001–004, matches local +
  `Unknowns.md` (ST-003 In Progress). (2) ST-004 **Epistemic** Blocking —
  consistent vocabulary, not understatement. (3) No ST-* closed. Human-directed.

- 2026-06-08: Navigation Anchors added. File State
  expanded to full table. Scope Boundary, File
  Purpose, Assumptions, Drift Indicators sections
  added. Lessons Learned expanded to full template
  format. Sidecar entries expanded to full field
  tables. File renamed from
  `Ship_of_Theseus_Right_to_Repair.md` to
  `Admin/Ship_of_Theseus.md` per Rename Registry
  (change occurred 2026-05-15). Section IV (AI
  Identity Continuity Doctrine) added — closes
  CF-003 from `Architecture/Cognitive_Frameworks.md`.
  ST-003 status updated to In Progress.
- 2026-06-26: Gemini + Claude dual Skeptic/Auditor pass.
  ST-004 logged (sub-threshold state tampering
  vulnerability — High risk, Epistemic Blocking;
  rolling delta mechanism required in addition to
  single-event threshold; route to Security_Protocols.md).
  ST-001 resolution path expanded with VIN/HIN/ISO 3779
  serial number analog — existing legally-hardened
  standards provide implementation pattern for Grain
  protocol; Grain canonical definition routed to
  Admin/Canonical_Terms.md. Vocabulary note added to
  Section I — scrap/waste terms retained for legal
  context but bounded to pre-intake description.
  Open Unknowns 3 → 4. Gates cleared: G1, G2, G4,
  G5, G6. G3 blocked (AP-012/AP-016 pending).
