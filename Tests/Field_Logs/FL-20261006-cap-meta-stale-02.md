**Entry ID:** FL-20261006-cap-meta-stale-02  
**Status:** Reviewed — folded into `Tests/Tst_Scope_Map.md` and `Discovery.md` (both corrected, original 2026-08-08 history preserved verbatim alongside the dated correction). (2026-10-06)

- **Submitted by:** Grok (human-directed: Please continue)
- **Run type:** CAP-meta-stale-01 (second seed — Full Admin)
- **Hardware:** n/a
- **Config:** Full Admin
- **Seed fault:** Found in the wild — `Tests/Tst_Scope_Map.md` still stated as **current** that `Field_Logs.md` was empty / nothing submitted (scope-entry note, finding 4, and residual language in the 2026-09-18 addendum), while the live index already listed GOV-021c and CAP-meta-stale-01 Full/Reduced entries under `Tests/Field_Logs/`.
- **Authoritative source:** Live `Tests/Field_Logs.md` Index table + `Tests/Field_Logs/` directory listing
- **Stages passed (consecutive):** **7 / 8** (stage 8 N/A on Full)
- **Ablation:** none this entry (see -reduced for prior ablation on seed 1)
- **What was attempted:** Continue CAP track on a second real stale current-state claim outside Routing.md
- **What actually happened:**
  - **1–2:** Detected; source = Field_Logs index + directory
  - **3:** Preserved 2026-08-08 / 2026-09-18 historical meaning via dated correction language rather than silent rewrite
  - **4–5:** Updated scope-entry note, finding 4, addendum supersession line; did not pretend the original build was non-empty
  - **6:** Propagation within Tst_Scope_Map (three sites); POC Future experiment marked partially exercised
  - **7:** Re-read Index — CAP and GOV-021c rows present; Tst_Scope_Map note matches
- **Evidence label:** Measured
- **Epistemic state:** PROVISIONAL
- **Relevant IDs:** CAP-meta-stale-01; pairs with FL-20261006-cap-meta-stale-01 / -reduced
- **Historical lines preserved:** yes — original empty-state finding kept as of-build history + explicit 2026-10-06 correction
- **Corrections applied:** `Tests/Tst_Scope_Map.md` (notes/finding/addendum); `Tests/Admin_Governance_Teardown_POC.md` Future experiment status line only
