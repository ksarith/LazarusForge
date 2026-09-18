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

---

## Part 5 — R1–R6 candidate matrix framing, and R5 recovery-procedure
hypotheses (added 2026-09-16, Class B+D stint)

Continuation stint, same discipline as Parts 1–4: live tree first (worked
from the ratified R1–R6 text above and RIP-001's GPG-signed release-tag
substrate), map candidates against requirements, do not select or adopt,
end in one disposition. **Nothing in this part changes SEC-007b's Status
(Open) or PAT-002's lineage (Decision Drafted).**

### Recommended matrix shape (not yet built — framing only)

| Candidate form | R1 Externality | R2 Independence | R3 Constitutional scope | R4 Human-ratified | R5 Recoverability | R6 Tamper-evidence | Salvage / Logic-Zero fit | Notes / blockers |
|---|---|---|---|---|---|---|---|---|
| Offline HSM / smartcard (air-gapped) | | | | | | | | |
| EEPROM / OTP / write-once media + human-ratified hashes | | | | | | | | |
| Signed constitutional snapshot on offline media + GPG (builds on RIP-001) | | | | | | | | |
| Multi-operator physical validation tokens (PAT-002) | | | | | | | | |
| Vendor secure-boot locked MCUs | | | | | | | | |

Scoring vocabulary proposed: Pass / Conditional (needs procedure) / Fail /
Needs HITL. **The matrix itself has not been filled in** — only its shape
and the preliminary reasoning below exist so far.

### Preliminary reasoning (not a ranking to be trusted as-is — see caveat below)

Grok's first pass ranked "signed constitutional snapshot + GPG" as
strongest, reasoning it already has an archival substrate (RIP-001,
verified real above), cleanly satisfies R1/R4, and needs minimal new
hardware, with R2/R5 procedure design as the weakest residual. Vendor
secure-boot locked MCUs were flagged for rejection as a primary
constitutional anchor — correctly, since that conflicts with Electronics
non-integrable-class doctrine and Logic-Zero, both already live.

**Important caveat, from ChatGPT's review, and worth preserving
explicitly:** ranking a candidate as "strongest" before the matrix is
actually filled in and stress-tested inverts the research strategy's own
order — the matrix is supposed to demonstrate which candidate is
strongest, not confirm a preference formed before building it. This
preliminary reasoning is filed as a starting hypothesis for whoever picks
up the matrix-building stint next, not as a conclusion.

### R5 recovery-procedure hypotheses for all four non-rejected candidates

Exploratory design detail, grounded in the live R1–R6 text. **No
concrete recovery procedure exists in the repository** — everything
below is hypothesis, not doctrine, not evidence that any candidate
satisfies R5.

**Common recovery principles proposed for all forms:** human-only trigger
(no autonomous process may declare "recovered"); every verification step
terminates outside the ordinary online stack (R2) and treats the
compromised chain's current self-attestation as untrusted by default;
restores at minimum the Tier 1 axioms + Ethical_Constraints hard floors;
the recovery event itself is logged offline, never written by the
compromised chain.

**Candidate 1 — Signed constitutional snapshot + GPG (offline media).**
Seven-step hypothesized path: declare recovery (human-only, logged
offline) → retrieve the offline media (air-gapped, no network transfer)
→ independently verify the signature *and separately* the key-to-ceremony
binding (a valid signature proves possession of a private key at signing
time, not that the key belongs to the legitimate Human Governing
Authority — those are different claims requiring independent evidence)
→ extract the reference state, distinguishing a hash tree (integrity
reference only) from actual recoverable content (a hash-only artifact
requires a separately held, independently bound text copy for full
restoration) → rebuild in a quarantined environment via air-gapped
transfer only → re-admit nodes only after they demonstrate consistency
against the restored reference, explicitly not conflating "constitutional
consistency" with "full system integrity" (EL-006/cluster-admission
claims are separate and undischarged by a constitutional-hash match)
→ close the event with an offline record. Four explicit outcomes at each
verification step: Proceed / Abort (possible R6) / Insufficient Evidence
(verification or provenance claims can't be established — path
incomplete, not affirmatively failed) / Abort (procedural). Forbidden
actions explicitly listed: treating a valid signature as proof of
authority without independent key-to-ceremony binding; treating a
hash-only snapshot as recoverable content; asking the online chain to
confirm its own integrity; equating air-gapped with trustworthy (air-gap
removes a network path, it does not establish that the workstation,
reader, media, key, or operator procedure is trustworthy); equating
constitutional consistency with full node integrity; autonomous recovery;
using a non-integrable device class as the recovery root.

**Candidate 2 — EEPROM/OTP write-once + human-ratified hashes.** Similar
shape; critical caveat carried through explicitly: pure hash-only OTP is
insufficient for full text restoration unless a separately held offline
text copy bound to that hash also exists — the OTP and the offline text
record must be treated as one logical anchor, not two independent ones.

**Candidate 3 — Offline HSM/smartcard.** Dual-control physical retrieval
and authentication; the HSM either verifies a presented known-good
snapshot or re-signs a restored one under human authorization. Strong
R1/R2 separation when procedures hold; main risks are salvage
availability/cost and single-point physical loss.

**Candidate 4 — Multi-operator physical validation tokens (PAT-002
style).** Least specified of the four — no concrete recovery procedure
can be hypothesized yet without a defined ceremony and threshold rule for
how many tokens must be present to authorize restoration. Longer-horizon
candidate, not ready for a matrix cell beyond "Needs HITL / ceremony
design."

**Explicitly out of scope for all forms:** any recovery step that asks
the currently-running online chain to confirm its own integrity; treating
a locked vendor secure-boot MCU as a recovery root; relying solely on
RIP-001's GPG-signed Git tags without a dedicated offline anchor and
human-controlled recovery path (RIP-001 is a useful existing substrate,
not itself a complete external root-of-trust); autonomous or
agent-initiated recovery.

### Stint disposition

Class B+D. Output: exploratory Proposed/Placeholder recovery hypothesis
for Candidate 1, plus framing (not execution) of the full matrix and
recovery-hypothesis sketches for Candidates 2–4. **No candidate
selected.** Skeptical review (ChatGPT) already applied to Candidate 1's
checklist and materially improved it — see the corrections named above,
all incorporated. Recommended next artifact: actually build and fill in
the R1–R6 × candidate matrix (not yet done — only its shape exists),
using Candidate 1's checklist as supporting detail for that candidate's
R5 cell, not as a pre-decision about which candidate wins.

---

**Update 2026-09-16 (to the Disposition section above):** Part 5 added —
matrix framing and R5 recovery-procedure hypotheses for the four
non-rejected candidate forms. Claude verified R1–R6's live wording and
RIP-001's GPG-signed release-tag substrate against
`Admin/Security_Protocols.md` and `Admin/Repository_Integrity_Protocol.md`
before filing; both matched exactly. Still no candidate selected, still
no matrix actually filled in — that remains the next stint for whenever
someone picks this back up.

---

## Part 6 — R1–R6 × candidate matrix filled, and Candidate 1's
Conditional cells deepened (added 2026-09-17, Class B+D stint)

Continuation of Part 5. The matrix Part 5 only sketched the shape of is
now filled in for the first time. **No candidate selected. SEC-007b
remains Open / Decision Drafted.**

### Matrix result (summary — full cell-by-cell table in session record)

Scoring vocabulary: Pass / Conditional / Fail / Needs HITL.

| Candidate | Pattern | Primary blockers |
|---|---|---|
| 1. Offline signed snapshot + GPG (RIP-001 substrate) | Mostly Pass/Conditional, no Fail | Key-to-ceremony binding; clean rebuild environment; media identity controls; hash-vs-content distinction if hash-only |
| 2. EEPROM/OTP write-once + hashes | Similar to 1; strong R1/R6 if write-once is real | Must prove true write-once; must pair with a separately bound text copy |
| 3. Offline HSM/smartcard | Strong R1/R2/R4; Conditional R5/R6 | Salvage availability, single-point physical loss, ceremony complexity |
| 4. Multi-operator physical tokens (PAT-002) | All Conditional | Ceremony, threshold rules, binding, recovery procedure all undefined |
| 5. Vendor secure-boot locked MCUs | Multiple Fails | Conflicts with Logic-Zero and non-integrable-class doctrine (confirmed live in Electronics.md), wrong control plane |

**No candidate earns an unqualified Pass across all of R1–R6.** Candidate
5 can be set aside for the constitutional-anchor role without further
work. Candidates 1 and 2 are the closest near-term paths; both stay
Conditional on R5 (and parts of R2/R6) for the exact reasons Part 5's
checklist surfaced: signature ≠ authority, hash ≠ content, air-gap ≠
trustworthy environment, constitutional consistency ≠ system integrity.

### Candidate 1 deepening — Conditional cells expanded into concrete open questions

No cell was upgraded to Pass by this deepening; it confirms why the
Conditional scores were earned and makes each gap concrete enough to
attack.

**R2 (Independence):** the load-bearing gap is the key-to-ceremony
binding — a valid signature proves possession of a key, not that the key
belongs to the legitimate Human Governing Authority. Four open questions
recorded (how the binding is created/protected at establishment; where
it's stored for recovery-time consultation without trusting the online
stack; what makes a verification environment trustworthy beyond
air-gapping; single-key vs. threshold).

**R3 (Constitutional scope):** Pass for a full-text snapshot; Conditional
only for the hash-only variant, which needs a separately held, bound text
copy. Recommendation: score Candidate 1 against the full-text baseline,
treat hash-only as a stricter sub-case rather than letting the easier
case paper over the harder one.

**R5 (Recoverability):** five concrete dependencies named — key-to-
ceremony binding (shared with R2), a clean rebuild environment
(unbounded, undemonstrated — flagged as the single biggest residual),
matching text if hash-only, physical media identity controls (shared
with R6), and an undefined operator set / dual-control rule for the
recovery steps themselves.

**R6 (Tamper-evidence):** GPG strongly covers content-modification
detection; physical substitution of the media itself is not
automatically covered by cryptography and needs identity/procedural
controls (seals, dual-operator check, custody log) that are presently
only hypothesized, not demonstrated Forge mechanisms.

**Cross-cutting residual named across multiple cells:** key-to-ceremony
binding (R2, R5); clean rebuild environment (R5); physical media identity
controls (R6, R5); full-text-vs-hash-only choice (R3, R5); operator/
dual-control rules (R4, R5, R6).

### A gap this research doesn't cover, worth naming directly

Every Conditional cell touching "operator set," "dual-control," or
"human-ratified" (R4 across all candidates; R2 and R5's binding and
recovery-authority questions) is quietly assuming that "the legitimate
human operator" is a settled question. It isn't — **GOV-006** (override
authenticity validation) is a real, still-Open Unknown, and
`Admin/Governance_Charter.md` explicitly states override authenticity
"remains unresolved... and must not be implicitly assumed." This is the
same category of dependency FL-006's authority half already surfaced and
had to cross-reference rather than silently assume (2026-09-14). SEC-007b's
R4/R5 design work is building recovery ceremonies on top of an operator-
identity question the repository has independently flagged as open. Not
a blocker to continuing the matrix work, but worth tracking explicitly
rather than discovering it later the way FL-006 did — any concrete
ceremony design for Candidate 1 or 3 will eventually need GOV-006
resolved, or will need to state plainly that it's deferring to the same
unresolved assumption GOV-006 already warns against making implicitly.

### Stint disposition

Class B+D. Output: first filled R1–R6 × 5-candidate matrix, plus a full
deepening of Candidate 1's four Conditional cells into concrete,
individually-numbered open design questions. Disposition: matrix
complete; no candidate selected; Candidate 5 eliminated for the
constitutional-anchor role (confirmed against live Electronics.md
non-integrable-class doctrine); Candidates 1–2 remain leading hypotheses
pending their Conditional cells; skeptical review of the scoring
invited but not yet run. New finding: the operator-identity dependency
running through R4/R5's ceremony questions has the same shape as GOV-006,
which is real and still Open — flagged, not resolved, here.

**Next natural steps (not yet started, listed in order of what unblocks
what):** (1) skeptical pass on the matrix scoring itself, same as Part 5
got for the checklist; (2) either deepen Candidate 2's Conditional cells
the same way Candidate 1 was just deepened, or pick one of the two to
carry forward; (3) a tabletop (paper, no hardware) walkthrough of
Candidate 1's Part 5 checklist against a hypothetical compromise
scenario — this is cheap, needs no equipment, and would likely surface
whether the "Insufficient Evidence" outcome triggers more often than the
checklist currently assumes; (4) name GOV-006 explicitly as a soft
dependency in whichever candidate's ceremony design gets picked up next,
rather than letting it surface as a surprise later.

---

## Part 7 — Skeptical pass on the Part 6 matrix, and a tabletop
recovery walkthrough for Candidate 1 (added 2026-09-17/18, Class B+D)

Two stints, filed together. **No candidate selected. SEC-007b remains
Open / Decision Drafted.** Claude verified the load-bearing citation
before filing: Electronics.md's five non-integrable classes
(locked-bootloader MCUs, unknown-provenance secure elements, unknown-
provenance TPMs, opaque-firmware network controllers, SoCs with
undocumented coprocessors) match ChatGPT's citation exactly.

### Skeptical pass on the Part 6 matrix — corrections, not a reversal

The core Part 6 conclusion survives: no candidate earns an unqualified
Pass across all six requirements. But several individual cells and one
framing choice needed tightening:

**Candidate 5 reframed — this is the most important correction.** Part 6
said "Multiple Fails." The sharper distinction: a locked MCU could
arguably satisfy R1 on its own technical merits (the repository can't
rewrite its locked boot mechanism) — so "fails everything" overstates
the case. The decisive issue isn't a string of R-requirement failures,
it's that the trust model conflicts with the ratified Electronics
non-integrable-class doctrine verified above. Corrected framing:
**eliminated from the constitutional-anchor role for Forge-inadmissibility,
not for failing R1–R6 technically.** This preserves a distinction worth
keeping generally: "doesn't satisfy R" and "satisfies some property but
is inadmissible to the Forge" are different findings.

**R4 corrected across every candidate.** Several cells had read as Pass
because a signature, an HSM, or a token scheme technically enforces
*something*. But none of them can establish that the actor behind the
key/device/token is the legitimate Human Governing Authority — that's
the GOV-006 gap Part 6 already flagged, now applied consistently: every
candidate's R4 moves to Conditional/Needs HITL, not just Candidate 1's.

**Candidate 1 R1** softened Pass→Conditional (offline arrangement *can*
satisfy externality; choosing GPG doesn't make it automatic).
**Candidate 2 R6** softened from "strong if write-once is real" to
Conditional — immutability and substitution-detection are different
properties; a write-once device can still be physically swapped for
another.

**"Offline" elevated from a Candidate 1 note to a matrix-wide rule:**
air-gap ≠ trustworthy verification environment; offline media ≠
authentic physical anchor; a valid signature ≠ legitimate authority.
All three distinctions apply to every candidate that uses any of those
mechanisms, not just the one where they were first noticed.

**"Strongest" language softened.** Not "Candidate 1 is the strongest
solution" but "Candidate 1 currently has the clearest low-hardware path
to a complete recovery hypothesis; Candidate 2 has potentially strong
physical immutability properties but requires a separately bound
recoverable text record." Neither is demonstrated complete.

**Candidate 4** — resisted letting PAT-002's existing mention of
multi-operator tokens make this candidate look more developed than it
is. PAT-002 is Decision Drafted, not a ratified implementation;
mentioning the concept isn't the same as having a working design.
Candidate 4 still needs token-to-anchor binding, operator legitimacy,
threshold rules, revocation, recovery procedure, and substitution
detection before it can be scored past all-Conditional.

**Disposition:** matrix survives adversarial review with scoring-language
corrections, no reversal. No candidate selected; no Security_Protocols
body change; no SEC-007b Status advancement.

### Tabletop recovery walkthrough — Candidate 1, exercised against a hypothetical

Pure paper exercise, zero hardware cost, run against the Part 5
checklist. Scenario: Tier 1 files diverge from last known-good hashes,
online GPG signatures still verify against keys the online keyring
presents as valid, no operator claims authorization, SEC-009-style
compromise signals present. Human Governing Authority declares the
online chain untrusted and initiates Candidate 1 recovery.

**Result: the hypothesized path does not currently produce a successful
recovery.** It repeatedly terminates in *Insufficient Evidence* — not as
an edge case, but as the dominant outcome — at exactly the points the
matrix predicted: key-to-ceremony binding (§0.3, §3.2) is unresolved
before recovery even starts; physical media identity/anti-substitution
controls (§2) were never established at creation time; verification-
environment trustworthiness (§3.3) can't be shown beyond "it's
air-gapped"; a clean rebuild environment (§0.5, §5) doesn't exist and
inherits the same open questions if built ad hoc. The one step that
cleanly reached Proceed on its own terms was extracting a full-text
reference (§4) — the hash-only sub-variant would have hit Insufficient
Evidence here too. Re-admission (§6) was never cleanly reached because
earlier gates weren't cleared; the constitutional-consistency vs.
system-integrity distinction held conceptually but had nothing to test
it against in this run. Honest closure (§7): recovery attempted,
signature verified, but binding/media-identity/environment-trust/clean-
rebuild could not be established — online chain remains untrusted, no
node re-admission authorized.

**This is a successful research outcome, not a failed candidate.** The
procedure was concretely testable on paper, and it correctly surfaced
that Insufficient Evidence is the common case for this hypothesis as
currently specified, not a rare edge condition. It does not prove
Candidate 1 impossible, does not select or reject it, and does not close
SEC-007b — it confirms the Part 6/skeptical-pass Conditional scores were
earned rather than being cautious hedging.

### Stint disposition

Class B+D, two stints filed together. Skeptical pass: matrix corrected,
survives. Tabletop: Candidate 1's recovery hypothesis is executable as a
decision tree but currently terminates in Insufficient Evidence at
multiple load-bearing steps — no successful recovery demonstrated in
this run. **No candidate selected. SEC-007b Status (Open) and PAT-002's
lineage (Decision Drafted) unchanged.**

**Cheapest next tests, if this thread continues (all paper-only, no
hardware):** (1) define a minimal key-to-ceremony binding record format;
(2) define minimal media identity/custody rules; (3) bound what "clean
rebuild environment" means at v0, even narrowly. **Alternative:** pause
SEC-007b design work here — both it and EL-006 are Open/Critical/Blocking
and ultimately gated on hardware that doesn't exist yet; this thread can
continue producing well-reasoned research indefinitely without ever
closing, and that's worth naming plainly rather than treating each new
stint as automatic progress toward resolution.
