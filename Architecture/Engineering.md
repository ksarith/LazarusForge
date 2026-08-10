# Engineering.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

> ⚠️ **Operational Safety Advisory**
> Engineering decisions directly govern physical systems that can fail catastrophically
> (structural collapse, energetic release, mechanical failure, fire, or loss of control).
> Incorrect assumptions, inadequate safety margins, or unvalidated models can cause
> injury, death, or total system loss.
> Prerequisite: Apply explicit safety factors, perform failure mode analysis, validate
> with testing, and never bypass calculations with "it should be fine." Cross-reference
> domain-specific files for thermal systems (Thermal_Systems.md), fluid mechanics and
> tribology (Friction_Dynamics.md), salvaged-frame fabrication (Mechanical_Structures.md),
> chemical and electrochemical processes (Chemistry.md), and materials processing
> (Woodworking.md, Plastics.md, etc.).
> When in doubt, increase margin or hold the design. The cost of a missed failure mode
> is always higher than the cost of conservative engineering.

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-07-05                                                          |
| Auditor          | Grok (2026-05-29); ChatGPT informal (2026-06-11); Claude retrofit; Claude — Architecture review 2026-06-21; Gemini — Exploration audit 2026-07-04; Claude — Documentation correction pass 2026-07-04; Gemini — Exploration audit 2026-07-05; Claude — EN-007 registration + reference cleanup 2026-07-05; Claude — EN-001 differentiated safety factor table 2026-07-05 |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Life Preservation; operator safety as foundational constraint |
| `Admin/Safety_Protocols.md` | PPE doctrine; safety factor cross-reference for structural operations |
| `Architecture/Facilities.md` | RDC climate baseline — substitute your deployment parameters via `Facilities.md` §VII Site Initialization Checklist |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Architecture/Mechanical_Structures.md` | Structural safety factors and margin doctrine inherited from this file |
| `Architecture/Thermal_Systems.md` | Systems engineering integration principles |
| `Architecture/Friction_Dynamics.md` | Peer file — broad engineering principles apply across all domains |
| `Architecture/Chemistry.md` | Peer file — materials behavior and derating doctrine |
| `Operations/Gate_06_Fabrication.md` | Forge-specific safety factors and tolerance standards |
| `Operations/Woodworking.md` | Wood derating and moisture behavior doctrine |
| `Operations/Plastics.md` | Materials behavior and failure mode analysis |
| `Architecture/Components.md` | Safety factors for salvaged component graduation |
| `Tests/Leviathan_testing.md` | Engineering principles for autonomous system structural design |

---

## Scope Boundary

**This file DOES define:**
- Foundational engineering principles, rules of thumb, and decision frameworks for
  the entire LazarusForge
- Core mechanical, structural, and systems engineering fundamentals
- Materials behavior overview and selection guidance
- Forge-specific parameters and safety factors
- **Reference Deployment Context (RDC)** baseline for environmental derating —
  builders must substitute their own parameters via `Architecture/Facilities.md` §VII
- Hierarchy of engineering evidence — from intuition to operational history
- Progressive path from basic to high-performance engineering

**This file DOES NOT define:**
- CNC kinematic protection protocols, salvaged gantry rigidity doctrine, or
  fabrication machinery structural specifics
  (→ `Architecture/Mechanical_Structures.md` — peer file)
- Heat transfer, thermodynamic laws, heat pump doctrine, Peltier or TEG systems
  (→ `Architecture/Thermal_Systems.md` — peer file)
- Fluid mechanics, aerodynamics, lubrication regimes, or tribology
  (→ `Architecture/Friction_Dynamics.md` — peer file)
- Chemical and electrochemical principles, corrosion doctrine, contamination
  identification, polymer degradation chemistry, or battery chemistry
  (→ `Architecture/Chemistry.md` — peer file)
- Domain-specific fabrication techniques
  (→ `Operations/Woodworking.md`, `Operations/Plastics.md`, etc.)
- Software engineering or electronics design (→ dedicated files)
- Full regulatory compliance or professional licensure requirements

**Peer file relationship:** `Architecture/Mechanical_Structures.md`,
`Architecture/Thermal_Systems.md`, `Architecture/Friction_Dynamics.md`, and
`Architecture/Chemistry.md` are peer files — same authority level, each owning
a distinct domain. This file owns broad engineering principles. Where a question
is thermal, fluid, tribological, or chemical in nature, the relevant peer file
governs. Conflicts escalate to a human contributor.

---

## File Purpose

This file exists to provide a single, durable source of engineering truth and
judgment for all Forge activities. It equips builders with condensed principles,
safety discipline, and practical parameters so that designs are safe, effective,
and improvable under real-world constraints including salvaged materials, limited
tools, and variable conditions.

**Role in the Forge operating stack:**

This file provides the physical-world constraint layer beneath the governance tier. The governing relationship is:
- `Admin/Ethical_Constraints.md` (Tier 1) — moral doctrine; hard floors; not subject to engineering override
- `Admin/Auditor_Protocols.md` (Tier 2) — epistemic doctrine; governs how all claims including engineering claims must be verified
- `Architecture/Engineering.md` (Tier 5 / Architecture) — physical-world doctrine; downstream of both

Engineering.md operationalizes the physical constraints that engineering work must satisfy. Where an engineering principle conflicts with Ethical_Constraints.md or Auditor_Protocols.md, the higher tier governs without exception. This file does not co-occupy Tier 1 with Ethical_Constraints.md — it is subject to it.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Builders have basic math and physics literacy (algebra, geometry, forces) | Typical maker/engineer entry level | Medium | Confirmed lower skill baseline |
| ASM-002 | Access to basic measurement tools and ability to prototype/test | Standard Forge shop capability | High | Fully resource-constrained deployment |
| ASM-003 | Reference Deployment Context (RDC) climate baseline applies — high humidity, thunderstorms, occasional freezes. Builders outside this climate zone must substitute their own parameters via `Architecture/Facilities.md` §VII. | RDC baseline — see `Architecture/Facilities.md` §VII | Medium | Deployment confirmed outside RDC climate zone |

---

## Body

### 1. Core Engineering Principles

- **First Principles Thinking** — Break problems down to fundamental physics (forces,
  energy, material properties) rather than analogy or tradition.
- **Margin of Safety** — Apply minimum 2×–4× factors depending on application (higher
  for critical/human-occupied structures, fatigue, or uncertainty).
- **Fail Safe, Not Fail Operational** — Design so that failures lead to non-energetic,
  fail-passive mechanical configurations (cross-reference `Admin/Safety_Protocols.md`
  for the operator-facing definition of an acceptable failed state), not continued
  operation.
- **Murphy's Law Discipline** — Assume what can go wrong will. Design accordingly.
- **Conservation of Complexity** — Complexity should only be introduced when simpler
  solutions have been exhausted. Every component, adjustment, and interface becomes
  another failure mode. Prefer passive over active systems. Prefer gravity over pumps.
  Prefer mechanical timing over software timing where feasible. Prefer standard parts
  over custom parts. Prefer repairability over peak performance.
- **Iterate Fast, Fail Small** — Prototype → test → refine before scaling.

**Rule of Thumb:** If you haven't identified at least three ways it can fail, you
haven't thought about it enough.

---

### 2. Hierarchy of Engineering Evidence

Not all engineering knowledge is equally reliable. The Forge requires explicit
confidence labeling — mirroring the epistemic doctrine in `Admin/Auditor_Protocols.md`.

| Level | Source | Confidence | Use |
|---|---|---|---|
| 1 | Intuition / experience | Lowest | Starting point only; never sufficient alone |
| 2 | Rule of thumb | Low | Quick sanity checks; document explicitly |
| 3 | Hand calculation | Medium | Required for all safety-critical sizing |
| 4 | Simulation / FEA | Medium | Hypothesis generator — validate with hand calcs |
| 5 | Prototype test | High | Required before production or deployment |
| 6 | Destructive test | High | Required for Specification-level claims |
| 7 | Operational history | Highest | Measured confidence; requires documented conditions |

**FEA doctrine:** Use FEA as a hypothesis generator. Validate critical results with
hand calculations, conservative assumptions, and physical testing. Blind trust in
FEA output without validation against hand calculations is an engineering failure,
not a tool limitation.

**Salvage note:** Unknown-history materials cannot progress past Level 2 confidence
without destructive testing. See EN-001.

---

### 3. Mechanical Engineering Fundamentals

**Conceptual distinctions that apply everywhere:**
- Stiffness vs. strength — a stiff structure resists deformation; a strong one resists
  failure. Both matter. Neither implies the other.
- Elasticity vs. permanent deformation — elastic range is recoverable; yield is not.
  Design to stay elastic under all expected loads including surprises.
- Concentrated loads vs. distributed loads — concentrated loads create stress
  concentrations; joints, holes, and abrupt changes amplify them significantly.
- Static vs. cyclic loading — fatigue failure occurs well below static yield strength.
  Any repeated load deserves a fatigue factor.

**Key relations:** Stress = Force/Area. Strain = deformation/original length.
Torque = Force × moment arm. For tribology detail see `Architecture/Friction_Dynamics.md` §7.
For thermal management detail see `Architecture/Thermal_Systems.md`.

---

### 4. Structural Engineering Basics

- Loads: Dead, live, environmental (wind, seismic, snow — consult your deployment
  region's load data; see `Architecture/Facilities.md` §VII and EN-002).
- Beams, columns, trusses, connections. Buckling, deflection, shear, bending moment.
- **Key Formula Reference:** Simple beam deflection, Euler buckling.
  Use FEA as hypothesis generator; validate with hand calculations (see §2).

**RDC climate note:** High humidity (RDC baseline) accelerates rot in wood and
corrosion in metals — favor rot-resistant species and protective coatings. Arid
deployments reduce this risk but increase thermal cycling concerns. Substitute your
climate via `Architecture/Facilities.md` §VII.

---

### 5. Materials Selection & Behavior

- Key properties: Strength, stiffness, toughness, fatigue resistance, corrosion
  resistance, density, cost, workability.
- Common Forge materials: Wood (anisotropic, moisture sensitive), metals (ductile
  vs brittle failure modes differ critically), plastics, composites.
- **Derating for salvaged materials:** Reduce allowable stresses for temperature,
  moisture, fatigue, and unknown history. As of 2026-07-05, unknown-history
  structural members follow the **differentiated interim safety factor table**
  in §8 by material category (structural steel 4×, aluminum 6×, timber 5×
  plus mandatory inspection, unidentified material — do not use structurally
  until classified). This replaces the prior single undifferentiated 6×+
  blanket floor. §8 is the authoritative table; this section may not restate
  or override it. (History: this section previously stated a 3× interim
  figure that conflicted with §8 and the EN-001 sidecar, corrected 2026-07-04
  to a uniform 6×+; that uniform floor has now itself been superseded by the
  differentiated table — see Resolution Log.)
- See `Architecture/Chemistry.md` for corrosion behavior. See `Architecture/
  Mechanical_Structures.md` for fabricated-frame specifics.

---

### 6. Systems Engineering & Integration

- Define requirements → architecture → interfaces → verification.
- Interface management (mechanical, electrical, thermal).
- Reliability, maintainability, scalability.
- **Documentation discipline:** If it isn't written down with a date and a confidence
  level, it didn't happen. Drawings, BOMs, revision control, and test records are
  not administrative overhead — they are the mechanism by which the Forge accumulates
  knowledge instead of repeating the same mistakes.

---

### 7. Design & Analysis Methods

- Sketching → CAD → FEA → Physical prototype → Testing (see §2 Hierarchy of Evidence).
- **FMEA:** Before any design is built, identify: what can fail, how likely, what the
  consequence is, and what the detection mechanism is. A design with no identified
  failure modes has not been analyzed — it has not been shown free of failure modes,
  only assumed to be, and an unlabeled assumption is not a substitute for analysis.
- **Low-tech detection methods:** In resource-constrained, sensor-scarce deployments,
  detection mechanisms need not be instrumented. Acceptable analog methods include:
  visual witness marks across fasteners and joints (paint or scribe lines to reveal
  slip), plumb lines or string lines to reveal structural creep or drift over time,
  and manual tap-testing to reveal delamination or internal voids in composite or
  laminated members. An FMEA's "detection mechanism" field may cite one of these
  without requiring instrumentation.
- Tolerance analysis: worst-case vs. statistical. For salvage stock, always worst-case.
- **High-performance caution:** Topology optimization, lattice structures, and
  composites are powerful tools that also create failure modes that are harder to
  inspect, repair, and understand. Apply only when simpler approaches are exhausted
  (Conservation of Complexity, §1). See EN-006.

---

### 8. Forge-Specific Parameters & Standards

**Common Safety Factors:**
- Static non-critical: 2–3×
- Structural/human load, known material with certified spec: 4×

**Salvaged/unknown-history structural materials (interim differentiated table
— added 2026-07-05, see EN-001):**

| Material Category | Interim Factor | Basis (brief) |
|---|---|---|
| Structural steel, unknown grade (ferrous, non-cast, magnetic, no visible casting texture) | **4×** | Ductile failure mode gives visible warning (yielding/deflection) before fracture. Scrap structural steel's real-world strength band is comparatively narrow — most unidentified structural steel meets or exceeds mild-steel-equivalent yield strength. Lower than the prior blanket floor specifically because the failure mode itself is forgiving, not because the material is better-characterized. |
| Aluminum extrusion, unknown alloy | **6×** | Alloy series (2000/6000/7000-class) vary roughly 3–4× in yield strength and differ in notch sensitivity and fatigue tolerance. Visual inspection alone cannot distinguish series. Kept at the prior blanket floor — the material class itself carries too much property variance to justify reduction without testing. |
| Salvaged timber, unknown species/moisture history | **5×**, plus **mandatory** moisture-content check and visual probe for rot/insect damage before the factor applies at all | Species and moisture content both swing strength significantly, and decay may not be visible externally. Partial offset: failure mode is usually progressive and visible (splintering, creaking) rather than sudden, and the mandatory inspection step removes the single largest hidden variable (active decay) before the factor is even relied on. |
| Unidentified alloy/material — cannot be placed in any category above | **Do not use structurally until classified.** No factor applies to an unclassified material. | Without knowing the base material class, no safety factor is trustworthy — a factor implies a known failure mode to derate against, and an unclassified material has none. Minimum field identification (magnet test, spark test, density/float test, or streak test — see `Operations/Gate_02_Triage.md`) is a precondition, not an optional refinement. |

*[Internally Derived — pending EN-001 destructive testing across all four
categories. This table replaces, not merely restates, the prior single 6×+
blanket floor — see Resolution Log. It remains conservative by design; it is
differentiated because failure mode and property variance genuinely differ
by category, not because any category is considered well-characterized yet.]*

**Units:** Default metric (mm, N, MPa) with imperial soft conversions. Be explicit.

**Tolerances:** ±0.5 mm general fabrication; tighter for bearings and interfaces.

**Environmental Derating** *(RDC baseline — substitute via `Architecture/Facilities.md` §VII)*:
- Wood strength: Reduce 20–30% for sustained high humidity (RDC). Arid deployments
  may use lesser derating; tropical deployments verify against local species data.
- Fastener corrosion: Specify galvanized or stainless in wet/humid environments.
- **Facilities.md unavailable fallback:** If `Architecture/Facilities.md` site
  parameters are unavailable, unverified, or not yet initialized for the
  deployment, builders must default unconditionally to the most conservative
  values within the RDC baseline stated in this file. Do not interpolate,
  average, or assume a milder climate in the absence of confirmed site data.

**Measurement Standards:** Calibrate tools regularly. Use moisture meters for wood,
torque wrenches for critical fasteners.

---

### 9. Measurement, Testing & Validation

- Always test to failure on non-critical samples when possible.
- Non-destructive testing: visual, tap test, deflection.
- Data-driven iteration: Record loads, failures, conditions.
- **Validation chain:** A design not validated at Level 5 or above (see §2) cannot
  make Specification-level claims in any dependent file.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|--------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-29 | Anecdotal | Relying solely on intuition for safety margins | Near-miss structural issues | Explicit calculation + margin is non-negotiable | Anecdotal | Yes |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| — | — | — | — |

---

## Drift Indicators

- Scope boundary revised to absorb thermal, fluid, tribology, or chemical
  doctrine from peer files without logging a dispute — trigger re-audit.
- FEA guidance weakened to allow simulation without hand-calculation validation
  — trigger re-audit.
- Conservation of Complexity principle removed or softened — trigger re-audit.
- Hierarchy of Evidence table removed or simplified below 5 levels — trigger re-audit.
- Verification Ref changed away from `Admin/Verification_Gates.md`.
- §5 and §8 interim safety-factor values diverge again — trigger immediate
  re-audit; this file has already had one uncaught internal contradiction on
  this exact value (see Resolution Log, 2026-07-04).

---

## Auditor Notes & Unknowns

### EN-001 — Validated safety factors for salvaged unknown-history materials

| Field | Value |
|-------|-------|
| Status | In Progress |
| Risk | High |
| Priority | **Critical** |
| Type | Technical |
| Blocking | **Yes** |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-07-05 |

**Description:** No Forge-specific *tested* safety factor table exists for
salvaged materials with unknown history — that part is still true. What
changed 2026-07-05: the blanket, undifferentiated 6×+ floor has been
replaced with a differentiated interim table (§8) reasoned per material
category from failure-mode behavior and known property variance (structural
steel 4×, aluminum 6×, timber 5× + mandatory inspection, unidentified
material barred from structural use until classified). This is real
progress, not resolution — every value in that table remains Internally
Derived, none are backed by an actual destructive test yet.

**Why It Matters:** A salvage system without conservative derating tables is
effectively operating blind. No structural specification in any Forge file
may be promoted to Specification confidence until this is resolved. This is
the most important unknown in the Architecture layer.

**Resolution Path:** Four Sandbox hypotheses registered in
`Tests/Chaos_Dynamics.md` §9 (SB-001 through SB-004, 2026-07-05), one per
material category in the §8 table, defining the destructive test each
would need to move from Internally Derived to Experimentally Verified.
Currently logged **Deferred** pending confirmation of physical testing
capability — promote to EXP-ID and begin physical execution per category
as testing resources become available. EN-001 moves to Resolved only when
all four categories have completed at least one destructive test series
and the §8 table is updated with real data; partial completion should
update individual category rows in place rather than waiting for all four.

---

### EN-002 — Deployment-specific environmental load data not compiled

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-06-11 |

**Description:** Precise local wind, snow, seismic, and humidity derating values for
the deployment region have not been compiled. The RDC baseline provides starting
values but is not a substitute for deployment-specific data. Builders in high-wind
or seismic zones using RDC baseline values will be under-margined.

**Resolution Path:** Each deploying builder compiles from their regional equivalent
of ASCE 7 and local meteorological data. The `Architecture/Facilities.md` §VII
Site Initialization Checklist Climate Parameters section is the interim capture
mechanism.

---

### EN-003 — Materials database for salvaged stock

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-06-11 |

**Description:** No structured database of material properties for common salvage
stream items exists. Builders currently rely on published spec sheets that may not
match actual salvage stock composition or condition.

**Resolution Path:** Build incrementally from destructive test data as operations
begin. Start with the highest-volume salvage categories identified at Gate_02 triage.

---

### EN-004 — High-performance low-tech fabrication methods

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-06-11 |

**Description:** Methods for achieving high-performance outcomes with limited tooling
(hand tools, basic welding, salvaged fasteners) are not documented. This limits
builder capability in low-infrastructure deployments.

**Resolution Path:** Document via Lessons Learned as builders accumulate experience.
Not blocking.

---

### EN-005 — Verification testing protocols

| Field | Value |
|-------|-------|
| Status | In Progress |
| Risk | Medium |
| Priority | Major |
| Type | Governance |
| Subtype | Vehicle |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-07-04 |

**Description:** Standardized verification testing protocols for Forge-built
components do not exist. The Hierarchy of Evidence (§2) defines confidence levels
but does not specify what a Level 5 or Level 6 test looks like for specific
component types.

**Resolution Path — updated 2026-07-04:** `Tests/Chaos_Dynamics.md` was created
2026-07-04 and supersedes this entry's original candidate names — the
previously-considered *Tests/Verification Methods* and *Admin/Test Protocols*
file names (retired, neither was ever created; rendered here as plain text,
not folder-prefixed paths, so no cross-reference parser attempts to resolve
them — see EN-006 Resolution Log, 2026-07-05). It defines the general Sandbox → Promotion Gate → EXP-ID → destructive
testing → derating pipeline this unknown asked for, with an explicit
Confirmed/Partially Confirmed/Refuted/Inconclusive feedback loop back to the
originating hypothesis. Status held at **In Progress / Vehicle** rather than
Resolved: the new file provides the process framework, but does not yet specify
what a Level 5/6 test looks like for any *specific* component type — that
requires actual EXP-ID cycles to run through the pipeline. Tests/Chaos_Dynamics.md
§8 self-declares this unknown resolved; that declaration is not accepted at face
value here pending that follow-through, consistent with the repository's
self-approval prohibition. Full resolution trigger: first completed EXP-ID cycle
producing a concrete Level 5/6 test definition for at least one component
category.

---

### EN-006 — Advanced engineering section drift risk

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Structural |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-06-11 |
| Last Reviewed | 2026-07-04 |

**Description:** Section 7 (high-performance engineering) covers topology
optimization, lattice structures, and composites. These subjects are deep enough
to eventually warrant their own file. As the Forge matures, this section is the
most likely to require splitting into `Architecture/Advanced_Engineering.md`
(planned) or `Architecture/Performance_Engineering.md` (planned). Neither file
currently exists in Routing.md's canonical registry — these are aspirational
targets, not active references.

**Resolution Path:** Monitor section length and complexity. Trigger split when
Section 7 exceeds 150 lines or when a downstream file begins citing it as a
domain authority rather than a survey.

---

### EN-007 — Dissimilar material junction fatigue profiles undefined

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-07-05 |
| Last Reviewed | 2026-07-05 |

**Description:** §6 (Interface Management) addresses broad materials selection
but has no standard treatment for junctions between highly dissimilar salvaged
materials under cyclic or environmental loading — e.g., high-stiffness
unknown-history metal fastened directly to low-stiffness, moisture-variable
timber. Such junctions concentrate stress at the fastener interface and are
prone to silent tear-out, shear, or localized rot/galvanic degradation that
isn't visible until failure.

**Why It Matters:** This compounds EN-001 — even a correctly-derated
individual member (per the §8 differentiated table) can fail at a
poorly-isolated junction to a dissimilar material, which no per-material
safety factor addresses because it is a bulk-material margin, not a
joint-interface specification.

**Resolution Path:** Define standard mechanical isolation methods for
junctions coupling salvaged metals to anisotropic organic or dissimilar
materials — e.g., sacrificial composite shims, specified fastener
distribution/spacing, or galvanic isolation layers. Candidate feeder into the
`Tests/Chaos_Dynamics.md` pipeline once a concrete joint geometry hypothesis
exists to test.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-05 Exploration audit.*

---

### Resolution Log

- 2026-07-05 (second entry, same day): **EN-001 — blanket 6×+ floor replaced
  with differentiated interim table.** §8 now carries four material-category
  rows (structural steel 4×, aluminum 6×, timber 5× + mandatory moisture/rot
  inspection, unidentified material barred from structural use until
  classified) reasoned from failure-mode behavior (ductile vs. brittle) and
  known material-property variance per category, not from new test data —
  every value remains Internally Derived. §5's cross-reference updated to
  match. EN-001 status moved Open → In Progress; this is real movement, not
  resolution. Four Sandbox hypotheses (SB-001–SB-004) registered in
  `Tests/Chaos_Dynamics.md` §9, one per category, logged Deferred pending
  confirmation of physical destructive-testing capability — this is the
  first real use of that file's Sandbox pipeline since it was built.
  EN-007's cross-reference to EN-001 updated to point at the table rather
  than the retired single-value floor.

- 2026-07-05: **EN-007 logged** (dissimilar material junction fatigue — see
  sidecar above), surfaced by Gemini's Exploration audit. Open Unknowns
  6 → 7. Same audit's G5 finding on EN-005's two retired candidate file
  names (`Tests/Verification_Methods.md`, `Admin/Test_Protocols.md`) was
  checked directly and found partially valid: the 2026-06-21 Resolution Log
  claimed all four aspirational/retired file references in this section were
  tagged `(planned)`, but only the two EN-006 references
  (`Architecture/Advanced_Engineering.md`, `Architecture/Performance_Engineering.md`)
  actually carried that tag — the two EN-005 names never did. Corrected:
  the two EN-005 names are no longer rendered as folder-prefixed backtick
  paths (they were never planned files, only retired candidate names, so
  `(planned)` would have been inaccurate; converted to plain text instead
  to remove them from cross-reference parsing entirely). Gemini's broader
  claim that this "breaks automated compilation" was not independently
  verified against `Automation/AUDIT_HARNESS.py` in this pass — treat the parser
  risk as plausible, not confirmed.

- 2026-07-04 (second entry, same day): EN-005 sidecar updated following
  confirmation that `Tests/Chaos_Dynamics.md` was created and committed.
  Status moved Open → In Progress, Subtype Vehicle — not closed to Resolved,
  despite the new file's own §8 declaring EN-005 "resolved here," because the
  file provides only the general process framework and has not yet run a
  single hypothesis through to a concrete Level 5/6 test definition for any
  component type. Cross-reference note: `Discovery.md` and `Routing.md` both
  updated same session to register the real file (previously tracked only as
  a `[PLANNED]` entry); two structural gaps were found on review and are not
  yet patched in the file itself — missing mandatory Navigation Anchors block
  and no File State table (Verification Ref, Auditor, Open Unknowns, Spec
  Gates all absent).
- 2026-07-04: Documentation correction pass following Gemini Exploration audit
  (2026-07-04) and Claude review. Six findings actioned: (1) §5's interim
  unknown-history safety factor corrected from 3× to 6×+ to match §8 and the
  EN-001 sidecar — this was an uncaught internal contradiction, not an
  intentional two-tier system; a Drift Indicator was added to catch recurrence.
  (2) File State Open Unknowns field corrected 5→6 — the 2026-06-21 Resolution
  Log entry claimed this update but the field itself was never changed. (3)
  EN-005 and EN-006 references to `Tests/Verification_Methods.md`,
  `Admin/Test_Protocols.md`, `Architecture/Advanced_Engineering.md`, and
  `Architecture/Performance_Engineering.md` tagged `(planned)` per Discovery.md's
  Fallacy 6 (Hallucinated Files) rule — none exist in Routing.md's canonical
  registry. (4) "Safe" language tightened in §1 (Fail Safe principle now
  cross-references Safety_Protocols.md and specifies non-energetic/fail-passive
  states) and §7 (FMEA text no longer uses unbounded "assumed safe"). (5) §7
  gained a low-tech hazard detection sub-clause (witness marks, plumb lines,
  tap-testing) addressing a gap where FMEA's "detection mechanism" requirement
  had no guidance for sensor-scarce deployments. (6) §8 gained an explicit
  fallback clause for when Facilities.md site parameters are unavailable or
  unverified — defaults unconditionally to RDC conservative baseline.
  **Not actioned:** Gemini's recommendation to apply Truth Provenance Labels
  to every quantitative value in §5/§8 (2–3×, 4×, 20–30%, etc.) was reviewed
  and judged disproportionate for a Draft-tier, 3/6-gate file — full
  provenance labeling is treated as Specification-tier rigor. A lighter label
  was applied only to the corrected 6×+ value, since that number was the
  subject of this session's correction. **Also not actioned:** Spec Gates
  field left at 3/6 despite Gemini's gate-by-gate table showing five of six
  gates passing — self-approval of gate status is prohibited, and this was a
  documentation pass, not a formal gate audit against Verification_Gates.md.
  Flagged for a dedicated gate-verification session before that field is
  touched, particularly given GOV-011 (Unknowns.md) was just registered for
  this exact failure pattern elsewhere in the repository.
- 2026-06-21: File Purpose corrected — "doctrine triad" framing replaced with explicit tier stack. Engineering.md is Tier 5 (Architecture), downstream of Ethical_Constraints.md (Tier 1) and Auditor_Protocols.md (Tier 2). Prior framing implied co-equal tier status with Tier 1 governance files, which is architecturally incorrect and creates a potential exploit path where engineering authority could be cited against a hard ethical floor. No body content changed. Eight findings actioned:
  (1) Navigation Anchors, Upstream/Downstream tables added. (2) Spec Gate
  advanced 0→3 — scope boundary, falsifiable safety factors, and peer
  relationships all clearly established. (3) Conservation of Complexity
  added to §1 Core Principles — joins First Principles Thinking, Margin of
  Safety, Fail Safe, Murphy's Law, and Iterate Fast. (4) Hierarchy of
  Engineering Evidence added as §2 — seven-level ladder from intuition to
  operational history; mirrors Auditor_Protocols epistemic structure; FEA
  doctrine updated to "hypothesis generator, validate with hand calcs."
  (5) §2 Mechanical fundamentals reframed around conceptual distinctions
  (stiffness vs. strength, static vs. cyclic) rather than terminology lists.
  (6) EN-001 elevated from High/Critical to explicitly Critical/Blocking with
  stronger "operating blind" framing. (7) EN-006 added — Section 7 advanced
  engineering drift risk. (8) All Arkansas/RDC abstraction applied — ASM-003
  updated, §3 and §8 environmental notes updated. Role in doctrine triad
  added to File Purpose. Open Unknowns updated 5→6 (note: this field update
  did not actually take effect — see 2026-07-04 entry above). Last Audit updated.
- 2026-05-31: Scope boundary updated — peer file references added.
  Stale references to retired planned files removed. Verification Ref corrected.
  Safety advisory cross-references updated. Drift Indicators section added.
