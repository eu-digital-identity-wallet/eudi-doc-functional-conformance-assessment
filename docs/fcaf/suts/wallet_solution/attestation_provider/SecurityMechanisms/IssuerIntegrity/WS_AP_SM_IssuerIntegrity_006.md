# WS_AP_SM_IssuerIntegrity_006

## Objective

When an SD-JWT VC using a JWT VC Issuer Metadata Issuer Signature Mechanism is provisioned to a wallet, if the value of the iss claim is an HTTPS URI but neither jwks nor jwks_uri Issuer Metadata configuration parameters are returned, verify that the wallet rejects the credential.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.5, 5.1 and 5.2

## Profile applicability

Wallet supports the JWT VC Issuer Metadata issuer signature mechanism.

## EUDI-wallet relevancy

EUDI_generic | EUDI_undefined

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_F` to the wallet with an `iss` claim that is an HTTPS URL; Issuer A serves `default_jwt_vc_issuer_metadata_A` at the well-known location derived from the `iss` value, without the `jwks` member and without a `jwks_uri` member.
2. Verify the wallet's JWT VC Issuer Metadata request.

## Expected results

1. The wallet sent an HTTP `GET` request for the JWT VC Issuer Metadata to the well-known location derived from the `iss` value.
2. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
