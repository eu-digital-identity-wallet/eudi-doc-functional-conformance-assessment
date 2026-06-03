# Changelog

This is the **framework & site** changelog - build/CI, MkDocs configuration, styling, templates,
governance and other scaffolding outside `docs/fcaf/`. Changes to the **test-case content** itself
are tracked in the FCAF changelog ([`docs/fcaf/CHANGELOG.md`](docs/fcaf/CHANGELOG.md)), per maturity stage.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semverdoc.org/).

## [Unreleased]
- Improve rendering of test cases on the documentation site: each aggregated test case is now
  shown as a separated card with legible section labels (Objective, References, …).
- Fix PDF generation by expanding MkDocs `include-markdown` directives before passing content to
  Pandoc, preventing raw include placeholders from appearing in generated PDFs.
- Improve PDF rendering of dense ICS tables by applying PDF-specific column widths and compact table styling for ICS tables.

## [0.0.1]
- Initial version.

## [0.0.2]
- Corrected timeline for public facing website.

## [0.0.3]
- Fixed PDF and website generation workflows.
- Minor editorial changes

## [0.0.4]
- Fix PDF and website generation workflows.

## [0.0.5]
- Fix github workflow to allow immutable releases.
- Disable workflow dispatcher in github workflow.

## [0.0.6]
- Update roadmap
- Minor editorial changes
- Add EUDI relevancy section to template

## [0.0.7]
- Aligned terminology for EUDI actors with Regulation
- Minor editorial changes

## [0.0.8]
- Aligned terminology for EUDI actors with Regulation
- Minor editorial changes

## [0.0.9]
- Changed title of main nav bar to be embedded into eudi.dev

## [0.0.10]
- Embed fucntional conformance into eudi.dev

## [0.1.0]
- Update roadmap to reflect iterative process model
- Update governance model
- Add issue templates
