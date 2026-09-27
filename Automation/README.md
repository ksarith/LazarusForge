# Candidate 3 — Transient Embedding Index (Colab)

Self-contained script for the pre-registered Persistent Cognition Candidate 3 experiment.

## Quick start (Google Colab)

1. Upload `LazarusForge_Unified_2026-09-27.zip` to the Colab session files.
2. Upload `Candidate3_Transient_Index_Colab.py` (or open it in a notebook cell).
3. Runtime → Run all (or `!python Candidate3_Transient_Index_Colab.py`).

The script will:
- Extract / locate the `lf116-merged` tree
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
`candidate3_results.json` — one entry per query with top-k hits from Corpus A and Corpus B (source, section, text snippet). Use this file for the pre-registered scoring dimensions.

## Notes
- `Tests/Persistent_Cognition_Candidates.md` is excluded from both corpora (self-contamination guard).
- `external_tests/Memory_Bridge_Test.md` is outside the repo tree and is not indexed.
- This is the **Candidate 3 condition** (transient semantic retrieval).  
  Uploading the zip and asking the model to read files directly is the **ordinary-routing baseline**, not this experiment.

## Correction applied 2026-09-27 (Claude, before first run)
Queries 10, 11, and 12 had drifted from the actual frozen text in
`Tests/Persistent_Cognition_Candidates.md` — reworded in ways that changed what was being
asked, not just reformatted (e.g. Q11 asked "why was that change made?" instead of the
frozen "why didn't the original CIR-F02 review catch it?" — a materially easier question).
Query 14 had also dropped a clause. All four corrected to match the frozen table exactly
before this script's first run, since running against altered queries would test an
unregistered question set rather than the pre-registered one. No other lines changed.
