# AUDIT_HARNESS.py — Version History

Full changelog for `Automation/AUDIT_HARNESS.py`, relocated out of the
script's own docstring as of v14 (2026-07-13). Newest entries first.
Add new entries here, not back into the .py docstring.

────────────────────────────────────────────────────────────────────

CONTENT-INTEGRITY REPAIR (2026-09-03, no code version change):
  - This file's own `## Audit Trail` section (below the patch log)
    contained ~45 lines of verbatim `Unknowns.md`/`Unknowns_Changelog.md`
    content wrongly present here — unrelated registration entries for
    AP-, GOV-, CLF-, SEC-, RIP-, EC- clusters, ending 2026-07-29.
    Removed and replaced with an explicit content-gap note; not
    reconstructed, since no clean copy was available to recover the
    genuine harness Audit Trail from. Full account in the note itself,
    below. Caught by Claude source-verifying a same-day Grok audit of
    `AUDIT_HARNESS.py` that had listed this changelog as loaded
    baseline without catching the mismatch (human-directed).

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

**Content-integrity note (2026-09-03):** This section previously contained ~45 lines of verbatim `Unknowns.md`/`Archive/Logs/Unknowns_Changelog.md` content (registration entries for AP-, GOV-, CLF-, SEC-, RIP-, EC- clusters, v1.0 through v4.30, ending 2026-07-29) — content that describes Unknowns.md's own history and has no connection to `AUDIT_HARNESS.py`. This was almost certainly a copy-paste error from a session working on multiple changelog files at once, given the timing lines up with `Unknowns_Changelog.md`'s own 2026-07-19 creation and its content trail continuing to the same 2026-07-29 endpoint. The error predates this session — it was present, identically, in every archive uploaded today, so no data was lost by today's work.

Found by Claude source-verifying a 2026-09-03 Grok audit of `AUDIT_HARNESS.py` (which had listed this changelog as loaded baseline material without catching the mismatch). No earlier clean copy of this file was available in any archive on hand to recover the genuine pre-v13-patched Audit Trail content from, so it is not reconstructed here — inventing plausible-sounding harness history would repeat the exact failure mode this repository's audit doctrine exists to prevent (see Auditor_Protocols.md Rule on fabrication). This section is intentionally left as a documented gap rather than backfilled.

If the genuine harness Audit Trail (predecessor entries to the "CHANGES IN THIS PATCH" log above, presumably covering v1 through v13's initial creation and early iteration) exists in an earlier local copy, a GitHub history/blame lookup, or a session transcript outside what's been uploaded this session, it should be restored from that source rather than reconstructed from memory.
