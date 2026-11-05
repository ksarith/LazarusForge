#!/usr/bin/env python3
"""
verify_manifest.py — re-hash the repository tree and diff against a
previously generated build_manifest_*.json.

Usage:
    python3 tools/verify_manifest.py path/to/build_manifest_v0.02.1.json

Exits non-zero if any file is missing, added, or hash-mismatched relative
to the manifest, so it can be used as a simple CI/pre-release gate.
"""

import hashlib
import json
import os
import sys


def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_current_manifest(root):
    manifest = {}
    for dirpath, _, files in os.walk(root):
        if "__pycache__" in dirpath:
            continue
        for fname in files:
            p = os.path.join(dirpath, fname)
            rel = os.path.relpath(p, root)
            manifest[rel] = {"size": os.path.getsize(p), "sha256": hash_file(p)}
    return manifest


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tools/verify_manifest.py <manifest.json>")
        sys.exit(2)

    manifest_path = sys.argv[1]
    with open(manifest_path) as f:
        expected = json.load(f)

    # Repo root = parent of the tools/ directory this script lives in
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    actual = build_current_manifest(root)

    expected_paths = set(expected.keys())
    actual_paths = set(actual.keys())

    missing = sorted(expected_paths - actual_paths)
    added = sorted(actual_paths - expected_paths)
    changed = sorted(
        p for p in (expected_paths & actual_paths)
        if expected[p]["sha256"] != actual[p]["sha256"]
    )

    ok = True

    if missing:
        ok = False
        print(f"MISSING ({len(missing)}):")
        for p in missing:
            print(f"  - {p}")

    if added:
        print(f"ADDED since manifest ({len(added)}):")
        for p in added:
            print(f"  + {p}")

    if changed:
        ok = False
        print(f"HASH MISMATCH ({len(changed)}):")
        for p in changed:
            print(f"  ! {p}")
            print(f"      expected: {expected[p]['sha256']}")
            print(f"      actual:   {actual[p]['sha256']}")

    if ok and not added:
        print(f"OK — {len(actual)} files match manifest exactly.")
    elif ok:
        print(f"OK — no missing/mismatched files ({len(added)} new file(s) not in manifest).")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
