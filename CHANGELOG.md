# Changelog

This is the **framework & site** changelog: build/CI, MkDocs configuration, styling, templates,
governance and other scaffolding outside `docs/fcaf/`.

Test-case content is tracked separately, in a changelog **per maturity stage**. Each one lives on
its own branch, because `site` carries no `docs/fcaf`:

- [`submitted`](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/submitted/docs/fcaf/CHANGELOG.md) - rolling latest draft
- [`reviewed`](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/reviewed/docs/fcaf/CHANGELOG.md) - beta
- [`rc`](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/rc/docs/fcaf/CHANGELOG.md) - release candidate
- [`main`](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/main/docs/fcaf/CHANGELOG.md) - released baseline

Unversioned, newest first. Release versioning lives only in the FCAF changelog.

- Check that protocol and data element identifiers are written in backticks rather than in quotes or bare, recognised by shape with test case identifiers excluded, and repair the quoted ones under `--fix`.
- Promote the test case checks whose backlog is cleared to blocking: section order and names, defaults resolution, final newline, invisible characters and indentation tabs.
- Add a structural guard for test cases (`tools/fcaf_lint.py`) and the reusable workflow that runs it on pull requests touching `docs/fcaf`. Enforcement is staged: a check blocks only once its backlog is cleared, everything else is reported as a counted warning.
- Build the PDF from the content-owned FCAF navigation and render numbered Preconditions with alphabetic markers on the website and in the PDF.
- Fix mermaid diagram rendering on the deployed (mike) site: load the runtime from a self-hosted, page-relative script so it resolves under every version alias, instead of Material's built-in loader whose absolute URL 404s under versioned paths.
- Point both the `latest` and `latest-draft` site aliases at the submitted draft.
- Switch the Architecture and reference framework nav link to the ARF `/about/` page, for coherence with the ARF deployment.
- Streamline this framework (non-FCAF) changelog: drop versioning, keep a flat newest-first list.
- Adopt the shared EUDI Wallet documentation theme.
- Clean up the test-suite navigation so it no longer lists every test case and its sub-headings.
- Render aggregated test cases as separate, legible cards.
- Render Preconditions as an A./B./C. list; minor list and backtick formatting fixes.
- Fix PDF generation of `include-markdown` content and ICS table rendering.
- Update roadmap, governance model and issue templates.
- Embed functional conformance into eudi.dev.
- Align terminology for EUDI actors with the Regulation.
- Add the EUDI relevancy section to the test template.
- Fix CI release and PDF/website generation workflows.
- Initial version.
