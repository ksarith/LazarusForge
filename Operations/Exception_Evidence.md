# Exception_Evidence.md — Operations/

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
[README.md](../README.md) | [Architecture/Forge_flow.md §1.3 HP-011](../Architecture/Forge_flow.md) | [Admin/Ethical_Constraints.md EC-003](../Admin/Ethical_Constraints.md) | [Operations/Tooling_Inventory.md](Tooling_Inventory.md) | [Tests/Field_Logs.md](../Tests/Field_Logs.md)

---

## File State

| Field | Value |
|-------|-------|
| Status | Proposed — structural home for FL-006 half A (evidence-control specification) |
| Spec Gates | 0/6 |
| Open Unknowns | FL-006-A (structural owner named; population and demonstrated maintenance still open) |
| Body Stability | Volatile — no operational trial against this structure has been run yet |
| Owning Domain | Operations/ |
| Last Reviewed | 2026-09-18 |
| Sidecar Link | `Architecture/Forge_flow.md` FL-006 |
| Ethical Anchor | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md`. |

---

## Scope Boundary

**This file DOES:**
- Define the **evidence classes** Oversight State may consume, the **required fields** for each, **deposit and handoff rules**, **freshness and provenance expectations**, and **pointers to where authoritative records live**.
- Fill the Operations cell in `Architecture/Forge_flow.md`'s HP-011 Transition Ownership table that was empty (FL-006 half A).
- Serve as the control specification and index — what evidence exists, where it comes from, how fresh it is, what epistemic state it has, and who has authority to interpret it.

**This file DOES NOT:**
- Store the entire operational evidence universe. Episodic packet bodies and standing-reference data live in the operational records this file *points to*.
- Define **want/need policy**. Policy lives in `Architecture/Forge_flow.md` (Oversight State's want/need criteria); this file holds facts relevant to the judgment, not the judgment itself.
- Decide **routing, authorization, or Escalate**. Escalate procedure is EC-003 (FL-006 half B, separately owned). Routing is Forge_flow.
- Resolve **GOV-006** or **GMP-004** (identity authentication gaps remain open; they affect who the designated maintainer is, not the structure of this file).
- Replace `Gate_01_Intake.md`, `Gate_02_Triage.md`, or any other gate's own operational procedure. Upstream gates own their procedures; this file owns the evidence-control specification for what they hand off to Oversight.

**Anti-policy rule (explicit):**
> Evidence MUST NOT be treated as a decision, authorization, routing instruction, or policy merely because it appears in or is referenced by this file.
> Evidence ≠ inference ≠ decision ≠ authorization.

This matters especially once autonomous agents operate inside the Forge. An agent reading this file should conclude: "this file tells me what evidence exists, where it comes from, how fresh it is, what epistemic state it has, and who has authority to interpret it" — not "this file authorizes an action."

---

## Roles

| Role | Assignment |
|------|------------|
| **Repository home / control specification** | This file — defines evidence classes, fields, deposit rules, freshness, pointers |
| **Operational maintainer of live records** | Designated Operations role / operator — **pending** (same honesty as `Tooling_Inventory.md`'s empty tables + TI-001) |
| **Oversight routing & want/need policy** | `Architecture/Forge_flow.md` (Oversight State) |
| **Escalate procedure** | `Admin/Ethical_Constraints.md` EC-003 (FL-006 half B — not this file) |

---

## Evidence Class 1 — Episodic Packages

Deposited by upstream gates or human operators when something is escalated to Oversight that requires exception-handling beyond the standard gate flow.

**Upstream depositors (own their procedures; this file owns the control spec for what they hand off):**

| Source | Deposits when |
|--------|--------------|
| `Operations/Gate_01_Intake.md` | Hazard, contamination, or unknown-item escalation at intake |
| `Operations/Gate_02_Triage.md` | Conflicting or insufficient evidence, triage-terminal holds escalated to Oversight |
| Other Operations gates | Gate-specific exception packets when they escalate |
| Human operator / field notes | Cases where a human identifies an exception requiring Oversight that no gate produced |

**Minimum control fields (required for each episodic entry):**

| Field | Description |
|-------|-------------|
| Trigger | What condition or event prompted deposit |
| Source gate / file | Which gate or human deposited this packet |
| Timestamp | When deposited |
| Epistemic label | Per AP-006 / existing two-axis practice (known/unknown × confident/uncertain) |
| Why deposited | Observation or reason for escalation — describes what was seen, **not** a routing recommendation or quasi-authorization |
| Pointer to full record | Path, log entry, case ID, or other locator for the packet body |
| Raw notes (optional) | Brief human-readable context |

The **packet body itself lives in the operational record the pointer names** (case log, `Tests/Field_Logs.md` entry, gate hold record, etc.). This file records the control entry + pointer, not the full dossier. Storing a growing collection of raw event records in this file would make it an operational ledger rather than a control specification — that is not its purpose.

---

## Evidence Class 2 — Standing Reference (Distributed)

Oversight may need ongoing context about resource state, capability, and operational conditions — not a one-time incident packet but maintained reference state. This context is **not centralized here**. This file defines what Oversight may need and where the authoritative source is expected to live.

| Concern | Likely authoritative home | Notes |
|---------|--------------------------|-------|
| Tool / capability availability | `Operations/Tooling_Inventory.md` | Already owned |
| Component / fabrication dependency | Component or fabrication records | Not yet a named file; pending operational maturity |
| Failure rates / empirical trends | Operational telemetry / field records | Pending first operational runs |
| Scarcity / deployment-local resource state | Deployment-local resource records | Per-deployment, not global (same caveat as TI-001) |
| Need-relevant facts | Facts only — **the need judgment stays in Oversight + Forge_flow policy** | This file holds supporting facts; it does not decide need |

When this file is first populated for a given deployment, the operational maintainer should confirm which sources are actually live and update the pointer column accordingly. An empty or unconfirmed pointer is honest; a pointer to a non-existent or stale source is not.

**Do not consolidate all standing data into this one file.** The risk: three agents simultaneously reading one centralized source could treat it as ground truth rather than as a pointer to authoritative records held elsewhere and maintainable independently.

---

## Freshness and Provenance

- Each episodic control entry should carry enough information that a future human or agent can locate the original record and assess whether it is still relevant.
- Standing reference pointers should note when they were last confirmed live (date, by whom if known).
- Stale pointers must be labeled as stale rather than silently left as if current.
- Epistemic labeling follows existing practice (`Admin/Auditor_Protocols.md` AP-006 / the two-axis schema in use elsewhere in this repository).

---

## Maintenance Honesty

Creating this file assigns **structural** ownership only. The following remain open:

| Checkpoint | Status |
|------------|--------|
| Structural owner identified (Operations) | YES |
| Control specification written | YES (this file) |
| Cross-references to HP-011, FL-006 sidecar, Gate_01/Gate_02 | Pending write to those files |
| First operational population of episodic entries | NO |
| First operational confirmation of standing-reference pointers | NO |
| Designated operational maintainer named | PENDING |
| FL-006 half A formally closed | NO — structural owner named; operational demonstration still open |

Empty control entries and unconfirmed pointers are intentional until first population — same pattern as `Tooling_Inventory.md` / TI-001. The absence of data in this file does not mean evidence does not exist; it means the control specification exists and is waiting to be connected to the operational reality of a specific deployment.

---

## Lessons Learned

*(Empty — no operational trial has been run against this structure yet.)*
