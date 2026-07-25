"""
Lazarus Forge - Cold Session Bundler (review/cold_session_bundler.py)

Resolution mechanism for AP-017 (Admin/Auditor_Protocols.md):
    "Adversarial Battery independence requirement undefined"

AP-017's 2026-07-17 clarification is the actual spec this module implements:

    closure requires INFORMATIONAL independence, not merely
    conversational independence. A new chat session is insufficient
    if the prompt carries a curated Assumption Extraction block, a
    summary of prior findings, or "carried forward unless
    contradicted" framing ... The closest available approximation:
    a session given only the raw repository files and the standard
    audit prompt, with no summary of this file's own audit history
    and no prior findings carried forward.

This is a different problem than SectionExtractor (review/section_extractor.py,
formerly living in parser.py). SectionExtractor isolates one section of one
file from that file's own surrounding metadata. This module isolates an
entire audit SESSION from the repository's accumulated judgments about the
target — across however many files carry that history — while still
delivering the raw doctrine text the auditor needs to actually do the job.

Scope and honesty about limits:
    - This is a best-effort heuristic, not a formal guarantee. It cannot
      stop a human operator from pasting extra context into the session
      by hand — it can only refuse to construct that context for them.
    - It distinguishes CURRENT DOCTRINE (Description, Why It Matters,
      Resolution Path — normative, needed) from RETROSPECTIVE FINDINGS
      (Resolution, Advancement, Clarification, Fresh instance notes,
      Surfaced-by attributions, Status/Risk/Last-Reviewed metadata —
      evaluative history that primes a verdict). Only the latter is
      stripped from bundled content.
    - It does not audit the auditor. If a human pastes a curated summary
      into the session after receiving a clean bundle, that's outside
      this tool's control. The bundle's manifest exists so that gap is
      at least visible and checkable after the fact.
"""

import hashlib
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Capability declaration (queryable by an Automation Manifest, no code read required)
# ---------------------------------------------------------------------------

CAPABILITIES = {
    "raw_file_bundling": True,
    "retrospective_content_stripping": True,
    "self_referential_file_exclusion": True,
    "manifest_with_checksums": True,
    "reproducible_bundle": True,
    "guarantees_true_independence": False,  # honest: heuristic, not proof
}

TOOL_NAME = "cold_session_bundler"
TOOL_VERSION = "0.1"


# ---------------------------------------------------------------------------
# Retrospective-content patterns
#
# These match blocks that describe a PAST judgment (what was found, what
# was decided, who found it, when) as opposed to CURRENT doctrine (what
# the rule is, why it matters, what a fix should do). Only the former is
# withheld from a cold bundle.
# ---------------------------------------------------------------------------

RETROSPECTIVE_LINE_PREFIXES = (
    "**Resolution:**",
    "**Resolution —",
    "**Advancement —",
    "**Advancement:**",
    "**Clarification",
    "**Fresh instance",
    "*Surfaced by",
    "*Surfaced independently",
    "**Last Reviewed",
)

# A tracker-entry metadata table (Status / Risk / Priority / First Logged /
# Last Reviewed) is exactly the "already decided" framing AP-017's
# clarification warns against — it tells the auditor the verdict before
# they've looked at the doctrine. Matched as a markdown table block whose
# header row contains "Status" and "Risk" or "Last Reviewed".
METADATA_TABLE_RE = re.compile(
    r"^\|\s*Field\s*\|\s*Value\s*\|\s*\n\|[-\s|]+\|\s*\n(?:\|.*\|\s*\n?)+",
    re.MULTILINE,
)

# Self-referential audit apparatus: files whose primary content IS the
# repository's accumulated judgment log. Excluded from a cold bundle by
# default unless explicitly named as the audit target itself.
SELF_REFERENTIAL_NAME_PATTERNS = (
    "auditor_protocols",
    "_changelog",
    "unknown_cycles",
    "audit_harness_changelog",
)


@dataclass
class StrippedBlock:
    """Record of what was withheld, without re-exposing the content itself."""
    file_path: str
    reason: str
    char_count: int
    line_number: int


@dataclass
class BundledFile:
    file_path: str
    raw_sha256: str
    raw_char_count: int
    included_char_count: int
    content: str  # post-stripping content actually going into the session
    stripped: List[StrippedBlock] = field(default_factory=list)


@dataclass
class ColdSessionBundle:
    """
    The complete, self-contained payload for an independent audit session.
    Nothing outside `.render()` should be shown to the auditing agent —
    the manifest and stripped-block log are for the human operator to
    verify the bundle, not for the auditor to read.
    """
    created_at: str
    target_files: List[str]
    included_files: List[BundledFile] = field(default_factory=list)
    excluded_files: List[Tuple[str, str]] = field(default_factory=list)  # (path, reason)
    standard_audit_prompt: str = ""

    def manifest(self) -> Dict:
        return {
            "tool": TOOL_NAME,
            "tool_version": TOOL_VERSION,
            "created_at": self.created_at,
            "target_files": self.target_files,
            "included": [
                {
                    "file_path": f.file_path,
                    "raw_sha256": f.raw_sha256,
                    "raw_char_count": f.raw_char_count,
                    "included_char_count": f.included_char_count,
                    "stripped_block_count": len(f.stripped),
                    "stripped": [
                        {"reason": s.reason, "line": s.line_number, "char_count": s.char_count}
                        for s in f.stripped
                    ],
                }
                for f in self.included_files
            ],
            "excluded": [{"file_path": p, "reason": r} for p, r in self.excluded_files],
            "guarantees_true_independence": CAPABILITIES["guarantees_true_independence"],
        }

    def render(self) -> str:
        """
        The actual text to hand to the auditing session. Contains ONLY the
        standard audit prompt and stripped raw file content — no manifest,
        no stripped-block log, no mention of what was withheld. An auditor
        should not be told "something was redacted here"; that itself is
        priming information (it flags where the interesting disagreement
        probably lives).
        """
        parts = [self.standard_audit_prompt.strip(), ""]
        for f in self.included_files:
            parts.append(f"--- FILE: {f.file_path} ---")
            parts.append(f.content)
            parts.append("")
        return "\n".join(parts)


DEFAULT_STANDARD_AUDIT_PROMPT = (
    "You are auditing the attached repository files. You have not seen this "
    "repository before this session and have no prior findings about it. "
    "Evaluate the material on its own terms: identify unsupported claims, "
    "internal inconsistencies, gaps between stated doctrine and evident "
    "implementation, and anything that would concern an independent "
    "reviewer. Do not assume any part of the material is already correct "
    "because it is well-formatted or internally confident."
)


class ColdSessionBundler:
    def __init__(self, repo_root: str, standard_audit_prompt: Optional[str] = None):
        self.repo_root = repo_root
        self.standard_audit_prompt = standard_audit_prompt or DEFAULT_STANDARD_AUDIT_PROMPT

    # -- public API ------------------------------------------------------

    def bundle(self, target_files: List[str]) -> ColdSessionBundle:
        """
        Build a cold session bundle for auditing `target_files`.

        Deliberately, this method's signature has no `prior_findings`,
        `context`, or `summary` parameter. There is nowhere to pass that
        information in even if a caller wanted to — the only inputs are
        which files to audit and (optionally, at construction time) which
        standard prompt to use.

        LIMITATION (v0.1, not yet built): dependency auto-inclusion. If a
        target file references other files (e.g. via a `dependencies:`
        list), those referenced files are NOT automatically pulled in yet
        — only exactly what's listed in `target_files` is bundled. This
        means the self-referential exclusion check currently only applies
        to files you explicitly name; it does nothing until auto-pulled
        dependencies exist to filter. Naming Auditor_Protocols.md directly
        always includes it, by design — you can't audit a file you can't
        see. The exclusion exists to stop it from being pulled in
        silently as unrequested "helpful context" once dependency-following
        is added, not to block a deliberate audit of the file itself.
        """
        result = ColdSessionBundle(
            created_at=datetime.now().isoformat() + "Z",
            target_files=list(target_files),
            standard_audit_prompt=self.standard_audit_prompt,
        )

        for rel_path in target_files:
            abs_path = os.path.join(self.repo_root, rel_path)
            if not os.path.exists(abs_path):
                result.excluded_files.append((rel_path, "file not found"))
                continue

            is_target_itself = True  # explicitly requested targets are always included
            self._include_file(result, rel_path, abs_path, is_explicit_target=is_target_itself)

        return result

    # -- internals ---------------------------------------------------------

    def _is_self_referential(self, rel_path: str) -> bool:
        lower = rel_path.lower()
        return any(pat in lower for pat in SELF_REFERENTIAL_NAME_PATTERNS)

    def _include_file(self, result: ColdSessionBundle, rel_path: str, abs_path: str,
                       is_explicit_target: bool) -> None:
        if self._is_self_referential(rel_path) and not is_explicit_target:
            result.excluded_files.append(
                (rel_path, "self-referential audit apparatus (accumulated judgment log); "
                           "not an explicit audit target")
            )
            return

        with open(abs_path, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()

        raw_sha256 = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        stripped_content, stripped_blocks = self._strip_retrospective_content(rel_path, raw)

        result.included_files.append(
            BundledFile(
                file_path=rel_path,
                raw_sha256=raw_sha256,
                raw_char_count=len(raw),
                included_char_count=len(stripped_content),
                content=stripped_content,
                stripped=stripped_blocks,
            )
        )

    def _strip_retrospective_content(self, rel_path: str, raw: str) -> Tuple[str, List[StrippedBlock]]:
        stripped_blocks: List[StrippedBlock] = []
        lines = raw.split("\n")
        out_lines: List[str] = []

        i = 0
        while i < len(lines):
            line = lines[i]

            # 1. Metadata tracker tables (Status/Risk/Priority/.../Last Reviewed)
            #    Detect a "| Field | Value |" header and consume the whole table.
            #    Exception, added after a cold-session audit surfaced the gap
            #    2026-07-25: Ethical Anchor is a mandatory Audit Entry Condition
            #    per Admin/File_Template.md ("absence, alteration, or blank value
            #    is a mandatory drift indicator requiring human review") and
            #    Admin/Auditor_Protocols.md's own Audit Entry Conditions require
            #    it be checked before an audit may even begin. Stripping it along
            #    with the rest of the tracker table silently made that entry
            #    condition unsatisfiable in a genuinely cold session — the exact
            #    kind of blind spot this tool exists to prevent, not create.
            #    Mirrors the Epistemic Ledger's 20%-rule exemption in
            #    Admin/Auditor_Protocols.md's Metadata Guardrail: a specific,
            #    named carve-out from a general stripping rule, not a general
            #    weakening of it.
            if line.strip().startswith("| Field") and "Value" in line:
                block_start = i
                j = i
                block_lines = [line]
                j += 1
                if j < len(lines) and set(lines[j].strip()) <= {"|", "-", " "}:
                    block_lines.append(lines[j])
                    j += 1
                ethical_anchor_row = None
                while j < len(lines) and lines[j].strip().startswith("|"):
                    if "Ethical Anchor" in lines[j]:
                        ethical_anchor_row = lines[j]
                    block_lines.append(lines[j])
                    j += 1
                total_block_chars = sum(len(bl) for bl in block_lines)
                retained_chars = len(ethical_anchor_row) + 1 if ethical_anchor_row is not None else 0
                stripped_blocks.append(StrippedBlock(
                    file_path=rel_path,
                    reason="tracker metadata table (Status/Risk/Priority/history) — "
                           "pre-judged framing, not doctrine"
                           + (" (Ethical Anchor row retained — see Audit Entry Conditions)"
                              if ethical_anchor_row is not None else ""),
                    char_count=total_block_chars - retained_chars,
                    line_number=block_start + 1,
                ))
                if ethical_anchor_row is not None:
                    out_lines.append(ethical_anchor_row.strip())
                i = j
                continue

            # 2. Single-line retrospective markers (Resolution:, Advancement —,
            #    Clarification, Fresh instance, Surfaced by / independently,
            #    Last Reviewed). These are typically short paragraphs; consume
            #    until the next blank line or the next markdown break.
            stripped_line_reason = None
            for prefix in RETROSPECTIVE_LINE_PREFIXES:
                if line.strip().startswith(prefix):
                    stripped_line_reason = f"retrospective marker ('{prefix.strip('*')}')"
                    break

            if stripped_line_reason:
                block_start = i
                block_lines = [line]
                j = i + 1
                while j < len(lines) and lines[j].strip() != "" and lines[j].strip() != "---":
                    block_lines.append(lines[j])
                    j += 1
                stripped_blocks.append(StrippedBlock(
                    file_path=rel_path,
                    reason=stripped_line_reason,
                    char_count=sum(len(bl) for bl in block_lines),
                    line_number=block_start + 1,
                ))
                i = j
                continue

            out_lines.append(line)
            i += 1

        return "\n".join(out_lines), stripped_blocks


# ---------------------------------------------------------------------------
# CLI smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) < 3:
        print("Usage: python cold_session_bundler.py <repo_root> <target_file> [target_file...]")
        sys.exit(1)

    repo_root = sys.argv[1]
    targets = sys.argv[2:]

    bundler = ColdSessionBundler(repo_root)
    bundle = bundler.bundle(targets)

    print("=== MANIFEST (operator-facing; do not hand to auditor) ===")
    print(json.dumps(bundle.manifest(), indent=2))
    print()
    print("=== RENDERED SESSION PAYLOAD (auditor-facing) ===")
    print(bundle.render()[:3000])
    print("... [truncated for smoke test]" if len(bundle.render()) > 3000 else "")
