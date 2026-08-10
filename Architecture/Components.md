# Lazarus Forge — Components (v0)

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-14 (Gemini 3 Flash — Skeptic/Auditor); revised 2026-06-08  |
| Auditor          | Gemini 3 Flash — Skeptic/Auditor                                    |
| Open Unknowns    | 2                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Component taxonomy for Lazarus Forge v0 through v3
- Classification criteria (Critical, Useful, Bootstrap)
- Bootstrap Doctrine and Graduation Rule
- Dual-use annotation standard for components
- Version mapping by material scope and capability

**This file DOES NOT define:**
- Electronics, software, biological, or optical fabrication systems
- Detailed engineering specifications for any individual component
- Energy infrastructure beyond grid bootstrap minimum
- G.E.C.K. manifest or redundancy stock
  (→ `Architecture/Geck_forge_seed.md`)
- Precision ceiling doctrine, tolerance tiers, or metrology methodology
  (→ `Architecture/Precision.md`)
- Cross-module governance or repository-level unknowns

---

## File Purpose

This file defines the minimum component architecture required for a Lazarus Forge to
function and persist. It answers three questions: what must exist, what helps, and what
can wait. The taxonomy is intentionally narrow — metal fabrication enabling layer only.
If this file disappeared, the Forge would lose its governing classification logic and no
principled distinction could be made between components whose absence causes silent failure
and those whose absence merely degrades performance.

---

## Assumptions

| ID      | Assumption                                                          | Basis                           | Confidence | Expiry Trigger                                            |
|---------|---------------------------------------------------------------------|---------------------------------|------------|-----------------------------------------------------------|
| ASM-001 | Grid power available at v0 bootstrap site                           | Terrestrial deployment context  | Medium     | Off-grid or disaster-zone deployment confirmed            |
| ASM-002 | Human operator present during v0 graduation assessments             | Bootstrap Doctrine v0 condition | High       | Autonomous sensing reaches graduation-detection threshold |
| ASM-003 | Salvage feedstock available in sufficient volume                    | v0 site selection criteria      | Medium     | Feedstock survey contradicts availability                 |
| ASM-004 | Forge loop closes in degraded form with proxy/downgrade substitutions | Bootstrap Doctrine            | Medium     | First loop closure attempt fails in degraded config       |

---

## Definitions

**Critical** — Absence allows silent failure. The Forge cannot detect its own malfunction
without this component. Loss is unrecoverable without outside intervention.

**Useful** — Absence limits the Forge but does not invalidate it. The Forge continues
operating in a degraded state.

**Bootstrap** — A component present at genesis that is expected to fail, be replaced, and
be improved upon. Bootstrap components are critical by function, not by quality.

---

## I. Critical Components (v0)

A component is critical if its absence allows **silent failure** — the Forge operates but
cannot detect that it is operating incorrectly.

### 1. Feedstock Reduction
Shredder, cutter, or mill capable of reducing mixed metal scrap to processable size.
Without this, no material enters the system.

### 2. Atmosphere Control
Enclosure and gas management preventing uncontrolled oxidation, toxic accumulation, or
explosive atmosphere. Without this, thermal processes are unsafe.

### 3. Metal AM / Forming
At least one system capable of producing functional metal parts from Forge output stock.
Without this, the Forge cannot replicate itself.

### 4. Thermal Processing
Controlled heat source capable of melting or sintering target materials. The Spin Chamber
is the v0 implementation.

### 5. Metrology
Measurement capability sufficient to verify output quality. Without this, the Forge cannot
confirm it is producing usable material.

*Metrology verifies output correctness. It is distinct from Baseline Observability, which
verifies system state correctness. A Forge can produce bad parts while mechanically healthy,
or produce good parts while internally degrading. Both failure modes require detection.*

### 6. Baseline Observability
Minimum instrumentation sufficient to detect unsafe process states and internal degradation.
Examples: thermal probes, motor current sensing, airflow monitoring, cameras, encoder
verification. Without this, the Forge cannot distinguish silent drift from normal operation.

*Baseline Observability verifies system state correctness. See Metrology (item 5) for
distinction between the two.*

*Power dependency: Requires stable power to function reliably. Minimum at v0: surge
protection on all sensor and compute circuits. Brownout or spike events that corrupt sensor
state defeat the purpose of this component. See also Artifact Memory (item 7).*

### 7. Artifact Memory
Persistent storage of process parameters, outcomes, and component provenance. Without this,
learning resets every generation.

*Power dependency: Vulnerable to power instability. Minimum at v0: surge protection and
graceful write handling to prevent corruption on unexpected power loss. Corrupted memory
that appears valid is worse than lost memory — a silent corruption is a silent failure.
See Baseline Observability (item 6).*

### 8. Human Override Interface
Physical or digital mechanism for operator intervention at any process stage. Without this,
autonomous failure cascades cannot be interrupted.

---

## II. Useful Components (Capability Amplifiers — Non-Critical)

Absence does not invalidate the Forge, only limits it.

### A. Closed-Loop Recycling
Internal recovery of process waste (slag, failed prints, spent powder). Reduces external
feedstock dependency over time.

### B. Advanced Sensing & Diagnostics
Higher-order monitoring enabling predictive maintenance, autonomous quality assessment, and
process optimization. Presupposes Baseline Observability (Critical item 6). Without the
observability floor, advanced diagnostics have no validated baseline to reason from.

### C. Compute & Autonomy
Decision-making systems above basic threshold logic. Enables reduced human oversight
over time.

### D. Energy Infrastructure
On-site generation, storage, and distribution beyond grid bootstrap. See `Operations/Energy.md`.

### E. Logistics & Transport
Material handling, sorting, and transfer automation. Enables higher throughput.

---

## III. Downstream Systems (Out of Scope v0)

- Electronics fabrication
- Software development environment
- Biological or chemical synthesis
- Precision optics

These emerge through growth, not seeding. They belong in future version taxonomies.

---

## IV. Version Mapping

| Version | Material Scope                | Key Capability Added                         |
|---------|-------------------------------|----------------------------------------------|
| v0      | Aluminum, copper, basic steel | Proof of persistence — the loop closes       |
| v1      | Expanded alloys               | Steel-class materials, closed-loop recycling |
| v2      | Multi-material                | Manufacture of Forge submodules              |
| v3      | Space-grade                   | Regolith and asteroid material processing    |

*v3+ version milestones are trajectory markers — component taxonomy for those stages is
not defined in this document.*

---

## V. Bootstrap Doctrine

**Core principle:** Imperfect beginnings are valid.

A v0 Forge built from salvage, with degraded components and manual oversight, is still a
Forge. The Bootstrap Doctrine establishes:

- Bootstrap components are expected to fail
- Failure is not a defect — silence is
- Every failed bootstrap component is a learning event
- Never auto-delete a failed component record

**Sufficiency criterion:** A component is sufficient if it allows the Forge loop to close.
The Forge loop: intake → triage → process → verify → learn → repeat.
(Loop definition per `Architecture/Geck_forge_seed.md` Section III.)

**Wear and consumables:** Bootstrap components operate under high maintenance cadence.
Blade dulling, nozzle clogging, bearing wear, and similar degradation are expected — not
exceptional. Consumables, wear parts, and tooling redundancy are addressed in the G.E.C.K.
manifest rather than this taxonomy. A G.E.C.K. is considered insufficient if it cannot
support at least one full maintenance cycle for each Critical component. The taxonomy
defines what must exist; the G.E.C.K. ensures it can keep existing.

**Proxy/Downgrade paths:** When a critical component is unavailable at spec, a
lower-capability substitute is acceptable if it allows the loop to close in degraded form.
Document the substitution.

**Graduation Rule:** A component graduates from Bootstrap to Specified when the Forge can:
(1) detect its degradation, (2) repair or replace it internally, (3) improve its successor.

*At v0, graduation assessment uses Baseline Observability plus human operator verification
together as the detection proxy. Baseline Observability (Critical item 6) provides the
minimum instrumentation floor; human operators supply interpretive judgment above that floor.
This is a defined v0 operating condition, not a gap. See CO-001.*

---

## VI. Dual-Use Annotation Standard

Components with known dual-use potential are annotated:

| Risk Level | Meaning                             | Action                                        |
|------------|-------------------------------------|-----------------------------------------------|
| Low        | Minimal weaponization potential     | No special handling                           |
| Medium     | Dual-use possible with modification | Log provenance, flag if pattern emerges       |
| High       | Direct weaponization path exists    | Full Stop — route to Ethical_Constraints.md   |

*No component in the current v0 taxonomy is rated High. High rating is expected to appear
in downstream capability documents (Leviathan chassis, remote autonomous systems). Its
absence here reflects current component scope, not a judgment that no Forge-adjacent
capability warrants it.*

---

## VII. Operating Principle

> A component is critical if its absence allows silent failure.

This single sentence governs all classification decisions. When in doubt, ask: if this
component fails, does the Forge know?

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|----------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review | Graduation Rule written without acknowledging detection dependency | At v0, Advanced Sensing is Useful not Critical — Forge may not detect its own component degradation | Human operator verification must be explicitly named as v0 proxy for automated detection | Anecdotal | No |
| May 2026 | Audit Review | Metrology and observability treated as a single category | Output verification and system-state verification are distinct failure modes | Split into two Critical items; distinction noted explicitly in both entries | Anecdotal | No |
| May 2026 | Audit Review | Power conditioning omitted from critical component notes | Brownout or surge can corrupt Artifact Memory and defeat Baseline Observability | Added power dependency notes to items 6 and 7; minimum: surge protection at v0 | Anecdotal | No |
| May 2026 | Audit Review | Wear and consumables left implicit in Bootstrap Doctrine | "Expected to fail" did not address maintenance cadence or redundancy location | Routed consumables and spare parts to G.E.C.K. manifest as designated redundancy path | Anecdotal | No |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### CO-001 — Graduation Rule detection circularity at v0

| Field         | Value                         |
|---------------|-------------------------------|
| Status        | In Progress                   |
| Risk          | Low (downgraded from Medium)  |
| Priority      | Major                         |
| Type          | Architectural                 |
| Blocking      | No                            |
| Owner         | Components.md                 |
| First Logged  | 2026-05-04                    |
| Last Reviewed | 2026-05-14                    |

**Description:** The Graduation Rule requires degradation detection, but at v0 Advanced
Sensing is Useful not Critical — creating a potential circularity in when graduation
can be assessed.

**Why It Matters:** Without a defined detection floor, graduation decisions at v0 have no
principled basis and could be made incorrectly or silently deferred.

**Resolution Path:** Two-part resolution applied: (1) Baseline Observability added as
Critical item 6 — minimum instrumentation floor distinct from Advanced Sensing. (2)
Bootstrap Doctrine updated — graduation at v0 uses Baseline Observability plus human
operator judgment together as the proxy. Remaining: same note should be added to
`Architecture/Forge_flow.md` Bootstrap Doctrine reference. UNK-026 in `Unknowns.md` should
be updated to reflect partial resolution.

*Cross-module reference: UNK-026 in `Unknowns.md`*

---

### CO-002 — Metrology Precision Thresholds

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Low           |
| Priority      | Minor         |
| Type          | Technical     |
| Blocking      | No            |
| Owner         | Components.md |
| First Logged  | 2026-05-14    |
| Last Reviewed | 2026-05-14    |

**Description:** The minimum viable dimensional tolerance for a bootstrap part to be
considered functional enough to continue the loop is not yet defined.

**Why It Matters:** Without a tolerance threshold, Metrology has no falsifiable pass/fail
criterion — the Forge cannot confirm loop closure with confidence.

**Resolution Path:** Payment via Specification — define minimum acceptable tolerance per
material class and part category at v0. Defer precise values to first fabrication trials;
tolerance requirements emerge from actual loop closure attempts, not pre-specification.

---

### Resolution Log

- May 2026: Bootstrap Doctrine updated — sufficiency criterion linked to Forge loop definition in geck_forge_seed.md. Human proxy for graduation detection added explicitly.
- May 2026: v3+ trajectory marker note added to Version Mapping table.
- May 2026: Dual-use annotation note added explaining absence of High-rated components.
- May 2026: Metrology and Baseline Observability split into separate Critical items (5 and 6). CO-001 partially resolved — detection circularity addressed structurally.
- May 2026: Power conditioning notes added to items 6 and 7. Gemini Gate 1 blocker cleared.
- May 2026: Wear and consumables note added to Bootstrap Doctrine. G.E.C.K. named as redundancy path. Gemini Gate 1 blocker cleared.
- May 2026: CO-002 logged per Gemini audit finding.
- May 2026: File retrofitted to canonical LF_File_Template structure. File State, Scope Boundary, File Purpose, Assumptions, Active Disputes, structured unknown tables, and Abandoned Paths added.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from
  `Verification_Gates.md` to `Admin/Verification_Gates.md` (PC-001). Scope
  Boundary updated — `Architecture/Geck_forge_seed.md` backtick path corrected;
  `Architecture/Precision.md` added as precision ceiling doctrine owner (PC-003).
  Section IID `energy_v0.md` corrected to `Operations/Energy.md`. Section V loop
  reference corrected to `Architecture/Geck_forge_seed.md`. CO-001 sidecar stale
  filenames corrected: `Lazarus_forge_v0_flow.md` → `Architecture/Forge_flow.md`,
  `Unknowns_LF.md` → `Unknowns.md`. Owner fields corrected to
  `Architecture/Components.md`.

---

## Abandoned Paths

| Date     | Path | Why Abandoned | Reconsider? |
|----------|------|---------------|-------------|
| May 2026 | Classifying Advanced Sensing as Critical to satisfy Graduation Rule detection requirement | Creates autonomy inflation — requires AI-grade sensing at v0, defeating bootstrap realism. Baseline Observability is the correct Critical floor. | No |
| May 2026 | Single combined Metrology/Observability category | Output verification and system-state verification are distinct failure modes. Merging them allows a Forge to confirm good parts while internally degrading without detection. | No |
