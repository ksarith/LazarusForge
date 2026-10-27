"""
Lazarus Forge - Shared Audit Library (audit_lib.py)

Extracted from Automation/AUDIT_HARNESS.py, 2026-07-21, so that
Automation/integrity_check.py (repo-wide checks) and AUDIT_HARNESS.py
(single-session audits) both import one implementation of routing
parsing, cross-reference extraction, and finding classification instead
of maintaining two.

This split exists because of a real, named failure pattern from this
repository's own audit history: a concept defined in two places desyncs
the moment one side updates (AP-021, recurred as AP-026). Routing parsing
and cross-reference classification were at risk of becoming a second
instance of exactly that pattern the moment a second tool needed them.
See Admin/Auditor_Protocols.md AP-025/AP-026 and Admin/File_Template.md
§Self-Referential Version Strings for the doctrine this follows.

Public API (previously underscore-prefixed internals of AUDIT_HARNESS.py —
promoted here rather than left private, since they are now an intended
reuse surface, not internal implementation detail):

    parse_routing(content) -> dict
    extract_md_refs(content) -> set
    check_cross_refs(filename, content, registry, aliases, findings) -> None

Also defines Finding, the structured-finding class both tools append to.
Every finding carries severity and category from construction — not
retrofitted onto a plain string later.
"""

import re


class Finding:
    """Structured finding with severity, category, file, and message."""
    def __init__(self, severity, category, file_path, message):
        self.severity = severity    # CRITICAL | MAJOR | WARNING
        self.category = category    # CONSTITUTION | STRUCTURE | REFERENCE | REGISTRY | DUPLICATE_ID | VERSION_STRING
        self.file_path = file_path
        self.message = message

    def __str__(self):
        return f"[{self.severity}/{self.category}] {self.file_path}: {self.message}"

    def to_dict(self):
        return {
            "severity": self.severity,
            "category": self.category,
            "file": self.file_path,
            "message": self.message,
        }


def parse_routing(content):
    """
    Parse Routing.md Master Routing Map table into {short_name: repo_path}.
    Expects rows like: | `Admin/Foo.md` | [Raw](...) | [Repo](...) | ... |
    Returns dict mapping basename → folder-prefixed path.
    NOTE: only matches backtick-quoted paths ending in .md or .py (case-
    sensitive by design — see Automation/Routing.md 2026-07-21 correction
    note on the AUDIT_HARNESS.PY casing incident this caught). Files
    without an extension or containing spaces (e.g. the two Admin/ Tier 0
    philosophical/theoretical documents) will not be picked up here and
    must be hand-maintained in a caller's ALIASES dict instead.
    """
    registry = {}
    for line in content.splitlines():
        m = re.search(r'`([^`]+\.(?:md|py))`', line)
        if not m:
            continue
        full_path = m.group(1)
        short = full_path.split("/")[-1]
        if short not in registry:
            registry[short] = full_path
    return registry


def extract_md_refs(content):
    """
    Extract internal .md file paths from content.
    Catches: markdown links, backtick paths.
    Skips URLs (http/https) and non-.md references.
    """
    refs = set()
    for link in re.findall(r'\[.*?\]\(([^)]+)\)', content):
        clean = link.split('#')[0].strip()
        if clean.endswith('.md') and not clean.startswith('http'):
            refs.add(clean)
    for path in re.findall(r'`([A-Za-z][A-Za-z0-9_/]+\.md)`', content):
        refs.add(path)
    return refs


# Planned renames: paths that appear in docs as future canonical names
# before Routing.md has been updated. Shared here rather than duplicated
# per-caller, same reasoning as the rest of this module.
PLANNED_RENAMES = {
    "Forge_Flow.md": "Architecture/Forge_flow.md — casing correction pending",
}

# Archive path pattern — references to versioned archive files.
_ARCHIVE_PAT = re.compile(
    r'(?:Archive/|_v\d+\.|_20\d{6}|v0\.\d+\.md$)', re.IGNORECASE
)


def check_cross_refs(filename, content, registry, aliases, findings):
    """
    Extract internal .md references and classify any that don't resolve
    against the registry: LEGACY (known alias), PLANNED (pending rename),
    ARCHIVE (versioned archive path), or UNKNOWN (investigate).

    `aliases` is passed explicitly rather than read from a caller's module
    global — the original AUDIT_HARNESS.py version of this function read
    a module-level ALIASES dict directly, which meant it could only ever
    be called correctly from inside that module. Fixed here as part of
    the extraction, not preserved as-is, since preserving it would have
    just relocated the same hidden-dependency problem into a second file.
    """
    refs = extract_md_refs(content)
    for ref in refs:
        clean = ref.lstrip('./')
        if any(x in ref for x in ['http', 'Lazarus-Forge-', 'Astroid', 'planned']):
            continue

        registry_paths = set(registry.values()) | set(registry.keys())

        if clean in registry_paths:
            continue  # Resolved — no finding

        if clean in aliases or clean.replace('Admin/', '').replace('Operations/', '') in aliases:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[LEGACY] '{ref}' — legacy name; check Rename Registry "
                f"in Discovery.md for canonical path."
            ))
        elif clean in PLANNED_RENAMES:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[PLANNED] '{ref}' — {PLANNED_RENAMES[clean]}"
            ))
        elif _ARCHIVE_PAT.search(clean):
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[ARCHIVE] '{ref}' — versioned archive reference; "
                f"expected once Archive/ is established."
            ))
        else:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[UNKNOWN] '{ref}' — no canonical or alias match. "
                f"Investigate: stale reference or missing Routing.md entry."
            ))

# ---------------------------------------------------------------------------
# Bare colliding-ID citation check (PKC-021 item iii, added 2026-10-27,
# human-authorized autonomous management).
#
# Canonical_Terms CT-007 and the PKC-003 ruling (2026-10-25) require that a
# citation of another file's ID use the qualified form `File.md XXX-NNN`.
# Prefixes in COLLIDING_PREFIXES are known to be defined in more than one
# file, so a bare occurrence is worth surfacing for reviewer judgment.
# Deliberately conservative: an ID is treated as qualified if a
# `Something.md` token appears within QUALIFY_WINDOW characters. Frozen
# history and a file's own sidecar definition rows are reviewer-exempt,
# not machine-exempt -- this is a review list, not an error list.

COLLIDING_PREFIXES = {"EC", "ASM", "CF", "AP", "TS", "SP", "FA", "FL", "GF", "GI"}

_BARE_ID_RE = re.compile(r"\b([A-Z]{2,4})-(\d{3})\b")
_MD_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+\.md")
QUALIFY_WINDOW = 60


def check_bare_id_citations(content, filename, own_prefixes=()):
    """Flag bare citations of colliding prefixes lacking a nearby file
    qualifier. Appends WARNING/REFERENCE findings to the returned list.

    own_prefixes: prefixes this file itself defines -- bare uses of those
    are local references, not cross-file citations, and are skipped.
    """
    findings = []
    for m in _BARE_ID_RE.finditer(content):
        prefix, num = m.group(1), m.group(2)
        if prefix not in COLLIDING_PREFIXES or prefix in own_prefixes:
            continue
        window = content[max(0, m.start() - QUALIFY_WINDOW): m.end() + QUALIFY_WINDOW]
        if _MD_TOKEN_RE.search(window):
            continue  # qualified within the window
        findings.append(Finding(
            "WARNING", "REFERENCE", filename,
            "[BARE-ID] '%s-%s' -- colliding prefix cited without a "
            "qualifying File.md within %d chars (CT-007 / PKC-003 ruling "
            "2026-10-25). Reviewer judgment: sidecar definition rows and "
            "frozen history are exempt." % (prefix, num, QUALIFY_WINDOW)
        ))
    return findings
