# Economics.md — LazarusForgeV0

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-07-06                                                          |
| Auditor          | Claude — Skeptic/Auditor (rename pass); Gemini — Skeptic/Auditor (Exploration audit, path/gap findings) |
| Open Unknowns    | 5 (ECN-001, ECN-002, ECN-004, ECN-005, ECN-006)                     |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Dynamic resource doctrine — buy what you need, sell what you don't
- Procurement doctrine — acquire against confirmed need
- Surplus disposition doctrine — decision logic for what to sell,
  when, and through what channel
- Market navigation framework — the optimal pathway model for
  operating on both sides of the market simultaneously
- Revenue model for external outputs (TR-001 input 2 of 3)
- Input cost doctrine — when purchasing exceeds fabrication cost
  and vice versa
- v1 profitability baseline framework (resolves TR-001)
- Interface between salvage-first philosophy and market participation
- Value stream taxonomy — what the Forge produces that has
  external market value
- Barter doctrine — canonical definition, valuation standard,
  and accounting treatment for all non-monetary exchange

**This file DOES NOT define:**
- FRT doctrine or floor value (→ `Admin/Trajectories.md`)
- FRT per-cycle logging (→ `Operations/Gate_07_Utilization.md`)
- Primary KPI definition (→ `Architecture/Forge_flow.md`)
- Energy operating cost model (→ `Operations/Energy.md` EV-001)
- Component procurement manifest (→ `Architecture/Geck_forge_seed.md`)
- Revenue allocation above FRT floor (→ `Admin/Trajectories.md`
  — operator-defined domain)
- Pricing schedules or market rate data (→ ECN-004 — real-time,
  operator-maintained)
- Legal or tax compliance (→ ECN-005 — human decision,
  jurisdiction-specific)
- Safety envelopes for commercial value streams involving hazardous materials or processes (→ `Admin/Safety_Protocols.md`, `Operations/Plastics.md`, `Operations/Woodworking.md` — commercial value realization is strictly subservient to these; a value stream is not authorized by this file's existence in the Taxonomy of Value Streams table)

---

## File Purpose

This file provides the economic framework the Lazarus Forge uses to
navigate the market it operates within. The Forge is simultaneously
a buyer and a seller — it acquires salvage, consumables, and
occasionally precision capability it cannot yet fabricate; it sells
recovered material, fabricated parts, and processing capacity it
produces in excess of internal need. The optimal economic pathway
at any moment depends on which side of that equation is more
favorable, and that is a dynamic judgment, not a fixed rule.

The core doctrine is simple: buy what you need, sell what you don't.
The framework exists to operationalize that instinct — to give the
operator a principled basis for procurement and surplus decisions
rather than leaving them to improvisation.

Without this file, three specific gaps persist: (1) TR-001 (v1
profitability baseline) has no resolution path — the v0→v1 transition
is blocked; (2) procurement decisions have no doctrine — the Forge
may accumulate stockpiles that consume capital without generating
return; (3) surplus disposition has no framework — recovered material
and fabricated output may be undersold, stockpiled indefinitely, or
disposed of at a loss when market participation would have funded
the next cycle.

**Relationship to salvage-first doctrine:** Market participation
does not contradict salvage-first philosophy — it extends it. The
same logic that says "preserve value before reducing" applies to
the Forge's own resource flows. Buy what delivers more value than
the cost of fabricating it. Sell what delivers more value externally
than the cost of holding it. The market is the mechanism; salvage-first
is the philosophy that governs what enters and exits through it.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | A local market exists for recovered ferrous and non-ferrous metals at v0 | Scrap metal markets are broadly available in most US regions | High | Site location has no accessible scrap market within viable transport distance |
| ASM-002 | Salvage acquisition cost is below fabrication cost for most feedstock at v0 | Core salvage-first premise | High | Fabricated feedstock becomes cheaper than salvage acquisition — unlikely at v0 scale |
| ASM-003 | Operating costs at v0 are primarily energy, consumables, and operator time | Bootstrap scale — no debt service, no facility lease assumed | Medium | Facility lease, debt service, or labor costs materially change the cost structure |
| ASM-004 | The Forge produces surplus recoverable material before it produces surplus fabricated parts | Gate sequence — recovery precedes fabrication | High | Fabrication throughput exceeds recovery throughput — unusual at v0 |
| ASM-005 | Barter is a valid economic exchange alongside monetary transaction | Rural and semi-rural operational contexts; Axiom P-3 alignment | Medium | Legal or tax context requires monetary-only accounting |

---

## I. Dynamic Resource Doctrine

### Core Principle

**Buy what you need. Sell what you don't.**

This is not a simplification — it is the complete doctrine. Every
procurement and surplus decision in the Forge derives from it.
The framework below operationalizes it; the principle governs
when the framework is ambiguous.

The doctrine has two active sides:

**Buy side:** Acquire inputs only against confirmed operational need.
Do not stockpile in anticipation of future need unless storage cost
is negligible and market availability is genuinely uncertain.
The Forge's capital is better deployed in operational cycles than
in inventory that may never be consumed.

**Sell side:** Surplus is recovered value waiting to be converted.
Holding surplus beyond operational need ties up storage, capital,
and attention. The market converts surplus into the resources the
next cycle needs.

### Why Dynamic

The optimal economic pathway shifts as the Forge matures, as local
market conditions change, and as the Forge's own capability
develops. What the Forge should buy at v0 bootstrap may be something
it fabricates by v1. What it sells as raw recovered material at v0
may become a fabricated component with higher margin at v1.

The doctrine does not prescribe a fixed economic model — it
prescribes a posture: stay close to operational need on the buy
side, stay close to market opportunity on the sell side, and
reassess both continuously.

---

## II. Procurement Doctrine

### Acquire Against Confirmed Need

Procurement is triggered by a confirmed operational gap — a
consumable depleted, a component unavailable from salvage within
the planning horizon, a precision capability the Forge cannot yet
produce. It is not triggered by opportunity, price signals alone,
or anticipated future need without a defined consumption path.

**Procurement decision sequence:**

1. **Can the Forge produce this from existing salvage or feedstock?**
   If yes — produce it. Procurement is not yet triggered.

2. **Can this be acquired through salvage acquisition rather than
   purchase?**
   If yes at acceptable time cost — acquire through salvage.
   Purchased precision capability is not a failure of salvage-first
   doctrine; purchasing a commodity available through salvage is.

3. **Is the purchase cost less than the fabrication cost plus
   opportunity cost of the fabrication time?**
   If yes — purchase. This is the input cost threshold. A Forge
   that fabricates everything it could purchase cheaply is
   misallocating its highest-value resource: fabrication capacity.

4. **Is the need confirmed within the current planning horizon?**
   If not confirmed — hold. Unconfirmed needs are logged as
   pending, not purchased against.

### Input Cost Threshold

The input cost threshold (step 3 above) is the economic expression
of salvage-first doctrine applied to the Forge's own operations.
The relevant comparison is:

> **Purchase price** vs. **Fabrication cost + Opportunity cost**

Fabrication cost includes: materials consumed, energy consumed,
operator time, and tool wear. Opportunity cost is what the
fabrication capacity could have produced instead.

At v0, opportunity cost is low — the Forge has limited throughput
and fabrication capacity is not yet the bottleneck. As the Forge
matures, opportunity cost rises and the input cost threshold shifts
toward purchasing more precision components.

This is not a contradiction of the salvage-first principle — it
is the principle applied recursively. Value recovery per kWh is
the primary KPI. If purchasing a precision component delivers more
value per kWh than fabricating it, purchasing is the correct
salvage-first decision.

### Stockpile Doctrine

Stockpiling is not procurement. Stockpiling is deferred procurement
decision-making that consumes storage and capital without advancing
operational capability.

**Acceptable stockpile conditions:**
- Consumables with known high consumption rate and negligible
  storage cost (welding wire, abrasives, flux)
- Components with genuinely uncertain market availability and
  confirmed future need within the planning horizon
- Salvage feedstock acquired below threshold cost where storage
  is available — this is feedstock inventory, not a stockpile

**Unacceptable stockpile conditions:**
- Materials acquired because the price was favorable without
  a confirmed consumption path
- Components acquired in anticipation of capability the Forge
  does not yet have
- Recovered output held indefinitely because a premium buyer
  has not been found — the market rate today is better than
  storage cost plus capital cost of holding

---

## III. Surplus Disposition Doctrine

### What the Forge Produces That Has External Value

The Forge generates several distinct value streams that may exceed
internal need:

| Value Stream | Description | Typical Form |
|---|---|---|
| Recovered ferrous metal | Iron, steel separated from mixed feedstock | Bulk scrap, sorted billet |
| Recovered non-ferrous metal | Copper, aluminum, zinc, lead from mixed feedstock | Bulk scrap, sorted bar |
| Recovered rare and critical minerals | From electronics, batteries, catalytic converters | Concentrated fraction — ECN-001 |
| Fabricated components | Parts made to spec, beyond internal need | Functional parts, tooling |
| Processing capacity | Gate operations as a service — triage, reduction, separation | Service offering |
| Recovered functional items | Items triaged as reusable, beyond internal need | Sold as-is or reconditioned |
| Pyrolytic outputs | Fuel oil, syngas from plastic processing | Energy commodity |
| Biochar | Wood processing byproduct | Agricultural amendment |

Not all value streams will be active at v0. The taxonomy exists
so surplus is recognized and routed rather than stockpiled or
discarded.

### Surplus Disposition Decision Sequence

When a value stream exceeds internal need:

1. **Can this surplus be consumed in the next operational cycle?**
   If yes within a defined horizon — hold as operational inventory.
   Not surplus yet.

2. **Does another Forge instance in the network need this?**
   If yes — route through `Architecture/Forge_Net.md` before external market.
   Internal network transfer preserves value within the ecology.

3. **What is the current market rate and what is the storage cost
   per unit time?**
   If market rate exceeds storage cost significantly — sell now.
   If storage cost is negligible and price is expected to improve
   with confidence — hold with a defined review horizon.

4. **Is barter more favorable than monetary sale for this surplus?**
   If yes — barter is a valid disposition path. A recovered
   aluminum surplus traded for welding wire is an economic
   transaction regardless of whether money changes hands.

5. **If no market exists at acceptable terms — can this surplus
   be consumed in a lower-value internal application?**
   Recovered material that cannot be sold at acceptable terms
   becomes internal feedstock for fabrication. Value recovery
   continues internally rather than being abandoned.

### The Hold Decision

Holding surplus is a decision, not a default. Every held surplus
item has a storage cost, a capital cost, and a degradation risk.
Held surplus requires a defined review horizon — a date at which
the hold decision is reassessed against current market conditions.

Surplus that has passed its review horizon without a disposition
decision is not being managed — it is being ignored. Ignored surplus
is stockpile by inaction, which is the failure mode this doctrine
exists to prevent.

---

## IV. Market Navigation Framework

### The Forge as Market Participant

The Forge operates on both sides of the market simultaneously.
At any given moment it is:
- A buyer of salvage feedstock, consumables, and precision capability
- A seller of recovered material, fabricated output, and processing
  capacity

The optimal economic pathway is not fixed — it is the configuration
at a given moment that maximizes value recovered per operational
dollar spent, while maintaining the FRT floor and covering operating
costs.

### Market Position Assessment

The operator should assess market position at each cycle close
(aligned with FRT logging in Gate_07). The assessment is not
a complex financial model — it is a structured comparison:

**Buy side assessment:**
- What did we purchase this cycle and at what cost?
- Was any purchase available through salvage that we bought instead?
- Did any fabrication consume capacity that should have been
  purchased externally?
- What confirmed needs exist for the next cycle?

**Sell side assessment:**
- What surplus exists from this cycle?
- What did we sell, at what price, through what channel?
- What is still held and what is its review horizon?
- Did any surplus degrade or lose market value while held?

**Optimal pathway signal:** If buy-side costs are rising and
sell-side returns are falling, the Forge is in margin compression.
The response is not to increase volume — it is to improve
the quality of the surplus (fabricated components rather than
raw recovered material) and reduce the cost of inputs
(more salvage, less purchase).

### Value Ladder Doctrine

Not all surplus from a value stream has the same market value.
The Forge should seek the highest position on the value ladder
available to it at each cycle:

| Raw recovered metal | → | Sorted and graded metal | → | Fabricated component |
|---|---|---|---|---|
| Lowest margin | | Medium margin | | Highest margin |

Moving up the value ladder requires capability and time. The
correct position on the ladder at any moment is the highest one
the Forge can reach without sacrificing operating cost coverage
or FRT floor maintenance. Reaching for a higher ladder position
that delays surplus disposition past its optimal sale window
is a margin optimization that costs more than it earns.

**Energy-cost floor for thermally-recovered surplus:** The primary
KPI (value recovered per kWh, `Architecture/Forge_flow.md`) applies
to surplus disposition, not only to primary recovery. A pyrolytic
or thermally-separated output (e.g., syngas, fuel oil from
`Operations/Plastics.md`) is not a positive-value stream by virtue
of having a buyer or barter partner — it must demonstrate a
net-positive value return relative to the localized energy cost of
the gate operation (`Operations/Plastics.md`, `Operations/Gate_05_Separation_Thermal.md`)
that produced it. A market or barter return that costs more energy
to generate than it recovers is an accounting illusion, not surplus.

### Channel Selection

The Forge has multiple channels for both acquisition and disposition.
Channel selection affects margin, speed, and relationship capital:

**Acquisition channels (ranked by salvage-first preference):**
1. Direct salvage acquisition — lowest cost, highest alignment
2. Community donation or drop-off — zero acquisition cost,
   variable quality
3. Barter with other Forge instances or community members
4. Local secondary market (auctions, estate sales, scrap dealers)
5. Direct purchase from suppliers — highest cost, reserved for
   confirmed precision needs

**Disposition channels (ranked by margin preference):**
1. Direct sale to known buyer — highest margin, requires
   relationship capital
2. Local secondary market (scrap dealers, fabricators,
   agricultural supply)
3. Online marketplace — broader reach, higher logistics cost
4. Barter — valid when the received item exceeds the cash
   equivalent value to the Forge
5. Forge network transfer — internal to the ecology;
   not a market transaction but preserves value

Channel selection is operator judgment. The framework provides
the ranking logic; the operator applies it to local conditions.

---

## V. v1 Profitability Baseline (TR-001 Resolution Framework)

TR-001 in `Admin/Trajectories.md` blocks the v0→v1 transition
because "profitably" in the v1 exit condition has no defined
meaning. This section provides the framework for that definition.
It is not the final baseline — that requires operational data
(ECN-002). It is the structure that operational data will fill.

### Profitability Definition

The Forge operates profitably at v1 when across a defined
measurement period:

> **Revenue + Barter Value Generated**
> minus **Operating Costs**
> minus **FRT Reinvestment (floor minimum)**
> = **Positive surplus**

All three components must be defined before the baseline
can be established:

**Component 1 — Operating Costs**
The sum of: energy cost (from `Operations/Energy.md` EV-001 when resolved),
consumables, any facility cost, and operator time valued at
a declared rate. At v0, operator time may be valued at zero
for bootstrap purposes — but must be declared, not assumed.

**Component 2 — Revenue and Barter Value**
The sum of: surplus disposition proceeds across all value
streams. Barter value is the market equivalent of received
goods. Internal Forge network transfers are not revenue —
they are value preservation within the ecology.

**Component 3 — FRT Reinvestment**
The FRT floor percentage (declared per Trajectories.md TR-002)
applied to the gross throughput value of the cycle. This is
subtracted before surplus is calculated — reinvestment is not
optional above the floor.

### Measurement Period

The measurement period for v1 profitability assessment is
operator-declared at v0 commissioning — aligned with the
FRT cycle definition in Gate_07. A measurement period too
short (single cycle) is noise. A measurement period too
long (annual) delays the v0→v1 signal. A rolling three-cycle
average is the suggested proxy until operational data
provides a better basis.

### Baseline Calibration Path

TR-001 closes when:
1. Operating cost model is established (`Operations/Energy.md` EV-001 resolved)
2. At least one full measurement period of revenue and barter
   value data exists
3. FRT floor is calibrated from placeholder to declared value
   (TR-002 resolved)
4. The operator declares the profitability calculation against
   these three inputs and confirms it is positive

This file provides the framework. The data comes from operations.
The declaration is a human decision.

---

## VI. Barter Doctrine

This file is the canonical owner of barter doctrine for the
LazarusForge repository. Any file that references barter as a
valid economic exchange routes here for definition, valuation
standard, and accounting treatment.

### What Barter Is

Barter is a direct exchange of goods, materials, or services
without monetary intermediary. Within the Forge's economic
framework, barter is a fully valid economic transaction — not
a workaround or a fallback. The Forge's primary KPI (value
recovered per kWh) does not distinguish between monetary and
barter transactions. A recovered aluminum surplus traded for
welding wire is an economic cycle that advanced the Forge's
capability regardless of whether money changed hands.

Barter is particularly natural in the Forge's operating context:
- Salvage networks are relationship-based and barter-friendly
- Rural and semi-rural contexts often prefer barter for
  equipment, materials, and services
- Forge network transfers between instances are barter by
  nature — internal value exchange without external pricing
- Axiom P-3 (Collaboration and Mutual Benefit) is structurally
  served by barter — it builds community relationships that
  monetary transactions do not

### Barter Valuation Standard

Barter transactions must be valued for FRT and profitability
calculations. The standard valuation method is:

> **Market replacement cost of received goods or services
> at the time of transaction**

This means: what would the Forge have paid to acquire the
received item through the next-best available channel at the
time of the exchange? That figure is the barter value for
accounting purposes.

**Why replacement cost, not market sale price of given goods:**
The Forge's economic interest is in what it received, not what
it gave up. Valuing barter by the sale price of surrendered
goods creates asymmetric accounting — it measures the cost
side of the exchange, not the value gained. Replacement cost
of received goods measures the value the Forge actually captured.

**When market replacement cost is unavailable:**
If no clear market rate exists for the received goods or
services, the operator declares a valuation basis and logs it.
Declared valuation is acceptable at v0. Undeclared and unlogged
barter is not acceptable — a transaction with no valuation
record cannot feed the profitability baseline or FRT calculation.

### Barter Accounting Treatment

Barter transactions appear in economic accounting as follows:

| Transaction Component | Accounting Treatment |
|---|---|
| Goods or materials given | Recorded as surplus disposition at declared barter value |
| Goods or materials received | Recorded as procurement at market replacement cost |
| Services given (processing capacity) | Recorded as revenue at market replacement cost of equivalent service |
| Services received | Recorded as operating cost reduction at market replacement cost |

**Net barter position:** If barter value received exceeds barter
value given in a transaction, the difference is positive economic
value for that cycle. If reversed, it is a cost. Both are valid
outcomes — the doctrine does not require barter to be favorable,
only that it be recorded.

### Barter and the FRT

Barter value counts toward FRT measurement when it represents
genuine value entering the Forge's resource pool. A barter
transaction that delivers consumables the Forge would otherwise
have purchased reduces operating cost and effectively frees
capital for reinvestment — it contributes to FRT health even
though no money changed hands.

Barter value does not count toward FRT when it represents
internal Forge network transfers. Shifting resources between
Forge instances is value preservation within the ecology —
not external value capture that funds regeneration.

### Barter Records

Minimum record for any barter transaction:
1. Date
2. What was given — quantity, condition, value basis
3. What was received — quantity, condition, replacement cost
4. Counterparty (person, organization, or Forge instance)
5. Net barter value (received minus given at declared valuations)
6. Whether the transaction contributed to FRT calculation and how

Records live in the operator's transaction log. They feed into
the cycle-close economic assessment (Section IV) and the FRT
logging in Gate_07_Utilization.md.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-07-06 | Governance | CT-007 (Canonical_Terms.md) identified an `EC-` prefix collision between this file and `Ethical_Constraints.md` | Rename not yet executed | ECN-001 through ECN-005 (all five of this file's own EC- entries, including Resolved ECN-003) renamed from `EC-` to `ECN-` to close the collision. CT-007's original write-up cited EC-008 as a sixth colliding ID — verified against this file directly: EC-008 does not exist here, that citation was in error. It also omitted EC-003 as a collision, likely because it is Resolved and drops out of Unknowns.md's active index — resolved status does not retire an ID from the shared namespace. | High — verified directly against source text | Update Unknowns.md's Economics table, CT-007 entry, and Canonical_Terms.md's ID-prefix registry to reflect `ECN-` |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### ECN-001 — Rare and critical mineral surplus disposition path undefined

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Medium             |
| Priority      | Major              |
| Type          | Operational        |
| Blocking      | No                 |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** Recovered rare and critical mineral fractions
(neodymium, cobalt, tantalum, indium, gallium) represent potentially
high-value surplus but have specialized market channels that differ
significantly from bulk scrap metal. Disposition path and channel
selection for these fractions is not defined.

**Why It Matters:** Disposing of critical mineral fractions through
bulk scrap channels destroys disproportionate value. The margin
difference between bulk scrap and refined critical mineral market
prices can be one to two orders of magnitude.

**Resolution Path:** Cross-reference `Challenges/Critical_Minerals.md`
and `Operations/Gate_05_Separation_Thermal.md` for recovery doctrine.
Define minimum acceptable disposition channel for critical mineral
fractions when first recovery cycle produces a measurable fraction.
Payment via Specification.

---

### ECN-002 — Operating cost baseline not yet established

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | High               |
| Priority      | Critical           |
| Type          | Architectural      |
| Blocking      | Yes — blocks TR-001 resolution |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** The operating cost model required for the v1
profitability baseline (Section V Component 1) does not yet exist.
It depends on `Operations/Energy.md` EV-001 (Forge demand baseline) which is
In Progress. Until EV-001 resolves, the cost side of the
profitability equation is a placeholder.

**Why It Matters:** A profitability baseline without a cost model
is not a baseline — it is an assumption. TR-001 cannot be formally
closed until the cost model exists.

**Resolution Path:** Dependent on `Operations/Energy.md` EV-001. When EV-001
resolves, establish cost baseline incorporating energy, consumables,
facility, and declared operator time rate. Update Section V
Component 1 from framework to figures. Cross-reference TR-001.

---

### ECN-003 — Barter valuation standard

| Field         | Value              |
|---------------|--------------------|
| Status        | Resolved           |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Operational        |
| Blocking      | No                 |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Resolution:** Barter doctrine defined in Section VI. Valuation
standard is market replacement cost of received goods at time of
transaction. Accounting treatment table defined. FRT contribution
logic defined. Records minimum content defined. Canonical ownership
of all barter doctrine assigned to this file.

---

### ECN-004 — Pricing and market rate data not maintained

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Operational        |
| Blocking      | No                 |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** Market rate data for scrap metal, recovered
materials, and fabricated components is real-time and
operator-maintained. This file does not attempt to capture it —
but no home for that data is currently defined.

**Why It Matters:** Market navigation without current price data
is intuition, not informed decision-making. The channel selection
and hold/sell decisions in Section III and IV depend implicitly
on the operator having current market information.

**Resolution Path:** At v0, operator-maintained local record is
sufficient — a simple log of transaction prices and channel
used per cycle. This feeds into the revenue model (ECN-002)
and informs future channel selection decisions. No repository
file needs to own price data — it is operational data, not doctrine.

---

### ECN-005 — Legal and tax compliance not assessed

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Medium             |
| Priority      | Major              |
| Type          | Governance         |
| Blocking      | No                 |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** Commercial sale of recovered materials, fabricated
components, and processing services may require business registration,
sales tax collection, income reporting, and scrap dealer licensing
depending on jurisdiction. None of these requirements have been
assessed.

**Why It Matters:** Operating commercially without required
registrations is a legal risk. Scrap dealer licensing in particular
has specific requirements in Arkansas and most US states that
apply even to small-scale operations.

**Resolution Path:** Human decision — jurisdiction-specific and
cannot be resolved by AI audit. Assign to human operator before
first commercial transaction. Cross-reference FA-003 in
`Architecture/Facilities.md` — both are pre-operation human compliance decisions.

---

### ECN-006 — Barter performance and default risk mechanics undefined

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Medium             |
| Priority      | Minor              |
| Type          | Governance         |
| Blocking      | No                 |
| Owner         | Admin/Economics.md |
| First Logged  | 2026-07-06         |
| Last Reviewed | 2026-07-06         |

**Description:** The Barter Doctrine (Section VI) defines valuation
(market replacement cost) and accounting treatment with internal
consistency, but implicitly assumes perfect counterparty performance.
No doctrine exists for asset quality divergence at exchange, an
unfulfilled counterparty commitment, or a valuation dispute between
the Forge and a barter partner.

**Why It Matters:** In decentralized, relationship-driven local
barter networks, these are predictable sources of friction, not edge
cases. Without a baseline posture, disputes have no defined
resolution path and asset-quality disagreements could silently
distort FRT accounting (Section VI, Barter and the FRT).

**Resolution Path:** Define a basic verification/recourse posture for
non-monetary exchanges — at minimum, a pre-exchange condition check
standard and a dispute logging requirement — prior to promoting this
doctrine beyond Exploration status.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-06 Exploration audit.*

---

### Adversarial Deferral (Gate 3)

Per `Admin/Verification_Gates.md`, Exploration-stage documents may
defer Adversarial Battery classes if the deferral is explicitly
declared with rationale, rather than left silent. This file defers:

- **Counterparty bad faith** — deferred; no barter transactions have
  occurred yet at v0 bootstrap scale to test this against (see ECN-006)
- **Localized market collapse** — deferred; disposition channels are
  not yet operational; premature to adversarially test a market
  navigation framework with no live channel
- **Hyper-inflationary liquidity distortion** — deferred; out of scope
  for a barter-tolerant, non-monetary-primary economic doctrine at v0

*Declared per Gemini (Skeptic/Auditor), 2026-07-06 Exploration audit.*

---

### Resolution Log

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **5** = ECN-001, ECN-002, ECN-004,
  ECN-005, ECN-006 (ECN-003 Resolved) — matches File State and `Unknowns.md`.
  (2) ECN-002 correctly **Blocking Yes** (blocks TR-001 resolution). (3) No
  ECN-* closed; no market claims advanced. Human-directed.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-05 | Fixed economic model with prescribed cost and revenue figures | No operational data exists at v0. A fixed model would be false precision — figures without basis. Framework-with-calibration-path adopted instead. | Reconsider at v1 when operational data exists |
| 2026-06-05 | Placing Economics.md in Admin/ alongside Trajectories.md | Economics.md provides market navigation doctrine used operationally — it is closer in character to Architecture/ foundational doctrine than Admin/ governance protocol. Placed in Admin/ per `Admin/Repository_Structure.md` Rule 1 because it sets standards other files reference, but the boundary is genuinely close. | Reconsider if operational use pattern suggests Architecture/ is more natural |
| 2026-06-05 | Defining specific pricing targets or margin floors | Pricing is market-dependent and time-dependent. A floor defined today is false doctrine tomorrow. Value ladder doctrine and channel selection framework provide the navigation logic without prescribing figures that would require continuous updating. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply.
Additional triggers specific to this file:*

- TR-001 remains open after ECN-002 (operating cost baseline) resolves
- Surplus is held beyond its declared review horizon without a
  logged reassessment
- Procurement occurs against unconfirmed need without a logged
  exception
- Barter transactions excluded from FRT and profitability
  calculations without a declared rationale
- ECN-005 (legal compliance) not assigned to a human owner before
  first commercial transaction
- Value ladder doctrine used to justify holding surplus indefinitely
  in pursuit of a higher ladder position
- FRT floor subtracted after profitability calculation rather than
  before — reinvestment is not optional surplus
