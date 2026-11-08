# PROPOSAL — 2026-11-08 MAINT-85 CHARTER (Revision 2, ratified whole)

**Status: RATIFIED (2026-11-08, whole) — the human governing authority’s ruling verbatim: "Ratified 2026-11-08. Open choice: Claude executes both the blind hand-count and the script from the zip (default). Proceed." Enacted at MAINT-85.**
**Predecessor:** MAINT-84 (`c8e8e7b6` / `05d916d7` + `37f10bd4`)
**Provenance:** drafted by the composing line at the human governing authority’s direction, incorporating Claude’s six points on the first draft; the ratified text is preserved verbatim below, as delivered for his ruling. No section severed; no edits made post-ratification.
**Execution note (dated, MAINT-85):** the charter’s named seat (Claude) reported genuine inability to fetch the pinned zip (no sandbox network access; automated GitHub archive download disallowed; his only zip, 1.35 Alpha, predates commit `c8e8e7b6`) and made no counts, refusing substitution (a hand-count of different aggregates would not be the blind count the charter specifies). The human governing authority routed both parts to Grok with the same zip hand-off and sha256 comparison — a human-routed deviation from the charter’s named seat, disclosed in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md` §2 and in the MAINT-85 entry; the deposit: `Archive/Audits/EXTERNAL_REVIEW_2026-11-08_GROK_MAINT-85_REGEN_AND_BLIND_HANDCOUNT.md` (Intake Log entry 20).

---

**Revised MAINT-85 Charter** (incorporating Claude’s six points)

**Title:** First live regeneration of the audit ledger + mismatch adjudication  
**Authority:** Human governing authority (Ksarith)  
**Date proposed:** 2026-11-08  
**Predecessor:** MAINT-84 (`c8e8e7b6` / `05d916d7` + `37f10bd4`)

### 1. Purpose
Execute the first live run of the regeneration script landed in MAINT-84, produce an independent recount of the 13 mismatches, adjudicate both the script’s disagreements and any script defects, and drive the ledger to a clean convergent state. Close the immediate post-redraft debt without expanding into the longer-held items.

### 2. In-scope work
1. **Live regeneration**  
   - Run the regeneration script against the current live aggregates.  
   - Capture the full raw output (open counts, W-C counts, any new mismatches).  
   - Deposit the run log and resulting tables as evidence.  
   - Confirm the script is fully offline-reproducible from the release zip (no live GitHub fetches at runtime).

2. **Independent recount of the 13 mismatches**  
   - A seat other than the script’s author and adjudicator performs a hand-count of all 13 mismatches from a release zip.  
   - This is not a Rule 5 tranche; it is a targeted independent check to break circularity.

3. **Mismatch / defect adjudication**  
   For each of the 13 mismatches, classify into one of:  
   - (a) correct mechanical count → ledger follows the script  
   - (b) correct recorded value → document why the mechanical count is wrong  
   - (c) both partially right → split disposition with explicit evidence  
   - **(d) script defect** → fix the parser, version the script, re-run  

   For each of the 8 stale §2 rows whose addenda already record MAINT-63 resolutions: apply the owed re-label under §5d or explicitly defer with rationale.

4. **Ledger remains derived**  
   - Table I / Table II are always the script’s output.  
   - Adjudication outcomes are recorded as dated addenda on the owning aggregates (owning-register rule).  
   - **Convergence criterion:** after adjudication and any script fixes, a re-run shows zero unexplained mismatches.

5. **Before-and-after evidence**  
   - Every changed count appears in a before → after table with its evidence link.  
   - No silent count changes.

6. **Landing-helper first**  
   - The helper that derives its own expectations is used for the multi-file landing.  
   - All guards are derived at runtime from composed and fetched strings.

### 3. Explicitly out of scope
- Monitoring-home question (intake-16 P2)  
- MAINT-67 Part B  
- Intake-16 P4  
- Ratio check  
- Status-line replacement  
- Tranche-2 verifier naming  
- Checker investigation  
- Option C / C3 review items  
- Any new Rule 5 tranche or broad external verification

### 4. Success criteria
- Regeneration script executes and is reproducible offline from the release zip by a second seat.  
- Independent hand-count of the 13 mismatches completed.  
- All 13 + 8 items receive an explicit disposition (a–d or deferred with rationale).  
- Any script defects fixed, versioned, and re-run to convergence (zero unexplained mismatches).  
- Ledger tables remain pure script output; adjudication lives in aggregate addenda.  
- Before-and-after table published for every changed count.  
- Single coherent MAINT-85 landing (LF + VS) with full non-independence disclosure.  
- Landing helper used; all guards derived.

### 5. Execution constraints
- All expectations derived at runtime.  
- PKC-023 retention of originals.  
- Non-independence disclosed on every authored artifact.  
- Guard-gated writes; abort on any failed guard.  
- Knowledge-file update is convenient but not blocking.

### 6. Proposed sequence
1. Confirm current head SHAs and fetch the 28 aggregates + ledger.  
2. Independent hand-count of the 13 mismatches (separate seat, from zip).  
3. Execute regeneration script; deposit raw output.  
4. Adjudicate the 13 + 8 items (including possible class (d) script fixes).  
5. Re-run to convergence.  
6. Compose aggregate addenda + before/after table + VS entry + Intake Log entry 20.  
7. Guarded push using the landing helper.  
8. Knowledge-file update if/when available.

---

This version directly addresses all six of Claude’s points while preserving the original tight scope.

**Ready for your word:**  
- Ratify this revision  
- Further edits  
- Or request the redline version against the first draft
