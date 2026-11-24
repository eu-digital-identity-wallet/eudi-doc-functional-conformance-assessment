# FCAF changelog

Changes to the FCAF test-case content under `docs/fcaf/`. Framework and site changes (build,
MkDocs configuration, styling, templates) are kept separately in the
[framework changelog](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/site/CHANGELOG.md).

This file is stage-specific: each maturity stage keeps its own copy on its branch and records what
is in that stage, newest first. The heading follows that stage's versioning - `submitted` is the
rolling latest draft (untagged), while `reviewed`, `rc` and `main` group entries under their beta,
release-candidate and released version tags.

## [Latest draft]

- Add thirteen Attestation Provider (WS_AP) test cases on how a Wallet verifies the integrity of an issued SD-JWT VC (`WS_AP_SM_IssuerIntegrity`): the Issuer signature (missing, incorrect, correct), the certificate chain in the `x5c` header (invalid chain, invalid end-entity certificate, self-signed certificate), the JWT VC Issuer Metadata issuer signature mechanism (incorrect signature, no key in the metadata, a `jwks_uri` whose JWK Set lacks the signing key, metadata that cannot be retrieved), a Disclosure without a matching digest, and the SHA-256 digest algorithm, stated in `_sd_alg` or applied by default. Adds to the defaults how a default credential carries its certificate chain (`x5c` for SD-JWT VC, `x5chain` for mdoc).
- Add fourteen Attestation Provider (WS_AP) test cases on how a Wallet processes an issued SD-JWT VC (`WS_AP_MS_Metadata`): the `typ` header and the `vct` claim, the claims that must not be selectively disclosable (`iss`, `nbf`, `exp`, `cnf`, `vct`, `vct#integrity`, `status`), the JWT VC Issuer Metadata issuer signature mechanism (keys referenced through `jwks_uri`, no valid key in the metadata, an `issuer` value that does not match `iss`), and retrieval of SD-JWT VC Type Metadata from the `vct` URL. Adds `default_jwt_vc_issuer_metadata_B` to the defaults.
- Add examples to the page on using the FCAF that show how the Implementation Conformance Statement (ICS) and `Profile applicability` relate: a test case without a restriction, a test case with one statement that repeats its ICS item word for word, and a test case with several statements. The profile line of `WS_RP_IA_ProtocolFlow__002b` and `WS_RP_IA_ProtocolFlow__002e_UF` now quotes ICS item P.2.
- Add ten Attestation Provider (WS_AP) test cases on how a Wallet retrieves SD-JWT VC metadata (`WS_AP_IA_MetadataExchange`): JWT VC Issuer Metadata from the well-known location, SD-JWT VC Type Metadata caching under `Cache-Control`, the `extends` chain, and alternative retrieval methods.
- Add nine Attestation Provider (WS_AP) test cases for SD-JWT VC credentials: three on the claim classes an issued credential may carry (`WS_AP_UC_Provisioning`) and six on SD-JWT VC Type Metadata retrieved from the `vct` URL (`WS_AP_MS_CredentialMetadata_TypeMetadata`). Adds `default_credential_E`, `default_credential_F` and the default metadata documents to the defaults, and the `[RFC2397]` entry to the reference catalogue.
- Add the shared JSON, JWS and JWE test cases under `suts/shared`: eleven building blocks that the baseline test cases invoke as a family (`Shared_JSON`, `Shared_JWT_JWS`, `Shared_JWT_JWE`). They are documented in the framework index as an exception to the test case ID convention, linked from both baseline-tests pages, and the `[RFC4648]` and `[RFC8259]` catalogue rows are added.
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
