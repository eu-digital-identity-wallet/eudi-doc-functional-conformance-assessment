# WS_AP_SM_IssuerIntegrity_010

## Objective

When a SD-JWT VC credential is provisioned by an Issuer publishing JWT VC Issuer Metadata, if the response to the JWT VC Issuer Metadata request is not a 200 HTTP status code, verify the credential is rejected by the wallet and the credential is not made available for use.

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

1. Issuer A issues `default_credential_F` to the wallet; the well-known location derived from the `iss` value answers the request for the JWT VC Issuer Metadata with the HTTP status code `204` and no content.
2. Verify the wallet's JWT VC Issuer Metadata request.

## Expected results

1. The wallet sent an HTTP `GET` request for the JWT VC Issuer Metadata to the well-known location derived from the `iss` value.
2. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
