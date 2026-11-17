# WS_AP_MS_CredentialMetadata_TypeMetadata_003

## Objective

When an SD-JWT VC is provisioned and the SD-JWT VC Type Metadata does not contain a `display` property, verify that the SD-JWT VC is accepted.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2
- [SD-JWT VC] Section 6.2

## Profile applicability

Wallet retrieves SD-JWT VC Type Metadata from the URL in the vct claim.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_E` to the wallet.
2. The Type Metadata endpoint responds with:
  - HTTP status code `200`
  - `application/json` content type
  - `default_type_metadata_A`, without the `display` member.

## Expected results

1. The wallet sends an HTTP `GET` request to retrieve the Type Metadata from the `vct` URL.
2. The SD-JWT VC is accepted and is made available for use.
