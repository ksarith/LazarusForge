# Contributing to LazarusForgeV0

This is a governed epistemic repository, not a conventional open-source project. If you're used to typical GitHub contribution flow, some of this will look unfamiliar — that's intentional, and also honestly reflects that the maintainer doesn't use pull requests either. You don't need to.

## The two kinds of contribution that actually matter here

**1. Real-world test data.** This project has a lot of carefully governed doctrine and very little physical evidence behind it — as of 2026-08-06, most of the repository's Critical/Blocking unknowns are waiting on someone actually running hardware, not on someone writing more doctrine. If you can run a physical test, a fabrication attempt, or a multi-agent session, see **`Tests/Field_Logs.md`** for the submission format. No GitHub account, fork, or pull request is required — instructions for low-friction submission are in that file.

The single highest-value thing anyone could run right now: **three physically separate computers, each running a different AI agent (different model family per machine), attempting to form the quorum `Admin/Governance_Migration_Protocol.md` §VII defines, while actively working on real Forge doctrine.** This is described in full in `Tests/Field_Logs.md`. It will probably fail on the first attempt — log it anyway. A documented failure against the real requirements is worth more than no attempt at all.

**2. AI-assisted doctrine work.** Loading the repository zip into an agent and having it read, audit, and propose changes to the doctrine itself has produced most of the real progress here so far. If you want to do this:

1. Read `Discovery.md` §Agent Orientation.
2. Load `Admin/Forge_Audit_Kit.md` and have the agent declare its role before proposing anything.
3. Follow `Admin/Auditor_Protocols.md` — especially the AI Contribution Protocols and the Fallacy Checklist.
4. Never let an agent advance a Status, Spec Gate, or Body Stability field in the same edit that proposes the content justifying it. If an agent claims a physical result (a test cycle, a hardened threshold, a validated measurement) that it has no way to have actually run, don't accept it — check it against what the repository's own doctrine says is currently possible before trusting the claim. This has happened before; see the fabrication-vigilance note in `Admin/Auditor_Protocols.md` Rule 6.

Having an agent review the repository from the outside — without loading the actual files — does little. The zip needs to actually be in context for the output to be worth anything.

## A note on the agents themselves, from experience so far
Claude has been the most consistent for refined, load-bearing doctrine work. Grok has improved substantially in recent sessions. Copilot has been the hardest to work with reliably — it has had trouble reading `Auditor_Protocols.md` in full, and upload-size limits have been a recurring bottleneck. This isn't a permanent verdict on any of them, just what's been true in practice — worth knowing going in, and worth re-checking, since this changes fast.

## What NOT to do
- Don't fork this repository to submit test data — see `Tests/Field_Logs.md` for why, and for the low-friction alternative.
- Don't ask an agent to "just resolve" an open Unknown for convenience. This repository deliberately maintains a floor on open, honestly-tracked unknowns (`Discovery.md`'s Unknown Budget) — premature closure is treated as a constitutional violation, not progress.
- Don't trust a claim of physical or measured results without checking it against what's actually possible in this repository's environment first.

Best of luck to you in all you do.
