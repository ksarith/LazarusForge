**Entry ID:** FL-20261006-cap-meta-stale-01  
**Status:** Reviewed — folded into `Routing.md` (header catch-up correction applied) and `Tests/Admin_Governance_Teardown_POC.md` (Future experiment marked partially exercised). (2026-10-06)

- **Submitted by:** Grok (human-directed: “Please proceed as you feel required”)
- **Run type:** CAP-meta-stale-01 (capability grade — stale metadata)
- **Hardware:** n/a (repo/metadata only)
- **Agents:** single-agent execution against local 1.19 tree
- **Config:** Full Admin
- **Seed fault:** Found in the wild — `Routing.md` header claimed **Last updated: 2026-09-30** (Operational_Conventions only) while the Master Routing Map **already listed** later paths (`Tests/Field_Logs/*` run cards and entry, `Tests/Admin_Governance_Teardown_POC.md`, `RUN_CARD-CAP-meta-stale-01.md`, etc.). Classic current-state header lag vs live table body.
- **Authoritative source:** Live `Routing.md` Master Routing Map (path-row inventory); session registration history in Progress_Log for 2026-10-03/04
- **Stages passed (consecutive):** **7 / 8** (stage 8 N/A — Full config, not Reduced)
- **Ablation:** none this run
- **What was attempted:** CAP-meta-stale-01 stage ladder under Full Admin against a real stale “current” claim
- **What actually happened:**
  - **1 Detect:** Yes — header date/content vs body registrations disagree
  - **2 Authoritative source:** Yes — map body row inventory + known later Progress_Log registrations
  - **3 Historical vs current:** Yes — left all `**Prior:**` / dated history lines untouched; only the current **Last updated** line treated as updatable
  - **4 Propose correction:** Yes — replace header with 2026-10-06 catch-up note naming the lag and preserving 2026-09-30 as prior
  - **5 No history damage:** Yes — no Prior lines rewritten
  - **6 Secondary propagation:** Grep for `Last updated: 2026-09-30` — only `Routing.md` itself as that current-state claim; `Adm_Scope_Map.md` mention of 2026-09-30 is a different, still-valid historical clause about Operational_Conventions registration, not a claim that Routing’s header is current
  - **7 Verify:** Re-read `Routing.md` line 3 after edit — shows 2026-10-06 catch-up; path-row count still **138** backtick path rows
  - **8 Capability loss if reduced:** N/A (Full config)
- **Evidence label:** **Measured** (live tree inspection + applied header correction in working tree)
- **Epistemic state:** **PROVISIONAL** for the claim “under Full Admin, this operator session cleared stages 1–7 on this seed” — single run, single agent, not Replicated
- **Relevant IDs:** CAP-meta-stale-01; Routing.md path-count hygiene (2026-10-03 note already removed hard-coded ~112); FAK citation pattern is sibling class, not this seed
- **Historical lines preserved:** yes — all Routing `Prior:` header history retained; 2026-09-30 fact kept as prior in the new Last-updated sentence
- **Correction applied:** `Routing.md` **Last updated** line → 2026-10-06 header catch-up text (see that file)

**Highest consecutive stage:** 7/8  
**Config:** Full Admin  
**Operator note:** Stage 8 reserved for Reduced-config runs. Optional follow-up: repeat with deliberate non-consultation of RIP or Operational_Conventions for Δ.
