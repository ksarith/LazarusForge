# Resolution_Methodology.md

**Version 0.1 — 2026-08-15**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Active — Reference                                                  |
| Body Stability   | Transitional                                                        |
| Spec Gates       | N/A — this file is a named reference for demonstrated patterns, not a specification or gate |
| Verification Ref | Admin/Verification_Gates.md                                         |
| Last Audit       | 2026-08-15                                                          |
| Auditor          | Grok — human-directed draft from 2026-08-15 session patterns        |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | N/A                                                                 |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- A short, citable set of resolution patterns that the 2026-08-15 Operations / Governance session demonstrated repeatedly and that produced durable architectural outcomes rather than restated gaps.
- The distinction between paper-closeable work and equipment-gated work under the current constraint (no physical equipment exists yet).
- How to treat cross-references, named mechanisms, and scope-map drift so that future sessions (any agent, or human solo) can invoke the same moves without rediscovering them.

**This file DOES NOT define:**
- A mandatory checklist that must be completed before any edit.
- A replacement for `Admin/Auditor_Protocols.md`, `Admin/Forge_Audit_Kit.md`, or the Verification Gates.
- New process gates, Spec Gate requirements, or ratification conditions.
- Numeric thresholds, independence scores, or claims that require Field_Logs data this file cannot produce.

**Relationship to other Admin files:**  
This is a reference document in the same tier as `Auditor_Protocols.md` and `Forge_Audit_Kit.md`. It is intended to be cited (“apply the Resolution_Methodology dependency-hollowness check”) rather than followed as ritual. Where it conflicts with Auditor_Protocols or the Epistemic Foundation, those documents win.

---

## File Purpose

The 2026-08-15 session closed or advanced multiple Critical unknowns (AS-005, PL-001/WA-002/TS-002 shared isolation destination, GF-007/FA-002 fire doctrine, GOV-021c first live evidence) without inventing hardware or claiming readiness the session could not produce. The durable product was not any single closure; it was a small set of repeatable moves that kept turning vague cross-references into named, reusable architecture.

This file names those moves so they can be invoked by citation instead of re-explained each time.

---

## Core Patterns

### 1. Dependency-Hollowness Check

Before treating a cross-reference as load-bearing, open the target file and verify that the claimed doctrine actually exists and has content.

**Demonstrated case:** GR-007 stated it was “downstream of WA-002.” Checking WA-002 literally showed a bare table-row description with no identification protocol. The resolution path was therefore to write the missing protocol first (Hazardous Fraction Identification Protocol, 2026-08-15), then give GR-007 real categories that could actually use it. Restating “blocked on WA-002” without the check would have left both files hollow.

**Move:** When an unknown or resolution path cites another unknown as a prerequisite, treat the citation as a hypothesis until the target’s body is inspected. If the target is empty or only a table row, the real work is often to fill the target, not to restated the dependency.

### 2. Reuse-Before-Invent

Prefer extending an existing named mechanism over creating a parallel path that solves the same problem under a new name.

**Demonstrated cases:**
- AS-005: GI-002’s “route through scrubber intake” had no mechanical meaning in Air_Scrubber.md. The resolution was a physically separate auxiliary release point that reused the file’s own Variant 1 (aerated bubbler) baseline and stayed chemically isolated from Stage D’s calibrated loop — not a new hardware doctrine and not a tap into the main A→E stream.
- PL-001 / WA-002 / TS-002: “specialist disposal” (Plastics) and “routed per WA-004/GR-003” (Waste) were two sentences pointing at the same undefined place. The resolution extended TS-002’s existing Contaminated bin (non-decontaminable state) to cover compositional hazards explicitly. No new destination was invented.
- BFR detection in WA-002: bromine is a halogen; PL-001’s already-established Beilstein test was reused rather than a parallel method written.

**Move:** When a gap appears, first search for an existing named hold, path, test, or bin that already sits in the right architectural position. Extend it. Invent only when nothing reusable exists.

### 3. Verify-Before-Accept

Primary-source check (grep / view / direct read) on every factual claim in a proposal before implementing it. Do not accept characterizations on trust, even from a prior agent in the same session or a prior session of the same agent.

**Demonstrated case:** GOV-021c Field_Logs entry of 2026-08-15. Grok proposed the shared-destination architecture with specific claims about PL-001 language, GI-003 kit contents, and WA-002 routing phrasing. Claude re-verified each claim against the primary files before acting. All claims held; the architecture was implemented. Model independence and evidence independence were thereby met and traceable. Role independence was not fully met (Reviewer/Implementer collapsed) and was named precisely rather than rounded up.

**Move:** Treat every cross-file factual assertion as provisional until the owning file is opened. Log the verification (or the failure of verification) so the independence dimensions remain inspectable.

### 4. Digital / Equipment-Gated Split

Explicitly separate what can be closed or advanced on paper from what requires physical validation, training data, or equipment that does not yet exist. Never invent a number, capacity, or “validated” claim the session cannot produce.

**Demonstrated cases:**
- AS-005 deliberately left the auxiliary release point unsized because capacity depends on GI-002’s still-open largest-plausible-vessel assumption.
- WA-002 protocol written at Analogous confidence; remains Open because feedstock validation and formal operator training cannot be produced without equipment.
- GF-007: four of five fire-doctrine items grounded on the sourced NFPA 51B 35 ft / 11 m standard; the fifth (ventilation/fire interlock) left open pending an Air_Scrubber addition rather than invented unilaterally.
- GOV-021c: one data point logged; the unknown left Open. No claim of closure on specification alone.

**Move:** When writing a Resolution Path, state which steps are paper-closeable now and which are gated on equipment, site, or Field_Logs data. Prefer an honest Open status with a clear remaining evidence need over a premature Resolved.

### 5. Scope-Map Stale-Pointer Pattern

The per-folder Scope_Maps (`Ops_Scope_Map.md`, `Adm_Scope_Map.md`, etc.) have already proven value by catching ownership reassignments and cross-file pointers that never fully propagated. After a folder has been heavily edited, the corresponding Scope_Map is a high-yield surface for residual drift.

**Demonstrated case:** Ops_Scope_Map.md Last Reviewed 2026-08-08; the 2026-08-15 Operations sweep (AS-005, PL-001/WA-002 shared destination, GF-007, Gate_01/02/03 updates) post-dates it. The map’s own methodology previously caught a 2026-07-19 ownership reassignment that had left stale pointers across three files.

**Move:** After a material session on a folder, either refresh the Scope_Map entry for the changed files or explicitly note the map as stale relative to the session date. Do not treat an unreviewed Scope_Map as current navigation.

---

## How to Cite

These patterns are intended to be referenced by short name in Resolution Logs, Field_Logs entries, and cross-agent handoffs:

- “Applied Resolution_Methodology §1 (dependency-hollowness check) to WA-002 before accepting GR-007’s downstream claim.”
- “Applied §2 (reuse-before-invent): extended TS-002 Contaminated bin rather than inventing a parallel specialist-disposal path.”
- “Applied §3 (verify-before-accept): primary-source check on every claim in the proposal before implementation.”
- “Applied §4 (digital/equipment-gated split): left capacity unsized; remains Open pending GI-002 vessel assumptions.”
- “Applied §5 (scope-map stale-pointer): Ops_Scope_Map last reviewed 2026-08-08; flagged for refresh after today’s Operations edits.”

Citation is optional. The value is that the move is named and therefore reusable without re-deriving the rationale each time.

---

## First Applied Case (intended)

**WA-004 / GR-003** — negative-value waste fraction and biological/chemical disposal doctrine.

Both remain Open and Critical. Both are now the explicit downstream of the shared Contaminated-bin destination established 2026-08-15. Both are still thin (table-row or high-level path only). Both are paper-addressable at the doctrinal level under the current equipment constraint.

Recommended application order under this methodology:
1. §1 — Confirm GR-003 and WA-004 still lack concrete disposal categories, hold limits, and escalation language (expected: yes).
2. §2 — Decide whether doctrine lives by extending an existing owner or whether a dedicated `Operations/Waste_Handling.md` is still warranted; prefer the former if a clean home exists.
3. §3 — Any proposal that claims regulatory or disposition language must be checked against primary sources (Ethical_Constraints, existing Gate_03 prohibited-input language, etc.) before acceptance.
4. §4 — Write minimum categories, hold doctrine, and escalation path at Analogous / doctrinal level; leave jurisdiction-specific regulatory research and physical validation explicitly Open.
5. §5 — Note any Scope_Map or Unknowns.md count/pointer updates required by the change.

This file itself does not perform that work; it only names the method so the next pass can invoke it cleanly.

---

## Lessons Learned

| Date       | Evidence Type     | What Was Tried                          | What Failed / What Held                      | What Was Learned                                      | Confidence | Revalidation Needed |
|------------|-------------------|-----------------------------------------|----------------------------------------------|-------------------------------------------------------|------------|---------------------|
| 2026-08-15 | Cross-agent session | Multiple Critical unknowns advanced under digital-only constraint | Hollow cross-refs and parallel invention were the failure modes that the patterns above prevented | Naming the moves once is higher leverage than any single closure; evidence independence is inspectable only when primary-source checks are performed and logged | Analogous  | After next applied case (WA-004/GR-003 or residual GF-007) |

---

## Active Disputes

None.

---

## Auditor Notes & Unknowns

None opened by this file. This document creates no unknowns and resolves none on its own.

---

## Abandoned Paths

None yet. Candidate for future review: any attempt to turn this reference into a mandatory gate or Spec Gate requirement — that would invert its purpose.

---

## Drift Indicators

- This file claims patterns that no longer match how resolution work is actually performed in later sessions.
- A new session rediscovers the same moves without citing this file, and the rediscovery produces a conflicting or expanded set that is not folded back here.
- Scope_Maps or Unknowns.md are left stale after a folder-scale edit that this methodology would have flagged under §5.
- Any claim that GOV-021c (or any other evidence-gated unknown) can be closed by methodology documentation alone.

---

## Resolution Log

- 2026-08-15: **File created (v0.1).** Captures the five resolution patterns demonstrated in the 2026-08-15 Operations / Governance session (AS-005, PL-001/WA-002/TS-002 shared destination, GF-007/FA-002, GOV-021c first live evidence). Written as an Admin-tier reference, not a process or gate. First intended applied case named (WA-004/GR-003). No unknowns opened or closed. Human-directed.

