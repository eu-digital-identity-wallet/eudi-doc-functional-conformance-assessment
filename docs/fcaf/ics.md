# EUDI-wallet Implementation Conformity Statement (ICS)

This is the general Implementation Conformity Statement (ICS) form for EUDI-Wallet
implementations under test. Before testing starts, the implementer completes the `value`
column to declare the capabilities and profiles the implementation under test supports. It
follows the same approach as the ICS of ISO/IEC TS 18013-6:2025 (Annex B), which the FCAF
already applies to ISO mdoc proximity presentation in
[Testing ISO mdoc presentation](suts/wallet_solution/relying_party/testsuite_isomdoc.md):
numbered capability statements, a value column for the implementer, and an EUDI-wallet
column stating the constraint the EUDI framework imposes on the answer.

How this ICS is used in conformance assessment:

- Each test case states its capability/profile conditions in `## Profile applicability`.
  Test selection compares those conditions with the answers declared in this ICS: a test
  case is selected when the declared capabilities satisfy its conditions. A test case
  whose `Profile applicability` is `None` applies to all implementations and needs no
  ICS entry.
- The EUDI-wallet column states the constraint that the European Digital Identity
  framework (Regulation (EU) No 910/2014 and its Implementing Regulations, including the
  standards they make binding) imposes on the declared value, with the source of the
  constraint. Options struck through are prohibited for EUDI-Wallets; `Yes/~~No~~` marks
  capabilities every EUDI-Wallet must declare.
- `TBD` means the EUDI constraint has not yet been established from the authoritative
  texts; treat the capability as unconstrained for test selection until the constraint
  is confirmed.

The ISO mdoc proximity capabilities (device engagement, device retrieval, session
encryption curves, reader authentication) are declared in the
[ISO mdoc ICS](suts/wallet_solution/relying_party/testsuite_isomdoc.md) and are not
repeated here.

Note that this list is non-exhaustive. It only covers items for which test coverage has been defined in the FCAF.

Items listed with ID "N/A" are surrogate ICS items. They are mandatory to implement for EUDI-wallets. These items can be used to select relevant test cases using the Technology section.

## Generic

| ID | ICS item | Options | EUDI-wallet specifics |
| --- | --- | --- | --- |
| N/A | Wallet supports credentials in IETF SD-JWT VC format. | Yes/~~No~~ | EUDI\_required; [EU CIR 2024/2979] Article 8 with Annex II ([ETSI TS 119 472-1] clause 5): wallet solutions shall support the usage of PID and EAAs issued in compliance with the listed standards, which include the SD-JWT VC format. |
| N/A | Wallet supports credentials in ISO/IEC 18013-5 mdoc format. | Yes/~~No~~ | EUDI\_required; [EU CIR 2024/2979] Article 8 with Annex II ([ETSI TS 119 472-1] clause 6, ISO/IEC-mdoc format); for presentation additionally [EU CIR 2024/2982] Annex II ([ETSI TS 119 472-2] clause 5.2, ISO/IEC 18013-SUPPORT-02: the EUDI Wallet shall meet the ISO/IEC-mdoc profile protocol requirements). |
| N/A | Wallet supports credential with key-binding | Yes/No | TBD |
| N/A | Wallet supports credential without key-binding | Yes/No | TBD |
| N/A | Wallet supports credential with revocation status information | Yes/No | TBD |
| N/A | Issuer uses compact serialization of SD-JWT and SD-JWT VC | Yes/No | TBD |
| N/A | Issuer uses JWS JSON serialization of SD-JWT and SD-JWT VC | Yes/No | TBD |

## Presentation related

| ID | ICS item | Options | EUDI-wallet specifics |
| --- | --- | --- | --- |
| N/A | Wallet supports invocation through the custom URL scheme `eu-eaap://`. | Yes/~~No~~ | EUDI\_required; [ETSI TS 119 472-2] clause 6.4.1 (OIDFVP-HAIP-REDIRECTS-03), IA-bound via [EU CIR 2024/2982] Annex II. |
| P.1 | Wallet supports invocation through the custom URL scheme `haip-vp://`. | Yes/No |
| N/A | Wallet supports remote presentations using OpenID4VP (as profiled by HAIP and ETSI TS 119 472-2). | Yes/~~No~~ | EUDI\_required; [ETSI TS 119 472-2] clause 6.2 (OIDFVP-HAIP-SUPPORT-01), IA-bound via [EU CIR 2024/2982] Annex II. |
| N/A | Wallet supports presentations via redirects (non-API mediated). | Yes/~~No~~ | EUDI\_required; [ETSI TS 119 472-2] clauses 6.2 and 6.4, IA-bound via [EU CIR 2024/2982] Annex II. |
| N/A | Wallet supports the same-device presentation flow. | Yes/~~No~~ | EUDI\_required; [HAIP] clause 5.1, applied through [ETSI TS 119 472-2] clause 6.4.1 (OIDFVP-HAIP-REDIRECTS-01), requires Wallets to support the same-device flow. |
| N/A | Wallet supports cross-device presentation flows. | Yes/No | EUDI\_optional; [EU CIR 2024/2982] Annex II, clause 6.2 (OIDFVP-HAIP-SUPPORT-03) says the Wallet should not support the redirects-based mechanism for cross-device flows, but its Note 3 states that implementing this mechanism should not trigger non-compliance. |
| N/A | Wallet supports presentations via the W3C Digital Credentials API (or equivalent platform API). | Yes/~~No~~ | EUDI\_required; [EU CIR 2024/2982] Annex II, clause 4.3 (EAAP-API-GEN-01), requires a mediating API supporting both the HAIP 5.2 protocol and ISO/IEC 18013-7 Annex C. Failures caused by missing OS/browser support are non-conformities attributed to the platform (NOTE to EAAP-API-GEN-01). |
| P.2 | Wallet supports the Request URI Method `post`. | Yes/No | TBD |
| N/A | Wallet supports `response_mode=direct_post.jwt` (encrypted authorization responses). | Yes/~~No~~ | EUDI\_required for redirects; [HAIP] clause 5.1 requires `direct_post.jwt`, applied through [ETSI TS 119 472-2] clause 6.4.1 (OIDFVP-HAIP-REDIRECTS-01) and [EU CIR 2024/2982] Annex II. |


## Issuance Related

| ID | ICS item | Options | EUDI-wallet specifics |
| --- | --- | --- | --- |
| I.1 | Wallet supports invocation through custom URL scheme `haip-vci://`. | Yes/No |
| I.2 | Wallet uses a `jwt` Proof Type for Authentication to Credential Issuers. | Yes/No | TBD |
| I.3 | Wallet uses an `attestation` Proof Type for Authentication to Credential Issuers. | Yes/No | TBD |
| N/A | Wallet supports the Issuer initiated issuance flow. | Yes/~~No~~ | TODO |
| N/A | Wallet supports revocation checking via the Token Status List mechanism. | Yes/No | TBD |
| N/A | Wallet supports Credential Issuance using the Authorization Code Flow. | Yes/~~No~~ | EUDI\_required; [EU CIR 2024/2982] Annex I applies [ETSI TS 119 472-3] clause 4.1 (GEN-REQ-4.1-03). |
| N/A | Wallet supports Credential Issuance using the Pre-Authorization Code Flow. | Yes/~~No~~ | EUDI\_required; [EU CIR 2024/2982] Annex I applies [ETSI TS 119 472-3] clause 4.1 (GEN-REQ-4.1-03). |
