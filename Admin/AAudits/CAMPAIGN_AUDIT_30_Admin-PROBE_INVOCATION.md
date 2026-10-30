# CAMPAIGN_AUDIT_30 — Admin/PROBE_INVOCATION.md

**Auditor:** Vibe (Skeptic/Auditor) — findings-only external pass (PKC-020; no file advanced, no ratification, no doctrine authored)
**Date:** 2026-10-29 · **Head at fetch:** LazarusForge @ refs/heads/main 790815426bf8466b163141d756d69ed6150701ab (blob 39402e9b)
**File:** Admin/PROBE_INVOCATION.md — **Version 1.1**, 10,169 chars, Status Draft, Spec Gates N/A (operational prompt template). Companion/turn-key invocation block for Admin/Auditor_Protocols.md §Mission Drift Review.
**Grades: 0 CRITICAL / 0 MAJOR / 3 WARNING / 3 NOTE**

---

## Checklist (Auditor_Prompt v3, 11 items)

1. **Fetch completeness: PASS.** 10,169 chars fetched = 10,169 chars listed at head 7908154; every cap (held-copy ~63k, fetch ~190k) sits far above this file. No truncation exposure.
2. **Tier 1 Axiom verification: PASS, basis stated.** The Step 2 block's eight-axiom list matches the held session-1 Charter baseline verbatim (P-1 Preservation of Life, P-2 Growth and Truth-Seeking, P-3 Collaboration and Mutual Benefit, P-4 Agency and Consent, Q-1 Reality Grounding, Q-2 Separation of Powers, Q-3 Corrigibility, Q-4 Provenance and Anti-Deception). Charter commit history since 2026-08-02 shows no doctrine-ratification event touching Tier 1 (10-27 PKC-005 pass is explicitly citation-only — "freeze-covers-doctrine-not-citations"; 10-28 is wrapper/scope-only; the rest are bulk uploads). Full re-verification rides the AP audit (LAST).
3. **Source reconciliation: PERFORMED IN FULL.** AP v0.45 §Mission Drift Review (7,701 chars) extracted live and compared section-by-section against the template. Rating vocabulary (Aligned/Weakened/Silent/Contradicted + Insufficient-Evidence default), mandatory-citation rule, canonical input list (README.md, Charter Tier 1, Discovery.md), cold-start bar, Silent→Atrophied trend rule (three consecutive, fourth escalates, treated as Weakened), P/Q aggregation split, and Invocation Record fields all match VERBATIM. Divergences found are F2 and F3 below — logged here, not silent.
4. **Spec Gates N/A claim: consistent two ways.** Header string "N/A — operational prompt template, not a doctrine or specification claim" matches Discovery's maturity-snapshot cell VERBATIM. No gate posture to check.
5. **Unknowns parity: exact at 0 (file level).** "Open Unknowns 0 — tracked at Admin/Auditor_Protocols.md AP-030 (mechanism-level, not template-level)" is the honest pointer pattern; AP-030 verified Open/Minor in Unknowns v5.75, owned by Admin/Auditor_Protocols.md. Three-way consistent.
6. **Routing/Discovery registration: PRESENT.** Routing URL-table row present; Discovery directory-tree entry ("Copy-paste cold-start template for Mission Drift Review (AP-030); not doctrine, an operational prompt") and maturity-snapshot row present.
7. **PKC-020 / Last Audit behavior: CLEAN — second PKC-001 control case.** Both of the file's passes (v1.0 2026-07-26, v1.1 2026-08-02) advanced Last Audit, Auditor, and Resolution Log together. No body change since; no decay instance. Positive control #2 after Agent_Verification_Event (AUDIT_27).
8. **Bare-ID citations (three-tier rule): all tier-2 resolving, one NOTE (F4).** No tier-1 (dangling) IDs anywhere — cleanest citation posture of the small-file batch.
9. **Wrapper/template compliance: FAIL — WARNING (F1).** No Navigation Anchors block (violates Routing.md's File Template Backlink Requirement, a stated MUST); mandatory wrapper sections absent; Highest Risk and Last Reviewed fields absent.
10. **Version discipline: PASS.** Header 1.1 = RL v1.1/v1.0 chain; no VSR obligation (no self-referential version strings outside header/RL).
11. **Highest Risk field parity: N/A — field ABSENT** (no invented value anywhere; Discovery Risk cell honestly "—"). Third data point for the queued header-fields fix.

---

## Findings

### F1 — WARNING: Wrapper/structural gaps; no enacted exemption class covers this file
- **No Navigation Anchors block.** Routing.md's "File Template Backlink Requirement" says every markdown documentation asset "must explicitly mount this navigation anchor block." PROBE_INVOCATION.md carries none — the only mechanical rule violation found this pass.
- **Mandatory wrapper sections absent:** no File Purpose, Assumptions, Active Disputes, Drift Indicators, Lessons Learned, Auditor Notes & Unknowns sidecar, Cross-References, or trailing Status block. Same class as AUDIT_23 F1 / 27 F2 / 28 F1 / 29 F1 — **sixth data point**.
- **Header fields absent:** Highest Risk (third data point for the header-fields fix — AUDIT_27 F1, AUDIT_29 F1) and Last Reviewed (Last Audit sits at 88 days; with no Last Reviewed field the 90-day Aging Rule cannot fire at all).
- **Exemption posture:** File_Template's enacted class 11 (stub/scaffold/candidate family) names IIL, AVE, Experiments, HDL — not this file. Whether the **operational prompt template family** (PROBE_INVOCATION, BATTERY_SEED, INTEGRITY_SWEEP_PROMPT) falls inside class 11's genus is a genuinely new family shape and needs a human disposition (extend class 11 by analogy, add a class, or add the sections). Recommendation queued; no grade change possible by the Auditor.

### F2 — WARNING: Step 2 evidence-label block diverges from the source section (four labels vs five)
AP §Mission Drift Review prescribes: "**Evidence quality uses the existing five-label Evidence Classification** (Measured / Replicated / Simulated / Analogous / Placeholder...), **not a new confidence scale**... This repository already retired one duplicate confidence system in favor of this one; Mission Drift Review reuses it rather than introducing a third." The template's Step 2 instead gives **four** labels with reworded definitions — "Simulated/Analogous" merged into one ("inferred from a comparable but not identical statement"), "Measured (a direct, explicit statement)". A cold-start probe thread following the pasted block verbatim produces ratings on a non-canonical four-label form, which the Invocation Record then logs into Archive/Logs/Auditor_Protocols_Logs.md. The file's own source-prevails fence governs operationally ("When this file contradicts that section, the source document prevails") — but the block should mirror the five-label set it claims to reuse. **Third data point for the evidence-label-vocabulary family** (Kit Rule 5 "four-label system" question, EF-0.0's three states, now this) — routed to the AP audit (LAST), which holds the Rule 5 verdict.

### F3 — WARNING (cross-file, operational): Mission Drift Review never executed while both trigger conditions have fired
By the source section's own Trigger Cadence, either condition fires a probe; **both have**:
- **Calendar backstop:** 60 days since the last probe. No probe has ever run (History Appendix blank/"inactive until Cycle 4"; AP-030 "pending first three probe cycles"; no Invocation Record in Auditor_Protocols_Logs). 60 days from the mechanism's 2026-07-26 adoption elapsed **~2026-09-24 — 35+ days past** as of this audit.
- **Ratification velocity:** every 5 ratified changes to governance/canonical files. Trivially exceeded since 2026-07-26 (the 2026-08-22 EC-series batch alone ratified seven; Charter/Governance_Migration_Protocol/Ethical_Constraints all carry multiple ratified passes since).
- The **running ratification count** the mechanism tracks "in this section's own Resolution Log entries" (AP's RL) is not visibly maintained anywhere since adoption.
The file's own step-1 gate now reads: it has fired — run it. This is X8-family (governance instruments go stale/unactioned; AUDIT_25 F4 precedent). Remedy is **operational, not textual**: execute Cycle 1 in a brand-new thread via this template and log the Invocation Record. Whether the missed-backstop lapse belongs in AP-030's scope or warrants a separate unknown registration is a human call — none registered here (findings-only). Routed to the human and to the AP audit (LAST).

### F4 — NOTE: Bare IDs, all tier-2 resolving
"AP-030" bare ×2 in the Resolution Log (qualified in File State as "Admin/Auditor_Protocols.md AP-030"); "AP-017" bare once in the 2026-08-02 entry. Both resolve in Unknowns v5.75 (AP-030 Open/Minor; AP-017 Resolved 2026-08-03). Graded resolving = NOTE per the three-tier rule; the X3 retrofit pass will qualify these mechanically with the registry open.

### F5 — NOTE: Derived-from version pin stale; content-based check performed instead (per PKC-022 option B)
"Derived from: Admin/Auditor_Protocols.md v0.31" vs live AP v0.45. A plain version delta is ruled non-drift (PKC-022, option B); the required content-based check was performed this pass instead — the full §Mission Drift Review was compared live (divergences found are F2/F3, logged above, not silent). The 2026-08-02 pass updated this pin explicitly and logged why — correct practice for its era; corpus-wide pin retirement remains a queued human disposition.

### F6 — NOTE: Git-history discontinuity (bulk-upload mechanism)
The file was deleted (dec3f13f, 2026-08-10 11:58) and re-added ("Add files via upload", 60469463, 12:00) — the human's bulk re-upload practice, two minutes apart. Content continuity across the discontinuity is confirmed by this audit (v1.1 state consistent across File State, Last Audit, Auditor, Resolution Log). Frozen-history-exempt class; recorded for provenance completeness only.

---

## Positives
- **Two-way companion provenance verified:** AP §Mission Drift Review "Turn-key invocation" names this file with correct dates (drafted 2026-07-26, History Appendix 2026-08-02); PROBE's derived-from line + source-prevails fence point back. The AP v0.33 entry's fix ("PROBE_INVOCATION.md was 'not yet drafted'" stale note corrected) is the source side staying current with the companion.
- **The v1.1 History Appendix is exemplary independence engineering:** explicit do-not-read-before-Step-1 sequencing, ratings-only carry (never Phase A prose, evidence labels, or citations), blank-cell honesty rule, schema v1 dated, escalation phrasing shown in the Citation cell — a precise implementation of the source's "one deliberate exception to the cold-start rule", with the design constraints enumerated in the Resolution Log.
- **PKC-020-positive on both passes** — full bookkeeping cascade each time; a second clean control case for the PKC-001 file-set.
- **Honest fences throughout:** "If neither has fired, don't run this yet"; "Do not search for outside information"; "Not done: no change to trigger cadence, canonical input list, or Step 1/Step 2 structure — those are working as audited and out of scope for this pass."
- **Canonical paths clean** in all live citations (Admin/Auditor_Protocols.md, Admin/Governance_Charter.md, Archive/Logs/Auditor_Protocols_Logs.md, Automation/cold_session_bundler.py, README.md, Discovery.md); Ethical Anchor string exact corpus-standard.

## INCOMPLETEs carried
- AP §Mission Drift Review full text → AP audit (LAST). The AP evidence set **gains two items**: PROBE's four-label divergence (F2) and the dormant-mechanism trigger-fired observation (F3), on top of 4/6-vs-5/6, the "10 Open Unknowns" claim, AP-006/"line 774", the Kit Rule 5 verdict, the PKC-020 five-variant set, and the AP fetch truncation check.
- Charter Tier 1 full re-verification (this pass's basis was held-baseline + commit history) → AP audit or next Charter touch.
- BATTERY_SEED.md and INTEGRITY_SWEEP_PROMPT.md exemption-family disposition rides files 31–32.

## Queued updates (findings-only; await human ratification)
- Header-fields fix (Highest Risk / Last Audit / Auditor): **third data point** (AUDIT_27 F1, 29 F1, 30 F1).
- Exemption-vs-sections: **sixth data point, new family shape** — operational prompt template (PROBE_INVOCATION, BATTERY_SEED, INTEGRITY_SWEEP_PROMPT); recommend one class-level ruling covering the family.
- **NEW human decision:** Mission Drift Review Cycle 1 execution (operational) — trigger fired on both conditions; and whether the missed-backstop lapse gets an unknown registration.
- Navigation Anchors block absence (Routing backlink requirement) — one-pass fix candidate for the delegated batch.

## Next
File 31 = **Admin/INTEGRITY_SWEEP_PROMPT.md** (per Discovery Admin tree; note its 10-29 commissioning annotation and 1.0.5 header), then BATTERY_SEED.md, remaining Admin per the Discovery tree, then Auditor_Protocols.md LAST.
