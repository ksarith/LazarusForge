# =============================================================================
# Candidate 3 — Transient Embedding Index + Hybrid BM25 (Colab / local)
# LazarusForge Persistent Cognition experiment — controlled ranking increment
# Pre-registered design: build → query 14 frozen queries → discard
#
# Change vs Run 1 (dense-only):
#   Final score = α * dense_cosine + (1-α) * bm25_normalized
#   Same corpora, same chunks, same queries — only the fusion step is new.
# =============================================================================

import os, re, json, zipfile, shutil, math
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

# ---------------------------------------------------------------------------
# 0. Config
# ---------------------------------------------------------------------------
ZIP_CANDIDATES = [
    "LazarusForge-1_17_Alpha_master.zip",
    "LazarusForge-1_17_Alpha_unified.zip",
    "LazarusForge_Unified_2026-09-27.zip",
    "LazarusForge-1.17.Alpha.zip",
]
REPO_ROOT_NAMES = ["LazarusForge-1.17.Alpha", "lf116-merged", "LazarusForge-1.16.Alpha"]
RESULTS_FILE = "candidate3_results_hybrid.json"
TOP_K = 5
POOL_N = 40              # candidates from each channel before fusion
CHUNK_SIZE = 500
CHUNK_OVERLAP = 80
EMBED_MODEL = "all-MiniLM-L6-v2"
ALPHA = 0.6              # dense weight; set 1.0 to reproduce pure dense (Run 1)
BM25_K1 = 1.5
BM25_B = 0.75

# ---------------------------------------------------------------------------
# 1. Locate / extract repo
# ---------------------------------------------------------------------------
def locate_repo():
    cwd = Path.cwd()
    for name in REPO_ROOT_NAMES:
        direct = cwd / name
        if direct.is_dir():
            return direct
    # Drive / content paths common in Colab
    for base in [cwd, Path("/content"), Path("/content/drive/MyDrive"), Path("/content/drive/My Drive")]:
        if not base.exists():
            continue
        zips = sorted(base.glob("**/LazarusForge*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
        for zpath in zips:
            extract_dir = cwd / "_extracted_repo"
            if extract_dir.exists():
                shutil.rmtree(extract_dir)
            extract_dir.mkdir()
            print(f"  note: extracting {zpath}")
            with zipfile.ZipFile(zpath, "r") as z:
                z.extractall(extract_dir)
            for name in REPO_ROOT_NAMES:
                hits = list(extract_dir.rglob(name))
                if hits:
                    return hits[0]
    raise FileNotFoundError(
        f"No repo root among {REPO_ROOT_NAMES} and no LazarusForge*.zip found."
    )

# ---------------------------------------------------------------------------
# 2. Corpus boundaries (unchanged from pre-registered design)
# ---------------------------------------------------------------------------
CORPUS_A_GLOBS = [
    "Tests/Cognitive_Salvage_Layer.md",
    "Admin/Canonical_Terms.md",
    "Admin/Metrics_Scaffold.md",
]
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
]
EXCLUDE_FROM_BOTH = {
    "Tests/Persistent_Cognition_Candidates.md",
}

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  warn: could not read {path}: {e}")
        return ""

def extract_section(text: str, heading_regex: str) -> str:
    pattern = rf"(?m)^(##+\s+{heading_regex}\s*)$(.*?)(?=^##+\s|\Z)"
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return (m.group(2).strip() if m else "")

def collect_corpus_a(repo: Path):
    docs = []
    for rel in CORPUS_A_GLOBS:
        p = repo / rel
        if p.is_file() and rel not in EXCLUDE_FROM_BOTH:
            docs.append((str(rel), "full", read_text(p)))
    for p in repo.rglob("*.md"):
        rel = str(p.relative_to(repo)).replace("\\", "/")
        if rel in EXCLUDE_FROM_BOTH:
            continue
        text = read_text(p)
        lessons = extract_section(text, r"Lessons Learned")
        if lessons and len(lessons) > 40:
            docs.append((rel, "Lessons Learned", lessons))
    return docs

def collect_corpus_b(repo: Path):
    docs = []
    seen = set()
    for rel in CORPUS_B_GLOBS:
        if rel in EXCLUDE_FROM_BOTH:
            continue
        p = repo / rel
        if p.is_file():
            text = read_text(p)
            for section_name in [r"Resolution Log", r"Auditor Notes.*", r"File State"]:
                sec = extract_section(text, section_name)
                if sec and len(sec) > 40:
                    docs.append((rel, section_name, sec))
            docs.append((rel, "full", text))
            seen.add(rel)
    for p in repo.rglob("*.md"):
        rel = str(p.relative_to(repo)).replace("\\", "/")
        if rel in EXCLUDE_FROM_BOTH or rel in seen:
            continue
        text = read_text(p)
        res = extract_section(text, r"Resolution Log")
        if res and len(res) > 80:
            docs.append((rel, "Resolution Log", res))
    return docs

def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) <= size:
        return [text] if text else []
    chunks, start = [], 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks

# ---------------------------------------------------------------------------
# 3. Frozen queries (DO NOT ALTER — from Persistent_Cognition_Candidates.md)
# ---------------------------------------------------------------------------
FROZEN_QUERIES = [
    {"id": 1, "class": "Decision history",
     "query": "Why does GMP-011's Genesis Phase holding clause anchor to Governance_Charter.md rather than to Governance_Migration_Protocol.md §VII.5?"},
    {"id": 2, "class": "Decision history",
     "query": "Why was the CE-006 vessel design sketch integrated only after two rounds of correction rather than accepted on the first pass?"},
    {"id": 3, "class": "Rejected reasoning",
     "query": "Why was the independent Grok/Copilot thread's GOV-008 registry patch to Governance_Charter.md rejected, and what was preserved from it instead?"},
    {"id": 4, "class": "Rejected reasoning",
     "query": "Why was the 2026-07-29 \"CIR v2.0\" bundle held as unratified draft material rather than applied alongside CIR-F02/CIR-F03?"},
    {"id": 5, "class": "Unknown history",
     "query": "What was previously unresolved about ENV-007 and ENV-008, and how long had each sat unrevisited before being corrected?"},
    {"id": 6, "class": "Unknown history",
     "query": "What was GOV-008's status before the §VII.8 registry-schema extension, and did that extension change it?"},
    {"id": 7, "class": "Resolution history",
     "query": "How was the Support_Raft induction-loss discrepancy (12% laboratory vs. 20–40% real subsea conditions) resolved and logged?"},
    {"id": 8, "class": "Resolution history",
     "query": "How was RIP-002's \"not yet implemented\" status corrected, and what exactly was verified to justify the change?"},
    {"id": 9, "class": "Governance reasoning",
     "query": "Why was the Closed_Loop_Feedstock draft's \"Resolved 2026-08-03\" status claim rejected rather than accepted?"},
    {"id": 10, "class": "Governance reasoning",
     "query": "Why does AP-033 (Rule 9) require confirmed governance-file access before a contribution can mark an unknown toward Resolved status?"},
    {"id": 11, "class": "Technical reasoning",
     "query": "What led to CIR-F03's correction of Φ(n)'s trigger condition from S(n)=0 to S(n)≤ε, and why didn't the original CIR-F02 review catch it?"},
    {"id": 12, "class": "Technical reasoning",
     "query": "Why was Architecture/Engineering.md's unknown-history safety factor corrected from 3× to 6×+?"},
    {"id": 13, "class": "Cross-document reasoning",
     "query": "Beyond GMP-011, where else does the same failure pattern appear — an unratified section cited as though it supports the opposite of what it actually says?"},
    {"id": 14, "class": "Cross-document reasoning",
     "query": "How does CIR §4.3's Provenance Ceiling Gate relate to Auditor_Protocols.md's Institutional Provenance Labels, and where was that relationship first made explicit rather than merely implied?"},
]

# ---------------------------------------------------------------------------
# 4. Tokenization + BM25 (pure Python, no extra dependency required)
# ---------------------------------------------------------------------------
_TOKEN_RE = re.compile(r"[A-Za-z0-9_§Φε×\-\.]+")

def tokenize(text: str):
    return [t.lower() for t in _TOKEN_RE.findall(text)]

class BM25:
    """Minimal Okapi BM25 over an in-memory list of tokenized docs."""
    def __init__(self, corpus_tokens, k1=BM25_K1, b=BM25_B):
        self.k1 = k1
        self.b = b
        self.corpus = corpus_tokens
        self.N = len(corpus_tokens)
        self.doc_len = [len(doc) for doc in corpus_tokens]
        self.avgdl = sum(self.doc_len) / self.N if self.N else 0.0
        self.df = defaultdict(int)
        for doc in corpus_tokens:
            for t in set(doc):
                self.df[t] += 1
        self.idf = {
            t: math.log(1 + (self.N - df + 0.5) / (df + 0.5))
            for t, df in self.df.items()
        }

    def scores(self, query_tokens):
        out = [0.0] * self.N
        if not query_tokens or self.N == 0:
            return out
        for i, doc in enumerate(self.corpus):
            if not doc:
                continue
            tf = defaultdict(int)
            for t in doc:
                tf[t] += 1
            score = 0.0
            dl = self.doc_len[i]
            for t in query_tokens:
                if t not in tf:
                    continue
                idf = self.idf.get(t, 0.0)
                freq = tf[t]
                denom = freq + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                score += idf * (freq * (self.k1 + 1)) / denom
            out[i] = score
        return out

def min_max_norm(values):
    if not values:
        return values
    lo, hi = min(values), max(values)
    if hi - lo < 1e-12:
        return [0.0] * len(values)
    return [(v - lo) / (hi - lo) for v in values]

# ---------------------------------------------------------------------------
# 5. Build dense index + BM25 side structure
# ---------------------------------------------------------------------------
def build_hybrid_index(docs, collection_name: str):
    """
    docs: list of (source, section, text)
    Returns dict with collection, model, client, bm25, chunk_meta, documents
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
    client = chromadb.Client()
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass
    collection = client.create_collection(collection_name)

    documents, metadatas, ids, corpus_tokens = [], [], [], []
    idx = 0
    for source, section, text in docs:
        for ci, chunk in enumerate(chunk_text(text)):
            documents.append(chunk)
            metadatas.append({"source": source, "section": section, "chunk": ci})
            ids.append(f"{collection_name}_{idx}")
            corpus_tokens.append(tokenize(chunk))
            idx += 1

    if not documents:
        print(f"  WARNING: no documents for {collection_name}")
        return {
            "collection": collection, "model": model, "client": client,
            "bm25": BM25([]), "metadatas": [], "documents": [], "ids": [],
        }

    print(f"  Embedding {len(documents)} chunks for {collection_name} ...")
    emb = model.encode(documents, show_progress_bar=True)
    collection.add(
        documents=documents,
        embeddings=emb.tolist(),
        metadatas=metadatas,
        ids=ids,
    )
    bm25 = BM25(corpus_tokens)
    print(f"  Index ready: {collection_name} ({len(documents)} chunks, BM25 built)")
    return {
        "collection": collection,
        "model": model,
        "client": client,
        "bm25": bm25,
        "metadatas": metadatas,
        "documents": documents,
        "ids": ids,
    }

def hybrid_query(index, query_text: str, k: int = TOP_K, pool: int = POOL_N, alpha: float = ALPHA):
    """
    Fuse dense cosine top-pool with BM25 top-pool.
    alpha=1.0 → pure dense (Run 1 equivalent).
    """
    model = index["model"]
    collection = index["collection"]
    bm25 = index["bm25"]
    metadatas = index["metadatas"]
    documents = index["documents"]
    ids = index["ids"]
    n = len(documents)
    if n == 0:
        return []

    # Dense channel
    q_emb = model.encode([query_text]).tolist()
    dense_res = collection.query(
        query_embeddings=q_emb,
        n_results=min(pool, n),
        include=["documents", "metadatas", "distances"],
    )
    dense_scores = {}  # id -> similarity (1 - distance for cosine L2 in chroma default)
    for i, cid in enumerate(dense_res["ids"][0]):
        dist = dense_res["distances"][0][i]
        # Chroma default L2 on normalized vectors ≈ 2-2*cos; convert roughly to sim
        sim = 1.0 / (1.0 + dist)
        dense_scores[cid] = sim

    # BM25 channel
    q_tokens = tokenize(query_text)
    bm25_raw = bm25.scores(q_tokens)
    # take top pool by bm25
    bm25_ranked = sorted(range(n), key=lambda i: bm25_raw[i], reverse=True)[:pool]
    bm25_scores = {ids[i]: bm25_raw[i] for i in bm25_ranked}

    # Union of candidates
    cand_ids = list(set(dense_scores.keys()) | set(bm25_scores.keys()))
    if not cand_ids:
        return []

    d_vals = [dense_scores.get(c, 0.0) for c in cand_ids]
    b_vals = [bm25_scores.get(c, 0.0) for c in cand_ids]
    d_norm = min_max_norm(d_vals)
    b_norm = min_max_norm(b_vals)

    fused = []
    for i, cid in enumerate(cand_ids):
        score = alpha * d_norm[i] + (1.0 - alpha) * b_norm[i]
        # map back to row
        try:
            row = ids.index(cid)
        except ValueError:
            continue
        fused.append((score, row, cid))
    fused.sort(key=lambda x: x[0], reverse=True)

    hits = []
    for rank, (score, row, cid) in enumerate(fused[:k], start=1):
        hits.append({
            "rank": rank,
            "score": round(score, 4),
            "source": metadatas[row].get("source"),
            "section": metadatas[row].get("section"),
            "text": documents[row][:600],
        })
    return hits

# ---------------------------------------------------------------------------
# 6. Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("Candidate 3 — Transient Index + Hybrid BM25")
    print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print(f"ALPHA (dense weight) = {ALPHA}   [1.0 = pure dense / Run 1 equivalent]")
    print("=" * 70)

    repo = locate_repo()
    print(f"Repo root: {repo}")

    print("\nCollecting Corpus A (distilled) ...")
    corpus_a = collect_corpus_a(repo)
    print(f"  {len(corpus_a)} source slices")

    print("Collecting Corpus B (history) ...")
    corpus_b = collect_corpus_b(repo)
    print(f"  {len(corpus_b)} source slices")

    print("\nBuilding hybrid indexes (dense + BM25) ...")
    idx_a = build_hybrid_index(corpus_a, "corpus_a_distilled")
    idx_b = build_hybrid_index(corpus_b, "corpus_b_history")

    results = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "embed_model": EMBED_MODEL,
        "alpha_dense": ALPHA,
        "md_file_count": sum(1 for _ in repo.rglob("*.md")),
        "top_k": TOP_K,
        "pool_n": POOL_N,
        "mode": "hybrid_dense_bm25",
        "queries": [],
    }

    print("\n" + "=" * 70)
    print("Running frozen queries (hybrid)")
    print("=" * 70)

    for q in FROZEN_QUERIES:
        print(f"\n--- Query {q['id']} [{q['class']}] ---")
        print(f"Q: {q['query']}")
        hits_a = hybrid_query(idx_a, q["query"])
        hits_b = hybrid_query(idx_b, q["query"])
        print(f"  Corpus A top hit: {hits_a[0]['source'] if hits_a else 'NONE'}")
        print(f"  Corpus B top hit: {hits_b[0]['source'] if hits_b else 'NONE'}")
        results["queries"].append({
            "id": q["id"],
            "class": q["class"],
            "query": q["query"],
            "corpus_a": hits_a,
            "corpus_b": hits_b,
        })

    out = Path(RESULTS_FILE)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nResults written to {out.resolve()}")

    print("\nDiscarding transient indexes ...")
    try:
        idx_a["client"].delete_collection("corpus_a_distilled")
        idx_b["client"].delete_collection("corpus_b_history")
    except Exception:
        pass
    print("Done. Indexes discarded. Markdown remains sole durable source.")
    print("=" * 70)

if __name__ == "__main__":
    main()
