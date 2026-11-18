# WS_AP_IA_MetadataExchange_001

## Objective

When JWT VC Issuer Metadata is used for key resolution, verify that the wallet retrieves the metadata from the correct well-known URI derived from the `iss` claim.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.5, 5 and 5.1

## Profile applicability

Wallet supports the JWT VC Issuer Metadata issuer signature mechanism.

## EUDI-wallet relevancy

EUDI_generic | EUDI_undefined

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_F` to the wallet with an `iss` claim that is an HTTPS URL with a path component (for example `https://example.com/tenant/1234`); Issuer A serves `default_jwt_vc_issuer_metadata_A` at the well-known location derived from the `iss` value.
2. Verify the wallet's JWT VC Issuer Metadata request.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
2. The wallet sent one HTTP request for the JWT VC Issuer Metadata:
    1. the method is `GET`;
    2. the request URL is `https://example.com/.well-known/jwt-vc-issuer/tenant/1234`.
