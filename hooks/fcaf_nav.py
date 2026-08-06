"""Load the versioned FCAF navigation fragment into the site navigation."""

from pathlib import Path, PurePosixPath
from typing import Any

import yaml


FCAF_SECTION = "Functional Conformance"
FCAF_NAV_FILE = PurePosixPath("fcaf/.nav.yml")
FCAF_PATH_PREFIX = PurePosixPath("fcaf")


def _content_target(target: str) -> str:
    """Resolve a content-owned navigation target relative to docs/fcaf."""
    path = PurePosixPath(target)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"FCAF navigation target must stay inside docs/fcaf: {target}")
    return str(FCAF_PATH_PREFIX / path)


def _content_nav(entries: list[Any]) -> list[Any]:
    """Prefix every local target in a nested MkDocs navigation list."""
    resolved: list[Any] = []
    for entry in entries:
        if isinstance(entry, str):
            resolved.append(_content_target(entry))
            continue

        if not isinstance(entry, dict) or len(entry) != 1:
            raise ValueError(f"Unsupported FCAF navigation entry: {entry!r}")

        title, value = next(iter(entry.items()))
        if isinstance(value, list):
            resolved.append({title: _content_nav(value)})
        elif isinstance(value, str):
            resolved.append({title: _content_target(value)})
        else:
            raise ValueError(f"Unsupported FCAF navigation value for {title!r}: {value!r}")

    return resolved


def on_config(config: Any) -> Any:
    """Append the content-owned FCAF fragment to the shell-owned section."""
    docs_dir = Path(config["docs_dir"])
    nav_file = docs_dir / FCAF_NAV_FILE
    if not nav_file.is_file():
        raise FileNotFoundError(f"Required FCAF navigation file not found: {nav_file}")

    fragment = yaml.safe_load(nav_file.read_text(encoding="utf-8")) or {}
    entries = fragment.get("nav")
    if not isinstance(entries, list):
        raise ValueError(f"{nav_file} must contain a top-level 'nav' list")

    for item in config["nav"]:
        if isinstance(item, dict) and FCAF_SECTION in item:
            shell_entries = item[FCAF_SECTION]
            if not isinstance(shell_entries, list):
                raise ValueError(f"The {FCAF_SECTION!r} navigation entry must be a list")
            item[FCAF_SECTION] = [*shell_entries, *_content_nav(entries)]
            return config

    raise ValueError(f"Navigation section not found: {FCAF_SECTION}")
