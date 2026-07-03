# Changelog

This is the **framework & site** changelog: build/CI, MkDocs configuration, styling, templates,
governance and other scaffolding outside `docs/fcaf/`. Test-case content is tracked separately in
the FCAF changelog ([`docs/fcaf/CHANGELOG.md`](docs/fcaf/CHANGELOG.md)).

Unversioned, newest first. Release versioning lives only in the FCAF changelog.

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
