"""Point the "edit" and "view source" actions at the branch a page actually lives on.

The rendering shell lives on `site` and the FCAF content lives on the maturity
branches, so a single `edit_uri` cannot be right for both: `site` carries no
`docs/fcaf` at all. With the static setting, every content page offered to
*create a new file* on `site`, and its "view source" counterpart 404'd.

Material derives both buttons from one value, `page.edit_url` (see
partials/actions.html: the view link is the edit link with `edit`/`blob`
swapped for `raw`), so setting it correctly per page fixes both at once.

Which ref a content page belongs to is a property of the build, not of the
repository, so it comes from the environment:

    FCAF_CONTENT_REF=submitted   (default)
    FCAF_CONTENT_REF=v0.1.0      release builds

On a release build the content is an immutable snapshot, so neither button makes
sense for a content page: you cannot edit a tag, and "view source" invites edits
to an archived version. Material hides both buttons when `edit_url` is empty
(`{% if page.edit_url %}` in partials/actions.html), so they are suppressed.
Shell pages keep theirs, because the shell is never versioned: it is always the
current `site` branch, whichever content version is being rendered.
"""

import os

CONTENT_PREFIX = "fcaf/"
SHELL_REF = "site"


def _content_ref() -> str:
    return os.environ.get("FCAF_CONTENT_REF", "submitted").strip() or "submitted"


def _is_tag(ref: str) -> bool:
    return ref.startswith("v") and ref[1:2].isdigit()


def on_page_context(context, page, config, nav):
    repo_url = (config.get("repo_url") or "").rstrip("/")
    if not repo_url:
        return context

    src = page.file.src_uri
    if src.startswith(CONTENT_PREFIX):
        ref = _content_ref()
        if _is_tag(ref):
            # immutable snapshot: hide both buttons rather than link into a tag
            page.edit_url = None
            return context
    else:
        # the shell is never versioned; it is always the current site branch
        ref = SHELL_REF

    page.edit_url = f"{repo_url}/edit/{ref}/docs/{src}"
    return context
