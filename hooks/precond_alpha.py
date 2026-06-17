"""MkDocs hook: render each test-case Preconditions list with alphabetic markers.

Preconditions are authored as an ordinary numbered Markdown list (1., 2., 3., ...)
so the raw Markdown stays clean and renders as a real list everywhere. On the
website this hook tags the ordered list that follows a "Preconditions" heading with
the ``precond-alpha`` class; ``docs/media/css/extra.css`` then displays it as
A., B., C., ... via ``list-style-type: upper-alpha``. The PDF build produces the
same effect with ``pandoc/filters/precond_alpha.lua``.

Only the Preconditions list is affected; Test Scenario and Expected results stay
numeric.
"""
import re

# A "Preconditions" heading (any level), optional include-markdown comment markers,
# then the start of the ordered list. The list must not already carry a class.
_PRECOND_OL = re.compile(
    r'(<h[1-6][^>]*>\s*Preconditions\s*</h[1-6]>\s*(?:<!--.*?-->\s*)*)'
    r'<ol(?![^>]*\bclass=)',
    re.IGNORECASE | re.DOTALL,
)


def on_page_content(html, page=None, config=None, files=None, **kwargs):
    return _PRECOND_OL.sub(r'\1<ol class="precond-alpha"', html)
