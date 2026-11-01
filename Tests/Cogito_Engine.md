# Cogito_Engine.md

**Version 0.4 — 2026-11-01 (human-ratified consolidation: threshold-eligibility clarification, minimum delta record, challenger disposition, retirement disposition, unknowns-count semantics, related-runtime pointer, deferred lineage direction; file status remains Exploration)**

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
| Spec Gates       | N/A — a named method, not a specification or gate; cell-asserted by file class per the Resolution_Methodology precedent (that file's own Spec Gates cell is likewise cell-asserted, not a registered Template Exemptions class). Whether method-class files warrant a registered exemption class is an open ruling — flagged here, not registered (MAINT-48 disclosure). |
| Verification Ref | Admin/Verification_Gates.md |
| Last Audit       | None — new file; no Campaign 2 deposit; first audit at the next sweep |
| Auditor          | None yet |
| Open Unknowns    | 0 — this count covers unknowns registered to this file; the Spec Gates ruling above is flagged, not registered, per MAINT-48, so it does not count here. Zero means "no unknowns registered to this file," never "no outstanding questions." |
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
2. **Carry-over is written, not remembered.** Each pass produces a dated delta note beside the draft (kept, changed, dropped, unresolved). The next pass starts from those artifacts, so the method works for an agent with no memory of earlier sessions (Discovery objective 4). Minimum delta record: (a) the draft identity reviewed (file and version); (b) what changed, and the objection or evidence that triggered the change; (c) kept / changed / dropped / unresolved; (d) the class of each material claim — observed / inferred / assumed / unknown; (e) the next review step. Historical deltas are preserved as written; nothing is conformed retroactively.
3. **Threshold before formal tools.** An idea is ready when: a cold reader (different agent) restates it correctly; the strongest opposing case is written and answered; the Hard Floor and Tier 1 check is done; at least one pass was by an agent other than the author; an owning seat and ratification path are named. The human judges whether the threshold is met. Passing the threshold establishes eligibility to enter formal review — nothing more; it is not evidence that the idea is correct, safe, implementable, or demonstrated, and procedural completion is not substantive evidence. The demonstrated-case record is Core Pattern 10 in `Admin/Resolution_Methodology.md` (v0.11); this file owns the threshold and method statement, the pattern records the demonstrated cases.
4. **Retirement is a result.** If passes cannot make the seed coherent, retire it with a one-line record (idea, date, reason). The record carries a disposition category: contradicts an established constraint / premise disproved / cost exceeds benefit / redundant with an existing mechanism / avenues exhausted. New evidence may reopen it, compared against the recorded disposition.
5. **Agreement is signal, not proof.** At least one pass is an attack by a different agent. A pass that only agrees adds no weight. The challenger records whether the strongest opposing case was answered, partially answered, or left unresolved, with a reason; a dissent may stay open while the candidate advances, and the readiness decision must acknowledge it. The attack pass discloses the reviewer's line, model family where known, and shared-context exposure. A different agent is not independent verification; that claim is reserved for independence conditions that are defined and satisfied.

### What this is not
Not a seat, not a ratification path, not required for routine maintenance, and not a way to turn conversation into doctrine.

### Working example
Reset-Event design, 2026-10-31: v0.1 → skeptic review → v0.2 → second review (found an omitted existing doctrine) → v0.3 overlay.

### Related runtime (non-normative)
A separate repository, `[CogitoEngine] README.md`, contains a runtime in the same epistemic family (written carry-over, provenance, refusal as a first-class result, evidence labels). This file does not govern that repository and makes no claim that it conforms. Whether and how a runtime could be shown to conform (a conformance test) is open and not registered here. That repository's `Cogito_Engine.md` is a runtime build contract — a different document class on a separate version line; do not conflate the two.

### Open direction (not built)
Candidate lineage — branching alternatives, explicit recombination, structured dissent — is a recognized direction for a future version, deferred until the cold-start trial (that repository's `docs/Cold_Start_Trial.md`) yields evidence. Not built here; branching in the runtime is likewise specified, not built.

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
- 2026-11-01: v0.4 — human-ratified consolidation, landed at human direction (MAINT-50). Threshold restated as review-eligibility, not evidence (P3); minimum delta record defined (P2); challenger disposition and independence disclosure added (P5); retirement disposition category added (P4); Open Unknowns semantics made explicit per MAINT-48 (the flagged-not-registered ruling does not count; zero never means "no outstanding questions"); Related-runtime section added (non-normative, `[ExternalRepo]` form); candidate-lineage direction registered as deferred. Sources: Claude v0.3→v0.4 delta note, Vibe (GLM 5.3) attack pass, external ChatGPT review (all 2026-11-01). Cascade check: no Routing or Tst_Scope_Map descriptor change; no MDR trigger.
- 2026-10-31: v0.3 — relocated `Admin/Cogito_Engine.md` → `Tests/Cogito_Engine.md` per human direction (MAINT-49); no body, principle, status, gate or cascade change; Routing row and Discovery tree/snapshot entries repointed; `Admin/Resolution_Methodology.md` Core Pattern 10 move-3 citation repointed (citation-form-only, no version bump there); Tst_Scope_Map entry added. The MAINT-48 registrations name the Admin/ path — those are the deposit records and stay as written.
- 2026-10-31: v0.2 — deposited in LazarusForge (human direction: "Please proceed"; MAINT-48). Attack-pass findings folded: Spec Gates cell reworded — the Resolution_Methodology precedent is cell-asserted by file class, not a registered Template Exemptions class, and the method-class exemption ruling stays open (flagged, not registered); Lessons Learned upgraded from "Analogous" to Direct with a single-case caveat; Principle 3 cross-referenced to Resolution_Methodology Core Pattern 10 (canonical-statement ownership: this file owns the method; the pattern cites it and records demonstrated cases). Routing row, Discovery tree entry and maturity-snapshot row registered in the same pass.
- 2026-10-31: v0.1 draft — normalized to template; principle 2 rewritten from "conversation" to written carry-over; principle 3 given a checkable threshold; retirement record and independent-attack rule added. Not deposited in LazarusForge.
