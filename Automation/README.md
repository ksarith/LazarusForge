# Automation/

Tooling for auditing, checking, and experimenting on the repository. Nothing here is doctrine; scripts observe and report, and humans and auditors decide. Everything is stdlib-only Python except the Candidate 3 script (see its dependencies below). No script in this folder calls a model API.

## What's here

| File | What it does | How you run it |
|------|--------------|----------------|
| `AUDIT_HARNESS.py` (v16) | Fetches `Forge_Audit_Kit.md`, the target file, and any extra files from GitHub `main`, runs Phase 1 structural checks, and returns a ready-to-paste audit prompt plus findings. It does not call a model; you paste the prompt into an agent session. | `Colab_Launcher.py` |
| `integrity_check.py` | Repo-wide checks: Routing.md coverage, Ethical Anchor and File State, duplicate sidecar IDs, cross-reference resolution, version-citation drift. `--health` adds active-unknown counts by priority. Deliberately emits no readiness or governance-state badge. | `Colab_Integrity.py`, or `python integrity_check.py <repo_root> [--json out.json] [--health]` |
| `cold_session_bundler.py` | Builds an informationally independent audit payload (AP-017): raw doctrine text with retrospective findings and evaluative metadata stripped, plus a manifest of what was removed. Best-effort, not a formal guarantee. | `Colab_cold_session.py` |
| `Candidate3_Transient_Index_Colab.py` | The pre-registered Persistent Cognition Candidate 3 experiment. See its section below. | Upload a zip, Run all |
| `audit_lib.py` | Shared library: Routing.md parsing, cross-reference extraction, `Finding` class. Imported by the harness and the integrity checker so routing logic lives in one place (AP-025/AP-026). | Imported, not run |
| `parser.py` | Metadata parser (evidence ledger, conflicts preserved) and section extractor for blind review. Imported by the integrity checker. | Imported, not run |
| `Colab_Launcher.py`, `Colab_Integrity.py`, `Colab_cold_session.py` | Paste-and-run Colab cells. Each clones GitHub `main` into `/content/LazarusForge`, adds `Automation/` to the path, and calls the tool above. Edit the target file or focus string at the top of the cell as needed. | Paste into a Colab cell |
| `Cold_session_manifest.py` | A saved example manifest from a bundler run (2026-08-03). Despite the `.py` extension it is JSON, not runnable Python. Kept under this name because Routing.md registers it that way. | Reference only |

## Which tool for which job

- **"Is the repo internally consistent?"** `integrity_check.py`.
- **"Audit this file with full context."** `AUDIT_HARNESS.py`.
- **"Audit this file without priming."** `cold_session_bundler.py`. The bundle goes to a brand-new chat as the very first message, with no framing added. The manifest stays with you and is never pasted to the auditor.
- **"Does transient retrieval recover prior reasoning better than routing?"** Candidate 3 below.

## Things to know

- The three Colab launchers audit what is committed to GitHub `main`, not a local zip. Candidate 3 works from an uploaded zip or folder. Keep the two apart when comparing results.
- `integrity_check.py` imports `ALIASES` from `AUDIT_HARNESS.py`. If that import fails, the reference pass degrades to an empty alias map and says so.
- As observed on the 1.17 release (2026-09-28), the 14 "duplicate sidecar ID" criticals are all pairs where one copy lives under `Archive/`. Re-check this before relying on it; it is a snapshot, not a standing claim.

---

# Candidate 3: Transient Embedding Index (Colab)

Self-contained script for the pre-registered Persistent Cognition Candidate 3 experiment. As of `Tests/Persistent_Cognition_Candidates.md` v0.15 the experiment is design-only and has not been run.

## Quick start (Google Colab)

1. Upload a LazarusForge release zip to the Colab session files (or upload the extracted folder). Any tree containing `Routing.md` is found automatically. The original `LazarusForge_Unified_2026-09-27.zip` / `lf116-merged` names still work as backward-compatible defaults.
2. Upload `Candidate3_Transient_Index_Colab.py` (or open it in a notebook cell).
3. Runtime, then Run all (or `!python Candidate3_Transient_Index_Colab.py`).

The script will:
- Locate the repo tree (see step 1)
- Build **Corpus A** (distilled) and **Corpus B** (history) per the locked boundaries
- Create two **in-memory** Chroma indexes (sentence-transformers `all-MiniLM-L6-v2`)
- Run all **14 frozen queries**
- Write `candidate3_results.json`
- **Discard** both indexes

No durable artifact is left in the repository.

## Dependencies
Installed automatically on first run if missing:
- `sentence-transformers`
- `chromadb`

## Output
`candidate3_results.json`: one entry per query with top-k hits from Corpus A and Corpus B (source, section, text snippet). Use this file for the pre-registered scoring dimensions. The file also records which repo state was indexed: `repo_root`, `source_zip`, `source_zip_sha256`, and `md_file_count`, so results can be tied to a specific release.

## Notes
- `Tests/Persistent_Cognition_Candidates.md` is excluded from both corpora (self-contamination guard).
- `external_tests/Memory_Bridge_Test.md` is outside the repo tree and is not indexed.
- This is the **Candidate 3 condition** (transient semantic retrieval). Uploading the zip and asking the model to read files directly is the **ordinary-routing baseline**, not this experiment.
- The queries omit the backtick code formatting the frozen table uses around file names; wording and quotation marks match the table exactly.

## Known coverage limit (recorded before any run)
Corpus boundaries are locked, so this is documented, not changed. For Query 10, the ground-truth source is `Admin/Auditor_Protocols.md` AP-033. The AP-033 rule body sits outside the sections the script collects from that file (Resolution Log and Lessons Learned); only later references to AP-033 are indexed. A Query 10 miss therefore reflects the corpus boundary, not retrieval quality, and should be scored accordingly. The ground-truth passages for Queries 9 and 12 were checked and are inside collected sections.

## Corrections applied 2026-09-27 (Claude, before first run)
Queries 10, 11, and 12 had drifted from the actual frozen text in
`Tests/Persistent_Cognition_Candidates.md`, reworded in ways that changed what was being
asked, not just reformatted (e.g. Q11 asked "why was that change made?" instead of the
frozen "why didn't the original CIR-F02 review catch it?", a materially easier question).
Query 14 had also dropped a clause. All four corrected to match the frozen table exactly
before this script's first run, since running against altered queries would test an
unregistered question set rather than the pre-registered one. No other lines changed.

## Corrections applied 2026-09-28 (Claude, human-directed, before first run)
- Query 8, 4, and 9 now match the frozen table character for character: Q8 had hyphenated "not-yet-implemented" where the table has the quoted phrase "not yet implemented"; Q4 and Q9 had dropped the quotation marks around "CIR v2.0" and "Resolved 2026-08-03". Verified 14/14 exact matches against the v0.15 table.
- Repo location generalized (any tree containing `Routing.md`, any `LazarusForge*.zip`); tested against the 1.17 zip and an extracted folder.
- Provenance fields added to the results file.
- Corpus collection is unchanged: Corpus A and Corpus B are identical to before (67 and 103 source slices on 1.17).
