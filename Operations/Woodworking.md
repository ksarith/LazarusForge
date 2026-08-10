# Woodworking.md — Timber Sourcing, Processing & Fabrication

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Felling operations carry lethal risk from falling trees, barber-chair failures, and chainsaw kickback — never fell alone and always establish two escape routes before the first cut. Power tool operations produce blade ejection, kickback, and entanglement hazards that cause permanent injury in fractions of a second. Fine wood dust is explosive at sufficient airborne concentration and causes permanent respiratory damage from chronic exposure — source capture dust extraction is required at all power tool stations. Several common species (walnut, cedar, yew) produce toxic or sensitizing dust; mixed-species milling has uncharacterized synergistic exposure effects — see WW-004. PPE (eye, ear, respiratory) and machine guarding are non-negotiable prerequisites before any powered operation begins. When in doubt, shut down. The cost of a stopped run is always recoverable.

---

## File State
| Field | Value |
|---|---|
| Status | Draft |
| Body Stability | Volatile |
| Spec Gates | 0/6 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-30 (Gemini — Systems/Auditor); revised 2026-06-08           |
| Auditor | Gemini — Systems/Auditor |
| Open Unknowns | 5 |
| Active Disputes | 0 |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

## Scope Boundary
**This file DOES define:**
 * Timber sourcing hierarchy — salvage, urban, storm-fall, and standing tree.
 * Felling and chainsaw safety doctrine for small-scale operations.
 * Green wood handling, rough dimensioning, anisotropic behavior, and drying doctrine.
 * Structural deployment of woodgrain (utilizing natural fiber orientation as an asset).
 * Power tool and hand tool milling workflows for irregular salvage stock.
 * CNC/router fixturing methods for slabs and live-edge material.
 * Heat treatment and surface modification methods.
 * Joinery, adhesive selection, and assembly doctrine.
 * Finishing doctrine for indoor and outdoor applications.
 * Waste valorization hierarchy through to basic paper making.
 * Dust and species-specific hazard doctrine based on climate-zone variables.

**This file DOES NOT define:**
 * CNC toolpath generation, G-code, or CAM software workflows.
 * Full shop-wide dust extraction system design (→ `Operations/Air_Scrubber.md`).
 * Structural engineering calculations for load-bearing wooden members.
 * Commercial lumber grading standards or large-scale industrial forestry operations.
 * Facility siting, shop layout, and clearance zone requirements
   (→ `Architecture/Facilities.md` — FA-001).
 * Formal hearing conservation program and PPE sourcing standards
   (→ `Admin/Safety_Protocols.md`).

## File Purpose
This file governs the full processing chain for wood within the Lazarus Forge — from standing tree or salvage source through to finished functional or structural object. Its emphasis is on salvaged and urban timber, irregular and green stock, and low-to-high technology methods appropriate for a self-reliant fabrication environment across variable high-humidity environments.

Wood is an anisotropic, living material. Unlike metal or polymers, it cannot be treated as a uniform substrate. Premature milling of green stock, ignoring grain orientation, inadequate drying, improper fixturing of irregular slabs, and uncontrolled dust exposure are recurring failure modes that destroy material and injure operators. This file establishes a durable baseline from the first cut to the finished surface.

## Assumptions
| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Basic power tools and hand tools are available at v0 bootstrap | Typical fabrication shop context | Medium | Fully off-grid or remote deployment confirmed — tool availability reassessed |
| ASM-002 | Target biome features diverse hardwood/softwood distribution with high seasonal humidity | Global temperate/subtropical deployment assumption | High | Relocation to arid or arctic biomes |
| ASM-003 | Dust extraction and PPE are implemented per Operations/Air_Scrubber.md doctrine | Cross-module dependency | Medium | Independent shop air quality measurement validates or invalidates current approach |
| ASM-004 | Salvaged and urban timber is structurally usable after proper drying and defect assessment | Analogous — urban timber salvage practice | Low | WW-002 resolved — long-term performance of salvaged urban timber characterized |
| ASM-005 | Air drying schedules must scale dynamically based on local ambient relative humidity (RH) | Standard timber physics | High | WW-001 resolved — deployment-site validated drying metrics established |

---

## 1. Sourcing Hierarchy & Material Selection
Consistent with the *Salvage Before Reduction* principle, timber enters a sourcing priority sequence:
 1. **Salvaged urban and storm timber** — downed trees, demolition lumber, storm fall. Highest priority. Zero harvest cost, reduces waste stream.
 2. **Pallet and packaging wood** — widely available, often kiln-dried, usable for smaller stock. Inspect for heat treatment stamps (HT) vs. methyl bromide treatment (MB — **reject** for indoor use).
 3. **Standing tree harvest** — only when salvage sources are insufficient for the application. Requires felling doctrine.
 4. **Commercial lumber** — purchased per *purchase-what-cannot-be-produced* doctrine when salvage stock cannot meet dimensional or quality requirements.

**Ingrown Foreign Matter (IFM) Screening Protocol**

Salvaged urban and storm timber carries a high probability of containing embedded metal or stone (fences, spikes, wire, overgrown signage). Processing unverified salvage stock carries terminal risk to tooling and high kinetic hazard to the operator.

 * *Visual Triage:* Scan log surfaces for localized swelling, unnatural bark patterns, or metallic staining (iron tannin reactions manifest as deep blue/black streaks in oaks).
 * *Electromagnetic Screening:* Every piece of salvage timber must pass a dual-axis metal detector scan prior to hitting any powered blade (bandsaw, jointer, planer, or CNC). Flag and isolate any deep-signal zones. See WW-005.
 * *The "Bike-in-a-Tree" Rule:* If a log segment shows deep, unextractable structural contamination, it is immediately downgraded from fabrication feedstock and routed to high-clearance mechanical splitters for firewood, or bypassed directly to biochar reduction.

### Standard Functional Typologies (Biome-Agnostic)
Rather than limiting documentation to specific regional flora, timber is classified by structural archetype:
 * **High-Density Siliceous/Interlocked Hardwoods:** (e.g., White Oak equivalents, Hickory equivalents). Chosen for extreme shock resistance, tool handles, high-stress structural joints, and rot-resistant outdoor deployments.
 * **Highly Unstable/Tension-Prone Hardwoods:** (e.g., Sweetgum/Eucalyptus equivalents). Plentiful but prone to severe warping. Must be dried under extreme physical restraint and restricted to non-structural utilities.
 * **Resinous Softwoods:** (e.g., Pine/Fir equivalents). Rapid growth, highly accessible structural stock. Soft, easy to mill, but requires chemical or thermal stabilization for exterior ground-contact use.
 * **High-Tannin/Phenolic Woods:** (e.g., Cedar/Walnut equivalents). Excellent natural insect and rot resistance. Dust is universally a high-tier respiratory sensitizer.

## 2. Utilizing Woodgrain as an Asset (Anisotropic Engineering)
Wood is completely non-isotropic; its tensile, compressive, and shear strengths depend entirely on grain direction. Forge components must be engineered to exploit these mechanics rather than fighting them.

### Grain Alignment Rules
 * **The Tensile/Columnar Asset:** Wood fibers have massive tensile strength along the grain. Structural columns, levers, and handles must align the grain continuously along the axis of primary force.
 * **Avoiding Shear Splitting:** Wood splits effortlessly *parallel* to the grain. Never position fasteners or drill holes in a perfectly straight line along a single grain line, as this acts as a wedge, inducing a mechanical cleavage plane.
 * **Curvilinear Grain Tracking:** When fabricating curved functional parts (e.g., tool handles, structural brackets), do not cut a curved profile across flat, straight-grained wood. This creates dangerous "short grain" zones that fail instantly under minimal load. Seek out natural tree forks, crotches, or curved limbs where the wood fiber naturally grew in a curve, capturing continuous structural integrity.

### Managing Dynamic Moisture Movement
Wood moves perpetually across its life cycle, expanding and contracting as relative humidity changes.
 * **Tangential vs. Radial Shift:** Wood shrinks and expands roughly twice as much *tangential* to the growth rings as it does *radially*, and virtually not at all *longitudinally* (along the length).
 * **Design for Movement:** Joints must never restrict cross-grain movement. Gluing or hard-fastening a wide solid tabletop grain perpendicular to a rigid cross-brace will cause the wood to self-destruct, split, or cup drastically. Use slotted mechanical fasteners or floating joinery.

## 3. Felling and Chainsaw Doctrine
Felling is the highest-risk operation in this file. It is governed by a conservative doctrine regardless of tree size.

**Never fell alone.** A second person is required for any felling operation — not to assist with cutting, but to maintain a wider spatial awareness and call stop if conditions change unexpectedly.

**Pre-fell assessment:**
 * Identify the natural lean direction of the tree.
 * Identify two escape routes at 45° angles behind and away from the planned fall direction — clear these routes before the first cut.
 * Assess for widow-makers (dead branches overhead) — do not fell under them.
 * Assess for barber-chair risk: trees under tension, leaning trees, or trees with significant rot at the base can split vertically and kick the butt backward unpredictably. If barber-chair risk is present, do not fell without specialist assessment.
 * Check fall zone for people, structures, and utility lines.

**Cutting sequence:**
 1. Face cut (notch) on the fall side — depth 1/4 to 1/3 of trunk diameter, angle 60–70°. This controls the fall direction.
 2. Back cut on the opposite side — slightly above the bottom of the face cut. Leave a hinge of uncut wood. The hinge steers the fall.
 3. Do not cut through the hinge. A severed hinge loses directional control.
 4. When the tree begins to move, disengage the saw, set the brake, and move immediately along one of the pre-cleared escape routes — do not watch the tree fall.

**Chainsaw safety minimums:**
 * Cut-resistant chaps or chainsaw trousers.
 * Helmet with face shield and integrated hearing protection.
 * Steel-toe boots and high-dexterity gloves.
 * Chain brake functional and tested before each session.
 * Never operate a chainsaw above shoulder height.

**Limbing and bucking (sectioning the felled tree):**
 * Work from the trunk outward on limbs.
 * Assess tension and compression in each limb before cutting — a branch under compression will pinch the bar; a branch under tension will kick.
 * Buck (cross-cut) into manageable sections at the felling site before transport — moving whole logs is a separate injury risk.

## 4. Green Wood Handling and Drying
Green wood milled to final dimension will warp, check, and crack as it dries. The correct sequence is: **rough dimension → dry → final mill.**

**Rough dimensioning before drying:**
 * Crosscut to rough length (add 6–12 inches over final length for end checking).
 * Rip to rough width (add 1–2 inches over final width).
 * Do not plane or joint to final dimension while green.
 * End-seal all exposed end grain immediately after crosscutting — paint, wax, or commercial end-grain sealer. End grain dries 10–15× faster than face grain and is the primary checking site.

**Moisture content targets:**
 * Outdoor structural use: 15–19% MC acceptable.
 * Indoor furniture and electronics integration: 6–8% MC.
 * Measurement: Pin-type moisture meter minimum; pinless preferred for non-destructive checking of drying progress.

**Air drying stack doctrine:**
 * Stack on stickers (1-inch square spacers) at 12–16 inch intervals across the width.
 * Stickers must be aligned perfectly vertically across the stack — misaligned stickers introduce localized leverage points that cause permanent bowing.
 * Elevate the stack off the ground minimum 12 inches to clear ground moisture and maximize base airflow.
 * Cover the top only — sides must remain open for cross-ventilation.
 * Baseline calculation: 1 year per inch of thickness, adjusted dynamically via local equilibrium moisture content (EMC) tracking (see WW-001).
 * Tension-prone species: Dry under physical restraint (heavy weights or ratcheted straps over the top of the stack) to limit twist.

**Accelerated drying options:**
 * Solar kiln: Simple construction, greenhouse-effect air cycling, significant time reduction, suitable for v0 bootstrap.
 * Dehumidifier kiln: Closed insulation loop, requires dedicated power draw.
 * Do not accelerate drying beyond the wood's specific fiber saturation threshold — surface checking and case-hardening (dry shell trapping a wet core) both result from premature ambient relative humidity drops.

## 5. Milling — Hand Tools, Power Tools, and CNC

⚠️ **Pre-Milling Gatekeeper: Hard Inclusions**
Prior to the first face pass on a jointer or resaw on a bandsaw, verify the piece has cleared the IFM Screening Protocol. Hitting embedded steel or stone with high-speed tool steel or carbide cutters induces instantaneous tool fracturing, projectile ejection, and severe machine damage.

### Hand Tools
Hand tools are the baseline capability — they function without power, develop operator material sense, and handle operations that power tools cannot safely perform on irregular stock.
 * *Core kit minimum:* hand saw, jack plane, smoothing plane, chisels (1/4", 1/2", 3/4", 1"), marking gauge, combination square, mallet.
 * Hand tools are primary for final fitting of joinery, working with short or awkward pieces that cannot be safely fed through power tools, and finishing surfaces where power tool tearout is structurally unacceptable.

### Power Tool Milling Sequence
For converting rough stock to dimensioned lumber:
 1. **Jointer** — flatten one face (reference face).
 2. **Planer** — flatten opposite face parallel to reference face; establish thickness.
 3. **Tablesaw or bandsaw** — rip to width with reference face against fence.
 4. **Crosscut saw or miter saw** — cut to final length.

**Irregular and live-edge stock:**
Salvage timber frequently arrives without a flat reference face. The jointer cannot safely process highly cupped, bowed, or live-edge stock without a sled.
 * *Router sled method:* Build a flat track wider than the workpiece; secure the workpiece to the track base with wedges/hot glue in waste areas; run the router across the surface to establish a reference plane; flip and joint or plane the opposite face.
 * *Bandsaw sled method:* Secure the workpiece to a flat sled; resaw to establish one flat face; proceed to planer.

### CNC and Router Fixturing for Slabs and Irregular Stock
CNC routing of salvage slabs represents a significant work-holding problem. Irregular geometry, variable thickness, and live edges work against standard hold-down methods.

**Vacuum fixturing:**
 * Effective for flat or near-flat stock with sufficient surface area.
 * Requires a vacuum pump and spoilboard with vacuum channels or gasket grids.
 * Minimum surface area for reliable hold: approximately 50% of spoilboard coverage with the workpiece — irregular slabs with large voids or live edges may not achieve sufficient contact.
 * Test hold before running: attempt to physically shift the workpiece by hand before beginning the cut cycle.

**Mechanical fixturing for slabs:**
 * Sacrifice screws driven directly into waste areas outside the finished boundary — most reliable method for highly irregular stock.
 * Locate screw positions digitally before generating toolpaths — screws must not intercept the path of any tool bit.
 * Toggle clamps or cam clamps at the perimeter where geometry allows.
 * Wedge packs under low corners to prevent workpiece rocking before clamping down.

**Surfacing irregular slabs (flattening):**
 * First pass: Large-diameter surfacing bit (spoilboard cutter or fly cutter), shallow passes (1–2mm), to establish a reference plane across the full slab.
 * Do not attempt to surface in a single deep pass — deflection and chatter increase with depth, and slab rocking under cut load is a real risk.
 * After first-face surfacing, flip and surface the second face parallel — this requires either a reference surface on the spoilboard or a thickness gauge to set the second-face pass depth.

**Tooling for wood CNC:**
 * *Upcut spiral:* Good chip evacuation, but pulls fibers upward — tearout on top surface of through-cuts.
 * *Downcut spiral:* Pushes fibers down — cleaner top surface, poorer chip evacuation, high heat buildup in deep slots.
 * *Compression spiral:* Upcut geometry at tip, downcut above — clean top and bottom surfaces, best for sheet goods and shallow-profile work.
 * *For live-edge preservation:* Climb-cutting the edge profile reduces tearout on irregular grain at the boundary — use with caution, requires a rigid hold-down.

**Probing irregular surfaces:**
Where CNC controller supports it, touch-probe the slab surface at a grid of points before running 3D toolpaths — this maps the actual surface topology and compensates for residual bow or twist not fully removed by surfacing. Manual shimming is the v0 alternative: shim the slab flat to the spoilboard before fixturing, verify with straightedge.

## 6. Heat Treatment and Surface Modification
 * **Steam bending:** Softens lignin for curves; requires a simple steam box and bending forms. Species matters — straight-grained green stock bends best; kiln-dried stock is brittle.
 * **Shou Sugi Ban (charred finish):** Torch char the surface to a consistent depth; wire brush to remove loose char; oil finish seals. Provides genuine weather and insect resistance. Depth of char controls durability vs. aesthetics.
 * **Oven stabilization:** Low-temperature oven treatment (90–120°C) drives residual moisture and can produce color change in some species. Not a substitute for proper drying — a wet core will still move after oven treatment.

## 7. Joinery and Assembly
**Traditional joinery** (mortise and tenon, dovetail, lap joint) requires no consumables and produces strong, repairable joints. Skill-dependent but tool-minimal.

**Modern joinery** (pocket screws, biscuits, domino loose tenons) is faster and more forgiving of minor dimensional variation — appropriate for utility work and jigs.

**CNC-cut joinery:** Finger joints, box joints, and custom mortise and tenon profiles are well-suited to CNC. Generates consistent, repeatable joints from variable stock.

**Adhesive selection:**
 * *PVA (wood glue):* Standard for indoor work, excellent strength, water cleanup.
 * *Epoxy:* Gap-filling, bonds dissimilar materials, waterproof — use for irregular fits, voids, and outdoor joinery.
 * *Polyurethane:* Expands slightly during cure (gap-filling), waterproof, bonds to slightly damp surfaces — useful for green or partially dried stock.

## 8. Finishing
**Surface preparation:**
 * Sand through grits — do not skip grits. Typical progression: 80 → 120 → 150 → 180 → 220.
 * Sand with the grain on final passes — cross-grain scratches telegraph through finish.
 * Raise the grain with a damp cloth after 150 grit on water-based finishes; sand lightly at 220 after drying to remove raised fibers.

**Finish selection:**
| Application | Recommended Finish | Notes |
|---|---|---|
| Indoor furniture | Tung oil, danish oil, hardwax oil | Penetrating — easy repair, low build |
| Indoor structural | Varnish, polyurethane | Film finish — durable, harder to repair |
| Outdoor | Marine varnish, teak oil + UV protectant | UV inhibitors critical under raw sunlight exposure |
| Highly porous/punky wood | Epoxy stabilization first, then topcoat | Consolidates weak fiber before finishing |
| Charred (Shou Sugi Ban) | Linseed or tung oil seal | Seals char; enhances weather resistance |

## 9. Waste Valorization
Wood waste follows a hierarchy consistent with Salvage Before Reduction doctrine:
 1. **Usable offcuts** — route to component storage; minimum useful size is application-dependent but a 12-inch square is a reasonable v0 threshold.
 2. **Chips and shavings** — animal bedding, garden mulch, compost amendment, smoking/BBQ fuel (species-appropriate).
 3. **Firewood** — larger offcuts and poor-quality material not suitable for fabrication.
 4. **Biochar** — controlled incomplete combustion produces biochar for soil amendment; cross-reference Operations/Energy.md for integration with biogas and thermal systems.
 5. **Mushroom substrate** — hardwood chips and sawdust support oyster and shiitake cultivation; low-cost, high-value output.
 6. **Paper pulp** — retting and beating cellulose fiber into sheet form; viable for low-volume applications from clean softwood fiber.

## 10. Dust and Species Hazard Doctrine
Wood dust is a respiratory hazard, a carcinogen at chronic exposure levels for certain species, and an explosion risk at sufficient airborne concentration. This is not optional PPE territory.

**Minimum PPE for all powered wood operations:**
 * *Dust mask:* N95 minimum for general operations; P100 half-face respirator for known sensitizers (walnut, cedar, exotic species).
 * *Eye protection:* Safety glasses minimum; face shield for lathe and routing.
 * *Hearing protection:* Foam plugs or earmuffs for all sustained power tool use.

**Source capture dust collection:**
 * Dust collector connected at the tool is more effective than ambient air filtration alone — capture at the source before dust becomes airborne.
 * *Minimum:* Shop vac with HEPA filter at hand tools and router; dedicated dust collector at tablesaw, planer, and jointer.
 * Cross-reference Operations/Air_Scrubber.md for system-level air management.

**Species-specific hazards:**
| Species Class | Hazard | Additional PPE |
|---|---|---|
| High-Tannin Walnut Typologies | Juglone sensitizer; respiratory | P100 respirator |
| Resinous Cedar Typologies | Respiratory irritant, sensitizer | P100 respirator |
| Toxic Alkaloid Typologies | Toxic (e.g., taxine alkaloids) | P100; avoid skin contact |
| Unknown salvage | Unknown profile | P100 until species confirmed |

**Dust explosion risk:**
Fine wood dust suspended in air is explosive. Do not allow dust to accumulate on surfaces — a sudden disturbance that raises accumulated dust into a cloud creates an immediate ignition risk. Empty dust collectors regularly. No open flames or ignition sources in dust-generating areas. Cross-reference WW-004 for mixed-species exposure threshold unknowns.

## Integration Hooks
 * `Operations/Air_Scrubber.md` — dust extraction system design, toxic species off-gas management, source capture integration.
 * `Operations/Gate_02_Triage.md` — salvage timber condition assessment follows triage logic; defect classification and routing to fabrication vs. firewood.
 * `Operations/Gate_03_Reduction.md` — low-value wood waste that cannot be repurposed follows Reduction doctrine to biochar or compost.
 * `Operations/Gate_06_Fabrication.md` — wood is a fabrication feedstock; fixturing, joinery, and finishing doctrine connects to fabrication workflow.
 * `Operations/Energy.md` — biochar and wood gas (gasification) are candidate energy inputs; firewood and offcuts feed thermal systems.
 * `Admin/Trajectories.md` — gasification of wood waste as an energy source, large-scale timber processing, and structural engineering calculations are v1+ scope items.
 * `Architecture/Facilities.md` — shop siting, floor loading for heavy log stock, clearance zones for power tool operation (FA-001).
 * `Admin/Safety_Protocols.md` — hearing conservation program; PPE sourcing standards for sustained power tool and chainsaw operations.

## Lessons Learned
| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| 2026-05-29 | Anecdotal | Immediate final milling of green stock | Severe warping and cracking after milling to dimension | Always rough dimension first, then dry to target MC, then final mill. Green stock milled to final dimension will move. | Anecdotal | Yes — validate drying schedule against local species per WW-001 |

## Active Disputes
| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### WW-001 — Ambient-relative humidity drying schedules not quantified

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Precise air-drying and kiln schedules for common local species under variable microclimate humidity conditions have not been validated. The one-year-per-inch rule of thumb is a generic analog estimate, not a locally measured figure.

**Why It Matters:** Improper drying leads to high material loss through checking, warping, and case-hardening. Underdried stock in joinery causes joint failure as the wood continues to move in service.

**Resolution Path:** Compile regional baseline forestry/extension data relative to the deployment node's climate envelope; cross-reference USDA Forest Products Laboratory drying schedules. Validate against first operational drying stack with moisture meter tracking.

---

### WW-002 — Long-term performance of salvaged urban timber uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Durability differences between urban salvaged timber and forest-grown timber are not characterized. Urban trees grow under different stress conditions — pollutant uptake, asymmetric wind stresses, soil compaction — that may affect structural performance and finishing behavior.

**Why It Matters:** Routing urban salvage to structural applications without understanding its performance profile introduces an uncharacterized failure mode in load-bearing assemblies.

**Resolution Path:** Survey available literature on urban timber structural performance. Flag salvaged urban timber as Analogous confidence for structural use until local destructive/non-destructive testing data exists.

---

### WW-003 — CNC fixturing best practices for live-edge slabs not validated

| Field | Value |
|---|---|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Technical |
| Blocking | No |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Section 5 provides fixturing guidance for irregular slabs but the methods have not been validated against actual live-edge slab operations. Vacuum hold performance on high-void slabs is particularly uncertain.

**Why It Matters:** Workpiece movement during CNC routing damages tooling, destroys the workpiece, and creates a projectile hazard at spindle speeds.

**Resolution Path:** Validate vacuum fixture hold-down force against representative slab geometries during first operational CNC cycle. Document actual minimum surface area requirements for reliable vacuum hold.

---

### WW-004 — Dust toxicity thresholds for mixed-species milling uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical / Safety |
| Blocking | Yes (for sustained mixed-species operations without P100 respirator) |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-30 |

**Description:** Precise exposure limits and synergistic effects when milling mixed local species simultaneously are not characterized. Sensitizer species mixed with inert species may produce combined exposures that exceed single-species thresholds at lower individual concentrations.

**Why It Matters:** Chronic wood dust exposure causes occupational asthma, nasal cancer, and sensitization reactions that can become debilitating. Mixed exposure profiles are harder to evaluate than single-species profiles.

**Resolution Path:** Until WW-004 is resolved, treat all mixed-species milling as requiring P100 half-face respirator minimum — do not rely on N95 alone. Cross-reference Operations/Air_Scrubber.md for source capture requirements.

---

### WW-005 — NDT standards for IFM detection not validated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical / Safety |
| Blocking | Yes (for processing raw urban salvage through powered machinery) |
| Owner | Operations/Woodworking.md |
| First Logged | 2026-05-30 |
| Last Reviewed | 2026-05-30 |

**Description:** The precise workflow and hardware sensitivity requirements for detecting deeply embedded ferrous and non-ferrous objects within dense hardwood logs have not been calibrated for the v0 shop environment.

**Why It Matters:** Undetected metal striking high-speed cutting machinery creates an immediate operator shrapnel hazard and can cause catastrophic failure of bootstrap tooling that cannot be easily fabricated or replaced.

**Resolution Path:** Source or fabricate a reliable deep-penetration wand metal detector. Establish a clear Scan-and-Mark workflow for all incoming urban salvage logs. Validate detection depth limits using a known control sample (e.g., a 16d nail driven into a test block at varying depths). Payment via Specification once detection workflow is validated and minimum detection depth is characterized.

---

### Resolution Log

- 2026-06-08: Navigation Anchors block added. Safety Advisory
  formatting corrected — horizontal rule added after advisory,
  stray `>` removed. Verification Ref corrected from
  `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates.md`
  (PC-001). Scope Boundary updated — `Architecture/Facilities.md`
  added for shop siting and clearance zones (PC-002);
  `Admin/Safety_Protocols.md` added for hearing conservation
  program and PPE sourcing standards (PC-003). Integration Hooks
  updated to canonical backtick paths; Facilities.md and
  Safety_Protocols.md added.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet | —    |

---

## Drift Indicators
Mandatory re-audit conditions for this document:

| Trigger | Reason |
|---|---|
| WW-004 remains unresolved and N95 masks used for mixed-species milling | Blocking unknown — P100 is the minimum until characterization is complete |
| WW-005 remains unresolved and urban salvage processed through powered machinery without electromagnetic screening | Blocking unknown — IFM screening is mandatory before any powered cut on salvage stock |
| Felling operations conducted without a second person present | Permanently required — never fell alone is non-negotiable doctrine |
| Green stock milled to final dimension without drying to target MC | Permanently abandoned path — always rough dimension, dry, then final mill |
| CNC operations begun without fixturing hold-down verified by hand | Workpiece movement at spindle speed is a projectile hazard — verify before running |
| Urban salvage timber used in structural applications before WW-002 is resolved | Uncharacterized structural performance — flag as Analogous confidence at minimum |
| Dust collector bypassed or disconnected at any power tool station | Source capture dust collection is non-negotiable — not an optional convenience |
| Geographic proper nouns or localized tracking vectors injected | Violates biome-agnostic system intent and breaches operational opacity guardrails |
| Structural design cuts elements directly across natural curved fibers | Short-grain structural vulnerability — forces curved components into failure |
| Ethical Anchor field absent, altered, or does not match canonical string | Load-bearing integrity requirement — applies to all files |

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.
