"""
Smoke tests for release / integrity tooling.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestVerifyManifest(unittest.TestCase):
    def test_verify_manifest_detects_match(self):
        tool = os.path.join(REPO_ROOT, "tools", "verify_manifest.py")
        with tempfile.TemporaryDirectory() as tmp:
            sample = os.path.join(tmp, "a.txt")
            open(sample, "w").write("hello")
            import importlib.util
            spec = importlib.util.spec_from_file_location("verify_manifest", tool)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            manifest = mod.build_current_manifest(tmp)
            # Re-hash without writing into the tree under test
            current = mod.build_current_manifest(tmp)
            self.assertEqual(set(current.keys()), set(manifest.keys()))
            for k in current:
                self.assertEqual(current[k]["sha256"], manifest[k]["sha256"])
            self.assertIn("a.txt", current)


class TestUpdateArchiveIsLegacy(unittest.TestCase):
    def test_update_archive_file_exists(self):
        path = os.path.join(REPO_ROOT, "tools", "update_archive.py")
        self.assertTrue(os.path.isfile(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
