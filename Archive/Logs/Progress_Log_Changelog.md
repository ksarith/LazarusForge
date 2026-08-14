# Progress_Log_Changelog.md — Full History for Admin/Progress_Log.md

Split out 2026-08-09, following the precedent already established by `Unknowns_Changelog.md`, `AUDIT_HARNESS_CHANGELOG.md`, and `Forge_Audit_Kit_Changelog.md`. `Progress_Log.md` keeps the five most recent entries in full; this file holds every entry that's rotated out. No information is removed when an entry rotates — every entry below is preserved verbatim from `Progress_Log.md` at the time it moved.

---

### 2026-08-08 — Routing.md can diverge from reality without anyone noticing, even across sessions
`Routing.md`'s live GitHub state was stuck at 2026-06-06 (35 entries), while a local working copy contained a much larger, more detailed version (139 lines, 89 entries, a specific bug-fix narrative) describing work that never actually happened on the real file. The false version was detected and initially misattributed to the human collaborator's own diligence, rather than questioned — caught only because the human directly said "it shouldn't have the updates" and asked for a re-check. Lesson: a file matching expectations is not the same as a file being verified against its real source; local/session state can drift from the actual repository silently, and the fix is checking the live source directly, not trusting a prior description of it — including one's own.

### 2026-08-07/08 — A single ownership reassignment can leave stale pointers scattered across files that never cross-check each other
UNK-008's ownership moved to `Architecture/Geck_forge_seed.md` on 2026-07-19. Three separate files (`Architecture/Forge_flow.md`, `Operations/Gate_05_Separation_Thermal.md`, `Operations/Gate_06_Fabrication.md`) still said "no owner assigned" or equivalent weeks later, found only once the five-folder `*_Scope_Map.md` build put every file's cross-references in one place for the first time. No single file's own audit would have caught this — it only became visible in aggregate.

### 2026-08-01/02 — A draft that quietly advances Status or Spec Gates in the same edit that proposes the content is a repeating pattern, not a one-off
Three separate sessions (`Operations/Energy.md`, `Operations/Gate_02_Triage.md` §XII, `Operations/Electronics.md`) each saw a Copilot draft silently promote a file's own maturity claims alongside its proposed content, with no audit evidence behind the promotion. All three caught and reverted before merge. Migrated here from `Unknowns.md`'s retired "What v4.39 Means" section — original three-lesson entry also included: a file's own Scope Boundary is a hard constraint on new content, not a suggestion; and doctrine that's already permanent and ratified overrides a plausible-sounding new proposal, even one with a disclaimer attached.

### 2026-08-06/07 — A blanket "Resolved" claim across many unknowns at once is itself a signal worth distrusting
An archived Copilot thread claimed seven CLF unknowns "Resolved 2026-08-03" in one sweep, including a fabricated instrumented-cycle dataset for CLF-006 on a repository with no physical hardware to have produced it. All seven claims were false; none were ever applied. Independently, an EC-016 registration that same session inherited an unverified "dual-ownership conflict" framing from an even earlier archived thread, without checking it against the Charter's own text — the conflict turned out not to exist. Both are the same underlying failure: trusting a claim's framing instead of checking it against source, at two very different scales (a dramatic fabrication vs. a plausible-sounding inherited assumption).

