# Gate_01_Intake

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Gate_01_Intake is the system's first and only opportunity
> to catch hazards before they enter the processing stream.
> Hazards missed here propagate through every downstream gate.
> Energetic materials — batteries, capacitors, compressed gas
> — must be identified and discharged before any further
> processing. Chemical and radiological hazards cannot be
> reliably detected by visual inspection alone. See GI-002
> and GI-003. When in doubt, hold. The cost of a missed
> hazard is always higher than the cost of a hold.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates.md                                      |
| Last Audit       | 2026-05-19                                                          |
| Auditor          | Claude — Skeptic/Auditor (actioning ChatGPT audit 2026-05-19)       |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Entry protocol for all items entering the Forge system
- Safety screening doctrine — hazards, energetics,
  biological, chemical, and radiological identification
- Physical document handling — scan on arrival,
  digital retention, network contribution
- Digital reference database lookup doctrine —
  primary automatic, secondary operator-assisted,
  tertiary unknown protocol
- Item tagging and provenance recording at entry
- Parts list generation doctrine for known assemblies
- Unknown item hold and inspect protocol before
  escalation to Human/AI Oversight Gate
- Fastener and small component recovery doctrine —
  preserve before reduction
- Integration with Architecture/Forge_Net.md reference
  database as primary lookup source
- Handoff to Classification and Triage
  (Operations/Gate_02_Triage.md)

**This file DOES NOT define:**
- Classification and triage workflow detail
  (Operations/Gate_02_Triage.md)
- Reference database content, schema, or maintenance
  (Architecture/Forge_Net.md — GI-001)
- Cognitive save state format or portability
  (Architecture/Forge_Net.md — FN-005)
- Network sync protocol for intake records
  (Architecture/Forge_Net.md)
- Detailed contamination handling beyond Intake
  screening (Architecture/Forge_flow.md Defined Terms,
  Operations/Gate_02_Triage.md)
- Energetic material disposal doctrine
  (not yet assigned — GI-002)
- Provenance tracking system specification
  (Admin/Ship_of_Theseus.md grain system)
- Air handling during intake screening
  (Operations/Air_Scrubber.md)
- Facility siting and intake area safety
  (Architecture/Facilities.md — FA-001)

---

## File Purpose

Gate_01_Intake is the entry point for all items entering
the Lazarus Forge system. Every component, assembly, and
material that the Forge will ever process passes through
here first. Intake does not make recovery decisions — it
makes the information available for recovery decisions to
be made correctly downstream.

The primary functions are safety screening, identification,
and tagging. Safety screening catches hazards before they
reach gate logic — a battery missed at Intake becomes a
Reduction incident; a lead-contaminated item missed at
Intake becomes an alloy contamination problem. Identification
connects the item to whatever is known about it — manuals,
parts lists, repair history — so that downstream gates have
the best available information rather than starting blind.
Tagging creates the provenance record that follows the item
through every subsequent gate.

At v0, Intake is primarily a human-judgment process
supported by digital lookup. The operator screens for
hazards, initiates the reference database query, scans
any physical documentation, generates a preliminary parts
list for known assemblies, and tags the item before
handoff to Classification and Triage. Automation is a
future capability, not a v0 assumption.

If this file disappeared, items would enter the Forge
system without safety screening, without identification,
and without provenance records. Hazards would propagate
downstream. Gate decisions would be made without context.
The grain system would have no starting point. The network
would receive no intake data to learn from.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | A human operator is present and capable of performing safety screening at every intake event | v0 human-judgment primary doctrine | Medium | Automated hazard detection validated and deployed — human presence becomes optional |
| ASM-002 | The reference database contains sufficient coverage of common appliances and assemblies to produce useful lookup results at v0 | Digital lookup primary path; database content not yet defined — see GI-001 | Low | Reference database content scope defined and validated against representative v0 feedstock samples |
| ASM-003 | Physical documents arriving with items contain recoverable information worth scanning — degradation is the exception, not the rule | Scan-on-arrival doctrine; document arrival is rare but signals owner care | Low | Scan yield data from first operational cycle shows documents are consistently too degraded to be useful |
| ASM-004 | Operators can identify most hazardous materials through visual inspection and basic testing at Intake | Safety screening doctrine; visual indicators exist for common hazards | Low | Intake safety incident occurs from a hazard that visual inspection cannot detect — detection capability must be augmented |
| ASM-005 | Items arrive in processable condition — not requiring special handling before entering the Intake protocol | Entry protocol — no pre-Intake triage exists | Medium | Item arrives in condition that cannot safely enter Intake without prior intervention — triggers pre-Intake protocol creation |
| ASM-006 | Provenance data recorded at Intake is compatible with the grain system format in Admin/Ship_of_Theseus.md | Tagging doctrine — grain system format not yet specified | Low | Grain system format defined — Intake tagging schema must be cross-validated and updated to match |
| ASM-007 | Fastener and small component recovery during Intake processing is net-positive at v0 scale — handling overhead is justified by component value | Junk drawer doctrine; inter-forge trade ecology | Low | Operational data shows recovery overhead exceeds component value at v0 scale — recovery threshold adjusted upward |

*Four Low confidence assumptions reflect genuine uncertainty
about detection capability, database coverage, document yield,
and grain system compatibility. ASM-004 is the most safety-
critical — visual inspection cannot detect lead, radiation,
or many chemical contaminants. Detection capability beyond
human visual inspection should be treated as a prerequisite
for unsupervised Intake operation. ASM-006 is load-bearing
for the Admin/Ship_of_Theseus.md grain system — Intake
tagging and grain format must be cross-validated before
either is treated as stable.*

---

## 1. Entry Protocol

All items entering the Lazarus Forge system pass through
Gate_01_Intake before any gate logic is applied. No item
proceeds to Classification and Triage without completing
Intake. No exceptions.

**Operator cognitive fatigue doctrine:**
Intake is cognitively expensive — ambiguity-heavy,
judgment-dependent, and interruption-heavy. A fatigued
operator is a systemic hazard propagation vector at
the system's first safety barrier.

- **Shift duration guidance** — sustained Intake
  operation beyond 2–3 hours without a break
  degrades judgment quality. *(Placeholder —
  validated against first operational cycle)*
- **Second-review triggers** — after three
  consecutive unknown or ambiguous items, a
  second operator reviews the next item before
  routing. Repeated ambiguity indicates either
  unusual feedstock or operator fatigue.
- **Mandatory escalation after repeated unknowns**
  — five consecutive unknown items without
  resolution triggers escalation to Human/AI
  Oversight Gate regardless of individual item
  status. Pattern recognition, not just item
  assessment.
- **Stop Intake authority** — any operator may
  suspend Intake operations without justification
  required. Queue accumulation never overrides
  operator judgment. Items in hold are safe.
  Items routed incorrectly are not.

**Intake backlog collapse doctrine:**
Intake can become a bottleneck under real salvage
conditions. Queue collapse is not theoretical — it
is an expected operational condition.

- **Maximum unresolved hold threshold** — when
  hold queue exceeds available physical storage,
  new intake is suspended until hold queue clears.
  *(Placeholder — threshold defined by physical
  facility capacity)*
- **Hold queue triage** — items in hold are
  reviewed in hazard priority order, not arrival
  order. Energetic and radiological holds are
  resolved before ambiguous-identity holds.
- **Physical quarantine overflow** — if quarantine
  space is saturated, intake of new items suspected
  to require quarantine is suspended. Accept only
  items that can be cleared or routed immediately.
- **Intake shutdown criteria** — intake stops when:
  hold queue is full, quarantine is saturated, or
  operator capacity is exhausted. Shutdown is not
  failure. Resuming with backlog is failure.

1. Visual inspection — gross condition, obvious hazards,
   visible contamination, structural integrity
2. Safety screening — identify energetic materials,
   chemical contamination indicators, biological matter,
   and any condition requiring special handling before
   processing. See Section 2.
3. Physical document handling — if documentation arrives
   with the item, scan immediately and retain digitally.
   See Section 3.
4. Reference database lookup — automatic query by model
   number, serial number, or visual identification.
   See Section 4.
5. Parts list generation — for known assemblies, generate
   preliminary parts list from database or operator
   knowledge. See Section 5.
6. Fastener and small component recovery — identify
   recoverable fasteners and small components before
   the item enters gate logic. See Section 6.
7. Item tagging — assign unique identifier, record
   provenance data, log intake condition. See Section 7.
8. Handoff — item enters Classification and Triage
   (Operations/Gate_02_Triage.md)

If any step cannot be completed safely, the item is
held at Intake until the blocking condition is resolved.
Intake is not a throughput gate — it is a safety gate.
Speed is never a success metric here.

**Degraded operation doctrine:**
Intake assumes digital infrastructure — scanning,
database lookup, digital record retention, network
sync — but must survive without it. Power loss,
network outage, or equipment failure must not stop
Intake from performing its core safety function.

| Condition | Degraded Response |
|---|---|
| Power loss during Intake | Switch to paper fallback intake log. Physical tag items manually. Sync digital records when power restores. |
| Database unavailable | Operator-assisted lookup only. Flag items as database-unverified. Do not skip safety screening. |
| Scanner unavailable | Log document presence in paper record. Scan when equipment restores. Physical document retained. |
| Network unavailable | Continue local logging. Queue network contributions. Do not delay Intake for sync. |
| Digital record system unavailable | Paper log is primary. Minimum record: item description, hazard status, tag number, date, operator. |

*Minimum survivable Intake operation: visual safety
screening, physical tagging, paper log entry. These
three functions must be executable without any
digital infrastructure. Everything else degrades
gracefully — safety screening does not.*

Cross-reference: `Operations/Energy.md`,
`Architecture/Forge_Net.md` sync doctrine.

---

## 2. Safety Screening

Safety screening is the most critical function of Intake.
Hazards missed here propagate through every downstream
gate. The cost of a missed hazard is always higher than
the cost of a hold.

**Hazard categories to screen at Intake:**

| Category | Examples | Visual Indicators | Detection Limit |
|---|---|---|---|
| Energetic | Lithium batteries, capacitors, compressed gas vessels | Swelling, leakage, pressure relief markings | Visual inspection — moderate reliability |
| Chemical | Lead, cadmium, mercury, solvents, flux residues | Corrosion patterns, coating discoloration, warning labels | Visual inspection — low reliability. See GI-003 |
| Biological/organic | Oils, fluids, biological matter | Staining, odor, visible growth | Visual inspection — moderate reliability |
| Radiological | Radiation-emitting materials | Warning markings only — no visual indicator without markings | Visual inspection — very low reliability. See GI-003 |
| Unknown | Any item that cannot be screened with confidence | No obvious indicators | Route to hold immediately |
| Digital/firmware | Malware-bearing storage devices, compromised firmware, infected embedded systems, hostile control boards | No visual indicator — presence of storage media, network interfaces, or programmable controllers is the trigger | Isolate from all networked systems before any connection attempt — see GI-007 |

**Screening doctrine:**
- Screen before any disassembly begins — disassembly
  can release contained hazards
- When in doubt, hold — do not route ambiguous items
  forward under throughput pressure
- Energetic materials must be discharged or safely
  isolated before any further processing — see GI-002
- Chemical and radiological hazards beyond visual
  detection require augmented detection capability —
  see GI-003
- **Digital hazard screening** — any item containing
  storage media, network interfaces, or programmable
  controllers must be treated as potentially hostile
  before any connection to forge systems. Do not
  plug in, power up connected to forge network, or
  allow firmware execution without isolation protocol.
  Cross-reference: GI-007, `Operations/Electronics.md`,
  `Architecture/Forge_Net.md`
- New hazard categories not listed above route to
  Human/AI Oversight Gate and trigger a new category
  entry per `Architecture/Forge_flow.md` contamination
  doctrine

**Operator safety:**
Physical separation from unknown items during initial
screening. Do not handle items showing energetic
distress signs — swollen batteries, leaking vessels,
deformed pressure containers. Log and hold for
specialist assessment.
Cross-reference: `Architecture/Facilities.md` FA-001 — siting and clearance
requirements not yet confirmed.

---

## 3. Physical Document Handling

Physical documentation arriving with an item is rare
and signals something about the previous owner's care
level — worth noting in the intake record as a quality
signal.

**Handling doctrine:**
- Scan all physical documents on arrival regardless
  of apparent condition — partial information is
  better than no information
- Retain digitally — paper documents degrade,
  digital copies persist
- Contribute scan to `Architecture/Forge_Net.md`
  reference database when network connectivity
  allows — one forge's manual becomes every
  forge's resource
- Note document type and condition in intake record:
  complete manual, partial manual, warranty card,
  repair receipt, or other
- Do not discard physical documents after scanning —
  retain until item completes gate routing, then
  archive or discard per local policy

**Document quality signal:**
An item arriving with complete, well-maintained
documentation warrants a note in the intake record.
It suggests the previous owner valued the item —
which may correlate with better maintenance history
and higher functional recovery probability.

---

## 4. Reference Database Lookup

The reference database is the primary knowledge source
for item identification at Intake. It connects items
to known assembly structures, parts lists, repair
guides, and hazard profiles.

**Lookup sequence:**
1. Automatic query — model number or serial number
   if visible. Primary path.
2. Visual identification query — description or
   image-based lookup if no model number available.
   Secondary path.
3. Operator-assisted lookup — operator identifies
   item from experience or external search.
   Tertiary path.
4. Unknown — no identification possible. Item
   proceeds with incomplete intake record.
   See Section 8.

**Database dependency:**
The reference database lives in
`Architecture/Forge_Net.md` local cache, synced from
the network when connectivity allows. At v0 bootstrap,
the local cache may be sparse — common appliances
and tools prioritized first. See GI-001.

**Lookup outcome recording:**
- Positive identification: record model, manufacturer,
  known assembly structure, hazard profile if any
- Partial identification: record what is known,
  flag gaps explicitly
- No identification: flag as unknown, proceed to
  Section 8

*Lookup is not a gate — a failed lookup does not
stop Intake. It produces an incomplete record that
downstream gates must account for.*

---

## 5. Parts List Generation

For identified assemblies, a preliminary parts list
documents the recoverable components before disassembly
begins. This is Gate A intelligence arriving before
Gate A — knowing what's inside before opening the item.

**Parts list doctrine at v0:**
- Human judgment primary — operator generates list
  from database lookup or direct knowledge
- Parts list is preliminary — actual disassembly
  may reveal differences from expected structure
- Record expected vs. actual at disassembly —
  discrepancies feed back to the reference database
- Fasteners, small components, and hardware are
  explicitly included — not ignored as bulk material.
  See Section 6.

**Parts list scope constraint:**
The parts list is a helpful approximation, not
structural certainty. Explicit limits at v0:
- No guarantee of completeness — hidden assemblies,
  non-standard modifications, and undocumented
  variants are not captured
- No inferred hidden assemblies — only what is
  known from documentation or direct operator
  knowledge is listed
- No automation assumption — the list is generated
  by human judgment, not machine vision or
  predictive modeling
- No dependency on database completeness — if the
  database has no entry, the parts list is blank
  until the operator fills it from knowledge
- "Gate A intelligence arriving before Gate A"
  means helpful context, not predictive certainty.
  Gate A makes the actual routing decision.

**Parts list minimum content:**
- Item identifier (linked to intake tag)
- Assembly model and manufacturer if known
- Expected major components with condition notes
- Known hazardous sub-components flagged
- Estimated recovery class for each component:
  Class A (functional), Class B (degraded),
  Class C (material only)

*Parts list is an estimate, not a commitment.
Gate logic makes the actual routing decisions.*

---

## 6. Fastener and Small Component Recovery

Fasteners and small components are the most commonly
discarded items in real-world scrapping and among the
most practically useful. A screw in the Component
Library is available for use. A screw through the
shredder is particulate.

**Recovery doctrine at v0:**
- Identify recoverable fasteners and small hardware
  during Intake visual inspection and parts list
  generation
- Route to Component Library as Class A salvage
  by default — do not route to bulk Reduction
  without explicit reason
- Common fastener types worth recovering: machine
  screws, bolts, nuts, washers, standoffs, clips,
  and springs in good condition
- Condition threshold: functional geometry, no
  significant corrosion, thread intact. Damaged
  fasteners route to Class C material.
- Handling overhead vs. recovery value: at v0 scale,
  human judgment governs whether recovery overhead
  is justified. See ASM-007. A formal fastener
  registry is a v1+ consideration when volume
  justifies it.

*The junk drawer instinct is correct. Systematize
it when scale demands — not before.*

---

## 7. Item Tagging and Provenance

Every item that completes Intake receives a unique
identifier and a provenance record. This is the
starting point for the grain system in
`Admin/Ship_of_Theseus.md`.

**Minimum intake record at v0:**
- Unique item identifier (sequential or hash-based)
- Date and location of intake
- Item description — what it is, condition on arrival
- Identification status — known, partial, unknown
- Hazard screening outcome — clear, hold, or flagged
- Physical document status — none, scanned, attached
- Parts list reference — linked if generated
- Operator identifier — who performed Intake
- Intake notes — anything unusual worth recording

**Tagging method at v0:**
- Physical tag attached to item (durable label,
  cable tie tag, or equivalent)
- Digital record created in local system
- Record contributed to `Architecture/Forge_Net.md`
  when connectivity allows

**Grain system compatibility:**
Intake tagging format must be cross-validated against
`Admin/Ship_of_Theseus.md` grain system requirements
before either is treated as stable. See ASM-006,
GI-004.

**Chain of custody integrity:**
The tag is the physical link between the item and
its record. Tag loss or detachment breaks the
provenance chain at its first link. Provisional
doctrine pending GI-006 resolution:
- Tags must be physically durable and attached
  securely — not adhesive labels on oily or wet
  surfaces, not paper tags on items that will
  be moved repeatedly
- If a tag is lost before the item completes
  gate routing: stop, re-identify the item
  against intake records, re-tag before routing
- Duplicate identifier prevention — tag numbers
  are sequential and never reused, even after
  an item is fully processed
- Record/item reconciliation — at handoff to
  `Operations/Gate_02_Triage.md`, the physical tag is verified
  against the digital record before the item
  proceeds. Mismatches are held, not routed.
- Cross-reference: GI-006, `Admin/Ship_of_Theseus.md`

---

## 8. Unknown Item Protocol

An item that cannot be identified through database
lookup or operator knowledge is not routed forward
blind. Unknown items receive a hold and inspect
protocol before escalating to the Human/AI Oversight
Gate.

**Unknown item sequence:**
1. Complete safety screening regardless of
   identification status — unknown items are not
   exempt from hazard screening
2. Record as unknown in intake record — explicit
   flag, not an omission
3. Hold and inspect — operator performs closer
   physical examination. Does any marking, label,
   or physical feature enable partial identification?
4. Extended lookup — operator attempts identification
   through external resources if connectivity allows
5. If partial identification achieved: proceed with
   incomplete record, flag gaps explicitly
6. If no identification after hold and inspect:
   escalate to Human/AI Oversight Gate with full
   inspection notes
7. Do not route unknown items to gate logic without
   at least partial identification — gate decisions
   made without context risk misrouting hazardous
   or high-value items

**Intake-to-Triage contamination authority boundary:**
Intake and Gate_02_Triage share responsibility for
contaminated items but with distinct roles:
- **Intake owns** initial containment and hazard
  flagging — the item is held, labeled, and
  physically isolated here
- **Gate_02_Triage owns** routing classification —
  once Intake has established the hazard state,
  Triage determines the downstream path
- **Human/AI Oversight Gate owns** unresolved
  hazard arbitration — contaminated-but-valuable
  items requiring partial disassembly or deferred
  classification escalate here, not to Triage

**Oversight Gate escalation capacity:**
The unknown item protocol assumes Oversight is
available when needed. No doctrine exists for
Oversight saturation. Provisional guidance:
- Items awaiting Oversight review remain in hold —
  they do not route forward while waiting
- If Oversight queue exceeds defined threshold,
  new escalations are logged and queued; priority
  order is safety-critical first, then age of hold
  *(Placeholder — threshold defined operationally)*
- Items in safe indefinite hold do not expire —
  a correctly held item is always better than a
  prematurely routed one
- Cross-reference: `Architecture/Forge_flow.md`
  Human/AI Oversight Gate doctrine

**Unknown item as network contribution:**
An unidentified item that is eventually identified
through human expertise or extended research is a
high-value network contribution. Record the
identification path and contribute to the reference
database — the next forge to encounter the same
item benefits from this forge's work.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Intake conceived as simple safety screen and tag | Scope expanded significantly during drafting — document lookup, parts list generation, fastener recovery, unknown item protocol, and network contribution all surfaced as load-bearing functions | Intake is not a trivial entry gate. It is the system's first and only opportunity to catch hazards, establish provenance, and seed the network with knowledge. Underspecifying Intake underspecifies everything downstream | Analogous | No — expanded scope is correct |
| 2026-05-15 | Audit Review | Visual inspection assumed sufficient for hazard detection | Chemical and radiological hazards have no reliable visual indicators. Lead, radiation, and many solvents are invisible to unaided inspection | Visual inspection is necessary but not sufficient for complete hazard screening at v0. Augmented detection capability is required before unsupervised Intake operation. See GI-003 | Analogous | Yes — validate detection capability before first unsupervised run |
| 2026-05-15 | Audit Review | Fasteners treated as bulk material defaulting to Reduction | Fasteners are among the most practically useful recoverable items and are routinely lost to shredding in conventional scrapping | Fastener and small component recovery doctrine added — Class A salvage by default, not bulk Reduction. Formal registry deferred to v1+ when volume justifies overhead. The junk drawer instinct is correct | Analogous | Yes — validate recovery overhead vs. value at first operational scale |
| 2026-05-19 | Audit Review | Digital hazards not included in safety screening categories | Items with storage media, network interfaces, or programmable controllers can carry malware or hostile firmware invisible to physical inspection. Given Forge_Net.md integration, digital contamination propagates faster and further than physical contamination | Digital contamination added as explicit hazard category in Section 2. Isolation before any forge system connection required. GI-007 logged | Analogous | Yes — validate isolation protocol before first electronics intake |
| 2026-05-19 | Audit Review | Intake assumed to have continuous digital infrastructure availability | Power loss, network outage, and equipment failure are real operational conditions. Safety screening must survive without digital infrastructure | Degraded operation doctrine added to Section 1. Minimum survivable Intake: visual screening, physical tagging, paper log. Everything else degrades gracefully | Analogous | No — degraded doctrine is correct |
| 2026-05-19 | Audit Review | Operator cognitive fatigue not acknowledged as a hazard | Intake is the first safety barrier and is cognitively expensive. Fatigued operator is a hazard propagation vector, not just a performance issue | Cognitive fatigue doctrine added — shift guidance, second-review triggers, stop-intake authority. Backlog collapse doctrine added | Analogous | Yes — validate thresholds against first operational cycle |
| 2026-05-19 | Audit Review | Parts list generation framed as Gate A intelligence without explicit scope limits | "Intelligence arriving before Gate A" risks implying predictive modeling capability that does not exist at v0 | Parts list scope constraint added — no hidden assemblies, no automation, no database dependency, helpful approximation not structural certainty | Analogous | No — scope constraint is permanent |
| 2026-05-19 | Audit Review | Chain of custody between physical item and digital record not formally addressed | Tag loss breaks the provenance chain at its first link. The grain system depends on an unbroken chain from Intake forward | Provisional chain-of-custody doctrine added to Section 7. GI-006 logged. Record/item reconciliation at Gate_02 handoff added | Analogous | Yes — validate against grain system requirements when GI-004 and GI-006 resolve |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts currently active. Several
design tensions exist (automation vs. human judgment
at v0, fastener recovery overhead vs. value at small
scale, document scan yield vs. handling cost) but all
are deferred pending first operational data. Tracked
as unknowns in sidecar, not disputes. Revisit after
first operational Intake cycle produces yield data.*

---

## Auditor Notes & Unknowns

### GI-001 — Reference database content and coverage not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** The reference database that
Gate_01_Intake queries for item identification has
no defined content scope, schema, or initial
population strategy.

**Why It Matters:** A sparse or poorly scoped database
makes the primary lookup path unreliable from first
operation. Operators fall back to tertiary paths —
external search or judgment — which are slower, less
consistent, and produce no network contribution.
Database coverage directly determines Intake
throughput and identification quality.

**Resolution Path:**
- Define minimum content scope for v0 — common
  household appliances, power tools, consumer
  electronics, and mechanical assemblies most
  likely to appear in salvage feedstock.
- Define schema — minimum fields: model identifier,
  manufacturer, assembly structure, known hazard
  profile, parts list reference.
- Define initial population strategy — manual entry,
  web scraping of public repair databases (iFixit
  and equivalents), or manufacturer documentation.
- Cross-reference `Architecture/Forge_Net.md` —
  database lives in local cache, synced from
  network. Content strategy must align with
  network contribution doctrine.
- Payment via Specification — once content scope,
  schema, and population strategy are defined,
  move to Section 4 as Placeholder promoting
  toward Analogous after first operational cycle.

**Grok review 2026-08-14:** Path adequate. Scope / schema / population strategy / Forge_Net alignment are the right four legs; Payment-via-Spec promotion rule is correct. No parallel doctrine invented. **Grok approved (doctrinal completeness of path).** Remains Open — content still needs to be written and first operational cycle run.

---

### GI-002 — Energetic material discharge doctrine not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | Yes — hard prerequisite before first operational Intake run |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Batteries, capacitors, compressed gas
vessels, and other energetic materials identified at
Intake must be discharged or safely isolated before
any further processing. How this discharge happens
safely is not yet defined.

**Why It Matters:** Energetic materials in an
undischarged state are the most acute hazard in the
Forge processing stream. A lithium battery entering
Reduction is a fire and explosion risk. A compressed
gas vessel entering a shredder is a projectile risk.
Discharge doctrine is a safety prerequisite for
Intake operation, not a refinement.

**Resolution Path:**
- Define discharge doctrine by energetic category:
  - Lithium batteries — deep discharge procedure,
    safe storage protocol, disposal or recycling
    path for non-recoverable cells
  - Other batteries — category-appropriate discharge,
    electrolyte handling if applicable
  - Capacitors — safe discharge procedure, voltage
    verification before handling
  - Compressed gas — controlled release or isolation
    protocol, vessel marking after discharge
- Define safe isolation for energetics that cannot
  be immediately discharged — storage location,
  container type, maximum hold duration
- Define operator safety requirements — PPE,
  distance, tooling
- Must be resolved before first operational Intake
  run — hard prerequisite, not a deferral
- Cross-reference: `Architecture/Facilities.md` FA-001 siting requirements,
  `Operations/Air_Scrubber.md` for off-gassing
- Payment via Specification — once discharge
  doctrine is defined and tested, move to
  Section 2 as Analogous.

**Grok review 2026-08-14:** Path adequate and correctly sequenced by energetic category (Li-ion, other batteries, capacitors, compressed gas) plus isolation, PPE, and hard-prerequisite language. Blocking Yes is correct. **Grok approved (path adequate).** Remains Open — written discharge doctrine + validation still required before first operational Intake run; do not close on path alone.

**Spec-depth pass, 2026-08-15 (digital-only — no equipment exists yet):** The prior path was an outline of what discharge doctrine needed to cover; this pass writes the doctrine itself, at Analogous confidence — standard industry battery/electrical safety practice, not anything requiring Forge-specific physical testing to specify. What stays genuinely open is noted per category. Checked cross-references first: `Architecture/Facilities.md` FA-001 confirmed as the siting doctrine (still Open, so isolation-storage siting itself stays deferred to it); `Operations/Air_Scrubber.md` currently only specifies Cl₂-specific off-gas handling, not general battery thermal-runaway off-gassing (HF, VOCs) — that gap is real and flagged below, not papered over. `Gate_04_Separation_Mechanical.md`'s existing lockout-before-access pattern (MG-007) is reused as the operator-safety precedent rather than inventing a separate one.

*Lithium-chemistry cells:* Triage before any discharge attempt — physically damaged, swollen, punctured, or hot-to-touch cells are **not** manually discharged; thermal runaway risk from mechanical intervention exceeds the risk of controlled isolation storage. These route directly to isolated storage (below), no discharge attempted. Undamaged cells: deep-discharge through a resistive load (not a direct short — arc and heat risk), monitored, inside a fire-rated container (steel, sand-lined or vermiculite-lined) with a vent path, never inside an enclosed operator space. Target discharge voltage is chemistry-dependent and genuinely needs verification per cell type at first operational run — flagged Placeholder, not asserted as a universal number. Cells that will not accept discharge (internal fault) are non-recoverable and route to isolated storage, not further intervention.

*Other battery chemistries:* Lead-acid — acid-resistant PPE (gloves, eye protection) mandatory before handling; discharge via resistive load; any electrolyte leakage is neutralized and contained per standard acid-handling practice before the cell is moved. Alkaline/NiMH/NiCd — lower acute hazard; resistive-load discharge without electrolyte-specific PPE, but visually inspected for casing corrosion or leakage first, since NiCd carries its own toxicity concern at breach.

*Capacitors:* Assume charged until measured — voltage verification with a meter is mandatory before any physical contact with terminals, regardless of how long the component has been de-powered. Discharge through a bleeder resistor sized to the capacitor's rated voltage/capacitance, not a direct short (arc and projectile risk on larger units). Large electrolytic or high-voltage capacitors (e.g., from CRTs or industrial drive equipment) are treated as a distinct highest-risk sub-case requiring resistor sizing appropriate to their higher stored energy — a single small-capacitor procedure does not generalize to these without checking rated values first.

*Compressed gas vessels:* Identify contents where labeling or valve type allows; where contents cannot be identified, treat as hazardous by default — fail closed, consistent with the file's existing confidence-labeling discipline elsewhere. Controlled release only in a ventilated area; if contents are suspected hazardous (not just inert), release routes through `Operations/Air_Scrubber.md`'s dedicated auxiliary release point (AS-005, registered 2026-08-15) — a physically separate intake from the main Stage A→E process pipeline, so an unpredictable unknown-content release doesn't enter Stage D's calibrated main water loop. AS-005's own capture-media sizing still depends on this file's largest plausible vessel-volume assumption, which is itself not yet specified — flagged as a residual gap, not silently closed by AS-005's registration. Vessels that cannot be safely released are isolated valve-protected, away from ignition sources and thermal sources, and tagged with contents-unknown status.

*Isolation storage (shared across categories):* A dedicated isolation area, physically separated from active processing stations, houses any energetic material pending discharge or awaiting non-recoverable disposition. Container type varies by category as specified above; siting distance and structural requirements for this area are FA-001's job, not invented here — this doctrine defines what goes in isolation and how, FA-001 defines where.

**Status after this pass:** discharge procedures now exist by category at Analogous confidence, closing the "define discharge doctrine" half of the Resolution Path. What remains genuinely open: (1) chemistry-specific discharge voltage targets for lithium cells — needs first-operational-run verification per cell type; (2) the general-gas Air_Scrubber.md intake gap surfaced above, tracked there rather than assumed away; (3) isolation-area siting specifics, correctly deferred to FA-001. GI-002 remains **Open**, Blocking Yes unchanged — doctrine is written, but "written and tested" (the file's own stated bar for promotion to Section 2) still requires the first operational run this file cannot produce without equipment.

---

### GI-003 — Augmented hazard detection capability not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-15                                       |

**Description:** Visual inspection cannot reliably
detect chemical contamination (lead, cadmium, mercury,
solvents) or radiological hazards. Augmented detection
capability is required for complete hazard screening
but specific tools, methods, and protocols are not
yet defined.

**Why It Matters:** Lead is present in consumer
products without visible indicators. Radiation sources
have no visual signature without markings. An Intake
process relying solely on visual inspection has a
known blind spot for the most serious contamination
categories — alloy contamination, equipment fouling,
and operator health risk downstream.

**Candidate augmentation options for v0:**
- Lead test swabs — low cost, simple, reliable for
  surface lead detection. Available commercially.
  Suitable for v0 bootstrap. *(Analogous)*
- Geiger counter — detects radiation. Low cost for
  basic models, no consumables, simple operation.
  Should be standard Intake equipment. *(Analogous)*
- Chemical test strips — basic pH, solvent, and
  contaminant screening. Low cost, limited scope.
  *(Analogous)*
- XRF analyzer — broad spectrum elemental analysis,
  non-destructive. High cost, high capability.
  Purchase-what-cannot-be-produced doctrine applies
  if budget allows. *(Analogous)*

**Resolution Path:**
- Select minimum augmentation kit for v0 bootstrap
  — geiger counter and lead test swabs address
  the two most critical blind spots at lowest cost.
- Define testing protocol — when to test, how to
  interpret results, what threshold triggers a hold.
- Augmented detection is a prerequisite for
  unsupervised Intake operation — human oversight
  partially compensates until detection is in place.
- Payment via Specification — once augmentation kit
  is selected, protocols defined, and first
  operational cycle validates detection reliability,
  move to Section 2 as Analogous.
- Cross-reference: ASM-004,
  `Operations/Air_Scrubber.md` for chemical hazard
  handling.

**Grok review 2026-08-14:** Path adequate. Candidate kit (Geiger + lead swabs as v0 minimum) is concrete and correctly scoped; unsupervised-operation gate is the right control. Blocking No is acceptable while human oversight compensates, but the drift indicator for unsupervised operation is correctly severe. **Grok approved (path adequate).** Remains Open — kit selection + protocol still required.

**Note, 2026-08-15 (Claude):** GI-003's tools (Geiger counter, lead swabs, chemical test strips) are the augmented detection layer feeding the same triage pipeline `Operations/Plastics.md` PL-001's Beilstein test and `Challenges/Waste.md` WA-002's identification protocol already share — a supporting dependency, not a parallel detection path. Positive results from any of the three feed the same downstream destination: `Operations/Gate_02_Triage.md` TS-002's Contaminated bin non-decontaminable state. This does not close GI-003 — kit selection and protocol definition remain open — but it keeps the four detection-and-routing unknowns (GI-003, PL-001, WA-002, TS-002) pointed at one converged pipeline instead of drifting toward separately-imagined ones.

---

### GI-004 — Intake tagging schema not cross-validated against grain system

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** The intake tagging schema has not
been cross-validated against the grain system
requirements in `Admin/Ship_of_Theseus.md`. Incompatible
schemas break the provenance chain at its first link.

**Why It Matters:** Intake tagging is the starting
point for the grain system. A schema mismatch means
every provenance record created at Intake requires
manual conversion. The legal and philosophical value
of the grain system depends on an unbroken provenance
chain — a schema mismatch breaks that chain at the
first link.

**Resolution Path:**
- Review `Admin/Ship_of_Theseus.md` grain system
  requirements — what fields does a grain record
  require at minimum?
- Cross-validate against Section 7 minimum intake
  record — do the fields align?
- If misaligned: extend the intake record to include
  grain system required fields — do not reduce grain
  system requirements.
- Intake schema should be a superset of grain system
  requirements.
- Payment via Specification — once schemas are
  cross-validated and aligned, move to Section 7
  as Analogous.
- Cross-reference: ASM-006,
  `Admin/Ship_of_Theseus.md`.

**Grok review 2026-08-14:** Path adequate. Correctly requires Intake schema to be a superset of grain requirements rather than the reverse; joint resolution with GI-006 is noted. **Grok approved (path adequate).** Remains Open — actual cross-check against Ship_of_Theseus grain fields still required.

---

### GI-005 — Pre-Intake protocol for items requiring special handling not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** No pre-Intake protocol exists for
items that are too damaged, contaminated, or dangerous
to enter standard Intake without prior intervention.

**Why It Matters:** Some items will arrive in
conditions that standard Intake cannot safely handle
— a leaking chemical container, a severely damaged
lithium battery showing thermal distress, an unlabeled
pressure vessel. Without a pre-Intake protocol,
operators face these situations without doctrine.
Improvised responses to hazardous conditions are a
primary source of workplace incidents.

**Resolution Path:**
- Define pre-Intake categories:
  - Active energetic distress (swollen, leaking,
    hot battery or capacitor)
  - Active chemical leak or visible fuming
  - Biological contamination beyond surface soiling
  - Structural instability creating collapse or
    falling hazard
  - Unidentifiable condition with no safe handling
    path
- Define pre-Intake response for each category —
  isolation, containment, specialist assessment,
  or controlled disposal.
- Define invocation authority — any operator should
  be able to call a hold without management approval.
- Cross-reference: GI-002 energetic discharge
  doctrine, `Architecture/Facilities.md` FA-001 siting requirements,
  `Operations/Air_Scrubber.md`.
- Payment via Specification — once pre-Intake
  categories and responses are defined and operator
  training covers them, move to Section 1 entry
  protocol as Analogous.

**Grok review 2026-08-14:** Path adequate. Category list (energetic distress, chemical leak, biological, structural instability, unidentifiable) + any-operator invocation authority are the right controls. **Grok approved (path adequate).** Remains Open — categories and responses still need to be written.

---

### GI-006 — Intake chain-of-custody integrity not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Governance                           |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** Intake establishes provenance,
hazard status, and grain initiation for every item.
No formal chain-of-custody doctrine exists to ensure
the physical item and its digital record stay linked
through the entire gate flow.

**Why It Matters:** Without chain integrity, provenance
can be corrupted, hazard-cleared items can be swapped
for unchecked ones, and records can drift from the
physical objects they describe. The grain system in
`Admin/Ship_of_Theseus.md` depends on an unbroken provenance
chain — Intake is where that chain starts.

**Resolution Path:**
- Define tag physical durability requirements —
  material, attachment method, environmental
  resistance for storage and handling conditions.
- Define re-identification protocol for lost tags —
  how is an untagged item matched back to its
  intake record?
- Define duplicate identifier prevention — tag
  numbers are sequential and never reused.
- Define record/item reconciliation at Gate_02
  handoff — physical tag verified against digital
  record before routing.
- Cross-validate with `Admin/Ship_of_Theseus.md`
  grain system requirements — GI-006 and GI-004
  may resolve together.
- Payment via Specification — once chain-of-custody
  doctrine is defined and tested, move to Section 7
  as Analogous.

**Grok review 2026-08-14:** Path adequate. Tag durability, re-identification, no-reuse IDs, and Gate_02 reconciliation are the correct integrity controls; joint resolution note with GI-004 is sound. **Grok approved (path adequate).** Remains Open — doctrine still needs to be written; may resolve jointly with GI-004.

---

### GI-007 — Digital contamination and hostile firmware handling not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Security                             |
| Blocking      | No                                               |
| Owner         | Operations/Gate_01_Intake.md                     |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-08-14                                       |

**Description:** Items containing storage media,
network interfaces, or programmable controllers may
carry malware, hostile firmware, or compromised
embedded systems. No isolation or handling protocol
exists for digital contamination at Intake.

**Why It Matters:** Given `Architecture/Forge_Net.md` network
integration, a compromised device connected to forge
systems before isolation could propagate malware to
the reference database, corrupt cognitive save states,
or compromise network trust scoring. Digital
contamination is invisible, fast-propagating, and
potentially irreversible at the network level. Physical
contamination hazards are better understood — digital
hazards are not yet acknowledged in the system.

**Resolution Path:**
- Define digital hazard indicators at Intake —
  presence of storage media, network interfaces,
  wireless capability, or programmable controllers
  triggers isolation protocol before any connection.
- Define isolation protocol — air-gapped assessment
  before any forge system connection. No exceptions
  for "probably safe" items.
- Define assessment capability — what tools and
  expertise are required to clear a device for
  connection? This may require external expertise
  at v0 bootstrap.
- Cross-reference: `Operations/Electronics.md`,
  `Architecture/Forge_Net.md`, `Architecture/
  Cognitive_Frameworks.md` rogue unit doctrine.
- Payment via Specification — once isolation protocol
  is defined and tested, move to Section 2 as
  Analogous.

**Grok review 2026-08-14:** Path adequate. Isolation-first / no-exceptions posture is correct given Forge_Net integration; indicators and assessment-capability questions are the right ones. **Grok approved (path adequate).** Remains Open — concrete isolation protocol still needs to be written; external expertise note for v0 is realistic.

---

### Resolution Log

- 2026-08-15 (second entry, same day): **GI-003 wired as a supporting
  dependency into the shared PL-001/WA-002/TS-002 detection-and-routing
  pipeline, not a parallel path.** No change to GI-003's own status — kit
  selection and protocol definition remain open. Human-directed.

- 2026-08-15: **GI-002 spec-depth pass — digital-only, no equipment exists.**
  Wrote actual discharge doctrine by energetic category (lithium cells,
  other battery chemistries, capacitors, compressed gas) at Analogous
  confidence — standard industry electrical/battery safety practice, not
  Forge-specific experimental content. Reused `Gate_04_Separation_Mechanical.md`
  MG-007's lockout-before-access pattern for operator safety rather than
  inventing a separate one; isolation-area content vs. FA-001 siting kept
  cleanly split. Surfaced a real gap in the process: `Operations/Air_Scrubber.md`
  has no general unknown-content gas intake path, only Cl₂-specific handling —
  flagged there as a note, not silently assumed solved, and not unilaterally
  given a new unknown ID. GI-002 remains **Open**, Blocking Yes unchanged —
  doctrine is now written; "written and tested" (this file's own bar for
  promotion) still needs a first operational run. Human-directed.

- 2026-08-14: **Grok resolution-path review (Round 1 — Operations start).** All seven GI unknowns reviewed against source. Every Resolution Path judged adequate; none invent parallel doctrine; none understate residual evidence needs. Markers added under each path. Last Reviewed → 2026-08-14 on all seven. **No GI-* closed.** Open Unknowns remain 7. Blocking status unchanged (GI-002 Yes; others No). Human-directed.

- 2026-08-10: **Pseudo-audit (Grok, same limits).** Spec Gates left locked
  at 0/6. (1) Open Unknowns **7** = GI-001–007, matches local + `Unknowns.md`.
  (2) **GI-002 Blocking No → Yes** — file’s own language (“hard prerequisite
  before first operational Intake run”, “safety prerequisite… not a
  refinement”, Safety Advisory points at GI-002) was stronger than the
  Blocking field; same pattern as TS-002 / EL-005. (3) GI-003 Critical /
  Safety / Blocking No logged for human review (detection capability gap).
  (4) No GI-* closed. Human-directed.

- 2026-05-19: GI-006, GI-007 — New entries logged
  following ChatGPT audit 2026-05-19. Chain-of-
  custody integrity and digital contamination both
  identified as structurally important gaps given
  Forge_Net.md integration. Provisional chain-of-
  custody doctrine added to Section 7. Digital
  contamination category added to Section 2 hazard
  table. Degraded operation doctrine added to
  Section 1. Cognitive fatigue and backlog collapse
  doctrine added to Section 1. Intake-to-Triage
  authority boundary added to Section 8. Parts list
  scope constraint added to Section 5.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from `Admin/Forge_Audit_Kit.md`
  to `Admin/Verification_Gates.md` (PC-001).
  Scope Boundary and sidecar UNK-006 references
  updated to `Architecture/Facilities.md` FA-001
  (PC-002). Section 2 operator safety cross-reference
  updated to match.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Intake as a simple pass-through screen — visual check and tag only | Underspecifies the entry point for the entire system. Hazard detection, document handling, database lookup, parts list generation, fastener recovery, and unknown item protocol all surfaced as load-bearing functions that a simple screen misses entirely | No — expanded scope is correct and necessary |
| 2026-05-15 | Direct escalation of unknown items to Human/AI Oversight Gate without hold and inspect | Wastes Oversight Gate capacity on items that a closer inspection could resolve. Hold and inspect recovers partial identification in many cases and produces higher-quality intake records and network contributions | No — hold and inspect is correct doctrine |
| 2026-05-15 | Fasteners routed to bulk Reduction by default | Fasteners are among the most practically useful salvage items and are routinely lost to shredding in conventional scrapping. Default Reduction wastes recoverable value and contradicts preserve-before-destruction doctrine | No — Class A salvage default is correct |
| 2026-05-15 | Formal fastener registry at v0 | Registry overhead not justified at v0 scale. Human judgment governs recovery threshold until volume data exists. A formal registry is a v1+ consideration when throughput makes manual judgment impractical | Reconsider at v1 when operational volume data justifies registry overhead |
| 2026-05-15 | Visual inspection as sole hazard detection method | Visual inspection cannot detect lead, radiation, or most chemical contaminants. Relying on it alone creates a known blind spot for the most serious contamination categories. Augmented detection capability required — see GI-003 | No — augmented detection is permanent doctrine once established |
| 2026-05-15 | Continuous document scanning as an ongoing Intake task | Documents arrive rarely. Treating document scanning as a routine continuous task creates overhead without proportional value. Scan-on-arrival when documents are present is correct — not a standing workflow step | No — scan-on-arrival is correct scoping |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
`Admin/File_Template.md` apply. The following are
additional local triggers specific to Gate_01_Intake:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| GI-002 energetic discharge doctrine remains undefined at first operational Intake run | Energetic materials without discharge doctrine are an acute safety hazard — hard prerequisite, not a deferral |
| GI-003 augmented detection capability remains undefined at first unsupervised Intake run | Visual inspection alone cannot detect lead or radiation — unsupervised operation without augmented detection has a known safety blind spot |
| Visual inspection reinstated as sole hazard detection method after augmented detection is established | Abandoned path — reverting requires explicit human authorization and documented justification |
| Fastener recovery default changed from Class A salvage to bulk Reduction without operational data justifying the change | Preserve-before-destruction doctrine applies to fasteners — override requires evidence that recovery overhead exceeds value at operational scale |
| Unknown items routed to gate logic without hold and inspect protocol completed | Unknown items proceeding without inspection risk misrouting hazardous or high-value material — hold and inspect is mandatory before escalation |
| Intake tagging schema revised without GI-004 cross-validation against grain system | Schema changes that break grain system compatibility sever the provenance chain at its first link |
| Reference database lookup removed from Intake sequence | Database lookup is the primary identification path — removal degrades identification quality to operator-judgment only and reduces network contribution |
| Automation introduced at Intake without GI-002 and GI-003 resolution | Automated Intake without validated hazard detection removes the human compensating factor — both safety prerequisites must be resolved first |
| Pre-Intake protocol invocation authority restricted to management approval only | Any operator must be able to call a hold without approval — restricting this creates pressure to proceed with unsafe items |
| Document scan-on-arrival practice abandoned without evidence that document yield is consistently too low to justify | Scan-on-arrival preserves rare but high-value documentation and contributes to network knowledge base — abandonment requires operational yield data |

### Canonical Drift Triggers

*All mandatory re-audit conditions from `Admin/File_Template.md`
Section 11 apply without exception. Local triggers above are
additive, not substitutes.*
