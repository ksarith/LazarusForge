"""
Offline tests for Automation/integrity_check.py's Size Census Pass (T1 roster).

Run from the repository root:
    python -m unittest discover -s Tests/Automation -v

Standard library only. No network: the pass runs against a synthetic
temp tree with exact byte counts, so every expected value below is
derived from the fixture construction, not from the live repository.
A passing run validates the census logic; it does not report the live
repo's roster. The first live-tree run of integrity_check.py v0.4 is
owed at the next battery run (MAINT-136).
"""
import os
import sys
import tempfile
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUTOMATION = os.path.join(ROOT, "Automation")

if AUTOMATION not in sys.path:
    sys.path.insert(0, AUTOMATION)

from integrity_check import size_census_pass, walk_repo, T1_BYTES  # noqa: E402


def _write(path, size):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(b"x" * size)


class SizeCensusPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        root = cls._tmp.name
        _write(os.path.join(root, "over.md"), T1_BYTES + 1)
        _write(os.path.join(root, "at_bar.md"), T1_BYTES)          # bar is inclusive
        _write(os.path.join(root, "under.md"), T1_BYTES - 1)
        _write(os.path.join(root, "Logs", "home_Log.md"), T1_BYTES + 5000)
        _write(os.path.join(root, "noext"), T1_BYTES - 100)        # extensionless: tracked
        _write(os.path.join(root, "skip.py"), 10)                  # .py: not trackable
        cls.findings = []
        cls.summary = size_census_pass(root, walk_repo(root), cls.findings)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def _finding_for(self, path):
        return [f for f in self.findings if f.file == path]

    def test_bar_constant_is_100000(self):
        self.assertEqual(T1_BYTES, 100000)

    def test_over_bar_file_warns_as_split_queue(self):
        hits = self._finding_for("over.md")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].severity, "WARNING")
        self.assertEqual(hits[0].category, "SIZE_CENSUS")
        self.assertIn("R8 Log-Split queued", hits[0].message)

    def test_bar_is_inclusive(self):
        hits = self._finding_for("at_bar.md")
        self.assertEqual(len(hits), 1)
        self.assertIn(str(T1_BYTES), hits[0].message)

    def test_under_bar_file_not_flagged(self):
        self.assertEqual(self._finding_for("under.md"), [])

    def test_log_home_classed_per_r6b(self):
        hits = self._finding_for("Logs/home_Log.md")
        self.assertEqual(len(hits), 1)
        self.assertIn("R-6b", hits[0].message)
        self.assertNotIn("R8 Log-Split queued", hits[0].message)

    def test_tracked_scope_and_counts(self):
        # over.md, at_bar.md, under.md, Logs/home_Log.md, noext = 5;
        # skip.py is not trackable and must not be measured.
        self.assertEqual(self.summary["files_measured"], 5)
        self.assertEqual(len(self.findings), 3)
        self.assertEqual(self.summary["over_bar_count"], 3)
        self.assertEqual(self.summary["over_bar_log_homes"], 1)
        self.assertEqual(self.summary["over_bar_split_queue"], 2)

    def test_roster_sorted_heaviest_first(self):
        sizes = [r["bytes"] for r in self.summary["roster_over_bar"]]
        self.assertEqual(sizes, [T1_BYTES + 5000, T1_BYTES + 1, T1_BYTES])

    def test_under_bar_and_extensionless_in_roster_not_findings(self):
        # noext (extensionless) is measured but under the bar:
        # it must appear in no finding.
        self.assertEqual(self._finding_for("noext"), [])


if __name__ == "__main__":
    unittest.main()
