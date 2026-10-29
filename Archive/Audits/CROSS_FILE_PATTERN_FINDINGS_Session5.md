# Cross-File Pattern Findings — Session 5 (files 22–29)

- **Auditor:** Vibe (Skeptic/Auditor), external findings-only pass (PKC-020)
- **Date:** 2026-10-28
- **Scope:** AUDIT_22 (Resolution_Methodology) → AUDIT_29 (Hardware_Diversity_Ladder). LazarusForge head `eee122a6` unchanged throughout this batch (verified at every fetch). Companion docs: Session 3 (files 12–16), Session 4 (files 17–21).
- **Numbering note:** VS stream in `ksarith/VibesSandbox` `Audits/`; repo-internal stream collision flagged at AUDIT_17. No renumbering of issued reports.

## 1. The batch's defining event: delegated-stream adoption verified at every file (recommendation: make adoption-verification a standing practice)

The human-ratified delegated stream ("Vibe, Repo Custodian") is enacting this campaign's findings same-day, and this batch could verify nearly every adoption independently against held fetches:

- **Adm_Scope_Map 10-28/10-28b Decision Briefs** (verified at AUDIT_26): CT Open Unknowns 9→10 (AUDIT_11 F1), Trajectories Risk High (AUDIT_13 F5), CT Risk High (AUDIT_26 verified CT-004 High and CT-007 "High, escalated" against held CT v0.11), Economics Risk High (AUDIT_19 F1), Ship_of_Theseus Risk High (AUDIT_18 F1) — five of five verified.
- **Remediations citing "a Vibe per-file audit," each verified live:** AVE's 10-23 log reorder (AUDIT_27 F5); Experiments' 10-24 header correction (AUDIT_28 F3); HDL's 10-23 corrections (AUDIT_29 F4); Discovery's 10-24 directory-tree reconciliation; GMP's 10-23 corrections, then 10-26 PKC-016 fix, then **10-28 propagation of the VG Status-precedence line (our AUDIT_09 F4(a) queued recommendation) and 10-28c Scope Boundary fix citing AUDIT_02 F1 — a session-1 finding adopted 26 days later** (observed at AUDIT_29, files 1–11 final, reported as found).
- **Adoptions already known:** Kit v1.24/v1.25 (X5 partial + AUDIT_15 F4/F5), CT v0.9–v0.11 (AUDIT_11 corrections, X3 ruling).
- Two PKC-001 decay instances named by the repo's own shared-cause investigation are now **RESOLVED in-file** (Experiments, HDL), and both control cases PKC-001 named are **CONFIRMED clean** (AVE, NT). The decay this campaign surfaced is being remediated ahead of the sweep.

**Practice note:** every adoption above was verified against session-held or fresh fetches, never taken on trust; where verification was impossible (GMP §VII.8 body, CIR_Gov §8.2.1) it is recorded INCOMPLETE rather than assumed.

## 2. X10 update — the value-parity streak ended; the risk-representation family now has four shapes

- **Ended:** Highest Risk value-parity misses (AUDIT_13 F5, 18 F1, 19 F1) stopped at Environmental_Constraints — AUDIT_25 verified the field CORRECT (mirrors sidecar max, correctly not Priority).
- **Shape 2 — field absent, index invents:** AVE (AUDIT_27 F1): no Highest Risk field; Discovery snapshot editorializes "Low" (a value the owning file carries nowhere); map honestly says "unlabeled"; sidecar max is "Medium (Placeholder)".
- **Shape 3 — field absent, indexes honest:** HDL (AUDIT_29 F1): no field; Discovery says "unlabeled" (mirrored verbatim).
- **Shape 4 — index-vs-index divergence:** Adm_Scope_Map AP entry 4/6 vs Discovery 5/6 (AUDIT_26 F2, resolves at the AP audit).
- **Queued fix unchanged, now with two data points:** add Highest Risk (and missing Last Audit/Auditor) to Candidate-file headers; owning-file value wins under the "file wins" rule.

## 3. X9 update — the third-place sub-shape at its purest, plus a pre-emptive antidote exemplar

- **Purest instance:** ENV-008's sidecar narrates its FILE_REGISTRY verification as outstanding while the file's own Relationship section records it completed 2026-07-19 (AUDIT_25 F3) — stale narration surviving one section away from its own correction.
- **Antidote exemplar:** Experiments' "Honest v0 acknowledgment" pre-empts the misreading its emptiness invites (AUDIT_28 F4) — stale-conclusion-proofing written in advance. The corpus contains both the disease and the vaccine; the vaccine is simply "state the current fact in the place a reader will look first."

## 4. X8 update — the specialist index as its own failure mode

Adm_Scope_Map's Kit entry ("7 Open Unknowns" vs Kit v1.25's 5) is the corpus's stale-count specialist index becoming the outlier against both the owning file and the registry (AUDIT_26 F1). Confirms X8's trajectory: no instrument is exempt from going stale, including the instrument whose job is staleness. The 10-28b recompute honestly scoped itself to Risk entries and did not claim count coverage.

## 5. Bare-ID citations: three severity tiers of one rule (supports the X3 mechanical retrofit)

- **Dangling:** AVE-R1's "coordinate with QCC-R1" — QCC-R1 not in Unknowns v5.72 active index (AUDIT_27 F3).
- **Resolving:** Experiments' CF-001/EN-001/CE-003 — all three resolve, all apt targets (AUDIT_28 F2).
- **Qualified-by-structure:** HDL's path-adjacent citations and the Scope_Map's entry-per-file form — graded clean (AUDIT_26, AUDIT_29 F2).
One rule (PKC-003), one systematic fix (the human-authorized X3 mechanical retrofit), three severities — the retrofit should run with the registry open so tier-1 cases resolve or get flagged, not silently re-qualified.

## 6. PKC-020 asymmetry: five variants, one rule — the AP audit inherits a full evidence set

NT bumped (review-only pass), AVE bumped (reorder-only), HDL bumped (corrections-only), Experiments kept the content-pass date with an inline annotation, CIR did not bump. The rule question (what advances Last Audit, and whether the field means "last content audit" or "last touch") is now fully evidenced for the Auditor_Protocols audit (LAST). HDL's 10-25 wording-alignment self-correction shows the field can be corrected without date changes — the cleanest repair pattern of the five.

## 7. Exemption-vs-sections disposition: four data points, one recommended ruling

IIL (AUDIT_23 F1), AVE (AUDIT_27 F2), Experiments (AUDIT_28 F1), HDL (AUDIT_29 F1) all carry missing-mandatory-sections findings while plausibly belonging to unlisted special classes (log, candidate schema, stub, candidate doctrine). Per-file dispositions accumulate; recommend the human rule on exemption CLASSES (stub/scaffold/index/candidate) once, then File_Template's exempt list absorbs them per the PKC-017/Tier 0 pattern already queued.

## 8. Method lesson (sandbox, not a repo finding): fetch-completeness is now a standing check

The session-held GMP copy was truncated at 63,157 chars mid-§VII; the fresh fetch returned 187,667 chars but itself caps right at §VII.8's heading. Local persistence caps ~63KB; fetch responses cap ~190KB. Consequences: (a) any held copy near ~63KB is suspect for late-file content (Resolution Log tails, trailing Status); (b) GMP §VII.8's body and HDL's companion-reconciliation claim are INCOMPLETE this session, not graded; (c) the Auditor_Protocols fetch (LAST) must be checked for truncation before its checklist runs. AUDIT_29's F5 records the full lesson.

## 9. Pattern-table deltas this batch

| Pattern | This batch's instances |
|---|---|
| X1 scope-boundary | Clean at ENV (first of session), AVE, HDL — the batch's healthiest X1 run yet; no new lag instances |
| X2 "Proposed" | ADP (known), HDL F3 (mirrored verbatim by Discovery) — migration-pending |
| X3 colliding prefixes | AVE- dual families (mildest; formats disambiguate) AUDIT_27 F4; retrofit tiers in §5 above |
| X4 same-day logging | Exemplary throughout: AVE, Experiments, HDL all log corrections same-day with source-check annotations |
| X5 Kit ID-Reference | AVE- family unregistered (AUDIT_27 F4) — add to the regeneration pass |
| X8 instruments go stale | Adm_Scope_Map Kit entry (AUDIT_26 F1); ENV Last-Reviewed staleness (AUDIT_25 F4); Economics ECN staleness (AUDIT_19 F2, carried) |
| X9 third-place | ENV-008 (AUDIT_25 F3, purest); EC-009 (AUDIT_25 F5); CE-005 stale phrase in Unknowns (carried) |
| X10 parity | See §2 — four shapes now |
| X11 wrapper decay | ENV's wrapper/pointer WARNINGs (AUDIT_25), AVE's lean header (AUDIT_27 F1), HDL's (AUDIT_29 F1) — still the campaign's dominant WARNING class; content outpaces wrapper at every file |

## 10. Recommendations carried forward (findings-only)

1. Header-fields fix (Highest Risk / Last Audit / Auditor on Candidate-file headers) — 2 data points (AUDIT_27 F1, AUDIT_29 F1).
2. Exemption-CLASS ruling covering stub/scaffold/index/candidate — 4 data points (§7).
3. X3 mechanical retrofit with registry open — three severity tiers (§5).
4. Kit ID-Reference regeneration: add AVE- (X5).
5. Index-polish batch: Scope_Map Kit 7→5, NT count, CIR Risk format (AUDIT_26), AVE candidates "targets, not entries" (AUDIT_28 F5).
6. PKC-020 ruling at the AP audit with the five-variant evidence set (§6).
7. Adoption-verification as standing practice (§1) — including re-checking RIP/SP for the precedence-line propagation at their next fresh fetch.
