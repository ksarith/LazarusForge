# CAMPAIGN4_AUDIT_25 — Admin/Experiments.md (findings-only deposit)

**Campaign:** Campaign 4 adversarial findings-only sweep of `Admin/` (34 files), artifact 25 of 34.
**Seat:** Vibe (GLM 5.3 Flash architecture), Repo Custodian line, delegated; human-directed continuation. No adjacent seat held on this file; this session's line authored none of the audited doctrine. Prior Vibe-line maintenance passes touching this file (the 2026-10-28 candidates-note clarification; the 2026-11-05 MAINT-63 execution pass) are disclosed in the file's own logs and are treated as third-party content here — one of them is itself the subject of F-EXP-2 below.
**Date:** 2026-11-10.
**Audited artifact:** `Admin/Experiments.md` at LF main `3ef1733ae34878c69faeefe8343285a1f4184235` (head re-checked immediately before composition per MAINT-109).
**File stats:** 12,341 chars / 141 lines / 12,444 bytes. SHA-256 `c3765f6c5725a46b387ebe7ff539bef67aa38b7b51c558ac0dd18bd1579a5b1d`.
**Discipline:** findings-only per PKC-020. No Last Audit, Last Reviewed, version, Status, Spec Gate, or unknown field advanced on any file touched. This deposit is append-only; conversion to an audit of record is the human's alone (MAINT-26 / AP-032).

## Method

Full fetch, complete (no truncation; char count stable across reads). Auditor Prompt §3.3 per-file checklist, checks 1–11, all derived from live source. Adversarial layer: fabrication probes on every cited ID and path; self-attestation probe (Open Unknowns and the X10 index-parity shape recomputed against `Unknowns.md` v5.79, 113,335 chars); staleness probe (Aging arithmetic — see F-EXP-5); index-parity probe (the `Routing.md` registration row); wrapper-decay watch (X11). Verification targets fetched live this pass: `Unknowns.md`; `Tests/Living_Waters.md` (47,952 chars), `Tests/Trophic_Forge.md` (33,855), `Tests/Solar_Descent.md` (54,137); `Routing.md` (186,416); `Operations/Electronics.md` (89,567); `Architecture/Engineering.md` (38,371); `Architecture/Chemistry.md` (106,991); `Admin/Auditor_Protocols.md` v0.47 (156,858); `Architecture/Cognitive_Frameworks.md` (70,636); `Tests/Field_Logs.md` (33,558); `Tests/Field_Logs/README.md`; `Admin/Forge_Audit_Kit.md` (72,124, for the FT exemption class).

## Findings

### F-EXP-1 — WARNING (internal schema contradiction; normative)

The Entry Schema section opens: "Each experiment occupies one named section. Five fields required. No entry may be created without a defined Grounding Target, Hypothesis, and Pass/Fail Criteria." The schema table immediately below carries **eight** fields (Grounding Target, Hypothesis, Method, Pass/Fail Criteria, Status, Outcome, Ledger Reference, Date Completed), and the mandatory set named in the same sentence is **three**. "Five" matches neither count. The figure reads as a carryover from `Admin/Auditor_Protocols.md` §EF-0.3, whose Epistemic Ledger is "recorded with five explicit fields" (verified live in AP v0.47) — a different instrument with a different field set. The 2026-10-28 clarification line under the Experiments section repeats the figure ("they carry none of the five Entry Schema fields"), propagating it. Consequence: an entry author following the schema literally cannot tell whether five, three, or eight fields are required, in the file that owns the grounding-artifact schema for the entire PROVISIONAL→VERIFIED pipeline. Category: internal consistency (the F-CT-3 shape, in this file's own normative instrument).

### F-EXP-2 — WARNING (wrong-home qualified citation introduced by the MAINT-63 qualification pass itself)

The candidates note (and the File State Last Audit cell and the 2026-11-05 Resolution Log entry describing the same edit) cites "`Operations/Electronics.md` CF-001 (hardware watchdog)". CF-001's owning file is `Architecture/Cognitive_Frameworks.md`, not `Operations/Electronics.md`: the Cognitive_Frameworks sidecar records "CF-001 as this file's sole Blocking unknown among five", and Electronics.md's own 2026-10-30 retrofit record qualifies the same ID as "CF-001 (Hardware Watchdog Doctrine note)" with owning file `Architecture/Cognitive_Frameworks.md` (closing CAMPAIGN2_AUDIT_28 F1). The hardware watchdog circuit implementation does live in Electronics.md; the unknown ID does not. The two sibling citations in the same sentence pair IDs with their verified owning files (EN-001 → `Architecture/Engineering.md`, verified live; CE-003 → `Architecture/Chemistry.md`, verified live, Status Open, Risk Critical), so the 2026-11-05 MAINT-63 pass — whose entire purpose was to qualify candidate-ID pointers with owning-file citations — produced a line with mixed qualification semantics: two owning-file pointers and one implementation-location pointer. A reader resolving CF-001's status is routed to Electronics.md, where no CF-001 status exists. Mitigation disclosed: `Architecture/Cognitive_Frameworks.md`'s own dependency list uses the identical "`Operations/Electronics.md` CF-001" pairing (path as implementation location), so the form has a precedent in the repo; but in a sentence whose stated convention is owning-file qualification, the pairing is a mischaracterization (the F-EIP-1 / F-TRJ-3 class), introduced by the very pass that existed to eliminate the defect class. Findings-only: no requalification enacted.

### F-EXP-3 — NOTE (post-retirement Last Audit/Auditor write; third instance)

File State still carries Last Audit and Auditor rows, both written 2026-11-05 (the MAINT-63 execution pass) — one day after MAINT-56 (2026-11-04) retired those rows from File State, per the AP v0.47 Status note ("Last Audit and Auditor rows retired from File State the same pass (MAINT-56)"). Third instance of the class (F-ISP-4 first, F-IIL-3 second). The conformant-at-touch doctrine does not apply: the write post-dates the retirement.

### F-EXP-4 — NOTE (Auditor cell "prior:  Prior:" duplication)

The Auditor cell reads "...Q-2 invoked, disclosed); prior:  Prior: Vibe — Repo Custodian, 2026-10-28..." — a lowercase "prior:" marker immediately followed by a capitalized "Prior:", duplicating the chain marker (the F-OC-4 / F-IIL-5 class, another instance).

### F-EXP-5 — NOTE (Aging vacuous; fourteenth no-trip control case)

All six drift indicators are event-based; the file defines no time-based re-audit trigger, so the 90-day Aging Rule has no surface to compute against (0 open unknowns; the in-body sidecar is empty at stub stage). Fourteenth no-trip control case of the campaign. Compound Drift Rule vacuously did not fire (no indicator in firing state).

### F-EXP-6 — NOTE (verified-clean record)

Every fabrication probe passed except as recorded in F-EXP-2: X10 0=0=0 (zero EXP- rows anywhere in `Unknowns.md` v5.79, matching Open Unknowns 0 and the empty in-body sidecar); Ethical Anchor exact ("Attempt to do no harm. Defer to Ethical_Constraints.md if present."); the governing EF-0.8b sentence "A simulation confirming a simulation is not external grounding." verified verbatim in AP v0.47, together with the Anti-Distortion Clause at EF-0.0 §2 and AP-010's open status (the file's "AP-010 partially resolves when entries in this file establish documented grounding paths" framing is accurate against AP-010's live registered-open state); EXP-ASM-001–003's bases (EF-0.8b, EF-0.0, the Anti-Distortion Clause) all live; the three named future-entry targets verified in their owners (EN-001 and CE-003 correct; CF-001 defective per F-EXP-2); both Field_Logs examples live — `Tests/Field_Logs/FL-20261006-ave-sample-01.md` and `Tests/Field_Logs/FL-20261006-cap-meta-stale-01.md` are index rows in `Tests/Field_Logs.md`, and `Tests/Field_Logs/RUN_CARD-CAP-meta-stale-01.md` is a registered run card; the Tests/ trio (Living_Waters, Trophic_Forge, Solar_Descent) all live as cited; the `Routing.md` registration row is Explicit with Raw+Repo links; the Resolution Log carries exactly the five recorded entries (2026-11-05, 2026-10-28, 2026-10-24, 2026-10-06, 2026-06-21) with append-only ordering intact; the FT exemption class 11 stub-family exemption (IIL, AVE, Experiments, HDL) verified live against `Admin/Forge_Audit_Kit.md` (72,124 chars); the honest-v0 acknowledgment ("no physical-grounding experiments have been logged in this file") is true as written.

## Control cases and pattern tallies

- Aging-Rule systemic pattern: no trip here (F-EXP-5); the running total stands at 55 of 68 with instances 1–10 recorded (pattern doc Update 2).
- Pattern 2 (relocation-repair-miss): no new instance — this file contains zero `Archive/` pre-relocation references.
- Mischaracterization class (F-EIP-1 / F-TRJ-3 / F-TRJ-4): F-EXP-2 joins as a new instance, notable because the defect was introduced by a repair pass rather than left unrepaired.
- Bare-citation grep remedy: no new evidence point (citation forms in this file are qualified or exact-path).

## Compound Drift Rule

Did not fire: no drift indicator of this file is in firing state (F-EXP-1 and F-EXP-2 are consistency and cross-file defects, not the file's own declared indicators; indicator 6, Ethical Anchor absent or altered, is dormant — the anchor is exact).

## Resume point

Next file: `Admin/CIR_Gov.md` (CAMPAIGN4_AUDIT_26). Head at this deposit's compose: `3ef1733a` (LF main).

---

*Findings-only deposit per PKC-020. Nothing herein advances any audited field. Dispositions are the human's alone.*
