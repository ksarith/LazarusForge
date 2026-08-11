# Archive/

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

## Purpose

This directory holds three distinct kinds of prior-state material, kept separate so each can be governed correctly:

**Archive/ (root)** — prior-state archives of repository files at significant version milestones. Archival is governed by `Admin/Repository_Integrity_Protocol.md`. Files are deposited here when:
- A file is promoted to a new major version (e.g., v0 → v1)
- A file is deprecated or superseded
- A pre-release snapshot is required before a major structural change

**Archive/Logs/** — condensed full-text changelogs split out from their owning files' Resolution Logs, so the main files stay a manageable size while full audit history remains available (e.g. `Unknowns_Changelog.md`, `Progress_Log_Changelog.md`).

**Archive/Transcripts/** — raw external-agent conversation transcripts (Copilot, Grok) retained as provenance for specific ratified decisions that cite them by name. Reclassified out of the flat Archive/ root 2026-08-10 once its stated Purpose (file-version snapshots) was found not to match this content. Files here are cited from Resolution Logs and doctrine files as the source of a specific claim or fix — do not delete a Transcripts/ file without first checking `Routing.md` and grepping the repository for its filename.

**This directory is read-only for all agents.** No file in Archive/, Archive/Logs/, or Archive/Transcripts/ may be edited, deleted, or overwritten after deposit except via an explicit, human-directed reclassification (as above). Append-only otherwise.

## Current Contents

*Archive/ root: empty at initialization, pending first Specification-level file promotion. Archive/Logs/ and Archive/Transcripts/: populated — see directory listing.*

## Relationship to GitHub Releases

GitHub Releases serve as the v0 prior-state archival solution for whole-repository snapshots. This directory holds file-level archives for targeted version pinning that does not warrant a full release.

*RS-003 resolved — Archive/ directory created 2026-06-11. RIP-001 partial dependency cleared.*
