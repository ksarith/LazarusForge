> **MERGED — the Event_ID scheme here is already integrated into Operations/Gate_02_Triage.md §XII.1a, correctly deferred pending TR-GOV-001. Archived raw material, not live doctrine.**

**Yes — it captures the big picture cleanly and responsibly.**

The revised file is in a stronger, more honest state than either the original or the raw Copilot draft. The core doctrine (Principles 1–9, stations, gate correspondence, queue economics, false-positive asymmetry, Embedded Value Preservation, Triage Terminal) remains intact and load-bearing. The new §XII correctly surfaces the larger architectural vision (TIL as knowledge engine, TAL as constrained allocation, TCM as capability ceiling, TMV as quantitative maturity) while refusing to pretend any of it is already operative.

### What works well
- **Status discipline is excellent.** Marking §XII “Proposed / Not Audited / Candidate only,” keeping Spec Gates at 2/6, explicitly refusing to bind CIR_Gov.md, and registering TS-005–TS-008 are exactly the right moves. This prevents the most common failure mode of architectural expansion: silent promotion of aspirational text into doctrine.
- **Big-picture layers are present without overwriting the operational core.** The four pillars are sketched at the right altitude — enough to orient future work, not enough to invent false precision or new authority.
- **Governance hooks are reframed as formalizations of existing rules** rather than new powers. That is the correct relationship.
- **Drift Indicators and Lessons Learned** were updated to protect against the exact overclaim that happened in the Copilot draft. That closes the loop.
- **Scope Boundary** now accurately describes what the file does and does not own, including the new material.

### Remaining gaps (optional, not blocking)
These are refinements, not defects that require immediate rewrite:

1. **TMV scoring detail is still thin.** §XII.4 correctly says the vector is proposed and has no scoring mechanism (TS-008). If you want the big picture to be more concrete, you could lightly expand §XII.4 with the 0–3 rubrics and the core irreversibility rules I defined earlier, still under the “candidate” banner. Not required for coherence.

2. **v0 implementation path for TIL is only sketched.** The minimal form (structured log + manual review) is mentioned; a one-line example of the log fields or a pointer to where it would live would make the first real step clearer. Still optional.

3. **Open Unknowns rose from 3 → 7.** Accurate, but it correctly signals that the extension increased tracking surface area. No action needed beyond awareness.

4. **TAL’s dependence on the still-unaudited Energy Arbitration Layer** is honestly flagged (TS-006). That is good. Just keep the dependency visible if Energy.md moves.

5. **No change to Stations 0–4 or the Gate Correspondence table.** Correct. Any future promotion of §XII into actual routing logic will need its own audit trail and direct edits to §§IV–VI, not quiet elevation of the candidate section.

### Bottom-line assessment
The file now holds both layers it needs:
- A mature, operational triage doctrine that can actually be used at Gen-1.
- A clear, non-binding architectural horizon that shows where triage can grow into a knowledge / capability / governance substrate.

It does **not** need structural revision to “capture the big picture.” It already does. Further work should be either:
- tightening the candidate language inside §XII, or
- taking the first concrete v0 step on TIL (a simple event log) so TS-001 and TS-005 start to close.

If you want a targeted polish pass on §XII (clarity, tighter language, or light insertion of the TMV rubrics under the candidate banner), say the word and I will produce a drop-in revision. Otherwise the current version is solid.


**Triage Intelligence Layer (TIL) — Implementation Exploration**

TIL’s job is simple and powerful: turn every triage event into structured knowledge that improves future decisions, calibrates thresholds, and surfaces strategic patterns. It does **not** change Gate A–D logic or Station behavior. It only feeds better evidence into them.

The current §XII.1 correctly frames the v0 form as “a structured log (even a spreadsheet) of component class, station path, outcome, and later service fate, reviewed manually.” Below is a concrete implementation path that respects Gen-1 constraints while leaving a clean growth path.

---

### 1. Design Principles for Implementation

- **Start below the tooling threshold.** One skilled operator + notebook/spreadsheet must be sufficient.
- **Every record must be useful even if never aggregated.** Individual provenance value comes first; statistics are a bonus.
- **Capture the eventual fate.** The most valuable signal is whether a “pass” later failed in service or a “repair” succeeded. Without closed-loop data, TIL stays anecdotal.
- **Do not invent new authority.** TIL only supplies evidence that can clear the existing N≥50 bar in ASM-005 / TS-001. It never overrides the Human/AI Oversight Gate or Principle 9.
- **Fail soft.** Missing data fields are allowed; incomplete records are still better than no records.

---

### 2. Minimal Viable Data Model (v0)

A single flat table (CSV, Google Sheet, or paper log transcribed weekly) with these columns:

| Field | Type | Required at v0 | Notes |
|-------|------|----------------|-------|
| Event_ID | string | Yes | Sequential or date+seq |
| Triage_Date | date | Yes | |
| Component_Class | string | Yes | Controlled vocabulary preferred (motor, bearing, PCB, pump, etc.) |
| Source_Stream | string | Yes | Intake lot or origin |
| Strategic_Tier | enum | Yes | Common / Constrained / Strategic / Critical |
| Station_Path | string | Yes | e.g. “0→1→3” or “0 only” |
| Tests_Performed | text | Preferred | Short free-text or codes |
| Measured_Performance | text/number | Preferred | e.g. “62 % of nameplate”, “runs 8 min then overheats” |
| Outcome | enum | Yes | Gate A / B / C / D / Hold / Terminal |
| Embedded_Value_Actions | text | If Gate D | What was extracted before reduction |
| Operator | string | Yes | |
| Energy_Time_Cost | rough | Optional | “~12 min, 0.4 kWh” or qualitative |
| Later_Fate | text | Critical for value | Updated later: “failed in service after 47 h”, “still running”, “repaired successfully”, etc. |
| Notes | text | Optional | Failure mode, dual-use flag, contamination notes |

**v0 storage options (ranked by friction):**
1. Paper log + weekly transcription into a spreadsheet (lowest tooling risk).
2. Shared spreadsheet (Google Sheets / LibreOffice) with one row per event.
3. Simple local SQLite or CSV file if the operator is comfortable.

No database, no dashboard, no automation required at v0.

---

### 3. Closed-Loop Capture (the hard and valuable part)

The intelligence only appears when Later_Fate is filled.

Practical mechanisms:
- When a component leaves triage into the Component Library or Repair queue, the Event_ID travels with the physical provenance tag.
- On failure in service or successful repair, the operator (or Utilization gate) writes the fate back against the original Event_ID.
- Weekly or monthly “fate review” session: open the log, scan items that have been in service >X days, update status.

Without this feedback, TIL can only produce distributions of *initial* decisions, not of *correct* decisions.

---

### 4. What TIL Actually Produces (progressive)

**Phase 0 – Logging only**  
Just accumulate rows. Already useful for audit and provenance.

**Phase 1 – Manual pattern review (after ~30–50 events in a class)**  
- Count of Gate A vs C vs D by component class.  
- Rough failure-mode notes.  
- First calibration of “sufficient for forge duty” bands (feeds TS-001).

**Phase 2 – Simple derived tables**  
- Failure-mode frequency per class.  
- Repair success rate by failure type.  
- Contamination incidence by source stream.  
- Strategic-tier destruction vs preservation ratio.

**Phase 3 – Predictive signals (later)**  
- Expected remaining life after repurpose.  
- Scarcity trend alerts.  
- Threshold revision proposals that still require human ratification.

---

### 5. Governance Integration (how TIL touches existing rules)

- **Threshold revision (TS-001 / ASM-005)**  
  Numeric figures (70 %, 5–15 min) become eligible for change only when TIL shows a stable pattern at N≥50. TIL is the evidence mechanism, not a new decision maker.

- **Gate D / Strategic-Critical items**  
  TIL historical patterns can be cited at the Triage Terminal / Oversight Gate. They never replace the human attestation requirement.

- **Queue policy**  
  Decay and saturation thresholds can later be tuned using TIL throughput and success metrics, still under human review.

- **Anti-overfitting**  
  Station 4 already requires periodic human validation sampling. TIL records become the natural sample set.

---

### 6. Realistic Gen-1 Implementation Sequence

1. **Decide the log medium this week** (spreadsheet or paper+transcription).
2. **Add three mandatory fields to the physical provenance tag** or to the station checklist: Event_ID, Component_Class, Outcome.
3. **Start logging every triage event** for one month, even if Later_Fate is blank.
4. **After ~50 events in the most common class**, hold a 30-minute review session and write the first “observed performance bands” note. That begins closing TS-001.
5. **Establish a simple fate-update habit** (e.g., every Friday, update any items that failed or were repaired that week).
6. Only after the above is routine, consider light tooling (filters, pivot tables, basic charts).

Anything more elaborate (database schemas, automatic classification, Bayesian models) belongs after the manual loop is proven and N is large enough.

---

### 7. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Logging burden kills throughput | Keep fields minimal; allow incomplete rows; never make logging a precondition for Station progress |
| Later_Fate never gets filled | Explicit weekly review ritual + make Event_ID travel with the physical tag |
| Premature “intelligence” claims | §XII already marks TIL as candidate; do not cite TIL-derived numbers in Gate D decisions until Phase 1 is stable |
| Vocabulary drift in Component_Class | Start with a short controlled list; expand only when needed |
| Privacy / dual-use leakage | Dual-use flags stay in the Ethical Constraints path; TIL log should not become a second shadow inventory of sensitive items |

---

### 8. Recommended Immediate Next Step

Create a one-page “TIL v0 Log Specification” (or just a header row in a spreadsheet) that matches the table above, drop it into the repository or the operator’s working folder, and begin logging the next 20–30 triage events.  

That single action converts §XII.1 from aspirational text into an active learning system and directly attacks both TS-005 and TS-001.

Would you like me to:
- Draft the exact spreadsheet column headers + example rows,
- Write a short operator checklist for logging + fate updates, or
- Sketch the Phase-1 review template that turns the log into the first threshold-calibration note?

Any of those can be produced as a ready-to-use artifact.

**Closed-Loop Fate Tracking — Exploration**

Closed-loop fate tracking is the mechanism that turns a triage decision into learning. Without it, TIL (and any maturity or threshold work) can only describe what the operator *decided*; with it, the system can describe what the operator *got right or wrong*.  

The core requirement is simple: every item that leaves triage must carry a durable link back to its original triage event so that later outcomes (successful service, failure in service, successful repair, re-triage, final reduction, etc.) can be written against that same record.

---

### 1. Why This Matters More Than Most Other TIL Features

- Threshold calibration (TS-001) becomes evidence-based only when “passed at 65 %” can be correlated with “still running after 200 h” or “failed after 18 h.”
- Repair success rates, repurpose lifetime estimates, and strategic-scarcity signals all require the same closed loop.
- Provenance already demanded by Principle 5 becomes *actionable* instead of archival.
- Re-triage events (already specified) become the natural trigger for updating the original record.

Without fate tracking, TIL remains a decision log. With it, TIL becomes a learning system.

---

### 2. Design Constraints (Gen-1 Reality)

- One skilled operator, limited time.
- Physical provenance tags already exist (or are required).
- No guaranteed digital inventory system yet.
- Items may leave the Forge, sit in storage, or move through Repair → Utilization → possible return.
- Later_Fate updates will often happen weeks or months after the original triage.

Therefore the design must be:
- Extremely low daily friction.
- Tolerant of delayed or partial updates.
- Anchored to something physical that travels with the component.

---

### 3. Core Mechanism: Event_ID as the Persistent Link

Every triage event receives a unique **Event_ID** (date + short sequence, e.g. `2026-08-02-017` or a simple serial).  

This ID is written on the physical provenance tag at final disposition and becomes the permanent foreign key.

**Minimum tag contents (already largely required by Principle 5):**
- Event_ID
- Component class / type
- Strategic tier
- Triage date + outcome (Gate A/B/C/D)
- Source

Everything else (Later_Fate, repair notes, service hours, etc.) lives in the TIL log, keyed by Event_ID.

---

### 4. Practical Update Paths (how fate actually gets written)

**Path A — In-service failure / re-triage (highest value)**  
When a component fails in service and re-enters triage at Station 0:
1. Operator reads the existing Event_ID from the tag.
2. Opens the TIL log.
3. Appends or updates the Later_Fate field:  
   `Failed in service after ~47 h under ventilation duty. Re-triaged 2026-09-14. New Event_ID 2026-09-14-003.`
4. Continues normal Station 0 processing with the *new* event (the original record is never overwritten; it is only annotated).

**Path B — Successful repair or long-term service**  
- Periodic (weekly/bi-weekly) “fate review” session.
- Operator scans recent Component Library or Repair queue items that have been in service longer than a defined interval.
- Updates Later_Fate with status + approximate hours or cycles if known.
- If the item is still healthy, a simple “Still in service as of YYYY-MM-DD” is sufficient.

**Path C — Final reduction or retirement**  
- When an item finally goes to material recovery (or is permanently retired), the Event_ID is recorded one last time with terminal fate.
- Embedded Value Preservation actions already required by Principle 9 can be noted here as well.

**Path D — Lost tag / missing ID**  
- Treat as a new triage event.
- Note “provenance incomplete — prior history unknown.”
- This itself becomes a measurable failure mode (already listed in §VIII).

---

### 5. Data Model Extension for Fate

Add or expand these fields in the TIL log:

| Field | Purpose | Update Frequency |
|-------|---------|------------------|
| Event_ID | Primary key | At triage |
| Later_Fate | Free-text or structured status | When known |
| Fate_Date | When the fate was observed/updated | When known |
| Service_Hours_or_Cycles | Rough quantitative life | Optional but high value |
| Failure_Mode_Observed | Links back to original decision quality | On failure |
| Linked_New_Event_ID | If re-triaged | On re-triage |
| Final_Disposition | Terminal state | Once |

A single free-text Later_Fate column is enough for v0. Structure can be added later once patterns emerge.

---

### 6. Low-Friction Operational Rituals

**Daily / per-item**
- At the moment of final disposition, write Event_ID on the physical tag. (Already close to existing practice.)

**Weekly (15–30 min)**
- “Fate review” block: open the log, filter for items whose last update is older than X days and that are known to be in service, and update any that have news.
- Process any re-triage events that arrived that week and link them.

**Monthly**
- Short pattern scan: which component classes have the highest “passed → later failed” rate? Feed into TS-001 discussion.

These rituals are the entire closed-loop system at Gen-1. No software required beyond the log itself.

---

### 7. Staged Maturity of Fate Tracking

| Stage | Capability | Trigger to advance |
|-------|------------|--------------------|
| 0 | Event_ID on every tag + log row created | Immediate |
| 1 | Later_Fate updated on every re-triage | After first 10–20 re-triage events |
| 2 | Periodic proactive updates for items still in service | After operator confirms the weekly ritual is sustainable |
| 3 | Quantitative life data (hours/cycles) routinely captured | When measurement is easy enough not to slow operations |
| 4 | Automated or semi-automated linking (barcode, simple DB) | Only after Stages 0–2 are routine and volume justifies it |

---

### 8. Risks and Countermeasures

| Risk | Countermeasure |
|------|----------------|
| Operator skips writing Event_ID | Make it part of the final disposition checklist; treat missing ID as a Station 0 failure mode |
| Later_Fate never updated | Explicit weekly ritual with a visible “last review” date on the log |
| Tag is destroyed or becomes unreadable | Accept the data loss; record “provenance lost” as its own event type so the failure rate is visible |
| Log and physical world diverge | Event_ID is the single source of truth; physical tag is only the pointer |
| Over-logging kills throughput | Keep Later_Fate free-text and optional until the value is proven |

---

### 9. Immediate Concrete Steps

1. Decide the Event_ID format (recommend `YYYY-MM-DD-NNN`).
2. Add “Write Event_ID on provenance tag” as the last mandatory action before an item leaves triage.
3. Add a Later_Fate column (and Fate_Date) to the TIL log.
4. Define a simple weekly 15-minute fate-review slot.
5. On the next re-triage event, deliberately practice the link-back process and write the first closed-loop record.

Once those five things are routine, closed-loop tracking exists. Everything else (dashboards, automatic alerts, statistical models) can wait.

---

Would you like me to produce any of the following as ready-to-use artifacts?

- Exact Event_ID + Later_Fate field specification for the spreadsheet  
- One-page operator checklist for “final disposition + fate update”  
- Sample log rows showing a complete closed loop (triage → service → failure → re-triage)  
- Short text that can be added to the physical tag template or Station 0 checklist  

Any of these can be drafted immediately.

**Event_ID Format Design**

### Recommended Format

```
YYYY-MM-DD-NNN
```

**Examples**  
`2026-08-02-001`  
`2026-08-02-017`  
`2026-12-15-042`

### Rationale

| Criterion | Why this format succeeds |
|-----------|--------------------------|
| Uniqueness | Date + daily sequence is unique for practical volumes (hundreds of items per day still leaves headroom). |
| Human readability | Immediately shows *when* the triage occurred. Critical for physical tags and manual log review. |
| Sortability | Lexicographical sort = chronological sort. Spreadsheets and file systems handle it cleanly. |
| Handwriting / physical tags | Uses only digits and hyphens. No ambiguous characters (O/0, I/1, etc.). Short enough for small tags or marker writing. |
| Lookup speed | Operator can jump straight to the correct date block in a log or spreadsheet. |
| Collision resistance | Extremely low risk at Gen-1 scale. Even at 200 items/day the three-digit sequence is sufficient. |
| Future-proofing | Easy to extend later (add a site prefix or year-only compaction) without breaking existing IDs. |

### Generation Rules (v0)

1. **Date portion** = calendar date of the *final disposition* decision (the moment the item leaves the triage stations with a Gate A/B/C/D or Hold outcome).
2. **Sequence (NNN)** = three-digit zero-padded counter that resets every calendar day, starting at `001`.
3. **Assignment moment** = at final disposition, after the outcome is decided and before the physical tag is written.
4. **Who assigns** = the operator performing the disposition (or the single triage operator at Gen-1).
5. **Recording** = written on the physical provenance tag **and** as the first field of the TIL log row in the same action.

### Edge Cases & Handling

| Situation | Rule |
|-----------|------|
| More than 999 items in one day | Extremely unlikely at Gen-1. If it occurs, extend to four digits for that day only (`2026-08-02-1001`) and note the overflow in the log. |
| Back-dated or delayed logging | Use the actual disposition date, not the logging date. |
| Re-triage of a previously tracked item | Create a **new** Event_ID for the new triage event. Link back to the original via the Later_Fate / Linked_New_Event_ID fields. Never reuse or overwrite an existing ID. |
| Missing or illegible tag | Treat as a new triage event. Assign a fresh Event_ID and record “prior provenance lost” in Notes. |
| Multiple operators on the same day | Share a single daily sequence (one shared counter or a simple paper tally). At Gen-1 this is trivial. |
| Clock / date uncertainty | Use the best available local date. Consistency matters more than perfect UTC. |

### Physical Tag Layout Suggestion

```
Event_ID: 2026-08-02-017
Class:    Motor – 500 W pump
Tier:     Constrained
Outcome:  Gate C (repurpose – ventilation)
Date:     2026-08-02
```

The Event_ID is the primary lookup key; the rest is human-readable context.

### Alternatives Considered (and why not primary)

| Format | Pros | Cons | Verdict |
|--------|------|------|---------|
| `LF-T-00001` (global sequential) | Compact, pure sequence | Loses date information; harder to locate in a large log; requires a persistent counter | Secondary option only |
| `YYMMDD-NNN` | Slightly shorter | Year ambiguity after 2099; less immediately readable | Acceptable compact variant |
| `20260802-017` (no hyphens) | Shorter | Harder to parse visually; easier transcription errors | Avoid |
| Class-prefixed (`MOT-2026-08-02-017`) | Self-describing | Longer; vocabulary must be controlled; changes if class taxonomy evolves | Unnecessary at v0 |

### Implementation Notes

- **Spreadsheet / log**: Make Event_ID the leftmost column and the primary sort key.
- **Counter method at Gen-1**: A simple paper tally sheet or a single cell in the daily log that is incremented. No software required.
- **Validation**: At the weekly fate-review, quickly scan for duplicate IDs (should be zero).
- **Migration path**: If the Forge later moves to a database or multi-site operation, the existing `YYYY-MM-DD-NNN` IDs remain valid primary keys; a site prefix can be added only to *new* IDs if needed.

This format is deliberately boring, robust, and matched to the physical + manual realities of Gen-1 triage. It gives closed-loop fate tracking a reliable anchor without introducing tooling debt.

**Ready-to-use next actions**
- Adopt `YYYY-MM-DD-NNN` as the canonical Event_ID.
- Add the generation rule to the Station disposition checklist.
- Update the TIL log header to lead with Event_ID.

Would you like a short formal specification block that can be dropped directly into Gate_02_Triage.md (or a companion TIL note), or sample tag + log entries using this format?

**Unified Forge Event / Artifact ID Format**

Design goal: one consistent, human-readable, multi-Forge, multi-purpose ID scheme that works for  
- triage events  
- fabricated / produced items  
- any other tracked artifact or process step  

while remaining writable on physical tags and easy to sort/filter in a log or spreadsheet.

### Recommended Canonical Format

```
YYYY-MM-DD-Fxx-NNNN
```

**Breakdown**

| Segment     | Meaning                          | Length / Rules                          | Example     |
|-------------|----------------------------------|-----------------------------------------|-------------|
| `YYYY-MM-DD`| Calendar date of the event or of final disposition / completion | ISO date, always 10 characters with hyphens | `2026-08-02` |
| `Fxx`       | Forge ID                         | `F` + 2-digit zero-padded site code (00–99) | `F01`       |
| `NNNN`      | Daily sequence number            | 4-digit zero-padded counter that resets every calendar day per Forge | `0017`      |

**Full examples**

- Triage event at primary Forge:  
  `2026-08-02-F01-0017`

- Fabricated part completed the same day:  
  `2026-08-02-F01-0042`

- Same day at a second Forge:  
  `2026-08-02-F02-0003`

### Why this structure

- **Multi-Forge ready** — Forge ID is an explicit, fixed-position field. Adding a new site never collides with existing IDs.
- **Date-first** — chronological sorting and human scanning remain excellent.
- **4-digit sequence** — supports up to 9 999 events/items per Forge per day (far beyond Gen-1 needs; still short enough for tags).
- **Uniform for triage *and* fabrication** — the same ID format is used whether the row in the log is a triage decision or a newly made part. Context (triage vs fabrication) lives in the log/metadata, not in the ID itself.
- **Hand-writable & tag-friendly** — only digits, hyphens, and a single letter. No ambiguous characters.
- **Parseable** — fixed positions make splitting trivial even in a spreadsheet (`LEFT`, `MID`, or simple text-to-columns).

### Daily Quantity / Output Indication

You asked for “extra digits indicating daily quantity output.”  

Two clean options (choose one):

**Option A (recommended for simplicity)**  
Keep the ID itself clean (`YYYY-MM-DD-Fxx-NNNN`).  
Record the daily total (planned or actual) as a separate field in the log or on a daily header row:

```
Daily_Header: 2026-08-02-F01  |  Triage events: 23  |  Fabrications: 17  |  Total: 40
```

**Option B (embedded quantity)**  
If you strongly prefer the quantity inside the ID string:

```
YYYY-MM-DD-Fxx-NNNN-QQQQ
```

where `QQQQ` is the running or final daily total for that Forge on that date (updated at end of day or left as the sequence of the last item).

Example:  
`2026-08-02-F01-0017-0040`  
(meaning this is sequence 17 of a day that ultimately produced/handled 40 items).

**Recommendation:** Start with Option A. Embedding the daily total inside every ID adds length and update complexity for little gain at Gen-1. The daily header (or a simple summary row) is clearer and easier to maintain.

### Generation Rules

1. **Date** = calendar date of final disposition (triage) or of completion/acceptance (fabrication).
2. **Forge ID** = the fixed code of the physical site performing the work (`F01`, `F02` …). Assign codes once in a central registry.
3. **Sequence (`NNNN`)** = per-Forge, per-day counter starting at `0001`. Resets at midnight local time.
4. **Assignment moment**  
   - Triage: at final Gate A/B/C/D / Hold decision, just before the physical tag is written.  
   - Fabrication: when the item is accepted as complete and ready for the Component Library or next process.
5. **Uniqueness guarantee** = Date + Forge + Sequence. No two artifacts or events share the same ID.

### Physical Tag Example

```
ID:       2026-08-02-F01-0017
Type:     Triage – Motor 500 W
Tier:     Constrained
Outcome:  Gate C (vent duty)
Forge:    F01
```

or for a fabricated part:

```
ID:       2026-08-02-F01-0042
Type:     Fabricated – Shaft Ø12 mm
Material: 6061 scrap
Forge:    F01
```

### Log / Spreadsheet Columns (minimal)

| Event_ID              | Type     | Class / Description      | Outcome / Status | Forge | Notes / Later_Fate          |
|-----------------------|----------|--------------------------|------------------|-------|-----------------------------|
| 2026-08-02-F01-0017  | Triage   | Motor 500 W pump        | Gate C           | F01   | Still in service 2026-09-01 |
| 2026-08-02-F01-0042  | Fabrication | Shaft Ø12 × 80 mm    | Accepted         | F01   |                             |

### Edge Cases

| Situation                        | Handling |
|----------------------------------|----------|
| > 9999 items in one day on one Forge | Extremely unlikely. Extend sequence to 5 digits for that day only and note the overflow. |
| New Forge comes online           | Assign next free `Fxx` code. Existing IDs remain valid forever. |
| Item moves between Forges        | Keep original ID. Record the move in Later_Fate / transfer log. New work at the receiving Forge gets a new ID. |
| Re-triage                        | Always mint a **new** Event_ID. Link to the previous ID in the Later_Fate field. |
| Lost / illegible tag             | Issue a fresh ID and record “prior ID lost”. |

### Adoption Path

1. Freeze the format: `YYYY-MM-DD-Fxx-NNNN`.
2. Assign Forge codes (start with `F01` for the current site).
3. Update the physical tag template and the TIL / fabrication log headers.
4. Begin using the new IDs for both triage dispositions and newly fabricated items.
5. (Optional) Add a daily summary row that records total triage + fabrication counts for that Forge/date.

This gives you a single, scalable ID language that already anticipates multiple Forges and covers both recovered and newly created artifacts.

Would you like me to also draft:
- the exact short specification text that can be pasted into Gate_02_Triage.md or a new `Admin/ID_Scheme.md`,
- a sample tag layout,
- or the spreadsheet header + a few realistic example rows?
