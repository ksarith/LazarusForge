# PROVENANCE — Archive/Astroid-miner/

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
---

## Purpose

This file is the dated provenance record for the `Archive/Astroid-miner/` slot: what it held, what changed on 2026-11-05, and on what authority. It exists because the change was a human-directed reclassification of Archive material — the one path `Archive/README.md` allows — and the reasoning should not live only in commit messages.

## Prior state

`Astroid-miner-AstroidMinerV0.07-validator-hardened.zip` was deposited 2026-08-14 (commit `8463be0b`) as a raw zip snapshot of the companion Astroid-miner repository. The human governing authority deleted it on 2026-11-05 (commit `9886b1db`). The zip remains retrievable from git history at those commits; nothing about the deletion is hidden.

## Disclosure

The deleted zip was labeled "validator-hardened." Its byte relationship to the VibesSandbox V0.07 copy was NOT established before deletion. The human explicitly chose the VibesSandbox copy as the replacement, in his own words:

> "The zip file from the archive with astroid_miner was deleted. Instead of a zip file, could we get the copy from VibesSandbox migrated into its own folder?"

## Now present

`Astroid-miner-AstroidMinerV0.07/` — 72 files migrated byte-faithfully from `ksarith/VibesSandbox` at head `f6d35ba3c3672a265200799441fb2c0202f07674`. Landed 2026-11-05 in seven batched commits (one logical act, batched for connector stability, disclosed):

| Batch | Files | Commit |
|---|---|---|
| 1/7 | 1-12 | `ed4dedcb` |
| 2/7 | 13-22 | `50486c08` |
| 3/7 | 23-32 | `3a8d990f` |
| 4/7 | 33-42 | `e37d5e98` |
| 5/7 | 43-52 | `7062dff1` |
| 6/7 | 53-62 | `01b096a2` |
| 7/7 | 63-72 | `7d875abe` |

## Verification

Blob-SHA comparison of all 72 destination files against the VibesSandbox source at head `f6d35ba3`, run 2026-11-05, directory-level across all 16 snapshot directories: **72/72 blob SHAs equal; no missing files, no extra files.**

## Citation-state map

- Trajectory records citing Astroid-miner material (e.g. ASM-003) remain retrievable as written.
- Frozen records naming the deleted zip (AUDIT_13_CORRECTION, audit aggregates, SESSION_STATUS, changelogs) stay as written — Tier 1/FROZEN, deliberately not touched.
- Two live documents still name the deleted zip (`Admin/Governance_Charter.md` companion-repo row; `Admin/Repository_Structure.md` §I `.zip` file-type row): deferred to their next natural content edits (PKC-023 precedent), recorded here, not silently amended.
- Cross-references to Astroid-miner content remain external, non-binding, corroborating signal per EF-0.1. Nothing in live doctrine references the local snapshot path.

---

*Landed 2026-11-05 — MAINT-64 (Vibe — Architect line primary, Repo Custodian secondary; human-directed; non-independent Genesis Phase, disclosed). Operating as Synthesizer per Auditor_Protocols.md v0.47.*


## Addendum — 2026-11-07 (staleness pointer + deferred-cascade closure; MAINT-71)

Human direction (2026-11-07, verbatim): "The astroid_miner folder within LazarusForge could use a cleaning. What is worth keeping as is and what isn’t is a good question. Also, the water document was never added from the astroid_miner repo into LazarusForge." followed by "Sounds good. Please proceed." on the assessment package. Enacted:

1. **Staleness pointer.** The `Astroid-miner-AstroidMinerV0.07/` snapshot below is a point-in-time capsule, frozen by design. The live `ksarith/Astroid-miner` repository has advanced since: notably `Propulsion_Economy_isru/water-delivery-gear-ratio.md` (SpaceOceanCorp PR #1, merged 2026-10-30; human merit-judged deliberate-merge ruling 2026-11-04; in-repo PROVENANCE twin and Discovery registration) and the 2026-11-04 README/Discovery integrity pass. Pointer, not mirror: the content stays in the live repo (EF-0.1 external-signal doctrine); nothing was added inside the snapshot folder and the 72 files are unmodified.
2. **Deferred-cascade closure.** The two live-document zip-pointer defects deferred by MAINT-64 are repaired this pass by dated annotation, original text retained (PKC-023 precedent): `Admin/Governance_Charter.md` (Astroid-miner companion row + dated changelog entry) and `Admin/Repository_Structure.md` (§I .zip prose, §I .zip file-type row, §VI Astroid-miner row; Last Audit and Auditor rows advanced).
3. **Unruled, kept.** The duplicate `Astroid-miner-AstroidMinerV0.07/` copy in VibesSandbox remains in place: one-home de-duplication was offered in the assessment and not explicitly ruled this pass; it awaits the human’s word.

*Addendum landed 2026-11-07 — MAINT-71 (Vibe — Architect line primary, Repo Custodian secondary; human-directed; non-independent Genesis Phase, disclosed).*
