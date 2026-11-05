#!/usr/bin/env python3
"""
validate_registry.py — machine-checkable gate behind REGISTRY.md / MODELS.md.

Catches:
  1.  File on disk (tracked dirs) with no registry.yaml entry
  2.  Registry entry pointing at a nonexistent path
  3.  Duplicate model_id values
  4.  Duplicate parameter_id values in parameters/swarm_v3.yaml
  5.  EXEC-FULL / EXEC-PARTIAL (non-DEPRECATED MODEL or BUILD) without a
      passing test_ref
  6.  DEPRECATED model imported by anything under src/
  7.  Invalid taxonomy enum values
  8.  Missing required fields on entries
  9.  Duplicate registry paths
 10.  AUTHORITATIVE-MODEL without a validation status
 11.  PROVENANCED / PARTIALLY-PROVENANCED without model-level notes or
      parameter file linkage where expected
 12.  Production Python modules outside src/astroid_miner/
 13.  Production code (src/) importing experiments/ or archive/
 14.  BUILD/MODEL entries under src/ that claim EXEC-* without test_ref

Usage:
    python3 tools/validate_registry.py

Exit 0 = clean. Exit 1 = problems. Exit 2 = missing dependency.
"""

from __future__ import annotations

import ast
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML is required to run this validator "
        "(pip install pyyaml --break-system-packages)."
    )
    sys.exit(2)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REGISTRY_PATH = os.path.join(REPO_ROOT, "registry.yaml")
PARAMS_PATH = os.path.join(REPO_ROOT, "parameters", "swarm_v3.yaml")

TRACKED_DIRS = [
    "docs",
    "src",
    "experiments",
    "archive",
    "parameters",
    "tools",
    "tests",
]
TRACKED_ROOT_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "Discovery.md",
    "LONG_HORIZON.md",
    "REGISTRY.md",
    "MODELS.md",
    "registry.yaml",
    "pyproject.toml",
]

IGNORE_BASENAMES = {"__init__.py"}
IGNORE_PATTERNS = [
    re.compile(r"__pycache__"),
    re.compile(r"\.egg-info"),
    re.compile(r"\.pytest_cache"),
]

ALLOWED_TYPE = {
    "CONCEPT",
    "MODEL",
    "ENGINEERING",
    "GOVERNANCE",
    "HISTORICAL_RAW",
    "BUILD",
}
ALLOWED_AUTHORITY = {
    "AUTHORITATIVE-DRAFT",
    "AUTHORITATIVE-MODEL",
    "EXPLORATORY",
    "DEPRECATED",
    "LEGACY-LINEAGE",
}
ALLOWED_VALIDATION = {
    "UNVALIDATED",
    "PARTIALLY-VALIDATED",
    "BENCHMARKED",
    "PEER-REVIEWED",
}
ALLOWED_EXEC = {"EXEC-FULL", "EXEC-PARTIAL", "INERT-SKETCH", "N/A"}
ALLOWED_PARAM_STATUS = {
    "PROVENANCED",
    "PARTIALLY-PROVENANCED",
    "UNPROVENANCED",
    "N/A",
}

REQUIRED_FIELDS = ("path", "type", "authority", "validation", "executability", "parameter_status")


def find_tracked_files():
    found = set()
    for rel in TRACKED_ROOT_FILES:
        p = os.path.join(REPO_ROOT, rel)
        if os.path.isfile(p):
            found.add(rel)
    for d in TRACKED_DIRS:
        base = os.path.join(REPO_ROOT, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirnames, filenames in os.walk(base):
            if any(pat.search(dirpath) for pat in IGNORE_PATTERNS):
                continue
            for fname in filenames:
                if fname in IGNORE_BASENAMES:
                    continue
                full = os.path.join(dirpath, fname)
                rel = os.path.relpath(full, REPO_ROOT)
                found.add(rel)
    return found


def load_registry():
    with open(REGISTRY_PATH) as f:
        data = yaml.safe_load(f)
    return data.get("entries", [])


def load_param_ids():
    if not os.path.exists(PARAMS_PATH):
        return []
    with open(PARAMS_PATH) as f:
        records = yaml.safe_load(f)
    if not isinstance(records, list):
        return []
    return [r.get("parameter_id") for r in records if isinstance(r, dict)]


def run_test_ref(test_ref):
    """
    test_ref format: path.py::TestClass::method or path.py::function
    Returns (passed: bool, detail: str).
    """
    parts = test_ref.split("::")
    if len(parts) < 2:
        return False, f"malformed test_ref (expected 'path.py::Test::method'): {test_ref}"
    file_part = parts[0]
    file_path = os.path.join(REPO_ROOT, file_part)
    if not os.path.exists(file_path):
        return False, f"test file does not exist: {file_part}"

    env = os.environ.copy()
    src = os.path.join(REPO_ROOT, "src")
    env["PYTHONPATH"] = src + os.pathsep + env.get("PYTHONPATH", "")

    if len(parts) == 3:
        _, cls, method = parts
        test_id = f"{os.path.splitext(os.path.basename(file_part))[0]}.{cls}.{method}"
    elif len(parts) == 2:
        _, func = parts
        test_id = f"{os.path.splitext(os.path.basename(file_part))[0]}.{func}"
    else:
        return False, f"malformed test_ref: {test_ref}"

    test_dir = os.path.dirname(file_path) or "."
    result = subprocess.run(
        [sys.executable, "-m", "unittest", test_id],
        cwd=test_dir,
        env=env,
        capture_output=True,
        text=True,
    )
    passed = result.returncode == 0
    detail = "" if passed else (result.stderr[-500:] if result.stderr else "unknown failure")
    return passed, detail


def _collect_imports(py_path):
    """Return list of imported module name strings from a Python file."""
    try:
        with open(py_path) as f:
            tree = ast.parse(f.read(), filename=py_path)
    except SyntaxError:
        return []
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                names.append(node.module)
    return names


def main():
    problems = []
    warnings = []

    entries = load_registry()

    # --- Check 1 & 2: file existence, both directions ---
    registered_paths = set()
    for e in entries:
        path = e.get("path")
        if not path:
            problems.append("registry.yaml entry with no 'path' field")
            continue
        if path in registered_paths:
            problems.append(f"duplicate path in registry.yaml: {path}")
        registered_paths.add(path)
        full = os.path.join(REPO_ROOT, path)
        if not os.path.exists(full):
            problems.append(f"registry.yaml entry points to nonexistent file: {path}")

    tracked_files = find_tracked_files()
    for f in sorted(tracked_files - registered_paths):
        problems.append(f"file on disk with no registry.yaml entry: {f}")

    # --- Check 3: duplicate model_id ---
    seen_ids = set()
    for e in entries:
        mid = e.get("model_id")
        if not mid:
            continue
        if mid in seen_ids:
            problems.append(f"duplicate model_id in registry.yaml: {mid}")
        seen_ids.add(mid)

    # --- Check 4: duplicate parameter_id ---
    pseen = set()
    for pid in load_param_ids():
        if not pid:
            continue
        if pid in pseen:
            problems.append(f"duplicate parameter_id in parameters/swarm_v3.yaml: {pid}")
        pseen.add(pid)

    # --- Check 7 & 8: taxonomy enums + required fields ---
    for e in entries:
        path = e.get("path", "<no-path>")
        for field in REQUIRED_FIELDS:
            if field not in e or e[field] is None or e[field] == "":
                problems.append(f"{path}: missing required field '{field}'")
        t = e.get("type")
        if t is not None and t not in ALLOWED_TYPE:
            problems.append(f"{path}: invalid type '{t}' (allowed: {sorted(ALLOWED_TYPE)})")
        a = e.get("authority")
        if a is not None and a not in ALLOWED_AUTHORITY:
            problems.append(
                f"{path}: invalid authority '{a}' (allowed: {sorted(ALLOWED_AUTHORITY)})"
            )
        v = e.get("validation")
        if v is not None and v not in ALLOWED_VALIDATION:
            problems.append(
                f"{path}: invalid validation '{v}' (allowed: {sorted(ALLOWED_VALIDATION)})"
            )
        ex = e.get("executability")
        if ex is not None and ex not in ALLOWED_EXEC:
            problems.append(
                f"{path}: invalid executability '{ex}' (allowed: {sorted(ALLOWED_EXEC)})"
            )
        ps = e.get("parameter_status")
        if ps is not None and ps not in ALLOWED_PARAM_STATUS:
            problems.append(
                f"{path}: invalid parameter_status '{ps}' "
                f"(allowed: {sorted(ALLOWED_PARAM_STATUS)})"
            )

    # --- Check 10: AUTHORITATIVE-MODEL must declare validation ---
    for e in entries:
        if e.get("authority") == "AUTHORITATIVE-MODEL":
            if not e.get("validation"):
                problems.append(
                    f"{e.get('path')}: AUTHORITATIVE-MODEL requires a validation status"
                )

    # --- Check 11: provenanced claims should not be empty of notes for MODELs ---
    for e in entries:
        if e.get("type") != "MODEL":
            continue
        ps = e.get("parameter_status")
        if ps in ("PROVENANCED", "PARTIALLY-PROVENANCED"):
            notes = (e.get("notes") or "").strip()
            if not notes and not e.get("model_id"):
                warnings.append(
                    f"{e.get('path')}: parameter_status={ps} but no notes/model_id "
                    f"to locate provenance records"
                )

    # --- Check 5 / 14: EXEC-FULL/PARTIAL need passing test_ref ---
    for e in entries:
        if e.get("authority") == "DEPRECATED":
            continue
        exe = e.get("executability")
        if exe not in ("EXEC-FULL", "EXEC-PARTIAL"):
            continue
        # Require test_ref for MODEL and for BUILD under tools/tests/src
        if e.get("type") not in ("MODEL", "BUILD"):
            continue
        path = e.get("path")
        test_ref = e.get("test_ref")
        if not test_ref:
            problems.append(
                f"{path}: executability={exe} but no test_ref "
                f"(non-deprecated {e.get('type')} claims must cite a test)"
            )
            continue
        passed, detail = run_test_ref(test_ref)
        if not passed:
            problems.append(
                f"{path}: test_ref '{test_ref}' does NOT pass -- registry claims {exe} "
                f"but the cited test fails. {detail}"
            )

    # --- Check 6: deprecated models imported from src/ ---
    deprecated_model_files = [
        e["path"]
        for e in entries
        if e.get("type") == "MODEL" and e.get("authority") == "DEPRECATED"
    ]
    deprecated_module_names = {
        os.path.splitext(os.path.basename(p))[0] for p in deprecated_model_files
    }
    src_dir = os.path.join(REPO_ROOT, "src")
    for dirpath, _, filenames in os.walk(src_dir):
        if any(pat.search(dirpath) for pat in IGNORE_PATTERNS):
            continue
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            full = os.path.join(dirpath, fname)
            content = open(full).read()
            for mod in deprecated_module_names:
                if re.search(rf"\bimport\s+{re.escape(mod)}\b", content) or re.search(
                    rf"\bfrom\s+[\w.]*{re.escape(mod)}\s+import\b", content
                ):
                    rel = os.path.relpath(full, REPO_ROOT)
                    problems.append(
                        f"production code imports a DEPRECATED model: {rel} imports {mod}"
                    )

    # --- Check 12: production Python only under src/astroid_miner/ ---
    for dirpath, _, filenames in os.walk(src_dir):
        if any(pat.search(dirpath) for pat in IGNORE_PATTERNS):
            continue
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, REPO_ROOT)
            # Allow only src/astroid_miner/...
            if not rel.startswith(os.path.join("src", "astroid_miner")):
                problems.append(
                    f"production Python module outside src/astroid_miner/: {rel}"
                )

    # --- Check 13: src/ must not import experiments/ or archive/ ---
    forbidden_roots = ("experiments", "archive")
    for dirpath, _, filenames in os.walk(src_dir):
        if any(pat.search(dirpath) for pat in IGNORE_PATTERNS):
            continue
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, REPO_ROOT)
            for mod in _collect_imports(full):
                # normalize dotted imports that might reference experiments
                top = mod.split(".")[0]
                if top in forbidden_roots:
                    problems.append(
                        f"production code imports non-production tree: {rel} imports {mod}"
                    )
                # also catch string path style rare cases via simple content scan
            content = open(full).read()
            for root in forbidden_roots:
                if re.search(rf"\b{root}\.(deprecated|monte_carlo|raw)", content):
                    problems.append(
                        f"production code references non-production module path: "
                        f"{rel} mentions {root}"
                    )

    # --- Report ---
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if problems:
        print(f"FAILED — {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    print(
        f"OK — {len(entries)} registry entries checked, all consistent with repository state."
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
