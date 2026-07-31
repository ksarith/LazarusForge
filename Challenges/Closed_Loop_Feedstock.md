# Challenges/Closed_Loop_Feedstock.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field              | Value |
|--------------------|-------|
| Status             | Exploration |
| Challenges Subtype | Solution-Track |
| Version            | v0.8.1 |
| Body Stability     | Transitional |
| Spec Gates         | 0/6 |
| Verification Ref   | `Admin/Verification_Gates_LF.md` |
| Ethical Anchor     | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Highest Risk       | Silent contamination cascades or toolhead destruction (CLF-003/CLF-006). |
| Last Audit         | 2026-07-31 (§8 CLF-003 detail added — no hardware exists yet on either polymer or metal extrusion path; provisional wear thresholds borrowed from §7.1) |
| Auditor            | Claude — Skeptic/Auditor (integration, 2026-07-07); prior: Grok, Gemini, Claude (2026-07-06); Claude — ratification pass (human-directed), 2026-07-17; Grok — drafted §7 contamination doctrine / MCM schema / validation logic (Skeptic/Auditor), Claude — Synthesizer (verified against source, integrated as §7, cross-consistency check vs Gate_04/05/Ethical_Constraints, adversarial stress-test additions), 2026-07-30; Claude — Synthesizer, expanded CLF-003 from single-line entry to full detail (§8), verified against Plastics.md and Gate_05 SC-004 source, human-directed, 2026-07-31 |
| Open Unknowns      | 10 (CLF-001 through CLF-010) — unchanged; CLF-006/CLF-009 remain Open pending §7 ratification; CLF-003 detailed but still Open pending hardware |
| Active Disputes    | 0 |
| Sidecar Link       | #6-open-unknowns |

---

> *"The Forge optimizes for the closure of loops, not the purity of outputs. A crude loop that stays closed is infinitely superior to a pristine process that relies on a ghost supply chain."*

## 1. The Crisis: The Illusion of Material Autonomy

Every advanced fabrication node in the legacy industrial paradigm relies on a hyper-optimized, low-entropy upstream supply chain. If the Forge requires pristine, pre-refined inputs, its **Supply Chain Dependency ($\Delta_{sc}$)** remains fatally high. True v0 persistence demands closing the material loop locally — transforming unpredictable salvage into trustable fabrication inputs while minimizing internal resource consumption and external dependency.

> ✅ **CLF-005 — symbol collision resolved 2026-07-07.** Previously this file used $\Phi_{\text{ext}}$, the same symbol `Challenges/Return_To_Eden.md`'s Eden Index ($I_E$) reserves for its own External Energy/Resource subsidy term. Direct comparison against Return_To_Eden.md's Section 3 formulation confirms these are different metrics: Return_To_Eden.md's $\Phi_{ext}$ is a normalized ratio ($\Phi_{ext}/\Phi_{ext,0}$) against a system-entry baseline, one of five terms in a site-wide ecosystem index. This file's usage was an unnormalized, process-level supply-dependency concept with no baseline reference — a different scope wearing the same symbol. Renamed here to **Supply Chain Dependency ($\Delta_{sc}$)** to remove the collision. No change to Return_To_Eden.md required — that file's $\Phi_{ext}$ was correctly scoped for its own purpose and RE-UNK-001/RE-UNK-005 remain that file's open items, unaffected by this rename.

## 2. Scope Boundary

**This file owns:**
- Definition and tracking of the Persistence Yield ($Y_p$) telemetry model.
- Cross-gate coordination heuristics for salvage-to-feedstock conversion.
- Overarching engineering pressures and recursive improvement doctrine.

**This file does not own:**
- Specific mechanical sorting (defers to `Operations/Gate_04_Separation_Mechanical.md` and `Operations/Gate_05_Separation_Thermal.md`).
- Detailed thermal/chemical parameters (defers to `Architecture/Thermal_Systems.md` and `Architecture/Chemistry.md`).
- Toolpath or fabrication adjustments (defers to `Operations/Gate_06_Fabrication.md`).
- Toxic/hazardous material handling doctrine, including electrolyte acids and chemical reclamation (defers to `Admin/Ethical_Constraints.md` §Toxic and Hazardous Material Handling, and to `Operations/Gate_03_Reduction.md` GR-003).

### 2a. Embedded Value Preservation — ratified 2026-07-17 (human governing authority)

**Principle:** *Preserve embedded value whenever practical. Reduction is not the default. A component that already embodies significant manufacturing effort — precision bearings, laminated motor cores, magnet wire, shafts, threaded fasteners — should be recovered and reused intact unless disassembly or degradation makes reduction the higher-value path. The Forge should prefer recovering existing manufacturing work over reducing it back to raw material by default.*

This extends the same repair-first logic `Admin/Ship_of_Theseus.md` already establishes for whole units, applied one layer earlier — to the components inside a unit that isn't itself repairable. It sits upstream of `Operations/Gate_02_Triage.md`'s existing station logic (which already distinguishes reuse from destruction at the whole-component level) rather than replacing it — see that file's Core Principles for the corresponding cross-reference. Now adopted into this file's operative Scope Boundary.

## 3. System Dependencies

**Upstream**
- `Architecture/Forge_flow.md`
- `Operations/Gate_03_Reduction.md`
- `Architecture/Chemistry.md`
- `Architecture/Characterization.md` — **[PLANNED]**, not yet created

**Downstream**
- `Operations/Gate_06_Fabrication.md`
- `Operations/Plastics.md`
- `Operations/Metals.md` — **[PLANNED]**, not yet created
- *Degraded/bleed-off material destination — currently undefined, see CLF-008. Candidate link: `Challenges/Return_To_Eden.md`'s $W_{\text{out}}$ (waste output) variable for toxic slag/anode-slime accumulation, and `Operations/Gate_03_Reduction.md` for material diverted to full reduction — neither link is confirmed or formalized yet.*

## 4. Telemetry: The Persistence Yield ($Y_p$)

$$Y_p = FIR \times PIR$$
*(Internally Derived / Conceptual)*

**FIR** = salvaged mass fraction: $FIR = \frac{M_{\text{salvaged}}}{M_{\text{total}}}$

*Boundary conditions for what counts toward $M_{\text{salvaged}}$ vs. $M_{\text{total}}$ (donated virgin resin, reclaimed-but-unprocessed copper wire, reused fasteners, scavenged commercial filament) are not yet defined — see CLF-010. Until resolved, different auditors may compute FIR inconsistently for the same physical stream.*

**PIR** = a multi-vector independence score, not a single measurement. The energetic ceiling added in a prior pass ($E_{\text{yield}} > E_{\text{proc}}$, including auxiliary loads for pumps, conveyance, assay, and thermal control per `Operations/Energy.md`) is a real and necessary constraint, but it is only the energy vector — narrowing PIR to that alone breaks the file's own worked example below, which turns on *chemical*, not energy, dependency:

- **PIR_energy** — ratio of locally harvested/regenerated energy to total process energy, bounded by $E_{\text{yield}} > E_{\text{proc}}$
- **PIR_chemical** — mass of internally recycled or zero-external-flux reagents vs. total chemical inputs
- **PIR_maintenance** — tool-wear lifespan measured in internal replication capability (can the tool fix its own wear?)
- **PIR_labor** — human-intervention minutes required per kilogram of output

> ⚠️ **CLF-007 — aggregation function undefined.** The worked example below collapses these four sub-vectors into a single "overall PIR" without stating the operator. An arithmetic mean is explicitly wrong for this file's own stated intent — a high energy score could mask a near-zero chemical score, exactly the failure mode the multi-vector breakdown exists to catch. A geometric mean or weighted product (with weights reflecting each vector's existential risk, summing to 1) would collapse toward zero if any single vector does; the arithmetic mean would not. No aggregation method is committed yet — this file's Y_p examples below should be read as illustrative, not as a specified computation.

**Worked example (illustrative — see CLF-007):** A 95%-pure rough melt-sort with FIR = 0.90 and overall PIR = 0.95 yields Y_p = 0.855. High-purity electrorefining has FIR = 1.00 and a *favorable* PIR_energy (low ambient-temperature process) — but a poor PIR_chemical (weekly acid replacement), dragging overall PIR down to roughly 0.30 and Y_p to roughly 0.30 despite the energy advantage. The Forge explicitly chooses the higher Y_p, not the higher-purity output, and not the better single vector.

## 5. The First Recursive Loop: Epistemic Ascent

Measurement → Processing → Fabrication → Upgrade.

1. Characterize unknown salvage with available low-tier methods.
2. Produce "good-enough" feedstock.
3. Fabricate improved sensors, rigs, and tooling using Generation-N output.
4. Tighten characterization for Generation-N+1.

This loop directly advances FIR while respecting energy and uncertainty constraints.

> ⚠️ **CLF-009 — data handoff interface contract undefined.** This loop assumes characterization output is legible to downstream fabrication tools (`Operations/Gate_06_Fabrication.md`), but no form factor for that handoff is defined — no equivalent of a "Material Certainty Manifest" specifying how a Bayesian certainty profile gets encoded and read. Without it, "epistemic ascent" is a philosophical goal rather than a software design pressure with an actual interface. **Proposed solution drafted 2026-07-30 — see §7.2; Status: Proposed, not ratified.**

**Degraded Operation & Failure Modes**

Recursive loops risk cascading contamination (heavy metals in polymers, alloy drift) and progressive tool wear. When purge thresholds or wear limits are exceeded:
- Divert degraded feedstock to low-spec structural applications or full reduction (`Operations/Gate_02_Triage.md`/`Operations/Gate_03_Reduction.md`).
- Maintain explicit bleed-off / slag handling protocols. *Where this material physically ends up past that point is not yet linked — see CLF-008 and the Section 3 note above.*
- Ensure maintenance access for dies/nozzles and end-of-life criteria for processing hardware.

## 6. Open Unknowns

| ID | Title | Owning File | Status | Subtype | Priority (Promo) |
|----|-------|-------------|--------|---------|------------------|
| CLF-001 | Blending ratios and thermal stabilizer performance for mixed, un-refined polymer streams across multiple thermal cycles. | Challenges/Closed_Loop_Feedstock.md | Open | — | Major |
| CLF-002 | Minimal viable field assay protocols (spot tests, melt-flow, etc.) for copper/aluminum alloys from salvage. | Challenges/Closed_Loop_Feedstock.md | Open | — | Major |
| CLF-003 | Nozzle and die wear tolerances when processing high-variance, particulate-laden salvage feedstocks. **Detailed 2026-07-31** — no dedicated extrusion hardware exists yet on either the polymer side (`Operations/Plastics.md` routes filament-drawing rigs to `Admin/Trajectories.md` as future blueprints) or the metal side (`Operations/Gate_05_Separation_Thermal.md` SC-004, wire extrusion nozzle design, also unspecified). Provisional acceptance-criteria numbers borrowed from the unratified §7.1 CLF-006 doctrine (nozzle diameter growth >8%, die pressure rise >25%, particulate >2%) — see §8 for full detail. Still Critical/Open; cannot reach Resolved without physical instrumented test cycles on hardware that does not yet exist. | Challenges/Closed_Loop_Feedstock.md | Open | — | Critical |
| CLF-004 | Chemical footprint of electrolytic/electrorefining pathways undefined — local/organic acid sourcing vs. closed-loop acid reclamation not decided. Intersects `Admin/Ethical_Constraints.md` §Toxic and Hazardous Material Handling, `Operations/Gate_03_Reduction.md` GR-003, PL-001/CE-003, and `Challenges/Critical_Minerals.md` CM-002 (closed-loop reagent recovery — same underlying problem, different material stream). **Candidate pathway logged 2026-07-07 (human-directed):** on-site acid synthesis via salt-water electrolysis with an ion-selective membrane (chlor-alkali-type process) — a third option alongside "external sourcing" and "closed-loop reclamation," not a replacement for them; the sourcing decision among the three remains open. Uses cheap/abundant, non-toxic precursors (salt, water, electricity). Not a resolution: standard chlor-alkali electrolysis co-produces chlorine gas, which requires a containment/scrubbing design to satisfy Ethical_Constraints.md's active-release-prohibited doctrine before this pathway can be adopted. **Directed approach added 2026-07-17 (human-directed) at `Architecture/Chemistry.md` CE-006:** capture and nullification via existing `Operations/Air_Scrubber.md` chemisorption infrastructure, subject to verification at this process's actual generation rate — see CE-006 for detail. **Mechanism corrected 2026-07-19:** the chemisorption infrastructure referenced above (Stage E) does not target Cl₂; redirected to Stage D wet caustic scrubbing, and reframed as value-recovery (sodium hypochlorite byproduct) rather than pure nullification — see CE-006/CE-007 for full detail. Still Critical/Open pending verification and formal ratification of the sourcing decision among the three candidate paths. | Challenges/Closed_Loop_Feedstock.md | Open | — | Critical |
| CLF-006 | Recursive cascading contamination thresholds, bleed-off, and purge metrics undefined — what triggers diversion to low-spec/full reduction, and what the quantitative purge/wear limits actually are. | Challenges/Closed_Loop_Feedstock.md | Open | — | Critical |
| CLF-007 | PIR aggregation function undefined — the four sub-vectors (energy, chemical, maintenance, labor) are collapsed into "overall PIR" with no stated operator. An arithmetic mean would let one strong vector mask a near-zero vector, contradicting this file's own stated intent. Needs a geometric mean or weighted product, with weights reflecting each vector's existential risk. | Challenges/Closed_Loop_Feedstock.md | Open | — | Major |
| CLF-008 | Downstream destination for degraded/bleed-off material and hazardous byproducts (toxic slag, anode slime) undefined. Section 3's dependency table has no link for where this material physically flows. Candidate links: `Operations/Gate_03_Reduction.md` (full-reduction diversion) and `Challenges/Return_To_Eden.md` $W_{\text{out}}$ (waste-output accumulation) — neither confirmed. | Challenges/Closed_Loop_Feedstock.md | Open | — | Major |
| CLF-009 | Interface contract for characterization→fabrication data handoff undefined — no form factor (e.g. a "Material Certainty Manifest") specifies how a Bayesian certainty profile is structurally encoded so `Operations/Gate_06_Fabrication.md` can read and adapt toolpaths to it. | Challenges/Closed_Loop_Feedstock.md | Open | — | Minor |
| CLF-010 | FIR boundary conditions undefined — how donated virgin resin, reclaimed-but-unprocessed copper wire, reused fasteners, and scavenged commercial filament count toward $M_{\text{salvaged}}$ vs. $M_{\text{total}}$ is not specified, risking inconsistent FIR calculation across auditors/sessions. | Challenges/Closed_Loop_Feedstock.md | Open | — | Major |

*CLF-003 and CLF-006 are Critical — CLF-003 blocks sustained polymer extrusion operations; CLF-006 blocks safe recursive-loop operation without defined contamination thresholds.*
*CLF-004 is Critical — no electrolytic/electrorefining pathway may proceed without a chemical footprint decision, and a candidate pathway now exists pending a chlorine containment answer.*
*CLF-005 — Resolved 2026-07-07 (see §1). Retained in this table as a closed record rather than removed, consistent with this file's own audit trail practice.*
*CLF-006 and CLF-009 — Proposed solutions drafted 2026-07-30 (contamination doctrine, Material Certainty Manifest schema, and validation/hardening logic), including a compound sub-threshold trigger and an assay-gated confidence ceiling surfaced by adversarial stress-testing. Full text in §7 below. Status remains Open/Proposed — not yet ratified by human governing authority. §7 does not itself resolve CLF-003 or CLF-004; CLF-004 remains fully untouched, and CLF-003 is treated separately below.*
*CLF-003 — expanded 2026-07-31 from a single-line entry to full detail (§8). No extrusion hardware exists yet on either the polymer (`Operations/Plastics.md`) or metal (`Operations/Gate_05_Separation_Thermal.md` SC-004) path; provisional wear-tolerance numbers borrowed from §7.1 by citation. Still Critical/Open — documentation progress only, not a resolution.*

**ID collision history:** originally registered as `CF-001` through `CF-003` (collided with `Architecture/Cognitive_Frameworks.md`/`Operations/Electronics.md`), corrected to `CLF-001`–`CLF-003`. An intervening hygiene pass renamed these to `FL-001`–`FL-004`, reintroducing a collision with `Architecture/Forge_flow.md`'s FL-001 (Blocking) — reverted back to `CLF-`. Do not rename off this prefix without checking `Unknowns.md`'s full active index first.

**Registration status:** registered in `Routing.md`, `Discovery.md`, `Unknowns.md`, and `Automation/AUDIT_HARNESS.py` FILE_REGISTRY — confirmed 2026-07-19 (see `Unknowns.md` PC-005, resolved that date). This note previously claimed registration was outstanding; that was stale as of at least 2026-07-12 (registration had already happened 2026-07-06) and sat unconfirmed for a week before this correction. *(Note: `AUDIT_HARNESS.py` v13's FALLBACK_REGISTRY/UNKNOWN_FIRST_CYCLE mechanism referenced below is separate and was retired in v15 — see that file's own comments; not relevant to this file's core registration status.)*

Full sidecar details maintained here; register cross-references in `Unknowns.md` on next audit.

---

## 7. Proposed Solutions — Pending Ratification (CLF-006, CLF-009)

**Status: Proposed.** The three sub-sections below (7.1–7.3) are a complete, internally cross-referenced draft package addressing CLF-006 (contamination doctrine) and CLF-009 (Material Certainty Manifest + data handoff), including a compound-metric aggregation rule and an assay-gated confidence ceiling added after adversarial stress-testing (Auditor_Protocols.md Challenge Classes 2, 3, and 5). **None of this is ratified.** CLF-006 and CLF-009 remain Open in §6 above until human governing authority reviews and formally adopts this package. It is written to be adopted as **one atomic unit** — several values in 7.2's examples (e.g. the 0.15% carbon-pickup limit) only exist because 7.1 proposes them, and 7.3 governs how every number in 7.1/7.2 gets revised. This proposal does not address CLF-003 or CLF-004, which remain separately Open and Critical.

### 7.1 CLF-006 Contamination Doctrine (Proposed)

**Priority:** Critical · **Downstream action points on ratification:** Gate_04 (Unknown Bulk / Class C), Gate_05 (slag / ranked streams / wire path), Gate_02 (Triage), Gate_03 (full reduction), Gate_06 (fabrication), Plastics.md (polymer path)

**Governing Principle:** A closed loop that stays closed under progressive contamination is superior to a higher-purity process that eventually fails open. Contamination is treated as an expected, measurable state variable — not an anomaly. Diversion is a success condition when it preserves tooling life, alloy utility, and operator safety. Reduction is never the default; it is the last controlled exit from the recursive loop. This implements Embedded Value Preservation (§2a) one layer earlier than Gate_02.

**Definitions (provisional):**

| Term | Definition |
|------|------------|
| **Contamination Load (\(C\))** | Mass fraction of non-target species (heavy metals in polymer, alloy tramp elements, particulate > specified size, halogenated residue, carbon pickup beyond baseline) relative to total stream mass. |
| **Bleed-off Fraction (\(B\))** | Mass intentionally diverted from the primary recursive path in a given cycle. |
| **Contamination Diversion** | The purge/bleed-off action defined here — material routed away from the recursive path due to a fired contamination trigger. **Distinct from Gate_04's "Material Diversion Rate"** (`Operations/Gate_04_Separation_Mechanical.md`, Falsifiable Performance Metric), which measures successful recovery of intact value to Class A/B reuse and treats high diversion as a *success* signal. This doctrine's Unknown Bulk escalation trigger (25%) sits numerically inside Gate_04's healthy 10–30% band without being the same measurement — do not conflate a healthy Gate_04 diversion rate with an active CLF-006 contamination cascade. *On ratification, add this note to Gate_04's Falsifiable Performance Metric section as well.* |
| **Purge Event** | Controlled diversion of a defined mass fraction when a trigger below is met. |
| **Low-Spec Structural** | Non-critical use (brackets, ballast, sacrificial wear parts, non-load-bearing frames) where alloy drift or particulate is tolerable. |
| **Full Reduction** | Return to Gate_03 for irreversible sizing / re-entry into the lowest-value recovery path. |
| **Wear Proxy** | Observable proxy for tooling degradation (nozzle diameter growth, die pressure rise, vibration signature change, motor current drift under constant load). |

**Quantitative Triggers (v0 Provisional — design-intent starting points, falsifiable, revised per §7.3):**

*Polymer / Extrusion Path (CLF-003 interface):*

| Trigger | Threshold | Action | Destination |
|---------|-----------|--------|-------------|
| Particulate mass fraction > 2% | Immediate | Divert batch | Low-Spec or full reduction |
| Nozzle diameter growth > 8% from new | After current run | Purge + replace/ream | Bleed-off to Low-Spec; tooling to maintenance |
| Die pressure rise > 25% at constant throughput | After current run | Purge + inspect | Same |
| Black specking / gel count rising 3 consecutive batches | Progressive | Increase \(B\) by 10% each cycle until clear | Low-Spec or Gate_03 |
| Halogen positive (Beilstein or equivalent) | Any detection | Full diversion | Specialist disposal / Gate_03 — never pyrolysis or extrusion. Cites `Admin/Ethical_Constraints.md`; note EC-014 (concrete encapsulation/failure-mode standard) is itself still Open — direction is sound, target standard is not yet fully specified. |

*Metallic Path (Gate_04 → Gate_05):*

| Trigger | Threshold | Action | Destination |
|---------|-----------|--------|-------------|
| Gate_04 confidence < 90% (MG-003) | Per fragment/parcel | Route to Unknown Bulk | Gate_02 Triage |
| Unknown Bulk accumulation > 25% of intake/shift | System | Tighten confidence threshold or reduce RPM; escalate review | — |
| Gate_05 slag/oxide layer mass > 8% of melt | Per batch | Skim + divert | Low-Spec or Gate_03 |
| Carbon pickup (SC-008) > 0.15% C above charge composition | Per batch | Divert inner fraction or entire melt | Low-Spec or full reduction |
| Vibration signature drift > baseline for 10 min (existing Gate_05 rule) | Continuous | Reduce RPM; abort + divert if persistent | Remaining melt to Low-Spec/Gate_03 |
| Alloy tramp elements > application-specific limit | Per batch | Divert affected radial fraction | Low-Spec |

*Cross-Path / Recursive Cascade:*

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Same contaminant species, 3 successive generations | Cascade declared | Mandatory 15–25% bleed-off + root-cause isolation |
| Tooling end-of-life (CLF-003) | Per tool | Immediate diversion of feedstock contacting failed tool |
| Toxic/hazardous species not covered above | Any detection | Immediate stop + full diversion per Ethical_Constraints.md and Gate_03 GR-003 |

*Compound Sub-Threshold Trigger (added after adversarial stress-test, Challenge Class 2/5):* Individual triggers above evaluate independently, so a batch sitting just under several thresholds at once passes every check despite elevated aggregate risk. **Trigger:** two or more of {\(C\)-estimate, confidence (inverse), slag/oxide fraction, particulate fraction, carbon-pickup estimate} sitting within 15% of their respective trigger values simultaneously. **Action:** treat as if the more severe of the near-miss metrics had fired outright. Provisional; revise once real or constructed compound cases exist.

**Bleed-off Mechanics:** Minimum intentional bleed-off 5% of processed mass per cycle while CLF-003/CLF-004/CLF-006 remain Open (safety floor, not efficiency target). Maximum continuous bleed-off 30% of intake over any rolling 5-batch window — exceeding forces formal Triage/Reduction review. Purge sequence preference: Low-Spec Structural → Gate_03 full reduction → specialist hazardous handling. Slag, anode slime, and polymer char are never treated as inert.

**Degraded Operation Rules:** When any trigger is active, continue at reduced throughput rather than pass contaminated material downstream. Hot-idle/long-hold doctrines (Gate_05) remain in force. Sensor fouling, jams, or vibration events (MG-007/008, SC-001/005) automatically tighten relevant thresholds until cause is cleared.

**Explicit Non-Goals:** Achieving zero contamination; replacing Gate_04 refusal-first or Gate_05 progressive-enrichment philosophy; defining exact chemical assay methods (defers to `Architecture/Characterization.md` [PLANNED] and `Architecture/Chemistry.md`); final disposition of hazardous byproducts beyond diversion rules (CLF-008 remains open).

**Integration Hooks (on ratification):** Replace this file's §5 Degraded Operation & Failure Modes prose with this doctrine · Gate_04 Fail-to-Bin/Unknown Bulk sections reference cascade/accumulation triggers + terminology note above · Gate_05 Extraction/Failure Philosophy references slag mass and carbon-pickup triggers · CLF-003 wear proxies become measurable acceptance criteria · CLF-008 gets Low-Spec/Gate_03 as interim destinations · CLF-009 gets the Material Certainty Manifest as its first concrete form factor (§7.2).

### 7.2 CLF-009 Material Certainty Manifest — Schema & Examples (Proposed)

**Why it matters:** `Architecture/Characterization.md` remains `[PLANNED]`. Gate_06 already assumes variable-quality feedstock and owns the precision ceiling (add-to-excess, mill-to-spec) but has no structured way to receive a certainty profile. Without a defined handoff, characterization data dies at the gate boundary and "epistemic ascent" (§5) stays philosophical rather than operational. Design rule: **never collapse uncertainty into a single grade code** — the Manifest exists so fabrication sees a distribution, not a false certainty.

**v0 Schema (binding on ratification):** Physical tag or attached sheet on the batch container, optional plain-text/JSON digital twin; physical tag is authoritative.

```
MCM-v0
batch_id:          <string>          # required
source_gate:       Gate_04 | Gate_05 | Gate_03 | mixed | other
nominal_class:     <string>
mass_kg:           <float>
generation:        <int>
C_estimate:        <float|unmeasured>
confidence:        <0.0–1.0|low|med|high>
assay_method:      <list or none>    # gates the confidence ceiling — see below
segregation_note:  <free text>
wear_flags:        [<flag>, ...]
intended_destination: Gate_06-weld | Gate_06-mill | Low-Spec | Gate_03 | Triage | Specialist
carbon_pickup_est: <float%|unmeasured|n/a>
halogen_status:    negative | positive | untested
weldability_proxy: acceptable | high-spatter | unknown | n/a
recommended_excess_mm: <float|default>
certainty_profile:                   # required block
  primary:         <element/alloy>
  secondary:       [<species range or unmeasured>, ...]
  confidence:      <0.0–1.0>
  method:          <how derived>
  notes:           <free text>
timestamp:         <ISO or local>
operator:          <id or name>
prior_manifests:   [<batch_id>, ...] # optional, for blends
```

**Validity rule:** A Manifest is valid with at least `batch_id`, `source_gate`, `nominal_class`, `mass_kg`, `C_estimate`, `confidence`, `assay_method`, `intended_destination`, and `certainty_profile`. Missing optional fields default to "unmeasured"/empty/n/a.

**Assay-gated confidence ceiling (added after adversarial stress-test, Challenge Class 3):** without this, an operator under time pressure could write a high `confidence` value with no instrumented backing behind it.

| `assay_method` | Maximum claimable `confidence` |
|---|---|
| none / unstated | 0.30 |
| visual only | 0.65 |
| density or melt-flow only | 0.75 |
| visual + one instrumented method | 0.85 |
| two or more instrumented methods | 0.95 |
| cross-checked against Gate_04 confidence (prior manifest) | inherits the more conservative of the two |

A Manifest claiming `confidence` above its `assay_method` ceiling is INVALID (§7.3) and is force-corrected to the ceiling before any Gate_06 rule applies.

**Gate_06 Consumption Rules (v0):**

| Manifest signal | Gate_06 action |
|-----------------|----------------|
| confidence ≥ 0.80 and \(C\) ≤ 0.05 and no flags | Standard weld parameters; default excess |
| confidence 0.60–0.79 or \(C\) 0.05–0.10 | +50% excess (min +1mm); reduce heat input; enhanced fume capture |
| confidence < 0.60 or \(C\) > 0.10 or cascade/wear flags | Refuse load-bearing/precision; Low-Spec or sacrificial only, or reject to Gate_03 |
| halogen_status: positive | Immediate refuse; never weld or extrude |
| weldability_proxy: high-spatter/unknown | Trial coupon required before production parts |
| generation ≥ 3 and elevated secondary species | Next-stricter tramp limit; prefer diversion |
| Missing required fields | Treat as confidence: low, C: unmeasured → refuse critical use |
| confidence exceeds assay_method ceiling | Force-correct before applying any other rule |

**Physical tag minimum:** `ID / Src / Gen / Mass / Class / C≈ / Conf (assay method) / Dest / Flags / Primary (+secondary) / Operator / timestamp` — enough for pure analog operation while still supporting the confidence-ceiling check.

**Relationship to other unknowns:** feeds CLF-006 (\(C\), wear flags, cascade, diversion decision), CLF-003 (wear proxies travel with the batch that caused them), CLF-008 (destination field makes bleed-off routing explicit), CLF-010 (generation/source fields clarify FIR counting), SC-002/SC-007 (segregation note), SC-008 (carbon-pickup field), Gate_06 ASM-001/ASM-005 (weldability proxy and confidence feed wire and base-metal decisions), and becomes `Characterization.md`'s first concrete output schema once that file exists.

**Open design questions (for human/multi-agent decision on ratification):** minimum required fields for validity vs. "unmeasured" as a valid state; authority to write/amend a Manifest; blending rule when two Manifests combine (worst-case? mass-weighted? explicit Bayesian update?); hard confidence floor vs. advisory guidance at Gate_06; retention period for tags/digital twins across generations.

### 7.3 Validation Logic — MCM + CLF-006 (Proposed)

**Manifest Validity Check (entry gate):**

| Check | Pass Condition | Fail Action |
|-------|----------------|-------------|
| Required fields present | All required fields (§7.2) present | Reject or force high-risk defaults |
| confidence range | 0.0–1.0 or {low, med, high} | Force confidence = low |
| confidence vs. assay_method ceiling | ≤ ceiling for stated assay_method | Force down to ceiling; log Medium-severity discrepancy |
| C_estimate | ≥ 0 or "unmeasured" | Force "unmeasured" |
| halogen_status | {negative, positive, untested} | Force "untested" |
| Internal consistency | wear/cascade flags present → destination not critical unless human-overridden | Auto-redirect to Low-Spec/Triage |
| Generation + cascade | generation ≥ 3 + elevated species → destination not critical without sign-off | Hold for Triage |
| Compound sub-threshold (§7.1) | Two or more metrics within 15% of trigger simultaneously | Treat as the more severe metric fired outright |

Result codes: `VALID` (normal rules) · `VALID-DEGRADED` (tightened rules) · `INVALID` (refuse/re-characterize/divert).

**Material Acceptance Logic (Gate_06, severity-ordered, higher overrides lower):**

| Condition | Severity | Action |
|-----------|----------|--------|
| halogen_status = positive | Critical | Immediate refuse; route per Ethical_Constraints |
| Cascade flag, or generation ≥ 3 with elevated tramp, or compound trigger fired | High | Refuse load-bearing/precision; Low-Spec/sacrificial only; human review for other use |
| C > 0.10, or confidence < 0.60, or active wear flags | High | Refuse critical use; increase excess if used; trial coupon mandatory |
| confidence 0.60–0.79, or C 0.05–0.10, or weldability high-spatter/unknown | Medium | +50% excess (min +1mm); reduce heat input; trial coupon; log as degraded |
| confidence ≥ 0.80, C ≤ 0.05, no flags, weldability acceptable | Low/Normal | Standard parameters, default excess |
| Missing/unmeasured critical fields | Treat as High | Apply High-severity rules |

Trial-coupon rule: any Medium/High path still allowed must produce an inspected test coupon before the rest of the batch commits; coupon failure diverts the remainder immediately. Precision-ceiling interaction: if Gate_06/Precision.md's current ceiling cannot absorb the Manifest's uncertainty, refuse for that part regardless of the table above.

**CLF-006 Threshold Hardening (asymmetric, safety-conservative):** Validation cycle = ≥3 instrumented batches deliberately exercising the relevant trigger (or honest natural occurrence), recording actual \(C\)/wear/slag/vibration, downstream outcome, and whether the provisional threshold correctly diverted or incorrectly allowed the batch. Compute false-negative rate (contaminated material that passed and caused harm) and false-positive rate (clean material unnecessarily diverted). **Decision rule:** any false negative on a safety-critical outcome → tighten immediately. High false-positive rate with zero safety false-negatives → may loosen, but only with human governing authority ratification and an Epistemic Ledger entry. No threshold changes solely to improve \(Y_p\) or throughput while any Critical unknown remains Open. The safety-critical/non-critical severity boundary itself is provisional — a false negative on a batch classified non-critical that later causes unexpected harm is evidence the *classification*, not just the threshold, needs revision; log both.

**Feedback into Epistemic Ascent (§5):** part meets spec → raise confidence for that material class/generation; part fails → lower confidence, flag sibling batches from the same parent, trigger root-cause review; wear proxy observed → append flag, feed CLF-003; cascade detected → mark related generation-N manifests, force bleed-off next cycle.

**Authority:** automated systems apply the tables above only, never loosen a threshold or override a High/Critical refuse. Human operator may temporarily override a Medium path with logged justification. Human governing authority required to change any numeric threshold, accept a High-severity batch for critical use, or retire a provisional rule.

**Logging (minimum for validation):** every decision point records MCM snapshot/batch_id, decision code + severity, action taken, later outcome when known — the evidence base for promoting any provisional number to Measured under the repository's Verification Algebra.

**Stress-test provenance (for context):** a cross-consistency check against existing repo thresholds (Gate_04's 30%/10% diversion-rate metric, Gate_05's 10-minute vibration rule, `Ethical_Constraints.md` EC-014) found no numeric contradictions, one terminology collision (addressed via the Contamination Diversion definition in §7.1), and one soft dependency gap (CLF-006's halogen routing cites Ethical_Constraints' toxic-handling doctrine, which itself has EC-014 open — noted, not blocking). Two adversarial scenarios (Auditor_Protocols.md Challenge Class 2/5 stacked sub-threshold contamination; Class 3 asserted-vs-measured confidence) directly produced the compound sub-threshold trigger (§7.1) and the assay-gated confidence ceiling (§7.2) above.

---

## 8. CLF-003 — Nozzle and Die Wear Tolerances (Detail)

**Status: Open, Critical.** Previously a single line in §6 with no supporting detail — expanded 2026-07-31 to bring it to the same standard as other Critical unknowns in this repository. This is a documentation-honesty pass, not a resolution; CLF-003 cannot become Resolved from writing alone.

**Description:** Nozzle and die wear tolerances when processing high-variance, particulate-laden salvage feedstocks are undefined on both halves of the extrusion problem this file's recursive loop depends on:

- **Polymer path:** `Operations/Plastics.md` has no concrete extrusion hardware specification. Filament-drawing rigs and custom extrusion screws are explicitly routed to `Admin/Trajectories.md` as future blueprints — they do not exist yet, even on paper, beyond that forward pointer.
- **Metal path:** `Operations/Gate_05_Separation_Thermal.md` SC-004 (wire extrusion nozzle design not specified) is the direct counterpart — Open, also routed to Trajectory pending a validated design. Wire drawn from Gate_05's ranked/segregated output needs a die; that die's wear behavior under salvage-grade, contamination-variable metal is exactly what CLF-003 asks about, and no design exists to characterize yet.

**Why It Matters:** Wear tolerances are the acceptance criteria that let §7's contamination-diversion doctrine actually function — CLF-006's triggers (§7.1) route material away from tooling *before* it causes damage, but that only works if the wear thresholds those triggers protect are real numbers, not placeholders. Without CLF-003, the whole recursive loop's tooling-protection logic rests on unvalidated assumptions. This file's own Highest Risk field already names toolhead destruction as a top concern (§File State).

**Provisional acceptance criteria (borrowed, not independently derived):** §7.1's contamination doctrine already contains numeric wear-proxy thresholds designed for a different purpose (contamination-triggered diversion) that are functionally identical to what CLF-003 needs:

| Trigger | Threshold | Source |
|---|---|---|
| Nozzle diameter growth from new | >8% | §7.1, polymer/extrusion path |
| Die pressure rise at constant throughput | >25% | §7.1, polymer/extrusion path |
| Particulate mass fraction | >2% | §7.1, polymer/extrusion path |

These numbers carry the same provisional, design-intent status as the rest of §7 — unratified, and revised only by the evidence rules in §7.3 (any false negative on a safety-critical outcome tightens immediately; loosening requires human governing authority ratification and an Epistemic Ledger entry). Adopting them here does not require ratifying all of §7 — it is a citation, not an independent CLF-003 resolution — but it means CLF-003 is no longer working from zero.

**Resolution Path:**
1. **Hardware must exist before tolerances can be measured.** Neither the polymer filament-drawing rig nor the metal wire-extrusion die (SC-004) has a validated design yet. This is real engineering work with an open solution space, not something a documentation pass can shortcut — per this file's own framing, "it could go a million different paths at present."
2. **Once hardware exists (either path), run the same instrumented-cycle validation §7.3 already specifies:** ≥3 batches deliberately exercising particulate load, nozzle growth, and die pressure; record actual outcomes against the borrowed thresholds; compute false-negative/false-positive rates; tighten or loosen per §7.3's asymmetric rule.
3. **Register the design work itself** — when a polymer extrusion rig or SC-004's wire-die spec moves from Trajectory to active development, that should be logged here and cross-linked, not left implicit.

**Cross-references:** `Operations/Plastics.md` (polymer path, no hardware spec yet); `Operations/Gate_05_Separation_Thermal.md` SC-004 (metal path, wire extrusion nozzle); §7.1 (borrowed provisional thresholds); §7.3 (validation/hardening methodology to apply once hardware exists); `Admin/Trajectories.md` (current parking location for both hardware paths).

---

## Resolution Log

- 2026-07-31: **v0.8.1 — CLF-003 expanded from a single-line table entry to full detail (§8).** Confirmed against source that neither the polymer extrusion path (`Operations/Plastics.md` — filament-drawing rigs routed to Trajectories, no hardware spec) nor the metal path (`Operations/Gate_05_Separation_Thermal.md` SC-004 — wire extrusion nozzle design not specified) has any extrusion hardware yet, real or detailed-on-paper. Borrowed §7.1's provisional wear-proxy thresholds (nozzle diameter growth >8%, die pressure rise >25%, particulate >2%) as CLF-003's acceptance criteria by citation, not independent derivation — same provisional/design-intent status, same §7.3 evidence rules for revision. Explicitly not a resolution: CLF-003 remains Critical/Open, and cannot reach Resolved without physical hardware and instrumented test cycles that do not yet exist. Human governing authority noted the hardware question "could go a million different paths at present" — documentation-honesty progress only, engineering solution space deliberately left open. Operating as Synthesizer per Auditor_Protocols.md v0.29.

- 2026-07-30: **v0.8.0 — §7 Proposed Solutions added** — CLF-006 contamination doctrine, CLF-009 Material Certainty Manifest schema, and validation/hardening logic, drafted and merged as one cross-referenced package. Includes a compound sub-threshold trigger (§7.1) and an assay-gated confidence ceiling (§7.2), both added after adversarial stress-testing against Auditor_Protocols.md Challenge Classes 2, 3, and 5. A cross-consistency check against existing repo thresholds found no numeric contradictions; one terminology collision between this doctrine's "Contamination Diversion" and Gate_04's existing "Material Diversion Rate" was resolved via an explicit disambiguation note (§7.1, with a corresponding addendum to add on Gate_04's side at ratification). **Status: Proposed only — CLF-006 and CLF-009 remain Open in §6.** Nothing in §7 is binding until human governing authority reviews and ratifies the package as a unit; CLF-003 and CLF-004 are untouched by this proposal and remain separately Open/Critical. Operating as Synthesizer per Auditor_Protocols.md v0.29.

- 2026-07-19: Stale "Registration status" note corrected — this file's own text claimed registration in `Routing.md`, `Discovery.md`, `Unknowns.md`, and `Automation/AUDIT_HARNESS.py` was outstanding, contradicting all four of those files, which have carried it since 2026-07-06. `Unknowns.md`'s PC-005 had flagged this as "possibly stale, not independently re-verified" since v4.20 (2026-07-12) without anyone closing the loop — done now, PC-005 marked Resolved.

- 2026-07-17: **v0.7.0 — Embedded Value Preservation ratified; CLF-004
  reframed; CE-006 directed approach cross-referenced (human governing
  authority).** §2a's proposed doctrine adopted into operative Scope
  Boundary text — Pending Ratification 1 → 0. Cross-reference to
  `Operations/Gate_02_Triage.md` added there (see that file's Resolution
  Log). CLF-004's candidate chlor-alkali pathway reframed explicitly as
  one of three options under consideration, not a selected path — the
  file's own prior wording ("third option... distinct from") was already
  non-exclusive; tightened further to make that reading unambiguous.
  Cross-referenced `Architecture/Chemistry.md` CE-006's 2026-07-17 directed
  approach (capture-and-nullification via existing Air_Scrubber.md
  infrastructure). CLF-004 remains Open/Critical — a directional decision
  on the chlorine problem is not the same as CLF-004 being resolved; the
  sourcing choice among the three candidates and CE-006's verification
  work both remain outstanding.

- 2026-07-12: Ethical Anchor field corrected — was using a non-canonical variant (backticked, `Admin/`-prefixed: "Defer to `Admin/Ethical_Constraints.md` if present.") instead of the canonical plain-text string ("Defer to Ethical_Constraints.md if present."). Same drift found across 9 files in a full-repository Phase 1 sweep (ChatGPT, adapted local-disk harness run) — verified independently against source before patching. No semantic change; the anchor's meaning was never in question, only its exact text.
- 2026-07-11: **v0.6.1 — Challenges Subtype field added: Solution-Track.** This file has used the full eleven-field File State schema and worked-engineering content since v0.3.0, and `Admin/File_Template.md`'s Challenges/ subtype doctrine names it directly as a current Solution-Track example. Declaring the field explicitly closes the gap between doctrine and this file's own File State table — no schema change, no promotion event (promotion already happened in practice; this just records it).
- 2026-07-07: **v0.6.0 — CLF-005 resolved (symbol rename); CLF-004 candidate pathway logged (human-directed).**
  (1) **CLF-005 resolved.** Direct comparison of this file's $\Phi_{ext}$ usage against `Challenges/Return_To_Eden.md`'s Section 3 Eden Index formulation confirmed the two are different metrics — Return_To_Eden.md's is a normalized, baselined ecosystem-subsidy ratio; this file's was an unnormalized, process-level supply-dependency concept. Renamed to **Supply Chain Dependency ($\Delta_{sc}$)** throughout §1 to remove the collision. No change required in Return_To_Eden.md.
  (2) **CLF-004 candidate pathway logged**, sourced from human governing authority directly rather than an agent audit pass: on-site acid synthesis via salt-water electrolysis with a homemade ion-selective membrane (chlor-alkali-type process), offered as a third option alongside external sourcing and closed-loop reclamation. Logged as a candidate, not a resolution — chlorine gas co-production requires a containment/scrubbing design against Ethical_Constraints.md's toxic-handling doctrine before this can be adopted. CLF-004 remains Open/Critical.
  (3) Both changes made under explicit human direction this session; no self-approval of unknown resolution.
- 2026-07-06: v0.5.0 — Math rendering fix; four structural gaps logged; embedded-value principle drafted (unratified). *(full detail in prior version's log — see repository history)*
- 2026-07-06: v0.4.0 — Reconciliation pass. FL- collision reverted to CLF-; CLF-004/005 restored after being dropped; CLF-006 added; PIR multi-vector definition reconciled with worked example; Sidecar Link corrected; version numbering corrected.
- 2026-07-06: v0.2.4 (intervening) — Multi-auditor hygiene pass. Added Degraded Operation & Failure Modes section; downgraded Status to Exploration; renamed unknowns CF-→FL- (introduced new collision); dropped CLF-004, CLF-005, and Resolution Log without carrying content forward.
- 2026-07-06: v0.3.0 — Integration audit. Ethical Anchor restored to canonical string. CF-001/002/003 renamed to CLF-001/002/003. CLF-004/005 logged. Characterization.md/Metals.md labeled [PLANNED]. Flat path fixed. File State standardized. PIR sub-vector breakdown restored.
- 2026-07-06: v0.2.0 — Initial committed version.

---

*Challenges/ files define problems and requirements. They do not freeze solutions. The Forge's answer to this challenge will evolve. The obligation it names will not.*
