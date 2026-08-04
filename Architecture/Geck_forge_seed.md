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
| Last Reviewed | 2026-08-03                        |

**Description:** Welding wire specification (diameter, alloy) and qualification for G.E.C.K.-class fabrication is undefined. Previously listed in `Unknowns.md`'s global table as owned by `Operations/Gate_05_Separation_Thermal.md` — but that file's own Scope Boundary explicitly states this is "downstream — not yet assigned," and its Drift Trigger table calls it "the unowned cross-module gap." Reassigned here since §VI.4's Weld Unit Sizing Doctrine (above) is where the actual design reasoning now lives.

**Why It Matters:** An owning-file contradiction meant this unknown had a table entry but no file actually treating it as its responsibility — a bookkeeping gap of the same kind this repository's own audit discipline exists to catch.

**Resolution Path:** §VI.4 above establishes the design *principle* (favor smaller weld units for tolerance and peak-power reasons, with an honest non-monotonic limit) but not the *specification*. Remaining: actual wire diameter/alloy selection suited to small-pass work, empirical validation against `Operations/Gate_05_Separation_Thermal.md`'s planned wire extrusion interface once built, and the specific power/size envelope that qualifies as "small" for G.E.C.K. purposes. Cross-reference `Architecture/Precision.md` §V for the ceiling-declaration framework this feeds into.

**Candidate resolution vehicle — car-derived weld feedstock (Proposed, 2026-08-03, human-directed; drafted by Copilot, audited and refined by Grok under Skeptic/Auditor constraints).** Does not resolve UNK-008. Adds a falsifiable acceptance-criteria table and a buildable apparatus sketch as a candidate pathway toward it, both explicitly Provisional/Placeholder pending first physical trials. The underlying assumption — that a salvaged car body supplies usable weld feedstock — was itself audited first: predominant feedstock must be mild/low-carbon steel (older-vehicle body panels and many structural members), coatings (paint, undercoating, zinc) must be removable in the regions processed, and heat-affected-zone behavior must stay within §VI.4's small-pass doctrine. None of that is confirmed on real stock yet — it remains PROVISIONAL/Analogous until measured.

*Acceptance criteria (WF-01 through WF-10, all thresholds Placeholder pending first physical trials):* WF-01 material identity (mild/low-carbon steel, spark test + visual, restricted for AHSS/boron-steel/exotic-alloy markers) · WF-02 coating residual (no continuous zinc layer, mechanical stripping required) · WF-03 cross-section consistency (±15% variation ceiling; strip-feed relaxation explicitly permitted if full round wire isn't achievable) · WF-04 dimensional logging (every batch logged to Artifact Memory before first weld test) · WF-05 arc stability (≥80% continuous arc on a sample weld) · WF-06 HAZ behavior (no cracking, workable with hand tools) · WF-07 joint integrity (weld fails in parent metal or at ≥ design load, not at the fusion line) · WF-08 distortion bound (stays within fit-up tolerance for the next assembly step) · WF-09 fume/process safety (cross-ref CE-006/Air_Scrubber.md — does not claim full industrial hygiene compliance) · WF-10 repeatability (≥3 independent qualifying batches from different vehicle regions — "one-off success is not a capability"). Full criterion table with measurement methods and fail conditions available on request; compressed here to keep this sidecar entry proportionate.

*Apparatus sketch (two-stage, both stages buildable from the Critical modules already listed in §VI):* **Stage 1 — Guided Strip Cutter**, mandatory: car-steel base plate, salvaged-rail guide rails, adjustable fence (target 6–12 mm initial strip width), existing 120V angle grinder for cutting, calipers for verification. **Stage 2 — Simple Roller** (optional forming) or a **rudimentary drawing die** (secondary path, more labor-intensive): salvaged rod/axle rollers, car-steel side plates, one salvaged motor via belt/friction drive, threaded-rod gap adjustment. Strip-feed welding is an explicit relaxation — full round wire is preferred, not required, for the initial capability claim. Honest limitations stated in the source draft: first-generation apparatus needs real precision (parallelism, axle alignment) and will scrap several iterations; roller wear is uncontrolled; no tension/diameter feedback (open-loop); motor/roller thermal management under sustained 120V operation is uncharacterized. This is deliberately crude — its purpose is converting the "car → weldable feedstock" assumption into a falsifiable, buildable process, not claiming industrial wire quality.

*What this does not do:* advance UNK-008's Status, change its Priority/Risk, or authorize building anything now. It is Payment via Specification only — a falsifiable criteria table and a buildable sketch, neither yet subjected to Gate 1–6 review or an adversarial battery pass. The next concrete step, if pursued, is either the first physical trial mapped directly onto WF-01–WF-10, or an adversarial pass against the thresholds themselves (Challenge Classes focused on power envelope, wear, and operator-skill assumptions).

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

- 2026-08-03: **UNK-008 gained a candidate resolution vehicle, human-directed.**
  A Copilot draft (car-derived weld feedstock: acceptance criteria WF-01–WF-10
  plus a two-stage apparatus sketch) was audited and refined by Grok under
  Skeptic/Auditor constraints before reaching this file — every cross-reference
  (§VI.4's small-pass doctrine, CE-006/Air_Scrubber.md, Precision.md's honest-
  ceiling framework) verified exact against source. Added as a candidate
  pathway, not a resolution: the underlying assumption (salvaged car body
  supplies usable weld feedstock) remains PROVISIONAL/Analogous pending
  measurement on real stock, all WF- thresholds are explicitly Placeholder,
  and the apparatus sketch is deliberately crude — meant to make the "car →
  weldable feedstock" claim falsifiable and buildable, not to claim industrial
  wire quality. UNK-008's Status, Priority, and Risk are unchanged (still Open,
  Major, Medium). Open Unknowns unchanged.

---

## Abandoned Paths

| Date     | Path | Why Abandoned | Reconsider? |
|----------|------|---------------|-------------|
| May 2026 | Treating purchased equipment as outside G.E.C.K. doctrine | Procurement is triage applied to the seed. Excluding it created an implicit assumption that bootstrap realism requires fabricating everything from salvage, which is false and counterproductive at v0. | No |
