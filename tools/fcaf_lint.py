#!/usr/bin/env python3
"""FCAF test-case format guard.

Validates the structural conventions of FCAF test-case files. Structure only:
it never judges whether an assertion matches a specification.

    fcaf_lint.py [--root docs/fcaf] [--changed-only REF] [--fix]
                 [--format text|github] [--enforce CODES | --enforce-all
                 | --warn-only] [paths...]

Exit status is 1 when a blocking finding remains, 0 otherwise. Warnings never
change the exit status; they are reported with a count so progress is visible.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
from collections import Counter, defaultdict

# --------------------------------------------------------------------------- phasing
#
# Enforcement is staged. A check blocks only once its backlog in the corpus has
# been cleared, so an existing defect never blocks an unrelated pull request.
# Promoting a check is a one-line change here, with a visible history.
#
# Phase 1 (this list): every check whose corpus backlog was already zero.
# Still reported as warnings, with counts, until their backlog is cleared:
#   FC052 final newline, FC002 section order, FC041 undefined defaults,
#   FC043 dead placeholder text, FC042 TODO/TBD, FC040 reference tokens,
#   FC032 empty profile applicability, FC021 step/result parity,
#   FC003 unknown section name, FC014 duplicate test case ID.
# Permanently advisory (large, judgement-bound backlogs):
#   FC100 CIR/ETSI anchor, FC101/FC102 ICS vocabulary, FC011/FC013 identifiers.
ENFORCED = {
    "FC001",  # required section missing
    "FC004",  # duplicate section heading
    "FC010",  # missing H1 test case ID
    "FC012",  # unknown test layer in the ID
    "FC020",  # list numbering not consecutive
    "FC022",  # pseudo list marker such as "3a."
    "FC023",  # no numbered test steps
    "FC030",  # relevancy format, vocabulary and separator
    "FC031",  # mutually exclusive relevancy combination
    "FC050",  # CR characters
    "FC051",  # trailing whitespace
    "FC053",  # unbalanced code fence
    "FC054",  # heading without a space after the hashes
    "FC055",  # heading not followed by a blank line
    "FC060",  # broken relative link
}

SECTIONS = [
    "Objective",
    "References",
    "Profile applicability",
    "EUDI-wallet relevancy",
    "Technology",
    "Preconditions",
    "Test Scenario",
    "Expected results",
    "Comments",
]
OPTIONAL = {"Technology", "Comments"}
REQUIRED = [s for s in SECTIONS if s not in OPTIONAL]
ORDER = {s: i for i, s in enumerate(SECTIONS)}

ORIGIN = ("EUDI_agnostic", "EUDI_generic", "EUDI_specific")
SCOPE = ("EUDI_required", "EUDI_optional", "EUDI_forbidden", "EUDI_undefined")
RELEVANCY_RE = re.compile(rf"^({'|'.join(ORIGIN)}) \| ({'|'.join(SCOPE)})$")
EXCLUSIVE = {("EUDI_agnostic", "EUDI_required"), ("EUDI_specific", "EUDI_forbidden")}

PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|XXX|to be defined|to be completed|to be determined)\b", re.I)
DEAD_TEXT_RE = re.compile(r"This is the case\.")
ISSUE_REF_RE = re.compile(r"#\d+|https?://\S*/issues/\d+")
TOKEN_RE = re.compile(r"\[([^\]\[]{1,60})\](?!\()")
ANCHOR_RE = re.compile(r"\[(EU )?CIR \d{4}/\d+( amended)?\]|\[ETSI[^\]]*\]")
DEFAULT_RE = re.compile(r"default_[A-Za-z0-9_]+")
PSEUDO_MARKER_RE = re.compile(r"^\s*(?:\d+[a-z]|[a-z]\d)[.)]\s+\S", re.M)
LIST_ITEM_RE = re.compile(r"^(\d+)[.)]\s")

LAYERS = {"DM", "MS", "IA", "SM", "UC", "SH", "O"}


class Finding:
    __slots__ = ("path", "line", "code", "message")

    def __init__(self, path, line, code, message):
        self.path, self.line, self.code, self.message = path, line, code, message

    def blocking(self, enforced):
        return self.code in enforced


def split_sections(text):
    """[(name, start_line, body)] for every level-2 heading, in file order."""
    out, cur, buf, start = [], None, [], 0
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if m:
            if cur is not None:
                out.append((cur, start, "\n".join(buf)))
            cur, buf, start = m.group(1), [], i
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out.append((cur, start, "\n".join(buf)))
    return out


def numbered(body):
    return [m.group(1) for m in (LIST_ITEM_RE.match(l) for l in body.splitlines()) if m]


def controlled_vocabulary(root: pathlib.Path):
    """ICS statements from ics.md and the ISO mdoc test suite page."""
    vocab = set()
    for rel in ("ics.md", "suts/wallet_solution/relying_party/testsuite_isomdoc.md"):
        p = root / rel
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[1] and not set(cells[1]) <= set("-: "):
                vocab.add(cells[1].rstrip(".").strip().lower())
    return vocab


def reference_keys(root: pathlib.Path):
    p = root / "references.md"
    if not p.is_file():
        return set()
    return set(re.findall(r"^\|\s*(\[[^\]]+\])\s*\|", p.read_text(encoding="utf-8"), re.M))


def defined_defaults(root: pathlib.Path):
    p = root / "defaults.md"
    if not p.is_file():
        return set()
    text = p.read_text(encoding="utf-8")
    return {m.group(1) for m in re.finditer(r"^#{2,4}\s+`?(default_[A-Za-z0-9_]+)`?", text, re.M)}


def check_file(path: pathlib.Path, root: pathlib.Path, ctx):
    text = path.read_text(encoding="utf-8")
    out = []
    add = lambda ln, code, msg: out.append(Finding(path, ln, code, msg))
    rel = path.relative_to(root.parent) if root.parent in path.parents else path

    # --- whitespace and encoding hygiene -------------------------------------
    if "\r" in text:
        add(1, "FC050", "file contains CR characters, use LF line endings")
    for i, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            add(i, "FC051", "trailing whitespace")
    if not text.endswith("\n") or text.endswith("\n\n"):
        add(len(text.splitlines()), "FC052", "file must end with exactly one newline")
    if text.count("```") % 2:
        add(1, "FC053", "unbalanced fenced code block")
    for m in re.finditer(r"^(#{1,6})(?!#)(\S)", text, re.M):
        add(text[: m.start()].count("\n") + 1, "FC054", "heading needs a space after the hashes")
    for m in re.finditer(r"^(#{1,6} .*)\n(?!\n|\Z)", text, re.M):
        add(text[: m.start()].count("\n") + 1, "FC055", "heading must be followed by a blank line")
    for m in PSEUDO_MARKER_RE.finditer(text):
        ln = text[: m.start()].count("\n") + 1
        add(ln, "FC022", "pseudo list marker such as '3a.' does not render as a list item")

    # --- identity ------------------------------------------------------------
    h1 = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    if not h1:
        add(1, "FC010", "missing H1 title with the test case ID")
    else:
        tid = h1.group(1).strip()
        ctx["ids"][tid].append(rel)
        if tid != path.stem:
            add(1, "FC011", f"H1 '{tid}' does not match filename '{path.stem}'")
        parts = tid.split("_")
        if len(parts) >= 3 and parts[2] not in LAYERS:
            add(1, "FC012", f"unknown test layer '{parts[2]}' in the test case ID")
        if "__" in path.stem:
            add(1, "FC013", "double underscore in the filename marks an empty ID subdivision")

    # --- sections ------------------------------------------------------------
    secs = split_sections(text)
    names = [s[0] for s in secs]
    body = {n: b for n, _, b in secs}
    lineno = {n: l for n, l, _ in secs}
    for want in REQUIRED:
        if want not in names:
            add(1, "FC001", f"missing required section '## {want}'")
    for n, ln, _ in secs:
        if n not in ORDER:
            add(ln, "FC003", f"unknown section '## {n}'")
    idx = [ORDER[n] for n in names if n in ORDER]
    if idx != sorted(idx):
        add(1, "FC002", "sections are not in the canonical order: " + " > ".join(SECTIONS))
    if len(names) != len(set(names)):
        add(1, "FC004", "duplicate section heading")

    # --- numbering and parity ------------------------------------------------
    for name in ("Preconditions", "Test Scenario", "Expected results"):
        nums = numbered(body.get(name, ""))
        if nums and [int(x) for x in nums] != list(range(1, len(nums) + 1)):
            add(lineno.get(name, 1), "FC020",
                f"'{name}' numbering is not consecutive: {', '.join(nums)}")
    steps = len(numbered(body.get("Test Scenario", "")))
    results = len(numbered(body.get("Expected results", "")))
    if steps != results:
        add(lineno.get("Expected results", 1), "FC021",
            f"{steps} test steps but {results} expected results")
    if steps == 0:
        add(lineno.get("Test Scenario", 1), "FC023", "no numbered test steps")

    # --- relevancy -----------------------------------------------------------
    rel_body = body.get("EUDI-wallet relevancy", "").strip()
    m = RELEVANCY_RE.match(rel_body)
    if not m:
        add(lineno.get("EUDI-wallet relevancy", 1), "FC030",
            f"relevancy must read '<origin> | <scope>' with single spaces, found {rel_body!r}")
    elif (m.group(1), m.group(2)) in EXCLUSIVE:
        add(lineno.get("EUDI-wallet relevancy", 1), "FC031",
            f"mutually exclusive relevancy combination {m.group(1)} | {m.group(2)}")

    # --- profile applicability and technology --------------------------------
    prof = body.get("Profile applicability", "").strip()
    if not prof:
        add(lineno.get("Profile applicability", 1), "FC032",
            "empty Profile applicability, write 'None' when no profile restricts the test")
    elif prof.lower().rstrip(".") != "none":
        for line in [l.strip(" -*+\t") for l in prof.splitlines() if l.strip()]:
            if line.rstrip(".").lower() not in ctx["vocab"]:
                add(lineno.get("Profile applicability", 1), "FC101",
                    f"profile condition not found in the ICS: {line!r}")
    for line in [l.strip(" -*+\t") for l in body.get("Technology", "").splitlines() if l.strip()]:
        if line.rstrip(".").lower() not in ctx["vocab"]:
            add(lineno.get("Technology", 1), "FC102",
                f"technology condition not found in the ICS: {line!r}")

    # --- references ----------------------------------------------------------
    refs = body.get("References", "")
    for tok in sorted({f"[{t}]" for t in TOKEN_RE.findall(refs)}):
        if tok not in ctx["refkeys"]:
            add(lineno.get("References", 1), "FC040",
                f"reference token {tok} is not an Item reference in references.md")
    if refs.strip() and not ANCHOR_RE.search(refs):
        add(lineno.get("References", 1), "FC100",
            "no [EU CIR ...] or [ETSI ...] item anchors this test in the EUDI profile")

    # --- defaults, placeholders, links ---------------------------------------
    for name in sorted(set(DEFAULT_RE.findall(text))):
        if name not in ctx["defaults"]:
            add(1, "FC041", f"{name} is not defined in defaults.md")
    lines = text.splitlines()
    for m in PLACEHOLDER_RE.finditer(text):
        ln = text[: m.start()].count("\n") + 1
        # A placeholder is acceptable while it is tracked. Without an issue
        # reference on the same line nobody ever finds it again.
        if not ISSUE_REF_RE.search(lines[ln - 1]):
            add(ln, "FC042",
                f"placeholder {m.group(1)!r} needs a GitHub issue reference on the same line, "
                f"for example 'TBD (#123)'")
    for m in DEAD_TEXT_RE.finditer(text):
        add(text[: m.start()].count("\n") + 1, "FC043", "placeholder text 'This is the case.'")
    for m in re.finditer(r"\]\((?!https?:|#)([^)]+)\)", text):
        target = (path.parent / m.group(1).split("#")[0]).resolve()
        if not target.exists():
            add(text[: m.start()].count("\n") + 1, "FC060", f"link target does not exist: {m.group(1)}")
    return out


# ---------------------------------------------------------------------------- fixes


def autofix(path: pathlib.Path):
    """Repair only what cannot change meaning. Returns the list of applied fixes."""
    original = path.read_text(encoding="utf-8")
    text = original.replace("\r\n", "\n").replace("\r", "\n")
    applied = []
    if text != original:
        applied.append("line endings")
    stripped = "\n".join(l.rstrip() for l in text.split("\n"))
    if stripped != text:
        applied.append("trailing whitespace")
        text = stripped
    spaced = re.sub(r"^(#{1,6} .*)\n(?!\n)", r"\1\n\n", text, flags=re.M)
    if spaced != text:
        applied.append("blank line after heading")
        text = spaced
    text = text.rstrip("\n") + "\n"
    if text != original.rstrip("\n") + "\n":
        pass
    if not original.endswith("\n") or original.endswith("\n\n"):
        applied.append("final newline")

    secs = split_sections(text)
    names = [s[0] for s in secs]
    idx = [ORDER[n] for n in names if n in ORDER]
    if names and all(n in ORDER for n in names) and idx != sorted(idx):
        head_end = text.splitlines(keepends=True)
        preamble = "".join(head_end[: secs[0][1] - 1])
        blocks = {}
        lines = text.splitlines(keepends=True)
        for i, (name, start, _) in enumerate(secs):
            end = secs[i + 1][1] - 1 if i + 1 < len(secs) else len(lines)
            blocks[name] = "".join(lines[start - 1 : end]).rstrip("\n") + "\n"
        text = preamble + "\n".join(blocks[n] for n in sorted(names, key=lambda x: ORDER[x]))
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip("\n") + "\n"
        applied.append("section order")

    if text != original:
        path.write_text(text, encoding="utf-8")
    return applied


# ---------------------------------------------------------------------------- driver


def changed_files(ref):
    cmd = ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{ref}...HEAD"]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=ACMR", ref],
                             capture_output=True, text=True, check=True)
    return [pathlib.Path(p) for p in out.stdout.split()]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=pathlib.Path)
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path("docs/fcaf"))
    ap.add_argument("--changed-only", metavar="REF", help="only files changed against REF")
    ap.add_argument("--fix", action="store_true", help="apply meaning-preserving repairs")
    ap.add_argument("--format", choices=("text", "github"), default="text")
    ap.add_argument("--enforce", metavar="CODES",
                    help="comma separated check codes that block, overriding the staged default")
    ap.add_argument("--enforce-all", action="store_true", help="every finding blocks")
    ap.add_argument("--warn-only", action="store_true", help="never block, report only")
    args = ap.parse_args(argv)

    root = args.root
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    universe = sorted(p for p in (root / "suts").rglob("*.md") if p.name.startswith("WS_"))
    if args.paths:
        selected = [p for p in args.paths if p.name.startswith("WS_") and p.suffix == ".md"]
    elif args.changed_only:
        changed = {p.resolve() for p in changed_files(args.changed_only)}
        selected = [p for p in universe if p.resolve() in changed]
    else:
        selected = universe

    ctx = {
        "vocab": controlled_vocabulary(root),
        "refkeys": reference_keys(root),
        "defaults": defined_defaults(root),
        "ids": defaultdict(list),
    }

    fixed = Counter()
    if args.fix:
        for p in selected:
            for what in autofix(p):
                fixed[what] += 1

    findings = []
    for p in selected:
        findings.extend(check_file(p, root, ctx))
    # duplicate IDs are a corpus-level property, so always scan the whole corpus
    all_ids = defaultdict(list)
    for p in universe:
        m = re.search(r"^#\s+(.+?)\s*$", p.read_text(encoding="utf-8"), re.M)
        if m:
            all_ids[m.group(1).strip()].append(p)
    for tid, owners in sorted(all_ids.items()):
        if len(owners) > 1 and any(o in selected for o in owners):
            for o in owners:
                findings.append(Finding(o, 1, "FC014",
                                        f"test case ID '{tid}' is used by {len(owners)} files"))

    enforced = set(ENFORCED)
    if args.enforce:
        enforced = {c.strip().upper() for c in args.enforce.split(",") if c.strip()}
    if args.enforce_all:
        enforced = {f.code for f in findings}
    if args.warn_only:
        enforced = set()
    blocking = [f for f in findings if f.blocking(enforced)]
    warnings = [f for f in findings if not f.blocking(enforced)]

    for f in sorted(findings, key=lambda f: (str(f.path), f.line)):
        level = "error" if f.blocking(enforced) else "warning"
        if args.format == "github":
            print(f"::{level} file={f.path},line={f.line},title={f.code}::{f.message}")
        else:
            print(f"{f.path}:{f.line}: {level}: [{f.code}] {f.message}")

    print(f"\nchecked {len(selected)} test case files "
          f"({len(universe)} in the corpus)")
    if fixed:
        print("applied fixes: " + ", ".join(f"{v}x {k}" for k, v in fixed.most_common()))
    print(f"blocking findings: {len(blocking)}    warnings: {len(warnings)}")
    if blocking:
        counts = Counter(f.code for f in blocking)
        print("by check: " + ", ".join(f"{c}={n}" for c, n in counts.most_common()))
    if warnings:
        counts = Counter(f.code for f in warnings)
        print("warnings by check: " + ", ".join(f"{c}={n}" for c, n in counts.most_common()))
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
