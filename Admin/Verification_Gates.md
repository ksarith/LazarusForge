# Verification_Gates.md — Canonical Verification Gate Definitions

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Self (this file is the verification reference)                      |
| Last Audit       | 2026-07-10                                                          |
| Auditor          | ChatGPT — Skeptic/Auditor (findings actioned by Claude); Claude — EMS merge integration and VG-002/AP-021 resolution cascade (human-directed), 2026-07-10 |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The six canonical verification gates required for document promotion
- Pass criteria and evidence standards for each gate
- Failure routing and holding logic for each gate
- Full Stop Review trigger conditions
- Gate enforcement rules (sequential requirement, block authority, override
  doctrine)

**This file DOES NOT define:**
- Full auditor role class doctrine — governed by `Admin/Auditor_Protocols.md`
- Full audit sequencing and phase logic — governed by
  `Admin/Auditor_Protocols.md`
- Full Adversarial Challenge Battery — governed by
  `Admin/Auditor_Protocols.md`
- Condensed audit operational reference — governed by
  `Admin/Forge_Audit_Kit.md`
- Cryptographic enforcement of gate passage — governed by
  `Admin/Security_Protocols.md`
- Ethical policy — governed by `Admin/Ethical_Constraints.md`
- Constitutional governance hierarchy — governed by
  `Admin/Governance_Charter.md`

---

## File Purpose

This document is the single canonical source for the six verification gates
of LazarusForgeV0. Every file's `Verification Ref` field in the File State
table points here. The gates defined here are the authoritative versions —
condensed representations in `Admin/Forge_Audit_Kit.md` are derived from
this file and must remain consistent with it.

This file exists to give the gate definitions a stable home that does not
grow with governance doctrine additions, role class expansions, or audit
sequence revisions. The gates themselves should change rarely. When they
do change, this file is the canonical update point, and all derived
representations must be updated to match.

**Derivation note:** Gate definitions are extracted from
`Admin/Auditor_Protocols.md` §Verification Gate Enforcement, which remains
the authoritative governance source. If this file conflicts with
Auditor_Protocols.md, Auditor_Protocols.md prevails until this file is
formally reconciled and the conflict logged.

---

## Assumptions

| ID      | Assumption                                                              | Basis                         | Confidence | Expiry Trigger                                        |
|---------|-------------------------------------------------------------------------|-------------------------------|------------|-------------------------------------------------------|
| ASM-001 | Six gates remain the repository-wide canonical requirement              | Auditor_Protocols.md v0.7     | High       | Gate structure formally revised in Auditor_Protocols  |
| ASM-002 | Gates apply sequentially — no gate may be skipped without documentation | Current governance doctrine   | High       | Sequential requirement formally revised               |
| ASM-003 | This file is derived from Auditor_Protocols.md, not independent of it   | Governance tier structure      | High       | This file elevated to independent governance authority|
| ASM-004 | "Canonical" in this file refers to repository governance intent, not cryptographically enforced implementation | Honest v0 acknowledgment | High | Phase 3 cryptographic enforcement implemented per `Admin/Security_Protocols.md` |

---

## The Six Canonical Verification Gates

*Disambiguation (2026-07-03): "Gate" and "canonical" here refer only to this
file's six Verification Gates — document promotion readiness. Two other
repository uses of "Gate" exist and are distinct: `Operations/Gate_01`
through `Gate_07` (physical material-flow pipeline stages, owned by
`Architecture/Forge_flow.md`) and `Admin/Governance_Charter.md`'s
Enforcement Checkpoints (governance-action legitimacy, renamed from "Gate
1–6" 2026-07-03 specifically to end a naming collision with this section
— see GOV-011 and `Admin/Canonical_Terms.md` §4). A file's `Spec Gates X/6`
File State field always refers to this file's Verification Gates, never
to Enforcement Checkpoints, regardless of which document the field
appears in.*

Gates are sequential. An auditor has binding block authority at each gate.
Self-approval loops are not permitted — an agent may not pass its own output
through a gate it authored. Blocks require documented rebuttal and a
second-pass audit by a different agent to override.

---

### Gate 1 — Fallacy Check

**Test:** Has the Fallacy Checklist been actively applied with substantive
notes?

**Pass criteria:**
- All ten fallacy checklist items applied to specification-level claims
- Substantive notes provided for non-trivial claims (1–2 sentences minimum
  stating what was checked, what nearly failed, and what was adjusted)
- Bare checkmarks without notes do not satisfy this gate

**Fail routing:** Return to author. Document remains at current status.
Gate 1 must be re-applied after revision before proceeding to Gate 2.

*Full Fallacy Checklist: `Admin/Auditor_Protocols.md` §The Fallacy Checklist
| condensed: `Admin/Forge_Audit_Kit.md` §Fallacy Checklist*

---

### Gate 2 — Physical Plausibility

**Test:** Does the document contain any violation of known physical,
engineering, or operational constraints?

**Pass criteria:**
- No claims that violate thermodynamic, mechanical, or material science
  constraints
- Quantitative values labeled with one of the five canonical confidence
  levels defined in `Admin/Auditor_Protocols.md` §Evidence Classification:
  Measured / Replicated / Simulated / Analogous / Placeholder. ("Estimated"
  is retired — see `Admin/Auditor_Protocols.md` AP-021, resolved
  2026-07-10; a claim previously labeled Estimated should be relabeled
  Analogous or Simulated per that section's criteria.)
- Unlabeled numbers treated as Placeholder and flagged
- Analogous-sourced estimates carry documented scaling factors
- **A claim labeled Measured or Replicated must be backed by an evidence
  record meeting the Gate 2 Evidentiary Backing thresholds below** —
  `m_phys ≥ 0.75` for Measured; `m_phys ≥ 0.75` **and** `m_rep ≥ 0.50` for
  Replicated. Simulated and Analogous labels are not yet gated by this
  mechanism (no corresponding vector threshold defined) and remain
  self-asserted, consistent with prior practice, until a future revision
  extends coverage.

**Fail routing:** Return for revision. Specific violations must be
identified and logged. Gate 2 must be re-applied after revision before
proceeding to Gate 3.

---

### Gate 2 Evidentiary Backing — Physical Evidence Vector (active, 2026-07-10)

**Status: active.** Merged in from a standalone Exploration-status proposal (`Admin/Evidence_Management_System.md` v0.2, retired into this file 2026-07-10) after review concluded four of the six gates here have no overlap with an evidence-vector model, but Gate 2 specifically does — its pass criteria previously rested on a *self-asserted* confidence label with no verification mechanism behind it. `Admin/Auditor_Protocols.md` AP-021 resolved 2026-07-10 (five-label Evidence Classification confirmed canonical), unblocking this mechanism per the Gate Definition Synchronization Protocol. Gate 2's pass criteria above now requires it for any Measured or Replicated claim.

**The mapping, now active per Gate 2's pass criteria above:**

| Confidence Label (`Admin/Auditor_Protocols.md` §Evidence Classification) | Proposed Evidentiary Requirement |
|---|---|
| Placeholder | `m_phys = 0` — no evidence submitted |
| Analogous | External comparable system only — no `m_phys` evidence; `m_eng`/`m_math` may be present |
| Simulated | `m_math` or `m_eng` present (computational/procedural model); `m_phys` still 0 |
| Measured | `m_phys ≥ 0.75` — single verified instance; `m_rep` not required |
| Replicated | `m_phys ≥ 0.75` **and** `m_rep ≥ 0.50` — independently repeated, not a single lucky run |

**Architecture (Claims → Evidence → Computed Maturity):** A document does not self-report `m_phys`, `m_rep`, or any vector dimension by direct edit — that reintroduces exactly the self-authorization problem `Admin/Repository_Integrity_Protocol.md` exists to prevent. A document may only submit evidence records (pointers to timestamped, provenance-tagged JSON artifacts); `Automation/AUDIT_HARNESS.py`, if this is ever implemented, would be the sole computer and injector of the resulting vector. See the schemas and reference implementation below, preserved verbatim from the source proposal.

**Evidence record schema (physical):**

```json
{
  "evidence_id": "run_log_leviathan_2026_07_09_14",
  "target_node_id": "node_fa_001_fluid_stratification",
  "timestamp": "2026-07-09T14:22:18Z",
  "provenance": {
    "environment": "RIG-LEVIATHAN-01",
    "operator_or_agent": "agent_gemini_auditor_v1",
    "hardware_signature": "0x3c9a...88ff"
  },
  "instrumentation_metadata": {
    "sensor_id": "THERMOCOUPLE-K-042",
    "last_calibration_date": "2026-05-12",
    "estimated_sensor_drift_per_annum_pct": 0.4,
    "systemic_confidence_interval_pct": 95.0
  },
  "empirical_data": {
    "target_metric": "thermal_equilibrium_temperature",
    "observed_value": 417.0,
    "absolute_uncertainty": 2.0,
    "unit": "C",
    "duration_held_seconds": 3600
  },
  "validation_criteria": {
    "expected_range": "410C to 425C",
    "outcome": "PASS"
  },
  "reproducibility_context": {
    "trial_series_id": "SERIES-PYRO-04",
    "sequence_number": 1,
    "total_consecutive_passes_in_series": 1
  }
}
```

All numeric fields are typed as numbers, never embedded in free-text strings — a naive string-matching evaluator (e.g., checking whether `"±2"` appears in a text field) is trivially defeated by a value like `"±200°C (Not ±2°C)"`, and was an identified vulnerability in an earlier draft of this proposal.

**Reference implementation (preserved, unexecuted — not called by `Automation/AUDIT_HARNESS.py`):**

```python
import math
import datetime
from typing import Dict, Any, Tuple

def calculate_maturity_from_evidence_v2(
    node_metadata: Dict[str, Any],
    evidence_vault: Dict[str, Any],
    lambda_decay: float = 0.05,
    current_time: datetime.datetime = None
) -> Tuple[Dict[str, float], float]:

    if current_time is None:
        current_time = datetime.datetime.utcnow()

    computed = {
        "m_phys": 0.0, "m_exp": 0.0, "m_math": 0.0,
        "m_eng": 0.0, "m_gov": 1.0, "m_ops": 0.0, "m_rep": 0.0
    }

    ledger = node_metadata.get("evidence_ledger", {})

    if ledger.get("mathematical"):
        computed["m_math"] = 0.95
    if ledger.get("engineering"):
        computed["m_eng"] = 0.90

    physical_refs = ledger.get("physical", [])
    total_runs_attempted = len(physical_refs)
    passed_runs = 0
    max_phys_score = 0.0

    for ref in physical_refs:
        run = evidence_vault.get(ref)
        if not run:
            continue
        if run.get("validation_criteria", {}).get("outcome") == "PASS":
            passed_runs += 1
            empirical = run.get("empirical_data", {})
            val = float(empirical.get("observed_value", 0.0))
            abs_unc = float(empirical.get("absolute_uncertainty", float('inf')))
            relative_precision = abs_unc / val if val != 0 else float('inf')

            if relative_precision <= 0.005:
                run_score = 0.90
            elif relative_precision <= 0.02:
                run_score = 0.75
            else:
                run_score = 0.50

            drift_val = float(run.get("instrumentation_metadata", {}).get(
                "estimated_sensor_drift_per_annum_pct", 0.0))
            if drift_val > 1.0:
                run_score *= 0.8

            max_phys_score = max(max_phys_score, run_score)

    computed["m_phys"] = max_phys_score
    if total_runs_attempted > 0:
        computed["m_exp"] = 0.90 * (passed_runs / total_runs_attempted)

    # Reproducibility as a stability-ratio-weighted scale — NOT a raw success
    # count. An earlier draft scored m_rep from passed_runs alone, which let
    # a rig that failed 45 of 50 attempts still score a near-perfect m_rep;
    # this version penalizes low pass fraction directly.
    if passed_runs > 0 and total_runs_attempted > 0:
        stability_ratio = passed_runs / total_runs_attempted
        volume_scale = min(1.0, 0.4 * math.log2(passed_runs + 1))
        computed["m_rep"] = round(stability_ratio * volume_scale, 2)

    ops_reports = ledger.get("operational", [])
    if ops_reports:
        latest = evidence_vault.get(ops_reports[-1])
        if latest:
            ts_str = latest.get("timestamp", "").replace("Z", "+00:00")
            evidence_time = datetime.datetime.fromisoformat(ts_str)
            delta_days = (current_time - evidence_time).days
            computed["m_ops"] = round(0.90 * math.exp(-lambda_decay * delta_days), 2)

    # Governance starts at 1.0 and is degraded by deduction, never
    # auto-granted by the mere presence of a signature field.
    if not node_metadata.get("signature"):
        computed["m_gov"] -= 0.50
    for ref in physical_refs + ops_reports:
        run = evidence_vault.get(ref)
        if run and not run.get("provenance", {}).get("hardware_signature"):
            computed["m_gov"] -= 0.10
    computed["m_gov"] = max(0.0, computed["m_gov"])

    m_effective = min(computed.values())
    return computed, m_effective
```

**What this subsection does not yet do:** it does not mean any file currently claiming "Measured" or "Replicated" has actually been checked against these thresholds — `Automation/AUDIT_HARNESS.py` does not implement `calculate_maturity_from_evidence_v2()` or any evidence-vault loader. The requirement is now live in Gate 2's pass criteria (an auditor applying Gate 2 by hand must check for it), but automated enforcement remains future work. This is the same Phase 0/Phase 1 distinction `Admin/Repository_Integrity_Protocol.md` draws elsewhere: the rule is active and human-checkable; the automation that would check it without a human doing the reading is not.

---

### Gate 3 — Adversarial Challenge

**Test:** Has the Adversarial Challenge Battery been applied proportional
to the document's coupling and risk profile?

**Pass criteria:**
- Full Battery (all ten challenge classes) required when any of the
  following factors are high: irreversibility, coupling, energy density,
  autonomy, silent failure risk, governance authority
- Partial Battery permitted for Exploration-stage documents if deferred
  classes are explicitly documented with rationale and no safety-critical
  claims are present
- Each applied challenge class requires at least one concrete scenario,
  not a general acknowledgment
- Findings from adversarial pass logged as unknowns if not immediately
  resolved

**Hazard-class proportionality:** Thermal, mechanical, and autonomy-bearing
documents require full Battery regardless of document status. Governance-only
documents may defer physical hazard classes where no operational claims
are present — but must document the deferral explicitly.

**Fail routing:** Return for adversarial analysis. Document must undergo
the required Battery classes before Gate 3 can be re-evaluated.

*Full Adversarial Challenge Battery: `Admin/Auditor_Protocols.md`
§Adversarial Audit Layer*

---

### Gate 4 — Scope Alignment

**Test:** Does the document's content fit within the current repository
version scope, or does it belong in a future trajectory?

**Pass criteria:**
- Claimed capabilities are consistent with current version (v0) operational
  reality or explicitly scoped to a defined future version
- No silent capability expansion beyond what the current version can
  demonstrate
- Out-of-scope capabilities explicitly routed to `Admin/Trajectories.md`
  rather than embedded in current-version specifications

**Fail routing:** Route out-of-scope content to `Admin/Trajectories.md`.
Document may proceed once scope is contained to current version or
explicitly trajectory-labeled.

---

### Gate 5 — Cross-Reference Integrity

**Test:** Do all file references in the document resolve to real, committed
files using canonical folder-prefixed paths?

**Pass criteria:**
- All cross-references resolve against the confirmed file list in
  `Discovery.md`
- Canonical folder-prefixed paths used throughout (Admin/, Architecture/,
  Operations/, Tests/) — legacy flat names are not acceptable in new
  contributions
- Aspirational references to files not yet created labeled *planned*
- No hallucinated files presented as confirmed

**Fail routing:** Hold at current status. Each unresolved reference must
be corrected, labeled *planned*, or removed before Gate 5 can be
re-evaluated. Log unresolved references as unknowns if they represent
genuine gaps.

---

### Gate 6 — Conflict Check

**Test:** Does the document contain any contradiction with existing
committed specifications?

**Pass criteria:**
- No direct contradiction with any file at Specification or Hardened
  Doctrine status
- Where apparent conflicts exist, the conflict is explicitly logged as an
  Active Dispute with positions named
- Terminology consistent with `Admin/Canonical_Terms.md` and
  `Architecture/Forge_flow.md` vocabulary standards
- Ethical Anchor field present and matching canonical string exactly

**Fail routing:** Resolve conflict before committing. If conflict requires
negotiation between two specifications, open an Active Dispute in the
relevant file sidecar and escalate to `Unknowns.md` if cross-module.
Document may not advance to Specification status with unresolved
contradictions.

---

## Full Stop Review

A Full Stop Review resets the document to Gate 1 and focuses on
foundational premise re-evaluation. It is not a normal audit cycle — it
is a recognition that something systemic is wrong that incremental gate
passage would not catch.

**Mandatory triggers:**

1. The same foundational claim has been blocked across two separate
   audit cycles
2. A new finding invalidates the core premise of a previously promoted
   Specification
3. A pattern of documented overrides has eroded a governance principle
   without explicit revision to that principle
4. Multiple Adversarial Challenge Battery findings converge on the same
   structural gap

**Invocation record required:**
- Triggering agent identity
- Triggering concern stated as one falsifiable sentence
- Date and document version at time of invocation
- Outcome of the Full Stop Review

Record belongs in the document's sidecar Resolution Log.

---

## Gate Enforcement Rules

**Sequential requirement:** Gates must be applied in order. Skipping a
gate is prohibited unless explicitly documented with rationale. A document
that passes Gate 3 but has not passed Gate 1 has not passed Gate 1.

**Binding block authority:** An auditor's gate block is binding. The
blocked document may not advance until the block is resolved through:
- Revision that addresses the block, followed by re-audit
- Documented rebuttal that demonstrates the block was incorrect, reviewed
  by a different agent

**Self-approval prohibition:** An agent may not apply gates to content it
authored in the same session. Independence is required for gate passage to
be meaningful.

**Override doctrine:** Gate outcomes may be overridden by a human operator.
Overrides must be explicit, dated, include rationale, and record accepted
risk. Undocumented overrides are governance failures. Override rights apply
to gate process decisions — they do not extend to Tier 1 Axiom violations
or Anti-Weaponization doctrine.

**Override retention:** Override records must persist in a reviewable audit
trail location defined by repository integrity doctrine. Deferred to
`Admin/Repository_Integrity_Protocol.md` and `Admin/Security_Protocols.md`
for implementation specifics.

**Repeated override pressure:** Repeated unresolved gate overrides on the
same document trigger mandatory re-audit. Two-cycle unresolved gate disputes
escalate to Full Stop Review consideration.

**Reversibility:** Specification status is reversible. If instability
later emerges in a promoted document, it may be demoted and must re-enter
the gate sequence from the appropriate stage.

---

## Gate Definition Synchronization Protocol

Resolves VG-001. Governs the three-layer chain: `Admin/Auditor_Protocols.md`
(source) → this file (canonical gate-definition layer) → `Admin/Forge_Audit_Kit.md`
(condensed derivative).

1. **Update trigger:** any Resolution Log entry in `Admin/Auditor_Protocols.md`
   touching §Verification Gate Enforcement, §Specification Promotion Rules,
   or §Adversarial Audit Layer requires a same-cycle review of this file for
   consistency. The reviewing agent logs the review in this file's Resolution
   Log even if no change is needed — a reviewed-and-consistent entry, not
   silence, is the evidence the trigger fired.
2. **Reconciliation owner:** whichever agent holds the Skeptic/Auditor role
   for the current audit cycle, per `Admin/Auditor_Protocols.md` File State
   Auditor field. If no Skeptic/Auditor is active that cycle, the trigger in
   item 1 queues until one is assigned rather than being skipped.
3. **Conflict escalation path:** if this file and `Admin/Auditor_Protocols.md`
   are found to define a gate differently, `Admin/Auditor_Protocols.md`
   prevails (per this file's own File Purpose section). The divergence itself
   must be logged as a new row in this file's Active Disputes table within
   the same cycle it is found — corrected silently is not an option, matching
   `Admin/Auditor_Protocols.md` §Dispute Handling Protocol's requirement that
   disputes be tracked explicitly, not left to silently disappear.
4. **Promotion freeze condition:** no file — this one, `Forge_Audit_Kit.md`,
   or any other consumer — may record a Spec Gate as passed using a gate
   definition currently named in an open, unresolved row of this file's
   Active Disputes table. The freeze lifts when the dispute row's Status
   changes to Resolved.

---

## Promotion Requirements Summary

A file may only reach Specification status if all six gates have been
cleared, and:
- All open unknowns are Non-blocking
- Evidence quality supports the certainty level claimed
- Drift indicators are inactive
- Scope boundaries remain stable
- Frozen sections are justified and marked
- Sidecar governance thresholds are compliant (10-entry rule, 20% rule)

Specification is not permanent. Instability discovered after promotion
triggers re-entry into the gate sequence.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                              | What Failed                                                   | What Was Learned                                                                                              | Confidence | Revalidation Needed |
|------------|---------------|-------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-28 | Audit Review  | Gates defined in two places simultaneously (Auditor_Protocols.md and Forge_Audit_Kit.md) | No stable canonical reference; Verification Ref field pointed to nonexistent file | Gate definitions need a stable dedicated home; derived representations must be clearly subordinate to it | Replicated | No                  |
| 2026-05-28 | Audit Review  | First draft claimed Specification/6/6 without audit against existing gate definitions | Draft defined different gates than existing governance system | Self-referential authority claims on first-draft governance files are premature promotion — gates must be verified against source before promotion | Replicated | No |
| 2026-07-03 | Audit Review  | VG-001 (gate-definition synchronization chain) treated as needing new infrastructure | An abstract three-file drift risk had no forcing function until a real near-miss occurred | Naming an existing tracked-disputes mechanism as the enforcement point resolved it — check for reusable existing mechanisms before proposing new tooling for a derivation-chain unknown | Operationally Hardened | No |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### VG-001 — Gate Definition Synchronization Authority Chain Undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Resolved — Discharge via Lessons Learned |
| Risk          | High                            |
| Priority      | Major                           |
| Type          | Governance                      |
| Blocking      | No (Exploration/Draft); Yes (Specification promotion) |
| Owner         | Admin/Verification_Gates.md  |
| First Logged  | 2026-05-29                      |
| Last Reviewed | 2026-07-03                      |

**Description:** The three-layer gate definition chain
(Auditor_Protocols.md → Verification_Gates.md → Forge_Audit_Kit.md)
has no explicit synchronization authority sequence, no drift reconciliation
owner, no conflict escalation path, and no promotion freeze condition for
gate divergence.

**Why It Matters:** Derived governance compression layers accumulate drift
pressure at the derivation boundaries. Without a governed synchronization
mechanism, gate definitions in the three files can silently diverge — each
appearing internally coherent while disagreeing on what a gate actually
requires.

**First concrete incident (2026-07-02):** A gate-scope clarification was
drafted directly into `Admin/Forge_Audit_Kit.md` citing only
`Admin/Auditor_Protocols.md`, because this file was not in context at the
time — the intermediate layer was skipped entirely, exactly as this unknown
predicted. Checked against this file once it became available: the drafted
text turned out to be independently consistent (Gate 3 partial-battery
criteria and Gate 6's textual-contradiction-only scope both matched this
file's definitions, and the Promotion Requirements Summary here already
states the same gates/open-unknowns separation). No actual divergence
resulted, but the near-miss confirms the risk this unknown describes is
live, not hypothetical — it was luck that both derivations landed on the
same reading of Auditor_Protocols.md, not a mechanism that guarantees it.

**Resolution:** Gate Definition Synchronization Protocol added above (2026-07-03),
answering all four items: update trigger tied to Auditor_Protocols.md
Resolution Log entries touching gate-relevant sections; reconciliation owner
set to the active Skeptic/Auditor; conflict escalation routed through this
file's own Active Disputes table per Auditor_Protocols.md's Dispute Handling
Protocol; promotion freeze tied to unresolved Active Disputes rows.
Cross-reference AP-007, GOV-003, RIP-001 (Resolved 2026-06-27) retained as
originally scoped.

**Lessons Learned:** The resolution didn't require new tooling — it required
naming an existing mechanism (this file's own Active Disputes table, and the
Skeptic/Auditor role already defined elsewhere) as the enforcement point for
a problem that looked like it needed a new synchronization system. The
2026-07-02 near-miss was the forcing function: an abstract "these three files
could drift" risk became concrete once an actual citation was drafted against
the wrong layer. Future derivation-chain unknowns should check first whether
an existing tracked-disputes mechanism can serve as the escalation path
before proposing new infrastructure — this is the same pattern RIP-004's
Lessons Learned entry already names for detection-latency unknowns.

---

### VG-002 — Gate 2 Evidentiary Backing merge, blocked on AP-021 — RESOLVED

| Field         | Value                           |
|---------------|----------------------------------|
| Status        | Resolved — Discharge via Specification |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Governance / Technical           |
| Blocking      | No                                |
| Owner         | Admin/Verification_Gates.md   |
| First Logged  | 2026-07-10                       |
| Last Reviewed | 2026-07-10                       |

**Description:** A physical-evidence maturity vector, originally proposed and preserved at Exploration status in a standalone file (`Admin/Evidence_Management_System.md`), was merged into this file as backing material for Gate 2. The confidence-label mapping this backing material depends on cited `Admin/Auditor_Protocols.md`'s five-label Evidence Classification system — but that file defined confidence labels two different, disagreeing ways (`Admin/Auditor_Protocols.md` AP-021).

**Resolves/supersedes:** `Admin/Evidence_Management_System.md`'s EMS-001 (relationship to Spec Gates — resolved by this merge: Gate 2 specifically, not a structural replacement of all six gates) and EMS-002 (GOV-008 misattribution — moot; tracking lived here under this file's own VG- prefix instead).

**Resolution:** AP-021 resolved 2026-07-10 — human governing authority confirmed the five-label Evidence Classification system canonical. Gate 2's pass criteria above updated in the same session to require the mapping table's evidentiary thresholds for any document claiming "Measured" or "Replicated." The mechanism is now live at the human-audit level; `Automation/AUDIT_HARNESS.py` automation of it remains unimplemented — see the Evidentiary Backing subsection's closing note.

---

### Resolution Log

- 2026-08-09: **Filename Track A — `Verification_Gates_LF.md` →
  `Verification_Gates.md`.** `_LF` suffix retired under Repository_Structure
  no-version-suffix rule. All inbound references updated across the tree;
  Rename Registry row added. Content unchanged. Human-directed.

- 2026-07-10: **v0.7 — Gate 2 evidentiary backing activated; VG-002 resolved.** `Admin/Auditor_Protocols.md` AP-021 resolved this same session (human governing authority confirmed the five-label Evidence Classification system canonical). Gate 2's pass criteria updated to require it: Measured claims need `m_phys ≥ 0.75`; Replicated claims additionally need `m_rep ≥ 0.50`. Simulated and Analogous remain self-asserted pending a future revision. The mechanism is live at the human-audit level only — `Automation/AUDIT_HARNESS.py` does not implement the reference calculation or an evidence vault loader; this gap is noted explicitly in the Evidentiary Backing subsection rather than left implicit. Open Unknowns 1 → 0.

- 2026-07-10: **v0.6 — Evidence Management System merged in as Gate 2
  backing material (human-directed).** Reviewed a standalone Exploration-
  status proposal (`Admin/Evidence_Management_System.md` v0.2 — a 7-
  dimensional physical-evidence maturity vector) against all six gates
  here. Found overlap with Gate 2 only — Gates 1, 3–6 test fallacious
  reasoning, hazard battery application, scope alignment, cross-reference
  resolution, and textual contradiction respectively, none of which an
  evidence vector has any mechanism to evaluate. Ruled out full structural
  replacement on that basis. Merged the proposal's schemas, hardened
  reference implementation, and a confidence-label mapping into a new
  "Gate 2 Evidentiary Backing" subsection, explicitly marked proposed and
  inactive. VG-002 logged: the mapping depends on `Admin/Auditor_Protocols.md`'s
  five-label Evidence Classification system, which was found — in the
  course of this same review — to conflict with that file's own four-
  label Fallacy Checklist list (see `Admin/Auditor_Protocols.md` AP-021,
  logged same session). Gate 2's live pass criteria is therefore
  unchanged pending AP-021's resolution, per this file's own Gate
  Definition Synchronization Protocol. `Admin/Evidence_Management_System.md`
  discharged as merged; its EMS-001 and EMS-002 unknowns superseded by
  VG-002. Open Unknowns 0 → 1.

- 2026-05-28: File created (v0.1). Derived from `Admin/Auditor_Protocols.md`
  v0.7 §Verification Gate Enforcement. Corrects first draft (Gemini —
  Engineer/Auditor) which defined six different gates inconsistent with
  existing governance system and claimed premature Specification status.
  Gates now match Auditor_Protocols.md canonical definitions exactly.
  Spec Gates set to 2/6 — G1 (internal coherence) and G2 (physical
  plausibility as a governance document) assessed as passing; G3 through
  G6 require formal audit pass before claiming.
- 2026-05-29: ChatGPT Skeptic/Auditor findings actioned. Gate 3 hazard-class
  proportionality clarification added. Override retention requirement added
  to Gate Enforcement Rules. Repeated override escalation doctrine added.
  ASM-004 (canonical status clarification) added to Assumptions. VG-001
  logged — gate synchronization authority chain undefined. Open Unknowns
  updated 0 → 1. Navigation Anchors block added 2026-06-06.
- 2026-07-02: VG-001 first concrete incident logged — a Forge_Audit_Kit.md
  edit skipped this file entirely (unavailable in session context) and
  cited Auditor_Protocols.md directly. Checked post-hoc: no actual
  divergence, gate definitions matched. Incident recorded as evidence the
  risk is live; resolution path itself unchanged and still unaddressed.
  Forge_Audit_Kit.md's derivation line and gate-note citation corrected to
  route through this file (kit bumped to v1.6). Last Audit still 2026-05-29
  — this was an incident log update, not a full re-audit.
- 2026-07-03: **VG-001 discharged** (Payment via Specification). Gate
  Definition Synchronization Protocol added, answering all four resolution-
  path items by naming this file's own Active Disputes table and the
  Skeptic/Auditor role as the enforcement mechanism rather than proposing
  new infrastructure. Status → Resolved — Discharge via Lessons Learned;
  Resolution and Lessons Learned narrative fields added to the sidecar
  entry per the Resolved Unknown Discharge Procedure (`Admin/Forge_Audit_Kit.md`
  v1.4+). Matching top-table Lessons Learned row added. Open Unknowns 1 → 0.
- 2026-07-03: Disambiguation note added atop §The Six Canonical Verification
  Gates, confirming this file as sole owner of unqualified "Gate"/"canonical"
  terminology within its domain, distinct from Operations/Gate_01–07 (physical
  pipeline, Forge_flow.md) and `Admin/Governance_Charter.md`'s Enforcement
  Checkpoints (renamed from "Gate 1–6" the same day to end the naming
  collision — see GOV-011, `Admin/Canonical_Terms.md` §4).

---

## Abandoned Paths

| Date       | Path                                                           | Why Abandoned                                                                                         | Reconsider? |
|------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-28 | Self-referential Verification Ref field                        | Creates closed loop with no external anchor; field value is now descriptive rather than a file reference | No        |
| 2026-05-28 | Redefining gates differently from Auditor_Protocols.md         | Repository already uses established gate definitions; redefining creates conflicting governance systems | No         |
| 2026-05-28 | Claiming Specification/6/6 on first draft                      | Premature promotion; gates must be audited against source document before any status claim is made     | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Gate definitions diverge from `Admin/Auditor_Protocols.md`
  §Verification Gate Enforcement without a logged reconciliation entry
- Gate numbering or names changed without corresponding update to all
  files using gate references
- Full Stop Review triggers modified without corresponding update to
  `Admin/Auditor_Protocols.md`
- Gate enforcement rules weakened — sequential requirement, block
  authority, or self-approval prohibition removed or made optional
- Promotion requirements summary diverges from
  `Admin/Auditor_Protocols.md` §Specification Promotion Rules
- Verification Ref field in this file changed to point to another file
- Ethical Anchor field absent, altered, or does not match canonical string
- Any gate's fail routing changed to allow advancement without revision
- Navigation Anchors block absent or URLs modified from canonical values

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Relationship to Existing Documents

- `Admin/Auditor_Protocols.md` — Tier 2; source of truth for gate
  definitions; this file is derived from §Verification Gate Enforcement
  there; if conflict exists, Auditor_Protocols.md prevails
- `Admin/Forge_Audit_Kit.md` — Tier 3; carries condensed gate table
  derived from this file; must remain consistent with definitions here
- `Admin/Governance_Charter.md` — Tier 1; gate enforcement rules operate
  within the authority hierarchy defined there; human override doctrine
  applies to gate process decisions per §Human Override Doctrine
- `Admin/File_Template.md` — all repository files point to this file via
  the Verification Ref field in their File State table; this file is the
  resolution target for that reference
- `Admin/Security_Protocols.md` — Phase 3 cryptographic enforcement will
  eventually verify gate passage via commit signing; this file defines
  what is being enforced
- `Discovery.md` — this file is listed in the Admin/ scope map and
  Maturity Snapshot; Suggested Reading Order position: after File_Template.md

---

## Status

Version 0.7 — Gate 2 evidentiary backing activated; requires the physical-
evidence maturity vector's thresholds for Measured/Replicated confidence
claims. Human-audit-level enforcement only; `Automation/AUDIT_HARNESS.py`
automation remains future work (2026-07-10).

**Gate status:** G1 and G2 assessed as passing at Draft stage. G3 through
G6 require formal audit pass against Auditor_Protocols.md before claiming.

**What must remain constant:**

**Gates are sequential. Blocks are binding. Self-approval is prohibited.**

**These gates exist to prevent premature promotion, not to obstruct
legitimate progress.**
