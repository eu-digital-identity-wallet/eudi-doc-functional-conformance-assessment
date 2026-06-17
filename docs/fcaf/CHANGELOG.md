# FCAF changelog

Changes to the FCAF test-case content under `docs/fcaf/`. Framework and site changes (build,
MkDocs configuration, styling, templates) are kept separately in the
[framework changelog](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/main/CHANGELOG.md).

This file is stage-specific: each maturity stage keeps its own copy on its branch and records what
is in that stage, newest first. The heading follows that stage's versioning - `submitted` is the
rolling latest draft (untagged), while `reviewed`, `rc` and `main` group entries under their beta,
release-candidate and released version tags.

## [Latest draft]

- Rendering and formatting pass across test cases (editorial only, no functional change): Preconditions now use one alphabetic list item (`A.`, `B.`, `C.`, ...) per line, separated by blank lines, so each item renders on its own line in MkDocs and PDF; nested bullet lists in the date-format Expected results are correctly indented under their parent step; and missing backticks were added around claim and data-element identifiers (for example `issuance_date`).
- Relying Party (WS_RP) test cases for OpenID4VP sections 5-8: Authorization Request, DCQL, claims path pointer, and Response.
- Token Status List (TSL) test cases (section 6).
- PID data-model test cases for ISO mdoc and IETF SD-JWT VC formats (ISO/IEC 18013-5).
- Relying Party (WS_RP) engagement test cases for the High Assurance Interoperability Profile (HAIP).
- Relying Party (WS_RP) Security Mechanisms test cases: RP authentication, trust, and session binding.
- PID data-model test cases for name-at-birth attributes (family name at birth, given name at birth) in ISO mdoc and IETF SD-JWT VC formats.
- Consistency pass across Relying Party (WS_RP) test cases: explicit `none` for empty Preconditions and Profile applicability, harmonised EUDI-wallet relevancy and Profile applicability formatting, standardised TODO markers, and Markdown formatting fixes.
- Citations aligned to canonical references; references catalogue updated with specification versions and entries for HAIP, Token Status List, ISO/IEC 18013-7, and the referenced RFCs.
