# Experiments.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Stub                                                                |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | `Admin/Verification_Gates.md`                                    |
| Last Audit       | 2026-06-21                                                          |
| Auditor          | Claude — Synthesizer                                                |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Structured falsification records for specific PROVISIONAL claims requiring physical grounding
- The institutional mechanism by which PROVISIONAL claims become VERIFIED in the Forge's epistemic system
- Pass/fail criteria for physical tests, sensor reads, material assays, and code execution grounding events
- Linkage between experimental outcomes and Epistemic Ledger entries in owning file sidecars
- The grounding artifact referenced when a claim is promoted from PROVISIONAL to VERIFIED

**This file DOES NOT define:**
- Operational test system specifications (→ `Tests/Living_Waters.md`, `Tests/Trophic_Forge.md`, `Tests/Solar_Descent.md`)
- System-level design validation (→ `Admin/Verification_Gates.md`)
- Unknown tracking or status management (→ `Unknowns.md`)
- Future or speculative experiments without defined method and pass/fail criteria (→ owning file sidecar resolution paths or `Admin/Trajectories.md`)
- Lab notebook or engineering journal content
- Project planning or experiment scheduling

---

## File Purpose

This file is the physical-world complement to the Epistemic Ledger defined in `Admin/Auditor_Protocols.md` §EF-0.3. Where the Ledger records state corrections after reality has spoken, this file records the structured tests that produce those corrections — the falsification events themselves.

Every entry targets a specific PROVISIONAL claim or open unknown in another file. The entry defines the hypothesis, the method, and the criteria by which the outcome constitutes grounding (VERIFIED) or falsification (new unknown or revised PROVISIONAL). When an experiment completes, its outcome feeds an Epistemic Ledger entry in the owning file's sidecar, and the EXP-ID becomes the grounding artifact for any provenance claim.

**The governing constraint from `Admin/Auditor_Protocols.md` §EF-0.8b:** A simulation confirming a simulation is not external grounding. Every entry in this file must specify a method that contacts physical reality — sensor telemetry, material assay, hardware test, or code execution against real tool returns. Internally derived modeling alone does not qualify as an experimental method here.

**Relationship to `Admin/Auditor_Protocols.md` §AP-010:** This file is the institutional coupling layer between the epistemic grounding doctrine (EF-0.8b) and the physical test infrastructure in `Tests/`. AP-010 partially resolves when entries in this file establish documented grounding paths to active test harnesses.

**Honest v0 acknowledgment:** At current maturity, no experiments have been run. This file is a governance stub — its structure and field definitions are established so that when physical testing begins, outcomes are recorded in a form the audit system can consume. Do not treat the absence of entries as evidence that all claims are grounded. The absence of entries means grounding has not yet occurred.

---

## Entry Schema

Each experiment occupies one named section. Five fields required. No entry may be created without a defined Grounding Target, Hypothesis, and Pass/Fail Criteria — entries without these three fields are incomplete and must not be referenced as grounding artifacts.

```
### [EXP-ID] — Short descriptive title

| Field               | Value |
|---------------------|-------|
| Grounding Target    | (Unknown ID or PROVISIONAL claim reference — owning file and section) |
| Hypothesis          | (The specific falsifiable claim being tested) |
| Method              | (Physical test, sensor read, material assay, or code execution — must contact reality) |
| Pass/Fail Criteria  | (What outcome = VERIFIED; what outcome = falsified / new unknown) |
| Status              | (Planned / In Progress / Complete) |
| Outcome             | (VERIFIED / PROVISIONAL / UNKNOWN / Falsified — populate on completion) |
| Ledger Reference    | (EF-0.3 Epistemic Ledger entry ID in owning file sidecar — populate on completion) |
| Date Completed      | (Populate on completion) |
```

**Status values:**
- `Planned` — method and criteria defined; test not yet run
- `In Progress` — test underway; outcome pending
- `Complete` — outcome recorded; Ledger entry created

**Outcome values:**
- `VERIFIED` — claim survived falsification attempt; passes provenance ceiling to Experimentally Verified
- `PROVISIONAL` — partial grounding achieved; uncertainty bounds narrowed but full verification not reached
- `UNKNOWN` — test was inconclusive; insufficient data
- `Falsified` — claim contradicted by physical result; new unknown(s) logged; Epistemic Ledger entry mandatory

---

## Experiments

*No entries yet. File is a governance stub. First entries will be created when physical testing begins on priority unknowns. Candidates for first experiments: CF-001 (hardware watchdog validation), EN-001 (salvaged material safety factors), CE-003 (field polymer identification reliability).*

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| EXP-ASM-001 | Physical testing will precede any specification promotion to Operational Spec | Governance doctrine (EF-0.8b) | High | EF-0.8b amended |
| EXP-ASM-002 | Simulation results alone will not satisfy VERIFIED status for physical claims | Epistemic Anchor (EF-0.0) | High | Axiom Zero amended |
| EXP-ASM-003 | Pass/fail criteria must be defined before an experiment begins — post-hoc criteria invalidate the grounding artifact | Scientific method; Anti-Distortion Clause (EF-0.0 §2) | High | EF-0.0 amended |

---

## Drift Indicators

- Entry added without defined Grounding Target, Hypothesis, or Pass/Fail Criteria
- Outcome field populated as VERIFIED without a corresponding Epistemic Ledger entry in the owning file sidecar
- Method field describes internal modeling or simulation only — no physical contact point
- EXP-ID cited as grounding artifact for a VERIFIED claim but entry Status is still Planned or In Progress
- File begins accumulating speculative future experiments rather than completed or in-progress grounding events
- Ethical Anchor absent or altered

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

*No sidecar unknowns at stub stage. First unknowns will emerge from experimental outcomes.*

---

## Resolution Log

- 2026-06-21: File created as Admin-layer governance stub. Schema defined. No experiments logged. Identified as partial resolution path for AP-010 (physical test harness coupling to epistemic grounding layer). Three priority candidates for first entries noted in Experiments section.
