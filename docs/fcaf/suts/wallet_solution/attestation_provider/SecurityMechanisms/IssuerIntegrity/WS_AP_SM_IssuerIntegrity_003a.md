# WS_AP_SM_IssuerIntegrity_003a

## Objective

When an SD-JWT VC using X509 Certificate Issuer Signature Mechanism is provisioned to a wallet, if the SD-JWT VC issuer signature is correct, the SD-JWT VC is accepted by the wallet and the credential is made available for use.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] sections 3.4 and 3.5
- [HAIP] section 6.1.1

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet, signed with the `ES256` algorithm.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
