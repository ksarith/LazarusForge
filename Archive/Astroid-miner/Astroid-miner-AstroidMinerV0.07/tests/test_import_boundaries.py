"""
Repository contract: production code (src/) must not depend on
experiments/ or archive/, and must not import DEPRECATED models.
"""

from __future__ import annotations

import ast
import os
import re
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(REPO_ROOT, "src")


def _iter_src_py():
    for dirpath, _, filenames in os.walk(SRC_ROOT):
        if "__pycache__" in dirpath:
            continue
        for fname in filenames:
            if fname.endswith(".py"):
                yield os.path.join(dirpath, fname)


def _imports(path):
    try:
        tree = ast.parse(open(path).read(), filename=path)
    except SyntaxError:
        return []
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                names.append(a.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.append(node.module)
    return names


class TestImportBoundaries(unittest.TestCase):
    def test_src_does_not_import_experiments_or_archive(self):
        forbidden = ("experiments", "archive")
        offenders = []
        for path in _iter_src_py():
            rel = os.path.relpath(path, REPO_ROOT)
            for mod in _imports(path):
                if mod.split(".")[0] in forbidden:
                    offenders.append(f"{rel} imports {mod}")
        self.assertEqual(offenders, [], msg="\n".join(offenders))

    def test_src_modules_live_under_astroid_miner(self):
        bad = []
        for path in _iter_src_py():
            rel = os.path.relpath(path, REPO_ROOT)
            if not rel.startswith(os.path.join("src", "astroid_miner")):
                bad.append(rel)
        self.assertEqual(bad, [], msg="\n".join(bad))

    def test_no_deprecated_model_basename_imports(self):
        # MDL-GRA-04 lives under experiments/deprecated/
        banned = {"replication_constraint_graph_v4_silicate"}
        offenders = []
        for path in _iter_src_py():
            content = open(path).read()
            rel = os.path.relpath(path, REPO_ROOT)
            for name in banned:
                if re.search(rf"\b{name}\b", content):
                    offenders.append(f"{rel} references {name}")
        self.assertEqual(offenders, [], msg="\n".join(offenders))


if __name__ == "__main__":
    unittest.main(verbosity=2)
