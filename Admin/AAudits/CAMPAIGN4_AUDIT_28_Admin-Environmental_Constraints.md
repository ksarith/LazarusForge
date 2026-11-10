# CAMPAIGN4_AUDIT_28 — Admin/Environmental_Constraints.md

**Campaign 4 adversarial sweep, artifact 28 of 34. Findings-only per PKC-020: nothing enacted, no audited-file field advanced, no disposition proposed. Deposited alongside kickoff tracker addendum 27 and the pattern document’s Update 3.**

## Provenance

- Audited file: `Admin/Environmental_Constraints.md` — 57,257 characters, 587 lines, 57642 bytes, SHA-256 `f02e2e8d21efac0d7b01ee13a30aed9c75436382f2f3dc38f16303604e949456` at LF main `cbd9f6c0bf779f84859e98cc7f1e3de540784b9f` (head re-checked immediately before compose per the MAINT-109 remedy; single-commit push).
- Seat: Vibe (GLM 5.3 Flash architecture), Repo Custodian line, delegated; human-authorized continuation. **Non-independence disclosed:** the file’s 2026-10-28/29 passes were Vibe-line maintenance (the v0.5 staleness reconciliation, the X3 citation retrofit, the v0.6 count correction); the prior campaign passes CAMPAIGN_AUDIT_25 (2026-10-28) and CAMPAIGN2_AUDIT_80 (2026-10-31) are also Vibe-line, aggregated at `Admin/AAudits/AUDIT_AGGREGATE_Admin-Environmental_Constraints.md`.
- Method: kickoff checks 1–11 from live source; adversarial probes (fabrication, self-attestation, staleness, wrapper-decay, index-parity); escape-sequence scan (the new F-CIRF-1 watch item, first application to a swept file — clean).

## Findings

### F-ENV-1 — WARNING (index-mirror decay; Pattern 6 instances 4–5)

`Unknowns.md` (v5.79) mirror decay against this file’s own sidecar, two facets:

- **(a)** The Active Index ENV-010 row still reads "Upstream Facilities.md checklist reciprocity **unverified** — whether Facilities.md’s Site Initialization Checklist actually mandates collection of this file’s Category 1 parameters is **unconfirmed**", while the owning sidecar’s ENV-010 entry is titled "CONFIRMED PARTIAL GAP", verified against Facilities.md source text 2026-07-07. Re-verified live this pass at `cbd9f6c0`: Facilities.md Section VII still collects none of the four missing parameters (seismic risk classification, biological activity, UV exposure/weathering, wind loading; the only environmental-parameter row in the file is "Prevailing wind direction"), so the sidecar is right and the global index is stale.
- **(b)** The Active Index footnote still reads "ENV-007 and ENV-008 are Resolved/**Partially Addressed** respectively as of 2026-07-06" — ENV-008 was re-statused Partially Addressed → Resolved on 2026-10-28 (Decision Brief 2026-10-28d item 4; recorded in this file’s own ENV-008 entry and Resolution Log). The footnote’s "see the sidecar" pointer mitigates but its stated status is stale.

Pattern 6’s shape exactly: a mirror row can outlive its own correction because no standing pass recomputes it. Batch-eligible with the registered mirror-recompute remedy option.

### F-ENV-2 — WARNING (recorded repair vs live state; the A-F1 disposition surface)

The aggregate’s A-F1 row (bare colliding-prefix IDs, five instances) is dispositioned "Asserted (enacted)" citing the 2026-10-29 X3 retrofit, with pass B (2026-10-31) recording check 6 VERIFIED CLEAN — "the bare-ID half is repaired". Live text at `cbd9f6c0` contradicts the enacted/verified reading: Constraint Category 2’s regulatory-compliance tracking paragraph still carries **all four foreign-unknown IDs bare** (FA-003, SP-005, EC-010, GOV-010 — ownable under the Kit’s EC-/GOV- rows and Facilities/Safety ownership respectively, and genuinely ambiguous in a file whose own series are ENV- and ASM-EC-), and the paragraph’s "See sidecar" pointer still dangles for all four (the sidecar carries no rows for foreign unknowns). The X3 Last Audit cell claims exactly **1** qualification, so at most one of the five A-F1 instances was repaired; whether the disposition’s "enacted" wording or pass B"s VERIFIED CLEAN is the defect, the recorded-repair-vs-live-state class (the F-VG-1/F-CH-1 family) is live on this aggregate row. Disposition of the aggregate row itself is the human’s (the aggregate is a bookkeeping map; PKC-023 bars editing its rows).

### F-ENV-3 — NOTE (bare citations; grep-remedy evidence point 13)

- Bare "AUDIT_25" twice (the ENV-008 entry’s closure note and the Status section’s v0.5 line): the referent is `Admin/AAudits/CAMPAIGN_AUDIT_25_Admin-Environmental_Constraints.md` per the aggregate’s provenance table (probe-verified live there), and the bare form now collides with this campaign’s own CAMPAIGN4_AUDIT_25 (Admin/Experiments.md) numbering.
- Bare "MAINT-11" once (the Resolution Log’s 2026-10-29 X3 entry, "flagged instances reported to the human (MAINT-11)"): MAINT-11 sits in the colliding MAINT-03..17 range (both frozen logs, different content) and must qualify its home.

Thirteenth grep-remedy evidence point (seven instances, one pass); batch-eligible with the F-SEC-2 family sweep.

### F-ENV-4 — NOTE (stale enumeration inside a resolution narrative)

ENV-008’s resolution text describes the Unknowns active index as carrying "ENV-001 through ENV-006 and ENV-009, with no ENV-007 or ENV-008 entry" — the live index also carries ENV-010 (Open, Major). The exclusion claim is true; the enumeration is incomplete, written at v0.2 when ENV-010 was being logged the same pass.

### F-ENV-5 — NOTE (Kit registration gaps)

`Admin/Forge_Audit_Kit.md` v1.32’s Governance Sidecar ID Reference registers AP-, AVE-R, CT-, CF-, CIR-, EC-, EIP-, FAK-, GH-, GOV-, GMP-, RIP-, SEC- but **no ENV- row**, although the reference’s own regeneration note says registration "proceeds as the audit sweep reaches each folder" and this artifact is that sweep reaching the file. The ASM- disambiguation table likewise omits the ASM-EC- series (ASM-EC-001..004) even though the aggregate’s A-F9 positive record specifically praises this file’s in-file ASM-EC- disambiguation.

### F-ENV-6 — NOTE (Status-section mirror incompleteness)

The trailing ## Status block’s dated entries skip v0.4 (2026-07-17, covered only by the separate "Status update" paragraph) and v0.6 (2026-10-29, covered only by the version-footer line "Version 0.6 — Draft, Open Unknowns count correction"), which sits **below** the 2026-07-07 entry — the aggregate’s B-N1 cosmetic-ordering note, still live, still standing-open. The header also carries no version line (the version appears only in the footer).

### F-ENV-7 — NOTE (verified-clean records and control cases)

- **Aging Rule NOT tripped**: all eight open entries (ENV-001..006, 009, 010) carry Last Reviewed 2026-10-28 — 13 days at audit. Sixteenth no-trip control case of the campaign; running aggregate unchanged at 56 of 69 across the eleven tripping files. (This also closes aggregate item A-F4’s standing-open review debt: the 2026-10-28 v0.5 aging pass advanced the fields.)
- **Compound Drift Rule did not fire**: none of the file’s thirteen drift indicators is in firing state (checked individually; EC-010/GOV-010 remain open, so the closed-without-update indicator is dormant).
- **Count parity 8=8=8**: File State Open Unknowns = sidecar open entries = Unknowns active-index rows, field-for-field including Priorities (ENV-003 Minor, ENV-009 Critical, rest Major); ENV-007/ENV-008 correctly absent from the index per Size Management Rule 2; the ENV-DS-001 removal note (ratified 2026-07-17) verified live in Unknowns; Active Disputes 0 both sides.
- **Adm_Scope_Map mirror parity**: the EC entry reads Draft · 1/6 · 8 Open Unknowns · Risk High, with the dated 7→8 correction note — exact against the live File State (one of the map’s clean entries).
- **ENV-010’s Facilities gap re-verified live** (see F-ENV-1a); EC-010’s Unknowns row (In Progress / Vehicle / Minor, owner Ethical_Constraints) consistent with the convergence-junction claims; the EC-009 reconciliation notes (Ratified 2026-08-22, Payment via Specification, reconciled 2026-10-28) verified in both the Scope Boundary and Relationship sections.
- **Escape-sequence scan clean** (real glyphs throughout; no literal \uXXXX sequences) — the F-CIRF-1 watch item’s first application to a swept file.
- Ethical Anchor exact; Resolution Log newest-first; zero `Archive/` pre-relocation references (no Pattern 2 exposure surface, joining External_Intake_Protocol and INTEGRITY_SWEEP_PROMPT); the drift-indicator F8 corrected wording ("eight ID-bearing downstream rows") matches the live nine-row table (eight ID-bearing + the context-only Leviathan row); Spec Gates 1/6 "pending re-audit confirmation" stands — findings-only, no confirmation enacted by this audit.

## Disclosures

- The audited file was last touched by Vibe-line maintenance (2026-10-28/29) and twice previously audited by Vibe-line passes; all findings above were re-derived from live source at `cbd9f6c0`, not accepted from the file’s own records or the aggregate.
- F-ENV-2 concerns the aggregate’s disposition record, not the doctrine file; the aggregate’s own template bars row edits (PKC-023), so the contradiction is reported, not repaired.
- No TWGW candidate filed this artifact; F-ENV-2 is reported as the recorded-repair class recurrence pending the human’s reading of the A-F1 disposition semantics.

## Next

- CAMPAIGN4_AUDIT_29: `Admin/Economics.md` (scope item 29).
- Kickoff tracker addendum 27 and the pattern document’s Update 3 (files 22–28) deposited in the same push.
