# Pyrolysis_Cascade.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft — Exploration                                                 |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6 (not yet audited)                                               |
| Verification Ref | `Admin/Verification_Gates.md`                                    |
| First Logged     | 2026-08-04                                                          |
| Last Audit       | — (pre-audit skeleton; ID-collision fix applied 2026-08-04, not a Gate audit) |
| Auditor          | — (Claude — Synthesizer, PC-/PYC- namespace collision fix only, human-directed, 2026-08-04) |
| Open Unknowns    | 8 (PYC-001 … PYC-008)                                                 |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High (thermal processing of mixed salvage; halogen & hazardous-fraction exposure) |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.  |

**Version String Registry** (self-referential citations outside File State — update on every version bump):
- §Organizing Principle (if retained)
- §Relationship to Repository Domains

---

## Scope Boundary

**This file DOES define:**
- Exploratory architecture for a staged thermal cascade: primary pyrolysis of pre-triaged salvage → secondary high-temperature reduction of the resulting char/coke fraction (bloomery-type or equivalent candidate) with heat integration between stages.
- Candidate material-separation pathways (hydrocarbons, metals, residual carbon, slag) and the open questions required to evaluate them.
- Explicit dependency surface on upstream triage, reduction-method selection, hazardous-fraction handling, site, energy, and scrubber doctrine owned by other files.
- Test concepts and measurement priorities that would be required before any claim of technical or economic viability.

**This file DOES NOT define:**
- Halogenated-polymer triage protocols or field polymer identification methods (→ `Operations/Plastics.md` PL-001, `Architecture/Chemistry.md` CE-003).
- Selection or ownership of the reduction method itself (→ `Operations/Gate_03_Reduction.md` GR-002).
- Air scrubbing design, performance, or waste-stream doctrine (→ `Operations/Air_Scrubber.md`).
- Chemical / biological / negative-value waste disposal doctrine (→ GR-003, WA-004).
- Site assessment, emergency response, or structural safety factors for salvaged furnaces (→ `Architecture/Facilities.md` FA-001, `Admin/Safety_Protocols.md` SP-006, `Architecture/Engineering.md` EN-001).
- Operating-cost baseline, power-demand characterization, or profitability claims (→ `Admin/Economics.md` ECN-002, `Operations/Energy.md` EV-001, `Admin/Trajectories.md` TR-001).
- Any Specification-level performance guarantee, yield number, or “self-sufficiency” claim.
- Fabrication procedures, experimental methodology standards beyond the test concepts listed, or canonical terminology.

**Hard preconditions (non-negotiable):**
- No hot pyrolysis or high-temperature reduction of mixed urban salvage may be proposed, piloted, or claimed under this file until PL-001 and CE-003 are resolved or the feedstock is demonstrably free of halogenated polymers by a validated method.
- No structural or refractory claims using salvaged materials may advance until EN-001 is closed for the relevant material classes.
- No site-dependent operational claims (emergency response, real energy balance, tipping-fee economics) until FA-001 is closed.

---

## File Purpose

This file records an exploratory thermal-cascade concept originally developed in archive conversation: load pre-processed salvage into a pyrolysis stage, recover condensable and gaseous hydrocarbons, transfer the solid residue to a higher-temperature reduction stage for metal separation and further carbon burnout, and integrate waste heat from the hot stage back into the pyrolysis stage while routing all off-gas through the repository’s air-scrubbing doctrine.

It exists to keep the architectural idea legible, to surface its dependency on already-registered Critical/Blocking unknowns, and to define the minimum empirical questions that would have to be answered before the concept could be considered for any higher maturity state. It does not assert that the cascade is currently feasible, safe, or economically viable.

**This document is subject to Auditor_Protocols.md.** Gate logic, fallacy checklist, and confidence-label rules apply.

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence   | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|--------------|-----------------------------------------------------|
| ASM-PYC-001 | Pre-triage can reduce halogenated polymer content to a level compatible with the chosen thermal path | External industrial practice (XRF/NIR sorting) | Low (Analogous) | PL-001 / CE-003 resolution or measured residual-Cl data on Forge salvage |
| ASM-PYC-002 | A bloomery-type or equivalent high-temperature stage can accept pyrolysis char and separate ferrous / non-ferrous fractions | Historical metallurgical practice; unvalidated on pyrolysis char | Low (Analogous) | GR-002 decision + char characterization |
| ASM-PYC-003 | Meaningful heat integration between 1100–1300 °C and 400–700 °C stages is thermodynamically possible | Basic heat-transfer principles     | Medium (Analogous) | First energy-balance calculation with bounded yields |
| ASM-PYC-004 | Off-gas from both stages can be rendered acceptable by the existing Air_Scrubber architecture once upstream halogen load is controlled | Air_Scrubber.md doctrine + external incineration practice | Low | AS-003 closure + residual-Cl acceptance limit |
| ASM-PYC-005 | Mixed urban salvage will remain highly variable in moisture, metal content, and contamination | Observed Forge development state   | High         | Site-specific characterization after FA-001 |

---

## Body

### Organizing Principle (Exploratory)

> A staged thermal cascade can, in principle, convert pre-triaged salvage into separable material fractions while recovering heat between stages. Whether this is safer, more recoverable, or more economical than existing Gate_03 / Plastics pathways is an open empirical question, not a design premise.

All quantitative targets that appeared in the archived draft (heat-recapture %, metals recovery %, break-even tonnage, tipping-fee ranges) are retired to Placeholder / external-analogous status and are not repeated as claims in this file.

### Candidate Cascade Outline (non-normative)

1. **Upstream triage & pre-processing** (owned elsewhere)  
   Halogen screen → energetic-material screen → size reduction → moisture conditioning.

2. **Primary pyrolysis stage** (400–700 °C, oxygen-starved)  
   Outputs: syngas, condensables, char/coke + entrained metals/inerts.

3. **Secondary high-temperature stage** (candidate: bloomery-type 1100–1300 °C)  
   Functions under evaluation: further carbon burnout, metal melting/separation, slag formation, high-grade heat source.

4. **Heat integration**  
   Hot-stage waste heat → pyrolysis preheat / feedstock drying; pyrolysis syngas as candidate fuel for hot stage.

5. **Off-gas path**  
   Both stages → multi-stage scrubbing per Air_Scrubber.md; residual hazard streams → GR-003 / WA-004 doctrine.

6. **Product disposition**  
   Hydrocarbons, metals, residual carbon, slag — each requires an explicit beneficial-use or disposal path before any recovery claim is advanced.

### Relationship to Repository Domains

| Domain / File | Relationship |
|---------------|--------------|
| `Operations/Plastics.md` | Upstream owner of pyrolysis chemistry and PL-001 |
| `Operations/Gate_03_Reduction.md` | Owner of reduction-method selection (GR-002) and waste-disposal doctrine (GR-003) |
| `Operations/Air_Scrubber.md` | Owner of off-gas treatment |
| `Architecture/Chemistry.md` | CE-003 field polymer ID; CE-006 chlorine containment |
| `Challenges/Waste.md` | WA-002 / WA-004 hazardous & negative-value fractions |
| `Operations/Energy.md` | EV-001 power demand; any energy-integration claims |
| `Architecture/Facilities.md` / `Admin/Safety_Protocols.md` | FA-001 site; SP-006 emergency response |
| `Architecture/Engineering.md` | EN-001 salvaged-material safety factors |
| `Admin/Economics.md` / `Admin/Trajectories.md` | Cost baseline and any future profitability trajectory |

This file owns none of the above. It only records the cascade concept and the questions that must be answered before the concept can be re-evaluated.

### Test Concepts (pre-empirical)

These are candidate measurements, not approved test plans:

- **PYC-TEST-001** — Residual halogen content after candidate triage methods on real salvage samples.
- **PYC-TEST-002** — Mass and energy balance of a laboratory-scale pyrolysis run on pre-triaged, characterized feedstock (halogen-free or quantified).
- **PYC-TEST-003** — Char composition (fixed carbon, metals, ash, residual Cl) and behavior under high-temperature reducing conditions.
- **PYC-TEST-004** — First-order heat-integration calculation (not physical HX test) using measured or tightly bounded yields.
- **PYC-TEST-005** — Off-gas speciation (acid gases, condensables, particulates) under controlled residual-Cl loads.

No test may be run that violates the hard preconditions in Scope Boundary.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|----------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-08-04 | Archive review + Critical/Blocking map | Promoted archived conversation draft toward live Exploration | Multiple Critical unknowns already block the core thermal claims | Cascade must be framed as dependent architecture, not autonomous process; economic and efficiency numbers retired to Placeholder | Measured (process) | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| —  | —       | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### PYC-001 — Halogenated-polymer triage dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking |
| Type | Safety / Technical |
| Blocking | Yes — blocks all hot thermal work under this file |
| Owner | Tests/Pyrolysis_Cascade.md (dependency); resolution owned by Plastics.md / Chemistry.md |
| First Logged | 2026-08-04 |
| Last Reviewed | 2026-08-04 |

**Description:** The cascade assumes a feedstock that is either free of, or controlled for, halogenated polymers. PL-001 and CE-003 remain open.

**Resolution Path:** Payment via Specification + Validation on the owning files. This entry closes only when those unknowns close or when this file is rewritten to require exclusively pre-certified halogen-free feedstock.

---

### PYC-002 — Reduction-method selection dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | High |
| Priority | Blocking (for bloomery-specific claims) |
| Type | Architectural |
| Blocking | Yes for any claim that the secondary stage is a bloomery |
| Owner | Tests/Pyrolysis_Cascade.md (dependency); resolution owned by Gate_03_Reduction.md (GR-002) |
| First Logged | 2026-08-04 |

**Description:** Archived draft treats bloomery-type reduction as the secondary stage. GR-002 has not selected a reduction method.

**Resolution Path:** Payment via Specification (GR-002 decision) or Discharge via Trajectory / Refactoring if bloomery is rejected.

---

### PYC-003 — Hazardous-fraction and disposal dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking |
| Type | Safety |
| Blocking | Yes |
| Owner | Dependency on WA-002, GR-003, WA-004 |
| First Logged | 2026-08-04 |

**Description:** Mixed salvage and thermal residues generate hazardous and negative-value fractions whose identification and disposition are still open.

**Resolution Path:** Payment via Specification on the owning unknowns.

---

### PYC-004 — Site and emergency-response dependency

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Critical |
| Priority | Blocking (for any physical pilot) |
| Type | Operational |
| Blocking | Yes for hot operations |
| Owner | Dependency on FA-001 → SP-006 |
| First Logged | 2026-08-04 |

**Resolution Path:** Payment via Specification (site assessment).

---

### PYC-005 — Energy integration quantitative claims

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No (blocks only efficiency claims) |
| Owner | Tests/Pyrolysis_Cascade.md + Energy.md (EV-001) |
| First Logged | 2026-08-04 |

**Description:** Archived targets (≥40–60 % heat recapture, near self-sufficiency) have no Forge energy balance or measured yields.

**Resolution Path:** Payment via Validation after a bounded mass-and-energy model exists; until then all such numbers remain Placeholder.

---

### PYC-006 — Metals-recovery yield claims

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Pyrolysis_Cascade.md (after GR-002) |
| First Logged | 2026-08-04 |

**Description:** ≥70 % metals recovery was stated without measurement or even a selected reduction method.

**Resolution Path:** Payment via Validation; claim retired to Placeholder until then.

---

### PYC-007 — Structural / refractory adequacy for salvaged construction

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | High |
| Priority | Blocking (for any physical build claim) |
| Type | Safety / Structural |
| Blocking | Yes |
| Owner | Dependency on EN-001 |
| First Logged | 2026-08-04 |

**Resolution Path:** Payment via Validation on EN-001 for the material classes actually used.

---

### PYC-008 — Economic viability framing

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Economic |
| Blocking | No (blocks only profitability claims) |
| Owner | Dependency on ECN-002, EV-001, FA-001, TR-001 |
| First Logged | 2026-08-04 |

**Description:** Tipping-fee ranges, break-even tonnage, and “eventual profitability” statements lack an operating-cost baseline and a site.

**Resolution Path:** Payment via Validation (site-dependent) or Discharge via Trajectory if the cascade is retained only as a technical concept.

---

### Resolution Log

- 2026-08-11: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **8** = PYC-001–008, matches local +
  `Unknowns.md`. (2) PYC-001/003/004 Critical Blocking Yes correct (hot thermal
  work / disposal / physical pilot). (3) PYC-002/007 Blocking Yes for specific
  claim classes correct. (4) No PYC-* closed; no yield or break-even claims
  advanced. Human-directed.

- 2026-08-04: Skeleton created from archived conversation + Critical/Blocking claim map. All prior quantitative performance and economic numbers retired to Placeholder / external-analogous. Eight dependency unknowns registered. File positioned strictly as Exploration under Tests/.
- 2026-08-04: **ID collision fixed, human-directed.** The original local unknown series used `PC-001` through `PC-008` (and `PC-TEST-001` through `PC-TEST-005`). `PC-` is not a free local prefix — it is already a live, repo-wide series in `Unknowns.md` tracking cross-file Process Corrections, currently running through PC-006 (e.g., the real PC-001 is "Verification Ref corrections," Resolved — unrelated to this file's halogenated-polymer dependency). Renamed throughout to `PYC-001`–`PYC-008` and `PYC-TEST-001`–`PYC-TEST-005` (confirmed unused anywhere in the repository before adopting), including the `ASM-PC-00x` assumption IDs → `ASM-PYC-00x` for consistency. No content, status, risk, or dependency changed — this was a namespace fix only, caught before merge by checking the prefix against the live global registry rather than assuming it was free.

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-08-04 | Treating the cascade as an autonomous, near-term operable process with stated yields and break-even economics | Direct collision with multiple Critical/Blocking unknowns (PL-001, CE-003, GR-002, FA-001, EN-001, ECN-002, etc.) | Only after the dependency set closes |

---

## Drift Indicators

Standard mandatory re-audit conditions per File_Template.md apply.

**File-specific:**
- Any Body text that re-introduces quantitative heat-recapture, metals-recovery, or break-even claims without a corresponding Payment via Validation entry.
- Any statement that softens or omits the hard preconditions in Scope Boundary (especially PL-001 / CE-003).
- Promotion of Status or Spec Gates without an independent audit event.
- Addition of ownership claims over Plastics, Gate_03, Air_Scrubber, or disposal doctrine.
- Physical test proposals that do not explicitly satisfy the hard preconditions.

---

## Status

**Version 0.1 — Draft, Exploration.**  
Skeleton only. No Body technical specification beyond the non-normative outline. All performance and economic claims from the archived draft are suspended pending resolution of the registered dependencies.

**What must remain constant:**  
Confidence never outruns verification.  
No hot thermal work under this file while PL-001 and CE-003 remain open.
