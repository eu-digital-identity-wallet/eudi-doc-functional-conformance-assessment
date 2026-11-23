# WS_AP_MS_Metadata_020

## Objective

When processing an issued SD-JWT VC using the JWT VC Issuer Metadata Issuer Signature Mechanism and the JWT VC Issuer Metadata references the issuer's keys through `jwks_uri`, verify that the wallet retrieves the JWK Set from the `jwks_uri` and accepts the SD-JWT VC.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.4, 3.5, 5, 5.1 and 5.2

## Profile applicability

Wallet supports the JWT VC Issuer Metadata issuer signature mechanism.

## EUDI-wallet relevancy

EUDI_generic | EUDI_undefined

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_F` to the wallet; Issuer A serves `default_jwt_vc_issuer_metadata_B` at the well-known location derived from the `iss` value, and the JWK Set at the `jwks_uri` it contains.
2. Verify the wallet's JWT VC Issuer Metadata and JWK Set requests.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
2. The wallet sent two HTTP `GET` requests, in this order:
    1. to the well-known location derived from the `iss` value, receiving `default_jwt_vc_issuer_metadata_B`;
    2. to the `jwks_uri` in `default_jwt_vc_issuer_metadata_B`, receiving the JWK Set.
