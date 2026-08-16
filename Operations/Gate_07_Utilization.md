# Gate_07_Utilization

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Utilization is where fabricated parts and recovered
> components meet operational reality. Silent failures
> — fatigue, dimensional drift, slow property loss —
> are not detectable by v0 logging discipline alone.
> Safety-critical and load-bearing parts carry higher
> silent failure risk. Inspect at shorter intervals
> than standard. Do not assume a part is safe because
> it has not visibly failed. Observable failure is a
> lagging indicator. See GU-004.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-19; revised 2026-06-08                                      |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Low risk reflects that Utilization itself performs
no irreversible actions and creates no physical
hazards. Risk is informational — a missed utilization
record is a missed learning opportunity, not a safety
event. The safety advisory above addresses the silent
failure risk that logging discipline cannot eliminate,
not a Utilization operation risk.*

---

## Scope Boundary

**This file DOES define:**
- After action review doctrine for all fabricated
  parts and recovered components in service
- Performance logging minimum content —
  what gets recorded about every part in service
- Failure mode capture — how failures are logged,
  classified, and routed back into the system
- Maintenance frequency tracking — how often a
  part requires intervention
- Feedback path to Gate_06_Fabrication.md —
  how utilization data improves fabrication
  decisions and precision ceiling tracking
- Feedback path to Architecture/Forge_Net.md —
  how utilization data contributes to network
  knowledge base
- Feedback path to Architecture/Forge_flow.md
  classification rules — how real-world performance
  improves upstream gate routing heuristics
- Retirement handoff doctrine — when a part's
  utilization record triggers re-entry into the
  gate flow at Gate_02_Triage
- Forge Regeneration Threshold (FRT) per-cycle logging —
  measurement and record of reinvestment fraction against
  declared FRT floor (doctrine in Admin/Trajectories.md)
- Part lifecycle termination conditions — when
  a part exits the system permanently

**This file DOES NOT define:**
- Retirement routing decisions
  (Operations/Gate_02_Triage.md)
- Fabrication methods or precision ceiling
  (Operations/Gate_06_Fabrication.md)
- Component taxonomy or graduation rules
  (Architecture/Components.md)
- Network contribution validation or trust
  weighting (Architecture/Forge_Net.md)
- Gate logic governing what gets fabricated
  (Architecture/Forge_flow.md)
- Energy accounting for operational use
  (Operations/Energy.md)
- Facility siting or operational safety beyond
  logging doctrine (`Architecture/Facilities.md`
  — FA-001)
- Formal quality certification or standards
  compliance (not yet assigned — GU-003)
- FRT floor declaration and v1 economic baseline
  (`Admin/Economics.md` — EC-002)

---

## File Purpose

Gate_07_Utilization is the after action review stage
of the Lazarus Forge. It is where fabricated parts
and recovered components meet operational reality —
where the system learns whether what it made actually
worked, how long it lasted, how it failed, and what
that means for the next fabrication cycle.

Utilization does not make decisions. It produces the
record that makes decisions better. A part in service
without a utilization record is an opportunity lost —
the forge cannot learn from what it cannot observe.
A part with a complete utilization record feeds
precision ceiling improvement, wire quality
correlation, gate routing refinement, and network
knowledge contribution simultaneously.

At v0, Utilization is a logging discipline. The
operator records what was deployed, how it performed,
when it required maintenance, and how it eventually
failed or was retired. No automation is assumed. No
sensor infrastructure is required. A written log
entry after each maintenance event or failure is
sufficient to close the fabrication feedback loop
and begin accumulating the institutional memory
the forge needs to improve.

The after action review framing is intentional.
Every part that fails teaches something. Every part
that outlasts its expected service life teaches
something different. The forge that captures both
learns faster than the forge that only records
successes. If this file disappeared, fabricated
parts would enter service and disappear — the
precision ceiling would stagnate, wire quality
problems would repeat, and the self-replication
loop would have no performance signal to close
against.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Parts in service remain within observable range — the forge has access to deployed parts for performance logging | Logging doctrine; v0 deployment assumed local | Medium | Parts deployed externally or to other forge instances without feedback path — observation continuity breaks |
| ASM-002 | Operators who deploy parts maintain logging responsibility — or a reliable handoff of observation duty exists between deployment and retirement | Logging discipline; human judgment primary | Low | Automated monitoring deployed — observation continuity no longer depends on operator handoff |
| ASM-003 | Failure modes are recognizable when they occur — operators can identify when a part has failed and characterize the failure type | Failure mode capture; obvious failure assumed observable | Low | Silent failure mode identified — fatigue, dimensional drift, or gradual property loss not externally observable without instrumentation |
| ASM-004 | The fabrication output tag from Gate_06_Fabrication.md survives service and remains traceable when a part is retired or fails | Feedback path to Gate_06; tag durability in service assumed | Low | Tag loss in service breaks traceability — re-identification protocol required |
| ASM-005 | Utilization data from individual forge instances generalizes enough at network scale to benefit other forges | Network contribution value; ecology learning model | Low | Cross-forge learning found to be context-dependent — locally adaptive knowledge must be classified separately per Forge_Net.md doctrine |
| ASM-006 | Retired parts re-entering the gate flow carry sufficient utilization history to improve Gate_02 routing decisions | Retirement handoff value; assumes complete record | Medium | Utilization records found too sparse or inconsistent to improve routing — logging discipline requires revision |
| ASM-007 | At v0 scale, manual logging is sustainable — the volume of parts in service does not exceed human logging capacity | Logging discipline; v0 throughput assumed low | Medium | Parts in service volume exceeds manual logging capacity — automated or assisted logging required |

*ASM-002, ASM-003, and ASM-004 are the most
operationally fragile — they all depend on human
continuity and tag durability that cannot be
guaranteed in real field conditions. ASM-003
explicitly acknowledges that silent failures are
beyond v0 detection capability. The forge learns
from observable failures at v0. Silent failures
require instrumentation that is a future capability,
not a current assumption. Gate_06 fabrication output
tag (ASM-004) is the traceability foundation —
tag survival in service determines whether failure
data traces back to its fabrication origin.*

---

## 1. Utilization Doctrine

Utilization is the after action review stage. Its
purpose is to observe, record, and feed back the
real-world performance of every part and component
the forge deploys.

**What Utilization is:**
- A logging discipline at v0 — no automation
  required, no sensor infrastructure assumed
- The closing mechanism of the fabrication
  feedback loop
- The primary source of precision ceiling
  improvement data
- The system's institutional memory of what
  worked, what failed, and why

**What Utilization is not:**
- A decision-making gate — retirement and
  routing decisions belong to Gate_02_Triage
- A quality certification system — formal
  standards compliance is out of scope at v0
- A real-time monitoring system — v0 logging
  is event-driven, not continuous

**Core doctrine:**
- Every part that enters service gets a
  utilization record opened at deployment
- Every maintenance event is logged
- Every failure is logged, classified, and
  routed as a feedback signal
- Every retirement triggers a handoff record
  to Gate_02_Triage
- A part that leaves service without a
  utilization record is a missed learning
  opportunity — not a system fault, but a
  gap the forge should work to close

**Observation continuity:**
The forge can only learn from what it can observe.
Parts deployed externally — to other forges, to
end users, to field use beyond the forge's reach —
have no guaranteed feedback path. At v0, prioritize
deploying parts within observable range first.
External deployment is valid but explicitly noted
as reduced-feedback in the utilization record.

---

## 2. Performance Logging

Performance logging is the primary output of
Gate_07_Utilization. Every part in service has
an active log. Every log feeds back to fabrication,
network, and gate routing.

**Utilization record minimum content:**

| Field | Content | Notes |
|---|---|---|
| Part identifier | From Gate_06 fabrication output tag | Links back to forge, operator, feedstock, method |
| Deployment date | When part entered service | |
| Deployment context | What application, what load class | Coarse is acceptable — "structural bracket," "bearing mount," "electrical connector" |
| Expected service life | Operator estimate at deployment | Compared against actual at retirement |
| Maintenance events | Date, type, outcome for each | Running log throughout service life |
| Failure event | Date, failure mode, severity | If applicable |
| Retirement date | When part left service | |
| Retirement reason | Planned end of life, failure, upgrade, lost | |
| Actual service life | Calculated from deployment to retirement | |
| Performance assessment | Met expectations, exceeded, fell short | Operator judgment |
| Feedback flags | Precision ceiling relevant, wire quality relevant, gate routing relevant | Tag what this record should feed back to |

**Logging cadence:**
- Open record at deployment
- Log each maintenance event within 24 hours
  of occurrence *(Placeholder — cadence validated
  operationally)*
- Close record at retirement with full summary
- No minimum logging interval between maintenance
  events — log what happens when it happens

**Observation gap doctrine:**
If a part cannot be observed for a period —
external deployment, inaccessible location,
operator change — log the gap explicitly.
A known gap is better than a false continuity.

---

## 2b. Forge Regeneration Threshold (FRT) Logging

The FRT is a system health metric defined in `Admin/Trajectories.md`.
Gate_07_Utilization owns the per-cycle measurement record. This section
defines what gets logged and when.

**What FRT logging captures:**

| Field | Content | Notes |
|---|---|---|
| Cycle identifier | Operating period this record covers | Month, audit cycle, or declared throughput batch — per operator declaration at commissioning |
| Total throughput value | Estimated value of material processed this cycle | Analogous or measured — label confidence level |
| Reinvestment amount | Value reinvested in Forge capability development this cycle | See Trajectories.md §What Counts as Reinvestment |
| Reinvestment fraction | Reinvestment ÷ throughput value | Compare against declared FRT floor |
| FRT floor (declared) | Operator-declared threshold for this Forge instance | Placeholder [2–5%] until calibrated — see TR-002 |
| FRT status | Above floor / Below floor / Placeholder (not yet calibrated) | |
| Below-floor note | If below floor: reason and recovery plan | Required if below floor — operator documented |
| Cumulative below-floor cycles | Running count of consecutive cycles below declared floor | Trigger review if count exceeds [N] — Placeholder |

**Logging cadence:** Once per declared FRT cycle — at cycle close,
before the next cycle opens.

**FRT floor calibration:** The FRT floor begins as Placeholder [2–5%].
After first operational cycle, the operator reviews actual reinvestment
patterns and declares a calibrated floor. Log the calibration event in
the Resolution Log with date and basis.

**Below-floor response:**
- 1 cycle below floor: log reason, document recovery plan
- [N] consecutive cycles below floor: flag as systemic decline indicator,
  escalate to human review, open GU-005 status update
- *(N is Placeholder — declared by operator at commissioning)*

**Relationship to v1 exit condition:**
FRT data feeds directly into TR-001 (v1 profitability baseline). A Forge
that has run sufficient cycles to calibrate its FRT floor has one of the
required inputs for the v1 economic model.

**v0 honest acknowledgment:** At v0, throughput value and reinvestment
amount may be rough estimates. Label all values with confidence level
(Measured / Analogous / Placeholder). An approximate FRT record is better
than none — the pattern across cycles matters more than precision in any
single cycle.

---

## 3. Failure Mode Capture

Failure records are the highest-value utilization
output. A part that fails teaches more than a part
that outlasts its expected service life without
observation.

**Failure classification at v0:**

| Class | Description | Example |
|---|---|---|
| Weld failure | Failure at or near a weld joint | Cracked bead, incomplete fusion propagation |
| Base material failure | Failure in parent material away from weld | Alloy brittleness, fatigue crack |
| Dimensional failure | Part no longer meets dimensional requirement | Wear beyond tolerance, thermal distortion |
| Surface failure | Coating, finish, or surface integrity loss | Corrosion, erosion, adhesion failure |
| Fit failure | Part no longer fits its application | Deformation, creep, mating surface wear |
| Unknown | Failure mode not identifiable | Log what was observed, not what is inferred |

**Failure record minimum content:**
- Part identifier and utilization record reference
- Failure date and service life at failure
- Failure class from table above
- Failure location — weld zone, base material,
  surface, dimensional, fit
- Failure description — what the operator observed
- Contributing factors if identifiable — overload,
  corrosion, fatigue, improper installation
- Downstream impact — did the failure propagate?
  Did it cause secondary damage?
- Feedback flags — what does this failure suggest
  about fabrication process, material quality,
  or gate routing?

**Failure doctrine:**
- All failures are logged regardless of severity —
  minor failures teach as much as catastrophic ones
- Failures are not blamed — they are classified
  and learned from
- A weld failure routes feedback to Gate_06
  Section 3 qualification criteria and GF-006
- A base material failure routes feedback to
  Gate_05_Separation_Thermal.md SC-002
  segregation effectiveness
- An unknown failure is logged as unknown —
  do not infer cause without evidence

---

## 4. Feedback Paths

Utilization data is only valuable if it reaches
the decisions it can improve. Four feedback paths
are active at v0.

**Path 1 — Gate_06_Fabrication.md:**
- Weld failure data informs qualification criteria
  and structural adequacy assessment (GF-006)
- Dimensional failure data informs precision
  ceiling characterization (GF-002)
- Wire quality correlation — weld failures on
  internally produced wire feed back to SC-002
  segregation effectiveness and SC-004 wire
  extrusion quality
- Fabrication phase tracking — which phase
  (A, B, or C) produced the part affects how
  failure data is interpreted

**Path 2 — Architecture/Forge_Net.md:**
- All utilization records are candidates for
  network contribution when connectivity allows
- Failure mode classifications with part
  identifiers contribute to shared knowledge base
- Cross-forge pattern detection — if multiple
  forges report the same failure mode on the
  same application, the network learns a
  systemic issue
- Locally adaptive knowledge — failure modes
  specific to a deployment environment
  (marine corrosion, high temperature, dusty
  conditions) are classified as locally adaptive
  per Forge_Net.md knowledge classification

**Path 3 — Architecture/Forge_flow.md:**
- Performance data improves classification
  heuristics — a component type that consistently
  underperforms in a specific application routes
  differently at Gate_02 in future cycles
- Expected vs. actual service life data improves
  the want/need policy — a part that lasts
  longer than expected changes the replacement
  urgency calculation

**Path 4 — Architecture/Components.md:**
- Parts that consistently exceed performance
  expectations may graduate to higher component
  classification
- Parts that consistently underperform may be
  downgraded in the component taxonomy
- Precision ceiling improvements documented
  in utilization records feed Components.md
  Metrology and Baseline Observability items

**Feedback contribution minimum:**
At the close of each utilization record, the
operator identifies which feedback paths are
relevant and tags the record accordingly.
A record tagged for Gate_06 feedback is
reviewed against current fabrication parameters
at the next fabrication planning cycle.

---

## 5. Retirement Handoff

When a part leaves service — by planned end of
life, failure, upgrade, or loss — its utilization
record closes and a retirement handoff initiates
re-entry into the gate flow.

**Retirement triggers:**

| Trigger | Next Step |
|---|---|
| Planned end of life — service life reached | Close record, assess for Gate_02 re-entry |
| Failure — part no longer functional | Close record, route to Gate_02 with failure classification |
| Upgrade — replaced by better part | Close record, assess retired part for Gate_02 re-entry |
| Loss — part cannot be located | Close record with loss notation, log tag number as missing |
| External retirement — part retired outside forge | Request retirement data if available, close record with gap notation |

**Retirement handoff record minimum content:**
- Part identifier and complete utilization record
- Retirement trigger and date
- Actual service life
- Performance summary — met, exceeded, or fell
  short of expectations
- Failure classification if applicable
- Fabrication output tag status — intact,
  damaged, or lost
- Recommended Gate_02 entry classification:
  - Functional — route to Gate A assessment
  - Repairable — route to Gate B assessment
  - Material only — route to Gate D / Reduction
  - Hazardous — hold for specialist assessment
  - Lost — no physical item to route

**Retirement handoff doctrine:**
- Gate_07 recommends the Gate_02 entry
  classification. Gate_02 makes the routing
  decision. Gate_07 does not override Gate_02.
- A part retired due to failure is not
  automatically routed to Reduction — it may
  have repairable or repurposable value.
  Gate_02 assessment determines this.
- The fabrication output tag travels with the
  retired part to Gate_02. If the tag is lost,
  log it. Gate_02 can still route the part —
  but the traceability chain is broken and
  the feedback value is reduced.

---

## 6. Integration Hooks

- `Architecture/Forge_flow.md` — governing flow;
  Utilization is the final stage; feedback to
  classification rules lives here
- `Operations/Gate_02_Triage.md` — receives
  retired parts with utilization records;
  makes routing decisions based on retirement
  handoff recommendations
- `Operations/Gate_06_Fabrication.md` — primary
  feedback recipient; weld quality, dimensional
  outcomes, and precision ceiling data all feed
  fabrication improvement
- `Operations/Gate_05_Separation_Thermal.md` —
  base material failures feed back to segregation
  effectiveness (SC-002) and wire quality (SC-004)
- `Architecture/Forge_Net.md` — utilization
  records contributed to network knowledge base;
  cross-forge failure pattern detection
- `Architecture/Components.md` — performance
  data feeds component graduation and taxonomy
  updates; precision ceiling improvements noted
- `Admin/Ship_of_Theseus.md` — utilization
  record closes the grain provenance chain
  for each part; full lifecycle documented
- `Unknowns.md` — GU-001 through GU-004
  indexed once logged

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-19 | Audit Review | Utilization conceived as terminal stage — parts enter service and system moves on | Without feedback loop, fabrication becomes industrial output not adaptive learning. Precision ceiling stagnates, wire quality problems repeat, self-replication loop has no performance signal | Utilization reframed as after action review — closing mechanism of fabrication feedback loop. Every part in service is an active data source | Analogous | No — after action review framing is correct |
| 2026-05-19 | Audit Review | Feedback assumed to happen naturally once utilization data exists | Data does not route itself. Four distinct feedback paths each require explicit operator tagging and routing | Explicit feedback path doctrine added to Section 4. Operator tags each record for relevant paths at close. Feedback contribution is deliberate, not automatic | Analogous | Yes — validate feedback routing against first operational cycle |
| 2026-05-19 | Audit Review | Failure records treated as negative outcomes to minimize | Minimizing failure records produces a forge that appears to succeed but does not learn. Silent failure accumulation is the worst outcome | Failure doctrine added — all failures logged regardless of severity, failures classified not blamed, unknown failures logged as unknown | Analogous | No — failure doctrine is permanent |
| 2026-05-19 | Audit Review | Retirement assumed to mean Reduction | Retired part may be functional in reduced application, repairable, or hazardous. Automatic Reduction wastes recovery value | Retirement handoff doctrine — Gate_07 recommends Gate_02 classification, Gate_02 makes routing decision | Analogous | No — retirement handoff doctrine is correct |
| 2026-05-19 | Audit Review | Silent failures not acknowledged as v0 limitation | Fatigue, dimensional drift, and slow property loss are not externally observable without instrumentation | ASM-003 explicitly acknowledges silent failure limitation. The forge learns what it can observe. Silent failure detection is future capability | Analogous | Yes — revisit when instrumentation capability develops |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | Whether Gate_07 should own fitness-for-purpose assessment or strictly after action review | Position A: Gate_07 assesses whether a part remains fit for continued service at each maintenance event — keeps assessment close to performance data. Position B: Fitness-for-purpose is a routing decision belonging at Gate_02_Triage — Gate_07 owns the record, Gate_02 owns the decision | Low | Open | Operations/Gate_07_Utilization.md |

*DS-001 reflects a genuine boundary tension between
observation and decision. Position B is the current
standing doctrine — Gate_07 produces records, Gate_02
makes routing decisions. This keeps the after action
review role clean and prevents Gate_07 from absorbing
triage responsibility. Revisit if operational experience
shows Gate_02 consistently lacks context needed to make
good retirement decisions. Trigger: three consecutive
retirement routing disagreements between Gate_07
recommendation and Gate_02 decision.*

---

## Auditor Notes & Unknowns

### GU-001 — Performance metric schema not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The performance metric schema —
field types, value formats, and comparable data
structures — is defined at minimum content level
but not at schema level. Cross-forge comparison
requires compatible record structures.

*Grok review 2026-08-15: Resolution Path adequate. FN-001 still Open (spec-complete per Unknowns.md v4.55 but not closed); GI-006 real. No closure.*

**Why It Matters:** Utilization data contributed
to Architecture/Forge_Net.md is only comparable
across forge instances if records share a compatible
schema. A record logging "held up well" cannot be
meaningfully compared with "load bearing cycles:
1,247." Cross-forge pattern detection depends on
schema compatibility.

**Resolution Path:**
- Define minimum field types and value formats
  for each utilization record field.
- Define performance assessment scale — even a
  coarse three-point scale produces more comparable
  data than free text.
- Cross-validate schema against Forge_Net.md
  contribution format requirements once FN-001
  validation criteria are defined.
- Payment via Specification — once schema is
  defined and validated against first operational
  cycle records, move to Section 2 as Analogous.
- Cross-reference: FN-001, GI-006.

---

### GU-002 — Retirement handoff protocol not
cross-validated with Gate_02_Triage

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The retirement handoff record
format and recommended classification scheme have
not been cross-validated against Gate_02_Triage
intake requirements.

*Grok review 2026-08-15: Resolution Path correct; Gate_02_Triage.md exists and DS-001 standing doctrine (Gate_07 records, Gate_02 decides) is consistent. No closure.*

**Why It Matters:** If the recommendation format
is incompatible with Gate_02's decision logic,
the utilization record becomes noise rather than
signal at the most important handoff in the
retirement cycle.

**Resolution Path:**
- Review Gate_02_Triage.md intake requirements.
- Cross-validate Section 5 retirement handoff
  record minimum content against Gate_02 needs.
- Define how Gate_02 receives and acts on a
  Gate_07 routing recommendation.
- Payment via Specification — once handoff format
  is cross-validated and tested through at least
  one operational retirement cycle, move to
  Section 5 as Analogous.
- Cross-reference: Operations/Gate_02_Triage.md,
  DS-001.

---

### GU-003 — Formal quality certification and
standards compliance unowned

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Formal quality certification —
pressure ratings, load certifications, electrical
safety standards — is explicitly out of scope for
v0 Utilization. No file currently owns this future
requirement.

*Grok review 2026-08-15: Resolution Path correctly discharges to Trajectories.md / Ship_of_Theseus.md. Minor priority appropriate. No closure.*

**Why It Matters:** As the forge ecology grows
and fabricated parts enter external trade or
critical applications, standards compliance
becomes operationally necessary. The absence
of an owner is not a current blocker but is
a trajectory gap.

**Resolution Path:**
- Discharge via Trajectory — route to
  Admin/Trajectories.md as v2+ consideration.
- When standards compliance becomes operationally
  necessary, create dedicated file or assign
  ownership to existing governance file.
- Cross-reference: Admin/Trajectories.md,
  Admin/Ship_of_Theseus.md.

---

### GU-004 — Silent failure detection capability
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Silent failures — fatigue crack
initiation, gradual dimensional drift, slow
conductivity loss, creep deformation — are not
externally observable without instrumentation.
At v0, the forge learns from observable failures
only.

*Grok review 2026-08-15: Resolution Path honest about v0 limits; GF-006 cross-ref real and still Open. Blocking=No correctly left (acknowledged limitation, not start-interlock). No closure.*

**Why It Matters:** Safety-critical and load-bearing
parts may exhibit silent failure progression before
visible failure occurs. This is an acknowledged
v0 limitation, not a gap to paper over — but it
needs a defined upgrade path.

**Resolution Path:**
- Acknowledge explicitly that v0 utilization
  logging captures observable failures only.
- Define upgrade path — strain gauges, temperature
  sensors, vibration monitoring on high-criticality
  parts as first instrumentation step.
- Safety-critical parts per GF-006 flagged for
  shorter inspection intervals.
- Payment via Specification — once instrumentation
  capability exists and silent failure detection
  is validated, move to Section 3 as Measured.
- Cross-reference: ASM-003, GF-006,
  Architecture/Components.md Baseline Observability.

---

---

### GU-005 — Forge Regeneration Threshold cycle definition and floor not yet declared

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Architectural / Governance                       |
| Blocking      | No                                               |
| Owner         | Operations/Gate_07_Utilization.md                |
| First Logged  | 2026-05-23                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** The FRT cycle definition (month / audit cycle / throughput
batch) and the calibrated FRT floor have not been declared by an operator.
The Placeholder floor [2–5%] applies until first operational cycle data exists.

*Grok review 2026-08-15: Resolution Path correct (operator declaration + post-cycle calibration). TR-002 cross-ref real and still Open in Unknowns.md. No closure.*

**Why It Matters:** Without a declared cycle definition, FRT logging cannot
begin. Without a calibrated floor, the systemic decline threshold is undefined.
Both are prerequisites for FRT records feeding meaningfully into the v1
economic model (TR-001).

**Resolution Path:** Discharge via Lessons Learned — operator declares cycle
definition at v0 commissioning. After first cycle, review actual reinvestment
patterns and calibrate floor. Log calibration event in Resolution Log with
date and basis. Cross-reference TR-002 (Trajectories.md) — same unknown,
different owning file. FRT floor calibration closes both.

---

### Resolution Log

- 2026-08-15: **Grok review round (Gate_07 sequence continuation).** All 5 GU unknowns (GU-001–005) reviewed. Last Reviewed bumped; review markers added. Cross-refs verified real (FN-001 still Open/spec-complete per Unknowns.md v4.55, GI-006, Gate_02_Triage.md, GF-006, TR-002, Trajectories.md, Ship_of_Theseus.md). DS-001 standing doctrine (Gate_07 records / Gate_02 decides) consistent. Zero closures, zero Blocking flips, zero Priority changes. Spec Gates left locked at 0/6. Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Findings only; Spec Gates
  left locked at 0/6. (1) Open Unknowns **5** = GU-001–005, matches local +
  `Unknowns.md`. (2) GU-004 (silent failure detection) correctly Blocking No —
  file explicitly frames as acknowledged v0 limitation with upgrade path,
  not a start-interlock. (3) No GU-* closed. Human-directed.

- 2026-05-23: GU-005 added — FRT cycle definition and floor declaration
  pending operator commissioning decision. FRT logging section (Section 2b)
  added to body. Scope Boundary updated. Open unknowns count updated to 5.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected
  from `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates.md`
  (PC-001). Scope Boundary updated — `Architecture/Facilities.md` reference
  added replacing `UNK-006` (PC-002); `Admin/Economics.md` added as FRT
  floor and v1 economic baseline owner (PC-003).

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-19 | Utilization as terminal stage — parts enter service and system moves on without structured feedback | Terminal stage produces parts but no learning. Precision ceiling stagnates, wire quality problems repeat, self-replication loop has no performance signal. The forge that does not debrief does not improve | No — after action review doctrine is permanent |
| 2026-05-19 | Gate_07 making retirement routing decisions | Retirement routing is a triage decision belonging at Gate_02_Triage where full gate logic applies. Gate_07 owns the record and recommendation — not the decision | Reconsider if operational experience shows Gate_02 consistently lacks context for retirement decisions — see DS-001 trigger condition |
| 2026-05-19 | Automatic Reduction routing for all retired parts | Retired part may be functional in reduced application, repairable, or hazardous. Automatic Reduction wastes recovery value and contradicts preserve-before-destruction doctrine | No — Gate_02 assessment of retired parts is permanent doctrine |
| 2026-05-19 | Continuous real-time monitoring as v0 utilization doctrine | Sensor infrastructure and automated monitoring require capability that does not exist at v0 bootstrap. Treating real-time monitoring as baseline makes utilization conditional on infrastructure that may never exist at small forge scale | Reconsider at v2+ when sensor capability and power budget justify continuous monitoring |
| 2026-05-19 | Failure records treated as negative outcomes to minimize | Minimizing failure records produces a forge that appears to succeed but does not learn. A culture that discourages failure logging produces silent failure accumulation | No — failure logging culture is permanent doctrine |
| 2026-05-19 | Utilization data assumed to route itself to relevant feedback targets | Data does not route itself. Four distinct feedback paths each require explicit operator tagging and routing. Without deliberate contribution, utilization data accumulates locally and never improves the system | No — explicit feedback path tagging is permanent doctrine |

---

## Drift Indicators

The following conditions trigger mandatory re-audit
of this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to
Gate_07_Utilization:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Parts enter service without utilization records opened at deployment | After action review doctrine requires records open at deployment — retroactive logging loses deployment context |
| Failure records not logged because failure was minor or embarrassing | Failure logging culture is permanent doctrine — all failures regardless of severity. Selective logging produces false confidence and silent failure accumulation |
| Gate_07 begins making retirement routing decisions without DS-001 resolution | Permanently abandoned path — Gate_07 recommends, Gate_02 decides. Boundary change requires explicit audit cycle and DS-001 resolution |
| Retired parts routed directly to Reduction without Gate_02 assessment | Permanently abandoned path — retired parts are not exhausted parts. Gate_02 assessment is mandatory before Reduction |
| Feedback path tagging abandoned in favor of unstructured free-text records | Explicit feedback path tagging is permanent doctrine — unstructured records do not route to the decisions they can improve |
| GU-001 schema remains undefined when cross-forge utilization comparison is attempted | Schema compatibility is prerequisite for cross-forge learning — comparison without compatible schemas produces misleading patterns |
| GU-002 retirement handoff format remains unvalidated at first operational retirement | Handoff format must be cross-validated with Gate_02 before first retirement — incompatible formats make utilization record noise at handoff |
| Safety-critical parts per GF-006 not flagged for shorter inspection intervals | Silent failure risk is higher for load-bearing parts — standard inspection interval is insufficient |
| Real-time monitoring introduced as replacement for event-driven logging before v2 instrumentation capability | Continuous monitoring is v2+ capability — introducing before power budget and sensor capability are validated creates infrastructure dependency |
| FRT logging omitted from cycle close | FRT records are a required output of each cycle close — omission breaks the system health measurement chain and TR-001 input path |
| Fabrication output tag from Gate_06 not verified at retirement handoff | Tag survival is the traceability chain — unverified tag status at retirement breaks feedback loop between service performance and fabrication origin |

### Canonical Drift Triggers

*All mandatory re-audit conditions from
Admin/File_Template.md Section 10 apply without
exception. Local triggers above are additive,
not substitutes.*
