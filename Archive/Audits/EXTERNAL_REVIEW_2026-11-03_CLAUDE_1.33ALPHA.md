# EXTERNAL_REVIEW — Claude, 1.33 Alpha release review (relayed 2026-11-03)

**Author:** Claude (external architecture, independent of the Vibe line) · **Relayed by:** the human governing authority, 2026-11-03, verbatim including mid-stream progress lines · **Deposited by:** Vibe (GLM 5.3, Mistral) — Repo Custodian, findings-only deposit (PKC-020 precedent) · **Class:** external review record, not a LazarusForge audit pass; no file's Last Audit, version, or Status is advanced by this deposit · **Scope reviewed:** the 1.33 Alpha release tree as a standalone (post-MAINT-54 state)

## Custodian verification (2026-11-03)

Every checkable claim in the review was live-verified by the Custodian (Vibe, non-independent) before the review's new defects were acted on. All confirmed:

- **AUDIT_81 F1 / AUDIT_83 F1 / F2 repair states** — verified: Engineer_Protocols Highest Risk Medium (blob 4303f628 lineage), Verification_Gates Highest Risk Low (blob 52f30d20 lineage), FAK-009 index row corrected (Unknowns.md blob 875d534f), v5.77 changelog entry present.
- **The three index-vs-sidecar mismatches** (EN-005, CF-002, TF-002) — verified against the three owning sidecars (`Architecture/Engineering.md` EN-005 In Progress; `Architecture/Cognitive_Frameworks.md` CF-002 Open; `Tests/Trophic_Forge.md` TF-002 Status field Open, Resolution Path prose "partially addressed").
- **Chemistry Highest Risk High vs open CE-003 at Risk Critical** — verified at `Architecture/Chemistry.md` blob 68cc1c23; CE-003 sidecar fields: Status Open, Risk **Critical**, Priority Critical, Blocking Yes.
- **File_Template Low / Medium / High-only vocabulary vs live Critical use** — verified at `Admin/File_Template.md` blob ccc2ba96; Critical-as-Highest-Risk provenance confirmed at `Challenges/Closed_Loop_Feedstock.md` (blob 7767ef3e) and `Challenges/Living_Waters.md` (blob e1ceb06d).
- **AUDIT_81 "Head at fetch" blemish** — verified at AUDIT_81 blob cef5a250; corrected by dated correction file `Admin/AAudits/CORRECTION_2026-11-03_AUDIT81_HEADATFETCH.md` (the deposit itself is append-only).

**Human rulings received 2026-11-03 on this review's findings (MAINT-55):** (1) the three index rows corrected sidecar-wins; (2) Critical IS a valid Risk value — Chemistry Highest Risk → Critical and File_Template amended by dated entry, superseding the PKC-004/PKC-024 vocabulary clause on that point only; (3) this review deposited verbatim in-repo plus the dated correction file for the AUDIT_81 blemish; (4) Claude named the Rule 5 verifier for the five standing aggregates (packets deposited).

## Verbatim relay

The four sections below are the human's relay of Claude's review exactly as received, including the mid-stream progress lines. Preservation fidelity is the point of this deposit; nothing is paraphrased.

---

`Part 1 — initial review`

New release. Claude reviewed.

Nearly done: I'm checking that the Engineer_Protocols Highest Risk value matches its five open unknowns, then I'll give you the verdict.

1.33 Alpha holds up well as a standalone tree. The checks below found nothing broken, and I'd call it clean.

**What I checked, and the results:**
- **Structure:** 350 files, no junk (`__pycache__`, `.pyc`, `.DS_Store`, backups). The pycache you deleted on Oct 20 hasn't come back.
- **Links:** every relative markdown link resolves. The only dangling raw-GitHub URL is a stray backtick from the regex, not a real link.
- **Routing:** every file outside Archive and `Admin/AAudits` is in Routing.md.
- **Status field:** no file uses "Proposed" in a File State table, so the Oct 25 retirement of that value is respected.
- **Automation:** no hardcoded version declarations in the Python harness, so the old v0.14 problem hasn't recurred.
- **Latest change, v5.77, checked against the owning files:**
  - The changelog has a matching v5.77 entry.
  - VG-001 is Resolved in its own sidecar, and the FAK-009 index row now says so. FAK-009 itself stays Open, as the header claims.
  - Engineer_Protocols' Highest Risk of Medium matches its five open unknowns (EP-001/003/004/006 are Medium, EP-002 is Low).
  - Verification_Gates reads Highest Risk Low with Open Unknowns 0, which is consistent.

**Two things to look at, neither of them a defect:**
- **`Tests/Reset_Event_Design.md`:** it has no File State table, and its header banner says "PROPOSED — PENDING SKEPTIC PASS." That's probably deliberate, since it was relocated byte-identical from VibesSandbox. But it's a Tests/ file in Routing carrying a status word you retired, so decide whether it gets a File State at Exploration or stays as a deposit.
- **Discovery.md:** it doesn't list the per-folder audit files (RAudits, CAudits, OAudits, TAudits). I'm treating that as intended, since Routing covers them.

**What I didn't check:** whether the audit findings themselves were right, or whether the claimed fixes were the correct fixes. I only confirmed that the files say what the changelog says they say. Since Vibe authored both the CAMPAIGN2 findings and the fixes (disclosed as non-independent), the content of AUDIT_81 and AUDIT_83 is worth an independent read. Want me to do that?

---

`Progress line 1`

Still on the independent read. The two audits' claims verified, so I'm now checking a few index-vs-sidecar status mismatches I found on the side.

---

`Progress line 2`

Wrapping up: I'm doing one last check on whether Critical is a valid Risk value, since Chemistry.md has an open Critical entry under a "High" header.

---

`Part 2 — final report`

Both audits hold up. I did find a few related problems in the same family that the audits didn't catch.

**The two audits, checked against the files**
- **AUDIT_81 F1:** Engineer_Protocols' open entries are EP-001/003/004/006 at Medium and EP-002 at Low. EP-005 is Resolved. Highest Risk should be Medium, and it now is.
- **AUDIT_83 F1:** VG-001 is Resolved in its own sidecar and the FAK-009 index row now says so.
- **AUDIT_83 F2:** with zero open unknowns, Low matches the Resolution_Methodology control case.
- **Fix pass:** the File States, resolution logs and changelog agree with each other.
- **Blemish in AUDIT_81:** its "Head at fetch" line has a half-finished self-correction left in the record ("blob 6c73… no — 36f6…"). The file is append-only, so the only fix is a dated correction file. It's cosmetic.
- **Remaining check:** I ran a corpus-wide Highest Risk check on the 36 files whose sidecars I could parse. Only Chemistry.md failed, so the 10-30 recompute's misses look limited to EP, VG and Chemistry. It's not yet clear anyone reviewed the recompute's selection rule, which both audits recommended.

**Problems the audits didn't catch**
1. **Index and sidecar statuses disagree on three unknowns.** I parsed 347 Unknowns.md index rows and compared each to its owning file:
   - EN-005: index says Open, sidecar says In Progress.
   - CF-002: index says In Progress, sidecar says Open. AUDIT_06 verified the sidecar count but not this index row.
   - TF-002: index says Partially Addressed, sidecar says Open.

   This is the same kind of stale row as FAK-009. I can't tell which side is current. File-wins would make the sidecar the source.
2. **Chemistry.md Highest Risk reads High, but CE-003 is open at Risk Critical.** Closed_Loop_Feedstock and Living_Waters already use Critical as a Highest Risk value. So either Chemistry is stale, or Critical isn't meant to be a valid Risk value.
3. **`Admin/File_Template.md` defines Risk as Low / Medium / High only,** but Critical is in live use. The template and practice disagree, and that likely caused the Chemistry ambiguity.

**What I couldn't check:** 78 index rows point to files that keep their unknowns in other formats (Governance_Charter's changelog, Challenges files, Local_Governance_Framework). My parser skipped those, so they're unverified.

Want me to fix the three index rows and Chemistry in place and hand back only the changed files? For the index rows, I'd treat the sidecar as authoritative unless you tell me otherwise.

---

End of relay.

**Open items this review surfaced that remain with the human:** the X10 10-30 recompute's selection-rule review (both audits recommended it; the recompute's misses are now evidenced as EP, VG and Chemistry); `Tests/Reset_Event_Design.md`'s retired status word + absent File State (parked in the CAMPAIGN3 rulings); the 78 index rows whose owning files keep unknowns in non-sidecar formats (unverified by the review's parser — future sweep candidate; EN/CF/TF sidecars use ### ID subsections rather than table rows).

Disclosed: Vibe (GLM 5.3, Mistral) — Repo Custodian, Genesis Phase, non-independent custodian of this deposit; the review's author (Claude) is the independent layer. Human-directed. Open Parked Concerns rows: 8 (recounted 2026-11-03, Progress_Log §Parked Concerns).
