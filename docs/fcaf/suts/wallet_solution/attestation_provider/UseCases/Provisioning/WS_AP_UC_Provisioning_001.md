# WS_AP_UC_Provisioning_001

## Objective

When an SD-JWT VC contains registered JWT claims and private claims, verify that the wallet accepts the issued SD-JWT VC.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1
- [SD-JWT VC] sections 3.2.2.2 and 3.2.2.3
- [RFC7519] section 4
- [RFC7519] sections 4.1 and 4.3

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet.

## Expected results

1. The SD-JWT VC is accepted and is made available for use.
