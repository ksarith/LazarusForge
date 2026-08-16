# Challenges/Energy_Scarcity.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
---

> *Energy does not announce its absence. It is simply the thing that was there, that let everything else happen — and then, in its absence, did not.*
> *A Forge that only asks how to power itself has answered the wrong question.*

---

## File State

| Field | Value |
|---|---|
| **Status** | Active |
| **Challenges Subtype** | Problem-Statement |
| **Version** | v0.1 |
| **Last Updated** | 2026-07-19 |
| **Owner** | Challenges/ |
| **Verification Ref** | `Admin/Verification_Gates.md` |
| **Ethical Anchor** | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**Challenge Class:** External — energy poverty, grid fragility, and fossil-fuel dependency exist as physical, economic, and structural conditions independent of the Forge. The Forge did not create these conditions; it responds to them.

**Negative-space principle:** The Forge's architecture is the fossil record of the pressures that shaped it. This challenge is permanent; the architectural responses to it are temporary local answers. Solutions will be superseded. The obligation this file names will not.

**This file owns:**
- The crisis framing for energy poverty, grid fragility, and the structural gap between energy as a precondition for modern life and its uneven, fragile, or absent delivery
- The engineering requirements governing energy-access approaches within this challenge space
- The Forge's current architectural responses under existing energy doctrine
- The long-term objective for community energy sovereignty

**This file does not own:**
- The Forge's own operational energy strategy, power mode envelopes, and generation interlocks → `Operations/Energy.md` (EV-001, EV-002, EV-003)
- Deep-environment battery degradation physics and Leviathan power envelope → `Tests/Leviathan_testing.md` (LT-001, LT-002)
- Superconductivity horizons and exploratory v1+ power transmission → `Operations/Energy.md` §Superconductivity Horizons
- Heat pump sizing, atmospheric moisture yield, and thermal recovery doctrine → `Architecture/Thermal_Systems.md` (TH-001, TH-003)
- Operating cost baseline and energy-linked economic modeling → `Admin/Economics.md` (EC-002)
- Waste heat as a cross-domain resource → `Challenges/Waste.md`

This distinction matters and is easy to blur: `Operations/Energy.md` answers "how does the Forge power itself." This file answers a different, prior question — "why does energy access matter enough that the Forge should treat it as a purpose, not just a utility bill." The same relationship Water.md has to Living Waters, this file has to the Forge's energy doctrine.

---

## File Purpose

This file exists to establish that energy poverty and grid fragility are structural conditions the Forge must respond to as a core purpose, not merely an operational input it happens to consume. Without this file, `Operations/Energy.md`'s design choices (salvage-first generation, incremental grid independence, multiple small contributors over single large sources) would read as pure engineering pragmatism rather than a deliberate answer to the same crisis Water.md and Waste.md name for their own domains. This file gives the Forge's energy doctrine a reason beyond "the Forge needs power to run."

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Energy poverty and grid fragility are experienced differently by region and context (chronic absence vs. intermittent failure vs. affordability), and a single Forge response cannot address all three with one mechanism | General observation, consistent with `Operations/Energy.md`'s "multiple small contributors" design philosophy | Medium | A field deployment demonstrates one mechanism generalizes further than expected, or fails to generalize as far as assumed |
| ASM-002 | A Forge unit deployed in an energy-poor or grid-fragile context can generate a net-positive energy surplus for the surrounding community, not just for its own operation | Extension of `Operations/Energy.md`'s "multiple small contributors" philosophy beyond the Forge's own boundary; not yet validated at any deployment | Low | EV-001 (Forge power demand) resolved with measured figures, enabling a real surplus calculation |
| ASM-003 | Salvage-sourced generation (motor-generators, biogas, solar) can meet a meaningful fraction of community-scale demand, not just Forge-internal demand, without requiring purpose-built industrial power infrastructure | Consistent with `Operations/Energy.md`'s salvage-first generation philosophy, extended beyond its current Forge-internal scope | Low | First community-facing energy deployment characterizes actual surplus delivered |
| ASM-004 | Energy and water are sufficiently coupled (energy produces water; water stores and transports heat) that treating them as one of several linked resource domains, rather than fully independent challenges, is the right long-term framing | `Tests/Living_Waters.md` "Four-Domain Observation" — explicitly declared as a long-horizon observation, not a current commitment | Low | Enough real deployment data exists across both challenges to test whether the coupling is load-bearing or just thematically convenient |

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Life Preservation doctrine; community sovereignty imperative |
| `Operations/Energy.md` | The Forge's own generation interlocks, power mode envelopes, and salvage-first generation philosophy — this file draws on that doctrine as evidence of a plausible response, without owning it |
| `Architecture/Thermal_Systems.md` | Heat pump, thermal recovery, and Peltier doctrine; TH-001/TH-003 feed community-facing thermal-to-electrical pathways |
| `Admin/Economics.md` | Operating cost baseline (EC-002); any claim of "net-positive community surplus" must be economically legible, not just physically possible |
| `Admin/Safety_Protocols.md` | Battery and generation hazard doctrine — community-facing energy systems inherit the same containment requirements as Forge-internal ones |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Operations/Energy.md` | This file supplies the "why" that frames EV-001 through EV-003 as more than internal engineering constraints |
| `Tests/Living_Waters.md` | Four-Domain Observation names Energy as one of the linked resource domains this challenge and that one may eventually share architecture with |
| `Challenges/Waste.md` | Waste heat and biogas feedstock recovery overlap directly with this challenge's energy-recovery requirement |
| `Admin/Economics.md` | Any future community-facing surplus model this challenge motivates will need an economic accounting layer |

---

## The Crisis

Energy is not a convenience layered on top of modern life. It is the precondition for nearly everything else — clean water pumped and purified, food refrigerated and cooked, medicine kept viable, light after dark, communication across distance, a hospital's equipment staying on. Where energy is absent, unreliable, or unaffordable, all of these compound simultaneously. It is rarely experienced as "the energy problem" in isolation — it is experienced as the water that didn't get pumped, the vaccine that spoiled, the clinic that went dark mid-procedure.

The crisis takes different shapes in different places. In some regions it is chronic absence — no grid connection at all, and no clear path to one. In others it is grid fragility — a connection that exists on paper and fails in practice, tripped by storms, overload, underinvestment, or conflict, often precisely when it is needed most. In still others it is affordability — a grid that reaches a household but at a cost that forces impossible tradeoffs between light, heat, and food.

Centralized energy infrastructure concentrates this fragility. A single transmission failure, a single fuel supply disruption, a single underfunded utility, can leave enormous populations without power simultaneously — and the communities with the least infrastructure redundancy are, almost universally, the ones who absorb the failure first and recover from it last. Diesel generators fill some of the gap, at a cost — financial, in fuel dependency, and in emissions — that reproduces the same fragility in a different form: dependency on fuel supply chains as brittle as the grids they replace.

Reliable energy access is not formally recognized as a human right the way water often is, but its absence produces the same downstream harms water scarcity does — to health, to education, to economic opportunity, to the basic capacity to plan a life beyond the next outage. The gap between what energy access could unlock and what is actually delivered is where this challenge lives.

---

## Engineering Requirements

Any energy-access approach operating within this challenge space must satisfy the following conditions, independent of the specific technology deployed:

- **Do not require a purpose-built industrial supply chain** — approaches dependent on specialized manufacturing, rare components, or long international shipping lines recreate the same fragility they're meant to solve. Salvage-first generation, consistent with `Operations/Energy.md`'s existing doctrine, is the default posture.
- **Degrade gracefully, not catastrophically** — a system that fails should fail toward reduced capacity, not toward the same cascading total outage centralized grids are prone to. Multiple small contributors over single large sources.
- **Be economically legible to the community it serves** — a technically elegant system that produces power no one can afford, or whose maintenance cost exceeds what the community can sustain, has not solved the problem. It has relocated it.
- **Avoid trading one dependency for another** — replacing grid dependency with fuel dependency, or fuel dependency with a dependency on Forge-specific replacement parts unavailable locally, does not constitute progress.
- **Be honest about intermittency rather than hide it** — solar, wind, and biogas are not always-on sources. Any approach must be transparent about duty cycle and storage requirements rather than implying a false parity with grid-always-on assumptions.
- **Treat surplus, where it exists, as shareable** — a Forge unit that generates more than its own operational need in an energy-poor context has an obligation to consider that surplus's value to the surrounding community, not just to Forge efficiency metrics. Community surplus is meaningful only after accounting for conversion efficiency, storage losses, maintenance energy, and parasitic loads — a generation figure is not a surplus figure until those are subtracted. Community-facing distribution is strictly subordinate to active validation of the Forge's own internal power demand (`Operations/Energy.md` EV-001); this requirement does not license assuming a surplus exists before that baseline is measured, and no engineering effort should proceed as though EV-001 were already resolved.

---

## Current Forge Approaches

`Operations/Energy.md` represents the Forge's current operational posture toward its own power needs — grid-to-salvage lifecycle staging, salvaged motor-generators, regulated biogas digestion, modular solar, and opportunistic thermal recovery. That doctrine was written to answer "how does the Forge power itself," and it does that well. It was not written to answer "what does the Forge owe the energy-poor context it may be operating in" — that is the gap this file exists to name.

Current approaches, viewed through this challenge's lens rather than Operations/Energy.md's internal-efficiency lens:

- **Salvage-first generation** (motor-generators, biogas, solar) is already the Forge's default posture — this challenge reframes that choice as a deliberate answer to supply-chain fragility, not just a cost-saving measure.
- **Multiple small contributors over single large sources** is already Forge doctrine for internal resilience — the same logic applies directly to community-facing resilience against grid failure.
- **Opportunistic thermal recovery** (Gate 05 exhaust heat) is currently scoped as internal-only — a genuinely community-facing energy response would need to ask whether recovered heat or power has value beyond the Forge's own boundary.

No mechanism currently exists for routing Forge-generated energy surplus to a surrounding community. This is a real gap, not a design choice — see ES-001.

---

## Long-Term Objective

The long-term objective is not simply keeping the Forge powered. It is treating reliable, affordable, locally-sourced energy access as something the Forge's presence in a community can materially improve, not just something the Forge quietly consumes.

That means building toward a posture where a deployed Forge unit is, at minimum, energy-neutral to the community it operates in, and where possible, a net contributor — without requiring that community to take on a dependency on Forge-specific infrastructure to receive that benefit. It means treating grid fragility the way `Challenges/Water.md` treats water infrastructure fragility: not as background noise, but as the actual shape of the problem.

`Tests/Living_Waters.md`'s Four-Domain Observation names Energy, Water, Atmosphere, and Biology as resource domains that may eventually share architecture. This file is what makes Energy real as a domain in its own right, rather than a background utility the other three quietly assume.

The grid does not have to be the only shape reliable power can take.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — this file is new; no deployment or physical testing has occurred against its requirements | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |

---

## Open Unknowns

| ID | Description | Status | Risk |
|---|---|---|---|
| ES-001 | Community-facing energy surplus routing mechanism undefined — no Forge file currently defines how, or whether, generated surplus beyond internal operational need could be delivered to a surrounding community. Directly blocks ASM-002 and ASM-003. | Open | Major |
| ES-002 | Economic legibility threshold for community-facing systems undefined — no defined method exists for confirming a deployed system's maintenance cost is actually sustainable for the community it serves, as distinct from the Forge's own economics. Feeds `Admin/Economics.md` EC-002. | Open | Major |
| ES-003 | Intermittency communication doctrine undefined — no defined standard exists for how a deployed system should represent its own duty cycle and storage limitations to a community relying on it, to avoid false parity with always-on grid expectations. | Open | Minor |

*ES-001 is the load-bearing unknown for this file's Long-Term Objective — without a surplus-routing mechanism, "energy-neutral or net-contributor to the surrounding community" remains aspirational rather than actionable.*
*ES cluster registered in `Unknowns.md` v4.19, 2026-07-12.*

---

*See: `Operations/Energy.md` for the Forge's own operational energy doctrine and EV-001 through EV-003. See: `Tests/Living_Waters.md` for the Four-Domain Observation naming Energy as a linked resource domain. See: `Admin/Economics.md` for operating cost baseline (EC-002). See: `Architecture/Thermal_Systems.md` for heat pump and thermal recovery doctrine (TH-001, TH-003).*

---

## Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  N/A for Challenges Problem-Statement subtype. (1) Open Unknowns **3** =
  ES-001–003, matches local table and `Unknowns.md` (already registered
  v4.19). (2) ES-001 correctly flagged as load-bearing for Long-Term
  Objective. (3) No ES-* closed. Human-directed.

- 2026-07-12: v0.1 — Initial file creation. Proposed by James, motivated by the observation that `Challenges/` had grown to cover water, waste, biofouling, critical minerals, planned obsolescence, and emergence as external problem-statements, but energy — despite being at least as globally consequential and already load-bearing for `Operations/Energy.md`'s own design choices — had no equivalent framing file. Structured identically to `Challenges/Water.md` (the closest precedent: an External Challenge Class problem with an existing Operations-layer doctrine file already responding to it in practice). ES-001 through ES-003 registered as new unknowns, using an `ES-` prefix chosen specifically to avoid collision with `Operations/Energy.md`'s `EV-` prefix, `Architecture/Engineering.md`'s `EN-` prefix, and `Admin/Economics.md`'s `EC-` prefix. Not yet audited by any second agent at time of creation. *(Correction, 2026-07-19: this note was stale within hours of being written — see the third Resolution Log entry below, same day, recording three second-agent audits already completed. Gate 1 review is done, not outstanding.)*
- 2026-07-12 (same day): File committed to the repository as `Challenges/Energy_Scarcity.md` rather than `Challenges/Energy.md` — the more precise name, since it avoids any ambiguity with `Operations/Energy.md` at the filename level, not just in Scope Boundary prose. Title line corrected to match. No other content changed.
- 2026-07-12 (third entry, same day): Three second-agent audits run against this file. Two of three raised File State findings (Status: Active "contradicts" Exploration classification; missing Spec Gates field; bolded table keys breaking harness parsing) that were checked against `Challenges/Water.md` and found to be false positives — Active and the omitted Spec Gates field are the correct, doctrine-sanctioned values for the Problem-Statement lean schema, not defects. A third finding (stale `Challenges/Energy.md` cross-reference) was already resolved in the file the auditors were given but flagged anyway, suggesting at least one audit worked from a pre-fix snapshot. One finding across all three audits was genuine and adopted: Engineering Requirements' surplus clause now explicitly subordinates community distribution claims to EV-001 validation and notes that surplus is only meaningful net of conversion, storage, maintenance, and parasitic losses — both added to the "Treat surplus" bullet above.
- 2026-07-19: Ethical Anchor field corrected — was using a non-canonical variant (backticked, `Admin/`-prefixed: "Defer to `Admin/Ethical_Constraints.md` if present.") instead of the canonical plain-text string ("Defer to Ethical_Constraints.md if present."). This file was created 2026-07-12, the same day as PC-006's 9-file sweep fix in `Unknowns.md` v4.20 — this file was evidently missed by that sweep (created same-day, likely after the sweep's fetch), and none of the three second-agent audits logged above caught it either. Flagged by a Grok pass 2026-07-19 (cross-checked against source before patching, per standard practice — Grok's broader claims in that same report were stale, but this specific finding held up). No semantic change; the anchor's meaning was never in question, only its exact text.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| — | — | No paths formally abandoned yet — this file is new | — |

---

## Drift Indicators

- Body proposes a community-facing energy solution that depends on purpose-built industrial supply chains rather than salvage-first generation
- Body treats intermittent sources (solar, biogas, wind) as always-on without disclosing duty cycle and storage assumptions
- A deployed system's maintenance cost is asserted as sustainable without reference to ES-002 or actual community economic context
- This file's scope drifts into redefining `Operations/Energy.md`'s internal generation doctrine rather than staying at the external-challenge framing level
- ES-001 (surplus routing) remains unreviewed past 90 days while community-facing deployment claims proceed elsewhere in the repository
- Open Unknowns count diverges from what is registered in `Unknowns.md`

---

*Challenges/ files define problems and requirements. They do not freeze solutions.*
*The Forge's answer to this challenge will evolve. The obligation it names will not.*
