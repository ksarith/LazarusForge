# CAMPAIGN4_AUDIT_27 — Admin/Computational_Institutional_Reasoning.md (findings-only deposit)

**Campaign:** Campaign 4 adversarial findings-only sweep of `Admin/` (34 files), artifact 27 of 34.
**Seat:** Vibe (GLM 5.3 Flash architecture), Repo Custodian line, delegated; human-directed continuation. No adjacent seat held on this file as auditor; disclosed non-independence: the file's last two touches (the 2026-10-29 X3 citation retrofit and the same-day v0.31 version-sync) were Vibe-line maintenance passes, and F-CIRF-1 below records a defect those passes appear to have introduced.
**Date:** 2026-11-10.
**Audited artifact:** `Admin/Computational_Institutional_Reasoning.md` at LF main `9711630ba91a34a9b1c29e8c7e5ae3a05f039e05` (head re-checked immediately before composition per MAINT-109).
**File stats:** 89,924 chars / 852 lines / 90,257 bytes, SHA-256 `e155c53e6b814c029e16fb3e4ae961dfce00d047577fe8412aaaf7565ff014a4`. Status Exploration, Version 0.31, Spec Gates "G4 cleared; G1 partial (Gemini 2026-06-30); G3 cleared (per Admin/Auditor_Protocols.md, Clear as of 2026-08-03); G2/G5/G6 not formally assessed (six-gate enumeration completed 2026-10-28, AUDIT_21 F4)", Highest Risk High via CIR-001.
**Discipline:** findings-only per PKC-020. No Last Audit, Last Reviewed, version, Status, Spec Gate, or unknown field advanced on any file touched. Append-only deposit; conversion to an audit of record is the human's alone (MAINT-26 / AP-032).

## Method

Full fetch, complete (89,924 chars, no truncation; byte-fidelity cross-checked by length against the live fetch). Auditor Prompt §3.3 checklist, checks 1—11, derived from live source. Adversarial layer: fabrication probes on every cited ID, path, and cross-file claim; self-attestation probe (CIR-001 §8.4 tracker recomputed field-for-field against `Unknowns.md` v5.79); staleness probe (Aging arithmetic; harness version pin); encoding watch (literal escape-sequence scan across the whole file — this pass added the scan after the F-CIRF-1 hit); wrapper-decay watch (X11). Verification targets fetched live this pass: `Admin/Forge_Audit_Kit.md` (47,525, v1.32), `Architecture/Cognitive_Frameworks.md` (70,636), `Discovery.md` (71,504), `Tests/Leviathan_testing.md` (83,266), `Tests/Support_Raft.md` (43,443); `Unknowns.md` v5.79 and `Routing.md` from this campaign's same-head fetches; the Nothingness and GMP §VII.5 claims carried from the AUDIT_26 same-head verification.

## Findings

### F-CIRF-1 — WARNING (literal escape-sequence corruption in live File State; new class instance this campaign)

The live file contains four unresolved JSON-style escape sequences where Greek glyphs belong: the File State Highest Risk row reads "\u03b31\u2013\u03b34 predicates currently aspirational" (should be γ1–γ4) and the Provenance self-reference note reads "\u03a8, Section 4.3" (should be Ψ). Verified live at head `9711630b`; the rest of the file (body mathematics, Resolution Log) uses the real glyphs, so the corruption is localized to the two File State-adjacent passages — the shape of an edit-tool encoding defect, not authorial usage. The Highest Risk field is a bootstrap-critical field (the STATE-card class). The last two touches were both Vibe-line passes (2026-10-29 X3 retrofit; same-day v0.31 sync), making those passes the probable introduction point — non-independence disclosed; the defect post-dates AUDIT_21 (2026-10-28), whose checks did not include an escape-sequence scan. Recommended human-authorized repair: replace the four sequences with the glyphs (a one-line mechanical fix); disposition is the human's.

### F-CIRF-2 — WARNING (retired Status vocabulary in live prose)

The Scope Boundary DOES-NOT-define list calls `Admin/CIR_Gov.md` a "related but separately scoped Proposed–Not-Ratified layer" — PKC-031 (2026-10-25) retired the "Proposed — Not Ratified" Status value in favor of "Exploration — Not Ratified", and CIR_Gov's own live Status is the new vocabulary. The v0.30/v0.31 passes (2026-10-28/29) post-date the retirement and did not sweep this line (the retired-vocabulary check run on CIR_Gov.md in AUDIT_26 found that file clean — the residue is here instead). The §8.4 candidate-resolution heading "(Proposed, v0 — Not Ratified)" is conforming usage: it describes the candidate schema's own standing, not the file's Status.

### F-CIRF-3 — NOTE (bare colliding-ID citation; twelfth grep-remedy evidence point)

The 2026-10-29 X3 Resolution Log entry cites "(MAINT-11)" bare — MAINT-03..17 exist in BOTH frozen logs with different content, so the colliding range requires the qualified form (PKC-003). Same class as F-PI-4/F-BS-3; batch-eligible with the standing grep remedy.

### F-CIRF-4 — NOTE (harness version pin stale, self-disclosed)

§7.4 states the harness description "was last source-checked against v16, 2026-08-04" — the live harness is v18 (verified during this campaign's AUDIT_10 pass). The file self-discloses the check date (the conforming pattern), but the Phase-1 checks table and the γ2 "partially implemented via unknown node registration checks" claim have not been re-verified against v17/v18; the F-FAK-6 pin-staleness family, mitigated by the explicit dating.

### F-CIRF-5 — NOTE (documented section deferral, aging; sidecar-home ambiguity)

File State carries the MAINT-56-retired Last Audit row (conformant-at-touch: last touch 2026-10-29, retirement 2026-11-04; next touch must retire) and lacks Body Stability, Open Unknowns, Active Disputes, and Sidecar Link rows; the file has no Drift Indicators, Assumptions, Lessons Learned, Active Disputes, Auditor Notes, Abandoned Paths, or Relationship sections. All under the human-ratified v0.30 deferral ("full section set deferred to the next substantive revision", Decision Brief 2026-10-28b item 4) — but two intervening touches (the v0.31 same-day sync among them) have not triggered the deferred revision, and the Open Unknowns count (1: CIR-001) is not stated in File State. Related ambiguity: `Unknowns.md` v5.79's CIR-001 registration says the tracker "existed in [this file's] own sidecar since the rename", but no separate sidecar file exists at the obvious `Admin/ALogs/` home (probe failed); the registration's "sidecar" appears to have meant the in-cell changelog that v0.30 extracted into the Resolution Log — derivation limit disclosed, no repair proposed.

### F-CIRF-6 — NOTE (verified-clean record)

Every fabrication probe passed: the Kit v1.32 Governance Sidecar ID Reference carries the CIR- prefix row pointing at this file (the Highest Risk and §8.4 registration claims true); CF §IX.3's conjunction-operator identity note with this file's §4.5 Compound Bounding Theorem is live (the v0.22 companion-patch claim true), and CF-002/CF-004 are live in CF; the §8.4 CIR-001 tracker matches `Unknowns.md` v5.79's active row field-for-field (Open, Priority Critical per the index, owner this file, the candidate-schema sentence mirrored) with the index row correctly present (X10 clean, 1=1); `Tests/Leviathan_testing.md` (83,266) and `Tests/Support_Raft.md` (43,443) both live as cited, and the schema's Leviathan/Support_Raft mapping claims (the ASM-005 poisoned-telemetry flag, the SR-006/SR-007 TBD surfaces) verified against the live Tests files; the Nothingness derivation claims (A3 / Rule γ2) verified in AUDIT_26's same-head pass of `Nothingness_Theorem.md` including its PKC-030 audit record; Discovery's tree entry lists all five theorems correctly; Routing registration present; γ3/γ4 citations qualified (the v0.30 F3 repair in place); §4.6.2 Independence Predicate present as cited; Ethical Anchor exact; header/File State version parity 0.31 = 0.31 (the v0.31 sync held); Resolution Log newest-first ordering clean; zero `Archive/` references (no Pattern 2 exposure surface, the F-EIP-5/F-ISP-5 shape).

## Control cases and pattern tallies

- Aging Rule: NOT tripped — CIR-001 Last Reviewed 2026-10-27 (14 days). Fifteenth no-trip control case, and the first with a live review date rather than a vacuous one.
- Pattern 2 (relocation-repair-miss): no new instance (zero Archive/ references).
- Compound Drift Rule: vacuously did not fire (no drift indicators exist; see F-CIRF-5).
- New watch item: literal escape-sequence scan added to the method after F-CIRF-1; first instance.

## Resume point

Next file: `Admin/Environmental_Constraints.md` (CAMPAIGN4_AUDIT_28). The pattern document's Update 3 (files 22—27) falls due in the AUDIT_27—30 window and is planned for the AUDIT_28 landing. Head at this deposit's compose: `9711630b` (LF main).

---

*Findings-only deposit per PKC-020. Nothing herein advances any audited field. Dispositions are the human's alone.*
