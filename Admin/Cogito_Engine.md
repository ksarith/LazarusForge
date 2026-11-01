# Cogito_Engine.md

**Version 0.2 — 2026-10-31 (deposited per human direction; not ratified)**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value |
|------------------|-------|
| Status           | Exploration |
| Body Stability   | Volatile |
| Spec Gates       | N/A — a named method, not a specification or gate; cell-asserted by file class per the Resolution_Methodology precedent (that file’s own Spec Gates cell is likewise cell-asserted, not a registered Template Exemptions class). Whether method-class files warrant a registered exemption class is an open ruling — flagged here, not registered (MAINT-48 disclosure). |
| Verification Ref | Admin/Verification_Gates.md |
| Last Audit       | None — new file; no Campaign 2 deposit; first audit at the next sweep |
| Auditor          | None yet |
| Open Unknowns    | 0 |
| Active Disputes  | 0 |
| Highest Risk     | Low |
| Sidecar Link     | N/A |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**DOES define:** A method for taking an idea from a first-pass seed to a form fit for formal review, or to honest retirement; the checks that mark it ready.

**DOES NOT define:** Decision Brief format or the Architect proposal format (→ `Archive/Architect_Prompt.md`); audit method (→ `Admin/Auditor_Protocols.md`); ratification (the human governing authority; → `Admin/Governance_Migration_Protocol.md` for axioms); demonstrated resolution patterns (→ `Admin/Resolution_Methodology.md`, of which this is the pre-design counterpart).

---

## File Purpose

Several instruments in this repository were improved by repeated critique (the Reset-Event design, the seat prompts). This file names that loop so it is used on purpose: refuse the first version, carry state forward in writing, apply formal tools only when a checkable threshold is met, and retire ideas that cannot reach it.

---

## Assumptions

| ID | Assumption | Evidence | Confidence |
|----|------------|----------|------------|
| (none registered) | | | |

---

## Body

### Principles

1. **First pass is raw material.** Not a candidate for audit, brief or ratification.
2. **Carry-over is written, not remembered.** Each pass produces a dated delta note beside the draft (kept, changed, dropped, unresolved). The next pass starts from those artifacts, so the method works for an agent with no memory of earlier sessions (Discovery objective 4).
3. **Threshold before formal tools.** An idea is ready when: a cold reader (different agent) restates it correctly; the strongest opposing case is written and answered; the Hard Floor and Tier 1 check is done; at least one pass was by an agent other than the author; an owning seat and ratification path are named. The human judges whether the threshold is met. The demonstrated-case record is Core Pattern 10 in `Admin/Resolution_Methodology.md` (v0.11); this file owns the threshold and method statement, the pattern records the demonstrated cases.
4. **Retirement is a result.** If passes cannot make the seed coherent, retire it with a one-line record (idea, date, reason). New evidence may reopen it.
5. **Agreement is signal, not proof.** At least one pass is an attack by a different agent. A pass that only agrees adds no weight.

### What this is not
Not a seat, not a ratification path, not required for routine maintenance, and not a way to turn conversation into doctrine.

### Working example
Reset-Event design, 2026-10-31: v0.1 → skeptic review → v0.2 → second review (found an omitted existing doctrine) → v0.3 overlay.

---

## Lessons Learned

| Lesson | Evidence Type | Confidence |
|--------|---------------|------------|
| Carry-over in writing is what let later passes find what earlier passes missed (Reset-Event v0.2 → v0.3). | Audit Review (direct in-repo observation) | Direct — single demonstrated case; revalidate after the next refinement cycle |

---

## Active Disputes
None.

---

## Auditor Notes & Unknowns
None.

### Resolution Log
- 2026-10-31: v0.2 — deposited in LazarusForge (human direction: “Please proceed”; MAINT-48). Attack-pass findings folded: Spec Gates cell reworded — the Resolution_Methodology precedent is cell-asserted by file class, not a registered Template Exemptions class, and the method-class exemption ruling stays open (flagged, not registered); Lessons Learned upgraded from “Analogous” to Direct with a single-case caveat; Principle 3 cross-referenced to Resolution_Methodology Core Pattern 10 (canonical-statement ownership: this file owns the method; the pattern cites it and records demonstrated cases). Routing row, Discovery tree entry and maturity-snapshot row registered in the same pass.
- 2026-10-31: v0.1 draft — normalized to template; principle 2 rewritten from “conversation” to written carry-over; principle 3 given a checkable threshold; retirement record and independent-attack rule added. Not deposited in LazarusForge.
