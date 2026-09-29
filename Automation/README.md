# Candidate 3 — Transient Embedding Index (Colab)

## Scripts

| File | Mode | Notes |
|------|------|-------|
| `Candidate3_Transient_Index_Colab.py` | Dense only (Run 1) | Bi-encoder cosine; original pre-registered path |
| `Candidate3_Transient_Index_Colab_hybrid.py` | **Hybrid dense + BM25** | Controlled ranking increment |

## Hybrid increment (new)

Final score per chunk:

```text
score = α * dense_normalized + (1-α) * bm25_normalized
```

- Default `ALPHA = 0.6` (dense weight)
- Set `ALPHA = 1.0` to reproduce pure dense / Run 1 ranking
- BM25 is pure Python (no extra dependency)
- Same corpora, same 14 frozen queries, same top-k=5
- Still fully transient: build → query → discard

### What this is meant to test
- Whether exact tokens (`GMP-011`, `§VII.5`, `ENV-007`, `Resolved 2026-08-03`, …) pull the right Resolution Log / sidecar chunks above Canonical_Terms attractors
- Whether Q5 / Q9-style misses enter the top-5 at all
- Rank movement of ground-truth sources vs Run 1 (especially Q10 rank-3 → rank-1)

### Quick start (Colab)
1. Upload a 1.17 repo zip (master / unified / Alpha).
2. Upload `Candidate3_Transient_Index_Colab_hybrid.py`.
3. Runtime → Run all.

Output: `candidate3_results_hybrid.json`

### Comparison discipline
Score hybrid results with the same six pre-registered dimensions and the same frozen query table. Do not alter queries or corpus boundaries between Run 1 and the hybrid run.
