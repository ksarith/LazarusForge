"""
Repository contract: registry.yaml is consistent and the validator passes.

Running these tests is itself the execution proof for tools/validate_registry.py.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VALIDATOR = os.path.join(REPO_ROOT, "tools", "validate_registry.py")


class TestRegistryValidator(unittest.TestCase):
    def test_validate_registry_exits_clean(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.join(REPO_ROOT, "src") + os.pathsep + env.get(
            "PYTHONPATH", ""
        )
        result = subprocess.run(
            [sys.executable, VALIDATOR],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"validate_registry.py failed:\n{result.stdout}\n{result.stderr}",
        )
        self.assertIn("OK —", result.stdout)

    def test_registry_yaml_exists_and_has_entries(self):
        import yaml

        path = os.path.join(REPO_ROOT, "registry.yaml")
        self.assertTrue(os.path.isfile(path))
        with open(path) as f:
            data = yaml.safe_load(f)
        self.assertIn("entries", data)
        self.assertGreaterEqual(len(data["entries"]), 1)


class TestRegistryTaxonomy(unittest.TestCase):
    def test_all_entries_have_required_fields(self):
        import yaml

        required = (
            "path",
            "type",
            "authority",
            "validation",
            "executability",
            "parameter_status",
        )
        with open(os.path.join(REPO_ROOT, "registry.yaml")) as f:
            entries = yaml.safe_load(f)["entries"]
        for e in entries:
            for field in required:
                self.assertIn(field, e, msg=f"{e.get('path')}: missing {field}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
