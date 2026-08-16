# Resolution_Methodology.md

**Version 0.7 — 2026-08-16**

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
| Last Audit       | 2026-08-16 (v0.7 release-layer refinements)                         |
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

