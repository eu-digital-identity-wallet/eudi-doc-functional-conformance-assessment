#!/usr/bin/env python3
"""Replace mike alias symlinks with small HTML redirect trees."""

from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
from urllib.parse import quote


def redirect_document(target_url: str) -> str:
    escaped_url = html.escape(target_url, quote=True)
    javascript_url = json.dumps(target_url)
    return (
        "<!doctype html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        f'  <meta http-equiv="refresh" content="0; url={escaped_url}">\n'
        f'  <link rel="canonical" href="{escaped_url}">\n'
        "  <title>Redirecting</title>\n"
        f"  <script>location.replace({javascript_url} + location.search + location.hash)</script>\n"
        "</head>\n"
        f'<body><a href="{escaped_url}">Continue</a></body>\n'
        "</html>\n"
    )


def replace_alias(root: Path, alias: str) -> tuple[str, int]:
    alias_path = root / alias
    if not alias_path.is_symlink():
        raise RuntimeError(f"Expected mike alias symlink: {alias_path}")

    root_resolved = root.resolve()
    target_path = alias_path.resolve(strict=True)
    try:
        target_relative = target_path.relative_to(root_resolved)
    except ValueError as error:
        raise RuntimeError(f"Alias target escapes site root: {alias_path}") from error
    if not target_path.is_dir():
        raise RuntimeError(f"Alias target is not a directory: {target_path}")

    source_pages = sorted(target_path.rglob("*.html"))
    if not source_pages:
        raise RuntimeError(f"Alias target has no HTML pages: {target_path}")

    alias_path.unlink()
    for source_page in source_pages:
        relative_page = source_page.relative_to(target_path)
        destination = alias_path / relative_page
        destination.parent.mkdir(parents=True, exist_ok=True)

        logical_source = root / target_relative / relative_page
        if source_page.name == "index.html":
            redirect_target = logical_source.parent
            trailing_slash = True
        else:
            redirect_target = logical_source
            trailing_slash = False

        relative_url = os.path.relpath(redirect_target, destination.parent)
        target_url = quote(relative_url.replace(os.sep, "/"), safe="/.")
        if trailing_slash:
            target_url += "/"
        destination.write_text(redirect_document(target_url), encoding="utf-8")

    return target_relative.as_posix(), len(source_pages)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("aliases", nargs="+")
    args = parser.parse_args()

    if not args.root.is_dir():
        raise RuntimeError(f"Site root is not a directory: {args.root}")

    for alias in args.aliases:
        target, page_count = replace_alias(args.root, alias)
        print(f"Replaced {alias} -> {target} with {page_count} redirect pages")


if __name__ == "__main__":
    main()
