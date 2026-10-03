# Operational_Conventions.md — LazarusForge

**Quick-reference for mechanical rules that are easy to violate silently.**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|----------------------------------------------------------------------|
| Status           | Specification                                                       |
| Body Stability   | Stable                                                               |
| Spec Gates       | N/A — reference index, not a governed doctrine surface               |
| Verification Ref | Admin/Verification_Gates.md                                          |
| Last Audit       | 2026-10-03 — Convention 8 added (rotation-rule self-enforcement failure, Progress_Log.md + Unknowns.md). Prior: 2026-09-30 — file created. |
| Auditor          | Claude — human-directed                                              |
| Open Unknowns    | 0                                                                     |
| Active Disputes  | 0                                                                     |
| Highest Risk     | Low                                                                   |
| Sidecar Link     | N/A — this file carries no sidecar entries of its own                |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present.   |

---

## Purpose

This file exists because several mechanical rules in this repository were found,
independently, to have been violated without anyone (including Claude) noticing at the
time — not because the rules were unclear once found, but because each one lives buried
inside the doctrine file it happens to be adjacent to, with nothing pointing a
contributor there before the mistake is made. Every rule below has already caused a real,
observed error in this repository's history, cited alongside it.

**This file does not duplicate doctrine.** Each entry is one to three lines plus a
pointer to the file that actually owns the rule. If this file and its source disagree,
the source wins — update this file, not the other way around. This file is exempt from
the full File_Template.md structure (Template Exemptions, class: reference index) for the
same reason Discovery.md and Routing.md are: forcing Lessons Learned / Active Disputes /
Abandoned Paths sections onto a pointer list would bury the pointers it exists to surface.

Add an entry here only once a rule has demonstrably been missed in practice — not
speculatively. A rule nobody has ever actually violated doesn't need to be here yet.

---

## Conventions

### 1. Cross-repository filename tags go *inside* the backticks

Reference a file in a companion/external repository (Astroid-miner, etc.) with the
bracket tag inside the same backtick pair as the filename — for example, the correct form
for Astroid-miner's models registry is `` `[Astroid-miner] MODELS.md` ``, never the
filename alone in its own backtick pair with the tag outside. The two forms are not
interchangeable: `Automation/audit_lib.py`'s reference extractor requires the character
immediately after an opening backtick to be a letter, so a bracket there correctly removes
the whole span from cross-reference checking — a bare filename inside backticks with no
tag gets checked as if it were a same-repo file and flagged `[UNKNOWN]`.

**Violated:** 2026-09-29, this session — two Astroid-miner filenames written as bare,
untagged backtick references in `Admin/Trajectories.md` and `Admin/Progress_Log.md`, found
only when the resulting cross-reference warnings were investigated for a different reason.
Fixed same session. Not a novel failure mode: the `[ExternalRepo]` convention itself was
registered 2026-08-11 in `Admin/Canonical_Terms.md` precisely because the same problem
was first hit and debugged in `Admin/Autonomy_Divergence_Protocol.md` — that file tried
the tag outside the backtick pair, then the whole `[Astroid-miner] filename.md` string
inside one pair, before the explicit convention was written down. This session repeated
the same mistake the rule already existed to prevent, which is itself evidence for why a
pointer here (rather than relying on the rule being found once and remembered) is needed.
**Source of truth:** `Admin/Canonical_Terms.md`, "`[ExternalRepo]` reference convention"
(2026-08-11); debugging history in `Admin/Autonomy_Divergence_Protocol.md`.

### 2. The Ethical Anchor field is one exact string, everywhere

`Attempt to do no harm. Defer to Ethical_Constraints.md if present.` — no backticks around
the filename, no abbreviation, no rewording, in every file that carries the field.

**Violated:** found drifted (backticked filename, or missing "if present") in three live
files — `Operations/Exception_Evidence.md`, `Tests/Multi_Agent_Quorum_Trial.md`,
`Tests/Persistent_Cognition_Candidates.md` — as of the 1.17 release, cause not established
(pre-dated this session's records).
**Source of truth:** `Admin/File_Template.md` File State section; enforcement mechanics in
`Admin/Repository_Integrity_Protocol.md`.

### 3. A suffixed ID is a distinct ID, not a variant of its base

`EC-011-R3`, `GMP-010-R1`, `EC-012-PR` are each their own entry — not a residual note
folded under `EC-011`, `GMP-010`, or `EC-012`. Give each its own `### ID — Title` header.
Verified real examples of the pattern, not illustrative placeholders: `AP-013-R1`
(`Admin/Auditor_Protocols.md`) and `EC-012-PR-R1` (`Admin/Ethical_Constraints.md`) — a
suffix can itself carry a further suffix, and each layer is still its own distinct ID.

**Violated:** `Automation/integrity_check.py`'s sidecar-ID regex used a plain `\b` word
boundary after the numeric portion, which also matches the boundary before a trailing
hyphen — so `### EC-012-PR` was parsed as a second definition of plain `EC-012` and
flagged as a same-file duplicate. Found and fixed 2026-09-29.
**Source of truth:** the suffix pattern itself is established usage across
`Admin/Ethical_Constraints.md` and `Admin/Governance_Migration_Protocol.md`; the fixed
regex is in `Automation/integrity_check.py`.

### 4. A relocated sidecar's real text may not be where its ID is registered

Several files moved their full sidecar write-ups and Resolution Log to
`Archive/Logs/<FileName>_Logs.md` (or `_Changelog.md`) while the ID stays registered
against the original file in `Unknowns.md`. `Admin/Auditor_Protocols.md` →
`Archive/Logs/Auditor_Protocols_Logs.md` is one instance; check for a
similarly-named `_Logs.md`/`_Changelog.md` in `Archive/Logs/` before concluding a
registered ID's content is missing or thin.

**Violated:** 2026-09-29 — AP-033/Rule 9's actual text was assumed absent from Candidate
3's indexed sections based on checking only `Admin/Auditor_Protocols.md`; it was actually
present and correctly retrieved from `Archive/Logs/Auditor_Protocols_Logs.md`, which a
first-pass note had not checked.
**Source of truth:** each relocation is logged in the owning file's own Resolution Log at
the time it happened (e.g. `Admin/Auditor_Protocols.md`'s 2026-07-23 entry). Also confirmed
in use for `Discovery.md` → `Archive/Logs/Discovery_Changelog.md` and `Unknowns.md` →
`Archive/Logs/Unknowns_Changelog.md` (changelog-naming variant of the same pattern) — check
for a same-named `_Logs.md`/`_Changelog.md` file under `Archive/Logs/` before concluding a
registered ID's case history doesn't exist.

### 7. New files need a `*_Scope_Map.md` entry too, same session

`Admin/File_Template.md`'s New File Creation Checklist requires registering a new file in
its folder's `*_Scope_Map.md` (`Admin/Adm_Scope_Map.md`, `Architecture/Arc_Scope_Map.md`,
`Operations/Ops_Scope_Map.md`, `Challenges/Cha_Scope_Map.md`, `Tests/Tst_Scope_Map.md`) as
a Does/Does-not entry — separate from, and in addition to, the `Routing.md` row.

**Violated:** this file itself — added to `Routing.md` and linked from `Discovery.md`'s
Agent Orientation on 2026-09-30, but not added to `Admin/Adm_Scope_Map.md` until this rule
was written and the omission checked for. Fixed in the same pass as this entry.
**Source of truth:** `Admin/File_Template.md`, New File Creation Checklist.

### 5. `Archive/` duplicate sidecar IDs are expected, not a defect

A live file and an `Archive/Logs/` or `Archive/Transcripts/` file legitimately sharing a
sidecar ID is normal — it means the archive holds a preserved prior-state snapshot, per
`Admin/Repository_Integrity_Protocol.md`'s prior-state doctrine. This is not something to
"fix" by renaming or deleting either copy.

**Violated:** N/A — this was a checker false-positive, not a repository error, but it was
flagged as "probably not real, unconfirmed" across several audits before actually being
checked. `Automation/integrity_check.py` now excludes `Archive/` from this scan.
**Source of truth:** `Admin/Repository_Integrity_Protocol.md` prior-state preservation
rules; the two clearest live examples self-declare it in their own header
(`Archive/Transcripts/Configurations.md`).

### 6. `Automation/`'s `.py` sources are exempt from `Routing.md` registration

Scripts under `Automation/` do not need a `Routing.md` row. Documentation that is itself
doctrine (not a script) still does.

**Not yet violated** — included pre-emptively, since `Automation/README.md` and
`Candidate3_Transient_Index_Colab.py` were checked against this rule in 2026-09-28
session work and correctly left unregistered; recorded here so the next check doesn't
have to re-derive the reasoning from `Routing.md`'s own text.
**Source of truth:** `Routing.md`, registration-scope note near the top of the file.

### 8. A "keep only the N most recent, rotate the rest" rule does not enforce itself

Several files carry a stated self-maintenance rule of this shape — `Admin/Progress_Log.md`
("rotate to `Archive/Logs/Progress_Log_Changelog.md` once more than five entries
accumulate") and `Unknowns.md` ("this block now keeps only the current version," full
history in `Archive/Logs/Unknowns_Changelog.md`) are the two confirmed instances. Writing
the rule into the file does not make a new entry trigger the rotation; each addition has
to actively check the count/version against the stated limit and move the overflow, every
time, or the file silently grows past its own stated bound with nobody noticing until
someone counts.

**Violated:** 2026-10-03, both files, independently. `Progress_Log.md` had accumulated 16
dated entries under its five-entry rule, un-rotated since the file's creation (2026-08-09)
— eleven moved to `Progress_Log_Changelog.md` in one pass. `Unknowns.md` had five versions
(5.53–5.57) stacked in its current-version-only block; three of them (5.54–5.56) had never
even been migrated to `Unknowns_Changelog.md` at all, not just left stacked — a stricter
failure than Progress_Log's, since the changelog itself had a real gap, not just a
duplicate. Neither was caught by a scheduled audit; both were found only because a human
asked a direct question about changelog state after an unrelated piece of work.
**Not a new defect class:** `Unknowns_Changelog.md`'s own 2026-09-10 migration note records
this exact pattern happening once before on that same file (14+1 versions stacked, caught
only when asked directly) — meaning this rule class has now been violated and separately
re-discovered at least three times (2026-08-09 Progress_Log/Discovery.md origin pair,
2026-09-10 Unknowns.md, 2026-10-03 both files again) without anyone adding the standing
checklist item that would catch it earlier next time. This entry is that checklist item.
**Check before closing any session that added Current Lessons/version entries to either
file:** count entries against the stated limit; rotate if over, in the same session, not
as a follow-up.
**Source of truth:** `Admin/Progress_Log.md`'s own "Size discipline" paragraph; `Unknowns.md`
line 4 (the block's own stated rule); migration history in both files' `Archive/Logs/`
changelogs.

---

*This section holds candidate entries only until they graduate to full write-ups above,
or are declined. None currently pending.*
