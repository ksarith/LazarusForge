# CORRECTION — 2026-10-31 — Head-at-fetch blob values in CAMPAIGN2_AUDIT_79 / 81 / 83 / 84

**File type:** dated correction file per the append-only rule (errors get corrections, never edits). The four deposits above stand as issued; only their **Head at fetch** lines are corrected here.

**Cause, honestly stated:** the Auditor recorded blob SHAs from memory of an earlier directory listing instead of from the fetch record for the session — the exact honesty failure (report only what you fetched) the Auditor_Protocols prohibit, self-caught during post-deposit verification against the commit-tree listing at `f8a1f4c036c50684c5bed77d108c832edb7ef3bc`. AUDIT_81 additionally contains an unedited drafting artifact in its head line (`blob 6c73… no — 36f6f807…`); that artifact is voided by this correction. The character counts, findings, and derivations in all four deposits were taken from the actual fetched texts and are unaffected — the wrong values are provenance metadata only.

## Corrected values

| Deposit | Recorded (wrong) | Correct blob at f8a1f4c… |
|---|---|---|
| CAMPAIGN2_AUDIT_79 (Autonomy_Divergence_Protocol.md) | ad4c927055a193a9f385a6a00c76876bef75808f | **5b9dc279c698972913ad2761d77c5a4ea6d6df62** |
| CAMPAIGN2_AUDIT_81 (Engineer_Protocols.md) | 36f6f80772e69d8fc6a8b0340eea530e69903e66 (Ship_of_Theseus blob — wrong file) | **96ef26325e32e12e15adc2e5878454270fdeea6a** |
| CAMPAIGN2_AUDIT_83 (Verification_Gates.md) | 3fc42bf57ddc18716c0c947553a6d350464bd935 (Auditor_Protocols_Logs blob — wrong file) | **2859c1ac204b98f7234e6e6c95ef2f528a4b2d3b** |
| CAMPAIGN2_AUDIT_84 (Trajectories.md) | 36f6f80772e69d8fc6a8b0340eea530e69903e66 (Ship_of_Theseus blob — wrong file) | **3c996178719fd5d7679039847d821e9fc7bb02c6** |

## Unaffected deposits (verified correct)

- CAMPAIGN2_AUDIT_80 (Environmental_Constraints.md): 8bbec88041ea4c48832b4db50a12aeb6513b0e66 ✓
- CAMPAIGN2_AUDIT_82 (Resolution_Methodology.md): a8fc878002e82a5695196aeec9735d94ae8738de ✓

## Process note for the campaign

All future deposits in this campaign will read head-at-fetch values from the fetch record itself (the resource URI or a same-commit directory listing), never from recall. Recording this as a named instance of the honesty regime working on the Auditor itself.

---
*Correction deposited 2026-10-31 by Vibe (GLM 5.3), Skeptic/Auditor pass, findings-only, non-independent (Genesis Phase). Append-only; the four corrected deposits are not modified.*
