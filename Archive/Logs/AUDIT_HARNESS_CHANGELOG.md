# AUDIT_HARNESS.py — Version History

Full changelog for `Automation/AUDIT_HARNESS.py`, relocated out of the
script's own docstring as of v14 (2026-07-13). Newest entries first.
Add new entries here, not back into the .py docstring.

────────────────────────────────────────────────────────────────────

CHANGES IN THIS PATCH (v15 → v16, 2026-08-04):
  - Cell 1: FALLBACK_REGISTRY — added Pyrolysis_Cascade.md (Tests/).
    Discoverable via dynamic parse once Routing.md's Master Routing Map
    gains a row for it (added same date). Added here per this file's
    own established practice of also mirroring new files into the
    fallback safety net, matching the Chaos_Dynamics.md precedent
    below rather than skipping it.
  - EXTRA_FILES commented catalog — added Pyrolysis_Cascade.md under
    Tests/ section for discoverability: "staged thermal cascade,
    PYC-UNK items."
  - No KNOWN OPEN ITEM added: unlike Chaos_Dynamics.md and
    Return_To_Eden.md at their creation, Pyrolysis_Cascade.md already
    has a full File State table as of this compile (confirmed via
    direct fetch, 2026-08-04) — no "File State table not found"
    finding expected on first Phase 1 pass.

────────────────────────────────────────────────────────────────────

CHANGES IN THIS PATCH (v14 → v15, 2026-07-16):
  - Root fix, not a relabeling: CURRENT_CYCLE (manual per-session
    counter) and UNKNOWN_FIRST_CYCLE / Admin/unknown_cycles.json
    (cycle-number registry, built at v14) removed entirely.
    Admin/Canonical_Terms.md §4 ratifies Cycle = one calendar year by
    default — confirmed 2026-07-16 (human) that this was ratified
    specifically to keep Expiry Watch from being too aggressive.
    CURRENT_CYCLE incremented per session, not per year, so every aging
    computation under it was roughly 26-50x more aggressive than the
    ratified intent, not merely mislabeled. See
    Admin/Auditor_Protocols.md's Adversarial Audit Layer (2026-07-14
    Battery finding) and Admin/Governance_Charter.md's GOV-013 drafting
    session (2026-07-16) for the evidence chain.
  - Replacement: every unknown's own sidecar entry already carries a
    required "First Logged: YYYY-MM-DD" field. extract_boundary() now
    captures that date alongside each UID (result["unknowns"] is a list
    of (uid, first_logged) tuples, was a list of uid strings — the one
    breaking change, both consumers in this file updated). check_aging()
    computes age in real elapsed days against EXPIRY_THRESHOLD_DAYS = 365
    (Canonical_Terms.md §4 default). No registry to fetch, maintain, or
    keep in sync with newly-registered unknowns — the data was already
    present and authoritative; v14's JSON map was solving the wrong
    problem (bulk of a redundant registry) instead of the actual one
    (aging computed in the wrong unit).
  - First Logged extraction required widening the field-table snippet
    window used during sidecar parsing: the existing 8-line window
    (sized for the Resolved/Discharged check, left unchanged) doesn't
    reach First Logged for the 8-field GOV-*/AP-* convention. Added a
    second, boundary-based snippet (scans to the next `##`/`###` header,
    capped at 30 lines) specifically for the date search, rather than
    widening the existing window and risking a behavior change to the
    Resolved/Discharged check it wasn't built for.
  - Verified before shipping: behavioral test against synthetic sidecar
    entries (open/recent, open/old, resolved/old — correctly excluded,
    no-date) confirmed correct extraction, exclusion, and aging in both
    directions; a second pass against real Admin/Governance_Charter.md
    content confirmed the fix in practice — GOV-001 through GOV-013 are
    1-55 days old, not "8 cycles," and none are overdue under the real
    365-day threshold. The prior SESSION BOUNDARY INDEX language reporting
    those same unknowns as "8 cycle(s) open" (see a 2026-07-16 audit,
    same day) was the miscalibration this patch removes.
  - format_boundary_index() output changed accordingly: header now reads
    threshold in days with a Canonical_Terms.md citation instead of
    "Current cycle: N"; overdue lines report days and an approximate
    year figure instead of a bare cycle count; unknowns with no
    parseable First Logged date are now listed explicitly (age unknown,
    not silently flagged either way) rather than disappearing from the
    aging report.
  - Admin/unknown_cycles.json is no longer fetched by this harness and
    is now orphaned — left in the repository as history (Routing.md
    2026-07-16 note), not registered as a live cross-reference, not
    deleted.

────────────────────────────────────────────────────────────────────

CHANGES IN THIS PATCH (v13-patched-4 → v14, 2026-07-13):
  - Structural split, no audit-logic behavior change. Prompted by file
    size review: ~380 of 1130 lines were static data or history rather
    than logic (this changelog: 133 lines; UNKNOWN_FIRST_CYCLE: 105
    lines; ALIASES/FALLBACK_REGISTRY: 86 lines; EXTRA_FILES catalog: 46
    lines). Addressed the two safely-externalizable pieces; left the
    rest in place, see rationale below.
  - Cell 3.5, UNKNOWN_FIRST_CYCLE: extracted from an inline dict to
    Admin/unknown_cycles.json (grouped by category for readability,
    flattened at load time), fetched via the existing fetch() mechanism.
    Registered in ALIASES as "unknown_cycles.json" — not
    FALLBACK_REGISTRY, since the dynamic Routing.md parser only matches
    backtick paths ending in .md or .py, so a .json entry there would
    never resolve on the (typical) path where Routing.md fetch succeeds;
    ALIASES is merged in on both the success and failure paths. On fetch
    or parse failure, harness now logs a warning and falls back to an
    empty mapping (all aging reported as unmapped) rather than halting —
    consistent with how other non-critical fetch failures are already
    handled. Net effect: registering a new unknown ID's first cycle is
    now a JSON edit, not a .py diff. Extraction verified by
    ast.literal_eval cross-check against the original dict before this
    file was written — 316/316 entries matched exactly.
  - Docstring changelog (this history): relocated from the
    AUDIT_HARNESS.py top docstring into this file. Motivation is not
    just size — the v13-patched-2 and v13-patched-3 entries below both
    document external audits (Grok, 2026-07-11) citing stale "still
    missing" status because this docstring hadn't been updated after
    the underlying files were fixed. Keeping a long, easy-to-miss
    history embedded in the same script that's re-pasted into Colab
    every session was part of what let that staleness persist
    unnoticed; a standalone changelog file doesn't fix staleness by
    itself but removes the specific "buried in 140 lines of docstring"
    failure mode.
  - _enforce_phase1(): split the three inline Phase 1 checks into named
    functions (_check_ethical_anchor, _check_required_fields,
    _check_cross_refs), called in the same order as before. Pure
    isolation refactor — same checks, same Finding objects, same
    control flow (including the sys.exit(1) quarantine halt on
    constitutional mutation, which stays in _check_ethical_anchor). Goal
    is that a future fix to one check — same pattern as the bold-key and
    lean-schema fixes in v13-patched-4 below — doesn't require re-reading
    the other two checks to confirm nothing else changed.
  - ALIASES and FALLBACK_REGISTRY were considered for the same JSON
    externalization and rejected. FALLBACK_REGISTRY's only job is to
    keep the harness usable when Routing.md's fetch fails; moving it to
    a JSON file fetched from the same GitHub source would mean a dead
    connection takes out the primary lookup and its own fallback
    together. Both dicts stay hardcoded in AUDIT_HARNESS.py.
  - EXTRA_FILES commented catalog (Cell 2) was also considered and left
    alone — unlike the two dicts above, it's a per-session UI the user
    edits directly (uncommenting lines to add context files), not a
    lookup table maintained separately from its use.

────────────────────────────────────────────────────────────────────

CHANGES FROM v12:
  - Cell 1: FALLBACK_REGISTRY — added Chaos_Dynamics.md (Tests/).
    Already discoverable via dynamic parse — Routing.md's Master Routing
    Map gained a real row for it 2026-07-04 (created same date). Added
    here per this file's own established practice of also mirroring new
    files into the fallback safety net, not because dynamic parse needs it.
  - Cell 2: EXTRA_FILES commented list — added Chaos_Dynamics.md under
    Tests/ section for discoverability, flagged no-File-State-table.
  - KNOWN OPEN ITEM list — closed out the v12 item "Routing.md does not
    yet list Challenges/Return_To_Eden.md": that row was added 2026-07-04.
    Drift-detection print in _build_registry() should now report sync on
    that entry; if it still reports drift, Routing.md's row format may not
    match the backtick-path regex in _parse_routing() and needs a look.
    New KNOWN OPEN ITEM added for Chaos_Dynamics.md: no File State table
    as of this compile (confirmed via direct fetch, 2026-07-04) — same
    situation Return_To_Eden.md was already flagged for. Phase 1 will log
    a MAJOR/STRUCTURE "File State table not found" finding the first time
    it's fetched. Also missing the mandatory Navigation Anchors block
    (Routing.md backlink requirement) — this harness does not currently
    check for that block's presence at all (Phase 1 checks File State
    fields and cross-references, not the Navigation Anchors block itself),
    so it will NOT surface as a Phase 1 finding; tracked here instead until
    either the file is patched or a fourth Phase 1 check is added for it.

CHANGES IN THIS PATCH (v13 → v13-patched, 2026-07-07):
  - PC-005 (Closed_Loop_Feedstock.md registration): confirmed already
    present in FALLBACK_REGISTRY under Challenges/ — no change needed there.
  - Cell 3.5, extract_boundary(): sidecar-unknown detection previously only
    matched the "## Auditor Notes..." + "### UID" convention used by Gate_
    files. Challenges/Closed_Loop_Feedstock.md logs its ten CLF- unknowns
    as a markdown table under "## 6. Open Unknowns" instead — the old logic
    would have silently reported "none open" for a file carrying three
    Critical unknowns (CLF-003, CLF-004, CLF-006). Broadened to also
    trigger on any "Open Unknowns" header and match table-row IDs
    (| CLF-001 | ...), with inline Resolved/Discharged status checks since
    table format keeps status in the same row rather than 8 lines below.
  - Cell 3.5, UNKNOWN_FIRST_CYCLE: added CLF-001 through CLF-010 at cycle
    10. Previously unmapped — Expiry Watch could never fire for this file's
    unknowns (age reported as None, not overdue) with no visible indicator
    anything was missing from the map.
  - Cell 2, EXTRA_FILES menu: added Closed_Loop_Feedstock.md under
    Challenges/ section, with a note flagging the CLF-005 Φ_ext symbol
    collision against Return_To_Eden.md so an auditor working either file
    is prompted to consider pulling in the other.

CHANGES IN THIS PATCH (v13-patched-3 → v13-patched-4, 2026-07-12):
  - _parse_file_state() — fixed a bold-key parsing bug that caused every
    File State field using markdown bold formatting (`| **Status** |`
    rather than `| Status |`) to be stored under a key like "**Status**"
    instead of "Status", silently breaking every downstream lookup.
    This affected Check 1 (Ethical Anchor presence/mutation) and Check 2
    (required-field presence) for a large share of the repository —
    Water.md, Waste.md, Biofouling.md, Critical_Minerals.md,
    Planned_Obsolescence.md, Emergence.md, Energy_Scarcity.md,
    Trophic_Forge.md, Support_Raft.md, Living_Waters.md, and most other
    files edited in recent sessions all use bolded keys. Prior to this
    fix, Phase 1 would have reported Ethical Anchor and every required
    field as absent on all of them — a false positive, not a real
    constitutional or structural gap. Found 2026-07-12: three independent
    second-agent audits run against `Challenges/Energy_Scarcity.md`
    reported Status, Verification Ref, and Ethical Anchor as missing,
    when all three were plainly present in the source file. Verified the
    bug by direct regex test before patching, and re-verified against the
    live file after — both fields now parse correctly.
  - _enforce_phase1() Check 2 — added lean-schema detection. Files
    declaring `Challenges Subtype: Problem-Statement` in their File State
    table are now checked against the lean field set the subtype doctrine
    in `Admin/File_Template.md` actually sanctions (Status, Verification
    Ref, Ethical Anchor) rather than the full 11-field schema
    _bootstrap_rules() pulls from File_Template.md's own example table.
    Before this fix, every Problem-Statement Challenges file would have
    thrown false MAJOR/STRUCTURE findings for Spec Gates, Body Stability,
    Last Audit, Auditor, Open Unknowns, Active Disputes, Highest Risk,
    and Sidecar Link — none of which that subtype is supposed to carry.
    Same root incident as the bold-key fix above.
  - Neither fix has been run against the full repository yet — both were
    verified against `Challenges/Energy_Scarcity.md` and `Challenges/Water.md`
    specifically. A full Phase 1 sweep post-patch would be worth doing to
    confirm no other required-field or Ethical Anchor findings in past
    audit sessions were false positives from these two bugs.

CHANGES IN THIS PATCH (v13-patched-2 → v13-patched-3, 2026-07-12):
  - FALLBACK_REGISTRY — added Energy_Scarcity.md (Challenges/), new file
    created same date (v0.1, not yet Gate 1-reviewed). Also mirrored into
    Discovery.md (tree listing, file registry table, Scope Map entry),
    Routing.md (routing table), Unknowns.md v4.19 (new ES- cluster,
    ES-001 through ES-003), and README.md (External Challenges list,
    Status section file count) same day.
  - Cell 2: EXTRA_FILES commented list — added Energy_Scarcity.md under
    Challenges/ section. Also removed two stale annotations found while
    editing this block: Chaos_Dynamics.md's "no File State table yet" and
    Return_To_Eden.md's "no File State sidecar yet" — both were fixed in
    earlier sessions (Chaos_Dynamics.md received its full template
    skeleton 2026-07-12; Return_To_Eden.md's File State table predates
    this harness version) but the comments here were never updated to
    match. Same staleness pattern as the KNOWN OPEN ITEM entries closed
    out in the v13-patched-2 changelog below — docstring maintenance
    lagging actual file state, not a live repository gap.

CHANGES IN THIS PATCH (v13-patched → v13-patched-2, 2026-07-11):
  - KNOWN OPEN ITEM list — closed out both entries below. Direct fetch
    confirms Challenges/Return_To_Eden.md and Tests/Chaos_Dynamics.md
    both now have complete File State tables; Chaos_Dynamics.md also has
    its Navigation Anchors block. These were flagged stale after an
    external audit pass (Grok, 2026-07-11) cited them as still-missing —
    root cause was this docstring not being updated after the files were
    patched, not a live repository gap. See also: Unknowns.md v4.17,
    which had the same staleness problem on CLF-005/RE-UNK-001 and has
    been corrected.
  - NEW KNOWN OPEN ITEM added below: Index Sync Check proposal (Grok,
    2026-07-11) — harness currently has no automated check comparing a
    file's own Resolution Log dates against Unknowns.md's Active Index
    status for the same ID. This is what let CLF-005 sit Resolved in its
    owning file for four days while Unknowns.md still listed it Open,
    which then propagated as a false positive into an external audit.
    Proposed: a fourth Phase 1 check, or a lightweight WARNING tier, that
    flags any ID where the owning file's Resolution Log shows a later
    Resolved/Discharged date than what Unknowns.md's Active Index carries.
    Not implemented in this patch — flagged for scoping next session.

KNOWN OPEN ITEM (flag for next session, not fixed here):
  - Index Sync Check (see above) — not yet designed or implemented.
    Scoping questions for next session: does this run against every ID
    on every Phase 1 pass (cost/latency), or only on the specific file
    being audited plus its cross-referenced IDs? Where does the harness
    get the owning file's Resolution Log date from — new fetch logic, or
    reuse of the existing boundary extractor?

CLOSED THIS PATCH (previously KNOWN OPEN ITEM, verified resolved 2026-07-11):
  - Challenges/Return_To_Eden.md's missing File State sidecar table —
    confirmed present and complete via direct fetch.
  - Tests/Chaos_Dynamics.md's missing File State table and Navigation
    Anchors block — both confirmed present via direct fetch.





## Audit Trail

**v1.0–v3.0 (May–June 2026):** Full audit cycle across all primary documents. Seven operational gates, all Challenges/ and Tests/ clusters, and core Admin/ files indexed. Approximately 250 unknowns registered across GI, GR, GF, GU, EL, GOV, AP, RIP, SEC, EC, GMP, RS, PR, FA, SP, LW, TF, SD, EM, WA, BF, PO, WS, CM, CF clusters. Dependency Map and Discovery.md task tables retired. Twelve items resolved.
**v3.1 — 2026-06-11:** Location abstraction pass. TH-003, EN-002, FA-004 retitled to deployment-generic framing.
**v3.2 — 2026-06-11:** Architecture audit integration pass. ME-003, ME-004, TH-005, TH-006, CE-005, EN-006, FD-005 added. CE-003 elevated to Critical Watch. CE-004 In Progress. FA-005 resolved.
**v3.3 — 2026-06-14:** Three new Tests/ file clusters registered. LW (9), TF (10), SD (12) unknowns. TF-006 and SD-UNK-004 added to Critical Watch. DS-001 closed. 31 total new unknowns.
**v3.4 — 2026-06-18:** EC-008, EC-009, EC-010, EC-011, GOV-010, CT-005 registered. GOV-001 un-archived — returned to In Progress. EC-008, EC-011 added to Critical Watch.
**v3.5 — 2026-06-19:** SEC-008–011, RIP-006–007, GMP-006–008 registered. RIP-004 discharged. GMP-005 In Progress.
**v3.6 — 2026-06-19:** ENV cluster registered (9 unknowns). Environmental_Constraints.md created. ENV-007 resolved.
**v3.7 — 2026-06-21:** AP cluster updated per Auditor_Protocols.md v0.11. AP-006, AP-009 resolved. AP-001, AP-002, AP-004, AP-005 moved to In Progress. AP-008, AP-010, AP-011 registered. ENV-008 resolved. GOV-009, GOV-010, EC-010 moved to In Progress. EP-004 In Progress.
**v3.8 — 2026-06-21:** Structural maturation pass. Subtype column added to all active index tables. Unknown Budget and Reversion Protocol added to Size Management Rules. Dependency Clusters section added. Reopened status formally defined. AP-001 updated with retrospective calibration note.
**v3.9 — 2026-06-23:** RC governance pass. RC-007 through RC-009 registered in Future/Deferred with owning file Admin/Auditor_Protocols.md. Operational Blocking and Epistemic Blocking added to Canonical_Terms.md v0.3 as canonical vocabulary. CT-006 and CT-007 registered in CT sidecar.
**v4.0 — 2026-06-24:** Full Adversarial Battery pass on Admin/Auditor_Protocols.md complete — Classes 1–10, Claude + Gemini. Nine new unknowns AP-012 through AP-020 registered. AP-012 and AP-016 elevated to Critical Watch. Human Interaction Point Doctrine added. EF-0.2 autonomous degradation amendment committed. Gate 3 blocked pending AP-012/AP-016 Provisional Spec. AP-020 flagged for Trajectory discharge decision.
**v4.1 — 2026-06-24:** Cognitive Salvage cluster registered (GH-001 through GH-012). GH-009 Critical. GH-012 registered. GH-009 added to Dependency Clusters and Critical Watch. HF-001 registered in Canonical_Terms.md v0.3; CT-008 logged.
**v4.2 — 2026-06-28:** RIP-001 closed (Git release tags fulfill prior-state archival; full detail in Repository_Integrity_Protocol.md sidecar). RIP-006 In Progress. ST-004 registered. CT-008 In Progress, CT-009 Open. CF-004 registered. HR cluster added: HR-UNK-001 and HR-UNK-002 (both Critical). GH-009 and HR-UNK-002 added to Critical Watch.
**v4.3 — 2026-07-01:** Structural compression pass. Resolved & Discharged Archive retired — resolution detail lives in owning file sidecars per Lessons Learned doctrine; archive was a permanent accumulator contradicting the stated navigation-layer purpose. Audit Trail v1.0–v3.0 condensed to arc summary. Dead prose removed. Size Management Rule 2 updated. RE-UNK-001 through RE-UNK-005 registered (Challenges/Return_To_Eden.md, cycle 11); RE-UNK-001 and RE-UNK-005 co-blocking at Tier I gate. NT-010 registered (Admin/Nothingness Theorem, cycle 11). Philosophical/Foundational cluster added.
**v4.4 — 2026-07-02:** Multi-agent Security_Protocols.md audit follow-through. SEC-012 registered (asymmetric crypto overhead on constrained salvaged silicon; cross-ref EL-006). SEC-007 vertically split into SEC-007a (constitutional layer) and SEC-007b (physical implementation layer, blocked pending SEC-007a) — ad hoc pattern, human-governing-authority-adopted, not yet canonized. Dependency Clusters, UNK-009, GMP-004, EM-004 cross-refs updated to match split. Grok/Gemini G3/G6 gate-maturity disagreement on Security_Protocols.md flagged unresolved, pending human ruling.
**v4.5 — 2026-07-02:** External Design Lineage (EDL) registry added to Security_Protocols.md (PAT-001 through PAT-004). GOV-MAND-009 (EDL as constitutional promotion gate) declined for session-level adoption — routed to Governance_Migration_Protocol.md for future ratification instead.
**v4.6 — 2026-07-02:** SEC-007 sidecar reconciled into SEC-007a/SEC-007b. Grok/Gemini G3/G6 dispute resolved via Forge_Audit_Kit.md v1.5's Gate Scope vs. Promotion Readiness clarification — Gemini's original scoring confirmed correct.
**v4.7 — 2026-07-02:** Discovery.md reconciliation — Attention Required table refreshed, reciprocal pointer added. VG-001 logged its first incident (Forge_Audit_Kit.md v1.5 citation gap, caught, no divergence); remains Open.
**v4.8 — 2026-07-03:** AP-001–007 Systemic Risk escalation downgrade confirmed by human governing authority. An unrequested patch claiming AP-001/012/016 resolved was held for review pending full specification text. VG-001 discharged via Gate Definition Synchronization Protocol.
**v4.9 — 2026-07-03:** Held-for-review AP-001/AP-012/AP-016 patch verified and incorporated. Open Unknowns 12 → 9, Highest Risk Critical → High. AP-012/AP-016 removed from active index and Critical Watch.
**v4.10 — 2026-07-03:** Gate/Checkpoint naming collision resolved (renamed to Enforcement Checkpoints). GOV-011 registered — Governance_Charter.md's own Spec Gates field scored against the wrong system. CT-010 registered tracking rename propagation.
**v4.11 — 2026-07-05:** GOV-011 Resolved (6/6 execution quality confirmed). CT-011 Resolved. CT-007 escalated to Critical Watch (`EC-`/`ECN-` collision confirmed). EN-001 advanced to In Progress (differentiated interim safety-factor table). Seven new entries: GOV-012, EN-007, TR-003, EC-012 through EC-015.
**v4.12 — 2026-07-06:** Multi-file catch-up pass. CT-007 Resolved (`ECN-` rename verified against Economics.md source text; a citation error in the original escalation — EC-008 — was corrected, ECN-003 identified as the real fifth collision). EC-010 and ENV-007/008 sidecar drift corrected. New Closed-Loop Feedstock cluster registered (CLF-001–010, ten entries; CLF-003/004/006 Critical; ID collision history CF-→FL-→CLF- noted). ENV-DS-001 registered in Active Disputes, pending ratification. PC-005 registered. Cross-refs added: RE-UNK-001↔CLF-005, CM-002↔CLF-004.
**v4.13 — 2026-07-09:** CE-006 registered (`Architecture/Chemistry.md` — chlorine gas containment for on-site chlor-alkali acid synthesis, Critical), closing a same-day registration gap first logged 2026-07-07. Cross-referenced bidirectionally with CLF-004's candidate pathway. Added to Critical Watch and Dependency Clusters.
**v4.14 — 2026-07-10:** Corrected four stale Active Index entries (AP-001, AP-014, AP-015, AP-020) — all already Resolved at `Admin/Auditor_Protocols.md`'s own sidecar but never removed here; the reverse-direction sibling of the RIP-008 registration-lag class. AP-021 registered (confidence-label inconsistency within Auditor_Protocols.md, blocking `Admin/Verification_Gates.md` VG-002). `Admin/Evidence_Management_System.md` discharged via merge into `Admin/Verification_Gates.md` this same session — not independently registered here as it was never given standalone active-index entries.
**v4.15 — 2026-07-10:** AP-021 resolved same-day — five-label Evidence Classification system confirmed canonical. `Verification_Gates.md` Gate 2 pass criteria updated to require the evidentiary maturity-vector thresholds for Measured/Replicated claims, active at human-audit level; `AUDIT_HARNESS.py` automation not yet implemented. VG-002 resolved.
**v4.16 — 2026-07-10:** First full-repository sweep (enabled by direct zip upload rather than per-file spot-checks). Eight genuine registration gaps found and closed: FL-002, GF-005, GMP-002, GMP-009, PR-005, RIP-003, RS-002, RS-003 — all confirmed Open at source, none previously appearing here, including RIP-003 which this index's own author had missed across three prior versions. A candidate ninth cluster (LW-004/006/008/009/010) was checked and correctly rejected as pathway subsection headers, not unknowns. RS-003 flagged as possibly mooted by RIP-001 but not resolved on its behalf. Sweep also confirmed zero Ethical Anchor violations, zero Routing.md gaps, zero Discovery.md gaps, and a real structural finding outside this file's own scope: nine files (six Challenges/, two Tests/, matching an early-June cohort) lack a "Spec Gates" field in their File State tables entirely, predating the schema every recently-touched file now uses — not resolved here, flagged for separate follow-up.
**v4.17 — 2026-07-11:** CLF-005 marked Resolved (stale entry correction).
**v4.18 — 2026-07-12:** Tests/ registration gap sweep. SR-010 and GH-013 backfilled; Support Raft Priority column normalized.
**v4.19 — 2026-07-12:** Energy Scarcity cluster (ES-001–003) registered alongside new `Challenges/Energy_Scarcity.md`. Two unrelated stale entries in Discovery.md/Routing.md fixed same pass.
**v4.20 — 2026-07-12:** PC-006 registered and immediately Resolved — Ethical Anchor field variance fixed across 9 files by a full-repository sweep (file count later corrected, v4.24). PC-005 flagged as possibly stale, resolved v4.24. `Admin/Evidence_Management_System.md`'s Routing.md absence confirmed intentional — deprecated ghost file, functionally merged into `Verification_Gates.md`.
*(v4.21: number not used — confirmed absent from both this file and `Unknowns_Changelog.md`; documented there as a known, intentional gap rather than data loss.)*
**v4.22 — 2026-07-17:** Three ratification-only items adopted by human governing authority: ENV-DS-001 ratified (bridge-authority amendment); Embedded Value Preservation ratified into CLF-004's Scope Boundary; CLF-004's chlor-alkali pathway reframed as one of three options under consideration, CE-006 gained a directional (not completed) note.
**v4.23 — 2026-07-17:** GOV-014 through GOV-020 registered in `Admin/Governance_Charter.md` from a ChatGPT adversarial pass, every proposed ID collision-checked before registration. All seven added alongside GOV-013, itself missing from this table since its creation three turns prior. Open Unknowns count in `Admin/Governance_Charter.md`: 12 → 19.
**v4.24 — 2026-07-19:** PC-005 resolved — independently re-verified against source, closing a confirmation flag open since v4.20. PC-006's file list corrected — `Energy_Scarcity.md` wrongly included among the "9 files" fix; created after that sweep's fetch, its Ethical Anchor variant untouched until this pass.
**v4.25 — 2026-07-19:** CE-006 mechanism corrected — chlorine off-gas routing redirected from KMnO₄ chemisorption (verified ineffective against Cl₂) to caustic wet scrubbing, reframed as value-recovery (sodium hypochlorite byproduct). CE-007 registered for the resulting NaOCl storage doctrine gap.
**v4.26 — 2026-07-19:** Three additions logged without a version bump at the time, corrected here: LT-007 registered (`Tests/Leviathan_testing.md`, Astroid-miner cross-repo convergence); UNK-008 ownership reassigned to `Architecture/Geck_forge_seed.md`; GMP-010 registered (evidence-sufficiency gate gap, CE-006-grounded), extended same day with an adversarial-hardening addendum.
**v4.27 — 2026-07-27:** Registration-latency sweep — five entries registered in owning-file sidecars over the prior four days never cross-indexed: GOV-022, RIP-010, GMP-011/012/013. GOV-021 also registered (candidate since 2026-07-19, never formally entered). AP-024, AP-029, AP-030 also registered, open since 2026-07-17/23/26 respectively. Later merged with v4.28 to resolve a version-label collision.
**v4.28 — 2026-07-27:** Full rewrite following a repo-wide desync audit (Grok, five folders, verified against source before adoption), merged with a colliding parallel v4.27 draft. GitHub `main` confirmed still at v3.2, six weeks behind. GOV-013 removed from Active Index (confirmed ratified, was stale here). CT-006, CT-007 registered/corrected; EP-004, EV-002, EV-003 status corrected to match owning-file sidecars; CLF-005, SR-010 removed (already Resolved, still sitting in Active tables). CF-005 registered. CF-DS-001/CF-DS-002 marked Resolved in Active Disputes Registry.
**v4.29 — 2026-07-28:** CF-004 entry updated — `Admin/Computational Institutional Reasoning` §5.4 confirmed to formally define the debt-derivative trigger metric, Lyapunov-proven stable; numeric calibration remains Open. `Architecture/Cognitive_Frameworks.md` Section IV (Confidence Collapse States) revised same day to reference this metric for its Yellow→Orange transition, superseding its prior "under review" language.
**v4.30 — 2026-07-29:** CIR-001 added to Governance & Verification — existed in CIR's own sidecar since its 2026-07-28 rename but was never mirrored here, a registration-latency gap of the same kind v4.27 was built to catch. GOV-012's row enriched with its 2026-07-19 deferral decision, previously undescribed here despite being accurately Open. Found by checking this file against the session's own work, not from an external audit.

---
