# SEC-007b design-lineage research — session transcript

**Filed 2026-09-15.** This is preserved reference/background research, not
doctrine and not a body-text insertion. Produced by Grok on 2026-09-15,
following CF-006's resolution, as exploratory groundwork for SEC-007b
(External Root-of-Trust: Physical Implementation Undefined) — still Open,
Critical, design lineage PAT-002 at Decision Drafted. Claude spot-verified
the live-repo claims (PAT-002's entry, SEC-007b's status fields) against
`Admin/Security_Protocols.md` before filing; they check out. The general
technical material (TCG, DICE, RATS) is industry background, not a repo
claim to verify, but is included because it consistently and correctly
maps onto the Forge's existing three-level split (component recovery /
node admission / external root-of-trust) rather than proposing anything
be adopted. Nothing here is selected, adopted, or ready for insertion —
SEC-007b's actual physical form is still an open design decision requiring
hardware-in-the-loop testing and multi-agent review per PAT-002, per this
file's own Resolution Path.

---

## Part 1 — SEC-007b status review

### Identity

| Field | Live value |
|-------|------------|
| **Full name** | External Root-of-Trust: Physical Implementation Undefined |
| **Status** | Open |
| **PAT-002 lineage** | Decision Drafted (open) |
| **Risk / Priority** | High / Critical |
| **Type** | Architecture / Hardware |
| **Owner** | Security_Protocols.md (owning layer noted as Operations) |
| **Split** | From SEC-007 on 2026-07-02 (007a = constitutional, 007b = physical) |
| **Blocking** | No longer blocked on SEC-007a (007a Ratified 2026-08-22). 007b is the sole remaining blocker on the original SEC-007 split. |
| **Last reviewed** | 2026-09-10 (stale "pending 007a" language removed) |

**Not ratified.** Only SEC-007a completed Closure Event + human ratification.

### What problem it owns

**SEC-007a** answers: *What must be true of an anchor so circular
self-certification is broken?* → R1–R6 (FROZEN, ratified).

**SEC-007b** answers: *How is that anchor physically realized in a
salvage/bootstrap world?*

Without 007b, R1–R6 are requirements with no instantiation.

### What 007b must implement (via R1–R6)

| Req | Core demand | Physical implication |
|-----|-------------|----------------------|
| R1 Externality | Anchor cannot be modified through the repository execution environment | Offline / air-gapped / human-only change path; not writable by cluster nodes or agents |
| R2 Independence | Verification must not depend only on keys/policies the compromised chain could rewrite | At least one check terminates outside ordinary governance–crypto–integrity stack |
| R3 Constitutional scope | Can cover Tier 1 surface (Charter axioms, Ethical_Constraints hard floors) | Anchor binds those texts (hash tree, signed snapshot, etc.) — format detail may vary |
| R4 Human-ratified establishment/change | Create/rotate/retire anchor only with Human Governing Authority | No autonomous anchor lifecycle |
| R5, R6 | Further mechanical constraints in the FROZEN body | Design must not weaken them |

007a residuals already point at 007b: no instantiation yet (007a-R1),
binding format (007a-R2), multi-anchor succession (007a-R3) — deferred
until at least one anchor exists.

### Design lineage (PAT-002)

| Aspect | PAT-002 stance |
|--------|----------------|
| External patterns | TCG / IETF secure & measured boot; air-gapped bootstrap via manufacturer device certificates |
| Adopt | Measured-boot and air-gap principles |
| Modify / depart | Do not assume pristine vendor-provisioned silicon or manufacturer device provenance |
| Salvage bridge | Multi-operator physical validation tokens (conceptual — not a finished protocol) |
| Example forms named | Offline HSM, EEPROM, or equivalent |
| Validation needed | Hardware-in-the-loop testing + multi-agent review before leaving Decision Drafted |

So 007b is explicitly not "buy a TPM and turn on vendor secure boot on
e-waste MCUs." That path conflicts with Electronics non-integrable
classes and EL-006.

### Candidate physical forms (exploratory — not selected)

| Form | Fits salvage? | Notes vs R1–R6 |
|------|---------------|----------------|
| Offline HSM / smartcard holding root keys | Possible if never networked into cluster control | Strong R1/R2 if procedures enforce air-gap; cost/availability |
| EEPROM / OTP / write-once media with human-ratified hashes | Compatible with scavenged parts if write-once is real | Must prevent online rewrite (R1) |
| Signed constitutional snapshot on offline media + GPG (RIP-001 related) | Repo already has GPG-signed release tags as archival substrate | 007a notes RIP-001 helps but is not a full dedicated anchor by itself |
| Multi-operator physical tokens (PAT-002) | Matches no-manufacturer-provenance constraint | Needs ceremony design; not specified |
| Vendor secure-boot locked MCUs | Poor as the constitutional anchor | Locks out Logic-Zero; non-integrable for logic roles; wrong control plane |

No form is adopted in-repo. Choosing one is the core of 007b work.

### Dependencies and consumers

| Direction | Relationship |
|-----------|----------------|
| Upstream | SEC-007a (done) — constitutional floor |
| Parallel | EL-006 v1+ (signing + key storage + RoT); SEC-005 trusted init environment; GOV/GMP ratification auth |
| Downstream consumers (when real) | Honest "signature-verified" admission (CF-006 now correctly defers to v1+/007b); firmware image authorization; constitutional rewrite detection |
| Does not unblock by itself | FA-001 site, first MCU batch for v0 hash practice (that is EL-006 procedure executability) |

### Resolution path (live, unchanged by this filing)

1. SEC-007a is done — physical design may proceed.
2. Cross-ref Electronics for salvage / Logic-Zero constraints.
3. Hardware-in-the-loop + multi-agent review per PAT-002 before advancing
   past Decision Drafted.
4. Implied house bar for something this critical: map design → R1–R6,
   evidence, likely human ratification (same class as 007a), Payment via
   Specification — mechanism exists, not only described.

**Explicitly insufficient:** more Security_Protocols prose, Copilot-style
five-anchor protocols without hardware, or treating locked donor
bootloaders as the RoT.

### Practical exploration order (if/when hardware work starts)

1. Pick one minimal instantiation that can satisfy R1 and R4 first
   (human-ratified, offline-only change).
2. Define how Tier 1 texts are bound (R3) — even a single signed hash list.
3. Define verification path that does not rely only on cluster keys (R2).
4. HITL test: can an online process alter the anchor? (Must fail.)
5. Multi-agent review → only then consider Status movement past Decision
   Drafted.
6. Keep EL-006 v0 and 007b tracks separate in Resolution Logs so procedure
   success never reads as RoT success.

---

## Part 2 — TCG secure / measured boot standards (background)

TCG (Trusted Computing Group) is the industry body behind TPM and related
attestation. What people casually call "TCG secure boot" is usually a
bundle of specs, not one document. The important split for the Forge is
**measured boot vs verified (UEFI) secure boot**, and what root of trust
the chain assumes.

**Core ideas:** Root of Trust for Measurement (RTM, static or dynamic);
measured boot (hash each stage, extend into PCRs, plus event log);
attestation (remote party evaluates PCR values against golden
measurements); verified/UEFI secure boot (refuses to run unsigned code —
related but not identical to measured boot). Measured boot answers "what
ran?"; verified secure boot answers "may this run?"

**Spec families (PC-centric):** TPM Library (Family 2.0); PC Client
Platform TPM Profile; PC Client Platform Firmware Profile (defines what
firmware measures, which PCR each class of code goes into, event log
structure). PCR 7 carries secure boot policy; PCRs 0–6 cover firmware,
config, UEFI drivers, boot manager. Extend rule: `PCR_new =
Hash(PCR_old || measurement)`.

**Lighter-weight roots relevant to MCUs:** MARS (minimal
measurement/attestation IP block for microcontrollers); DICE (Device
Identity Composition Engine — hardware Unique Device Secret + measurement
of first mutable code → Compound Device Identifier; layered attestation;
very small hardware requirement). DICE is the most plausible pattern if
the Forge ever builds new or fully controlled devices.

**What TCG assumes that salvage breaks:** manufacturer-provisioned
TPM/EK/platform certs (usually absent on e-waste); immutable
vendor-controlled RTM in ROM (unknown, may be locked or backdoored);
golden measurements from OEM (no OEM reference for arbitrary boards);
"secure boot on" implying platform health (often means locked bootloader
→ cannot Logic-Zero → Electronics non-integrable). This is exactly why
PAT-002 says: adopt measured-boot and air-gap principles, but Modify away
from pristine vendor-provisioned silicon.

**Useful takeaway (principles only):** trust must start somewhere
immutable or external (RTM / SEC-007a externality); record what ran
separately from "it booted"; authorization (who may load this image) is a
different control from measurement (what was loaded); manufacturer roots
are not Forge roots on salvage. **Not useful as drop-in:** PC Client PFP
PCR maps, OEM RIMs, or treating scavenged TPM+secure-boot boxes as
SEC-007b.

---

## Part 3 — DICE attestation protocols (background)

DICE is TCG's lightweight alternative to a full TPM for device identity +
layered attestation, aimed at constrained devices where a discrete TPM is
impractical.

**Core objects:** UDS (Unique Device Secret, hardware-protected, never
leaves the DICE RoT after use); TCI (measurement/hash of the next
code/config layer); CDI (Compound Device Identifier — secret derived from
UDS ⊕ measurements, or prior CDI ⊕ measurements, binding this device to
what ran). First transition: measure first mutable code → TCI, derive
CDI₀ from UDS + TCI, lock UDS in hardware, pass CDI₀ forward. Later layers
derive from the previous CDI, not the UDS — change the code and all
descendant CDIs change. Identity and integrity are coupled by design.

**Open-dice-style split:** Attestation CDI (mixes in code/config
measurements, changes on firmware update) vs Sealing CDI (stable inputs
only, can seal data across updates).

**Relevance to LazarusForge:** EL-006 v0 remains wipe + hash + log on
wipeable parts — DICE doesn't replace Logic-Zero on scavenged chips.
Locked/vendor-DICE devices with vendor-owned UDS and policies are the same
non-integrable class as locked bootloaders unless the Forge controls the
RoT. DICE is a plausible pattern for Forge-built or fully controlled
hardware later (minimal RoT, air-gapped UDS provisioning, layered measure
of Forge firmware) — aligned with PAT-002's Modify stance, not current
doctrine. What DICE does not give the Forge for free: trust in random
e-waste that happens to implement DICE, a substitute for SEC-007b's
external anchor, or closure of EL-006 without controlled keys and a
verifier policy the Forge owns.

---

## Part 4 — RATS endorsement models (background)

RATS = Remote ATtestation procedureS (IETF, RFC 9334). Role- and
message-oriented, not tied to any one chip or standard.

**Roles:** Attester (produces Evidence — claims about its state);
Verifier (appraises Evidence using policy + trusted inputs → Attestation
Results); Relying Party (uses Attestation Results under its own policy);
Endorser (supplies Endorsements — trusted assertions about the Attester or
its roots); Reference Value Provider (supplies expected/golden
measurements). Appraisal is roughly: Evidence + Endorsements + Reference
Values + Policy → Attestation Results.

**Endorsements vs Reference Values:** an Endorsement establishes *who/what
is allowed to speak* (e.g., "this key is the manufacturer's root for
device family X"); a Reference Value establishes *what state counts as
good* (e.g., expected firmware hash). RATS keeps these separate so a
Verifier can trust a key while still rejecting wrong software.

**Interaction models:** Challenge/Response (fresh Evidence per session);
Uni-directional (Attester pushes Evidence); Streaming (continuous). Also
Passport (Attester carries stamped Results to Relying Parties) vs
Background-check (Relying Party asks the Verifier directly) deployment
shapes.

**Endorsement sourcing models:** Manufacturer-primary (closed supply
chain, new devices); Owner-controlled (deployer provisions roots and
golden values after intake — fits salvage, air-gapped, no OEM trust);
Multi-endorser/supply-chain (layered Attesters, DICE-like); Self-endorsement
only (not real remote attestation in the RATS sense — just local claims).

**Relevance to LazarusForge:** EL-006's provenance log + hash is a local
Evidence-like record of what was done, not yet a full remote Attester
protocol. The run sheet's known-good image hash (P3–P4) is a seed of
owner-defined Reference Values, not OEM ones. SEC-007a is a constitutional
Endorsement root for governance texts, not device attestation by itself.
SEC-007b is the possible hardware basis for Attester keys if
Forge-provisioned. Node admission (Security §III, post-CF-006) is a
Relying Party decision currently based on v0 hash procedure, not signature
Evidence. The Forge's abandoned dual-ownership path and PAT-002's Modify
stance point toward an owner-controlled endorsement model — the Forge
defines reference firmware hashes and any roots after Logic-Zero, not the
donor OEM. Until SEC-007b and EL-006 v1+ exist, the Forge has procedure
compliance Evidence (run sheet Outcome S) but not a full RATS loop — no
general Verifier service, no endorsement distribution, no Attestation
Results format. Appropriate for Exploration, not a gap to paper over.

---

## Disposition

Filed 2026-09-15 on James's request, as reference material for whenever
SEC-007b's physical design work actually starts. Nothing here changes
SEC-007b's Status (Open), PAT-002's lineage (Decision Drafted), or any
other live field. Cross-referenced from SEC-007b's own sidecar entry in
`Admin/Security_Protocols.md`.
