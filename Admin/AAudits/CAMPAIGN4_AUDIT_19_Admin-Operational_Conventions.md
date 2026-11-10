# CAMPAIGN4_AUDIT_19 — Admin/Operational_Conventions.md

**Campaign 4 adversarial sweep of `Admin/` — artifact 19 of 34. Findings-only deposit per PKC-020: no audited-file field advanced (no Last Audit / Last Reviewed / version / Status / Spec Gates / unknown changes); deposits are append-only; conversion of any finding into an audit-of-record disposition is the human's alone (MAINT-26 / AP-032).**

- Date: 2026-11-10. Auditor line: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.
- Target: `Admin/Operational_Conventions.md`, fetched complete at LF main head `f476362a` — 17,890 chars / 18,016 bytes / 214 lines; SHA-256 `b0f2b98dc3fd28a4624576fea64eb1908260ac7f5fef7608719563f64bdd329b`.
- Classification: Template Exemptions class 9 (reference index), verified live in `Admin/File_Template.md` (class 9 "Reference index" lists this file with the exact declared terms: exempt from Lessons Learned / Active Disputes / Abandoned Paths and from keeping a Resolution Log; passes recorded in its Last Audit field; listed from 2026-10-25, PKC-017). Template checks adapted accordingly (the EIP/ISP/PROBE/BATTERY_SEED adaptation family): no Resolution Log, Drift Indicator or Abandoned Paths checks; File State, citation hygiene, cross-file claim verification and fabrication probes all run.

## File State as found (recorded, not advanced)

Status Specification; Body Stability Stable; Spec Gates N/A (reference index, not a governed doctrine surface); Verification Ref `Admin/Verification_Gates.md`; Last Audit 2026-11-05 (MAINT-63 execution pass, Architect line PRIMARY, Repo Custodian secondary; non-independent Genesis Phase, Q-2 invoked, disclosed); Open Unknowns 0; Active Disputes 0; Highest Risk Low; Sidecar Link N/A; Ethical Anchor exact canonical string. Body: Navigation Anchors, eight Conventions each with a violated-in-practice record and a source-of-truth pointer, a Candidates section ("None currently pending"), and two dated pass-record notes. No version string anywhere (consistent with the no-Resolution-Log class 9 design; nothing cites one).

## Findings

### F-OC-1 — WARNING — Convention 8 cites the pre-relocation Progress_Log_Changelog home (relocation-repair-miss, Pattern 2 instance 15)

Convention 8 renders Progress_Log's rotation rule as "rotate to `Archive/Logs/Progress_Log_Changelog.md` once more than five entries accumulate" and its supporting-sources line cites "migration history in both files' `Archive/Logs/` changelogs". Live tree at `f476362a`: the `Archive/Logs/` directory contains exactly two files (`Discovery_Changelog.md`, `Unknowns_Changelog.md` — directory listing); a fetch of `Archive/Logs/Progress_Log_Changelog.md` fails (path does not point to a file); the live changelog is `Admin/ALogs/Progress_Log_Changelog.md` (ALogs directory listing), relocated 2026-10-30 (MAINT-29) — Routing's own history records the changelog's original 2026-08-09 registration at the Archive/Logs home, so the citation was correct when written (2026-10-03) and is wrong now. Progress_Log's live rotation instruction reads "Rotate to `Admin/ALogs/Progress_Log_Changelog.md` — relocated 2026-10-30, MAINT-29 — once more than five entries accumulate." The 2026-11-05 MAINT-63 touch repaired Convention 4's two stale AP pointers in this same file with the same relocation as its subject, and did not sweep Convention 8. The Unknowns_Changelog half of the same supporting-sources line is correct (`Archive/Logs/Unknowns_Changelog.md` exists). Nuance disclosed: OC's quotation is faithful to Progress_Log's own Size-discipline paragraph, which itself still carries the stale home (see out-of-scope observation 2) — but the supporting-source citation and the convention's operative guidance are this file's own, and its "the source wins — update this file" doctrine made the refresh owed at the 2026-11-05 touch.

### F-OC-2 — NOTE — Convention 6's "all nine" script count is stale (substance verified true)

Convention 6: "Scripts under `Automation/` are listed in `Routing.md`'s URL table — all nine as of the PKC-026 pass". Live `Automation/` holds twelve `.py` files (directory listing); all twelve verified present in `Routing.md` (per-file probe 12/12), so the rule's substance holds — the count is stale. The time-scoped wording ("as of the PKC-026 pass") mitigates; recorded as recorded-count staleness (the F-SEC-5 family). The entry's source-of-truth pointer resolves: Routing's Scope sentence on `Automation/` verified (".py sources are listed, packaged archives are excluded"; the PKC-026 rewording confirmed in Routing's own record).

### F-OC-3 — NOTE — Convention 4's generic check heuristic still routes to Archive/Logs/ only

Convention 4's generic text and its check heuristic ("check for a similarly-named `_Logs.md`/`_Changelog.md` in `Archive/Logs/` before concluding a registered ID's content is missing or thin") predate the 2026-10-30 relocation: `Archive/Logs/` now holds only the two root-file changelogs and no `_Logs.md` file at all (the AP logs the convention was written around live at `Admin/ALogs/`). The two AP-specific mentions were repointed by the MAINT-63 pass and the flagship instance now names the live home, but a reader following the generic heuristic alone would check only the directory that no longer holds Admin doctrine sidecars. The MAINT-63 repair disclosed its own scope as "Citation-form-only; no convention changed" — the residual is recorded, not repaired.

### F-OC-4 — NOTE — Auditor cell transition-marker duplication

The File State Auditor cell contains a doubled transition marker: "...Q-2 invoked, disclosed); prior:  Prior: Vibe — Repo Custodian, 2026-10-29..." — cosmetic; the rest of the audit chain renders correctly.

## Clean-check record (all verified against live source at `f476362a`)

- X10 three-way 0=0=0: File State Open Unknowns 0; Sidecar Link N/A; `Unknowns.md` contains zero OC- IDs (its sole Operational_Conventions mention is the v5.79 companion-edits list, not an unknown row). Highest Risk Low recomputes (0 unknowns, 0 disputes).
- Convention 1 mechanics claim code-true: `Automation/audit_lib.py`'s `extract_md_refs` backtick regex `([A-Za-z][A-Za-z0-9_/]+\.md)` requires the character immediately after the opening backtick to be a letter, exactly as stated.
- Convention 2: all three named files (`Operations/Exception_Evidence.md`, `Tests/Multi_Agent_Quorum_Trial.md`, `Tests/Persistent_Cognition_Candidates.md`) now carry the exact canonical anchor string — the 1.17-era drift is repaired; the historical record stands.
- Convention 3: `Automation/integrity_check.py`'s SIDECAR_ID_RE captures suffix layers (`(?:-[A-Z0-9]+)*`) as part of the ID — the EC-012-PR double-definition fix is present as claimed; EC-012-PR verified live in `Unknowns.md` ("Resolved 2026-09-23 as EC-012-PR ... parent EC-012 remains Open"). AP-013-R1 not re-probed this artifact (AP-sidecar ID; AP-013's resolution was verified in AUDIT_11's probe battery).
- Convention 4 instances verified: AP → `Admin/ALogs/Auditor_Protocols_Logs.md` (ALogs listing); Discovery.md → `Archive/Logs/Discovery_Changelog.md` and Unknowns.md → `Archive/Logs/Unknowns_Changelog.md` (both in the Archive/Logs listing).
- Convention 5: `integrity_check.py` excludes `Archive/` from the duplicate-ID scan (source: "Archive/ is excluded from this scan" + the `rel_path.startswith("Archive/")` guard, with the false-positive history in its docstring) — claim true.
- Convention 7: `Admin/File_Template.md`'s New File Creation Checklist requires the `*_Scope_Map.md` registration (verified live); all five named scope maps exist; `Admin/Adm_Scope_Map.md` carries the OC entry (dedicated subsection plus companion list) — the file's own Convention 7 violation story checks out as repaired.
- Convention 8: RM §9 exists ("### 9. Self-Maintenance Verification (Prose and Code)" — OC renders the parenthetical as a dash; resolves); the attributed history verified in RM: "failed to preserve its own stated 'most recent first' ordering and five-entry rotation limit on five separate occasions across one week, including once while a fix for a *previous* instance of the same failure was being written" (OC's quotation of the parenthetical is verbatim; its summary says "five separate times in one week" against RM's "five separate occasions across one week" — faithful paraphrase); Progress_Log's Size-discipline paragraph exists; Unknowns.md's line-4 block carries the quoted rule ("This block now keeps only the current version"); the `Unknowns_Changelog.md` 2026-09-10 migration note verified verbatim (14+1 versions stacked, caught "until James asked directly"). Live self-check per the convention's own instruction: Progress_Log's rotating section currently holds 4 dated entries (within the five-entry cap) and Unknowns.md's version block holds only v5.79 with no stacked version headings — no live violation of either rule.
- Candidates section: "None currently pending" consistent with the body.
- Ethical Anchor exact; Navigation Anchors resolve (`Discovery.md`, `Routing.md` both live).
- MAINT-29/62/63 mentions match the VibesSandbox maintenance records (the MAINT-63 index row records the OC pointer repair).

## Out-of-scope observations

1. `Unknowns.md`'s header (line 4) cites `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` and `Archive/Logs/Forge_Audit_Kit_Changelog.md` — both fetch-fail at that path; both live at `Admin/ALogs/` (verified). Same wrong-home class, in the global index's own header; Unknowns.md is outside the 34-file Admin/ sweep scope. Queued for the human alongside F-OC-1.
2. `Admin/Progress_Log.md` carries the same split internally: its Size-discipline paragraph still routes to `Archive/Logs/Progress_Log_Changelog.md` while its rotation instruction names `Admin/ALogs/` with the relocation note. Progress_Log.md is a later sweep artifact; recorded here only as corroboration.

## Deliberate shapes recorded, not findings

- The Last Audit/Auditor fields are this file's designated pass-record home per its class 9 exemption (FT: "its passes are recorded in its Last Audit field") — not the MAINT-56-retired-row class; the tension between MAINT-56's corpus-wide row retirement (2026-11-04) and the class 9 designation (2026-10-25, still live in FT) is disclosed for the human's consolidated ruling if desired.
- Convention 6's pre-emptive-entry deviation is self-annotated in the entry (retained per the human-ratified batch as an annotated exception).
- No version string anywhere — consistent with the no-Resolution-Log class 9 design; nothing cites one.

## Disclosures

- Event: (ii) recurrence — the wrong-home class recurs (F-OC-1, Pattern 2 instance 15); no new pattern established.
- Aging Rule vacuous (0 open unknowns — the campaign's ninth no-trip control case); Compound Drift Rule vacuously did not fire (class 9, no drift indicators).
- Adjacency: the Last Audit cell records this delegated line's predecessor passes (2026-11-05 MAINT-63; 2026-10-29 X3) as auditors, including the MAINT-63 repair whose completeness F-OC-1 examines; audited as third-party content; the pass is non-independent with respect to this line's own prior repairs, disclosed.
- No harness defects this artifact.

## Disposition

None. Findings stand as recorded; awaiting the human's rulings. Next artifact: CAMPAIGN4_AUDIT_20 — `Admin/Repository_Structure.md`.
