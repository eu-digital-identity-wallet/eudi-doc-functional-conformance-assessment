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
# Phase 1: every check whose corpus backlog was already zero.
# Phase 2: the conventions settled and normalised across the corpus, so
#   FC002 section order, FC003 section names, FC041 defaults, FC052 final
#   newline, FC056 invisible characters and FC057 indentation tabs now block.
# Phase 3: FC033, the spelling of None. All 378 test cases that carry no
#   profile restriction already write a plain None, so the backlog is zero.
# Phase 4: FC034 and FC035, the shape of References and Preconditions. All
#   1175 reference lines are already "- " items, and Preconditions is already
#   a numbered list, a bare None, or a fenced fixture. Both backlogs are zero.
# Still reported as warnings, with counts, until their backlog is cleared:
#   FC043 dead placeholder text, FC042 untracked TODO/TBD, FC040 reference
#   tokens, FC032 empty profile applicability, FC021 step/result parity,
#   FC014 duplicate test case ID.
# Warnings that wait on the ICS vocabulary being seeded and sorted:
#   FC103 condition that belongs in Preconditions, FC104 two conditions in one
#   entry. FC104 clears mechanically with --fix and can be promoted after one
#   normalisation pass; FC103 rests on a heuristic and must stay a warning.
# Permanently advisory (large, judgement-bound backlogs):
#   FC100 CIR/ETSI anchor, FC101/FC102 ICS vocabulary, FC011/FC013 identifiers.
ENFORCED = {
    "FC001",  # required section missing
    "FC002",  # sections not in the canonical order
    "FC003",  # unknown section name
    "FC004",  # duplicate section heading
    "FC010",  # missing H1 test case ID
    "FC012",  # unknown test layer in the ID
    "FC020",  # list numbering not consecutive
    "FC022",  # pseudo list marker such as "3a."
    "FC023",  # no numbered test steps
    "FC030",  # relevancy format, vocabulary and separator
    "FC031",  # mutually exclusive relevancy combination
    "FC033",  # None written in anything but its one accepted spelling
    "FC034",  # References not written as a "- " list
    "FC035",  # Preconditions neither a numbered list nor None
    "FC041",  # default_* not defined in defaults.md
    "FC050",  # CR characters
    "FC051",  # trailing whitespace
    "FC052",  # missing or duplicated final newline
    "FC053",  # unbalanced code fence
    "FC054",  # heading without a space after the hashes
    "FC055",  # heading not followed by a blank line
    "FC056",  # invisible character where a space belongs
    "FC057",  # tab used for indentation
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

# Profile applicability None means no profile restricts the test, so there is
# nothing to look up in the ICS. Exactly one spelling is accepted.
NONE = "None"

# A profile condition states what the implementation under test can do, so an
# implementer can declare it in the ICS: "Wallet supports X", "Wallet uses Y".
# A statement about what is stored instead describes one test's fixture, can
# never be declared, and belongs in Preconditions. The verb separates the two.
PRESENCE_RE = re.compile(r"(?i)\bcontains?\b|\b(is|are) (present|included)\b")

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

# Characters that look like an ordinary space but are not one. A single
# no-break space inside a profile condition is enough to stop it matching its
# ICS row, and nobody spots it by reading.
INVISIBLE = {
    "\u00a0": "no-break space",
    "\u202f": "narrow no-break space",
    "\u2007": "figure space",
    "\u2009": "thin space",
    "\u200b": "zero width space",
    "\ufeff": "zero width no-break space",
    "\u00ad": "soft hyphen",
}


def fenced_lines(text):
    """Per line: is it inside a fenced code block? Fixes stay out of those."""
    out, inside = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            inside = not inside
            out.append(True)
        else:
            out.append(inside)
    return out


# Protocol and data element identifiers must be written in backticks. The corpus
# writes the same one up to five ways: bare, in backticks, in straight, single
# or typographic quotes. `vp_token` appears 41 times in backticks, 41 times bare
# and 5 times quoted, which makes any search unreliable and reads as if the
# variants meant different things.
#
# Recognised by shape rather than by a list that would need maintaining:
# snake_case, reverse dotted names such as eu.europa.ec.eudi.pid.1, and JOSE
# algorithm names. Test case identifiers are excluded: they start with an
# upper-case class prefix, and the word boundaries below keep fragments of them
# from matching inside a cross reference.
_ID = (r"[a-z][a-z0-9]*(?:_[a-z0-9]+)+"
       r"|[a-z]+(?:\.[a-z0-9]+){2,}"
       r"|(?:ES|PS|RS|HS)(?:256|384|512)")
_EDGE_L = r"(?<![\w./_`'\u201c\u201d-])"
_EDGE_R = r"(?![\w/`'\u201c\u201d-])"

QUOTED_ID = re.compile(r"(['\"\u201c\u201d])(" + _ID + r")(['\"\u201c\u201d])")
BARE_ID = re.compile(_EDGE_L + r"(" + _ID + r")" + _EDGE_R)
TESTCASE_ID = re.compile(r"^WS_[A-Za-z0-9_]+$")
CURLY = re.compile(r'[\u201c\u201d]')


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
    fenced = fenced_lines(text)
    for i, line in enumerate(text.splitlines(), 1):
        if fenced[i - 1]:
            continue
        for ch, label in INVISIBLE.items():
            if ch in line:
                add(i, "FC056", f"{label} (U+{ord(ch):04X}) in the text, use a normal space")
                break
        if re.match(r"^[ ]*\t", line):
            add(i, "FC057", "tab used for indentation, use spaces")
        outside = re.sub(r"`[^`\n]*`", "", re.sub(r"\]\([^)]*\)", "]()", line))
        for m in QUOTED_ID.finditer(outside):
            add(i, "FC070", f"identifier {m.group(2)} is quoted, write it as `{m.group(2)}`")
        for m in BARE_ID.finditer(outside):
            add(i, "FC071", f"identifier {m.group(1)} is unmarked, write it as `{m.group(1)}`")
        if CURLY.search(line):
            add(i, "FC072", "typographic quotation mark in a test case, use a straight one")

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

    # --- section shape -------------------------------------------------------
    # Content lines of a section, with their file line number. Fenced blocks are
    # skipped, and so is the line that introduces one, because a fixture and the
    # sentence announcing it are not list items. The corpus writes that lead-in
    # both with and without a trailing colon, so the fence decides, not the
    # punctuation.
    def content(name):
        raw = body.get(name)
        if raw is None:
            return []
        out, inside, lines = [], False, raw.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("```"):
                inside = not inside
                continue
            if inside or not line.strip():
                continue
            nxt = next((l for l in lines[i + 1:] if l.strip()), "")
            if nxt.strip().startswith("```"):
                continue
            out.append((lineno.get(name, 1) + 1 + i, line))
        return out

    for ln, line in content("References"):
        if not re.match(r"^- \S", line) and not re.match(r"^\s+\S", line):
            add(ln, "FC034",
                f"every reference must be a '- ' list item, found {line.strip()!r}")

    if body.get("Preconditions", "").strip() != NONE:
        for ln, line in content("Preconditions"):
            if not LIST_ITEM_RE.match(line) and not re.match(r"^\s+\S", line):
                add(ln, "FC035",
                    "every precondition must be a numbered list item, or the "
                    f"whole section must read None, found {line.strip()!r}")

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
    elif prof != NONE:
        # Strip a leading list marker, but nothing else: a bare *None* is not a
        # list item, and stripping its asterisks would hide the very defect
        # FC033 is here to catch.
        for raw in [l for l in prof.splitlines() if l.strip()]:
            line = re.sub(r"^\s*[-*+]\s+", "", raw).strip()
            if line == NONE or line.rstrip(".").lower() in ctx["vocab"]:
                continue
            # A value that mentions none is a decorated none, not a profile the
            # ICS is missing. Same verdict either way, but say which one it is.
            # Same verdict in every branch, the value is not in the ICS. The
            # branches differ only in which repair they point at, so a wrong
            # guess costs a misleading sentence, never a wrong gate.
            if "none" in line.lower():
                add(lineno.get("Profile applicability", 1), "FC033",
                    f"write the value {NONE} plainly, not {line!r}")
            elif ";" in line:
                add(lineno.get("Profile applicability", 1), "FC104",
                    "one condition per entry, split this at the semicolon: "
                    f"{line!r}")
            elif PRESENCE_RE.search(line):
                add(lineno.get("Profile applicability", 1), "FC103",
                    "this states what the wallet contains, not what it "
                    f"supports, so it belongs in Preconditions: {line!r}")
            else:
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
    fenced = fenced_lines(text)
    repaired, touched_inv, touched_tab, touched_quotes = [], False, False, False
    for i, line in enumerate(text.split("\n")):
        if i < len(fenced) and fenced[i]:
            repaired.append(line)
            continue
        before = line
        line = QUOTED_ID.sub(lambda m: f"`{m.group(2)}`", line)
        if line != before:
            touched_quotes = True
        for ch in INVISIBLE:
            line = line.replace(ch, " " if ch not in ("\u200b", "\ufeff", "\u00ad") else "")
        while re.match(r"^[ ]*\t", line):
            line = re.sub(r"^([ ]*)\t", lambda m: m.group(1) + " " * (4 - len(m.group(1)) % 4), line)
        touched_inv |= before != line and any(c in before for c in INVISIBLE)
        touched_tab |= before != line and "\t" in before
        repaired.append(line)
    joined = "\n".join(repaired)
    if joined != text:
        if touched_inv:
            applied.append("invisible characters")
        if touched_tab:
            applied.append("indentation tabs")
        if touched_quotes:
            applied.append("quoted identifiers")
        text = joined

    # Both sections take None as a whole-section value, and both are written
    # with emphasis often enough to be worth repairing.
    for name in ("Profile applicability", "Preconditions"):
        sec = re.search(rf"(?m)^## {name}[ \t]*\n(.*?)(?=\n## |\Z)", text, re.S)
        if sec and sec.group(1).strip() != NONE and "none" == re.sub(
                r"[^a-z]", "", sec.group(1).lower()):
            body = sec.group(1)
            text = text[: sec.start(1)] + NONE + body[len(body.rstrip()):] + text[sec.end(1):]
            applied.append("None spelling")

    # Preconditions written with letters. The site renders the numbers as A., B.,
    # C., so a source letter is always someone copying what they saw. Nothing in
    # the corpus refers back to a precondition by its marker, so renumbering is
    # safe. Only an all-lettered section is touched; anything else is reported.
    pre = re.search(r"(?m)^## Preconditions[ \t]*\n(.*?)(?=\n## |\Z)", text, re.S)
    if pre:
        body_lines = pre.group(1).splitlines()
        content = [l for l in body_lines if l.strip()]
        if content and all(re.match(r"^[A-Za-z][.)]\s+\S", l) for l in content):
            n, out = 0, []
            for line in body_lines:
                if line.strip():
                    n += 1
                    line = re.sub(r"^[A-Za-z][.)]\s+", f"{n}. ", line)
                out.append(line)
            text = text[: pre.start(1)] + "\n".join(out) + text[pre.end(1):]
            applied.append("precondition numbering")

    # One condition per line. The corpus already writes several conditions as
    # several lines, so splitting a bundled entry only makes the existing shape
    # explicit. Skipped when a half would come out empty.
    papp = re.search(r"(?m)^## Profile applicability[ \t]*\n(.*?)(?=\n## |\Z)", text, re.S)
    if papp and papp.group(1).strip() != NONE:
        out, changed = [], False
        for line in papp.group(1).splitlines():
            parts = [x.strip() for x in line.split(";")]
            if len(parts) > 1 and all(parts):
                indent = re.match(r"^\s*(?:-\s+)?", line).group(0)
                out.extend(indent + x for x in parts)
                changed = True
            else:
                out.append(line)
        if changed:
            body = papp.group(1)
            tail = body[len(body.rstrip("\n")):]
            text = text[: papp.start(1)] + "\n".join(out) + tail + text[papp.end(1):]
            applied.append("profile condition split")

    refs = re.search(r"(?m)^## References[ \t]*\n(.*?)(?=\n## |\Z)", text, re.S)
    if refs:
        out, inside, changed = [], False, False
        for line in refs.group(1).splitlines():
            s = line.strip()
            if s.startswith("```"):
                inside = not inside
                out.append(line)
                continue
            if inside or not s or re.match(r"^- \S", line) or re.match(r"^\s+\S", line):
                out.append(line)
                continue
            other = re.match(r"^\s*[*+]\s+(.*)$", line)
            out.append("- " + (other.group(1) if other else s))
            changed = True
        if changed:
            body = refs.group(1)
            tail = body[len(body.rstrip("\n")):]
            text = text[: refs.start(1)] + "\n".join(out) + tail + text[refs.end(1):]
            applied.append("reference list")

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
            # GitHub consumes file=, line= and title= to build the annotation and
            # prints only the message into the log, so the location has to be in
            # the message too. Annotations are also capped at ten per level per
            # step, which makes the log the only complete list.
            print(f"::{level} file={f.path},line={f.line},title={f.code}"
                  f"::{f.path.name}:{f.line}: [{f.code}] {f.message}")
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
