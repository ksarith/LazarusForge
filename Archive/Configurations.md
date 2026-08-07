> **SUPERSEDED — prior-state snapshot of Architecture/Components.md, not a chat thread.** Live file has since advanced (Open Unknowns 3→2, Last Audit updated). Correctly preserved per RIP prior-state doctrine; no unmerged content here.

components and the G.E.C.K 
# Lazarus Forge — G.E.C.K.
**(Genesis / General Environmental Construction Kit)**

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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-04 (Claude — Skeptic/Auditor); revised 2026-06-08           |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Minimum viable seed required to instantiate a new Lazarus Forge in a fresh location
- Core G.E.C.K. module list and criticality rationale
- Procurement doctrine — when purchasing is the correct bootstrap strategy
- Precision as a capability threshold concept (introductory — full treatment deferred)
- Marine variant module list and success criteria (exploratory)
- G.E.C.K. success criteria and scaling pathway to v1

**This file DOES NOT define:**
- Detailed engineering specifications for any G.E.C.K. module
- Full precision doctrine or precision tracking methodology
  (→ `Architecture/Precision.md`)
- Leviathan chassis or deep-marine systems
  (→ `Admin/Trajectories.md`)
- Energy infrastructure beyond portable generation minimum
  (→ `Operations/Energy.md`)
- Component taxonomy or classification criteria
  (→ `Architecture/Components.md`)

---

## File Purpose

This file defines the smallest coherent set of tools, data, and doctrine capable of
instantiating a new Lazarus Forge from a standing start in an unfamiliar location. It
answers: what must be in the seed, why each piece earns its place, and how the seed grows
into a functioning Forge. If this file disappeared, new deployments would lose the
canonical module list, the procurement rationale, and the criteria for declaring a G.E.C.K.
deployment successful.

---

## Assumptions

| ID      | Assumption                                                              | Basis                            | Confidence | Expiry Trigger                                      |
|---------|-------------------------------------------------------------------------|----------------------------------|------------|-----------------------------------------------------|
| ASM-001 | Deployment site has some access to commercial supply chains at v0       | Procurement doctrine foundation  | Medium     | Fully off-grid deployment with zero resupply confirmed |
| ASM-002 | Salvage is more abundant than new manufacturing at target sites         | G.E.C.K. use-case definition     | Medium     | Site survey contradicts salvage availability        |
| ASM-003 | Human operator present and trained during initial deployment            | v0 bootstrap condition           | High       | Autonomous deployment capability demonstrated       |
| ASM-004 | Terrestrial deployment is the primary v0 context                        | Scope definition                 | High       | Marine or orbital deployment becomes primary target |

---

## I. Definition

A G.E.C.K. is the smallest coherent set of tools, data, and doctrine that can:

1. Preserve embodied complexity (triage before destruction)
2. Create replacement parts for itself
3. Bootstrap power, motion, and fabrication capability
4. Retain memory across generations of artifacts

If a deployed kit cannot eventually rebuild itself, it is not a true seed.

---

## II. When a G.E.C.K. Is Deployed

A G.E.C.K. is appropriate when:

- Infrastructure is sparse, damaged, or absent
- Supply chains are unreliable or nonexistent
- Salvage is abundant relative to new manufacturing
- Human presence is limited or temporary

Typical scenarios:
- Remote terrestrial locations
- Disaster recovery zones
- Frontier industrial sites
- Early orbital / lunar deployments
- Marine deployments (see Marine Variant — Section IX)

---

## III. G.E.C.K. Capability Threshold (v0 → v1 Bridge)

A G.E.C.K. must support v0 Forge operations immediately, and enable growth toward v1
using local means.

The Forge loop that defines sufficiency: **intake → triage → process → verify → learn →
repeat.** A G.E.C.K. is sufficient if it allows this loop to close, even in degraded or
partial form. Components that allow the loop to close in a reduced application are Gate C
passes — useful, not critical. Components whose absence breaks the loop entirely are
critical.

---

## IV. Procurement Doctrine

**Purchasing equipment is a valid and often correct bootstrap strategy.**

The G.E.C.K. is a capability seed, not a proof of self-sufficiency. Self-sufficiency is
earned through Forge development over time — it is a v1 and v2 property, not a v0
requirement. At v0, the correct question is not "can we fabricate this?" but "does
fabricating this serve the Forge better than purchasing it?"

**When procurement is the correct path:**

- The component cannot be reliably fabricated at v0 capability levels
- Fabrication cost in time, material, and iteration exceeds commercial availability
- The component requires precision levels the v0 Forge cannot yet achieve
- The component is a known commercial commodity with established reliability data

**Examples of valid v0 procurement targets:** digital calipers, multimeters, servo drives,
induction heaters, quality bearings, precision lead screws, surge protectors, durable
storage media.

**Procurement does not exempt a component from triage.** Purchased components must still
be logged, provenance-tracked, and assessed for dual-use potential per Components.md
annotation standards.

**Precision and procurement are linked.** Some precision cannot be bootstrapped at v0. A
commercially available measuring instrument will outperform anything a v0 Forge can produce
to measure itself with. Purchasing precision tools early is an investment in the Forge's
ability to verify its own output — which is a Critical function. See Section V (Precision
Threshold) and Components.md item 5 (Metrology).

---

## V. Precision Threshold (Introductory)

*Full treatment in `Architecture/Precision.md` — T0–T4 tolerance tier system,
precision ceiling doctrine, metrology doctrine, and fabrication-precision feedback
loop. This section establishes the concept and its connection to G.E.C.K. seeding.*

**Precision is a capability gate.** The world's productive capability is bounded by the
precision with which materials can be measured, cut, formed, and verified. A Forge limited
to coarse tolerances cannot produce components that require fine tolerances — and those
components may include the Forge's own upgrade path.

**Precision must be monitored as a Forge metric.** At each version stage, the Forge should
be able to answer: what is our current precision ceiling, and what does it prevent us from
building? Improvement in precision ceiling is a graduation criterion, not merely a
performance optimization.

**The G.E.C.K. seeds precision capability deliberately.** The Sensing & Metrology Module
(Section VI.6) is not generic instrumentation — it is the Forge's initial precision floor.
What the G.E.C.K. brings determines what the v0 Forge can verify, and therefore what it
can reliably produce.

*Cross-reference: `Architecture/Components.md` CO-002 (Metrology Precision Thresholds).
Full precision doctrine in `Architecture/Precision.md` — cross-referenced from
Components.md Metrology (item 5), CO-002, and Version Mapping.*

---

## VI. Core G.E.C.K. Modules (Critical)

### 1. Power & Energy Module
- Portable generation (engine, solar, or hybrid)
- Energy storage (batteries, capacitors)
- Power conditioning and distribution
- **Minimum at v0: surge protection on all sensor, compute, and memory circuits**

*Reason: No power, no learning. Power instability that corrupts Artifact Memory or
Baseline Observability defeats two Critical components simultaneously.*

---

### 2. Triage & Salvage Module
- Multimeter
- Basic electrical loads
- Hand tools
- Marking and tagging system

*Reason: The Forge must recognize value before it destroys it.*

---

### 3. Motion & Actuation Module
- At least one reliable motor
- Linear motion components (rails, screws, belts)
- Basic bearings and couplings

*Reason: Motion enables every other capability.*

---

### 4. Fabrication Module (Minimal)
- Small metal AM system or CNC / hybrid tool
- Manual machining tools (drill press, grinder)
- Welding or joining capability

*Reason: The seed must be able to repair and extend itself.*

**Weld Unit Sizing Doctrine, 2026-07-19 (human-directed design principle, resolves part of UNK-008):**

Favor smaller weld units — finer passes, lower heat input per pass — over larger single-pass welding for G.E.C.K.-class fabrication. The reasoning has two independent legs, not one:

1. **Tolerance:** smaller passes carry less heat input, producing less thermal distortion and a smaller heat-affected zone per pass, which improves dimensional repeatability — the same principle behind "aim small, miss small": bounding the magnitude of each individual action bounds the magnitude of its error, even before accuracy improves. This directly feeds `Architecture/Precision.md`'s positional-accuracy and dimensional-repeatability ceiling components.
2. **Power budget, not throughput:** this is not a claim that smaller weld units finish jobs faster or use less total energy — more passes to cover the same joint means more total time, a real and accepted tradeoff. The actual benefit is to **peak power draw**: a smaller weld unit demands less peak current, which directly shrinks what the Power & Energy Module (§VI.1 above) must be sized to supply. Since a G.E.C.K.'s power module sizing is driven by the Fabrication Module's worst-case draw, a smaller weld unit means a lighter, more compact seed overall — the relevant metric for "more reasonable G.E.C.K." is peak power and mass, not job completion speed.

**Honest limit, not a monotonic rule:** this does not mean smaller is always better without bound. Excessive pass count reintroduces problems from a different direction — accumulated inter-pass residual stress, and if passes don't get adequate cooling between them, total arc-on time and cumulative heat input can approach or exceed a coarser single-pass approach. There is a real optimum weld-unit size for a given joint and material, not an unbounded improvement curve. Consistent with `Architecture/Precision.md`'s own doctrine: a stated precision or efficiency ceiling must be an honest bound demonstrated in practice, not an aspirational claim.

**Remaining open work (UNK-008, still Open):** this doctrine establishes the *design principle*, not the *specification*. Still needed: actual welding wire specification and qualification (wire diameter/alloy suited to small-pass work), the specific weld-unit size/power envelope that qualifies as "small" for G.E.C.K. purposes, and empirical validation of the distortion-reduction claim against `Operations/Gate_05_Separation_Thermal.md`'s planned wire extrusion interface once that interface exists. Cross-reference `Architecture/Precision.md` §V (Precision Threshold) for the ceiling-declaration framework this doctrine feeds.

---

### 5. Thermal Module
- Heat source capable of controlled temperatures
- Basic temperature measurement
- Insulation and containment

*Reason: Metallurgy begins with heat control.*

---

### 6. Sensing & Metrology Module
- Calipers and micrometers
- Scale
- Simple optical inspection

*Reason: Discernment requires measurement. This module establishes the v0 precision
floor — what the Forge can verify determines what it can reliably produce. Precision
instruments are a valid and recommended procurement target; commercial metrology tools
at v0 will outperform anything the Forge can self-fabricate. See Section V.*

---

### 7. Memory & Doctrine Module
- Local compute
- Durable storage media
- Core Lazarus Forge documents
- Artifact and triage logs (digital or paper)

*Reason: Without memory, growth resets every generation. Doctrine allows a newly
instantiated Forge to inherit prior lessons, operational heuristics, failure
classifications, and survival instincts without rediscovering them physically.*

---

### 8. Human Interface Module
- Manual overrides
- Clear labeling
- Simple operator instructions

*Reason: Early Forges are taught, not autonomous.*

---

## VII. What a G.E.C.K. Deliberately Does NOT Include

- High-throughput automation
- Exotic alloys
- Full autonomy
- Space-rated hardware (unless mission-specific)

These emerge through growth, not seeding.

---

## VIII. G.E.C.K. Success Criteria

A deployed G.E.C.K. is considered successful when it can:

- Replace its own failed components
- Upgrade at least one module using local material
- Generate surplus value through repair or fabrication
- Preserve and transfer its operational memory
- Demonstrate measurable precision floor for at least one output class *(Placeholder — metric not yet defined; see CO-002 in Components.md)*

---

## IX. Scaling Beyond the Seed

Once self-replacement is proven, the Forge graduates:

- G.E.C.K. → v1 Forge: Closed-loop material recycling
- v1 → v2: Reduced human dependency
- v2 → v3: In-situ resource utilization

---

## X. Marine Variant (Exploratory)

*Status: Exploratory — not binding for v0 terrestrial demonstration. Routes to
`Admin/Trajectories.md` v1/v2 scope for full specification. See GK-003 and GK-004.*

A marine G.E.C.K. seeds a Leviathan unit or Support Raft deployment from minimal
resources in an open-ocean or coastal environment. The terrestrial module list applies
with the following modifications and additions.

**Shared with terrestrial G.E.C.K. (largely unchanged):**
- Memory & Doctrine Module — waterproofed, pressure-tolerant storage
- Human Interface Module — simplified for intermittent operator contact
- Sensing & Metrology Module — corrosion-resistant instruments

**Modified modules:**

*Power & Energy Module (marine):*
- Primary: sealed battery bank, pressure-rated
- Supplemental: solar panels with marine-grade mounting, wave energy if available
- No combustion engines in submerged configurations
- Induction charging pad for Leviathan unit recharge *(Placeholder — pad design not yet
  specified; see GK-003)*

*Triage & Salvage Module (marine):*
- Waterproof multimeter and test equipment
- Marine salvage tools (cutting, lifting, retrieval)
- Contamination assessment for marine-recovered materials (biofouling, salt, corrosion)
- Tagging system rated for submersion

*Fabrication Module (marine):*
- Corrosion-resistant tooling preferred
- Welding capability adapted for humid/salt environment
- 3D printing materials must resist salt and UV degradation *(Placeholder — see GK-004)*

**Marine-specific additions:**

*Hull & Buoyancy Module (marine-critical):*
- Minimum viable hull sufficient to support module payload
- Passive buoyancy reserve — unit must surface safely without power
- SWATH or pontoon configuration preferred for stability
- Sacrificial anode system for galvanic corrosion protection *(Placeholder — material
  selection not yet specified; see GK-002)*

*Biofouling Management Module (marine-critical):*
- Sacrificial Shell System: designed colonization zones, scheduled shedding, structured
  reef substrate contribution per `Tests/Support_Raft.md` doctrine
- Fouling monitoring — detect colonization growth rate
- Shedding mechanism — mechanical, chemical, or biological *(Placeholder — mechanism
  not yet specified)*

**Marine G.E.C.K. success criteria:**
- Unit remains positively buoyant under degraded conditions
- Triage loop closes using marine-salvaged material
- Self-replacement demonstrated for at least one hull-exposed component
- Operational memory survives one full biofouling cycle

**Marine G.E.C.K. explicit non-goals (v0):**
- Full underwater operation — surface or near-surface only
- Deep pressure tolerance — Leviathan-class depth is a separate program
- Full energy independence — grid or tender-assisted charging acceptable at v0

---

## XI. Guiding Axioms

- A seed that cannot grow is cargo.
- Tools matter less than the order they are used.
- Memory is the most compact machine.
- A marine seed that cannot float is not a seed.
- Purchasing precision is not a failure of doctrine — it is triage applied to the seed itself.

---

> The G.E.C.K. is not meant to impress. It is meant to survive.

This document defines the minimal conditions for Forge genesis and should change only
with demonstrated field experience.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|----------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review  | Forge loop left implicit in prior versions | Sufficiency criterion in Bootstrap Doctrine had no falsifiable anchor | Forge loop explicitly defined: intake → triage → process → verify → learn → repeat | Anecdotal | No |
| —        | —             | —              | —           | No operational entries yet — document is pre-deployment | — | — |

*Priority entries to capture when marine variant is first deployed: (1) which terrestrial
modules transferred cleanly vs. required significant modification; (2) actual biofouling
cycle timeline vs. predicted; (3) which hull configuration provided adequate stability at
minimum cost.*

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### GK-001 — Forge loop not explicitly defined in prior versions

| Field         | Value         |
|---------------|---------------|
| Status        | Resolved      |
| Risk          | Low           |
| Priority      | Major         |
| Type          | Architectural |
| Blocking      | No            |
| Owner         | Architecture/Geck_forge_seed.md |
| First Logged  | 2026-05-04    |
| Last Reviewed | 2026-05-14    |

**Description:** The Forge loop was not explicitly defined, leaving the sufficiency
criterion in Bootstrap Doctrine without a falsifiable anchor.

**Why It Matters:** Without a defined loop, no component classification decision could be
verified as correct.

**Resolution Path:** Payment via Specification — Forge loop defined in Section III:
intake → triage → process → verify → learn → repeat. Feeds UNK-024 resolution and
UNK-026 (Graduation Rule detection circularity).

---

### GK-002 — Sacrificial anode material selection for marine hull

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Medium             |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | Architecture/Geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** Anode material (zinc, aluminum, magnesium) for the marine G.E.C.K. hull
is not yet selected.

**Why It Matters:** Wrong anode selection accelerates galvanic corrosion of the hull in
deployment environment.

**Resolution Path:** Discharge via Trajectory — standard marine engineering selection
criteria apply (zinc for saltwater, magnesium for freshwater, aluminum general-purpose).
Add material selection table to marine variant when first deployment environment is
confirmed.

---

### GK-003 — Induction charging pad design for Leviathan unit recharge

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | Architecture/Geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** Pad geometry, power transfer efficiency, alignment tolerance, and depth
rating for the induction charging interface between Support Raft and Leviathan units are
not yet defined.

**Why It Matters:** Without a defined interface, Leviathan units cannot be reliably
recharged from the Support Raft in operational conditions.

**Resolution Path:** Discharge via Trajectory — depends on Leviathan unit power envelope
(UNK-006) and hull design. Route full specification to `Admin/Trajectories.md` v1/v2 scope.

---

### GK-004 — Marine 3D printing material durability in salt/UV environment

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | Architecture/Geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** AM materials suitable for parts exposed to salt spray, UV, and biofouling
pressure in a marine deployment context have not been identified.

**Why It Matters:** Parts that degrade faster than the Forge can replace them break the
loop.

**Resolution Path:** Discharge via Lessons Learned — literature review of marine-grade
polymers used in existing ocean buoy and AUV programs (MBARI, WHOI specs are publicly
available analog data). Placeholder until first marine deployment selects a specific AM
system.

---

### GK-005 — Precision doctrine home document not yet created

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Resolved                         |
| Risk          | Low                              |
| Priority      | Minor                            |
| Type          | Architectural                    |
| Blocking      | No                               |
| Owner         | Architecture/Geck_forge_seed.md  |
| First Logged  | 2026-05-14                       |
| Last Reviewed | 2026-06-08                       |

**Description:** Section V introduced precision as a capability gate and Forge metric but
deferred full treatment to `Architecture/Precision.md`, which did not exist at time of
logging.

**Why It Matters:** Without a home document, the precision insight remained introductory
and could not be cross-referenced with full force from Components.md, Graduation Rule, or
Version Mapping.

**Resolution Path:** Resolved — `Architecture/Precision.md` created 2026-06-06. Full
precision doctrine now lives there: T0–T4 tolerance tier system, precision ceiling
doctrine, metrology doctrine, salvage equipment derating, and fabrication-precision
feedback loop. Section V cross-reference updated to `Architecture/Precision.md`. CO-002
in Components.md routes to PR-001 for resolution.

---

### UNK-008 — Welding wire specification and qualification (cross-module, ownership reassigned here 2026-07-19)

| Field         | Value                            |
|---------------|-----------------------------------|
| Status        | Open                              |
| Risk          | Medium                            |
| Priority      | Major                             |
| Type          | Technical                         |
| Blocking      | No                                 |
| Owner         | Architecture/Geck_forge_seed.md (reassigned — was `Operations/Gate_05_Separation_Thermal.md`, which had explicitly disclaimed ownership) |
| First Logged  | 2026-06-24 (approx., per `Unknowns.md`) |
| Last Reviewed | 2026-07-19                        |

**Description:** Welding wire specification (diameter, alloy) and qualification for G.E.C.K.-class fabrication is undefined. Previously listed in `Unknowns.md`'s global table as owned by `Operations/Gate_05_Separation_Thermal.md` — but that file's own Scope Boundary explicitly states this is "downstream — not yet assigned," and its Drift Trigger table calls it "the unowned cross-module gap." Reassigned here since §VI.4's Weld Unit Sizing Doctrine (above) is where the actual design reasoning now lives.

**Why It Matters:** An owning-file contradiction meant this unknown had a table entry but no file actually treating it as its responsibility — a bookkeeping gap of the same kind this repository's own audit discipline exists to catch.

**Resolution Path:** §VI.4 above establishes the design *principle* (favor smaller weld units for tolerance and peak-power reasons, with an honest non-monotonic limit) but not the *specification*. Remaining: actual wire diameter/alloy selection suited to small-pass work, empirical validation against `Operations/Gate_05_Separation_Thermal.md`'s planned wire extrusion interface once built, and the specific power/size envelope that qualifies as "small" for G.E.C.K. purposes. Cross-reference `Architecture/Precision.md` §V for the ceiling-declaration framework this feeds into.

*Surfaced by human governing authority (weld-unit-sizing design principle), formalized by Claude 2026-07-19.*

---

### Resolution Log

- 2026-07-19: Weld Unit Sizing Doctrine added to §VI.4 Fabrication Module
  (human-directed design principle) — smaller weld passes for tolerance
  (reduced heat input/distortion) and peak-power reasons (smaller Power &
  Energy Module sizing), with an explicit non-monotonic limit stated per
  `Architecture/Precision.md`'s honest-ceiling doctrine. UNK-008 (welding
  wire specification and qualification) ownership reassigned here from
  `Operations/Gate_05_Separation_Thermal.md`, which had explicitly
  disclaimed it in its own Scope Boundary — a table/file contradiction of
  the kind this repository's audit discipline exists to catch. Open
  Unknowns 2 → 3.
- 2026-05-04: **GK-001** — Resolved. Forge loop explicitly defined in Section III.
- 2026-05-04: **UNK-005** — Partially resolved. Marine G.E.C.K. variant stub added
  (Section X). Full specification deferred to `Admin/Trajectories.md` v1/v2 scope.
- 2026-05-14: File retrofitted to canonical `Admin/File_Template.md` structure. File
  State, Scope Boundary, File Purpose, Assumptions, Procurement Doctrine (Section IV),
  Precision Threshold introduction (Section V), Active Disputes, structured unknown
  tables, and Abandoned Paths added.
- 2026-05-14: **GK-005** logged — `Architecture/Precision.md` identified as needed
  home document for full precision doctrine.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from
  `Verification_Gates_LF.md` to `Admin/Verification_Gates_LF.md` (PC-001). Scope
  Boundary stale filenames corrected: Precision_LF.md →
  `Architecture/Precision.md`, Trajectories_LF.md → `Admin/Trajectories.md`,
  energy_v0.md → `Operations/Energy.md` (PC-003). All stale filenames corrected
  throughout body: Support_Raft_v0.md → `Tests/Support_Raft.md`,
  LF_File_Template → `Admin/File_Template.md`. All sidecar Owner fields corrected
  to `Architecture/Geck_forge_seed.md`. **GK-005 resolved** — `Architecture/Precision.md`
  created 2026-06-06; Section V cross-reference updated. Open Unknowns updated from
  3 to 2 (GK-005 now Resolved; GK-002, GK-003, GK-004 remain Open but are
  non-blocking trajectory items).

---

## Abandoned Paths

| Date     | Path | Why Abandoned | Reconsider? |
|----------|------|---------------|-------------|
| May 2026 | Treating purchased equipment as outside G.E.C.K. doctrine | Procurement is triage applied to the seed. Excluding it created an implicit assumption that bootstrap realism requires fabricating everything from salvage, which is false and counterproductive at v0. | No |

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
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
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
  `Verification_Gates_LF.md` to `Admin/Verification_Gates_LF.md` (PC-001). Scope
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
