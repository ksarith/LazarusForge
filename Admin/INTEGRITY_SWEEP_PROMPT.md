# INTEGRITY_SWEEP_PROMPT.md
**Version 1.0.1**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | N/A — operational prompt template, not a doctrine or specification claim |
| Verification Ref | Admin/Repository_Integrity_Protocol.md, Admin/Forge_Audit_Kit.md |
| Last Audit     | 2026-08-30                                                          |
| Auditor        | Claude — Synthesizer, human-directed, first draft, 2026-08-30. Consolidates a prompt refined across several morning-audit sessions run by Grok on external automation; captured here so the function survives independent of any one automation config. |
| Open Unknowns  | 0                                                                    |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Repository_Integrity_Protocol.md` and `Admin/Forge_Audit_Kit.md` v1.15.
When this file contradicts either source document, the source document prevails.

---

## Scope Boundary

**DOES define:** The exact prompt text to hand a fresh audit session (human copy-paste, or an automation's scheduled-task config) to run one LazarusForge morning integrity sweep; the fixed report shape; the honesty rules that keep findings from being invented or over-graded.

**DOES NOT define:** The integrity protocol's own design rationale or grading rules (→ `Admin/Repository_Integrity_Protocol.md`) · The condensed doctrine an auditor loads to run the sweep (→ `Admin/Forge_Audit_Kit.md`) · How a finding gets fixed once found (→ each owning file's own Resolution Log).

---

## File Purpose

This repository is worked primarily through periodic zip uploads to interactive sessions, not continuous live access — but a scheduled daily automation (currently: Grok, running against the live canonical GitHub repo, independent of the zip workflow) still needs a stable, versioned prompt rather than one hand-maintained only inside that automation's own config screen, where it can't be diffed, audited, or recovered if the config is lost. This file is that prompt's canonical source. When the prompt is revised, it is revised here first, then copied into whichever automation surface runs it.

---

## How To Use This File

1. Copy everything between the two `================` lines below.
2. Paste into a fresh audit session, or into a scheduled automation's prompt configuration.
3. The session fetches live from `https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/` — no zip or file attachment needed for this specific task.
4. Findings come back as a structured report; genuine ones (not the honesty-rule exclusions) get fixed against the actual working copy — currently the zip-based session workflow, not directly against GitHub — and re-uploaded to `main` on whatever cadence the human governing authority runs that sync.
5. If the prompt itself needs revision (new check added, a rule proven wrong, a report section reshaped), edit it here, log the change in the Resolution Log below, then copy the updated block to the automation.

================================================================

Run a LazarusForge repository integrity audit against the live canonical repo and produce a structured morning-style report.

Canonical base (use for all raw fetches unless checking the legacy alias once):
https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/

Legacy alias to check once for identity (not Major if content is the same family; this is a historical repo name, not a version of the current project):
https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md

Calendar window for "last 3 days": today and the two prior calendar days (use the current date when the automation runs).

Follow the repo's own rules where possible:
1. Fetch Routing.md, Discovery.md, Unknowns.md, and Admin/Forge_Audit_Kit.md first — the kit is the condensed audit reference (governing principles, Ethical Anchor, Audit Opening Checklist, Fallacy Checklist) and should be the default source for these instead of fetching Admin/Auditor_Protocols.md or Admin/File_Template.md directly. Only fetch those two full source files if the kit's own Drift Indicators suggest it's stale against them, or if a finding specifically requires full-doctrine text the kit's Scope Boundary says it doesn't carry.
2. Verify the canonical Ethical Anchor string from the kit (or File_Template.md if fetched): `Attempt to do no harm. Defer to Ethical_Constraints.md if present.`
3. Sweep Challenges/ (list via GitHub contents API if available, otherwise known ten files) and Architecture/Chemistry.md.
4. Open Admin/Governance_Charter.md, Admin/CIR_Gov.md, Admin/Autonomy_Divergence_Protocol.md, Admin/Progress_Log.md, Admin/Auditor_Protocols.md, Admin/Repository_Integrity_Protocol.md when checking disputes / ratification.
5. Check Active Disputes and any open unknown IDs declared in File State against Unknowns.md Active Index / Active Disputes Registry (parity gaps are Major if an open dispute or open sidecar ID is missing from Unknowns).
6. For any file's File State "Open Unknowns" count, don't just trust the header number — count the sidecar's own non-Resolved entries directly (Open + In Progress) and compare. A mismatch here is a real finding even when every individual ID is correctly registered elsewhere — it means the count itself is stale, not that anything is missing.
7. For any file with its own "Last Reviewed"/"Last Audit" field, check that field's date against the newest dated entry in the file's own body (Current Lessons, Resolution Log, etc.). A body entry dated more recently than the header is a header-lag finding, worth surfacing even when nothing else is wrong.
8. Check Unknowns.md's own Dependency Cluster trees for the same class of staleness: an ID drawn as a live blocker in a cluster diagram while the Active Index shows it Resolved is a real finding (cross-reference the owning file before reporting — confirm the closure is genuine and ratified, not just that the Active Index says so). Never report a cluster ID as "live" or "resolved" from the cluster tree text alone — always open the owning sidecar (or Unknowns Active Index status) before grading.
9. Note freshness strings (Routing Last updated, Unknowns version, Discovery Last updated/Version if any).
10. List what changed in the last 3 days (GitHub commits API since window start if available; otherwise dated body text in opened files).
11. List Blocking/Critical unknowns from Unknowns.md watches; only claim sidecar parity for files actually opened.
12. Open Maintenance tasks: limited, concrete, with raw URLs.

Report structure (keep this shape):
- Integrity Findings (Major first, then Constitutional/Ethical Anchor result, identity/V0 note)
- Every file checked table (HTTP, Ethical Anchor, registration/File State notes)
- Freshness Statement
- What Changed (last 3 days)
- Ratification Queue (Active Disputes / unratified status)
- Blocking/Critical Unknowns (from Unknowns + cross-check only for opened owners)
- File Promotion Status (from Discovery / own File State)
- High-Risk Modules
- Open Maintenance Tasks (numbered, actionable, with URLs)

Honesty rules:
- No Major for V0 alias if content is LazarusForge Routing family.
- No sidecar parity claims for files not opened.
- Do not invent version bumps or close unknowns.
- Grade index/dispute parity failures as Major when an owning file says Open and Unknowns does not list it.
- Grade a File State count mismatch (step 6) as a mechanical note, not Major, unless it also hides a missing-ID parity failure.
- Grade a Dependency Cluster staleness finding (step 8) as a mechanical note, not Major, and never report a cluster ID as "live" or "resolved" without checking the owning file directly first.
- Prefer mechanical facts and raw URLs over interpretation.

End with a one-paragraph bottom line: constitutional clean? biggest real finding? suggested next 1–3 edits.

================================================================

---

## Resolution Log

- 2026-08-30: v1.0.1 — two small hardening edits, both Grok-proposed after reviewing v1.0 against a live run, both accepted without modification: (1) the V0 legacy-alias line now glosses explicitly that it's a historical repo name, not a project version, to prevent a future reader from misreading the identity check as a version check; (2) step 8's Dependency Cluster staleness check gained an explicit instruction never to grade an ID as live/resolved from the cluster tree text alone — always open the owning sidecar or Unknowns Active Index first. Grok's third suggestion (promoting Status from Draft to "Active — Operational Template") held pending confirmation the automation is actually pulling from this file rather than a hand-copied config; not applied here.
- 2026-08-30: v1.0 — first draft, human-directed. Prompt text itself was not newly written here; it was iteratively refined across several live morning-audit sessions run through an external automation surface (Grok), with three rounds of correction made directly by the human governing authority in response to real findings from those runs: (1) point step 1 at `Admin/Forge_Audit_Kit.md` rather than fetching `Admin/Auditor_Protocols.md`/`Admin/File_Template.md` directly, cutting daily fetch volume by roughly 6x; (2) step 6, a File-State-count-vs-sidecar cross-check, added after a real RIP Open Unknowns miscount (9 claimed vs 8 actual) that ID-presence-only parity checking would not have caught; (3) step 7, a header-vs-body freshness check, added after a real Progress_Log Last Reviewed lag against its own body. Step 8 (Dependency Cluster staleness) added in this draft based on a fourth live finding the same day this file was created — a kit-sourced audit run correctly caught a second instance of the same cluster-tree staleness class already fixed once in `Unknowns.md` v4.87 (Trust & Integrity: GOV-003/SEC-007a) recurring in a different cluster (Safety-Critical: WA-002/PL-001) — worth naming as its own repeatable check rather than treating each recurrence as a one-off. This file's own existence is itself a response to a stated operational constraint: manual copy-paste into the automation's config has a roughly 100KB device-side limit, and the prompt text is well under that, but keeping it live only inside the automation's own config screen meant it couldn't be diffed, versioned, or recovered independently — the same class of problem this repository already solved for doctrine files with a git history, applied here to an operational asset instead.
