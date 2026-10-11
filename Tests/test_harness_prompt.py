"""
Offline tests for Automation/AUDIT_HARNESS.py prompt text and version consistency.

Run from the repository root:
    python -m unittest discover -s Tests/Automation -v

Standard library only. No network: urllib is patched to fail while the harness
is imported (so its registry uses the built-in fallback), and fetch() is
replaced with a reader of the local checkout. A passing run shows what the
harness generates from the LOCAL files. It does not show behavior against a
live GitHub fetch.
"""
import contextlib
import io
import os
import re
import sys
import unittest
from unittest import mock

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUTOMATION = os.path.join(ROOT, "Automation")


def _load_harness():
    if AUTOMATION not in sys.path:
        sys.path.insert(0, AUTOMATION)
    with mock.patch("urllib.request.urlopen", side_effect=OSError("offline test")):
        import importlib
        import AUDIT_HARNESS
        return importlib.reload(AUDIT_HARNESS)


def _run_with_local_fetch(harness, target, fetch_override=None):
    def local_fetch(name):
        path = harness.FILE_REGISTRY.get(name, name)
        full = os.path.join(ROOT, path)
        if os.path.exists(full):
            with open(full, encoding="utf-8") as fh:
                return fh.read()
        return "[FETCH FAILED] " + path

    harness.fetch = fetch_override or local_fetch
    buf = io.StringIO()
    exit_code = None
    try:
        with contextlib.redirect_stdout(buf):
            harness.run_audit(target, "offline prompt-string check", None, "Exploration")
    except SystemExit as exc:
        exit_code = exc.code
    return buf.getvalue(), exit_code


class PromptTextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.harness = _load_harness()
        cls.output, cls.exit_code = _run_with_local_fetch(cls.harness, "Ethical_Constraints.md")
        marker = "PROMPT (copy everything below this line):"
        cls.assertTrue = cls.assertTrue  # keep linters quiet
        cls.prompt = cls.output.split(marker, 1)[1] if marker in cls.output else ""
        # Instruction text only: everything before the fetched file contents.
        cls.instructions = cls.prompt.split("FILES PROVIDED", 1)[0]

    def test_run_completed_and_prompt_assembled(self):
        self.assertIsNone(self.exit_code, "run_audit exited early")
        self.assertTrue(self.prompt, "no prompt section found in output")
        self.assertIn("FILES PROVIDED", self.prompt)

    def test_role_declaration_uses_live_version_instruction(self):
        self.assertIn(
            "per Auditor_Protocols.md (use the live version from its header)",
            self.instructions,
        )

    def test_no_pinned_protocol_version_in_instructions(self):
        self.assertIsNone(
            re.search(r"Auditor_Protocols\.md v0\.\d+", self.instructions),
            "instruction text pins an Auditor_Protocols version",
        )

    def test_kit_contents_claim_has_no_condensed_registry(self):
        self.assertNotIn("condensed Unknowns Registry", self.instructions)
        self.assertIn("AI Contribution Rules", self.instructions)

    def test_fetch_failure_is_reported_not_hidden(self):
        def failing_fetch(name):
            return "[FETCH FAILED] simulated outage for " + name

        output, _ = _run_with_local_fetch(
            self.harness, "Ethical_Constraints.md", fetch_override=failing_fetch
        )
        self.assertIn("FETCH FAILURES", output)


class StaticConsistencyTests(unittest.TestCase):
    def test_no_hardcoded_protocol_version_pins_in_automation_sources(self):
        pattern = re.compile(r"Auditor_Protocols\.md v0\.\d+")
        offenders = []
        for name in sorted(os.listdir(AUTOMATION)):
            if not name.endswith(".py"):
                continue
            with open(os.path.join(AUTOMATION, name), encoding="utf-8") as fh:
                for number, line in enumerate(fh, 1):
                    if line.lstrip().startswith("#"):
                        continue  # comments may quote an example string
                    if pattern.search(line):
                        offenders.append(f"{name}:{number}")
        self.assertEqual(offenders, [], "hard-coded Auditor_Protocols version pins found")

    def test_harness_version_matches_automation_readme(self):
        with open(os.path.join(AUTOMATION, "AUDIT_HARNESS.py"), encoding="utf-8") as fh:
            head = fh.read(600)
        in_source = re.search(r"AUDIT HARNESS v(\d+)", head)
        with open(os.path.join(AUTOMATION, "README.md"), encoding="utf-8") as fh:
            readme = fh.read()
        in_readme = re.search(r"`AUDIT_HARNESS\.py` \(v(\d+)\)", readme)
        self.assertIsNotNone(in_source, "version label not found in harness header")
        self.assertIsNotNone(in_readme, "version label not found in Automation/README.md")
        self.assertEqual(in_source.group(1), in_readme.group(1))


if __name__ == "__main__":
    unittest.main()
