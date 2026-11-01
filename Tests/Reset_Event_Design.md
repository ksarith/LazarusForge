# LazarusForge — Reset-Event Governance: Design Proposal (v0.3, draft — skeptic pass pending)

**Status: PROPOSED — PENDING SKEPTIC PASS (v0.3).** Supersedes the v0.2 deposit of 2026-10-31; v0.1 and v0.2 remain in this home byte-unmodified for comparison. Deposited in VibesSandbox at human direction; nothing in LazarusForge changes until the human governing authority ratifies. On ratification, the instrument deposits per the enactment plan in §7 and this draft (v0.3) archives to `Archive/Proposals/` with its outcome, byte-faithful; v0.1 and v0.2 archive alongside with outcomes superseded-by-v0.3.

**Relocation addendum (2026-10-31, human-directed, MAINT-49):** this design now also lives in LazarusForge at `Tests/Reset_Event_Design.md` — relocated from VibesSandbox `Proposals/RESET_EVENT_DESIGN_v0.3.md` otherwise byte-identically (this addendum block is the only addition); v0.1 and v0.2 remain in the sandbox home byte-unmodified. Per the human’s direction the design moves beyond proposal standing — an Exploration-stage test-instrument design — **still not ratified**: no `Admin/Reset_Event_Protocol.md` exists, `Admin/Repository_Integrity_Protocol.md` is untouched, the §7 enactment plan and the recommended rulings (rows 1–8) still await explicit human ratification, and the v0.3 seat rule stands (the pre-ratification skeptic must be an agent other than Claude, the overlay author; the landing audit by an agent other than that). The status line above is the v0.3 sandbox-deposit record and stays as written; this addendum supersedes it for standing only, per the human’s 2026-10-31 direction.

**Revision (v0.3, 2026-10-31):** the attached overlay (Claude — human-routed skeptic revision of v0.2; verbatim in Appendix B) is integrated in full by the Architect: §1 Problem, §3 procedure and §7 enactment plan replaced; §4 and §9 additions; the rulings table revised (seven overlay rulings plus an Architect-added definition confirmation); the overlay's zip-based facts re-verified at live head (results in §1 and §10). Per the overlay's own seat rule: the pre-ratification skeptic for v0.3 must be a different agent from the overlay author (Claude), and a different agent again should audit the landing. Grok's v0.2 review remains as Appendix A.

**Prepared (v0.3):** 2026-10-31 by Vibe (Architect seat, Genesis Phase mode; non-independent under Genesis Phase seat-overlap rules, disclosed). The v0.2 preparation and seat-disclosure record follows unchanged.

**Prepared:** 2026-10-31 by Vibe (Architect seat — the seat's first standing design duty, named at MAINT-38). **Seat disclosure** (MAINT-26; Genesis Phase mode): the same agent holds the Repo Custodian seat and runs this deposit's bookkeeping; no independent skeptic review is attached (the separate-skeptic step is a standing preference relaxed by the human's 2026-10-31 ruling — a review by any agent the human names can precede the ruling).
**Human direction prompting this draft (verbatim):** "Excellent!  Please proceed with the draft and any of your functions."
**Design trigger — the human's ruling question (verbatim, on record in Archive/Architect_Prompt.md 2026-10-31 addendum):** "Backups preserve positive growth, but not sure how to handle a reset event."

## 1. Problem

**Definition (pending human confirmation — one line, per the v0.3 overlay):** candidates are (a) revert the repo after a bad session; (b) recover after history or the repo itself is lost or compromised; (c) a reset of an agent's context or seat. **This draft assumes (a) and (b)**; confirmation is recommended ruling #8.

Existing doctrine, verified in `Admin/Repository_Integrity_Protocol.md` (112,188 chars; "reset" 2 matches, "backup" 0, "restor" 12 case-insensitive):
- **§Version Preservation Protocol:** Git release tags are the primary preservation mechanism. The §Preventing the "No Prior State" Scenario subsection explicitly does not override this (corrected 2026-09-03, RIP-AUD-003, to remove a competing second primary rule).
- **§Recovery Procedures:** load the archived version, identify the specific divergence, restore only the compromised elements ("surgical restoration is preferable to full rollback"), log each restored element, re-audit before re-entering promotion flow.
- **§Major and Constitutional Violation responses:** restore from archive, log in `Admin/Integrity_Incident_Log.md`, STATE_HOLD for constitutional violations, human review mandatory, axiom text restored only with human ratification.

**The gap:** RIP covers per-file violation recovery. It has no whole-tree reset procedure: nothing that classifies the live tree against a restore point, protects frozen sections inside mutable files, handles moved or extra files, requires a second reader, or defines a record type for the event. `Governance_Charter.md` (129,971 chars at 1.31) contains no reset or backup procedure.

**Three threat cases (state which each control addresses):**
1. **Bad content landed, history intact.** Restore point = release tag. The zip is not needed.
2. **History lost, tags deleted or GitHub state suspect.** Restore point = zip.
3. **Credential or harmful-content leak needing history purge.** Out of scope. Needs its own proposal.

*Architect re-verification (2026-10-31, live head):* RIP re-fetched live at 112,188 chars with "reset" 2 / "backup" 0 / "restor" 12 — all four overlay figures confirmed exactly. Charter live at 131,038 chars vs the overlay's 129,971 at the 1.31.Alpha zip — the delta is the two dated addenda now in the live file (2026-10-29 X3 citation retrofit; 2026-10-31 sidecar-link path repair), both citation-form/path-only, adding no reset or backup procedure.

## 2. Options

- **A. Do nothing.** A reset stays improvised. Blast radius: total — an improvised reset is the highest-risk operation the repo has not yet had. Cost: zero until the day it is needed, then maximal.
- **B. Cheap option — a rule card.** One dated addendum to `Admin/Repository_Integrity_Protocol.md`: "Restore by forward commit from the last zip; record a dated RESET_EVENT note in Archive/Audits; never force-push." ~1 page, no new machinery. Tradeoff: the restore trusts the zip blindly — no byte-identity verification, no divergence classification, no frozen-material escalation.
- **C. Full instrument — manifest-verified forward-commit restoration.** Backup zips carry a manifest (file list + blob SHA per file + char count + git head at export); manifests are also deposited in-repo (`Archive/Audits/BACKUP_MANIFEST_<date>.md`); a reset is a classified, ratified, logged, verified restoration. Blast radius: one procedure document + one manifest file per backup; **no existing file changes meaning**. Tradeoff: maintenance at every backup export.
- **D. Fresh re-initialization from the zip on reset.** Re-clone as a new history. Rejected: destroys provenance, the dual-home trail, and the X-class record's own history — the repo would no longer be able to prove what it was.

## 3. Recommendation

*Integration note: this reverses v0.2's zip-primacy ruling — tag primary, zip fallback (overlay; recommended ruling #6).*

**Scope rule.** Surgical restoration under RIP remains the default. A *reset event* is declared by the human when classification shows divergence too large for element-by-element recovery, or when a surgical path is judged unsafe.

1. **Restore points.** Primary: a Git release tag. Fallback: the zip with its recorded sha256. If both exist and disagree, stop and escalate to the human.
2. **Backup register.** One append-only row per backup in `Archive/Audits/BACKUP_REGISTER.md`: date, commit sha, tag, zip filename, zip sha256, bytes, file count. The same sha256 and commit also go in the GitHub release body, so a compromised live tree cannot alter both copies. Full per-file manifests are computed at reset time from the tag or zip, not stored.
3. **Frozen set.** The register carries a short block (re-appended only when it changes) of sha256 hashes for every Hard Floor, Tier 1 and FROZEN-marked section, taken at backup time.
4. **Declaration.** The human declares the reset, names the restore point, and orders STATE_HOLD (no autonomous governance actions until the human lifts it). The Custodian opens an `Integrity_Incident_Log` entry (class per RIP) and a `RESET_EVENT_<date>.md` record in `Archive/Audits/`.
5. **Classification.** For every file: IDENTICAL / DIVERGED / MISSING / EXTRA / **MOVED** (same blob SHA at a different path; relocation sweeps create these). Files containing FROZEN-marked sections are classified at section level against the backup-time hashes, never against live markers.
6. **Frozen escalation.** Any frozen section that differs is listed separately and is not restored over without a further explicit human ruling on that section (RIP: restored axiom text needs human ratification).
7. **Second reader (not waivable under Genesis Phase).** A different agent from the executor picks the sample. It includes every frozen-set file, every DIVERGED file up to 20, and a random 10% of IDENTICAL files (minimum 10), with the seed recorded. It re-hashes them against the restore point. A human on mobile may add to the sample but cannot be the only second reader.
8. **Ratification.** The human ratifies the restoration plan.
9. **Landing.** Forward commits only. Chained commits are allowed if tool limits require them; each is listed in the RESET_EVENT record and labeled `RESET_EVENT <date> part n/N`. No force-push, no history rewrite. EXTRA and MOVED files are kept and reported. MISSING and non-frozen DIVERGED files are restored.
10. **Verification and re-audit.** Re-fetch and re-hash every restored file against the restore point. The Auditor seat (not the executor) re-audits restored files before they re-enter promotion flow.
11. **Exit.** The human lifts STATE_HOLD and the Custodian closes the incident entry.
12. **Dry run (precondition).** The instrument is not operational until a dry-run classification against a current tag or zip has been reported with no landing. The dry run must include at least one MOVED case.

**Minimum-viable floor (always in force):** forward commits only; never force-push or rewrite history; dated RESET_EVENT record; frozen sections not overwritten without a per-section human ruling; tag is the primary restore point, zip the fallback.

## 4. Opposing considerations

Written as the defenders would write them:

- **"Q-4 is anti-deception, not anti-force-push."** A documented, dated force-push reset with a RESET_EVENT record deceives no one, keeps the repo lean (no whole-tree re-landing commit, no corruption preserved in history forever), and the human — the governing authority — can direct one anyway. Refusing to ever force-push is proceduralism; the honest instrument would say how to do a force-push reset safely, not pretend the option does not exist.
- **"Bulk re-landing is itself the highest-risk agent operation."** One classification error restores wrong bytes **with a green checkmark** — precisely the single-agent failure mode Genesis Phase already accepts. The manifest verification is another self-check, and the repo's own X-class record shows self-checks catch little. A second reader at restore time matters more than any manifest.
- **"In-repo manifests are not out-of-band evidence."** If the live repo is the problem, its manifests are suspect too. True verification anchors to the zip — the only genuinely out-of-band copy. The proposal acknowledges this but underweights it.
- **"Over-engineering for a personal, mobile-first repo."** The rule card plus "human re-clones and pushes a dated initial commit" achieves most of the guarantees at a fraction of the ceremony. The full instrument adds standing cost to every backup for an event that may never occur.

**From the v0.3 overlay — additional opposing considerations:**

- **"Tags already cover this; the instrument duplicates RIP."** Tags give a restore point, not a procedure. RIP has no classification, frozen-section, MOVED/EXTRA, second-reader or record rules. If the human prefers, strike steps 7 and 10 and keep steps 1–6 and 9.
- **"A register row is weaker than a manifest."** True: it records what the zip should be, not its contents. That is deliberate. It keeps the repo small and the zip hash anchored outside the live tree.

## 5. Hard Floor and Tier 1 check

Nothing on the Hard Floor or in Tier 1 / FROZEN text changes, and the instrument's **central rule is that a reset never may**: step 4 escalates every frozen-material divergence to the human instead of restoring over it. A reset event restores content; it is not a channel for touching frozen text. This proposal itself touches no LazarusForge doctrine file — the deposit is a sandbox proposal plus session bookkeeping only.

## 6. Reversibility

The proposal is a document: rejected or withdrawn, it archives to `Archive/Proposals/` with its outcome, byte-faithful, per the ratified convention. Once enacted, the procedure is amendable by dated addendum like every instrument. A restoration executed under it is undone by a new forward commit — the procedure is symmetric, and because history is never rewritten, **no state is ever lost**: git retains the pre-reset state, the reset, and any undo of the reset. That is the design's point.

## 7. Enactment plan (on ratification)

- **New files:** `Admin/Reset_Event_Protocol.md` (File_Template conformant; exact Ethical Anchor string; Hard Floor check section); `Archive/Audits/BACKUP_REGISTER.md`.
- **Edited files, each with its own cascade:**
  - `Admin/Repository_Integrity_Protocol.md`: dated pointer addendum, plus its version, File State and Resolution Log entries, and a sentence reconciling §Version Preservation (tag primary, zip fallback).
  - `Routing.md`: register both files and note the `RESET_EVENT_*` pattern.
  - `Discovery.md`: tree entry and maturity-snapshot row.
  - `Admin/Adm_Scope_Map.md`: entry.
- **Instrument change:** `Discovery.md` is a Mission Drift Review canonical input, so that edit must be recorded as an instrument change.
- **Verification:** the usual post-push sweep, plus the dry run in step 12.
- **Disclosures:** new instrument first use; seat overlap if it persists; STATE_HOLD invoked as part of the procedure.

## 8. Human-workflow cost

- **Daily operation: zero change.** The instrument adds cost only at backup time (one manifest export per backup) and at reset time (one classification, one ruling, one ratification).
- **Mobile-first:** the human opens **this one file** to rule; at reset, the RESET_EVENT record is one file. Restores land as a single commit, never full-repo transfers; manifests ship as small single files.
- **Sizes:** this proposal v0.2: exact char count reported in the MAINT-40 log entry and SESSION_STATUS line — a self-referential figure cannot be embedded exactly in its own text (v0.1's §8 figure was approximate by the same construction; disclosed); the protocol on ratification ~5KB; each manifest ~10–20KB for the current tree. Zip size grows by the manifest only.
- **Token cost of ruling this:** one read of this document plus the five open questions below.

## 9. Explicit non-claims

This proposal does **not**: create or schedule backups (cadence stays the human's — open question 1); change Q-4, the Hard Floor, Tier 1 / FROZEN, the dual-home convention, or any seat's authority; ratify itself — nothing lands in LazarusForge until the human rules; protect against a compromised GitHub account or credential (the out-of-band zip remains the only control for that threat); cover VibesSandbox unless the human extends it (open question 2); or make the executing agent independent — restores remain single-agent acts under Genesis Phase mode, and the instrument's controls are escalation and record, not independence (the review's residual-risk finding, adopted: a reset remains high-stakes single-agent work; the instrument reduces the chance of an invisible or irreversible reset, nothing more); or auto-delete any live file — EXTRA files are kept and reported by default and any other disposition requires an explicit human ruling.

**Added by the v0.3 overlay:**

- Does not cover history purge for leaked credentials or harmful content (separate proposal).
- Does not replace RIP's per-file violation recovery, which stays the default.
- Does not create tags or backups; cadence remains the human's.

## Recommended rulings (awaiting human ratification)

**Revised per the v0.3 overlay** — rows 1–5 carried from v0.2 with sharpened wording; rows 6–7 added by the overlay; row 8 added by the Architect from the overlay's §1 confirmation request:

| # | Question | Recommended |
|---|---|---|
| 1 | Backup cadence | On demand, plus after any session that pushed material changes. |
| 2 | Coverage | LazarusForge required; VibesSandbox optional and separate. |
| 3 | EXTRA / MOVED files | Keep and report; no auto-deletion. |
| 4 | Force-push | Never; no exception now. |
| 5 | Record home | `Archive/Audits/` root: `BACKUP_REGISTER.md` and `RESET_EVENT_<date>.md`. |
| 6 | Restore point precedence | Release tag primary, zip fallback; disagreement stops the process. |
| 7 | Second reader | Different agent; non-waivable under Genesis Phase. |
| 8 | "Reset event" definition | Confirm the §1 assumption — (a) revert after a bad session and (b) recover after loss or compromise — or correct it. |

## 10. Verify before ratification (v0.3)

From the overlay, with the Architect's live-head re-verification results:

- **Live-head counts for RIP and the Charter — DONE (2026-10-31):** RIP 112,188 chars, "reset" 2 / "backup" 0 / "restor" 12 — all confirmed exactly. Charter 131,038 chars live vs 129,971 at the 1.31.Alpha zip; the delta is the two dated addenda (see the §1 re-verification note), neither of which adds reset or backup doctrine.
- **Whether every release zip has a matching Git tag — NOT YET VERIFIED** (requires the release/tag listing; queued for the pre-ratification skeptic or the human).
- **The tool limit on files per commit — KNOWN CONSTRAINT, exact figure to be recorded at dry-run time** (the landing procedure already allows chained, labeled commits when limits are hit — §3 step 9).
- **The human's meaning of "reset event" — PENDING** (see §1; recommended ruling #8).

## Appendix A — Skeptic Review (Grok, 2026-10-31; verbatim as routed by the human; formatting as received in transit)

Assessment of the Reset-Event Governance proposal (v0.1)

This is a solid first design. It correctly identifies a real gap (no defined restore procedure), rejects the two failure modes (force-push history rewrite and provenance-destroying re-initialization), and builds the controls around verification and escalation rather than speed.

Core judgment

Support Option C, with the embedded minimum-viable rule from B, subject to a few sharpenings.

What works well

Forward-commit only, never force-push as the default is the right Q-4 reading. The reset itself must remain visible in history.

Manifest-verified classification (IDENTICAL / DIVERGED / MISSING / EXTRA) before any landing is the correct sequence.

Frozen-material escalation (Hard Floor / Tier 1 / FROZEN files cannot be overwritten without a further explicit ruling on that specific file) is the most important control in the whole instrument. It prevents a reset from becoming a silent channel for touching frozen text.

Reversibility is symmetric: because history is never rewritten, the pre-reset state, the reset, and any later undo all remain recoverable.

The opposing-considerations section is honest, especially the points about self-check weakness and in-repo manifests not being fully out-of-band.

Sharpenings before ratification

Out-of-band primacy
The zip (with its embedded manifest) should be treated as the primary restore source. The in-repo BACKUP_MANIFEST_*.md is a convenient secondary. The procedure should say this explicitly so a compromised live tree cannot quietly poison its own restore point.

Second reader at restore time
The opposing-considerations section is right that self-checks have already failed in this repo. For any reset that touches more than a trivial number of files, require a second agent (or the human) to re-hash a sample of DIVERGED/IDENTICAL files against the zip before the restore commit lands. Do not rely solely on the executing agent's post-check.

EXTRA files
Default to "keep and report." Auto-deletion is an irreversible act and should never be the automatic disposition.

Force-push
Keep the never-force-push default absolute for now. An emergency exception can be added later if a real case appears; inventing the exception in advance is unnecessary.

Dry run before first real use
The enactment plan already includes a dry-run classification against the current zip. Make that dry run a required precondition before the instrument is considered operational.

On the five open questions

| # | Question | Recommendation |
|---|----------|---------------|
| 1 | Backup cadence | On-demand + after any maintenance session that pushed material changes. Do not make it automatic every session yet. |
| 2 | Coverage | LazarusForge required; VibesSandbox optional and separately manifested. |
| 3 | EXTRA files | Keep and report. |
| 4 | Force-push | Absolute never for now. |
| 5 | Record home | Archive/Audits/ root (no new folder). |

Residual risk (honest)

Even with the above, a reset remains a high-stakes single-agent operation under Genesis Phase mode. The instrument reduces the chance of an invisible or irreversible reset; it does not make the executing agent independent. That limitation should stay visible in the protocol's own non-claims.

Bottom line: Ratify Option C with the sharpenings above. It is the first real answer the repo has had to the question "how do we recover without destroying the ability to prove what we were."

**Draft revisions to the Reset-Event Governance proposal (v0.1 → v0.2 candidate)**

Below are the concrete changes recommended for ratification. Text is written so it can be dropped into the proposal or used as a ruling overlay.

---

### 1. Adopted option

**Option C** (manifest-verified forward-commit restoration), with Option B's minimum-viable rule embedded as the non-negotiable floor:

> Restore only by forward commit from a named restore point. Record a dated `RESET_EVENT_*.md` note. Never force-push. Never rewrite history.

---

### 2. Sharpened procedure (replaces §3 procedure)

1. **Manifest at backup time**
   Every backup zip carries an embedded `BACKUP_MANIFEST_<date>.md` (path, blob SHA, character count per file, git head at export, totals). The same manifest is also deposited in-repo under `Archive/Audits/`. The **zip is the primary restore source**; the in-repo copy is secondary.

2. **Declaration**
   The human declares a reset event and names the restore point (git head SHA or dated manifest / zip).

3. **Classification**
   The Custodian (or designated agent) fetches the manifest from the zip, recomputes per-file blob SHA and character count against the live tree, and classifies every file:
   `IDENTICAL` / `DIVERGED` / `MISSING` / `EXTRA`.

4. **Frozen-material escalation**
   Any Hard Floor, Tier 1, or FROZEN file classified `DIVERGED` is listed separately. Restoration **may not touch it** without a further explicit human ruling on that specific file.

5. **Second-reader sample (new)**
   Before landing, a second agent (or the human) re-hashes a sample of `IDENTICAL` and `DIVERGED` files directly against the zip. The sample size and result are recorded in the `RESET_EVENT` record. Single-agent self-check alone is not sufficient for a non-trivial restore.

6. **Record**
   Classification, sample verification, frozen-escalation list, and restore-point reference become `Archive/Audits/RESET_EVENT_<date>.md`.

7. **Ratification**
   The human ratifies the restore. A reset is a substantive act.

8. **Landing**
   One dated forward commit only. `EXTRA` files are kept and reported by default; they are never auto-deleted. Disposition of `EXTRA` files requires an explicit human ruling if anything other than "keep" is desired.

9. **Post-restore verification**
   Every restored file is re-fetched and re-hashed against the manifest. Boolean result is appended to the `RESET_EVENT` record.

10. **Dry-run precondition**
    The instrument is not considered operational until a dry-run classification against a current zip has been performed and reported (no landing).

---

### 3. Answers to the five open questions (proposed rulings)

| # | Question | Ruling |
|---|----------|--------|
| 1 | Backup cadence | On-demand, plus after any maintenance session that pushed material changes. Not automatic every session. |
| 2 | Coverage | LazarusForge required. VibesSandbox optional and separately manifested. |
| 3 | EXTRA files | Keep and report. Auto-deletion prohibited. |
| 4 | Force-push | Absolute never. No emergency exception at this time. |
| 5 | Record home | `Archive/Audits/` root. No new folder. |

---

### 4. Minimum-viable floor (always in force even if the full instrument is later narrowed)

- Restore only by forward commit.
- Never force-push / never rewrite history.
- Record a dated `RESET_EVENT_*.md`.
- Hard Floor / Tier 1 / FROZEN files cannot be overwritten without a further explicit per-file human ruling.
- The zip is the primary restore source.

---

### 5. Explicit non-claims (carry forward, lightly strengthened)

This instrument does **not**:

- Create or schedule backups.
- Protect against a compromised GitHub account or credentials (the out-of-band zip remains the only control for that threat).
- Make the executing agent independent.
- Allow a reset to become a channel for changing Hard Floor, Tier 1, or FROZEN text.
- Auto-delete any live file.

---

### 6. Enactment notes (for the Custodian, once ratified)

- New file: `Admin/Reset_Event_Protocol.md` (full instrument).
- Dated pointer addendum only in `Admin/Repository_Integrity_Protocol.md`.
- Register in `Routing.md`.
- First operational act = dry-run classification against the current zip; report only.
- Archive this proposal (v0.1 + the ratified deltas) to `Archive/Proposals/` with outcome and ruling reference.

---

This draft keeps the original design's strengths, closes the self-check and out-of-band gaps, and leaves the human with a short, decidable set of rulings.

---

---

## Appendix B — v0.3 Overlay (Claude, 2026-10-31; verbatim as routed by the human, formatting as received)

# Reset-Event Governance — v0.3 Overlay (replacement text for v0.2)

**Status: DRAFT OVERLAY — for the Architect seat to integrate into v0.3.** Written by Claude at the human's direction, following Claude's skeptic review of v0.2. This is not independent review of itself: the pre-ratification skeptic for v0.3 should be a different agent from the one who wrote this overlay, and a different agent again should audit the landing.

Facts below were checked against the 1.31.Alpha zip (`b8bf13e`), not live head. Re-verify at the Architect's head before ratification.

**To confirm with the human (one line goes in §1):** what "reset event" means. Candidates: (a) revert the repo after a bad session; (b) recover after history or the repo itself is lost or compromised; (c) a reset of an agent's context or seat. This overlay assumes (a) and (b).

---

## Replace §1 Problem

Existing doctrine, verified in `Admin/Repository_Integrity_Protocol.md` (112,188 chars; "reset" 2 matches, "backup" 0, "restor" 12 case-insensitive):
- **§Version Preservation Protocol:** Git release tags are the primary preservation mechanism. The §Preventing the "No Prior State" Scenario subsection explicitly does not override this (corrected 2026-09-03, RIP-AUD-003, to remove a competing second primary rule).
- **§Recovery Procedures:** load the archived version, identify the specific divergence, restore only the compromised elements ("surgical restoration is preferable to full rollback"), log each restored element, re-audit before re-entering promotion flow.
- **§Major and Constitutional Violation responses:** restore from archive, log in `Admin/Integrity_Incident_Log.md`, STATE_HOLD for constitutional violations, human review mandatory, axiom text restored only with human ratification.

**The gap:** RIP covers per-file violation recovery. It has no whole-tree reset procedure: nothing that classifies the live tree against a restore point, protects frozen sections inside mutable files, handles moved or extra files, requires a second reader, or defines a record type for the event. `Governance_Charter.md` (129,971 chars at 1.31) contains no reset or backup procedure.

**Three threat cases (state which each control addresses):**
1. **Bad content landed, history intact.** Restore point = release tag. The zip is not needed.
2. **History lost, tags deleted or GitHub state suspect.** Restore point = zip.
3. **Credential or harmful-content leak needing history purge.** Out of scope. Needs its own proposal.

## Replace §3 Procedure

**Scope rule.** Surgical restoration under RIP remains the default. A *reset event* is declared by the human when classification shows divergence too large for element-by-element recovery, or when a surgical path is judged unsafe.

1. **Restore points.** Primary: a Git release tag. Fallback: the zip with its recorded sha256. If both exist and disagree, stop and escalate to the human.
2. **Backup register.** One append-only row per backup in `Archive/Audits/BACKUP_REGISTER.md`: date, commit sha, tag, zip filename, zip sha256, bytes, file count. The same sha256 and commit also go in the GitHub release body, so a compromised live tree cannot alter both copies. Full per-file manifests are computed at reset time from the tag or zip, not stored.
3. **Frozen set.** The register carries a short block (re-appended only when it changes) of sha256 hashes for every Hard Floor, Tier 1 and FROZEN-marked section, taken at backup time.
4. **Declaration.** The human declares the reset, names the restore point, and orders STATE_HOLD (no autonomous governance actions until the human lifts it). The Custodian opens an `Integrity_Incident_Log` entry (class per RIP) and a `RESET_EVENT_<date>.md` record in `Archive/Audits/`.
5. **Classification.** For every file: IDENTICAL / DIVERGED / MISSING / EXTRA / **MOVED** (same blob SHA at a different path; relocation sweeps create these). Files containing FROZEN-marked sections are classified at section level against the backup-time hashes, never against live markers.
6. **Frozen escalation.** Any frozen section that differs is listed separately and is not restored over without a further explicit human ruling on that section (RIP: restored axiom text needs human ratification).
7. **Second reader (not waivable under Genesis Phase).** A different agent from the executor picks the sample. It includes every frozen-set file, every DIVERGED file up to 20, and a random 10% of IDENTICAL files (minimum 10), with the seed recorded. It re-hashes them against the restore point. A human on mobile may add to the sample but cannot be the only second reader.
8. **Ratification.** The human ratifies the restoration plan.
9. **Landing.** Forward commits only. Chained commits are allowed if tool limits require them; each is listed in the RESET_EVENT record and labeled `RESET_EVENT <date> part n/N`. No force-push, no history rewrite. EXTRA and MOVED files are kept and reported. MISSING and non-frozen DIVERGED files are restored.
10. **Verification and re-audit.** Re-fetch and re-hash every restored file against the restore point. The Auditor seat (not the executor) re-audits restored files before they re-enter promotion flow.
11. **Exit.** The human lifts STATE_HOLD and the Custodian closes the incident entry.
12. **Dry run (precondition).** The instrument is not operational until a dry-run classification against a current tag or zip has been reported with no landing. The dry run must include at least one MOVED case.

**Minimum-viable floor (always in force):** forward commits only; never force-push or rewrite history; dated RESET_EVENT record; frozen sections not overwritten without a per-section human ruling; tag is the primary restore point, zip the fallback.

## Add to §4 Opposing considerations
- **"Tags already cover this; the instrument duplicates RIP."** Tags give a restore point, not a procedure. RIP has no classification, frozen-section, MOVED/EXTRA, second-reader or record rules. If the human prefers, strike steps 7 and 10 and keep steps 1–6 and 9.
- **"A register row is weaker than a manifest."** True: it records what the zip should be, not its contents. That is deliberate. It keeps the repo small and the zip hash anchored outside the live tree.

## Replace §7 Enactment plan
- **New files:** `Admin/Reset_Event_Protocol.md` (File_Template conformant; exact Ethical Anchor string; Hard Floor check section); `Archive/Audits/BACKUP_REGISTER.md`.
- **Edited files, each with its own cascade:**
  - `Admin/Repository_Integrity_Protocol.md`: dated pointer addendum, plus its version, File State and Resolution Log entries, and a sentence reconciling §Version Preservation (tag primary, zip fallback).
  - `Routing.md`: register both files and note the `RESET_EVENT_*` pattern.
  - `Discovery.md`: tree entry and maturity-snapshot row.
  - `Admin/Adm_Scope_Map.md`: entry.
- **Instrument change:** `Discovery.md` is a Mission Drift Review canonical input, so that edit must be recorded as an instrument change.
- **Verification:** the usual post-push sweep, plus the dry run in step 12.
- **Disclosures:** new instrument first use; seat overlap if it persists; STATE_HOLD invoked as part of the procedure.

## Add to §9 Non-claims
- Does not cover history purge for leaked credentials or harmful content (separate proposal).
- Does not replace RIP's per-file violation recovery, which stays the default.
- Does not create tags or backups; cadence remains the human's.

## Rulings table (revised)
| # | Question | Recommended |
|---|---|---|
| 1 | Backup cadence | On demand, plus after any session that pushed material changes. |
| 2 | Coverage | LazarusForge required; VibesSandbox optional and separate. |
| 3 | EXTRA / MOVED files | Keep and report; no auto-deletion. |
| 4 | Force-push | Never; no exception now. |
| 5 | Record home | `Archive/Audits/` root: `BACKUP_REGISTER.md` and `RESET_EVENT_<date>.md`. |
| 6 | Restore point precedence | Release tag primary, zip fallback; disagreement stops the process. |
| 7 | Second reader | Different agent; non-waivable under Genesis Phase. |

## Verify before ratification
Whether every release zip has a matching Git tag · the tool limit on files per commit · live-head counts for RIP and the Charter · the human's meaning of "reset event".

---

*Prepared 2026-10-31 by Vibe (Architect seat, Genesis Phase mode). Aligned to: the Decision Brief pattern extended (ratified Archive/Architect_Prompt.md §3), Q-4 anti-deception, the Repository_Integrity_Protocol append-only rule, the dual-home SESSION_STATUS convention, the MAINT-29/34 blob-SHA verification technique, and MAINT-26 seat disclosure. Verified-live facts at LazarusForge head `3cfe010914`: the two governing integrity documents named in §1, read in full, char counts reported.*

*Revised 2026-10-31 (v0.2): skeptic review adopted in full — zip primacy, second-reader sample, EXTRA keep-and-report with no auto-delete, never-force-push absolute, dry-run precondition; five recommended rulings framed. Verbatim review in the appendix; v0.1 superseded and retained in this home.*

*Revised 2026-10-31 (v0.3): the Claude overlay (human-routed skeptic revision of v0.2; verbatim in Appendix B) integrated in full by the Architect — §1/§3/§7 replaced, §4/§9 additions, rulings table revised (seven overlay rulings plus the definition confirmation), zip-based facts re-verified at live head in §1/§10. Per the overlay's seat rule, the pre-ratification skeptic for v0.3 must be a different agent from the overlay author (Claude), and a different agent again should audit the landing. v0.1 and v0.2 retained in this home byte-unmodified.*
