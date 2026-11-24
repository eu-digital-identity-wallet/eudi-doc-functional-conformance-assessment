# WS_AP_SM_IssuerIntegrity_001

## Objective

When a SD-JWT VC credential is provisioned, if the JWS Signature is not present in the SD-JWT VC, verify the SD-JWT VC is rejected by the wallet and the credential is not made available for use.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] section 3.4
- [RFC9901] sections 4.1, 7.1 and 7.2

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with the `alg` header value `none` and an empty signature.

## Expected results

1. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
