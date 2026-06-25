#!/usr/bin/env python3
"""
Assemble the FCAF docs into a single Markdown stream for the PDF build.

The MkDocs site expands `{% include-markdown ... %}` directives (and applies
heading offsets) via the include-markdown plugin. Pandoc does not understand
that plugin, so feeding the raw docs/fcaf/*.md to pandoc (a) prints the literal
`{% include-markdown ... %}` directives into the PDF and (b) produces a flat,
alphabetical, badly nested table of contents.

This script reproduces what MkDocs does, using only the standard library:
  - it walks the Functional Conformance nav order from mkdocs.yml,
  - recursively expands every include-markdown directive (resolving its glob
    relative to the including file and applying cumulative heading offsets),
  - compacts heading-level gaps so the structure nests cleanly (no skipped
    levels), which gives pandoc a sensible TOC.

Output goes to stdout. Run from the repository root:  python3 pandoc/assemble_pdf.py
Standard library only, so it does not need the venv.
"""
import os, re, sys, glob
import signal

DOCS_DIR = "docs"
MKDOCS = "mkdocs.yml"

INCLUDE_RE = re.compile(r'\{%\s*include-markdown\s+"([^"]+)"\s+heading-offset=(\d+)')
HEADING_RE = re.compile(r'^(#{1,6})(\s.*)$')
FENCE_RE = re.compile(r'^\s*(```+|~~~+)')
NAV_PATH_RE = re.compile(r'fcaf/[^\s\'"]+\.md')
PLACEHOLDER_RE = re.compile(r'^This section contains all tests applicable\b', re.IGNORECASE)
TOC_UNLISTED_RE = re.compile(r'^(?:\d+\.\s+|\[[^\]]+\]$)')

if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)


def nav_entry_paths():
    """Ordered, de-duplicated list of `docs/fcaf/....md` page paths from the MkDocs nav."""
    text = open(MKDOCS, encoding="utf-8").read()
    seen, out = set(), []
    for match in NAV_PATH_RE.finditer(text):
        path = os.path.join(DOCS_DIR, match.group(0))
        if path in seen or is_placeholder_page(path):
            continue
        seen.add(path)
        out.append(path)
    return out


def is_placeholder_page(path):
    """Skip leaf pages that only announce a future test section and contain no real content."""
    if not os.path.isfile(path):
        return False
    lines = open(path, encoding="utf-8").read().splitlines()
    if any(INCLUDE_RE.search(line) for line in lines):
        return False

    content = [line.strip() for line in lines if line.strip()]
    headings = [line for line in content if HEADING_RE.match(line)]
    body = [line for line in content if not HEADING_RE.match(line)]
    return len(headings) == 1 and len(body) <= 2 and any(PLACEHOLDER_RE.match(line) for line in body)


def shift(line, offset):
    if offset <= 0:
        return line
    hm = HEADING_RE.match(line)
    if not hm:
        return line
    level = min(len(hm.group(1)) + offset, 6)
    return "#" * level + hm.group(2)


def expand(path, offset, stack):
    """Return the expanded lines of `path`, headings shifted by `offset`."""
    if path in stack:                       # guard against accidental include cycles
        return [f"<!-- skipped recursive include: {path} -->"]
    if not os.path.isfile(path):
        return [f"<!-- missing include target: {path} -->"]
    lines = open(path, encoding="utf-8").read().splitlines()
    out, in_fence, fence = [], False, ""
    for line in lines:
        fm = FENCE_RE.match(line)
        if fm and not in_fence:
            in_fence, fence = True, fm.group(1)[0]
            out.append(line); continue
        if in_fence:
            if line.lstrip().startswith(fence * 3):
                in_fence = False
            out.append(line); continue
        inc = INCLUDE_RE.search(line)
        if inc:
            pattern, off = inc.group(1), int(inc.group(2))
            base = os.path.dirname(path)
            for match in sorted(glob.glob(os.path.join(base, pattern))):
                out.append("")
                out += expand(match, offset + off, stack + [path])
                out.append("")
            continue
        out.append(shift(line, offset))
    return out


def compact_headings(lines):
    """Remove heading-level gaps so nesting is contiguous (1,2,3,... with no skips)."""
    out, in_fence, fence, stack = [], False, "", []
    for line in lines:
        fm = FENCE_RE.match(line)
        if fm and not in_fence:
            in_fence, fence = True, fm.group(1)[0]
            out.append(line); continue
        if in_fence:
            if line.lstrip().startswith(fence * 3):
                in_fence = False
            out.append(line); continue
        hm = HEADING_RE.match(line)
        if hm:
            level = len(hm.group(1))
            while stack and stack[-1] >= level:
                stack.pop()
            stack.append(level)
            out.append("#" * min(len(stack), 6) + hm.group(2))
        else:
            out.append(line)
    return out


def compact_blank_lines(lines):
    """Collapse repeated blank lines outside fenced code blocks."""
    out, in_fence, fence, blanks = [], False, "", 0
    for line in lines:
        fm = FENCE_RE.match(line)
        if fm and not in_fence:
            in_fence, fence, blanks = True, fm.group(1)[0], 0
            out.append(line)
            continue
        if in_fence:
            if line.lstrip().startswith(fence * 3):
                in_fence = False
            out.append(line)
            continue

        if line.strip():
            blanks = 0
            out.append(line)
        else:
            blanks += 1
            if blanks == 1 and out:
                out.append("")
    while out and not out[-1].strip():
        out.pop()
    return out


def mark_unlisted_headings(lines):
    """Keep generated TOCs from listing numbered field headings or version labels."""
    out, in_fence, fence = [], False, ""
    for line in lines:
        fm = FENCE_RE.match(line)
        if fm and not in_fence:
            in_fence, fence = True, fm.group(1)[0]
            out.append(line)
            continue
        if in_fence:
            if line.lstrip().startswith(fence * 3):
                in_fence = False
            out.append(line)
            continue

        hm = HEADING_RE.match(line)
        if hm and TOC_UNLISTED_RE.match(hm.group(2).strip()):
            out.append(f"{line} {{.unnumbered .unlisted}}")
        else:
            out.append(line)
    return out


def main():
    assembled = []
    for entry in nav_entry_paths():
        assembled += expand(entry, 0, [])
        assembled += ["", ""]
    lines = compact_blank_lines(mark_unlisted_headings(compact_headings(assembled)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
