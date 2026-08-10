# Progress_Log.md — Active Notebook for Repository Progression

## Navigation Anchors
[README.md](../README.md) | [Discovery.md](../Discovery.md) | [Routing.md](../Routing.md) | [Unknowns.md](../Unknowns.md) | [Admin/Adm_Scope_Map.md](Adm_Scope_Map.md)

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Active — Living Document                                            |
| Spec Gates       | N/A — this file is a progression log, not a specification           |
| Open Unknowns    | 0 (references existing unknowns; creates none)                      |
| Owning Domain    | Admin/                                                               |
| Last Reviewed    | 2026-08-09                                                           |
| Ethical Anchor   | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md` if present. |

---

## Purpose

Created 2026-08-09 to fix a recurring failure mode found the same day, in two places at once: `Discovery.md` had a "Cross-Module Unknowns — Attention Required" table that was 19 versions stale (last refreshed at `Unknowns.md` v4.29 while the live file was at v4.48), and `Unknowns.md` itself had a "What v4.39 Means" section that had silently violated its own Size Management Rule 1 for nine consecutive version bumps — that rule requires the section to be retired and replaced every time a new version is cut, and nobody had been doing it. Both were narrative/progression content trapped inside structural index files, with no dedicated home and nothing forcing either to stay current.

**This file DOES:**
- Hold the rolling answer to "what did we just learn, what's currently open, what's next" — the thing `Unknowns.md`'s old "What vX.X Means" section tried to be, without a version number baked into the heading this time, so a new entry never requires renaming the section.
- Track recent completed work at a summary level, for continuity across sessions.

**This file does NOT:**
- Duplicate `Unknowns.md`'s Active Index — that remains the sole authoritative source for open unknowns; this file references IDs, never restates their full detail.
- Duplicate the five `*_Scope_Map.md` files' per-file scope content.
- Hold anything that belongs in a Resolution Log — file-specific change history stays in that file's own log, not here. This file is for cross-cutting lessons and session-level continuity, not a substitute for per-file logs.

**Size discipline, learned directly from what broke last time:** this section rotates. Keep the current entry plus the four most recent in full below; older entries move to `Archive/Logs/Progress_Log_Changelog.md` in full, same split pattern already established for `Unknowns.md`/`Unknowns_Changelog.md`. No version number in any heading here — headings are dated, so nothing about adding a new entry ever requires editing an old one's title. This rotation rule was exercised for the first time the same day this file was created — see Resolution Log.

---

## Current Lessons

*(Most recent first. Rotate to `Archive/Logs/Progress_Log_Changelog.md` once more than five entries accumulate.)*

### 2026-08-09 — A newly-fixed pattern can have a live instance sitting right next to it, unnoticed
Right after `Discovery.md`'s Rename Registry and Attention Required table were fixed for the "narrative content with no dedicated home" problem, that file's own five-entry correction-note history — sitting inline mid-file since 2026-07-04 — turned out to be exactly the same problem, one section over. Not caught independently; surfaced by direct human review of the delivered patch. Two lessons in one: fixing an instance of a pattern doesn't mean the search for other instances is done, and a second pair of eyes on a "complete" fix is still worth having, even from the person who didn't write the code.

### 2026-08-09 — Even this file's own creation caught a live instance of the pattern it exists to prevent
While retiring `Unknowns.md`'s stale "What vX.X Means" section, found that
its "keep only the current version in the main block" rule had itself been
unenforced for two versions — v4.46 and v4.47's full text were both still
sitting in the main block, never moved out when each was superseded,
duplicating content already safely in `Unknowns_Changelog.md`. Caught by
a routine post-edit verification pass, not by design. Same lesson as the
entry directly below, one level more recursive: a rule stated once is not
a rule enforced continuously, even in the file created specifically to
track that problem.

### 2026-08-09 — Progression content trapped in structural files goes stale in both directions
Two failures found the same day, from opposite ends of the same problem: `Discovery.md`'s shadow index of `Unknowns.md` (19 versions stale, nobody refreshing it) and `Unknowns.md`'s own "What vX.X Means" section (stale by nine version bumps, silently violating its own stated rule). Neither was caught by any audit pass in between — both were only found when directly asked to check whether Discovery.md content should migrate elsewhere. The general lesson: a rule that says "update this when X happens" is not the same as X reliably triggering the update. This file exists as the standing fix — one place, checked routinely, rather than duplicated content nobody remembers to touch.

### 2026-08-08 — Routing.md can diverge from reality without anyone noticing, even across sessions
`Routing.md`'s live GitHub state was stuck at 2026-06-06 (35 entries), while a local working copy contained a much larger, more detailed version (139 lines, 89 entries, a specific bug-fix narrative) describing work that never actually happened on the real file. The false version was detected and initially misattributed to the human collaborator's own diligence, rather than questioned — caught only because the human directly said "it shouldn't have the updates" and asked for a re-check. Lesson: a file matching expectations is not the same as a file being verified against its real source; local/session state can drift from the actual repository silently, and the fix is checking the live source directly, not trusting a prior description of it — including one's own.

### 2026-08-07/08 — A single ownership reassignment can leave stale pointers scattered across files that never cross-check each other
UNK-008's ownership moved to `Architecture/Geck_forge_seed.md` on 2026-07-19. Three separate files (`Architecture/Forge_flow.md`, `Operations/Gate_05_Separation_Thermal.md`, `Operations/Gate_06_Fabrication.md`) still said "no owner assigned" or equivalent weeks later, found only once the five-folder `*_Scope_Map.md` build put every file's cross-references in one place for the first time. No single file's own audit would have caught this — it only became visible in aggregate.

---

Full history, including entries rotated out of the five above, in `Archive/Logs/Progress_Log_Changelog.md`.

---

## Resolution Log

- 2026-08-09: **Second rotation, same day as the first.** Adding the
  "newly-fixed pattern, live instance right next to it" lesson (about
  `Discovery.md`'s correction-note history turning out to have the same
  problem as its Rename Registry) brought the total to six again. Rotated
  2026-08-06/07 out to the changelog. Human-directed — specifically,
  caught by the human reviewing a delivered patch, not by this session's
  own verification pass, which is itself worth being honest about in the
  entry rather than glossing over.

- 2026-08-09: **Rotation rule exercised for the first time, same day as file
  creation.** Adding the "even this file's own creation caught a live
  instance" entry brought the total to six, past the stated five-entry
  cap. Oldest entry (2026-08-01/02) rotated to the new
  `Archive/Logs/Progress_Log_Changelog.md`, verbatim, nothing altered.
  Also fixed while verifying this file: `Unknowns.md`'s main block was
  still carrying v4.46 and v4.47's full text after both had already been
  safely copied to `Unknowns_Changelog.md` — the "keep only current
  version" rule had gone unenforced across two version bumps. Removed
  the duplicates from `Unknowns.md` directly; nothing was lost, both
  versions were already intact in the changelog. Human-directed.

- 2026-08-09: **File created.** Absorbs the function of `Unknowns.md`'s retired
  "What v4.39 Means" section (migrated as the fifth entry above) and replaces
  `Discovery.md`'s removed "Cross-Module Unknowns — Attention Required" table,
  which was deleted outright rather than migrated — `Unknowns.md`'s own Active
  Index with Priority/Blocking columns already serves that exact function
  without a shadow copy. See `Discovery.md` and `Unknowns.md`'s own Resolution
  Log / correction-note entries, same date, for the removal side of this
  change. Human-directed.
