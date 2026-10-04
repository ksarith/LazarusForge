# Run Card — Lane B: Logic-Zero / EL-006 admission (v0)

**Source doctrine:** `Operations/Electronics.md` — Firmware Trust Doctrine +
**v0 Logic-Zero Run Sheet** (Proposed/Placeholder).  
**Evidence destination:** new file `FL-YYYYMMDD-logiczero-<mcu-or-board>.md` in this folder; register in `Routing.md` same pass.

**Explicit non-claims:** One Outcome S does **not** close EL-006, establish
cryptographic firmware trust, or generalize beyond the declared device context.

---

## Preconditions (do not start if P3–P5 blank)

| # | Item | Fill |
|---|------|------|
| P1 | Device — MCU family/package, intake Device ID | |
| P2 | Donor board ID (or "unknown donor") | |
| P3 | Known-good image — filename/version/source + who approved | |
| P4 | Expected hash — **SHA-256**, scope (full-chip default), hex | |
| P5 | Tools — programmer model + erase/write/read-back/hash software | |
| P6 | Operator ID | |
| P7 | Date/time (UTC) | |

Provisional defaults (Placeholder until first designation): SHA-256 full-chip;
image naming `KG-<MCU-family>-<purpose>-YYYYMMDD-<short-hash>.bin`.  
If P3–P5 cannot be filled → **Outcome B** (blocked), not a device fail.

---

## Procedure

1. Identify programmable (else **Outcome L** — material recovery only; no bypass).
2. Full erase — success criteria declared **before** run (programmer mass-erase + blank-check/read-back).
3. Reflash **only** the P3 image.
4. Verify hash against P4.
5. Complete provenance log: Device ID, Donor Board, Wipe Method, Firmware Hash, Operator, Timestamp.

---

## Outcome (circle one)

| Code | Meaning | Integrate? |
|------|---------|--------------|
| **S** | All steps succeeded; log complete | Yes under v0 triage — *procedure-complete only* |
| **F** | Fail erase/reflash/hash or incomplete log | No — Hold/scrap per Electronics rules |
| **L** | Locked / non-wipeable | Material recovery only |
| **B** | Blocked before start (P3–P5 missing) | N/A — fix preconditions |

**First-batch rule (EL-006 Payment path):** Outcome S must cite exact P3/P4/P5 and
state generalization limits (e.g. "STM32F103 only").

---

## Field_Logs paste block (after run)

```
**Entry ID:** FL-YYYYMMDD-logiczero-<slug>
**Status:** Unreviewed

- **Submitted by:**
- **Run type:** Logic-Zero admission / EL-006 v0 floor
- **Hardware:** (P1–P2, P5)
- **Agents:** none required
- **What was attempted:**
- **What actually happened:** (outcome S/F/L/B + step that failed if any)
- **Evidence label:** Measured | Analogous | Placeholder
- **Relevant Unknown IDs:** EL-006 (and CF-006 only if relevant)
- **Provenance log fields:** Device ID / Donor / Wipe method / Hash / Operator / Timestamp
- **Generalization limit:** 
```
