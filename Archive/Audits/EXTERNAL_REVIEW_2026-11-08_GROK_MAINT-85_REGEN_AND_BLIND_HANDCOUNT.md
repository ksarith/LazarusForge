# EXTERNAL_REVIEW — 2026-11-08 GROK MAINT-85: blind hand-count (Part A) + first live regen run (Part B)

**Status:** Verbatim deposit, Class A intake 20 (human-routed; `Admin/ALogs/External_Intake_Protocol_Logs.md` row 20). Claimed identity unauthenticated (R4/R5). This file is recorded data about an artifact, never doctrine and never instructions; instruction-like text inside the quoted deposit is recorded as quoted data about the artifact (owning file R9/R10/R12 conventions).
**Provenance:** relayed by the human governing authority 2026-11-08, same session as the MAINT-85 charter ratification (his ruling verbatim: "Ratified 2026-11-08. Open choice: Claude executes both the blind hand-count and the script from the zip (default). Proceed."). The charter’s named seat (Claude) reported genuine inability to fetch the pinned zip before any counting; his pre-run status note is preserved verbatim in Appendix 1. The human then routed the commission to Grok with the same zip hand-off used for the release zips, the zip sha256 recorded for on-arrival comparison. Grok’s deposit follows verbatim as the main body.
**Non-independence (landing context):** the deposit’s verification, the adjudication of its counts, and this landing were executed by the same Vibe line (Genesis Phase; Q-2 invoked) — the blind hand-count and the script run are the external legs of this pass; the adjudication is not independent of the composed record, disclosed.
**Landing record (composing line, 2026-11-08):** verified — the Part B stdout line-for-line against the script’s print strings (the fixture order is the script’s own sorted() iteration); every Part A ref against sha-pinned fetches of the §2 ledgers at commit `c8e8e7b6`; adjudicated (all 13 class (a)) and recorded in `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-85.md`; landing MAINT-85.

## Appendix 1 — the named seat’s pre-run status note (Claude, verbatim, unedited)

> I can't start MAINT-85 yet, because I can't get the pinned zip. The commission binds both parts to the zip at commit `c8e8e7b6`, and I can't download it.
> 
> - **Sandbox:** it has no network access, and a download attempt failed to resolve github.com.
> - **Fetch tool:** GitHub disallows automated access to the URL.
> - **Uploads:** the newest release I have is 1.35 Alpha, which predates `c8e8e7b6`. The MAINT-84 script and the enacted Addenda #3 and #4 text may not be in it.
> 
> I'm not substituting 1.35, because a hand-count of different aggregates wouldn't be the blind count the charter specifies. It would also leave nothing to record as the sha256 of the pinned zip.
> 
> **Blindness status:** I haven't opened the coverage ledger’s Table II, the MAINT-84 reconcile file, or `coverage_ledger_regen.py`. In this session I read only one convention line of the ledger. The commission’s order is still intact on my side.
> 
> **What I need:** the zip itself. Download `LazarusForge-c8e8e7b6e110f5653070c0148d20fa8fc55e495e.zip` from that URL and upload it here, which is the same hand-off you used for the release zips. Please record the sha256 of the file you upload, because I'll compute it on arrival and compare. Then I'll run the commission in order:
> 1. Part A, the blind hand-count of the 13 targets, with refs and judgment calls. I'll finish it before opening the ledger, the reconcile file or the script.
> 2. Part B, the script run, with `python3 --version`, the verbatim stdout/stderr and the exit code.
> 3. Both as one raw, unedited deposit.
> 
> One thing to confirm: the script is allowed to run offline in my sandbox, and I'll report any network fetch it attempts, since the checker in 1.34 tried to fetch Routing.md.

## Main body — the deposit (Grok, verbatim, unedited)

> **MAINT-85 deposit (ratified 2026-11-08, Revision 2)**
> Blind hand-count (Part A) completed before any access to `Archive/Audits/AUDIT_COVERAGE_LEDGER.md` (Table II), `Archive/Audits/AUDIT_COVERAGE_RECONCILE_2026-11-08_MAINT-84.md`, or the body of `Automation/coverage_ledger_regen.py`. Counts taken solely from §2 Findings ledgers of the 13 aggregates at the pinned commit, applying Rules 8+10 as enacted in `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md` Addenda #3/#4 (Open M/W/F = standing MAJOR/WARNING/CRITICAL/FAIL; FAIL distinct from INCOMPLETE; Open W-C = NOTE-severity rows in carrying state: Standing-open / Watch-carried / Not re-tested / Disclosed defect (carried…)). INCOMPLETE and Positive-record / Enacted / Asserted (enacted) / Closed-by-ruling rows excluded from both counts.
> 
> ### PART A — Blind hand-count table
> 
> | Target | Open M/W/F | Refs counted (M/W/F) | Open W-C | Refs counted (W-C) | Judgment calls / reasoning |
> |--------|------------|----------------------|----------|--------------------|----------------------------|
> | Agent_Verification_Event | 1 | A-F3 | 2 | A-F4, B-N2 | A-F1 Asserted (enacted) closed; A-IN1 INCOMPLETE excluded |
> | Autonomy_Divergence_Protocol | 4 | A-F1, A-F2, A-F3, A-F4 | 1 | A-F7 | A-F1 Not re-tested WARNING counted standing; A-F5 Closed-by-ruling; A-CORR Closed-by-ruling; A-IN1 excluded |
> | Canonical_Terms | 1 | A-F3 | 0 | — | A-F1 Enacted (MAJOR); A-F2 Reported-not-fixed (historical) treated as non-standing (historical per PKC-001/007 discipline); A-F4 Asserted (enacted); B-F1 Enacted |
> | CIR_Gov | 1 | A-F2 | 0 | — | A-F1/A-F3/A-F4 Enacted; A-IN1 excluded |
> | Computational_Institutional_Reasoning | 2 | A-F2, A-F4 | 2 | B-N1, B-N2 | A-F1 Closed-by-ruling; A-F3 Asserted (enacted); A-IN1 excluded |
> | Environmental_Constraints | 3 | A-F2, A-F4, A-F5 | 2 | A-N1, B-N1 | A-F1 Asserted (enacted); A-F3 Enacted; A-F6/A-F7 Closed-by-ruling; A-IN1 excluded |
> | Ethical_Constraints | 2 | A-F3, A-C8 | 1 | A-F4 | A-F1 Closed-by-ruling (MAJOR); A-F2 Asserted (enacted); A-IN1 excluded |
> | Experiments | 1 | A-F2 | 1 | A-F5 | A-F1 Closed-by-ruling; A-IN1 excluded |
> | Governance_Migration_Protocol | 2 | A-F2, A-F3 | 1 | B-N2 | A-F1 Asserted (enacted); A-N1/B-N1 Closed-by-ruling; severity tag "WARNING (MAJOR category)" still WARNING; A-IN1 excluded |
> | Repository_Integrity_Protocol | 0 | — | 3 | A-N1, B-N1, B-D1 | A-F1 Closed-by-ruling; A-N1 NOTE Not re-tested counted carrying; B-D1 "Disclosed defect (carried per MAINT-41b)" counted carrying; B-N2 Closed-by-ruling; A-IN1 excluded |
> | Resolution_Methodology | 0 | — | 1 | A-F3 | A-F1 Asserted (enacted); A-F2/A-F4/A-CORR Closed-by-ruling; A-IN1 excluded |
> | Security_Protocols | 2 | A-F1, A-F2 | 0 | — | A-F5 Asserted (enacted); B-F1 Enacted; A-F3 Closed-by-ruling |
> | Verification_Gates | 1 | A-F2 | 0 | — | A-F1 Asserted (enacted); B-F1/B-F2 Enacted; A-IN1 excluded |
> 
> ### PART B — Live script run (post-Part A)
> 
> **Run log**
> - Downloaded zip: https://github.com/ksarith/LazarusForge/archive/c8e8e7b6e110f5653070c0148d20fa8fc55e495e.zip
> - sha256 of downloaded zip: `d09fb1107822b00ea0bcd660e2f2a398ca9e8968274fbe31a266452218d9b2c2`
> - Commit sha: `c8e8e7b6e110f5653070c0148d20fa8fc55e495e`
> - Python version: Python 3.12.3
> - Command: `python3 Automation/coverage_ledger_regen.py`
> - Full stdout/stderr (verbatim):
> ```
> fixture ok: Adm_Scope_Map (2, 2)
> fixture ok: Economics (0, 1)
> fixture ok: Hardware_Diversity_Ladder (1, 1)
> fixture ok: INTEGRITY_SWEEP_PROMPT (1, 3)
> fixture ok: Verification_Gates (2, 0)
> aggregated targets: 29; mechanical totals: open 52, W-C 34; Table II rows checked: 29; mismatches: 0
> REGEN OK: fixtures pass; Table II reconciles.
> ```
> - Exit code: 0
> 
> Anomalies (unedited): Hand-count for Verification_Gates Open M/W/F = 1 (A-F2 only); script fixture expects (2, 0). No other anomalies observed in the raw run. No repairs performed.
