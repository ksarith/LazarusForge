# EL-006 ↔ SEC-007 lean binding-principles draft — session transcript

**Filed 2026-09-15.** This is a preserved record of design discussion, not
doctrine and not a body-text insertion. Produced 2026-09-14 by a
Copilot → Grok → ChatGPT → Grok review chain (Copilot's original
over-specified 5-anchor protocol was rejected; Grok redesigned lean;
ChatGPT's skeptical pass found the redesign sound but surfaced a real
cross-file discrepancy, now tracked as **CF-006**; Grok revised
accordingly). The two actionable outputs of that chain — **CF-006**
(`Admin/Security_Protocols.md`) and the **v0 Logic-Zero Run Sheet**
(`Operations/Electronics.md`, Firmware Trust Doctrine) — were
incorporated into the live tree 2026-09-14/15 after independent
verification. This binding-principles draft itself was explicitly
held out by its own authors' final disposition ("remain Proposed /
ready for re-verification — not insert yet") and by a second review
2026-09-15, on the reasoning that P1–P6 below mostly restate
boundaries CF-006 + the run sheet + EL-006 + SEC-007a/b already
enforce individually — a third formal subsection would risk parallel
prose without new Payment via Specification. Filed here so the
thinking isn't lost and isn't mistaken for doctrine. Available as
reference if SEC-007b or node-admission language is revised in the
future.

---

### Proposed — lean EL-006 ↔ SEC-007 binding principles

*(Revised 2026-09-14 after ChatGPT skeptical pass. Evidence grade:
Analogous / Placeholder where noted. Does not close EL-006 or
SEC-007b.)*

---

### Purpose

State the minimum cross-layer principles connecting:

- `Operations/Electronics.md` — Firmware Trust Doctrine + **EL-006** (Open, Blocking)
- `Admin/Security_Protocols.md` — **SEC-007a** (Ratified) + **SEC-007b** (Open physical realization)

without inventing protocols the live files do not support, and without
collapsing three different questions into one mechanism.

---

### Three levels (do not collapse)

| Level | Question | Home |
|-------|----------|------|
| 1. Component recovery | Can we establish the **current v0 firmware-trust condition**? | Electronics.md (Logic-Zero → hash → provenance log) |
| 2. Node authentication | Has this **node** satisfied admission requirements? | Security_Protocols.md (identity / cluster admission) |
| 3. Root of trust | What ultimately **anchors** the authority that says something is trusted? | SEC-007a (constitutional) / SEC-007b (physical, Open) |

Copilot-style "one giant firmware trust mechanism" is rejected. This
draft only addresses Level 1 principles and their link to Level 3 —
not a full node-admission redesign.

---

### 1. Problem (live)

Physical recovery of a chip does not guarantee integrity of its
embedded logic. Electrical PASS ≠ firmware trust.

**Current v0 floor** (Electronics Firmware Trust Doctrine):

1. Identify programmable device
2. Full flash erase (confirm success)
3. Reflash known-good Forge firmware from verified source
4. Verify flash hash before integration
5. Log provenance (device ID, donor board, wipe date, firmware version, operator)

Locked-bootloader / non-wipeable devices → material recovery only; do
not bypass locks in Forge context.

**Known gap (EL-006):** Hash verification of a compromised "known-good"
image still matches. Hash is interim, not a full root-of-trust. Full
cryptographic signing + hardware key storage + external root-of-trust
remains the v1+ target.

---

### 2. Current-state limitation *(required reading)*

The Forge presently has an **interim firmware-trust procedure**, not a
complete external root-of-trust implementation.

Successful Logic-Zero wipe, hash verification, and provenance logging
establish **compliance with the current v0 procedure**; they do **not**
prove that the source image itself is uncompromised.

EL-006 therefore remains **Open / Blocking** pending the conditions in
its Resolution Path (including validation against first MCU batch for
any promotion of practice grade, and v1+ cryptographic infrastructure
for full resolution).

Do not read: wipe → hash → log → PASS as "trusted firmware."

---

### 3. Constitutional floor (SEC-007a — already ratified)

An external root-of-trust must satisfy the ratified requirements
(R1–R6) that break circular self-certification: the anchor must not be
modifiable through the system it anchors.

This draft does **not** restate or extend R1–R6. Any future
firmware-signing or provenance-signing design must terminate in an
anchor that meets SEC-007a.

**Physical form of that anchor is SEC-007b — still Open.** No HSM,
smartcard, EEPROM, or multi-operator token design is adopted here.

---

### 4. Binding principles (proposed)

Design constraints for when SEC-007b and EL-006 implementation
advance — **not** current operational procedures beyond the existing
v0 list.

| # | Principle | Notes |
|---|-----------|--------|
| **P1** | **Firmware trust terminates outside runtime** | Keys or anchors that authorize "known-good" images must not be alterable by salvaged controllers, network nodes, or Forge application software under review. *Proposed / future constraint — mechanism = SEC-007b; not current implementation.* |
| **P2** | **v0 remains mandatory until v1+ exists** | Logic-Zero wipe + hash + provenance log stay required. This draft does not weaken v0. |
| **P3** | **Provenance log is evidence, not proof of honesty** | The log records what was claimed (device, donor, wipe, hash, operator, time). It does not prove the operator or image were uncompromised. *(Epistemic alignment with record-integrity discipline.)* |
| **P4** | **v0 completion ≠ cryptographic trust; failure/uncertainty does not authorize integration** | Completion of the current v0 firmware-trust procedure establishes the **documented interim condition** required by existing Electronics doctrine; it does **not** establish cryptographic root-of-trust. Failure or unresolved uncertainty in the applicable firmware-trust procedure does **not** authorize integration; use Hold or the existing non-integrable / material-recovery path as applicable under current owning-file rules. *No new Decision Point predicates are inserted by this draft — see §6.* |
| **P5** | **No silent promotion of trust grade** | Interim hash verification must not be labeled Measured cryptographic trust. EL-006 stays Open/Blocking until Payment via Specification conditions in its Resolution Path are met. |
| **P6** | **Changes to firmware-trust rules require explicit ratification** | Weakening wipe, hash, or non-integrable-class rules is a deliberate change, not an operational convenience. Uses **existing** governance / human authority paths — no new ratification machinery. |

---

### 5. Explicit non-claims

This draft does **not**:

- Define certificate hierarchies, key ceremonies, or product choices
- Assert that GMP-004, DV-001–006, or network sync already enforce firmware provenance
- Close EL-006, SEC-007b, GOV-006, or any FL-*
- Replace or extend SEC-007a R1–R6
- Insert new routing rows into Forge_flow Decision Point Contracts
- Silently "fix" Security_Protocols language that may overstate Electronics capability

---

### 6. Routing language — deferred

A future, verified mapping of firmware-provenance outcomes onto
Decision Points / Oversight State may be appropriate. It is **not**
included as insertable text here.

Before any such insertion: confirm whether firmware provenance is an
input to Decision Point evaluation, a Gate_02/Electronics precondition,
or both — against live Forge_flow and Gate_02 correspondence. Avoid
creating a cross-layer dependency that is not implemented anywhere.

---

### 7. Pre-existing discrepancy — now CF-006, resolved location

`Admin/Security_Protocols.md` contained language requiring
"signature-verified bootstrap load per Electronics.md doctrine," which
overstates Electronics.md's actual v0 hash-based floor. This was
registered as **CF-006** in `Security_Protocols.md`'s Auditor Notes
2026-09-14, with a four-part Resolution Path. Not fixed here or there
without provenance review, per this draft's own original discipline.

---

### 8. Relationship to open Unknowns (as of drafting)

| ID | Interaction |
|----|-------------|
| **EL-006** | Remains Open/Blocking. Principles only; does not satisfy first-batch validation or v1+ crypto. |
| **SEC-007b** | Remains Open. Physical anchor required before P1 is operational. |
| **GOV-006** | Unchanged (operator-identity residual; relevant to Oversight State / FL-006, not solved here). |
| **FI-2** | P4's "uncertainty does not authorize integration" is an application of existing Hold discipline, not a new invariant. |

---

### 9. Disposition history

- **2026-09-14:** ChatGPT's skeptical pass — "ready for the next skeptical
  pass, not ready for adoption." Recommended sequence: log the
  Security_Protocols discrepancy first (not repair), draft the v0 run
  sheet, resolve verified-source/hash/success-criteria ambiguity, keep
  first-batch criterion contextual, execute when hardware exists, only
  then consider Analogous promotion, leave EL-006 Open/Blocking
  throughout.
- **2026-09-14/15:** Claude incorporated the two ready, actionable
  pieces (CF-006, run sheet) into the live tree after independent
  re-verification of the chain's central factual claim. This
  binding-principles draft itself was held out, per the chain's own
  disposition.
- **2026-09-15:** Grok reviewed the incorporated state, confirmed CF-006
  and the run sheet as clean, and recommended this draft be filed as a
  transcript rather than inserted as a third formal subsection — P1–P6
  mostly restate boundaries the two live artifacts already enforce
  individually. Filed here on that recommendation.

**Next real work**, per this chain's own account: CF-006's Resolution
Path (establish provenance of the signature-verified phrase, identify
dependents, owner decision), then hardware availability for the run
sheet's first-batch validation.

**Update 2026-09-15:** CF-006 resolved. Grok investigated provenance
(2026-05-26 abandoned-path entry + this file's own Drift Indicators
both pointed to mistaken/aspirational language, not deliberate
policy); James ratified Option A. `Security_Protocols.md`'s two
operative sentences now state the actual v0 floor, with
signature-verified bootstrap named as the v1+ target contingent on
SEC-007b. Remaining open item from this chain: hardware availability
for the run sheet.
