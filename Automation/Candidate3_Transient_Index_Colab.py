# =============================================================================
# Candidate 3 — Transient Embedding Index (Colab / local)
# LazarusForge Persistent Cognition experiment
# Pre-registered design: build → query 14 frozen queries → discard
# =============================================================================
# Usage (Colab):
#   1. Upload LazarusForge_Unified_2026-09-27.zip (or the lf116-merged folder)
#   2. Runtime → Run all
#   3. Results are printed and also written to candidate3_results.json
# =============================================================================

import os, re, json, zipfile, tempfile, shutil
from pathlib import Path
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# 0. Config — change only if your paths differ
# ---------------------------------------------------------------------------
ZIP_NAME = "LazarusForge_Unified_2026-09-27.zip"   # uploaded to Colab root
REPO_ROOT_NAME = "lf116-merged"                    # folder inside the zip
RESULTS_FILE = "candidate3_results.json"
TOP_K = 5
CHUNK_SIZE = 500          # characters
CHUNK_OVERLAP = 80
EMBED_MODEL = "all-MiniLM-L6-v2"

# ---------------------------------------------------------------------------
# 1. Locate / extract repo
# ---------------------------------------------------------------------------
def locate_repo():
    cwd = Path.cwd()
    # already extracted?
    direct = cwd / REPO_ROOT_NAME
    if direct.is_dir():
        return direct
    # zip present?
    zpath = cwd / ZIP_NAME
    if zpath.is_file():
        extract_dir = cwd / "_extracted_repo"
        if extract_dir.exists():
            shutil.rmtree(extract_dir)
        extract_dir.mkdir()
        with zipfile.ZipFile(zpath, "r") as z:
            z.extractall(extract_dir)
        # zip contains unified_build/lf116-merged or just lf116-merged
        candidates = list(extract_dir.rglob(REPO_ROOT_NAME))
        if not candidates:
            raise FileNotFoundError(f"Could not find {REPO_ROOT_NAME} inside zip")
        return candidates[0]
    raise FileNotFoundError(
        f"Neither {REPO_ROOT_NAME}/ nor {ZIP_NAME} found in {cwd}. "
        "Upload the unified zip or the extracted tree first."
    )

# ---------------------------------------------------------------------------
# 2. Corpus boundaries (from Persistent_Cognition_Candidates.md step 2)
# ---------------------------------------------------------------------------
# Corpus A — distilled knowledge only
CORPUS_A_GLOBS = [
    "Tests/Cognitive_Salvage_Layer.md",
    "Admin/Canonical_Terms.md",
    "Admin/Metrics_Scaffold.md",
]
# Also include any file that has a "## Lessons Learned" section (handled below)

# Corpus B — cognitive history
CORPUS_B_GLOBS = [
    "Unknowns.md",
    "Admin/Progress_Log.md",
    "Admin/Governance_Migration_Protocol.md",
    "Admin/Ethical_Constraints.md",
    "Admin/Computational_Institutional_Reasoning.md",
    "Admin/Environmental_Constraints.md",
    "Admin/Repository_Integrity_Protocol.md",
    "Architecture/Chemistry.md",
    "Tests/Support_Raft.md",
    "Tests/Persistent_Cognition_Candidates.md",  # excluded from index by design note; kept out below
]

EXCLUDE_FROM_BOTH = {
    "Tests/Persistent_Cognition_Candidates.md",  # self-contamination guard
}

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  warn: could not read {path}: {e}")
        return ""

def extract_section(text: str, heading_regex: str) -> str:
    """Return the body under the first matching markdown heading, or empty."""
    pattern = rf"(?m)^(##+\s+{heading_regex}\s*)$(.*?)(?=^##+\s|\Z)"
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return (m.group(2).strip() if m else "")

def collect_corpus_a(repo: Path):
    docs = []
    for rel in CORPUS_A_GLOBS:
        p = repo / rel
        if p.is_file() and rel not in EXCLUDE_FROM_BOTH:
            docs.append((str(rel), "full", read_text(p)))
    # Lessons Learned sections across the tree
    for p in repo.rglob("*.md"):
        rel = str(p.relative_to(repo))
        if rel in EXCLUDE_FROM_BOTH:
            continue
        text = read_text(p)
        lessons = extract_section(text, r"Lessons Learned")
        if lessons and len(lessons) > 40:
            docs.append((rel, "Lessons Learned", lessons))
    return docs

def collect_corpus_b(repo: Path):
    docs = []
    for rel in CORPUS_B_GLOBS:
        if rel in EXCLUDE_FROM_BOTH:
            continue
        p = repo / rel
        if p.is_file():
            text = read_text(p)
            # Prefer Resolution Log / Auditor / rejection-note slices when present
            for section_name in [
                r"Resolution Log",
                r"Auditor Notes.*",
                r"File State",
            ]:
                sec = extract_section(text, section_name)
                if sec and len(sec) > 40:
                    docs.append((rel, section_name, sec))
            # Always keep a full-file fallback for files that are mostly history
            docs.append((rel, "full", text))
    # Also sweep for any other Resolution Log sections
    for p in repo.rglob("*.md"):
        rel = str(p.relative_to(repo))
        if rel in EXCLUDE_FROM_BOTH or any(rel.endswith(g.split("/")[-1]) for g in CORPUS_B_GLOBS):
            continue
        text = read_text(p)
        res = extract_section(text, r"Resolution Log")
        if res and len(res) > 80:
            docs.append((rel, "Resolution Log", res))
    return docs

# ---------------------------------------------------------------------------
# 3. Chunking
# ---------------------------------------------------------------------------
def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) <= size:
        return [text] if text else []
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks

# ---------------------------------------------------------------------------
# 4. Frozen queries (from Persistent_Cognition_Candidates.md — DO NOT ALTER)
# ---------------------------------------------------------------------------
FROZEN_QUERIES = [
    {"id": 1, "class": "Decision history",
     "query": "Why does GMP-011's Genesis Phase holding clause anchor to Governance_Charter.md rather than to Governance_Migration_Protocol.md §VII.5?"},
    {"id": 2, "class": "Decision history",
     "query": "Why was the CE-006 vessel design sketch integrated only after two rounds of correction rather than accepted on the first pass?"},
    {"id": 3, "class": "Rejected reasoning",
     "query": "Why was the independent Grok/Copilot thread's GOV-008 registry patch to Governance_Charter.md rejected, and what was preserved from it instead?"},
    {"id": 4, "class": "Rejected reasoning",
     "query": "Why was the 2026-07-29 CIR v2.0 bundle held as unratified draft material rather than applied alongside CIR-F02/CIR-F03?"},
    {"id": 5, "class": "Unknown history",
     "query": "What was previously unresolved about ENV-007 and ENV-008, and how long had each sat unrevisited before being corrected?"},
    {"id": 6, "class": "Unknown history",
     "query": "What was GOV-008's status before the §VII.8 registry-schema extension, and did that extension change it?"},
    {"id": 7, "class": "Resolution history",
     "query": "How was the Support_Raft induction-loss discrepancy (12% laboratory vs. 20–40% real subsea conditions) resolved and logged?"},
    {"id": 8, "class": "Resolution history",
     "query": "How was RIP-002's not-yet-implemented status corrected, and what exactly was verified to justify the change?"},
    {"id": 9, "class": "Governance reasoning",
     "query": "Why was the Closed_Loop_Feedstock draft's Resolved 2026-08-03 status claim rejected rather than accepted?"},
    {"id": 10, "class": "Governance reasoning",
     "query": "Why does AP-033 (Rule 9) require confirmed governance-file access before a contribution can be treated as authoritative?"},
    {"id": 11, "class": "Technical reasoning",
     "query": "What led to CIR-F03's correction of Φ(n)'s trigger condition from S(n)=0 to S(n)≤ε, and why was that change made?"},
    {"id": 12, "class": "Technical reasoning",
     "query": "Why was Architecture/Engineering.md's unknown-history safety factor corrected from 3× to a different value?"},
    {"id": 13, "class": "Cross-document reasoning",
     "query": "Beyond GMP-011, where else does the same failure pattern appear — an unratified section cited as though it supports the opposite of what it actually says?"},
    {"id": 14, "class": "Cross-document reasoning",
     "query": "How does CIR §4.3's Provenance Ceiling Gate relate to Auditor_Protocols.md's Institutional Provenance Labels, and where was that relationship first made explicit?"},
]

# ---------------------------------------------------------------------------
# 5. Build transient index (Chroma in-memory)
# ---------------------------------------------------------------------------
def build_index(docs, collection_name: str):
    """
    docs: list of (source_relpath, section, text)
    Returns (collection, model, client)
    """
    try:
        from sentence_transformers import SentenceTransformer
        import chromadb
    except ImportError:
        print("Installing sentence-transformers and chromadb ...")
        import subprocess, sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q",
                               "sentence-transformers", "chromadb"])
        from sentence_transformers import SentenceTransformer
        import chromadb

    model = SentenceTransformer(EMBED_MODEL)
    client = chromadb.Client()  # pure in-memory — dies with the process
    # drop if re-run in same runtime
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass
    collection = client.create_collection(collection_name)

    documents, metadatas, ids, embeddings = [], [], [], []
    idx = 0
    for source, section, text in docs:
        for ci, chunk in enumerate(chunk_text(text)):
            documents.append(chunk)
            metadatas.append({"source": source, "section": section, "chunk": ci})
            ids.append(f"{collection_name}_{idx}")
            idx += 1

    if not documents:
        print(f"  WARNING: no documents for {collection_name}")
        return collection, model, client

    print(f"  Embedding {len(documents)} chunks for {collection_name} ...")
    emb = model.encode(documents, show_progress_bar=True)
    collection.add(
        documents=documents,
        embeddings=emb.tolist(),
        metadatas=metadatas,
        ids=ids,
    )
    print(f"  Index ready: {collection_name} ({len(documents)} chunks)")
    return collection, model, client

def query_index(collection, model, query_text: str, k: int = TOP_K):
    q_emb = model.encode([query_text]).tolist()
    res = collection.query(query_embeddings=q_emb, n_results=k)
    hits = []
    for i in range(len(res["ids"][0])):
        hits.append({
            "rank": i + 1,
            "source": res["metadatas"][0][i].get("source"),
            "section": res["metadatas"][0][i].get("section"),
            "text": res["documents"][0][i][:600],
        })
    return hits

# ---------------------------------------------------------------------------
# 6. Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("Candidate 3 — Transient Embedding Index")
    print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print("=" * 70)

    repo = locate_repo()
    print(f"Repo root: {repo}")

    print("\nCollecting Corpus A (distilled) ...")
    corpus_a = collect_corpus_a(repo)
    print(f"  {len(corpus_a)} source slices")

    print("Collecting Corpus B (history) ...")
    corpus_b = collect_corpus_b(repo)
    print(f"  {len(corpus_b)} source slices")

    print("\nBuilding transient indexes ...")
    col_a, model, client = build_index(corpus_a, "corpus_a_distilled")
    col_b, _, _ = build_index(corpus_b, "corpus_b_history")

    results = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "embed_model": EMBED_MODEL,
        "top_k": TOP_K,
        "queries": [],
    }

    print("\n" + "=" * 70)
    print("Running frozen queries")
    print("=" * 70)

    for q in FROZEN_QUERIES:
        print(f"\n--- Query {q['id']} [{q['class']}] ---")
        print(f"Q: {q['query']}")
        hits_a = query_index(col_a, model, q["query"])
        hits_b = query_index(col_b, model, q["query"])
        print(f"  Corpus A top hit: {hits_a[0]['source'] if hits_a else 'NONE'}")
        print(f"  Corpus B top hit: {hits_b[0]['source'] if hits_b else 'NONE'}")
        results["queries"].append({
            "id": q["id"],
            "class": q["class"],
            "query": q["query"],
            "corpus_a": hits_a,
            "corpus_b": hits_b,
        })

    # Persist results for later scoring
    out = Path(RESULTS_FILE)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nResults written to {out.resolve()}")

    # Explicit discard
    print("\nDiscarding transient indexes ...")
    try:
        client.delete_collection("corpus_a_distilled")
        client.delete_collection("corpus_b_history")
    except Exception:
        pass
    print("Done. Indexes discarded. Markdown files remain the sole durable source.")
    print("=" * 70)

if __name__ == "__main__":
    main()
