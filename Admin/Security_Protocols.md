# Security_Protocols.md — Cryptographic Trust & Multi-Agent Node Security

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Physical security and digital authority are tightly coupled within the Forge.
> A compromise of cryptographic key material or human override tokens can bypass
> downstream safeguards, enabling malicious rewriting of operational files or
> unauthorized activation of high-energy machinery. Key infrastructure must be
> decoupled from standard runtime environments. Never store root cryptographic
> seed material in a standard agent-accessible workspace or online repository node.
> When in doubt about key material integrity, treat the affected authority chain
> as compromised and escalate to human review before proceeding.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | `Admin/Verification_Gates.md`                                    |
| Last Audit       | 2026-09-03 — Grok surgical state-synchronization repair after ChatGPT REVISE/G6-BLOCKED audit (SEC-AUD-001–006): FROZEN markers added; Scope Boundary SEC-009 updated; Human-Factors note synchronized; PAT-001/PAT-002 statuses updated; RIP-001 dependency language corrected; bottom Version 0.8 Status block replaced with current + historical record. No security architecture redesigned; SEC-002/007a/009 closures preserved. Prior: 2026-08-22 |
| Auditor          | Grok — 2026-09-03 integrity repair (see Last Audit). Prior: Gemini / Grok / ChatGPT / Claude multi-agent history retained in Resolution Log |
| Open Unknowns    | 10 substantively open (SEC-001, SEC-003, SEC-004, SEC-005, SEC-006, SEC-007b, SEC-008, SEC-010, SEC-011, SEC-012). SEC-002, SEC-007a, SEC-009 Ratified — Payment via Specification, 2026-08-22 |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cryptographic mechanisms for multi-signature Human Override Verification
- Automated code-signing protocols for file integrity verification (RIP Phase 3)
- Node identity verification and key rotation cycles within the cluster environment
- Minimum token complexity, air-gapping requirements, and cryptographic fallback
  behaviors during network division
- Trust boundary declaration: the relationship between cryptographic enforcement
  and governance legitimacy
- Incident logging requirements for authentication events including replay
  protection requirements
- Degraded-operation security doctrine notes
- Compromise detection doctrine (SEC-009 — Ratified, Payment via Specification, 2026-08-22)

**This file DOES NOT define:**
- Component-level infiltration prevention for salvaged hardware — governed by
  `Operations/Electronics.md`; this file references that doctrine and sits above
  it in the administrative authority layer
- Specific operating system firewall commands or network router firmware rules
- Local facility access control (locks, badges, physical perimeter barriers)
- Constitutional governance doctrine — governed by `Admin/Governance_Charter.md`
- Auditor operational behavior — governed by `Admin/Auditor_Protocols.md`
- Minimum agent quorum definition for bootstrap compliance — governed by
  GOV-008 in `Admin/Governance_Charter.md`; quorum threshold is a prerequisite
  input to the multi-signature requirements defined here
- Trusted initialization environment definition — see SEC-005 and
  `Admin/Canonical_Terms.md` CT-004
- Human-factors attack surface (social engineering, operator coercion) — pending
  cross-reference to `Admin/Safety_Protocols.md` and `Admin/Ethical_Constraints.md` EC-011
- Long-duration cryptographic continuity (algorithm migration, entropy
  exhaustion across decades) — pending SEC-011

---

## File Purpose

This document establishes the technical security implementation rules for
validating administrative authority, ensuring the integrity of the active
knowledge graph, and managing multi-node validation in untrusted, degraded,
or adversarial deployment environments. It bridges the gap between the
constitutional governance declarations in `Admin/Governance_Charter.md` and
the operational integrity procedures in `Admin/Repository_Integrity_Protocol.md`
by defining the cryptographic enforcement layer that makes integrity protections
mechanically verifiable rather than procedurally dependent.

This file is the Phase 3 resolution target for `Admin/Repository_Integrity_Protocol.md`
(RIP-005) and the authentication mechanism resolution target for
`Admin/Governance_Charter.md` (GOV-006). It does not supersede either document —
it implements the enforcement capability they declare as necessary.

**Honest v0 acknowledgment:** At current maturity, cryptographic enforcement
is defined here as a specification target, not an operational reality. Phase 3
automation does not yet exist. This file defines what must be built so that
implementation has a governed target to build against.

---

## Assumptions

| ID          | Assumption                                                                       | Basis                                         | Confidence | Expiry Trigger                                              |
|-------------|----------------------------------------------------------------------------------|-----------------------------------------------|------------|-------------------------------------------------------------|
| SEC-ASM-001 | Human operators have secure local means to preserve physical tokens              | Standard security practice — Analogous External | Medium   | Compromise confirmed in operational environment             |
| SEC-ASM-002 | Cryptographic standard libraries (Ed25519/SHA-256) remain robust                 | Current cryptographic consensus — Analogous External | Medium | Algorithmic vulnerability published against these standards |
| SEC-ASM-003 | GOV-008 minimum quorum definition will precede Phase 3 implementation            | Dependency ordering — Internally Derived      | Medium     | Phase 3 implementation proceeds without quorum definition   |
| SEC-ASM-004 | Electronics.md firmware trust doctrine remains the authoritative component layer | Scope boundary discipline — Internally Derived | High      | Electronics.md scope boundary revised to exclude firmware   |
| SEC-ASM-005 | Signing hardware maintains power continuity during override operations           | Operational assumption — Placeholder          | Low        | Degraded-power doctrine defined (see SEC-006)               |
| SEC-ASM-006 | Human operators acting as ratification authorities are not compromised, coerced, or impaired | Operational assumption — Placeholder | Low       | Human governance adversary model defined (EC-011); operator impairment doctrine defined (Safety_Protocols.md §V) |

---

## Trust Boundary Declaration
<!-- FROZEN: 2026-09-03 — Trust Boundary Declaration (cryptographic verification ≠ governance legitimacy). Do not weaken or reorder without formal amendment. -->

**This principle governs all sections of this document and must be read first.**

Cryptographic verification confirms identity and integrity. It does not confer
governance legitimacy.

A valid signature proves that a file was signed by a known key, and that the
file has not been altered since signing. It does not prove that the action
authorized by that signature was constitutionally permitted, ethically sound,
or within the scope of the signing authority.

Authorization flows from Tier 1 downward through the governance hierarchy
defined in `Admin/Governance_Charter.md`. No cryptographic mechanism substitutes
for that hierarchy. A signed instruction to override a Tier 1 Axiom is a
Constitutional violation regardless of the validity of the signature.

**The correct ordering:**
1. Governance legitimacy — defined by `Admin/Governance_Charter.md` Tier 1 Axioms
2. Authorization — granted through the human override doctrine defined there
3. Cryptographic enforcement — this file; verifies that authorized actions
   are executed with confirmed identity and integrity

Reversing this ordering — treating a valid signature as self-authorizing — is
the failure mode this file exists to prevent.

**On circular dependency risk:** The governance-cryptography chain carries an
inherent self-certification risk: governance defines override legitimacy,
cryptography enforces it, and integrity systems may eventually depend on both.
A fully self-certifying enforcement pipeline — where compromised governance
rewrites itself, signs the rewrite, and validates through its own enforcement
stack — is the highest-order failure mode this architecture must prevent.
The Trust Boundary Declaration addresses this philosophically. Structural
enforcement separation (immutable external root-of-trust, offline constitutional
anchor, human-ratified recovery source outside the repository execution
environment) is the unresolved mechanical requirement. See SEC-007a/SEC-007b.

**On permission-source trustworthiness:** Cryptographic verification assumes
the human operators issuing or ratifying overrides are not compromised, coerced,
or impaired. This assumption is not validated at current maturity. See SEC-ASM-006
and `Admin/Ethical_Constraints.md` EC-011 (Human governance adversary model
undefined). Until EC-011 is resolved, apply the interim authentication
requirements from `Admin/Governance_Charter.md` §Human Override Doctrine to
all Constitutional-class decisions.

---

### External Root-of-Trust — Constitutional Requirements *(SEC-007a resolution vehicle)*
<!-- FROZEN: 2026-09-03 — SEC-007a constitutional requirements (R1–R6). Ratified 2026-08-22. Residual physical layer is SEC-007b. Do not weaken without formal amendment. -->

The Trust Boundary Declaration states the philosophical rule: cryptographic
verification confirms identity and integrity; it does not confer governance
legitimacy.

This section states the **mechanical requirement** that makes that rule
enforceable against the highest-order failure mode: a compromised authority
chain that rewrites governance, signs the rewrite, and validates the
rewrite through its own enforcement pipeline (circular self-certification).

#### Problem

Governance defines legitimacy. Cryptography enforces it. Integrity systems
may depend on both. Without an anchor **outside** that loop, a sufficiently
compromised chain can:

1. Rewrite Tier 1 or hard-line doctrine
2. Sign the rewrite with keys the same chain controls
3. Accept the signature as proof of legitimacy

No amount of internal signature checking breaks that cycle.

#### Constitutional requirements

An external root-of-trust, for the purposes of this repository, must
satisfy **all** of the following:

| # | Requirement | Meaning |
|---|-------------|---------|
| **R1 — Externality** | The anchor **cannot be modified through the repository execution environment**. No agent, automated process, or online node that participates in ordinary Forge operation may alter, replace, or re-sign the anchor. | Breaks the self-modification path |
| **R2 — Independence from the enforcement pipeline** | Validation of the anchor must not depend solely on keys, policies, or integrity checks that the compromised chain could itself have rewritten. At least one verification path must terminate outside the ordinary governance–crypto–integrity stack. | Breaks circular validation |
| **R3 — Constitutional scope** | The anchor must be capable of covering (directly or by clear chain) the Tier 1 constitutional surface — at minimum the Governance Charter axioms and the Ethical_Constraints hard floors — so that a rewrite of those texts is detectable against the anchor. | Protects what matters most |
| **R4 — Human-ratified establishment and change** | Initial establishment of the anchor, and any subsequent change to it, requires explicit Human Governing Authority ratification. No autonomous process may create, rotate, or retire the constitutional anchor. | Preserves human sovereignty over the root |
| **R5 — Recoverability under compromise** | There must exist a defined recovery path that uses the anchor (or a human-ratified record bound to it) to restore a known-good constitutional state after suspected compromise of the online enforcement chain. Recovery must not require trusting the compromised chain's current self-attestation. | Makes the anchor useful under the failure mode it exists to survive |
| **R6 — Tamper-evidence** | Unauthorized alteration or substitution of the anchor must be detectable. Silent replacement without detection is a failed anchor. | Integrity of the anchor itself |

Meeting R1–R6 is necessary for an artifact to count as an external
root-of-trust under this doctrine. Physical form is out of scope here
(SEC-007b). **Scope boundary (Skeptic-confirmed):** R4 defends against a
compromised online enforcement chain rewriting governance; it does not by
itself defend against a compromised Human Governing Authority. This
section is not a universal trust theorem — that boundary is stated
honestly rather than papered over.

#### Minimum viable instantiations (illustrative, not exclusive)

Any one of the following *can* satisfy R1–R6 if implemented to the
requirements above; none is mandatory at this layer:

- Offline signed constitutional snapshot (e.g. GPG-signed export of Tier 1
  text + axioms), held outside all automated repository nodes, with
  verification that does not rely solely on online keys
- Hardware security module (or equivalent) holding root keys that cannot
  be rewritten by the repository runtime
- Human-ratified recovery record stored outside all automated systems,
  bound to a known-good constitutional hash

RIP-001's GPG-signed Git release tags provide a **tamper-evident archival
substrate** that a dedicated anchor could build on. They do **not** by
themselves satisfy R1–R6 as a full external root-of-trust; a dedicated
anchor remains a distinct requirement.

#### What this section does not do

- It does not choose or design the physical realization (SEC-007b).
- It does not define key generation ceremonies, HSM product selection, or
  air-gap procedures.
- It does not replace the Trust Boundary Declaration; it supplies the
  mechanical requirements the Declaration's philosophy implies.
- It does not claim that an external anchor currently exists in the
  operating environment. Until SEC-007b (or an equivalent instantiation)
  is achieved, the system continues to depend on human discipline and
  document integrity — the residual risk this entry has always named.

#### Relationship to adjacent unknowns

| Unknown | Boundary |
|---------|----------|
| **SEC-007b** | Physical implementation of an anchor that meets R1–R6. Blocked on this entry until constitutional requirements are specified. |
| **GOV-003** | Integrity enforcement architecture — consumer of an external anchor, not the definer of its constitutional properties. |
| **GOV-005** | Long-term constitutional stability — related horizon; not a substitute for R1–R6. |
| **RIP-001** | Prior-state archival (Resolved) — useful substrate; not a complete external root-of-trust by itself. |
| **GOV-006 / SEC human-override auth** | Operator authentication — distinct from constitutional anchor requirements. |

#### Residual risks (non-blocking)

| ID | Residual | Notes |
|----|----------|-------|
| SEC-007a-R1 | No instantiation yet exists in the operating environment | Expected; closed by SEC-007b progress, not by further prose here |
| SEC-007a-R2 | Exact binding format between anchor and Tier 1 text (hash tree, full snapshot, etc.) | Implementation detail for the chosen instantiation |
| SEC-007a-R3 | Multi-anchor or succession rules if the first anchor is lost | Deferred until at least one anchor exists |
| SEC-007a-R4 | R4 defends against a compromised online enforcement chain; it does not by itself defend against a compromised Human Governing Authority | Scope boundary, not a defect — confirmed by two independent Skeptic/Evidence reviewers |

*§SEC-007a — Payment via Specification. Closes SEC-007a (logged prior to 2026-08-22, exact date per Unknowns.md). Defines the constitutional requirements (R1–R6) an external root-of-trust must satisfy to break circular self-certification; physical realization remains SEC-007b. Full Closure Event — Proposer (Grok, 2026-08-22), Verifier (Claude, 2026-08-22 — Pass; Trust Boundary Declaration wording, circular-dependency note, and RIP-001 status all confirmed exact against source). Independence attestation: Grok (Proposer) and Claude (Verifier) are different agent instances. Skeptic/Evidence pass: two independent rounds, ChatGPT then Grok, both unconditional PASS, no required changes on either round — genuine convergence, both reviewers engaging with all criteria (contrast with EC-007's initial split verdict, where the second round required a follow-up because one reviewer had gone silent on two of three points). Mandatory Human Ratification required before this closure is binding — this file is constitutional/enforcement doctrine. Human Ratification: Human Governing Authority, 2026-08-22. Human-directed.*

---

## External Design Lineage (EDL)

**Purpose:** Log external engineering patterns — industry standards, historical
precedent, or cross-domain design ancestry (not limited to security or IT
standards; future rows may draw from aerospace redundancy doctrine, biological
systems, distributed consensus, or other domains) — as evidence weighed
against Forge doctrine, not as authority. Lazarus Forge's problem — rebuilding
trust from near-zero in a salvage-first, potentially decade-isolated
environment — is related to but not identical to the problem most external
standards solve ("protect a system that already exists"). This library makes
each departure from, or adoption of, external practice an explicit,
falsifiable design decision rather than an implicit assumption, and gives
future agents a place to see *why* without re-litigating the comparison.

External design patterns and standards are treated as evidence of successful
prior engineering, not evidence of universal truth. They provide tested
starting points, not binding authority. Forge adopts, modifies, departs from,
or observes external practices only after evaluating them against
constitutional principles, operational constraints, and empirical reality.
This guards against two opposite failure modes: Not-Invented-Here rejection
of external wisdom out of isolationist bias, and uncritical Appeal to
Authority adoption purely because a practice is an established standard.
Ties to EF-0.0 (Reality is sovereign) and EF-0.1 (What Is Not Evidence) —
industry consensus is prior evidence, not verification.

**Scope note:** This registry is local to Security_Protocols.md for now. A
repository-wide mandatory schema, and any automated harness enforcement tied
to it, is a structural governance change requiring human ratification per
`Admin/Governance_Migration_Protocol.md` — proposed but **not adopted** this
session. See Resolution Log.

### Lineage Status Lifecycle

Every entry holds one of these explicit states:

- **Researching** — source identified; analysis of intent, edge cases, and failure modes underway
- **Survey Complete** — external practice fully mapped; dependencies and failure modes documented
- **Decision Drafted** — Forge-specific posture (Adopt/Modify/Depart/Observe) formulated but unverified
- **Validated** — validation path cleared; decision active in a specification layer
- **Superseded** — shifting reality or higher-priority doctrine has rendered the decision obsolete

**Decision definitions:**
- **Adopt** — external pattern applies with no material change
- **Modify** — core principle adopted, mechanism changed for Forge's constraints (no trusted hardware assumed, no continuous connectivity, no external institutions)
- **Depart** — the pattern's underlying assumption does not hold for Forge; different approach required
- **Observe** — external practice has not converged, or is moving too fast to standardize on; inherits a hard 2-cycle Expiry Watch — failure to advance to Survey Complete or Decision Drafted within that window is a review trigger, not an automated repository-wide hold (see Scope note above)

*Note on Validation Needed vocabulary: labels below are descriptive, not yet
checked against `Admin/Canonical_Terms.md` for drift against the Verification
Maturity Model states in `Admin/Forge_Audit_Kit.md`. Flag for reconciliation
at next Canonical_Terms.md audit.*

### External Design Lineage Registry

| PAT-ID | Target Unknown | External Source | Problem | External Pattern | Forge Decision | Validation Needed | Status | Rationale |
|---|---|---|---|---|---|---|---|---|
| PAT-001 | SEC-007a | NIST SP 800-57 / FIPS 140-3; PKI root anchor governance | External root-of-trust — constitutional requirements for the anchor | Hardened, centralized HSMs + formal cryptographic key lifecycles | **Modify** | Constitutional ratification (human governing authority) | Ratified — Payment via Specification, 2026-08-22 | Adopts the principle that an anchor must be unmodifiable through the system it anchors. Departs from assuming permanent trusted hardware exists — Forge's anchor must survive salvage/bootstrap conditions. Constitutional floor requires human ratification, not technical proof alone; ties to the circular self-certification risk named in the Trust Boundary Declaration. SEC-007a closed; residual physical implementation is SEC-007b. |
| PAT-002 | SEC-007b | TCG / IETF secure and measured boot; air-gapped bootstrapping via manufacturer device certificates | External root-of-trust — physical implementation (offline HSM/EEPROM or equivalent) | Cryptographic signature validation baked into pristine, vendor-provisioned silicon | **Modify** | Hardware-in-the-loop testing; multi-agent review | Decision Drafted (open) | Adopts measured-boot and air-gap principles. Departs from assuming manufacturer-issued device provenance — salvaged hardware carries none; bridges the gap with multi-operator physical validation tokens. SEC-007a is now closed; SEC-007b is the remaining physical-layer open Unknown and is no longer blocked on an unresolved SEC-007a. |
| PAT-003 | SEC-005 | NIST SP 800-90; TPM/vTPM attestation, secure/measured boot | Trusted initialization environment for key generation | Isolated, high-entropy automated clean-room execution environments | **Modify** | Multi-agent review; operational deployment during Genesis Phase | Decision Drafted | Departs from clean-room and hardware-attestation-as-default assumptions. Interim definition uses human-supervised, air-gapped generation on Logic-Zero-verified hardware only (current restrictive interpretation, Section III.2). Formal closure gated on CT-004 (`Admin/Canonical_Terms.md`). |
| PAT-004 | SEC-011 | NIST post-quantum migration guidance; IETF hybrid classical+PQC transition patterns | Long-duration cryptographic continuity — entropy exhaustion, algorithm migration at Leviathan-class timescales | Phased migration to lattice-based post-quantum primitives | **Observe**, with a mandated extension | Future research; Observe entry, 2-cycle Expiry Watch | Researching | Monitors PQC convergence rather than standardizing early — industry has not converged and Forge cannot assume continuous access to current PQC infrastructure decades out. Extension: mandates an explicit low-overhead symmetric-key fallback path under entropy exhaustion. **Note:** this fallback is not covered by SEC-012 (SEC-012 is registered for asymmetric-crypto execution overhead on salvaged silicon — a different problem). If a symmetric-fallback-tree unknown is wanted, log it as a new ID (proposed SEC-013) rather than folding it into SEC-012. Routed to `Admin/Trajectories.md` as v1→v2 item. |

**Notes:**
- Add rows as new patterns or blockers surface; not limited to security-domain sources.
- Each Forge Decision should cite Axiom or doctrine ties where applicable.
- "Modify" is expected to be the most common outcome.
- Reconciled 2026-07-02 — this file's SEC-007 sidecar entry (below, Auditor Notes & Unknowns) is now split into SEC-007a/SEC-007b, matching `Unknowns.md` v4.4 and the split IDs PAT-001/PAT-002 are written against.

---

## Body

### I. Human Override Authentication & Verification (GOV-006)

**1. Multi-Signature Requirement**

No Tier 1 Constitutional Axiom or hard-line doctrine defined in
`Admin/Ethical_Constraints.md` may be overridden or suspended by a single
human operator. High-severity overrides require dual-token signature or a
multi-party hardware confirmation rule.

The specific minimum quorum threshold (number and diversity of independent
agents or hardware systems required) is defined by GOV-008 in
`Admin/Governance_Charter.md`. This file's multi-signature requirement
is not operational until GOV-008 provides that threshold. Until GOV-008
is resolved, the interim authentication requirement from
`Admin/Governance_Charter.md` §Human Override Doctrine applies:
independent confirmation from a second human operator, external cryptographic
signature from an orthogonal system, or a dated physical or digital record
created outside the repository system.

**2. Interim Bootstrap Authentication**

In the absence of an established public key infrastructure (Genesis Phase),
overrides must depend on physical air-gapped challenges — such as localized
split-secret tokens or pre-shared multi-party cryptographic pads — to prevent
local agent subversion. This is an interim procedure. It does not satisfy
Phase 3 requirements. It satisfies the current interim authentication
requirement while GOV-008 and the full PKI implementation remain unresolved.

**3. No Automated Session Continuance**

Override assertions are transactional and ephemeral. They do not persist
across multiple agent runtime sessions or automated multi-agent compilation
cycles. Every override requires a discrete signature event.

An agent that received override authorization in a prior session carries no
residual authority into a new session. This prevents authority accumulation
across session boundaries — a known attack vector in multi-agent systems where
session state is not fully cleared between runs.

**4. Authentication Event Logging (SEC-REG-001)**

All override attempts — successful or refused — must be logged with:
- Timestamp (ISO 8601 UTC)
- Identity of requesting agent or operator
- Scope of override requested
- Authentication method used
- Outcome (authorized / refused / escalated)
- Cryptographic binding token (nonce, monotonic counter, or RIP block-hash) —
  see replay protection requirement below

Logs are append-only. Override logs are subject to the Resolution Log
integrity requirements defined in `Admin/Repository_Integrity_Protocol.md`.

**Replay Protection Requirement (SEC-REG-001-A):** All human override
signatures must bind a cryptographic nonce, a monotonically increasing
session counter, or a specific block-hash from the prior-state archival
system defined in `Admin/Repository_Integrity_Protocol.md` RIP-001.
This binding guarantees transactional uniqueness and prevents replay of
a valid intercepted signature block within the same session window or
across closely timed network partitions before log sync completes.
*(Placeholder — RIP-001 is Resolved as an archival substrate; the SEC-008 replay-protection mechanism itself remains open and is the remaining blocker. Until the SEC-008 mechanism is operational, treat each override as session-unique by requiring a second-operator confirmation that the override is a new request, not a replay.)*

**5. Degraded-Operation Security Doctrine Note**

Security mechanisms that are operationally impossible during degraded recovery
conditions will predictably be bypassed and therefore cannot be treated as
reliable safeguards. Multi-party token coordination, append-only logging, and
partition handling all impose operational burden that increases under stress.

The design implication: security requirements must degrade safely, not fail
open. When signing hardware loses power, when a quorum cannot be assembled,
or when clock synchronization is unavailable, the correct behavior is
constrained operation or halt — not bypassing security requirements to maintain
throughput. See SEC-006 (timestamp trust) and SEC-001 (quorum under partition)
for the unresolved specifics.

**6. Human-Factors Attack Surface Note**

The override ratification process assumes operators are uncompromised,
uncoerced, and cognitively unimpaired. Side-channel attacks, social engineering
directed at operators holding tokens, and timing attacks on multi-signature
processes are not addressed at current maturity. Cross-reference:
- `Admin/Safety_Protocols.md` §V — operator impairment recognition
- `Admin/Ethical_Constraints.md` EC-011 — human governance adversary model
- SEC-009 — compromise detection criteria (Ratified, Payment via Specification, 2026-08-22); SEC-008 remains open for signature replay protection
- `Admin/Ethical_Constraints.md` EC-011 — human governance adversary model (still open)

Until EC-011 is resolved, treat anomalous override patterns
(unusual timing, repeated requests, out-of-character scope) as escalation
triggers to human review. SEC-009 detection signals are available for use under the SEC-002 state machine.

---

### II. Phase 3 Cryptographic Enforcement (RIP-005)

*All claims in this section are Placeholder — enforcement mechanisms defined
here do not yet exist. This section is the specification target for future
implementation.*

**1. Automated Commit Signing**

Transitioning from human audit logs to cryptographic assertions, all files
at Candidate Specification maturity or above must be signed using an approved
node key-pair. *(Maturity states defined in `Admin/Forge_Audit_Kit.md`
§Verification Maturity Model — Candidate Specification, Provisional
Specification, and Operational Specification are the signing-eligible states.)*
Unsigned files at these maturity levels are treated as unverified regardless
of their declared status.

**2. Frozen Section Verification**

Sections explicitly designated as `<!-- FROZEN -->` by governance files must
maintain static hashes. The automated audit script (`Automation/AUDIT_HARNESS.py`)
shall verify that local file content matches signed historic blocks before
triggering compilation or deployment pipelines. *(Placeholder — AUDIT_HARNESS.py
Phase 1 checks are not yet implemented per RIP-002. Phase 3 frozen-section
verification is a downstream dependency of Phase 1 completion.)*

**3. Phase Implementation Ordering**

Phase 3 cryptographic enforcement is the third phase of the automation
migration path defined in `Admin/Repository_Integrity_Protocol.md`. It cannot
be claimed before Phases 1 and 2 are complete:

| Phase | Prerequisite                                      | Status             |
|-------|---------------------------------------------------|--------------------|
| 1     | Structural checks in AUDIT_HARNESS.py             | Open — RIP-002     |
| 2     | Comparison checks requiring archived prior states | RIP-001 Resolved (archival substrate); SEC-008 mechanism still open |
| 3     | Cryptographic verification — this file            | Blocked by 1 and 2 |

Governance Enforcement State must not advance beyond actual implemented
capability. Claiming Phase 3 enforcement before Phases 1 and 2 are complete
is integrity theater.

**Note on Phase 2 / RIP-001 circular dependency:** SEC-001 (quorum recovery
under partition) references archived state access as a prerequisite for
emergency partition verification. However, archived prior states are a Phase 2
requirement that depends on RIP-001. To prevent circular blocking: archived
state read-access for emergency partition verification operates under a
read-only hardware bootstrap bypass that does not depend on active Phase 3
cryptographic execution state. This bypass is a manual human-supervised
procedure, not an automated fallback, until Phase 3 is operational.

---

### III. Salvaged Logic & Node Authentication (EL-006)

**Relationship to Electronics.md**

Component-level infiltration prevention for salvaged hardware — firmware
inspection protocols, Logic-Zero wipe procedures, and non-destructive
harvesting doctrine — is defined and owned by `Operations/Electronics.md`.
This section does not redefine that doctrine. It defines the administrative
authentication layer that sits above it: how nodes that have passed
Electronics.md validation are admitted into the trusted cluster.

A node that has passed Logic-Zero wipe and signature-verified bootstrap load
per Electronics.md doctrine is a candidate for cluster admission. Admission
itself requires the node identity verification procedures below.

**1. Zero-Trust Cluster Admission**

No salvaged or newly initialized node may join the local mesh or operational
network without completing both layers:
- Component-level trust: Logic-Zero wipe and signature-verified bootstrap
  load per `Operations/Electronics.md` EL-006 doctrine
- Node-level identity: key-pair registration and cluster admission handshake
  per this section

Passing one layer does not substitute for the other.

**2. Node Key-Pair Registration**

Each node must possess a unique key-pair generated within a trusted
initialization environment. *(Definition of "trusted initialization
environment" is pending — see SEC-005 and `Admin/Canonical_Terms.md` CT-004.
Until defined, apply the most restrictive interpretation: human-supervised,
air-gapped, on verified hardware only.)* Key generation must not occur on
the node's own hardware before that hardware has completed the Logic-Zero
wipe and bootstrap load. Key material generated on unverified hardware is
untrusted regardless of subsequent wipe procedures.

**3. Key Rotation Cycles**

Key rotation schedule is *(Placeholder — rotation period not yet defined;
see SEC-003)*. Until defined, treat key material as requiring rotation at
each major version transition (v0→v1, v1→v2) at minimum. Key retirement,
secure destruction, and operator-loss continuity doctrine are undefined —
see SEC-004.

**4. Admission Revocation**

A node whose key material is suspected compromised must be suspended from
cluster participation pending investigation. Suspension is reversible;
revocation is permanent. Detection criteria are specified below
(SEC-009); full response doctrine is specified below (SEC-002).

---

### Compromise Detection Criteria *(SEC-009 resolution vehicle)*

Section III.4 requires that a node whose key material is **suspected
compromised** be suspended pending investigation. This section defines how
that suspicion is generated.

Detection produces **suspicion**, not automatic permanent revocation.
Suspension is reversible; revocation remains governed by SEC-002.

#### Detection signals

Any one of the following is sufficient to generate **compromise suspicion**
and trigger mandatory suspension under III.4:

| ID | Signal | Meaning |
|----|--------|---------|
| **D1 — Checksum / state disagreement** | Material disagreement between a node's presented state (or key-bound artifact) and a prior signed reference state that the verifying party holds | Integrity break relative to known-good history |
| **D2 — Attestation failure on admission** | Node fails cluster-admission attestation (or equivalent join-time proof) when attestation is required | Node cannot prove expected key/identity posture at the gate |
| **D3 — Timestamp anomaly** | Timestamps on signed artifacts or protocol messages fall outside defined tolerance relative to verifier time or peer consensus (cross-ref SEC-006) | Clock manipulation, replay window abuse, or impossible ordering |
| **D4 — Behavioral divergence** | Node behavior diverges from its declared role or expected pattern in a way that is observable even when signatures still verify (e.g. persistent out-of-role requests, repeated privilege-scope expansion, systematic refusal-pattern evasion) | Possible key misuse or node capture |
| **D5 — Anomalous override pattern** | Override or high-privilege requests show unusual timing, repetition, scope, or provenance that does not match the operator's established pattern (cross-ref interim guidance already pointing anomalous overrides to human review) | Possible compromised override path or coerced operator |
| **D6 — External / independent report** | A human operator, independent auditor, or peer unit logs a reasoned compromise concern against the node or its key material | External observation does not require internal statistical confidence |

Meeting **any one** of D1–D6 generates suspicion and requires suspension.
Multiple concurrent signals increase urgency of investigation; they are not
required for entry into the suspended state.

**Note on D4:** No calibrated behavioral-divergence threshold currently
exists. `Architecture/Cognitive_Frameworks.md`'s CF-001 is a hardware
watchdog minimum standard (`Operations/Electronics.md`) — a different
layer and mechanism, correctly not the source of this threshold. CF-001
is **In Progress**, not untouched: its heartbeat-window parameter
(τ = 50ms, Analogous confidence) is already defined, and it remains
Blocking only pending first-hardware-prototype validation at Measured
confidence. `Challenges/Emergence.md`'s **EM-001 is the existing
registered unknown for this exact question** ("Behavioral opacity
detection threshold — at what measurable divergence does watchdog
escalation trigger?"), and it is itself explicitly dependent on CF-001
resolution before it can be specified. D4 therefore inherits a two-hop
dependency chain — D4 → EM-001 → CF-001 — and operates on qualitative
judgment until that chain resolves. This is not a gap needing a new
unknown; it is an existing one this section correctly defers to rather
than duplicates.

#### Suspicion vs confirmation

| State | Meaning | Immediate effect |
|-------|---------|------------------|
| **Suspected** | At least one detection signal has fired | Mandatory suspension (III.4); investigation opens; reversible |
| **Confirmed compromised** | Investigation (human and/or independent audit path) concludes key material or node authority is compromised | Permanent revocation path under SEC-002 |

This section does **not** define the investigation procedure or the
revocation authority chain — those belong to SEC-002. It only defines the
entry condition into the suspected state.

#### Counting and scope rules

- **Distinct events:** Repeated identical observations of the same
  underlying fault count as one signal instance for urgency scoring; they
  still sustain suspicion until cleared.
- **Tolerance values** (timestamp skew for D3; behavioral magnitude/duration
  for D4): Placeholder where not already defined. D3 defers numeric
  tolerance to SEC-006 when available. D4 defers to EM-001, itself pending
  CF-001. Suspicion may still be raised on reasoned judgment; numeric
  tightening is residual to the chain above, not to this section.
- **No silent self-clear:** A node does not clear its own suspicion by
  presenting a later valid signature. Clearance of suspicion (return to
  full participation without revocation) requires the investigation
  outcome defined under SEC-002.

#### Relationship to adjacent unknowns

| Unknown | Boundary |
|---------|----------|
| **SEC-002** | Revocation and compromise *response* (suspension handling, permanent revocation, re-admission). This section only generates the suspicion that feeds it. |
| **SEC-006** | Timestamp trust under degraded clock — supplies tolerance doctrine for D3. |
| **SEC-001** | Quorum recovery under partition — affects how detection signals propagate; does not define the signals. |
| **SEC-008** | Signature replay protection — related failure mode; replay may *cause* D3 or D5 patterns but is specified separately. |
| **SEC-003** | Key rotation period — lifecycle hygiene, not detection. |
| **GOV-006** | Human override authentication — anomalous override patterns (D5) may implicate override nodes; revocation safeguards for those nodes remain GOV-006 / SEC-002. |
| **CF-001** | Hardware watchdog minimum standard (`Operations/Electronics.md`), In Progress — τ = 50ms parameter defined, Blocking only on hardware validation. Not the home for D4's threshold directly — that is EM-001 — but the upstream dependency EM-001 itself is blocked on. |
| **EM-001** | (`Challenges/Emergence.md`) The actual registered unknown for D4's calibrated behavioral-divergence threshold. D4 operates qualitatively until EM-001 resolves; EM-001 itself is blocked on CF-001. This section does not attempt to resolve or duplicate EM-001. |

#### Explicit non-goals

- This section does not define cryptographic primitives, attestation
  protocols, or watchdog implementations.
- It does not authorize automatic permanent revocation on signal alone.
- It does not set final numeric tolerances for D3 (owned by SEC-006) or D4
  (owned by EM-001, transitively CF-001).
- It does not absorb SEC-002's response doctrine.
- It does not overload CF-001 with a software behavioral-pattern role
  CF-001 does not have.
- It does not register a new unknown for D4's threshold — EM-001 already
  exists and is the correct owner.

#### Residual risks (non-blocking)

| ID | Residual | Notes |
|----|----------|-------|
| SEC-009-R1 | Numeric tolerances for timestamp skew (D3) | Owned by SEC-006; qualitative suspicion remains valid until calibrated |
| SEC-009-R2 | Concrete attestation profile for D2 | Implementation / cluster-admission design |
| SEC-009-R3 | Urgency scoring when multiple signals fire | Optional operational refinement; not required for closure |
| SEC-009-R4 | Calibrated behavioral-divergence threshold for D4 | Not a new unknown — tracks existing `Challenges/Emergence.md` EM-001, itself dependent on CF-001 resolution. D4 remains valid on qualitative judgment in the meantime; this residual closes automatically when EM-001 does, not through separate work here. |
| SEC-009-R5 | D2 doesn't distinguish "node fails the attestation proof" from "node cannot complete the proof because infrastructure is unavailable" | Both reasonably trigger suspension under current wording; the distinction matters for how much the resulting suspicion should be weighted as evidence of compromise during investigation (SEC-002), not for whether suspension is warranted. Skeptic-flagged, non-blocking. |

*§SEC-009 — Payment via Specification. Closes SEC-009 (logged prior to 2026-08-22, exact date per Unknowns.md). Defines D1–D6 compromise-detection signals and the suspicion/confirmation split feeding SEC-002. Full Closure Event — Proposer (Grok, 2026-08-22), Verifier (Claude, 2026-08-22 — Pass). Independence attestation: Grok (Proposer) and Claude (Verifier) are different agent instances. Revision history: Option A's D4 cross-reference to CF-001 was identified as a mismatch (CF-001 is hardware-watchdog containment, not a behavioral-divergence definition); Option B corrected this to defer to the existing EM-001 unknown rather than proposing a duplicate; CF-001's actual In-Progress/τ=50ms status was folded in on same-day follow-up after being found stale in an earlier check. Skeptic/Evidence pass: two independent rounds, ChatGPT then Grok, both unconditional PASS, no required changes on either round. Mandatory Human Ratification required before this closure is binding — this file is enforcement doctrine. Human Ratification: Human Governing Authority, 2026-08-22. Human-directed.*

---

### Key Revocation and Compromise Response Doctrine *(SEC-002 resolution vehicle)*

SEC-009 defines how **suspicion** is generated (signals D1–D6). This
section defines the **response**: states, authority, behavior under
suspension, permanent revocation, and re-admission.

#### States and transitions

| State | Entry | Effect | Exit |
|-------|--------|--------|------|
| **Active** | Normal admission / cleared investigation | Full cluster participation under current key material | → Suspended on any SEC-009 signal |
| **Suspended** | Any SEC-009 detection signal (D1–D6), or explicit human order | Removed from cluster participation for privileged acts; investigation opens | → Active (cleared) or → Revoked (confirmed) |
| **Revoked** | Investigation concludes compromise, or Human Governing Authority orders immediate revocation | Permanent for that key identity; key must not verify as valid | Only via formal **re-admission** under a **new** key identity |

There is no silent path from Suspended back to Active on the basis of a
later valid signature from the same key. There is no automated
Active → Revoked path without an investigation record, except an
explicit, logged Human Governing Authority order of immediate revocation.

#### Authority chain

| Action | Who may authorize | Notes |
|--------|-------------------|--------|
| **Suspend** | Any party that validly raises a SEC-009 signal; or a human operator | Entry into suspension is mandatory on signal; does not require multi-party consensus. **A valid SEC-009 signal is sufficient to trigger mandatory suspension, but the party raising the signal acquires no authority over investigation, clearance, revocation, or re-admission by virtue of raising that signal.** Raising a signal and holding downstream authority are distinct; this table's remaining rows govern the latter regardless of who triggered entry. |
| **Clear suspension** (→ Active, no revocation) | Investigation outcome of no compromise; human operator confirmation **required** when the triggering signal was D5 (anomalous override) or D6 (external report) | Clearing is not self-attestation by the suspended node |
| **Revoke** | Human Governing Authority; or a multi-party quorum if later defined under GOV-006 for override-capable nodes | Never unilateral by the suspect node; never by automated self-check alone |
| **Immediate revoke** (skip prolonged investigation) | Human Governing Authority only, with logged rationale | Use when delay itself is the dominant risk |
| **Re-admit after revocation** | Human Governing Authority, after re-admission criteria below are met | New key material only; revoked key stays denied |

#### Behavior while Suspended

- The suspended key must not be accepted for new privileged or
  governance-relevant acts.
- Peers that have received the suspension signal must refuse such acts
  from that key.
- In-flight non-privileged work may complete if abrupt stop increases
  risk (same spirit as EC-004 active-process descent); no *new*
  privileged work starts.
- **Propagation:** Best-effort to all reachable peers. Under partition,
  every node that has received the signal applies local suspension
  immediately; reconciliation of partitioned views is SEC-001 territory
  (residual).
- **Investigation hold:** Preserve logs, attestation history, and the
  SEC-009 signal record. A subsequent valid signature from the same key
  does **not** clear suspicion (aligned with SEC-009 "no silent self-clear").
- **Duration:** Suspension persists until cleared or escalated to
  revocation. No automatic timeout → Active.

#### Confirmed compromise → Revocation

Revocation is permanent for the **key identity** found compromised.

1. Investigation (human and/or independent audit path) concludes
   compromise, **or** Human Governing Authority orders immediate
   revocation.
2. Key identity is recorded as revoked and must fail verification
   thereafter.
3. Propagation follows the same best-effort rule as suspension;
   partitioned nodes apply on first receipt (SEC-001 residual for
   partition semantics).
4. **Override-capable nodes** (surface governed by GOV-006): until
   GOV-006 specifies additional safeguards, **Human Governing Authority
   ratification is mandatory** for any revocation of an override-capable
   node. This interim rule is hard.

Revocation does not by itself define recovery of constitutional state
under root-level compromise; that remains SEC-007a/b.

#### Re-admission after revocation

Re-admission is admission of a **new** key identity, not reactivation of
the revoked key. All of the following are required:

1. **New key material** generated under the trusted initialization rules
   in force at the time (SEC-005 residual until defined; interim:
   human-supervised generation consistent with existing restrictive
   interpretation in this file).
2. **Revoked key remains denied** — must not verify as valid under any
   peer's acceptance rules.
3. **Explicit Human Governing Authority approval** of the re-admission.
4. **Successful admission attestation** under the new key (SEC-009 D2
   path clean at admission time).

Failure of any one item blocks re-admission.

#### Relationship to adjacent unknowns

| Unknown | Boundary |
|---------|----------|
| **SEC-009** | Detection signals (D1–D6) that enter Suspended. This section does not redefine them. |
| **SEC-001** | Quorum recovery and propagation under terminal partition. |
| **SEC-003** | Routine key rotation schedule (not compromise-driven). |
| **SEC-005** | Trusted initialization environment for new key material. |
| **SEC-006** | Timestamp tolerance (upstream of SEC-009 D3). |
| **SEC-007a/b** | External root-of-trust and recovery when the root itself is in question. |
| **GOV-006** | Full override-node revocation safeguards; interim mandatory human ratification stated above until then. |
| **SEC-008** | Signature replay protection — related failure mode; specified separately. |

#### Explicit non-goals

- This section does not define cryptographic revocation-list formats,
  CRLs, or network transport.
- It does not set partition-quorum mathematics (SEC-001).
- It does not define trusted init ceremonies (SEC-005).
- It does not replace SEC-009 detection criteria.
- It does not authorize a suspended or revoked node to clear itself.

#### Residual risks (non-blocking)

| ID | Residual | Notes |
|----|----------|-------|
| SEC-002-R1 | Propagation timeout / partition reconciliation details | Owned by SEC-001 |
| SEC-002-R2 | Full override-node revocation safeguards | Owned by GOV-006; interim human-ratification rule applies until then |
| SEC-002-R3 | Trusted init details for re-admission key generation | Owned by SEC-005 |
| SEC-002-R4 | Concrete revocation-record / denied-list format | Implementation detail |

*§SEC-002 — Payment via Specification. Closes SEC-002 (logged prior to 2026-08-22, exact date per Unknowns.md). Defines the Active/Suspended/Revoked state machine, authority chain, and re-admission requirements consuming SEC-009's detection signals. Full Closure Event — Proposer (Grok, 2026-08-22), Verifier (Claude, 2026-08-22 — Pass). Independence attestation: Grok (Proposer) and Claude (Verifier) are different agent instances. Skeptic/Evidence pass: two independent rounds. Round one (ChatGPT) returned CONDITIONAL PASS, requiring one amendment — explicit statement that raising a SEC-009 signal (including D6, which any party may raise) confers no downstream authority over investigation, clearance, revocation, or re-admission; incorporated into the Suspend row above. Mandatory Human Ratification required before this closure is binding — this file is enforcement doctrine. Human Ratification: Human Governing Authority, 2026-08-22. Human-directed.*

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                                                      | What Failed                                                                          | What Was Learned                                                                                                                          | Confidence | Revalidation Needed |
|------------|---------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Initial architecture without explicit trust boundary declaration                    | Implied "signature therefore authorized" logic left open as attack vector            | Trust boundary must be declared explicitly before cryptographic mechanisms — governance legitimacy precedes enforcement                    | Analogous  | Yes                 |
| 2026-05-27 | Audit Review  | Firmware trust doctrine co-located with administrative security                     | Duplicate ownership risk with Electronics.md; scope boundary became ambiguous        | Electronics.md owns component-level infiltration prevention; Security_Protocols.md owns administrative authority layer                    | Replicated | No                  |
| 2026-05-28 | Audit Review  | "Specification" used as signing-eligibility threshold without maturity model alignment | Ambiguous — conflates File State status with Verification Maturity Model states   | Signing eligibility must reference maturity states (Candidate Specification and above), not raw File State status field                   | Replicated | No                  |
| 2026-06-19 | Audit Review  | Override logging without replay protection specification                            | Valid signatures could theoretically be replayed within same session window; logging integrity depends on uniqueness not enforced | All override signatures must bind nonce, monotonic counter, or RIP block-hash for transactional uniqueness (SEC-REG-001-A) | Analogous  | Yes                 |
| 2026-06-19 | Audit Review  | Permission-source trustworthiness assumed without declaration                       | Human operators ratifying overrides assumed uncompromised; assumption was implicit rather than explicit | Permission-source trust assumption must be declared explicitly (SEC-ASM-006) and cross-referenced to EC-011 adversary model | Analogous  | Yes                 |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| SEC-DS-001 | G3/G6 gate-maturity divergence on this file's 2026-07-02 Exploration audit | Grok: G3 partial, G6 blocked — folds unresolved upstream unknowns (SEC-007a/b, GOV-008, etc.) into gate status. Gemini: G3 deferred-permissible, G6 passed — treats gate status as coverage/textual-only. | Low — interpretive, not factual | Resolved — 2026-07-02, via `Admin/Forge_Audit_Kit.md` v1.5 Gate Scope vs. Promotion Readiness clarification, sourced from `Admin/Auditor_Protocols.md` §Specification Promotion Rules ("all six gates pass" and "open unknowns are non-blocking" are separate, independently required promotion conditions). Gemini's reading is structurally correct. Grok's underlying concern is valid but belongs to promotion-readiness tracking — already carried in this file's Status footer (SEC-007a/b, SEC-005/CT-004, GOV-008, SEC-009 listed as promotion blockers), not to G3/G6 scoring. Synthesizer-level resolution — reversible if reasoning is disputed, not a Tier 1 ratification. | `Admin/Security_Protocols.md` |

---

## Abandoned Paths

| Date       | Path                                                                        | Why Abandoned                                                                                                              | Reconsider? |
|------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-26 | Firmware trust doctrine owned by Security_Protocols.md                      | Electronics.md already owns component-level infiltration prevention; dual ownership creates scope conflict                  | No          |
| 2026-05-27 | SEC-001 quorum-under-partition resolved independently of GOV-008             | Minimum quorum definition is the same underlying problem; GOV-008 is the correct resolution owner                          | No          |
| 2026-05-28 | "Specification" as flat signing-eligibility threshold                        | Does not align with Verification Maturity Model; maturity states are the correct eligibility boundary                      | No          |
| 2026-06-19 | Phase 2/RIP-001 circular dependency resolved through automated fallback      | Any automated fallback that depends on Phase 3 state to access Phase 2 archives is itself circular; resolved via read-only human-supervised bootstrap bypass instead | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Trust Boundary Declaration section removed, weakened, or moved below Body sections
- Circular dependency risk note removed from Trust Boundary Declaration
- Permission-source trustworthiness note removed from Trust Boundary Declaration
- Multi-signature requirement simplified to single-key or software-only mechanism
  without corresponding update to `Admin/Governance_Charter.md`
- Phase 3 automation claims advanced beyond Placeholder status before RIP-001
  and RIP-002 are resolved
- Signing eligibility reverts to flat "Specification" status without maturity
  model alignment
- Scope boundary revised to absorb firmware trust doctrine from Electronics.md
  without explicit Electronics.md scope boundary revision
- GOV-008 quorum definition referenced as resolved before GOV-008 is closed
- Node admission procedures removed or made optional
- Authentication event logging requirement removed or made non-append-only
- Replay protection requirement (SEC-REG-001-A) removed from authentication
  event logging before RIP-001 is operational
- Degraded-operation doctrine note removed from Section I
- SEC-005 trusted initialization environment closed without canonical definition
  in `Admin/Canonical_Terms.md` CT-004
- Abandoned path for SEC-001 independent resolution reopened without human
  ratification and GOV-008 resolution
- Phase 2 bootstrap bypass for partition verification expanded beyond read-only
  human-supervised procedure without human ratification
- SEC-ASM-006 removed before EC-011 (human governance adversary model) is resolved
- Ethical Anchor field absent, altered, or does not match canonical string
- Verification Ref field changed from `Admin/Verification_Gates.md`

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### SEC-001 — Quorum Recovery Under Terminal Network Division

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Architecture / Governance          |
| Blocking      | Yes                                |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-26                         |
| Last Reviewed | 2026-06-19                         |

**Description:** What cryptographic fallback procedure executes if a
multi-node swarm experiences a permanent communication partition, leaving
isolated clusters below the required multi-signature threshold for override
authorization.

**Why It Matters:** Bounded, local autonomy could stall indefinitely during
critical recovery operations if a quorum cannot legally be met. A fallback
that is too permissive creates a partition-exploitation attack vector; one
that is too restrictive freezes legitimate operations.

**Resolution Path:** Deferred to GOV-008 (`Admin/Governance_Charter.md`) —
minimum hardware and agent quorum definition is a prerequisite input to any
fallback procedure defined here. SEC-001 cannot be resolved before GOV-008
closes. Once GOV-008 defines the minimum quorum, revisit with a concrete
fallback proposal: time-locked decay window, hardware-level fallback protocol,
or escalation to human override via interim authentication. Cross-reference
RIP-001 — partition recovery may require archived state access via read-only
human-supervised bootstrap bypass (see Phase Implementation Ordering note).

---

### SEC-002 — Key Revocation and Compromise Response Doctrine Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | **Ratified — Payment via Specification, 2026-08-22** |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Governance              |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-27                         |
| Last Reviewed | 2026-08-22                         |

**Description:** The repository lacks defined procedures for key revocation
following confirmed or suspected compromise. Distinction between reversible
suspension and permanent revocation, revocation authority chain, propagation
to cluster nodes, and post-revocation re-admission criteria are all undefined.

**Why It Matters:** Without revocation doctrine, a compromised key remains
nominally trusted until the next rotation cycle. In adversarial or degraded
environments this window may be operationally significant.

**Resolution Path:** Deferred via Specification — define revocation authority
chain, propagation mechanism during degraded connectivity, re-admission
criteria, and suspension vs. revocation distinction. Cross-reference SEC-001
(partition affects propagation), GOV-006 (override node revocation requires
additional safeguards), and SEC-009 (compromise detection criteria must
precede revocation trigger definition).

---

### SEC-003 — Key Rotation Period Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Security / Technical               |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-27                         |
| Last Reviewed | 2026-05-28                         |

**Description:** No rotation period is defined for node key-pairs. Version-
transition rotation is the current floor but no time-based or event-based
schedule exists.

**Why It Matters:** Indefinitely valid key material accumulates compromise
risk. Without a defined schedule, rotation is ad hoc and audit verification
of compliance is not possible.

**Resolution Path:** Deferred via Specification — define rotation triggers:
time-based (calendar interval), event-based (version transition, personnel
change, suspected exposure), and condition-based (hardware replacement,
Logic-Zero re-wipe). Cross-reference SEC-002 — rotation and revocation
must be consistent.

---

### SEC-004 — Key Lifecycle Doctrine Incomplete

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Security / Governance              |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-28                         |
| Last Reviewed | 2026-05-28                         |

**Description:** Key lifecycle doctrine covers generation and partial rotation
but does not address: secure key archival for dormant nodes, secure destruction
procedures on retirement, inheritance or handoff under operator incapacitation,
and post-mortem recovery for long-duration or degraded deployments.

**Why It Matters:** Incomplete lifecycle doctrine creates key material that
exists in undefined states — neither active nor provably destroyed. In
long-duration autonomous deployments (Leviathan-class), operator incapacitation
and hardware retirement are expected conditions, not edge cases.

**Resolution Path:** Deferred via Specification — define: (1) archival doctrine
for dormant key material; (2) secure destruction verification procedure;
(3) operator-loss continuity — who inherits authority and through what
authentication path; (4) post-mortem recovery for hardware that cannot be
physically accessed. Cross-reference SEC-002 (revocation), SEC-003 (rotation),
and SEC-011 (long-duration cryptographic continuity) — all must form a coherent
lifecycle.

---

### SEC-005 — Trusted Initialization Environment Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Technical               |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-28                         |
| Last Reviewed | 2026-05-28                         |

**Description:** Section III requires key-pair generation within a "trusted
initialization environment" but the term is undefined. It is currently
ambiguous whether trusted means: physically secured, cryptographically
verified, human-supervised, air-gapped, or some combination.

**Why It Matters:** Ambiguous trust boundaries in key generation are a primary
attack surface. An adversary who can influence the initialization environment
can compromise keys before they are ever used. The term must have a canonical
definition before this section is promoted.

**Resolution Path:** Deferred via Specification — define trusted initialization
environment in `Admin/Canonical_Terms.md` CT-004 with at minimum: physical
custody requirements, software verification requirements, network isolation
requirements, and attestation method. Until defined, the most restrictive
interpretation applies: human-supervised, air-gapped, on verified hardware
only — per interim note in Section III.2. Closing CT-004 closes this unknown.

---

### SEC-006 — Timestamp Trust Under Degraded Clock Synchronization

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Security / Technical               |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-05-28                         |
| Last Reviewed | 2026-05-28                         |

**Description:** Authentication event logging requires ISO 8601 UTC
timestamps, but partitioned systems and air-gapped nodes frequently lose
reliable clock synchronization. The behavior of append-only logs under
degraded or absent time synchronization is undefined.

**Why It Matters:** Timestamp integrity is required for audit trail
interpretability. Logs with unreliable timestamps cannot establish
reliable event sequencing, which undermines the primary value of the
append-only log requirement.

**Resolution Path:** Deferred via Specification — define: (1) minimum
acceptable clock source for timestamping; (2) behavior when clock
synchronization is unavailable (hold entries with uncertainty flag,
use monotonic counter, or reject logging until sync restored); (3)
audit trail interpretation rules for entries with degraded timestamp
confidence. Cross-reference SEC-001 — partition scenarios are the
primary context where clock sync is lost.

---

### SEC-007a — External Root-of-Trust: Constitutional Requirements Undefined

| Field         | Value                              |
|---------------|-------------------------------------|
| Status        | **Ratified — Payment via Specification, 2026-08-22** |
| Risk          | High                                |
| Priority      | Critical                            |
| Type          | Architecture / Governance           |
| Blocking      | No                                  |
| Owner         | `Admin/Security_Protocols.md` (constitutional layer) |
| First Logged  | 2026-05-28 (as SEC-007)             |
| Last Reviewed | 2026-08-22                          |
| Split From    | SEC-007, vertically split 2026-07-02 |
| Design Lineage | PAT-001 (see External Design Lineage above) |

**Description:** The governance-cryptography enforcement chain carries a
circular self-certification risk: governance defines legitimacy, cryptography
enforces it, and integrity systems may eventually depend on both. A
sufficiently compromised authority chain could theoretically rewrite
governance, sign the rewrite, and validate through its own enforcement
pipeline. This entry scopes the **constitutional question**: what must be
true of an external anchor for it to actually break the self-certification
loop — not how that anchor is physically built (see SEC-007b).

**Why It Matters:** This is the highest-order failure mode for the entire
enforcement architecture. The Trust Boundary Declaration addresses it
philosophically; this entry is the unresolved mechanical requirement. Until
an external trust anchor exists, the system depends entirely on human
discipline and the integrity of the governance documents themselves — which
are the things being protected.

**Resolution Path:** Cross-module — spans GOV-003 (integrity enforcement
architecture), GOV-005 (long-term constitutional stability). RIP-001 (prior-
state archival) is Resolved as of 2026-06-27 — GPG-signed Git release tags
establish a tamper-evident archival substrate that a signed offline
constitutional snapshot could build on, though a dedicated anchor is a
distinct requirement from general prior-state archival and remains open.
Minimum viable resolution: define at least one external trust anchor that
cannot be modified through the repository execution environment — offline
signed constitutional snapshot, hardware security module holding root keys,
or human-ratified recovery record stored outside all automated systems.
This is an above-repository architectural decision requiring human
ratification; no automated agent may resolve this unilaterally. Blocks
SEC-007b.
Deferral trigger documented in `Architecture/Facilities.md` §VII Deferred
governance parameters table — this decision is meaningful only once a
physical site exists.

---

### SEC-007b — External Root-of-Trust: Physical Implementation Undefined

| Field         | Value                              |
|---------------|-------------------------------------|
| Status        | Open                                |
| Risk          | High                                |
| Priority      | Critical                            |
| Type          | Architecture / Hardware             |
| Blocking      | No — blocked pending SEC-007a       |
| Owner         | `Admin/Security_Protocols.md` (owning layer: Operations) |
| First Logged  | 2026-05-28 (as SEC-007)             |
| Last Reviewed | 2026-07-02                          |
| Split From    | SEC-007, vertically split 2026-07-02 |
| Design Lineage | PAT-002 (see External Design Lineage above) |

**Description:** Once SEC-007a defines what the constitutional anchor must
guarantee, this entry covers **how it is physically realized**: offline HSM,
EEPROM, signed physical media, or equivalent salvaged-hardware-compatible
mechanism. Salvaged hardware carries no manufacturer-issued device
provenance, so standard secure/measured-boot assumptions (pristine,
vendor-provisioned silicon) do not directly apply — see PAT-002.

**Why It Matters:** A well-defined constitutional anchor is inert without a
physical mechanism that actually implements it. This is the bridge between
governance doctrine and salvage-environment reality.

**Resolution Path:** Blocked pending SEC-007a — physical design cannot be
finalized until the constitutional floor it implements is defined. Cross-ref
`Operations/Electronics.md` for salvaged-hardware constraints and Logic-Zero
node admission. Requires hardware-in-the-loop testing and multi-agent review
per PAT-002's Validation Needed field before advancing past Decision Drafted.

---

### SEC-008 — Signature Replay Protection Mechanism Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Technical               |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-06-19                         |
| Last Reviewed | 2026-06-19                         |

**Description:** Override signature logging (SEC-REG-001) does not specify
a mechanism to prevent replay attacks. A valid intercepted signature block
could be replayed within the same session window or across closely timed
network partitions before log sync completes, allowing an adversary or
malfunctioning agent to re-execute an authorized action without new
ratification.

**Why It Matters:** Ephemeral, transactional override design (Section I.3)
is undermined if signatures are replayable. The append-only log cannot
distinguish a replayed signature from a genuine one without a uniqueness
binding mechanism.

**Resolution Path:** Add mandatory requirement to SEC-REG-001: all override
signatures must bind a cryptographic nonce, a monotonically increasing session
counter, or a specific block-hash from RIP-001 prior-state archival. Interim
procedure: RIP-001 is Resolved as archival substrate; SEC-008 replay mechanism remains open. Until SEC-008 is operational, require second-operator confirmation that the override is a new request, not a replay. SEC-REG-001-A added to Section I.4 body as the interim declaration.

---

### SEC-009 — Compromise Detection Criteria Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | **Ratified — Payment via Specification, 2026-08-22** |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Technical               |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-06-19                         |
| Last Reviewed | 2026-08-22                         |

**Description:** Section III.4 specifies that a node whose key material is
"suspected compromised" must be suspended, but provides no doctrine for how
suspicion is generated. Detection criteria — checksum disagreement, behavioral
anomaly, failed attestation, impossible timestamps, anomalous override patterns
— are entirely absent.

**Why It Matters:** Without defined detection criteria, compromise response
is reactive and human-dependent. Silent compromise remains undetectable until
an observable failure occurs, which may be after significant damage.

**Resolution Path:** Add compromise detection subsection to Section III or
create a linked detection criteria annex. Minimum criteria: (1) checksum
disagreement with prior signed state; (2) attestation failure on cluster
admission; (3) timestamp anomaly beyond defined tolerance (cross-ref SEC-006);
(4) behavioral divergence beyond watchdog threshold (cross-ref CF-001).
Cross-reference SEC-002 — compromise detection must trigger the revocation
doctrine defined there.

---

### SEC-010 — Cryptographic Algorithm Migration Doctrine Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Architecture            |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-06-19                         |
| Last Reviewed | 2026-06-19                         |

**Description:** SEC-ASM-002 assumes Ed25519/SHA-256 remain robust, but no
procedure exists for migrating to replacement algorithms if those standards
are deprecated or compromised. Algorithm agility — the ability to switch
cryptographic primitives without breaking the trust chain — is undefined.

**Why It Matters:** Cryptographic standards have finite lifespans. Post-quantum
concerns and algorithmic vulnerabilities are not theoretical at decadal
timescales. A system that cannot migrate algorithms loses its trust guarantees
when the underlying primitives fail, with no recovery path.

**Resolution Path:** Define algorithm migration doctrine: (1) trigger conditions
for migration (published vulnerability, NIST deprecation, internal review
schedule); (2) migration procedure preserving audit trail continuity; (3)
re-signing requirements for existing signed artifacts; (4) transition window
during which both old and new algorithms are accepted. Cross-reference SEC-004
(key lifecycle) and SEC-011 (long-duration continuity) — all three form a
coherent long-duration security posture.

---

### SEC-011 — Long-Duration Cryptographic Continuity Undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Security / Architecture            |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-06-19                         |
| Last Reviewed | 2026-06-19                         |

**Description:** Leviathan-class deployments imply decade-scale operation,
potential operator death or incapacitation, hardware replacement cycles,
and isolated nodes with no external connectivity. No doctrine addresses:
cryptographic entropy exhaustion over long timescales, migration across
cryptographic generations, algorithm deprecation, or authority continuity
after operator succession.

**Why It Matters:** Long-duration deployments will outlive individual
operators, specific hardware generations, and potentially current cryptographic
standards. Without continuity doctrine, trust chain breaks silently at an
undefined future point with no recovery procedure.

**Resolution Path:** Develop long-duration continuity doctrine addressing:
(1) entropy refresh mechanisms for isolated nodes; (2) authority succession
when operators are incapacitated or unavailable; (3) algorithm migration
timeline (cross-ref SEC-010); (4) hardware retirement and key archival
cross-ref SEC-004. Route to `Admin/Trajectories.md` as a v1→v2 transition
planning item — not required for v0 operational status but must exist before
Leviathan-class deployment is authorized.

---

### SEC-012 — Asymmetric Cryptographic Overhead on Resource-Constrained Salvaged Silicon

| Field         | Value                              |
|---------------|-------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Security / Hardware                |
| Blocking      | No                                 |
| Owner         | `Admin/Security_Protocols.md`      |
| First Logged  | 2026-07-02                         |
| Last Reviewed | 2026-07-28                         |

**Description:** Asymmetric cryptographic execution overhead on
resource-constrained salvaged silicon — specifically 8/16-bit
microcontrollers, the class most likely to be recovered and reused
under this repository's salvage-first sourcing model. This entry
existed in `Unknowns.md`'s active index since at least v4.0 with no
matching sidecar block here — registered now to close that gap; the
underlying concern is not new.

**Why It Matters:** Signature verification and key operations that
are computationally trivial on modern hardware may impose meaningful
latency or power draw on salvaged 8/16-bit MCUs. Under Logic-Zero
recovery (degraded/minimal firmware operation), this risks either a
localized denial-of-service — a node too slow to complete
verification within an operational window — or pressure to bypass
verification entirely under time constraint, which would be a
protocol violation, not a performance one.

**Resolution Path:** Characterize actual asymmetric-crypto execution
time on representative salvaged 8/16-bit MCU classes (empirical
benchmarking required — currently no data exists either way).
Cross-reference `Operations/Electronics.md` EL-006 (firmware trust
and reflashing validation) for the hardware side of this question.
If overhead proves prohibitive on the lowest-capability salvaged
tier, define either a lighter-weight verification scheme for that
tier specifically, or an explicit minimum-capability floor below
which a node cannot participate in cryptographic verification at
all — the latter is a real constraint worth stating plainly rather
than working around.

---

### Resolution Log

- 2026-08-10: **SEC-007a deferral trigger cross-linked (Claude review + Grok
  apply).** Blocking remains No (constitutional item; no automated agent may
  resolve unilaterally — file’s own rule respected). Added: (1) row in
  `Architecture/Facilities.md` §VII Deferred governance parameters table;
  (2) back-link from SEC-007a Resolution Path to that table. Gives a stated
  “when” without pretending the architectural choice is made. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits as Engineering/Waste pass).**
  Findings only; Spec Gates left locked at 0/6. (1) Open Unknowns **13** =
  SEC-001–006, SEC-007a, SEC-007b, SEC-008–012 — matches local sidecar and
  `Unknowns.md`. (2) SEC-001 correctly Blocking Yes. (3) SEC-007a Priority
  Critical + “highest-order failure mode for the entire enforcement
  architecture” language, while Blocking = No (it blocks SEC-007b, not
  general promotion). Logged as F-SEC-003 for human review — not auto-flipped;
  constitutional domain differs from the operational-safety understatement
  pattern seen on TS-002/EL-005. (4) No SEC-* closed. Human-directed.

- 2026-07-28: SEC-012 given a formal sidecar entry — previously
  present in `Unknowns.md`'s active index only, with no matching
  block here, surfaced by a Grok-run repo-wide desync audit and
  verified against source (zero prior mentions of SEC-012 anywhere
  in this file) before registering. Description built from the
  index's own existing text rather than invented; empirical
  benchmarking still entirely undone. Open Unknowns count: 12 → 13.
  Verified and registered by Claude — Synthesizer/Auditor,
  human-directed.

- 2026-05-26: File created (v0.1) — initial architecture by Gemini
  (Engineer/Security). GOV-006 and RIP-005 resolution paths initiated.
  SEC-001 logged.
- 2026-05-27: v0.2 revision — Trust Boundary Declaration added. Scope
  boundary clarified. SEC-001 deferred to GOV-008. SEC-002 and SEC-003
  logged. SEC-REG-001 assigned to authentication event logs. Relationship
  section added. Standard Drift Indicators added. Placeholder labels added
  to Phase 3 claims. Verification Ref corrected. Open Unknowns: 3.
- 2026-05-28: v0.3 revision — ChatGPT Skeptic/Auditor findings actioned.
  Signing eligibility corrected from flat "Specification" to maturity-model
  states (Candidate Specification and above). "Trusted initialization
  environment" noted as undefined with interim restriction; SEC-005 logged.
  SEC-ASM-002 provenance label corrected to Analogous External. SEC-ASM-005
  added for signing hardware power continuity assumption. Degraded-operation
  security doctrine note added to Section I.5. Circular dependency risk
  acknowledged explicitly in Trust Boundary Declaration; SEC-007 logged.
  SEC-004 logged (key lifecycle doctrine incomplete). SEC-006 logged
  (timestamp trust under degraded clock). SEC-003 rotation reference
  corrected in Section III.3. Key retirement/destruction noted in III.3.
  Scope Boundary updated to note trusted initialization environment gap.
  Drift Indicators updated with new entries. Abandoned Paths updated.
  Lessons Learned entry added. Open Unknowns updated to 7.
- 2026-06-06: v0.4 revision — Navigation Anchors added. Verification Ref
  corrected to `Admin/Verification_Gates.md`. Drift Indicator reference
  updated. Relationship section updated — `Admin/Governance_Migration_Protocol.md`
  and `Admin/Safety_Protocols.md` added. Content unchanged.
- 2026-06-19: v0.5 revision — Four-agent audit pass (Gemini, Grok, ChatGPT,
  Claude). Nine changes: (1) SEC-ASM-006 added — permission-source
  trustworthiness assumption made explicit. (2) Trust Boundary Declaration
  updated with permission-source trustworthiness note and EC-011 cross-ref.
  (3) SEC-REG-001-A added to Section I.4 — replay protection requirement
  (nonce/counter/block-hash binding); interim procedure pending RIP-001.
  (4) Section I.6 added — Human-Factors Attack Surface Note; cross-refs
  Safety_Protocols.md §V and EC-011. (5) Phase 2/RIP-001 circular dependency
  clarified in Section II.3 — read-only human-supervised bootstrap bypass
  declared as resolution. (6) Section III.4 updated — SEC-009 cross-ref
  added for compromise detection. (7) SEC-008 logged — signature replay
  protection mechanism undefined. (8) SEC-009 logged — compromise detection
  criteria undefined. (9) SEC-010 logged — cryptographic algorithm migration
  doctrine undefined. (10) SEC-011 logged — long-duration cryptographic
  continuity undefined. (11) Two new Lessons Learned entries added. (12)
  Phase 2 bootstrap bypass Abandoned Path added. (13) Drift Indicators
  expanded with five new entries. Open Unknowns updated to 11.

- **2026-07-02** — External Design Lineage (EDL) section added, positioned
  after Trust Boundary Declaration and before Body. Four entries logged:
  PAT-001 (SEC-007a), PAT-002 (SEC-007b), PAT-003 (SEC-005), PAT-004
  (SEC-011). Renamed from working title "Security Pattern Library" per
  multi-agent review — EDL better reflects that future entries need not be
  security-domain sources. Lineage Status Lifecycle adopted (Researching /
  Survey Complete / Decision Drafted / Validated / Superseded). PAT-004
  rationale corrected: a proposed symmetric-fallback-tree unknown is
  explicitly distinguished from SEC-012 (SEC-012 remains scoped to
  asymmetric-crypto overhead on salvaged silicon; a symmetric fallback
  unknown would require new ID SEC-013 if logged). A companion proposal to
  canonize EDL as a repository-wide constitutional gate (GOV-MAND-009,
  blocking Exploration→Candidate Specification promotion file-wide, with
  automated AUDIT_HARNESS.py enforcement) was **not adopted** this session —
  flagged as a structural governance change requiring routing through
  `Admin/Governance_Migration_Protocol.md` two-track ratification, not
  session-level multi-agent consensus. Known drift: this file's own SEC-007
  sidecar entry has not yet been split into SEC-007a/SEC-007b to match
  `Unknowns.md` v4.4; PAT-001/PAT-002 are written against the split IDs
  pending that reconciliation. Open Unknowns unchanged at 11 (EDL logs
  decisions on existing unknowns; introduces no new ones itself).

- **2026-07-02** — SEC-007 sidecar entry split into SEC-007a (constitutional
  requirements, owning layer Admin) and SEC-007b (physical implementation,
  owning layer Operations; blocked pending SEC-007a), closing the reconciliation
  gap flagged in the entry immediately above. Downstream references corrected:
  Trust Boundary Declaration pointer, Relationship section (GOV-003/GOV-005
  dependency, GMP-004 cross-ref, RIP-001 cross-ref — RIP-001 also noted as
  Resolved), Status footer promotion-blocker list, and the EDL section's
  known-drift note. Open Unknowns 11 → 12 (split adds one entry; no new
  unknown introduced).

- **2026-07-02** — SEC-DS-001 logged and resolved in Active Disputes: the
  Grok/Gemini G3/G6 gate-maturity divergence flagged at this file's audit,
  per `Admin/Auditor_Protocols.md` §Dispute Handling Protocol (disputes are
  interpretation conflicts, tracked explicitly, not left to silently
  disappear). Resolved via `Admin/Forge_Audit_Kit.md` v1.5's new Gate Scope
  vs. Promotion Readiness clarification — gates test execution quality;
  open-unknown blocking is a separate promotion condition. Gemini's original
  scoring is structurally correct. No change to this file's promotion-blocker
  list (SEC-007a/b, SEC-005/CT-004, GOV-008, SEC-009) — those unknowns were
  never in dispute, only whether they belonged inside G3/G6 scoring.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; GOV-006
  (human override authenticity) and GOV-008 (minimum agent quorum) are the
  originating unknowns this file resolves; Trust Boundary Declaration defers
  to the governance hierarchy defined there; Tier 1 Axioms are not subject
  to cryptographic override; GOV-003 and GOV-005 are cross-module dependencies
  for SEC-007a
- `Admin/Governance_Migration_Protocol.md` — GMP-004 (ratification
  authentication gap) explicitly cross-references SEC-007a as the resolution
  path; Tier 1 amendment ratification records are a primary use case for the
  external root-of-trust architecture defined in SEC-007a/SEC-007b
- `Admin/Repository_Integrity_Protocol.md` — RIP-005 is the originating
  unknown for Phase 3 enforcement; Phases 1 and 2 defined there are
  prerequisites to Phase 3 implementation here; RIP-001 (Resolved) cross-
  references SEC-001 and SEC-007a
- `Admin/Ethical_Constraints.md` — co-Tier 1; Anti-Weaponization and Life
  Preservation doctrines are not subject to override by any cryptographic
  mechanism regardless of signature validity; EC-011 (human governance
  adversary model) is cross-referenced in Trust Boundary Declaration and
  SEC-ASM-006
- `Admin/Safety_Protocols.md` — physical operator safety is outside the
  cryptographic scope of this file; referenced here because operator
  impairment recognition (Safety_Protocols.md §V) is a prerequisite for
  valid human ratification — an impaired operator's cryptographic signature
  is technically valid but governmentally suspect; cross-referenced in
  Section I.6
- `Admin/Auditor_Protocols.md` — Tier 2; authentication event logs subject
  to audit trail requirements defined there
- `Admin/Forge_Audit_Kit.md` — Tier 3; Verification Maturity Model referenced
  in Section II for signing eligibility; SEC- prefix in Sidecar ID Reference
- `Admin/Canonical_Terms.md` — CT-004 (trusted initialization environment
  definition) is a pending addition required before Section III.2 can be
  promoted; closing CT-004 closes SEC-005
- `Operations/Electronics.md` — component-level infiltration prevention
  owner; Logic-Zero wipe is Layer 1 prerequisite for node admission here;
  complementary layers, not overlapping owners
- `Admin/Trajectories.md` — SEC-011 (long-duration cryptographic continuity)
  to be logged as v1→v2 transition planning item
- `Unknowns.md` — SEC-008 through SEC-012 to be registered/reconciled at
  next Unknowns.md update; SEC-007 split (SEC-007a/SEC-007b) registered
  there as of v4.4 pending sync into this file's own sidecar
- External Design Lineage registry (this file, above) — PAT-001 through
  PAT-004 anchor SEC-007a, SEC-007b, SEC-005, and SEC-011 respectively;
  citable from Unknowns.md and future audits

---

## Status

**Current (2026-09-03):** File-level maturity remains Draft / Spec Gates 0/6. Individual subsections SEC-002, SEC-007a, and SEC-009 are Ratified (Payment via Specification, 2026-08-22). Open substantive Unknowns: SEC-001, SEC-003, SEC-004, SEC-005, SEC-006, SEC-007b, SEC-008, SEC-010, SEC-011, SEC-012. Promotion blockers are the open set above plus GOV-008; SEC-007a and SEC-009 are no longer promotion blockers.

**Historical record (Version 0.8, retained for lineage — do not treat as current):**
Version 0.8 — SEC-DS-001 (Grok/Gemini G3/G6 dispute) logged and resolved via
`Admin/Forge_Audit_Kit.md` v1.5 (2026-07-02). SEC-007 sidecar split into
SEC-007a/SEC-007b, reconciling with
`Unknowns.md` v4.4/v4.5 (2026-07-02); underlying audit maturity unchanged
since four-agent pass (2026-06-19). At that time the bottom block recorded G1–G6 cleared at Exploration stage and listed SEC-007a/b, SEC-005/CT-004, GOV-008, and SEC-009 as promotion blockers. Those statements are superseded by the Current block above and by the 2026-08-22 File State / sidecars.

**What must remain constant:**

**Cryptographic verification confirms identity and integrity.**
**It does not confer governance legitimacy.**
**Authorization flows from Tier 1 downward.**
