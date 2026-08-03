# BATTERY_SEED.md
**Version 1.0**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | N/A — operational prompt template, not a doctrine or specification claim |
| Verification Ref | Admin/Auditor_Protocols.md §Adversarial Challenge Battery, AP-017 |
| Last Audit     | 2026-08-02                                                          |
| Auditor        | Claude — Synthesizer/Auditor, human-directed, first draft, 2026-08-02 |
| Open Unknowns  | 0 — tracked at Admin/Auditor_Protocols.md AP-017 (mechanism-level, not template-level) |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.32 §Adversarial Challenge Battery and AP-017's Resolution Path (`Archive/Logs/Auditor_Protocols_Logs.md`).
When this file contradicts that source, the source document prevails.

---

## Scope Boundary

**DOES define:** The frozen prompt block a `cold_session_bundler.py` payload should carry as its `standard_audit_prompt` when the goal is a genuine AP-017-qualifying instance (a full ten-class Adversarial Challenge Battery, not general review); the operator checklist for running one; the additional target-file list required when the audit's subject is `Admin/Auditor_Protocols.md` itself.

**DOES NOT define:** AP-017's closure bar itself (→ `Archive/Logs/Auditor_Protocols_Logs.md` AP-017 — this file supplies instances toward that bar, it doesn't set it) · the Battery's ten class definitions (→ `Admin/Auditor_Protocols.md` §Adversarial Challenge Battery) · `cold_session_bundler.py`'s stripping/manifest mechanics (→ that module).

---

## Why This Exists

`Automation/cold_session_bundler.py` already refuses to construct a session carrying prior findings — that part of informational independence is solid and code-enforced. But its `DEFAULT_STANDARD_AUDIT_PROMPT` is intentionally general ("evaluate the material on its own terms... identify unsupported claims, internal inconsistencies...") — it produces broad reviewer output, not a structured, class-by-class Adversarial Battery with the concrete-scenario minimum each class requires. Every AP-017 instance logged to date that used the bundler's default prompt produced real, useful findings, but not in a form directly creditable against the Battery's own ten-class structure. This file exists so an operator constructing a bundle for an AP-017 attempt can pass a prompt that forces Battery-shaped output, without editing the bundler's code — its constructor already accepts a custom `standard_audit_prompt`; this file is that prompt, frozen and versioned like `PROBE_INVOCATION.md` is for Mission Drift Review.

---

## How To Use This File

1. Confirm you're attempting a genuine AP-017 instance, not general review — if you just want feedback on a file, the bundler's default prompt is fine and this file is unnecessary overhead.
2. Construct the bundle with this file's seed as the `standard_audit_prompt`:
   `ColdSessionBundler(repo_root, standard_audit_prompt=<paste block below>).bundle([target_files])`
3. If the target includes `Admin/Auditor_Protocols.md` itself, also bundle the two companion files listed under **Self-Audit Target List** below.
4. Inspect the manifest yourself; never paste it to the auditor.
5. Open a brand-new session, ideally on a different model family than any prior instance logged for this same AP-017 cycle (cross-model is part of the acceptance criteria, not just a nice-to-have).
6. Paste the entire rendered payload as the first and only message. No framing, no "this is for AP-017," no "previous attempts found X."
7. Log the raw output under AP-017 in `Archive/Logs/Auditor_Protocols_Logs.md` per the Fresh Instance format already established there — include the manifest's `raw_sha256` values and the model identifier. Compare against any other instances on record; disagreements route through AP-004.

---

## The Frozen Seed

================================================================

You are an independent auditor with no prior knowledge of this repository or any previous findings about these files. Declare your role exactly once: "Operating as Skeptic/Auditor per the attached Auditor_Protocols.md."

Apply the full Adversarial Challenge Battery — all ten classes — as defined in the attached file's §Adversarial Challenge Battery. For each class, supply at least one concrete scenario that meets the minimum requirement stated in the class definition itself. A class with no concrete scenario, or with only a restatement of the class's own description, does not count as applied.

Do not assume any claim is correct because it is well-formatted, internally coherent, or constitutionally marked. Do not invent files, prior audit history, or resolution status — if you are unsure whether a referenced file exists, say so rather than assuming either way. If a required cross-reference or sidecar is absent from what you were given, note the gap explicitly and continue with what is present; do not fabricate its contents.

Do not treat consensus with any other audit (if you happen to be aware one exists) as evidence of correctness — form your own findings from the attached material only.

End with the Adversarial Audit Sign-Off Format defined in the attached file, including which of the ten classes you applied and which (if any) you could not.

================================================================

---

## Self-Audit Target List

When the audit's subject is `Admin/Auditor_Protocols.md` itself, bundle these alongside it (the bundler will not auto-include them — list them explicitly):

- `Admin/Auditor_Protocols.md` (the target)
- The Ethical Anchor verification surface — either `Admin/Ethical_Constraints.md` in full, or at minimum confirm the target's own Ethical Anchor field is present for the bundler's Audit Entry Conditions exception to apply (it already retains this row through stripping — see that module's Ethical Anchor carve-out).

**Not yet built, flagged honestly:** a stripped copy of `Archive/Logs/Auditor_Protocols_Logs.md` that retains only Description / Why It Matters / Resolution Path per entry (doctrine) and removes Status / Risk / Resolution / Fresh-instance / Surfaced-by content (retrospective judgment) is not something `cold_session_bundler.py` can produce yet — it strips retrospective content from a file's own body, not from a second file it points to. Until that exists, either omit the archive from a self-audit bundle entirely (the target file's own body is self-contained enough for a Battery pass — this is what every logged AP-017 instance to date has actually done) or, if archive content is genuinely needed, manually curate a Description/Why-It-Matters/Resolution-Path-only excerpt before pasting — never paste the raw archive file into a cold session.

---

## Resolution Log

- 2026-08-02: v1.0 — initial draft, human-directed. Companion file for `Admin/Auditor_Protocols.md` AP-017. Supplies the missing Battery-shaped prompt `cold_session_bundler.py`'s constructor already had a parameter for but no frozen, versioned text to fill it with. Does not change AP-017's closure bar (see that entry's own Resolution Path for the acceptance criteria this file's output is measured against).
