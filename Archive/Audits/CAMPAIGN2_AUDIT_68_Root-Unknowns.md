# CAMPAIGN2_AUDIT_68_Root-Unknowns

**Audit of:** `Unknowns.md` (root-level)
**Campaign:** LazarusForge Campaign 2 — findings-only per-file audit (PKC-020; PKC-005 edit markers; findings-only passes never advance Last Audit/Status/Spec Gates)
**Auditor:** Vibe (AI Auditor, Campaign 2)
**Date:** 2026-10-30
**Repo head at fetch:** 644938a2500d68894105898be42dfb8c035c2599
**Fetched size:** 110618 chars (full text fetched and read)
**Deposit home:** Archive/Audits/ (human ruling 2026-10-30: root-phase audits go to the Archive's Audits subfolder — root files are corpus-base-layer artifacts, B-letter location per the X3 designation scheme)

## Checklist Results
**Global registry (Active Unknowns Index ~737 lines; version 5.75, 2026-10-29).**
- Sidecar count parity: THE CAMPAIGN'S CORE CROSS-CHECK — every open-unknown set verified during Campaign 2 was re-counted against this registry: LW-UNK 9✓, SR 12✓ (matches the file's 10-24 correction from 13), TF 10✓, PYC 8✓, SD-UNK 8✓ (with the file's own parity note at the SD cluster), LT 7✓, GH 13✓, CLF 9✓, RE-UNK 6✓, WS 4✓, BF 4✓, CM 4✓, EM 4✓, ES 3✓, PO 4✓, WA 2✓ (resolved rows correctly pruned per Size Management Rule 2), HR-UNK 2✓, QCC-R 3✓ (exactly R2/R5/R7, matching the file's declaration), MAQT 1✓ (MAQT-002 only — the owning file explicitly declares "MAQT-002 also indexed in `Unknowns.md`", so 001/003 are sidecar-only by design), CD 0✓ (Chrono sidecar-only, matching `Tst_Scope_Map.md`'s "sidecar only" note), and the Operations sets (EN/EV/EL/CE/TH) consistent with the Session 7 digests. **24 of 24 checked sets match. Zero registry-parity breaks found across the entire campaign.**
- Header vs body: version block follows its own Size Management Rule 2 (current version only) ✓; no File State / Ethical Anchor (registry family — see F2)
- Log vs body: `Archive/Logs/Unknowns_Changelog.md` homing verified ✓ (PC-007 migration honored)
- Scope/cross-refs: Expiry Watch and Blocking Watch sections verified against Campaign 2 digests (LW-UNK-001/003, SR-001, GH-009, CLF-003/004/006, GOV-008, PL-002, WW-004, RB-007 present and accurate)
- Bare colliding IDs: registry is the grounding target for X3's per-ID grounding; no bare-instance defects found
- Section integrity: clean (7 sections)
- Version/registry: self ✓ v5.75
- Aging: current (10-29 version bump)

### F1 — WARNING — T1 size trigger now tripped: 110,618 chars (~108KB) ≥ the 100KB Log-Split threshold (MAINT-28 Option C)
Unknowns.md was not on MAINT-28's named heaviest list (Progress_Log, Auditor_Protocols, Ethical_Constraints, Governance_Charter), but it has since crossed the T1 line. Under the human-ruled Option C, it splits at its next substantive touch; the split-order ruling should now include it (queue: Forge_flow ~179KB, AP ~157KB, GC ~130KB, Unknowns ~108KB, PCC ~82KB).

### F2 — NOTE — No File State / Ethical Anchor (registry family)
Same unruled family question as the navigation files (see AUDIT_63 F1): one ruling should name which root files carry the template and which are exempt. Unknowns.md is the global registry — an explicit exemption line would prevent every future audit re-flagging it.

### F3 — NOTE — Risk-vocabulary mapping instance: MAQT-002 listed Major (registry) vs Medium (owning sidecar)
One concrete instance of the corpus vocabulary divergence flagged in Session 8 (Major/Minor vs High/Medium/Low). Not a parity break — the registry consistently uses Major/Minor — but the mapping between the two scales has never been ruled. Feeds the standing vocabulary ruling.

### F4 — NOTE — Positives
Active-index-only discipline (resolved rows pruned with pointer to changelog), the Dependency Clusters section, and the Expiry Watch all make this registry genuinely auditable — and the 24/24 parity result above is the strongest single integrity finding of Campaign 2.
## Disposition

Findings-only (PKC-020): no changes were made to the audited file; no Status, Spec Gate, version, or Last Audit advancement. This report is deposited at Archive/Audits/ under the append-only rule; any correction to it must be a dated addendum, never an edit.
