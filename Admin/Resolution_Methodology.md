# Resolution_Methodology.md

**Version 0.9 — 2026-08-28**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Active — Reference                                                  |
| Body Stability   | Transitional                                                        |
| Spec Gates       | N/A — this file is a named reference for demonstrated patterns, not a specification or gate |
| Verification Ref | Admin/Verification_Gates.md                                         |
| Last Audit       | 2026-08-28 (Patterns 6–9 added: specification/operational-clearance split; discharge-vs-specification; verify-closure-format-against-precedent; self-maintenance verification — distilled from the 2026-08-23 through 2026-08-27 session's closures and hygiene fixes, none of which had been captured here despite being real, repeatable, and independently rediscovered rather than cited each time) |
| Auditor          | Claude — Patterns 6–9 drafted and registered, citation examples added (human-directed, prompted by an explicit question: what should following agents know that isn't yet in Progress_Log.md or here), 2026-08-28; prior: Claude — Fifth Applied Case registered, mislabeling corrected in four downstream citations (human-directed), 2026-08-25; prior: Grok — human-directed draft from 2026-08-15 session patterns |
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

### 6. Specification / Operational-Clearance Split

Closing an unknown via Payment via Specification does not mean the underlying capability is ready for real-world reliance. Keep the two states explicitly distinct: mark the unknown Resolved once the doctrine itself is complete, but name a residual (conventionally R1) that keeps real-world Blocking force in place until the actual empirical, jurisdictional, or physical gap is closed.

**Demonstrated cases:** GOV-003 (Integrity Enforcement Architecture — architecture specified, SEC-007b instantiation left as the named blocker), PL-001 (Halogenated Polymer Triage Protocol — protocol specified, PL-001-R1 feedstock validation left open, Blocking Yes retained for hot runs), WA-002 (identification protocol, training standard, and lab-arrangement structure specified, WA-002-R1 feedstock validation left open), GR-003 (five-category disposal doctrine with concrete hold-duration/container values specified, GR-003-R1 jurisdiction-dependent regulation left open) — all four closed the same way, independently verified against each other for consistency (see Pattern 8) rather than reinvented per file.

**Move:** When drafting a closure, ask "does this specification actually make the capability safe/ready to use today, or does it only make the *plan* for using it complete?" If the latter, close Resolved and name the residual explicitly — don't leave the unknown nominally Open just because real-world validation hasn't happened, and don't claim full readiness just because the paper is done. Risk and Priority fields stay unchanged on this kind of closure (see Pattern 8) — the specification closing is not itself a de-escalation.

### 7. Discharge via Consolidation vs. Payment via Specification

Before drafting a new specification for an unknown, check whether it is actually a duplicate of another unknown's tracking, not a distinct problem needing its own doctrine. If the underlying question is already owned and resolved elsewhere, the correct disposition is Discharge via Consolidation to the canonical entry, not a second specification pass.

**Demonstrated case:** WA-004 ("negative-value waste fraction disposal") had said in its own text for weeks that it tracked `Operations/Gate_03_Reduction.md` GR-003's doctrine from the Challenges/ side, "not a second one." Once GR-003 itself closed (concrete hold-duration/container values specified), the honest move for WA-004 was not to write a second specification but to discharge it to GR-003 — matching the repository's own prior precedent (`Operations/Gate_02_Triage.md` TS-004 → `Admin/Canonical_Terms.md` CT-002, `Admin/Forge_Audit_Kit.md`'s Resolved Unknown Discharge Procedure). One difference from that precedent worth noting: TS-004's canonical target (CT-002) was still Open at the time of discharge; WA-004's target (GR-003) was already Resolved, so WA-004's discharge carried GR-003's residuals by reference rather than tracking its own.

**Move:** Before treating a gap as needing a new specification, check the unknown's own cross-references and the owning file's Discharge Procedure doctrine for an existing canonical entry covering the same ground. If one exists, discharge to it rather than duplicating work — and if the canonical entry is itself Resolved, say so explicitly rather than leaving the discharged entry's status ambiguous.

### 8. Verify Closure Format Against Precedent Text, Not Assumed Convention

Distinct from Pattern 3 (which verifies factual claims): a drafted closure's *structure* — which fields change, which stay fixed, what gets annotated — should be checked against the actual post-closure text of prior real closures, not against a remembered or assumed description of the convention.

**Demonstrated case:** A draft closure for GR-003 annotated the Risk and Priority fields as "(residual)" and "→ residual only" after closure. This was new notation, not used in any of the three prior closures that same session (GOV-003, PL-001, WA-002), all of which left Risk and Priority unchanged on closure per Pattern 6. Caught by opening `Operations/Plastics.md` and `Challenges/Waste.md` directly and reading their actual post-closure header text, not by recalling what the convention was supposed to be.

**Move:** When integrating a drafted closure, open at least one prior real closure of the same kind and diff the drafted structure against it directly — field names, which fields change vs. stay fixed, annotation style — before trusting that the draft follows established convention.

### 9. Self-Maintenance Verification (Prose and Code)

A file that states its own maintenance rules (rotation limits, size caps, "most recent first" ordering, category lists, canonical version blocks) must be checked against its own actual content after any edit — not assumed compliant because the rule is written down. This applies equally to prose documentation and to source code; a Python module's category-string list is the same kind of self-claim as a changelog's stated rotation threshold, and both can silently drift from what the file actually does.

**Demonstrated cases:** `Unknowns.md` stated Resolved entries "leave the Active Index immediately" (Size Management Rule 2) and that its version-history block "keeps only the current version" — both had silently stopped being true, 26 stale rows and 20 stacked versions respectively, for weeks, with each new version's own closing line falsely claiming compliance. `Admin/Progress_Log.md` failed to preserve its own stated "most recent first" ordering and five-entry rotation limit on five separate occasions across one week, including once while a fix for a *previous* instance of the same failure was being written. `Automation/integrity_check.py`'s health-dashboard used two category-name strings (`UNKNOWN_ID`, `VERSION`) that did not match any `Finding` category actually produced anywhere in the codebase, silently showing a false PASS while 11 genuine CRITICAL findings sat completely unrepresented — caught only by programmatically cross-referencing the dashboard's category list against every `Finding(...)` call in the source, not by reading the code and judging it correct.

**Move:** After editing any file that makes a claim about its own structure or behavior — a stated rule, a category list, a canonical string, an ordering invariant — re-derive that claim mechanically (grep, count, re-run) rather than trusting that the edit landed as intended. For code specifically: run a syntax check after every edit, and when a check or dashboard produces a comfortable "all clear" result, verify that result actually covers everything it claims to, rather than trusting a clean summary at face value.

---

## How to Cite

These patterns are intended to be referenced by short name in Resolution Logs, Field_Logs entries, and cross-agent handoffs:

- “Applied Resolution_Methodology §1 (dependency-hollowness check) to WA-002 before accepting GR-007’s downstream claim.”
- “Applied §2 (reuse-before-invent): extended TS-002 Contaminated bin rather than inventing a parallel specialist-disposal path.”
- “Applied §3 (verify-before-accept): primary-source check on every claim in the proposal before implementation.”
- “Applied §4 (digital/equipment-gated split): left capacity unsized; remains Open pending GI-002 vessel assumptions.”
- “Applied §5 (scope-map stale-pointer): Ops_Scope_Map last reviewed 2026-08-08; flagged for refresh after today’s Operations edits.”
- “Applied §6 (specification/operational-clearance split): closed GR-003 Resolved via Payment via Specification; GR-003-R1 keeps jurisdiction-dependent reliance blocked.”
- “Applied §7 (discharge vs. specification): WA-004 discharged to GR-003 rather than drafting a second disposal specification.”
- “Applied §8 (verify closure format against precedent): checked Risk/Priority fields against Plastics.md and Waste.md's actual post-closure text before integrating.”
- “Applied §9 (self-maintenance verification): re-ran the health check after editing its own category list, rather than trusting the edit was correct.”

Citation is optional. The value is that the move is named and therefore reusable without re-deriving the rationale each time.

**Correction, 2026-08-15 (v0.4):** The First and Second Applied Case sections below originally used "§5" to mean "update cross-file pointers to the new content" — that is not the same thing as Pattern 5 (Scope-Map stale-pointer check) as defined above and cited in this section's own examples. Neither applied case actually ran a scope-map check. Corrected by running one for real against `Operations/Ops_Scope_Map.md` after today's Operations edits — see the note appended to the Second Applied Case section below.

---

## First Applied Case

**WA-004 / GR-003** — negative-value waste fraction and biological/chemical disposal doctrine. Applied 2026-08-15, same day as this file's creation.

Both were confirmed genuinely thin before writing anything (§1: GR-003 outline-only, WA-004 a single table row). §2 decided against a dedicated `Operations/Waste_Handling.md` — GR-003 was already the convergence point both WA-004 and TS-002 pointed at, so extending it kept one destination rather than fragmenting into three. §3 verified `Ethical_Constraints.md`'s active-release vs. passive-encapsulation distinction against source before building on it, rather than restating it from memory — that distinction turned out to structurally imply exactly two disposal outcomes (permanent passive containment or specialist hand-off), not an open-ended list, which is a stronger result than a flat category checklist would have been. §4 wrote category-specific doctrine, deliberately withholding disposal doctrine for the radiological category since no real handling capability exists for it. Cross-file pointers updated (WA-004's row, TS-002's non-decontaminable-state text) — originally mislabeled "§5" here; see the correction under How to Cite and the real Pattern 5 run logged in the Second Applied Case section.

Both GR-003 and WA-004 remain **Open** — categories exist at Analogous confidence; jurisdiction-specific regulatory research and physical validation are still explicitly open, per §4's own instruction not to close on doctrine alone.

**What this run confirmed about the methodology itself:** §2's reuse decision produced a genuinely better architectural result (the two-outcome model) than simply filling in the originally-outlined category list would have — verifying the upstream principle first, rather than treating it as settled, is what surfaced that. Worth noting for future applications: §3 is not just a safety check against fabrication, it can produce a better answer than the thing being verified would have on its own.

---

## Second Applied Case

**GF-007 ventilation/fire interlock (`Operations/Gate_06_Fabrication.md`) × `Operations/Air_Scrubber.md`'s fault-interlock table.** Applied 2026-08-15, same day as the first case — deliberately in a different domain (fire-suppression/safety-systems, not waste/disposal), per the first case's own Revalidation Needed note.

§1 confirmed the gap was real, not already covered by anything else in either file. §2 was the interesting step here: unlike WA-004/GR-003, this wasn't a choice between two owners with equal claim — the actual shutdown mechanism (halting forced ventilation) is Air_Scrubber's own system, so the interlock logic could only sensibly live in its existing five-row fault table, not duplicated in GF-007. §3 surfaced a real limit rather than a stronger structure this time: no automatic fire/smoke detection hardware is specified anywhere in the repository, so the row's trigger input was deliberately kept method-agnostic (manual call) rather than inventing sensor doctrine. §4 closed all five of GF-007's Resolution Path items — the first case to reach that. Cross-file pointers updated in both files (this was originally mislabeled "§5" — see correction above; it is not the Scope-Map pattern).

**Pattern 5 (Scope-Map stale-pointer check), actually run 2026-08-15:** Checked `Operations/Ops_Scope_Map.md` against today's Operations edits (Gate_02, Gate_03, Gate_06, Air_Scrubber all touched). Gate_03's Scope Boundary already correctly claims contamination-discovery doctrine — no drift. Gate_02's Scope Boundary said "Decontamination protocols and air handling → Air_Scrubber.md, AS-003" — in tension with TS-002's own disposition-workflow content now living in that file. Defensible on a narrow mechanism-vs-workflow reading, but ambiguous enough to correct; clarified in `Gate_02_Triage.md` directly. This is the same class of finding Ops_Scope_Map.md's own Gaps Exposed section has caught before (the 2026-07-19 UNK-008 pattern across three files) — a smaller instance of it, not a new failure mode.

**What this run confirmed about the methodology itself:** §2 doesn't always produce a genuine choice between owners — sometimes the mechanism itself dictates the owner, and the step's value is confirming that rather than picking between options. §3 doesn't always surface a better structure (as it did in the first case) — sometimes its honest output is a firm boundary on what can be claimed (no sensor spec without validation), and that's an equally valid result, not a lesser one.

---

## Lessons Learned

| Date       | Evidence Type     | What Was Tried                          | What Failed / What Held                      | What Was Learned                                      | Confidence | Revalidation Needed |
|------------|-------------------|-----------------------------------------|----------------------------------------------|---------------------------------------------------------|------------|---------------------|
| 2026-08-15 | Cross-agent session | Multiple Critical unknowns advanced under digital-only constraint | Hollow cross-refs and parallel invention were the failure modes that the patterns above prevented | Naming the moves once is higher leverage than any single closure; evidence independence is inspectable only when primary-source checks are performed and logged | Analogous  | After next applied case (WA-004/GR-003 or residual GF-007) |
| 2026-08-15 | First applied case (WA-004/GR-003) | Ran the five-step order against a real Critical-priority pair | §2's reuse check and §3's verify-before-accept check together produced a better architectural result (two-outcome disposal model) than the originally-outlined flat category list would have | §3 is not only a fabrication safeguard — verifying an upstream principle before building on it can surface a stronger structure than the thing being checked | Analogous | After a second applied case in a different domain (chemistry/safety rather than waste/disposal) |
| 2026-08-16 | Third applied case (CE-006) | Applied methodology in chemistry/safety domain after two prior cases | Top-of-entry Resolution Path had gone stale relative to its own body; paper surface assessed as exhausted | §3 catches internal staleness as well as external fabrication; §4's "stop when paper is exhausted" outcome should be stated explicitly | Analogous | After a fourth case, or after hardware data changes CE-006's remaining open set |
| 2026-08-16 | Fourth applied case (GR-007) | Applied after GR-003 doctrine existed from an earlier methodology case | Category C's hollow "pending GR-003" citation became fillable; A–C all paper-complete | Methodology compounds — filling one hollow citation unblocks the next downstream unknown | Analogous | After a fifth case, or when Category C is first exercised against a real retired item |
| 2026-08-15 | Second applied case (GF-007 × Air_Scrubber) | Ran the same order in a different domain (fire-suppression/safety-systems) | §2 sometimes has no real choice — the mechanism dictates the owner, and the step confirms rather than selects; §3 sometimes correctly outputs a firm limit (no sensor spec without validation) rather than a stronger structure | Both outcomes are valid results of the same step, not a failure mode of the first case's more generative result | Analogous | After a third applied case, ideally one where §2 and §3 disagree or produce tension, to see how the order handles that |

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

## Third Applied Case

**CE-006** — chlorine containment for on-site chlor-alkali acid synthesis (`Architecture/Chemistry.md`). Applied 2026-08-16.

*§1:* Remaining dependencies checked against source — AS-003 still Open, Gate_05 thermal still Placeholder, CE-007 quantitative still correctly blocked on CE-006 hardware; GR-003 two-outcome model (written under this methodology the previous day) now available as the named destination for residual NaOCl that cannot be reused under CE-007.

*§2:* No new scrubber, sensor class, or disposition file invented. Stage D path, Stage D flow/power monitoring as interlock trigger, and GR-003 disposal model all reused.

*§3:* Top-of-entry Resolution Path was stale — still listed detection/alarm thresholds and caustic dosing as "remaining work" after the 2026-07-31 and 2026-08-15 body passes had already answered them. Refreshed to an explicit paper-complete vs equipment-gated inventory.

*§4:* Paper surface on CE-006 assessed as substantially exhausted. Remaining work is equipment-gated by nature (vessel build, electrode-area selection, AS-003 calibration against real flow, Gate_05 exhaust data, quantitative NaOCl sizing, membrane sourcing/test). Further paper-only passes will not move Status toward Resolved. Stays **In Progress**; Blocking Yes for CLF-004 unchanged.

*§5:* Noted `Architecture/Arc_Scope_Map.md` for refresh on next Architecture folder pass; no immediate Scope Boundary contradiction found inside Chemistry.md itself.

**What this case added to the methodology's evidence base:** First application in the chemistry/safety domain (prior cases were waste/disposal and fabrication/fire). Confirmed that §3 can catch *staleness of the Resolution Path relative to its own body*, not only fabrication in a proposal. Confirmed §4's "stop when paper surface is exhausted" outcome is reachable and should be stated explicitly rather than left as an open-ended "continue refining."

---

## Fourth Applied Case

**GR-007** — contaminated equipment retirement threshold (`Operations/Gate_03_Reduction.md`). Applied 2026-08-16.

*§1:* Category C's prior "disposition pending WA-004/GR-003" citation checked against source — GR-003 two-outcome model now exists (written under this methodology the previous day), so the dependency is no longer hollow.

*§2:* Category C disposition reuses GR-003 (including its intact/fragmentation integrity rule) rather than inventing a parallel retirement-disposition path.

*§3:* GR-003 outcomes and WA-002 presumptive-match trigger verified against primary sources before rewriting Category C.

*§4:* Categories A, B, and C disposition paper-complete at doctrine level. Residual openness is operational/equipment-gated (validated cleaning methods for Category A, physical confirmation procedures that promote B→C, jurisdiction-specific specialist hand-off). Default-retire posture retained. Stays **Open**.

*§5:* Ops_Scope_Map already refreshed 2026-08-16; no new Scope Boundary contradiction found.

**What this case added:** First application that closed a *downstream dependency* opened by an earlier methodology case (GR-003 → GR-007 Category C). Demonstrates the method compounds: filling one hollow citation unblocks the next.

---

## Fifth Applied Case

**GR-003 concrete hold-duration and container-type values** (`Operations/Gate_03_Reduction.md`). Applied 2026-08-24.

*§1:* Confirmed the specific gap was real and narrowly scoped — the First Applied Case (2026-08-15) had already supplied the architectural two-outcome model and five-category structure; only concrete hold-duration values and container-type requirements per category remained unwritten, exactly as that case's own closing note said.

*§2:* No new category structure or disposal model invented — filled the existing five-category frame (heavy-metal, chemical, asbestos, biological, radiological) with concrete values rather than restructuring it.

*§3:* Values drawn from and checked against real external analogs (RCRA generator accumulation practice, industrial temporary-storage guidelines, lab holding tables, ACM handling norms, biosafety waste practice) at Analogous confidence, not asserted as Forge-validated.

*§4:* A first draft deviated from an established convention — this repository's PL-001/WA-002/GOV-003 pattern of leaving Risk/Priority fields unchanged on closure — by annotating them as "(residual)"/"→ residual only." Caught and corrected before integration by checking against those three files' actual post-closure text, not just their stated intent. Category structure closes Resolved via Payment via Specification; three residuals (GR-003-R1 jurisdiction-dependent regulation, R2 physical validation, R3 Ethical_Constraints permanent-placement confirmation) keep full operational reliance blocked. Stays functionally blocked pending R1; does not stay **Open** the way GR-007 did in the Fourth case — the distinction is that this case closed the specification itself, where GR-007 remained an unresolved doctrine gap.

*§5:* This case was mislabeled "second applied case" (GF-007's actual case number) at the time of integration, in four places — `Gate_03_Reduction.md`'s own closure note and Resolution Log entry, `Unknowns_Changelog.md`'s v4.83 record, and `Admin/Progress_Log.md` — and this file itself was never updated to register the case at all. Found and corrected 2026-08-25, during a systematic cross-reference sweep prompted directly by the question "have we closed all angles of previous work" — not caught by any of the verification passes run at the time of the original closure.

**What this case added:** First applied case to demonstrate that the method's own tracking apparatus — this file's ordinal case numbering — can itself drift out of sync with the work it records. The underlying doctrine work was real and correctly executed; the citation of it was wrong everywhere it appeared, for a full session, because nothing checked this file against its own citations until asked to.

---


## v0.7 refinements (release-layer, 2026-08-16)

Lessons from applied cases CE-006, GR-007, and integrity P1–P3 — still **reference**, not a gate.

1. **§3 internal-staleness sub-check:** Before writing new doctrine, diff the entry's Resolution Path against body claims already present. (CE-006: path still listed detection/alarm as open after body had answered them.)
2. **§4 stop rule:** When further paper cannot move Status, state **paper surface exhausted** and leave residual work explicitly equipment-gated or operational. Do not refine digitally for its own sake.
3. **Upstream-hollow preference:** Prefer closing a hollow citation that unblocks a downstream unknown before opening parallel paper fronts. (GR-003 doctrine unblocked GR-007 Category C.)
4. **Same-session registration:** New active Admin file → register in `Routing.md` (and Scope_Map if applicable) in the same session. (Resolution_Methodology and Integrity_Incident_Log both needed a later catch-up.)
5. **Classify ≠ create:** An integrity-harness UNKNOWN reference is a classification task, not a create-file order. Intentional non-creation (e.g. Waste_Handling under GR-003 ownership) remains valid.

Integrity incidents: log Major/Constitutional (and compound Minor) in `Admin/Integrity_Incident_Log.md` — not only Progress_Log or chat. This methodology does not own RIP; it cross-references the log home.

---

## Resolution Log

- 2026-08-16 (v0.7): Release-layer refinements A–E folded in (internal-staleness sub-check, paper-exhausted stop rule, upstream-hollow preference, same-session Routing, classify≠create). IIL cross-ref only. Human-directed.

- 2026-08-16 (v0.6): **Fourth applied case — GR-007 (equipment retirement / safety-governance domain).**
  Category C disposition named via GR-003 two-outcome model; Categories A–C
  paper-complete at doctrine level. Residual openness is operational validation
  and jurisdiction, not missing architecture. No unknowns opened or closed.
  Human-directed.


- 2026-08-16 (v0.5): **Third applied case — CE-006 (chemistry/safety domain).**
  Paper surface assessed as substantially exhausted under §4; Resolution Path
  refreshed from stale remaining-work list to explicit paper-complete vs
  equipment-gated split; residual NaOCl disposition pointed at GR-003 rather
  than a parallel path. No unknowns opened or closed. Human-directed.


- 2026-08-15 (v0.4): **Self-correction, prompted by a direct question about
  whether this file requires Unknowns.md/changelog updates.** Checking that
  claim precisely (it doesn't — §5 says "note... updates required," the
  changelog-migration convention is Unknowns.md's own, not this file's)
  surfaced two real problems: the File State Version field was stuck at
  0.1 despite the Resolution Log recording v0.3, and both Applied Case
  sections had mislabeled a generic "update cross-file pointers" step as
  "§5," which is specifically the Scope-Map stale-pointer pattern — neither
  applied case had actually run that check. Fixed the version field. Ran
  the real check against `Operations/Ops_Scope_Map.md`: found one genuine
  small drift (`Gate_02_Triage.md`'s Scope Boundary claimed Air_Scrubber
  owned "decontamination protocols" outright, in tension with TS-002's own
  disposition-workflow content now living there) and corrected it. Same
  class of finding as Ops_Scope_Map.md's own prior UNK-008 catches, smaller
  scale. Human-directed.

- 2026-08-15 (v0.3): **Second applied case complete — GF-007 × Air_Scrubber
  ventilation/fire interlock.** Deliberately a different domain than the
  first case, per its own Revalidation Needed note. §2 turned out to have
  no real choice — the shutdown mechanism itself dictated the owner
  (Air_Scrubber). §3 correctly output a firm limit (no fire-detection
  hardware spec without physical validation) rather than a stronger
  structure, showing that's an equally valid §3 outcome, not a lesser
  one than the first case's more generative result. GF-007 reached five
  of five Resolution Path items closed — the first case to do so. Neither
  file's unknown closed; both remain Open. Human-directed.

- 2026-08-15 (v0.2): **First applied case complete — WA-004/GR-003.**
  Ran the five-step order against a real Critical-priority pair. Result:
  §2 (reuse) and §3 (verify-before-accept) together produced a stronger
  architectural outcome (a two-outcome disposal model derived from
  `Ethical_Constraints.md`'s active-release/passive-encapsulation
  distinction) than the originally-outlined flat category list would
  have — logged as a Lessons Learned row, since it's a real finding
  about the methodology, not just about waste disposal. Neither GR-003
  nor WA-004 closed — both remain Open, doctrine only. Human-directed.

- 2026-08-15: **File created (v0.1).** Captures the five resolution patterns demonstrated in the 2026-08-15 Operations / Governance session (AS-005, PL-001/WA-002/TS-002 shared destination, GF-007/FA-002, GOV-021c first live evidence). Written as an Admin-tier reference, not a process or gate. First intended applied case named (WA-004/GR-003). No unknowns opened or closed. Human-directed.

