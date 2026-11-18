# WS_AP_IA_MetadataExchange_037

## Objective

When the wallet supports an alternative method for retrieving SD-JWT VC Type Metadata and the `vct` URL of an SD-JWT VC is unreachable, verify that the wallet accepts the SD-JWT VC.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02
- [SD-JWT VC] section 6.3.2
- [SD-JWT VC] section 6.3.3
- [SD-JWT VC] section 12.1

## Profile applicability

Wallet supports an alternative method for retrieving SD-JWT VC Type Metadata.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.
2. `default_type_metadata_A` is available to the wallet through its alternative retrieval method.
3. The `vct` URL of `default_credential_E` is unreachable for the duration of the test.

## Test Scenario

1. Issuer A issues `default_credential_E` to the wallet.

## Expected results

1. The SD-JWT VC is accepted and made available for use.

## Comments

An alternative method is any method of retrieving Type Metadata other than the `vct` URL, for example a registry ([SD-JWT VC] section 6.3.2) or a retrieval method defined for the type (section 6.3.3). Section 12.1 recommends methods that do not leak information about the usage of a credential to third parties.
