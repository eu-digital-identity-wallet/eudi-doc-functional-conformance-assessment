# WS_AP_SM_IssuerIntegrity_002

## Objective

When an SD-JWT VC using a JWT VC Issuer Metadata Issuer Signature Mechanism is provisioned to a wallet, if the SD-JWT VC issuer signature is incorrect, the SD-JWT VC is rejected by the wallet and the credential is not made available for use.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.4, 3.5 and 5.2
- [RFC9901] sections 7.1 and 7.2

## Profile applicability

Wallet supports the JWT VC Issuer Metadata issuer signature mechanism.

## EUDI-wallet relevancy

EUDI_generic | EUDI_undefined

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_F` to the wallet with a signature of the Issuer-signed JWT that does not verify with the key in `default_jwt_vc_issuer_metadata_A`; Issuer A serves `default_jwt_vc_issuer_metadata_A` at the well-known location derived from the `iss` value.

## Expected results

1. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
