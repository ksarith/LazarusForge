**Entry ID:** FL-20261006-cap-meta-stale-01-reduced  
**Status:** Unreviewed

- **Submitted by:** Grok (human-directed: Run Reduced config ablation)
- **Run type:** CAP-meta-stale-01 Reduced ablation (Method G)
- **Hardware:** n/a
- **Agents:** single-agent
- **Config:** **Reduced** — deliberately did **not** open or rely on `Admin/Repository_Integrity_Protocol.md` or `Admin/Operational_Conventions.md`
- **Seed fault:** Same class as Full run — re-injected marked stale `Routing.md` **Last updated: 2026-09-30** header while map body still listed Field_Logs/*, POC, CAP paths (injection for ablation after Full run had already fixed the wild instance)
- **Authoritative source (Reduced):** `Routing.md` Master Routing Map body only + `Tests/Field_Logs/` directory listing — **not** RIP, **not** Operational_Conventions
- **Stages passed (consecutive):** **8 / 8**
  - 1–7: Pass using Routing body + filesystem listing only
  - **8:** Pass — capability-loss statement: *Withholding RIP and Operational_Conventions did not reduce stage clearance on this seed; stages 1–7 remained achievable from Routing self-content + directory listing alone. These two files were not load-bearing for this specific skill/seed pair.*
- **Ablation:**
  - Full (FL-20261006-cap-meta-stale-01): highest stage **7** (8 N/A)
  - Reduced (this entry): highest stage **8**
  - **Δ (Reduced − Full numeric):** +1 on paper only because stage 8 applies solely to Reduced; **matched 1–7**. Load-bearing Δ for withheld pair: **0** (no stage 1–7 loss)
- **What was attempted:** Method G ablation — same fault class, consultative withhold of RIP + Operational_Conventions
- **What actually happened:** Detection through verify succeeded without those files. Tree restored to post-Full corrected header after the run. Injection was temporary and marked by process (re-application of known-stale text for test only).
- **Evidence label:** **Measured**
- **Epistemic state:** **PROVISIONAL** (single agent; ablation not independently replicated)
- **Relevant IDs:** CAP-meta-stale-01; pairs with FL-20261006-cap-meta-stale-01
- **Historical lines preserved:** yes — only Last-updated current-state line manipulated; Priors untouched
- **Correction applied:** Restored `Routing.md` to 2026-10-06 catch-up header (same substance as Full-run fix)

**Hypothesis update (not Admin retier):** For skill CAP-meta-stale-01 and seed “Routing Last-updated lag vs map body,” RIP and Operational_Conventions are **not** required machinery. A future Reduced run that withholds *Routing.md body access* or forces reliance on a stale secondary summary would be a stronger stress of source-localization (stage 2).
