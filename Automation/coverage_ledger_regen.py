#!/usr/bin/env python3
"""coverage_ledger_regen.py - regenerate Table II of AUDIT_COVERAGE_LEDGER.md and reconcile it against the recorded counts.

Composed 2026-11-08 at MAINT-84: stage 4 of the ratified MAINT-83 redraft section 8 (Addendum #4 to the aggregate template; the Rule 10 section 5c reconcile oracle, leg (i)). Python 3 stdlib only.

Pipeline:
  1. Parse section 2 (the findings ledger) of every Admin/AAudits/AUDIT_AGGREGATE_Admin-*.md.
  2. Classify every row with the fixed compound classifier (documented below).
  3. Recompute per-target Open M/W/F and Open W-C.
  4. Self-test the five frozen hand-counted fixtures (2026-11-08, MAINT-84).
  5. Compare against the recorded Table II in Archive/Audits/AUDIT_COVERAGE_LEDGER.md.

Fixed compound classifier:
  - severity = the first whitespace token of the Severity cell, uppercased.
  - Counting severities: MAJOR, WARNING, CRITICAL, FAIL (the ratified section 2 vocabulary).
  - INCOMPLETE and structural dash severities never count.
  - disposition = the first pipe cell from index 4 onward that starts with a recognized keyword.
  - COMPOUND dispositions split on slash; a row carries if ANY segment starts with a carrying
    keyword (the first-keyword-only rule undercounts compound rows; corrected at MAINT-84).
  - Carrying: Standing-open, Not re-tested, Asserted, Reported-not-fixed, Disclosed defect
    ("Reported-not-fixed (historical)" counts; the convention list is illustrative, disclosed).
  - Open M/W/F = counting severity AND carrying disposition.
  - Open W-C = NOTE severity AND a segment starting Standing-open or Watch-carried.
  - A disposition cell with no recognized keyword counts nowhere; the Table II reconcile
    surfaces any resulting drift rather than guessing.

Exit codes: 0 = fixtures pass and Table II reconciles; 1 = any fixture or reconcile failure (details printed). The first live execution is owed at the next Python-capable pass (no Python runtime on the composing line; MAINT-84 disclosure). Fixtures are frozen: if a fixture target's section 2 changes, the fixture fails BY DESIGN and must be re-frozen by dated addendum in the reconcile-report home, never edited silently.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AAUDITS = REPO_ROOT / "Admin" / "AAudits"
LEDGER = REPO_ROOT / "Archive" / "Audits" / "AUDIT_COVERAGE_LEDGER.md"

DISPOSITION_KEYWORDS = [
    "Standing-open", "Not re-tested", "Asserted", "Reported-not-fixed",
    "Disclosed defect", "Enacted", "Closed-by-ruling", "Positive-record",
    "Superseded", "Corrected-by-later-fact", "Watch-carried",
]
CARRYING = ["Standing-open", "Not re-tested", "Asserted", "Reported-not-fixed", "Disclosed defect"]
WC = ["Standing-open", "Watch-carried"]
COUNTING = {"MAJOR", "WARNING", "CRITICAL", "FAIL"}

FROZEN_FIXTURES = {
    # target short-name: (open_mwf, open_wc) - hand-counted 2026-11-08, MAINT-84
    "Adm_Scope_Map": (2, 2),
    "Economics": (0, 1),
    "Verification_Gates": (2, 0),
    "Hardware_Diversity_Ladder": (1, 1),
    "INTEGRITY_SWEEP_PROMPT": (1, 3),
}


def section(text, num):
    lines = text.split('\n')
    start = None
    for i, l in enumerate(lines):
        if l.startswith('## ' + str(num) + '.'):
            start = i
            break
    if start is None:
        return ''
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith('## '):
            end = i
            break
    return '\n'.join(lines[start:end])


def classify(text):
    s2 = section(text, 2)
    recs = []
    for l in s2.split('\n'):
        t = l.strip()
        if not t.startswith('|'):
            continue
        if '| Ref |' in t or '| Orig ID |' in t:
            continue
        cells = [c.strip() for c in l.split('|')]
        ref = cells[1] if len(cells) > 1 else ''
        if not ref or set(ref) <= {'-'}:
            continue
        sev = cells[3] if len(cells) > 3 else ''
        disp = ''
        for i in range(4, len(cells)):
            if not cells[i]:
                continue
            for k in DISPOSITION_KEYWORDS:
                if cells[i].startswith(k):
                    disp = cells[i]
                    break
            if disp:
                break
        recs.append((ref, sev, disp))

    def parts(d):
        return [p.strip() for p in d.split('/') if p.strip()]

    def starts_any(ps, keys):
        for p in ps:
            for k in keys:
                if p.startswith(k):
                    return True
        return False

    open_refs = []
    wc_refs = []
    for ref, sev, disp in recs:
        tokens = sev.split()
        token = tokens[0].upper() if tokens else ''
        ps = parts(disp)
        if token in COUNTING and starts_any(ps, CARRYING):
            open_refs.append(ref)
        if sev == 'NOTE' and starts_any(ps, WC):
            wc_refs.append(ref)
    return open_refs, wc_refs


def parse_table_two(text):
    rows = {}
    in_t2 = False
    for l in text.split('\n'):
        if l.startswith('## Table II'):
            in_t2 = True
            continue
        if in_t2 and l.startswith('## '):
            break
        if not in_t2:
            continue
        t = l.strip()
        if not t.startswith('|'):
            continue
        cells = [c.strip() for c in l.split('|')]
        if len(cells) < 7 or not cells[1].isdigit():
            continue
        target = cells[2].replace(chr(96), '')
        try:
            rec_open = int(cells[3])
            rec_wc = int(cells[4])
        except ValueError:
            continue
        rows[target] = (cells[1], rec_open, rec_wc)
    return rows


def main():
    failures = []
    for name in sorted(FROZEN_FIXTURES):
        exp_open, exp_wc = FROZEN_FIXTURES[name]
        path = AAUDITS / ('AUDIT_AGGREGATE_Admin-' + name + '.md')
        if not path.exists():
            print('FIXTURE FAIL: ' + name + ': ' + str(path) + ' missing')
            failures.append(name)
            continue
        o, w = classify(path.read_text(encoding='utf-8'))
        if len(o) != exp_open or len(w) != exp_wc:
            print('FIXTURE FAIL: ' + name + ': expected (' + str(exp_open) + ', ' + str(exp_wc) + ') got (' + str(len(o)) + ', ' + str(len(w)) + ')')
            failures.append(name)
        else:
            print('fixture ok: ' + name + ' (' + str(exp_open) + ', ' + str(exp_wc) + ')')

    computed = {}
    for path in sorted(AAUDITS.glob('AUDIT_AGGREGATE_Admin-*.md')):
        name = path.name[len('AUDIT_AGGREGATE_Admin-'):-len('.md')]
        o, w = classify(path.read_text(encoding='utf-8'))
        computed['Admin/' + name + '.md'] = (len(o), len(w), o, w)

    ledger_text = LEDGER.read_text(encoding='utf-8')
    recorded = parse_table_two(ledger_text)

    mismatches = []
    total_open = 0
    total_wc = 0
    for target in sorted(computed):
        open_n, wc_n, o_refs, w_refs = computed[target]
        total_open += open_n
        total_wc += wc_n
        if target not in recorded:
            mismatches.append('MISSING TABLE II ROW: ' + target)
            continue
        num, rec_open, rec_wc = recorded[target]
        if open_n != rec_open or wc_n != rec_wc:
            mismatches.append('MISMATCH row ' + num + ' ' + target + ': recorded (' + str(rec_open) + ', ' + str(rec_wc) + ') mechanical (' + str(open_n) + ', ' + str(wc_n) + ')')
    checked = len([t for t in computed if t in recorded])
    print('aggregated targets: ' + str(len(computed)) + '; mechanical totals: open ' + str(total_open) + ', W-C ' + str(total_wc) + '; Table II rows checked: ' + str(checked) + '; mismatches: ' + str(len(mismatches)))
    for m in mismatches:
        print(m)

    ok_fix = not failures
    ok_rec = len(mismatches) == 0 and checked == len(computed) and len(computed) > 0
    if ok_fix and ok_rec:
        print('REGEN OK: fixtures pass; Table II reconciles.')
        return 0
    print('REGEN FAIL: fixtures pass = ' + str(ok_fix) + '; reconcile pass = ' + str(ok_rec))
    return 1


if __name__ == '__main__':
    sys.exit(main())
