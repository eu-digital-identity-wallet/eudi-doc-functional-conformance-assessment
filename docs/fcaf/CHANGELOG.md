# FCAF changelog

Changes to the FCAF test-case content under `docs/fcaf/`. Framework and site changes (build,
MkDocs configuration, styling, templates) are kept separately in the
[framework changelog](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/site/CHANGELOG.md).

This file is stage-specific: each maturity stage keeps its own copy on its branch and records what
is in that stage, newest first. The heading follows that stage's versioning - `submitted` is the
rolling latest draft (untagged), while `reviewed`, `rc` and `main` group entries under their beta,
release-candidate and released version tags.

## [Latest draft]

- Pin the versions the tests are written against: OpenID4VP 1.0 and OpenID4VCI 1.0 without errata, and SD-JWT VC draft-13.
- Add the missing `[ETSI TS 119 475]` entry to the reference catalogue, so the trust mechanism test cases that cite it resolve.
- Normalise the test case sources against the settled conventions: canonical section order, a single trailing newline, no invisible characters, and spaces instead of tabs for list indentation. No wording changes.
- Settle the test case conventions the format guard checks: sections follow one canonical order, default configurations are numbered and default credentials are lettered so the two cannot be confused, and the optional comment section is called `Comments` everywhere.
- Editorial and rendering cleanup across FCAF documentation and test specifications, including consistent Markdown lists and tables, baseline test pages, stable ICS selection wording, and canonical Implementing Regulation references.
- Added baseline test reference indexes and separate test-case hierarchy pages for the Relying Party and Attestation Provider interfaces.
- Rendering and formatting pass across test cases (editorial only, no functional change): actual Preconditions use compact numbered Markdown lists in the source and render with uppercase-alphabetic labels (A., B., C., ...) on the website and in the PDF, while Preconditions with no entries and Profile applicability with no restriction use the canonical value `None` without a list marker or trailing period; pre-existing sibling relationships in Expected results are preserved as flat numbered entries, nested results remain numbered under their parent step, nested bullet lists in the date-format Expected results are correctly indented under their parent step, and missing backticks were added around claim and data-element identifiers (for example `issuance_date`).
- Relying Party (WS_RP) test cases for OpenID4VP sections 5-8: Authorization Request, DCQL, claims path pointer, and Response.
- Token Status List (TSL) test cases (section 6).
- PID data-model test cases for ISO mdoc and IETF SD-JWT VC formats (ISO/IEC 18013-5).
- Relying Party (WS_RP) engagement test cases for the High Assurance Interoperability Profile (HAIP).
- Relying Party (WS_RP) Security Mechanisms test cases: RP authentication, trust, and session binding.
- PID data-model test cases for name-at-birth attributes (family name at birth, given name at birth) in ISO mdoc and IETF SD-JWT VC formats.
- Consistency pass across Relying Party (WS_RP) test cases: explicit `none` for empty Preconditions and Profile applicability, harmonised EUDI-wallet relevancy and Profile applicability formatting, standardised TODO markers, and Markdown formatting fixes.
- Citations aligned to canonical references; references catalogue updated with specification versions and entries for HAIP, Token Status List, ISO/IEC 18013-7, and the referenced RFCs.
