#!/usr/bin/env bash
#
# Preview the rendered FCAF site from ANY branch.
#
# The rendering shell (mkdocs.yml, theme, hooks) lives only on `site`; the test
# cases live only on the maturity branches. Neither half builds on its own:
#
#   - a bare `site` checkout fails with
#     "Required FCAF navigation file not found: docs/fcaf/.nav.yml"
#   - a content checkout has no mkdocs.yml, Makefile, theme or hooks at all
#
# This script composes the two in a temporary directory and serves that, so
# your working tree is never modified and content can never be committed to
# `site` by accident.
#
# It always prefers YOUR WORKING TREE. Whatever branch is checked out, whatever
# is on disk right now, including uncommitted edits, is what gets previewed.
# Only the half your branch does not have is filled in from a git ref:
#
#   on `site`         -> shell from your tree,  content from `submitted`
#   on `submitted`    -> content from your tree, shell from `site`
#   on any content
#   feature branch    -> content from your tree, shell from `site`
#   on a composed tree-> both halves from your tree
#
# Usage:
#
#   make preview                          # the normal case, from a site checkout
#   ./tools/preview.sh                    # same thing without make
#   ./tools/preview.sh -c reviewed        # fill the missing half from another ref
#   ./tools/preview.sh -c ../fcaf-content # or from a second local checkout
#   ./tools/preview.sh --build            # build once instead of serving
#
# From a content branch there is no Makefile, so run it straight from `site`:
#
#   git show origin/site:tools/preview.sh | bash
#
# That form needs no arguments: it detects the docs/fcaf in your working tree
# and previews exactly what you are editing.

set -euo pipefail

CONTENT=""
ACTION="serve"
ADDR="127.0.0.1:8000"

usage() { sed -n '2,30p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

while [ $# -gt 0 ]; do
  case "$1" in
    -c|--content) CONTENT="${2:?--content needs a ref or directory}"; shift 2 ;;
    -a|--addr)    ADDR="${2:?--addr needs host:port}"; shift 2 ;;
    --build)      ACTION="build"; shift ;;
    -h|--help)    usage 0 ;;
    *) echo "unknown argument: $1" >&2; usage 1 ;;
  esac
done

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }
REPO="$(git rev-parse --show-toplevel)"

# --- locate the shell -------------------------------------------------------
# The working tree wins. Only fall back to a ref when this branch has no shell.
SHELL_MODE="" SHELL_SRC=""
if [ -f "$REPO/mkdocs.yml" ]; then
  SHELL_MODE="path"; SHELL_SRC="$REPO"
else
  for ref in site origin/site public/site upstream/site; do
    if git -C "$REPO" cat-file -e "$ref:mkdocs.yml" 2>/dev/null; then
      SHELL_MODE="ref"; SHELL_SRC="$ref"; break
    fi
  done
  if [ -z "$SHELL_MODE" ]; then
    echo "No mkdocs.yml in this tree and no 'site' ref found. Fetch it first:" >&2
    echo "  git fetch origin site" >&2
    exit 1
  fi
fi

# --- locate the content -----------------------------------------------------
# Three cases: an explicit directory, an explicit ref, or auto-detection.
#
# Bare branch names are resolved against the remotes too. `git archive reviewed`
# fails outright when there is no local `reviewed` branch, because git does not
# DWIM bare names to refs/remotes/*. Resolving here means an unreachable ref is
# reported immediately instead of aborting mid-compose.
# Returns 0 and a renderable ref; 2 and a ref that exists but cannot render;
# 1 when nothing matched. Renderable candidates win, so a stale local branch
# never shadows an up-to-date remote one: a local `submitted` left 120 commits
# behind predates .nav.yml and would otherwise be picked over origin/submitted.
resolve_content_ref() {
  local want="$1" r first_existing=""
  for r in "$want" "origin/$want" "public/$want" "upstream/$want"; do
    if git -C "$REPO" cat-file -e "$r:docs/fcaf/.nav.yml" 2>/dev/null; then
      echo "$r"; return 0
    fi
    if [ -z "$first_existing" ] && git -C "$REPO" rev-parse -q --verify "$r^{commit}" >/dev/null 2>&1; then
      first_existing="$r"
    fi
  done
  if [ -n "$first_existing" ]; then echo "$first_existing"; return 2; fi
  return 1
}

# A ref that exists is not necessarily renderable: hooks/fcaf_nav.py requires
# docs/fcaf/.nav.yml, which today only `submitted` has. Say which of the two
# went wrong rather than reporting everything as "not found".
assert_renderable_ref() {
  local r="$1" asked="$2"
  git -C "$REPO" cat-file -e "$r:docs/fcaf/.nav.yml" 2>/dev/null && return 0
  echo "Ref '$asked' (resolved to '$r') has no docs/fcaf/.nav.yml, so it cannot be rendered." >&2
  if git -C "$REPO" cat-file -e "$r:docs/fcaf" 2>/dev/null; then
    echo "It does have docs/fcaf, but without .nav.yml the navigation hook refuses to build." >&2
  else
    echo "It has no docs/fcaf at all. Is it a content branch?" >&2
  fi
  exit 1
}

CONTENT_MODE="" CONTENT_SRC=""
if [ -n "$CONTENT" ] && [ -d "$CONTENT" ]; then
  CONTENT_MODE="path"; CONTENT_SRC="$(cd "$CONTENT" && pwd)"
elif [ -n "$CONTENT" ]; then
  set +e; CONTENT_SRC="$(resolve_content_ref "$CONTENT")"; rc=$?; set -e
  case "$rc" in
    0) : ;;
    2) assert_renderable_ref "$CONTENT_SRC" "$CONTENT" ;;   # exits, with the precise reason
    *) echo "Content ref '$CONTENT' not found, and it is not a directory." >&2
       echo "Tried: $CONTENT, origin/$CONTENT, public/$CONTENT, upstream/$CONTENT" >&2
       echo "Fetch it first, e.g.:  git fetch origin $CONTENT" >&2
       exit 1 ;;
  esac
  CONTENT_MODE="ref"
elif [ -d "$REPO/docs/fcaf" ]; then
  CONTENT_MODE="path"; CONTENT_SRC="$REPO"
else
  set +e; CONTENT_SRC="$(resolve_content_ref submitted)"; rc=$?; set -e
  case "$rc" in
    0) : ;;
    2) assert_renderable_ref "$CONTENT_SRC" submitted ;;
    *) echo "No docs/fcaf in this working tree and no 'submitted' ref found." >&2
       echo "Fetch it first, e.g.:  git fetch origin submitted" >&2
       exit 1 ;;
  esac
  CONTENT_MODE="ref"
fi

if [ "$CONTENT_MODE" = "path" ] && [ ! -d "$CONTENT_SRC/docs/fcaf" ]; then
  echo "No docs/fcaf under: $CONTENT_SRC" >&2; exit 1
fi

# --- compose ----------------------------------------------------------------
WORK="$(mktemp -d "${TMPDIR:-/tmp}/fcaf-preview.XXXXXX")"
cleanup() { rm -rf "$WORK"; }
trap cleanup EXIT INT TERM

echo "shell:   $SHELL_SRC ($SHELL_MODE)"
echo "content: $CONTENT_SRC ($CONTENT_MODE)"
echo "compose: $WORK"

WATCH=()

if [ "$SHELL_MODE" = "path" ]; then
  # mkdocs.yml is copied, not symlinked: it resolves docs_dir and hooks relative
  # to the config's real path, so a symlink would point mkdocs back at the
  # source tree and defeat the composition. Everything else is symlinked so
  # edits to CSS, hooks and overrides are picked up live.
  cp "$SHELL_SRC/mkdocs.yml" "$WORK/mkdocs.yml"
  [ -f "$SHELL_SRC/requirements.txt" ] && cp "$SHELL_SRC/requirements.txt" "$WORK/requirements.txt"
  for d in hooks overrides pandoc; do
    [ -e "$SHELL_SRC/$d" ] && ln -s "$SHELL_SRC/$d" "$WORK/$d"
  done
  mkdir -p "$WORK/docs"
  for entry in "$SHELL_SRC"/docs/*; do
    [ -e "$entry" ] || continue
    [ "$(basename "$entry")" = "fcaf" ] && continue   # content half, handled below
    ln -s "$entry" "$WORK/docs/$(basename "$entry")"
  done
  WATCH+=(--watch "$SHELL_SRC/docs")
  [ -d "$SHELL_SRC/hooks" ]     && WATCH+=(--watch "$SHELL_SRC/hooks")
  [ -d "$SHELL_SRC/overrides" ] && WATCH+=(--watch "$SHELL_SRC/overrides")
else
  git -C "$REPO" archive --format=tar "$SHELL_SRC" | tar -xf - -C "$WORK"
  rm -rf "$WORK/docs/fcaf"   # a shell ref must not carry content, but be sure
fi

if [ "$CONTENT_MODE" = "path" ]; then
  # Symlink rather than copy so edits are picked up with no re-run. mkdocs does
  # not watch through symlinks, so also watch the real directory explicitly.
  rm -rf "$WORK/docs/fcaf"
  ln -s "$CONTENT_SRC/docs/fcaf" "$WORK/docs/fcaf"
  WATCH+=(--watch "$CONTENT_SRC/docs/fcaf")
else
  git -C "$REPO" archive --format=tar "$CONTENT_SRC" docs/fcaf | tar -xf - -C "$WORK"
fi

test -f "$WORK/mkdocs.yml"        || { echo "composed tree has no mkdocs.yml" >&2; exit 1; }
test -f "$WORK/docs/fcaf/.nav.yml" || { echo "composed tree has no docs/fcaf/.nav.yml" >&2; exit 1; }

# --- python environment -----------------------------------------------------
# Reuse the caller's .venv when it already has mkdocs, otherwise build one in
# the temp tree. Reusing keeps the common case fast.
MKDOCS=""
if [ -x "$REPO/.venv/bin/mkdocs" ]; then
  MKDOCS="$REPO/.venv/bin/mkdocs"
else
  echo "no .venv/bin/mkdocs in $REPO, creating a throwaway environment"
  python3 -m venv "$WORK/.venv"
  "$WORK/.venv/bin/pip" install -q --upgrade pip
  "$WORK/.venv/bin/pip" install -q -r "$WORK/requirements.txt"
  MKDOCS="$WORK/.venv/bin/mkdocs"
fi

# --- run --------------------------------------------------------------------
# Tell hooks/fcaf_edit_urls.py which ref the content came from, so the edit and
# view-source buttons point at the branch that actually holds these pages. For a
# working-tree preview there is no ref to name, so fall back to the hook's own
# default rather than inventing one.
if [ "$CONTENT_MODE" = "ref" ]; then
  export FCAF_CONTENT_REF="${CONTENT_SRC##*/}"
fi

# Deliberately not exec: the EXIT trap has to fire so the temp tree is removed
# on Ctrl-C as well.
cd "$WORK"
if [ "$ACTION" = "build" ]; then
  OUT="$REPO/build/preview-site"   # build/ is gitignored
  rm -rf "$OUT"                    # never let stale output look like success
  mkdir -p "$(dirname "$OUT")"
  "$MKDOCS" build --site-dir "$OUT"
  echo "built: $OUT"
else
  echo "serving on http://$ADDR/  (Ctrl-C to stop)"
  "$MKDOCS" serve --dev-addr "$ADDR" "${WATCH[@]}"
fi
