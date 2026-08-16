# Archive/

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForge/refs/heads/main/Routing.md)
---

## Purpose

This directory holds four distinct kinds of prior-state and cross-repository material, kept separate so each can be governed correctly:

**Archive/ (root)** — prior-state archives of repository files at significant version milestones. Archival is governed by `Admin/Repository_Integrity_Protocol.md`. Files are deposited here when:
- A file is promoted to a new major version (e.g., v0 → v1)
- A file is deprecated or superseded
- A pre-release snapshot is required before a major structural change

**Archive/Logs/** — condensed full-text changelogs split out from their owning files' Resolution Logs, so the main files stay a manageable size while full audit history remains available (e.g. `Unknowns_Changelog.md`, `Progress_Log_Changelog.md`).

**Archive/Transcripts/** — raw external-agent conversation transcripts (Copilot, Grok) retained as provenance for specific ratified decisions that cite them by name. Reclassified out of the flat Archive/ root 2026-08-10 once its stated Purpose (file-version snapshots) was found not to match this content. Files here are cited from Resolution Logs and doctrine files as the source of a specific claim or fix — do not delete a Transcripts/ file without first checking `Routing.md` and grepping the repository for its filename.

**Archive/Astroid-miner/** — periodic full-archive snapshots of the companion Astroid-miner repository (space-based extension of the same salvage-first philosophy; not actively developed alongside this one). Stored as raw zip snapshots, not extracted into live markdown — this repository's doctrine cites specific Astroid-miner content by filename (e.g. `Autonomy_Divergence_Protocol.md`'s `[Astroid-miner]`-qualified cross-references) as external, non-binding, corroborating design signal only (per EF-0.1), never as this repository's own governed content. Added 2026-08-14. Nothing in this repository's live doctrine currently references the archived zip file path itself — cross-references are to the companion repository's individual files by name, resolved externally, not to this local snapshot.

**This directory is read-only for all agents.** No file in Archive/, Archive/Logs/, Archive/Transcripts/, or Archive/Astroid-miner/ may be edited, deleted, or overwritten after deposit except via an explicit, human-directed reclassification (as above). Append-only otherwise.

## Current Contents

*Archive/ root: empty at initialization, pending first Specification-level file promotion. Archive/Logs/ and Archive/Transcripts/: populated — see directory listing.*

## Relationship to GitHub Releases

GitHub Releases serve as the v0 prior-state archival solution for whole-repository snapshots. This directory holds file-level archives for targeted version pinning that does not warrant a full release.

*RS-003 resolved — Archive/ directory created 2026-06-11. RIP-001 partial dependency cleared.*
