"""MkDocs hook: render numbered test-case Preconditions alphabetically.

Preconditions are authored as ordinary numbered Markdown lists. This hook tags
only the ordered list directly following a Preconditions heading with the
``precond-alpha`` class so CSS displays A., B., C., and so on.

Only the Preconditions list is affected; Test Scenario and Expected results stay
numeric.
"""
import re

# A "Preconditions" heading (any level), optional include-markdown comment markers,
# then the start of the ordered list. The list must not already carry a class.
_PRECOND_OL = re.compile(
    r'(<h([1-6])[^>]*>\s*Preconditions\b(?:(?!</h[1-6]>).)*</h\2>\s*'
    r'(?:<!--.*?-->\s*)*)'
    r'<ol(?![^>]*\bclass=)',
    re.IGNORECASE | re.DOTALL,
)

def on_page_content(html, page=None, config=None, files=None, **kwargs):
    return _PRECOND_OL.sub(r'\1<ol class="precond-alpha"', html)
