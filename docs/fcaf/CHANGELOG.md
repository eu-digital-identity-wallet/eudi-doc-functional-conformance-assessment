# Test-case changelog

Changes to the **test-case content** under `docs/fcaf/`. This is **stage-specific**: each maturity
stage (`submitted`, `reviewed`, `rc`, `main`) keeps its own copy of this file, recording what
entered *that* stage — so the entries differ per branch.

Framework & site changes (build, MkDocs config, styling, templates, …) are tracked separately in
the [framework changelog](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/blob/main/CHANGELOG.md).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## submitted

### Added
- Relying Party (`WS_RP`) test cases for **OpenID4VP** sections 5–8 (Authorization Request, DCQL,
  claims path pointer, Response).
- **Token Status List (TSL)** test cases (section 6).
- PID **data-model** test cases for ISO mdoc and IETF SD-JWT VC formats (**ISO/IEC 18013-5**).
