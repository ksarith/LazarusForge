"""
Lazarus Forge - Repository Integrity Checker (integrity_check.py)

Repo-wide version of checks previously only possible one file at a time
inside a single AUDIT_HARNESS.py session. Imports audit_lib.py and
parser.py rather than reimplementing their logic — see audit_lib.py's
own docstring for why that split exists.

One real dependency worth naming rather than hiding: the Reference Pass
needs a legacy-name ALIASES map to correctly classify LEGACY vs UNKNOWN
cross-references, and that map currently only lives in AUDIT_HARNESS.py
as data. This module imports ALIASES (a dict, not logic) from there.
That is a lesser coupling than duplicating parsing logic would be, but
it is still a dependency — if AUDIT_HARNESS.py's ALIASES import ever
fails, the Reference Pass degrades to an empty alias map rather than
crashing, and says so in its output.

Passes, run in sequence, each appending Finding objects to one shared list:

    1. Walk Repository
    2. Registry Pass       — orphan detection (file exists, not in Routing.md)
    3. Metadata Pass       — Ethical Anchor + File State, via parser.py
    4. Unknown Pass        — duplicate sidecar ID detection
    5. Reference Pass      — cross-reference resolution, via audit_lib.py
    6. Version String Pass — self-citation version drift (AP-025 pattern)
    7. Output              — structured JSON + human-readable summary

Honesty about scope, stated up front rather than discovered later:
    - Registry Pass inherits parse_routing()'s known limitation: files
      with no extension or a space in the name (e.g. the two Admin/
      Tier-0 philosophical documents) cannot be matched by the
      backtick-path regex. These are reported separately as NOTE
      severity ("could not be checked"), never as false-positive
      CRITICAL orphans.
    - Unknown Pass only matches defining occurrences (`### ID` sidecar
      headers), not table-row mentions in Unknowns.md's cross-reference
      index — a mention is not a duplicate definition, and conflating
      the two was the exact false-positive risk flagged when this tool
      was scoped.
    - Version String Pass only catches the specific "FILENAME vX.Y"
      self-citation pattern that caused AP-023/AP-025. It does not
      attempt to locate or verify a file's declared Version String
      Registry entries against arbitrary prose — that would require
      mapping a human-readable section description to actual text,
      which is a judgment task, not a mechanical one. Declining that
      here rather than shipping a heuristic that looks more thorough
      than it is.
"""

import os
import re
import json
import sys

from parser import MetadataParser
from audit_lib import Finding, parse_routing, check_cross_refs

try:
    from AUDIT_HARNESS import ALIASES
    _ALIASES_SOURCE = "AUDIT_HARNESS.ALIASES"
except Exception as e:
    ALIASES = {}
    _ALIASES_SOURCE = f"unavailable ({e}) — Reference Pass LEGACY classification degraded"


TOOL_NAME = "integrity_check"
TOOL_VERSION = "0.1"

# Sidecar ID pattern: matches "### AP-017 — ..." style defining headers,
# not table rows. Prefix is 2-6 uppercase letters, ID is 3+ digits.
SIDECAR_ID_RE = re.compile(r'^###\s+([A-Z]{2,6}-\d{3,})\b')

# Self-citation version pattern: "Auditor_Protocols.md v0.23" or
# "Auditor_Protocols v0.23" (both forms appear in the real repo).
SELF_VERSION_RE = re.compile(r'([A-Za-z_]+(?:\.md)?)\s+v(\d+\.\d+)')

# File State version line, e.g. "**Version 0.25**"
FILE_STATE_VERSION_RE = re.compile(r'^\*\*Version\s+(\d+\.\d+)\*\*', re.MULTILINE)


def walk_repo(root):
    """
    Returns a list of (relative_path, is_extensionless) for every
    trackable file under root. Trackable = ends in .md, or has no
    extension and isn't a hidden/build file. Mirrors the same
    convention used for the earlier one-off census in this project.
    """
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for fn in filenames:
            if fn.startswith('.'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), root)
            rel = rel.replace(os.sep, '/')
            if fn.endswith('.md'):
                results.append((rel, False))
            elif '.' not in fn:
                results.append((rel, True))
    return sorted(results)


def registry_pass(root, all_files, findings):
    """Orphan detection: does every trackable file appear in Routing.md's registry?"""
    routing_path = os.path.join(root, "Routing.md")
    if not os.path.exists(routing_path):
        findings.append(Finding("CRITICAL", "REGISTRY", "Routing.md",
                                 "Routing.md not found at repo root — cannot run Registry Pass."))
        return

    with open(routing_path, encoding="utf-8") as f:
        routing_content = f.read()

    registry = parse_routing(routing_content)
    registered_paths = set(registry.values())
    registered_names = set(registry.keys())

    for rel_path, is_extensionless in all_files:
        basename = rel_path.split('/')[-1]
        if is_extensionless or ' ' in basename:
            findings.append(Finding("NOTE", "REGISTRY", rel_path,
                                     "Extensionless or space-containing filename — "
                                     "parse_routing() cannot match this by design; "
                                     "verify registration in Routing.md manually."))
            continue
        if rel_path in registered_paths or basename in registered_names:
            continue
        if rel_path == "Routing.md" or rel_path == "Discovery.md" or rel_path == "README.md":
            continue  # root navigation files are not expected to register themselves
        findings.append(Finding("WARNING", "REGISTRY", rel_path,
                                 "Not found in Routing.md's Master Routing Map — "
                                 "possible orphan (unregistered file) or a registration gap."))


def metadata_pass(root, all_files, findings):
    """Ethical Anchor + File State sweep via parser.py, repo-wide."""
    for rel_path, is_extensionless in all_files:
        if is_extensionless:
            continue  # parser.py's table/YAML scan needs the .md body shape; skip by design
        full_path = os.path.join(root, rel_path)
        result = MetadataParser(full_path).parse()

        if not result.detected_schemas:
            continue  # no File State table at all — not this pass's concern; Registry/structural gap

        if result.ethical_anchor_status == "missing":
            findings.append(Finding("WARNING", "CONSTITUTION", rel_path,
                                     "Ethical Anchor missing from File State."))
        elif result.ethical_anchor_status == "present_but_altered":
            findings.append(Finding("CRITICAL", "CONSTITUTION", rel_path,
                                     f"Ethical Anchor present but does not match canonical string: "
                                     f"'{result.ethical_anchor.preferred_value}'"))

        for conflict_field in result.conflicting_fields:
            findings.append(Finding("WARNING", "STRUCTURE", rel_path,
                                     f"Conflicting readings for '{conflict_field}' across schemas."))


def unknown_pass(root, all_files, findings):
    """Duplicate sidecar ID detection — defining headers only, not table mentions."""
    id_locations = {}  # id -> list of (file, line_no)

    for rel_path, is_extensionless in all_files:
        if is_extensionless:
            continue
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except Exception:
            continue
        for i, line in enumerate(lines):
            m = SIDECAR_ID_RE.match(line.strip())
            if m:
                uid = m.group(1)
                id_locations.setdefault(uid, []).append((rel_path, i + 1))

    for uid, locations in id_locations.items():
        files_involved = {f for f, _ in locations}
        if len(files_involved) > 1:
            loc_str = "; ".join(f"{f}:{ln}" for f, ln in locations)
            findings.append(Finding("CRITICAL", "DUPLICATE_ID", uid,
                                     f"'{uid}' defined as a sidecar entry in more than one file: {loc_str}"))
        elif len(locations) > 1:
            # Same file, same ID header twice — different but related bug.
            loc_str = "; ".join(f"{f}:{ln}" for f, ln in locations)
            findings.append(Finding("WARNING", "DUPLICATE_ID", uid,
                                     f"'{uid}' has multiple sidecar headers within the same file: {loc_str}"))


def reference_pass(root, all_files, findings):
    """Cross-reference resolution sweep, repo-wide, via audit_lib.check_cross_refs."""
    routing_path = os.path.join(root, "Routing.md")
    if not os.path.exists(routing_path):
        return  # already flagged by registry_pass
    with open(routing_path, encoding="utf-8") as f:
        registry = parse_routing(f.read())

    for rel_path, is_extensionless in all_files:
        if is_extensionless:
            continue
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception:
            continue
        check_cross_refs(rel_path, content, registry, ALIASES, findings)


def version_string_pass(root, all_files, findings):
    """
    Self-citation version drift: "FILENAME vX.Y" strings that don't match
    the file's own current File State version. Scoped narrowly — see
    module docstring for what this deliberately does not attempt.
    """
    for rel_path, is_extensionless in all_files:
        if is_extensionless:
            continue
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception:
            continue

        fs_match = FILE_STATE_VERSION_RE.search(content)
        if not fs_match:
            continue
        current_version = fs_match.group(1)

        basename_stem = rel_path.split('/')[-1].replace('.md', '')
        for m in SELF_VERSION_RE.finditer(content):
            cited_name, cited_version = m.groups()
            cited_stem = cited_name.replace('.md', '')
            if cited_stem != basename_stem:
                continue  # citing a different file's version, not self-citation
            if cited_version != current_version:
                line_no = content[:m.start()].count('\n') + 1
                findings.append(Finding("WARNING", "VERSION_STRING", rel_path,
                                         f"Self-citation 'v{cited_version}' at line {line_no} does not "
                                         f"match File State version v{current_version}."))


def unknowns_summary_pass(root, all_files, findings):
    """
    Counts active (Open / In Progress / Reopened) rows in Unknowns.md's
    per-topic tables, bucketed by the table's own Priority (Promo) column
    value (Critical / Major / Minor / Blocking / Other).

    Scope, stated honestly: this counts what the Priority (Promo) column
    itself says. It does NOT reconcile against each owning file's own
    "Blocking: Yes/No" sidecar field — that field lives in 80+ separate
    files and cross-checking it here would be a much larger undertaking
    than this pass is scoped for. A row whose Priority column literally
    reads "Blocking" is counted as Blocking; a row whose owning file sets
    Blocking: Yes but whose Priority column here says "Major" is counted
    as Major. This is a real, current limitation, not a rounding error —
    noted in the output so it isn't mistaken for a reconciled count.

    Only counts rows inside this file's own topic tables (the standard
    "| ID | Title | Owning File | Status | Subtype | Priority (Promo) |"
    format). Resolved entries do not appear in these tables per this
    file's own Size Management Rule 2 (see Unknowns.md itself) and are
    correctly excluded by construction, not by filtering Status here.
    """
    unknowns_path = os.path.join(root, "Unknowns.md")
    if not os.path.exists(unknowns_path):
        findings.append(Finding("WARNING", "UNKNOWNS_SUMMARY", "Unknowns.md",
                                 "Unknowns.md not found — cannot summarize active unknowns."))
        return {"total": 0, "by_priority": {}, "by_status": {}}

    with open(unknowns_path, encoding="utf-8") as f:
        lines = f.readlines()

    row_re = re.compile(r'^\|\s*([A-Z]{2,8}-[\dR]{2,}[a-z]?)\s*\|(.*)\|(.*)\|(.*)\|(.*)\|(.*)\|\s*$')
    by_priority = {}
    by_status = {}
    total = 0

    for line in lines:
        m = row_re.match(line.rstrip('\n'))
        if not m:
            continue
        status = m.group(4).strip()
        priority = m.group(6).strip()
        if status.lower() in ("status", "---") or not status:
            continue  # header / separator row
        if "resolved" in status.lower():
            continue  # should not appear per Rule 2, but skip defensively rather than miscount
        total += 1
        by_status[status] = by_status.get(status, 0) + 1
        bucket = priority if priority in ("Critical", "Major", "Minor", "Blocking") else (priority or "Unlabeled")
        by_priority[bucket] = by_priority.get(bucket, 0) + 1

    return {"total": total, "by_priority": by_priority, "by_status": by_status}


def run(root):
    findings = []
    all_files = walk_repo(root)

    registry_pass(root, all_files, findings)
    metadata_pass(root, all_files, findings)
    unknown_pass(root, all_files, findings)
    reference_pass(root, all_files, findings)
    version_string_pass(root, all_files, findings)
    unknowns_summary = unknowns_summary_pass(root, all_files, findings)

    by_severity = {"CRITICAL": [], "WARNING": [], "NOTE": []}
    for f in findings:
        by_severity.setdefault(f.severity, []).append(f)

    report = {
        "tool": TOOL_NAME,
        "tool_version": TOOL_VERSION,
        "repo_root": root,
        "files_scanned": len(all_files),
        "aliases_source": _ALIASES_SOURCE,
        "summary": {sev: len(items) for sev, items in by_severity.items()},
        "findings": [f.to_dict() for f in findings],
        "unknowns_summary": unknowns_summary,
    }
    return report


def print_summary(report):
    print(f"Files scanned: {report['files_scanned']}")
    print(f"Aliases source: {report['aliases_source']}")
    print()
    for sev in ("CRITICAL", "WARNING", "NOTE"):
        count = report["summary"].get(sev, 0)
        print(f"{sev}: {count}")
    print()
    for sev in ("CRITICAL", "WARNING"):
        items = [f for f in report["findings"] if f["severity"] == sev]
        if items:
            print(f"=== {sev} ===")
            for item in items:
                print(f"  [{item['category']}] {item['file']}: {item['message']}")
            print()


def print_health_summary(report):
    """
    Tier 1 + Tier 2 health summary, added 2026-08-27 per a scoped
    dashboard request. Tier 1 = PASS/FAIL per existing check category,
    derived from CRITICAL/WARNING counts already in this report — no
    new checking logic, just a threshold read on what the five passes
    above already found. Tier 2 = active-unknown counts from
    Unknowns.md's own Priority column, via unknowns_summary_pass.

    Deliberately does NOT include a "Governance state" / "Physical
    validation" / overall "ALPHA readiness" badge. Those would require
    inventing a threshold this repository's own doctrine does not
    define anywhere, which is exactly the kind of manufactured-looking-
    mechanical number this repo's own Placeholder/Analogous confidence
    discipline exists to prevent. If that judgment is wanted, it
    belongs to a human, as an explicitly-dated, explicitly-manual
    field — not this function.
    """
    by_cat = {}
    for f in report["findings"]:
        by_cat.setdefault(f["category"], []).append(f)

    categories = [
        ("REGISTRY", "Registry (Routing.md coverage)"),
        ("CONSTITUTION", "Metadata / Ethical Anchor"),
        ("STRUCTURE", "Metadata / File State consistency"),
        ("DUPLICATE_ID", "Sidecar ID uniqueness"),
        ("REFERENCE", "Cross-reference resolution"),
        ("VERSION_STRING", "Version-citation freshness"),
    ]

    print("=" * 46)
    print("REPOSITORY HEALTH —", report["repo_root"])
    print("=" * 46)
    print()
    print(f"Files scanned: {report['files_scanned']}")
    print(f"Aliases source: {report['aliases_source']}")
    print()
    print("--- Tier 1: mechanical checks (PASS/FAIL) ---")
    for cat_key, cat_label in categories:
        items = by_cat.get(cat_key, [])
        crit = sum(1 for i in items if i["severity"] == "CRITICAL")
        warn = sum(1 for i in items if i["severity"] == "WARNING")
        status = "FAIL" if crit else ("REVIEW" if warn else "PASS")
        note = f" ({crit} critical, {warn} warning)" if (crit or warn) else ""
        print(f"  {cat_label:<38} {status}{note}")
    print()
    print("--- Tier 2: active unknowns (from Unknowns.md's own tables) ---")
    us = report["unknowns_summary"]
    print(f"  Total active (Open/In Progress/Reopened): {us['total']}")
    for bucket in ("Critical", "Blocking", "Major", "Minor", "Unlabeled"):
        if bucket in us["by_priority"]:
            print(f"    {bucket:<12} {us['by_priority'][bucket]}")
    other = {k: v for k, v in us["by_priority"].items()
             if k not in ("Critical", "Blocking", "Major", "Minor", "Unlabeled")}
    if other:
        print(f"    (other Priority-column values found: {other})")
    print()
    print("  Note: 'Blocking' here reflects this table's own Priority")
    print("  column value, not a cross-check of each owning file's")
    print("  Blocking: Yes/No sidecar field. See function docstring.")
    print()
    print("Not included: no generated \"ALPHA readiness\" or \"Governance")
    print("state\" badge. See print_health_summary() docstring for why.")
    print("=" * 46)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python integrity_check.py <repo_root> [--json output.json] [--health]")
        sys.exit(1)

    repo_root = sys.argv[1]
    report = run(repo_root)

    if "--health" in sys.argv:
        print_health_summary(report)
    else:
        print_summary(report)

    if "--json" in sys.argv:
        idx = sys.argv.index("--json")
        out_path = sys.argv[idx + 1]
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"Full report written to {out_path}")
