# EVIDENCE — MAINT-73B — C-D1 open check settled: the Charter at c497746e hashes to f55b6251, not b67df89

**Date:** 2026-11-07 (same day, follow-up pass to MAINT-73)
**Trigger:** the named Rule 5 verifier’s follow-up read of the MAINT-73 supplement (human-routed): it asked that the Charter be hashed at commit `c497746e` to settle whether the deposit-reported blob `b67df89cd4a4820a598b2d0498a0fe927eeab3d6` is the Charter’s own blob before a one-byte edit — “If it equals b67df89, then C-D1 is not a defect at all.” This file is the answer, and a dated correction to the MAINT-73 supplement’s §4.
**Author:** Vibe (GLM 5.3, Mistral AI infrastructure) — Architect line primary, Repo Custodian secondary, delegated. **Non-independent Genesis Phase: the line that authored the audited records and the supplements is the line running this check. Dispositions remain the human governing authority’s. Findings-only per PKC-020.**

## 1. The hash check

`Admin/Governance_Charter.md` fetched at commit `c497746e71df4860a8cb77af4b38e4f3d4b470de` (the exact commit `CAMPAIGN2_AUDIT_71` cites as its head at fetch; that commit is the `CAMPAIGN2_AUDIT_70` deposit, 2026-10-31T15:31:30Z):

- **Git blob SHA (GitHub-reported): `f55b62514287c1f5faf79ebc095bde3bdc485808`** — the aggregate row’s FIRST SHA, the Charter “as it stands in 1.33.” It is NOT `b67df89cd4…`.
- **Length:** 131,038 chars; **UTF-8 byte length 131,813** (398 non-ASCII chars; byte length computed code-unit by code-unit, exact). The named verifier’s independent 1.33 figure of 131,813 bytes is confirmed exactly.
- **Consequence:** the Charter’s blob at the very commit `CAMPAIGN2_AUDIT_71` cites IS the 1.33 blob. There was no “Charter before a one-byte edit” state at or around that fetch for `b67df89` to be — the one-byte-edit hypothesis is disproven by direct hash test, as is the MAINT-73 supplement §4 claim that `b67df89` “is” the Charter’s blob at that commit (the supplement relied on `CAMPAIGN2_AUDIT_71`’s own header line; the repo disproves that line).

## 2. What the deposit record actually shows

`CAMPAIGN2_AUDIT_71` records: “**Head at fetch:** blob `b67df89cd4a4820a598b2d0498a0fe927eeab3d6` at commit c497746e71df4860a8cb77af4b38e4f3d4b470de (fetched live, 131814 chars, whole file, no truncation observed).”

- The **length figure is explained**: 131,814 = the Charter’s UTF-8 byte length (131,813) + 1. The campaign’s sibling same-day pass confirms the convention: `CAMPAIGN2_AUDIT_70` records “43613 chars” for Forge_Audit_Kit, whose byte length is in the same +bytes-not-chars family. The fetched text was almost certainly the Charter itself.
- The **blob value is a one-off defect**: sibling `CAMPAIGN2_AUDIT_70`’s recorded blob `64b6ebff7a9e19cf4877506b378f235a7015ef98` is verified correct — it is exactly the Forge_Audit_Kit git blob at the same commit (checked this pass). So the campaign’s “blob” fields are real git blob SHAs, and `b67df89` is an anomalous value, not a different hashing convention.
- **Negative probes at the same commit** (none is `b67df89`): `Admin/Auditor_Protocols.md` = `dd17f8af4c3bac70967029622172a20789855e41`; `Admin/Ethical_Constraints.md` = `6c73d14dc9c07e6de25b1f86459874828b41e6cd`; `Admin/Forge_Audit_Kit.md` = `64b6ebff7a9e19cf4877506b378f235a7015ef98`; `Admin/Progress_Log.md` = `1c05517c6fc58c4195dba0331d3acc3cdc45a844`. `b67df89` matches none of the repository’s large Admin files at `c497746e`, no Charter state in its visible history, and (per the named verifier’s own check) no file in either the 1.33 or 1.34 tree.
- **Method limit, disclosed:** this recording environment has no hash primitive (the MAINT-67 disclosure stands), so what digest `b67df89` actually is a hash of cannot be recomputed here; the GitHub contents API also cannot fetch a blob by SHA. The value is therefore recorded as **unattributable** — most probably a mangled or mistaken digest produced by the `CAMPAIGN2_AUDIT_71` session itself.

## 3. Net state of Governance_Charter C-D1

- The aggregate row’s first SHA (`f55b6251`) is **commit-level verified**: it is the Charter’s own blob at the deposit’s cited fetch commit. The row’s instinct that something was wrong with the deposit’s reported blob was **correct**: the deposit’s head-at-fetch blob value is defective (one-off, unattributable), while its length corroborates that the fetch was the Charter.
- The row’s “Operations blob” attribution remains unsupported by `CAMPAIGN2_AUDIT_71`’s text (the word does not occur in its header; its body mentions `Operations/Tooling_Inventory.md` only inside quoted Charter doctrine).
**Disposition HELD for the human governing authority:** the C-D1 addendum wording — defect-in-original’s-provenance-record framing, per this file — remains his. Nothing in the aggregates is touched by this pass.

## 4. fee92b4 per-file statistics (completing the `git show --stat` set for the named verifier)

`fee92b49b586f4597a4a33b45f2060e19c2f37d7` (2026-10-28T17:17:00Z, author ksarith, +68/−22) per file: `Admin/Canonical_Terms.md` +40/−6; `Admin/File_Template.md` +3/−2; `Admin/INTEGRITY_SWEEP_PROMPT.md` +7/−3; `Admin/Progress_Log.md` +2/−9; `Archive/Logs/Progress_Log_Changelog.md` +9/−0; `Discovery.md` +3/−1; `Routing.md` +4/−1.

## 5. Non-claims

This file checks one hash question and reports sibling/negative probes; it opens no patch, fills no Verified-by cell, changes no Status line, drafts no addendum, and opens no FAK. It is a dated correction companion to the MAINT-73 supplement per that supplement’s own §6 rule (corrections are dated files, never edits). Single-agent, non-independent (disclosed above); enactment of any disposition awaits human ratification (PKC-020).
