# WS_AP_MS_Metadata_021

## Objective

When processing an issued SD-JWT VC using the JWT VC Issuer Metadata Issuer Signature Mechanism, verify that the wallet rejects the SD-JWT VC if the Issuer Metadata does not provide a valid public key for signature validation.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.4, 3.5, 5.1 and 5.2

## Profile applicability

Wallet supports the JWT VC Issuer Metadata issuer signature mechanism.

## EUDI-wallet relevancy

EUDI_generic | EUDI_undefined

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_F` to the wallet with an `iss` claim that is an HTTPS URL with host, port number and path components; Issuer A serves `default_jwt_vc_issuer_metadata_A` at the well-known location derived from the `iss` value, with a `jwks` that does not contain the key that signed the Credential.
2. Verify the wallet's JWT VC Issuer Metadata request.

## Expected results

1. The wallet sent an HTTP `GET` request for the JWT VC Issuer Metadata to the location formed by inserting `/.well-known/jwt-vc-issuer` between the host component and the path component of the `iss` value.
2. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
