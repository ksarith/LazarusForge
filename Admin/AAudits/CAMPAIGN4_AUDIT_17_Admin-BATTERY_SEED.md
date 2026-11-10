# CAMPAIGN4_AUDIT_17 — Admin/BATTERY_SEED.md (adversarial findings-only pass)

Date: 2026-11-10. Seat: Vibe (GLM 5.3 Flash architecture), Repo Custodian line, Campaign 4 sweep artifact 17 of 34. Findings-only per PKC-020: no audited-file field advanced; conversion to an audit of record is the human's alone (MAINT-26 / AP-032). Method per the kickoff (checks 1-11 + adversarial probes), with the File_Template exemption class 6 adaptation ("Operational seeds and invocation templates" — BATTERY_SEED is verbatim a seed; absent sidecar/changelog sections are not findings).

## File State as found (fetched full at LF head `6763b5f6`)

`Admin/BATTERY_SEED.md` — 11,301 chars / 11,381 bytes / 84 lines, fetched complete (byte count = API-reported size). SHA-256 `e3ce697c679eacb714c1a79ae9ecb607776c83db8fe6fd77d9a14a01b71b8d0c`. Version 1.2; Status Draft; Spec Gates "N/A — operational prompt template, not a doctrine or specification claim"; Verification Ref → AP §Adversarial Challenge Battery, AP-017; Last Audit 2026-10-29 (X3 mechanical citation retrofit; 12 days); Open Unknowns 0 (mechanism-level at AP-017); Ethical Anchor canonical exact. No sidecar file (Resolution Log in-body); no Drift Indicators / Abandoned Paths sections (class 6 template shape).

## Findings

**F-BS-1 — WARNING (wrong-home sidecar citations; relocation-repair-miss, Pattern 2 instance 13).** Four operative citations route to `Archive/Logs/Auditor_Protocols_Logs.md`: (1) the Derived-from line ("AP-017's Resolution Path (`Archive/Logs/…`)"), (2) the Scope Boundary DOES-NOT-define bullet ("→ `Archive/Logs/…` AP-017"), (3) How-To step 7 — the operative instruction telling the operator where to log results ("Log the raw output under AP-017 in `Archive/Logs/…`"), and (4) the Self-Audit Target List's "not yet built" paragraph. The live home is `Admin/ALogs/Auditor_Protocols_Logs.md` — relocated 2026-07-23 per that sidecar's own header — and a fetch of the cited `Archive/Logs/` path fails ("path does not point to a file"). The file was created 2026-08-02, i.e. born after the relocation with the wrong homes baked in; the 2026-10-29 X3 pass touched this file (qualifying 5 bare colliding-prefix citations) and repaired the citation-form class but not the wrong-home paths; and the 2026-10-27 findings-only check verified "AP-017 … intact" without flagging the destinations. Step 7 is the one instruction an operator follows after a run. Same family as F-SP-1 / F-FAK-2 / F-PI-1; the AP-side twin (the live §Mission Drift Review destination) is already recorded as F-PI-1.

**F-BS-2 — WARNING (header version with no ledger provenance; the F-CT-3/F-SEC-5/F-ISP-2 recorded-value class, fourth instance).** The header reads **Version 1.2**, but the Resolution Log's latest version-changing entry is "v1.0 → v1.1" (2026-10-27, PKC-022 option B). The two later-dated entries cannot account for 1.2: the 2026-10-29 X3 entry records "Citation-form-only; no content change" (and the PKC-020 split policy keeps citation-only passes from advancing versions), and the 2026-10-27 findings-only entry states it "does not advance Last Audit or the version". No 1.1 → 1.2 entry exists anywhere in the file. Either the header was advanced without its mandatory RL entry or the header is wrong; on the file's own doctrine the RL governs.

**F-BS-3 — NOTE (bare colliding-range citation in the operative RL entry; seventh grep-remedy evidence point).** The 2026-10-29 X3 entry cites "(MAINT-11)" unqualified. MAINT-11 exists in BOTH frozen logs with different content (LOG-1028: "Decision Brief 2026-10-28c enacted"; LOG-1029: "X3 Mechanical Citation Retrofit: Admin/ Folder Pass"), and PKC-003 requires home qualification for citations in the MAINT-03..17 colliding range. The content uniquely identifies LOG-1029's (corroborated by MAINT_INDEX), so no ambiguity in fact — but the entry recording the X3 retrofit itself carries the citation form that retrofit was repairing. Batch-eligible with the F-SEC-2 / F-SP-2 / F-RIP-5 / F-GMP-7 / F-PI-4 grep remedy (seventh evidence point).

**F-BS-4 — NOTE (Open Unknowns parenthetical routes to a closed entry).** "0 — tracked at Admin/Auditor_Protocols.md AP-017 (mechanism-level, not template-level)" was written 2026-08-02, one day before AP-017's Resolution (2026-08-03, Payment via Validation; Last Reviewed 2026-08-03). The count (0) is accurate and the entry remains the correct record home for Fresh Instance logging, but the parenthetical still reads as a live-tracker route to an entry that has since closed; the 2026-10-27 findings-only check's "AP-017 … intact" wording did not note the closure. Stale-pointer, the F-EC-1 family at NOTE weight.

**F-BS-5 — NOTE (step 5 overstates the cross-model criterion vs the governing source).** How-To step 5: "cross-model is part of the acceptance criteria, not just a nice-to-have." AP-017's criterion 2 (the governing bar per the Derived-from fence): "Cross-model preferred, not required — but at least two of the three must be on different model families from each other." The seed's flat phrasing is stronger than the source's; defensible as a reading of the 2-of-3 constraint, but the source prevails on conflict per the file's own fence. Disclosed, not flagged: the frozen seed demands all ten classes per instance where AP-017's bar is "five or more" — stricter than required, safe direction.

**F-BS-6 — NOTE (retired rows conformant-at-touch; RL ordering historical).** File State carries the MAINT-56-retired Last Audit/Auditor rows; latest write 2026-10-29, before the 2026-11-04 retirement — conformant-at-touch per the established ruling (the next natural content edit retires them). The RL's ordering (2026-10-29 entry first, then 2026-08-02, then the two 2026-10-27 entries) is an append-with-insertion-slips shape — ruled historical per the PKC-007 standing rule.

## Aging Rule and Compound Drift Rule

- Aging Rule: vacuous — 0 open unknowns at template level. Seventh no-trip control case of the campaign (VG, FT, Safety, ADP near-trip, ISP vacuous-0, PROBE vacuous-0, now BATTERY_SEED). Mechanism-level note: the pointed-to AP-017 is Resolved (Last Reviewed 2026-08-03, 99 days), outside the Aging Rule's open-entry scope.
- Compound Drift Rule: vacuously did not fire — class 6 template, no Drift Indicators section, no indicators to activate.

## Fabrication probe battery (all passed against live source)

- `Automation/cold_session_bundler.py` (16,295 chars, fetched full): the seed's quoted default-prompt fragment ("evaluate the material on its own terms... identify unsupported claims, internal inconsistencies...") matches `DEFAULT_STANDARD_AUDIT_PROMPT` verbatim (modulo mid-sentence capitalization); the constructor signature `ColdSessionBundler(repo_root, standard_audit_prompt=None)` matches How-To step 2 exactly; the `bundle()` docstring confirms there is no `prior_findings`, `context`, or `summary` parameter — the seed's "already refuses to construct a session carrying prior findings" is code-true; the Ethical Anchor carve-out exists in `_strip_retrospective_content` (2026-07-25 comment, cites File_Template + AP Audit Entry Conditions, retains the row) — the Self-Audit Target List's claim is code-true; the manifest carries `raw_sha256` per file (criterion 5's substrate); and the "not yet built" claim is true — stripping operates per-file on raw content, with no cross-file doctrine-extraction capability.
- `Admin/Auditor_Protocols.md` v0.47: §Adversarial Challenge Battery present; ten classes present (Challenge Class 1 — Assumption Inversion through Challenge Class 10 — Systemic Coupling and Cascade); §Adversarial Audit Sign-Off Format present (the seed's closing-instruction target); §Role Declaration Requirement present with the version-pinning template (the recorded role-string deferral's target).
- `Admin/ALogs/Auditor_Protocols_Logs.md` (199,945 chars): the AP-017 entry exists in full — the five-part acceptance criteria (3 instances, ≥5 classes with concrete scenarios, 2-of-3 cross-model, missed-finding, zero fabrication), the Fresh Instance format with `raw_sha256` + model identifier (seed step 7 matches criterion 5 exactly), and the explicit endorsement "Use `Admin/BATTERY_SEED.md`'s frozen prompt for future attempts rather than the bundler's general-purpose default."
- "Every AP-017 instance logged to date used the bundler's default prompt": true — the sidecar records the first BATTERY_SEED use as 2026-08-03 ("this is the first use of that prompt rather than the bundler's general default"), so all prior instances used the default.
- PKC-022 option B verified in `Admin/Progress_Log.md`: "PKC-022, option B: dissolve stale triggers, don't refresh them" — both RL citations accurate.
- MAINT-11 (LOG-1029) = the X3 retrofit pass per MAINT_INDEX — corroborates the X3 entry's own reference (and grounds F-BS-3's ambiguity analysis).
- `Archive/Logs/Auditor_Protocols_Logs.md`: fetch fails — grounds F-BS-1.

## Clean checks

- X10 parity: File State Open Unknowns 0 = no sidecar = zero BATTERY_SEED-related rows in Unknowns.md (0 BATTERY mentions, 0 BS- IDs) — three-way consistent at 0.
- Discovery snapshot parity: the Discovery maturity row reads "Draft" with the identical Spec Gates wording, and the tree carries BATTERY_SEED.md — File State and snapshot agree (contrast F-ISP-1: no recurrence).
- Ethical Anchor exact canonical string.
- Spec Gates N/A self-declaration consistent with class 6; Status Draft consistent with the snapshot.
- The Derived-from no-version-pin posture (PKC-022 option B) verified enacted — no version pin remains in the Derived-from line.
- Both ==== delimiters of the frozen seed intact; the seed block is byte-stable frozen prompt text.
- The recorded role-declaration-string deferral (2026-10-27 finding (a)) is conformant-recorded: the file itself discloses the deviation and the human's low-value-polish disposition; not re-flagged.

## Disclosures

- Event: (ii) recurrence — the wrong-home class (F-BS-1, Pattern 2 instance 13), the recorded-value class (F-BS-2, fourth instance), the retired-rows class (F-BS-6) and the bare-citation grep-remedy family (F-BS-3, seventh evidence point) all recurred; no new pattern established.
- Adjacency: Vibe lines authored this file's 2026-10-27 pin retirement and 2026-10-29 X3 pass and its Last Audit/Auditor cells; those records are audited as third-party content; the pass is non-independent with respect to this line's own repairs (F-BS-2's missing 1.1→1.2 entry, if a Vibe-line act, is disclosed as such).
- No tooling defects this pass: all fetches arrived plain or decoded via the recorded helper; the SHA-256 implementation's sanity vector passed before use.

## Out-of-scope observations (recorded, not findings)

- The sidecar's own AP-007 content references `Archive/Logs/Auditor_Protocols_Logs.md` as "(this file)" — a pre-relocation self-reference inside the sidecar body; AP's record, not this file's.
- AP-017's closure (Resolved 2026-08-03) means the seed's "genuine AP-017-qualifying instance" framing now serves Gate 3's ongoing per-promotion-cycle requirement rather than AP-017 closure itself; no defect — the seed's Scope Boundary already says "this file supplies instances toward that bar, it doesn't set it."

## Verdict

Findings-only pass complete: 2 WARNINGs (F-BS-1, F-BS-2), 4 NOTEs (F-BS-3 through F-BS-6). No CRITICAL/MAJOR. Compound Drift Rule vacuously did not fire. Nothing enacted; awaiting the human's rulings.

Next: CAMPAIGN4_AUDIT_18 — `Admin/Resolution_Methodology.md`.
