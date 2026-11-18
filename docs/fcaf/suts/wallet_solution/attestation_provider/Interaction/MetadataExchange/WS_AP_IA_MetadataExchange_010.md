# WS_AP_IA_MetadataExchange_010

## Objective

When Type Metadata has been pre-populated in the wallet's local cache before credential use, verify that the wallet accepts a subsequently issued SD-JWT VC referencing that type without requiring a live metadata fetch.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02, EAA-5.2.1.2-03
- [SD-JWT VC] section 6.3.4
- [SD-JWT VC] section 10.4

## Profile applicability

Wallet supports retrieval of SD-JWT VC Type Metadata from a local cache.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.
2. Issuer A has issued `default_credential_E` to the wallet, and the wallet has retrieved `default_type_metadata_A` from its `vct` URL; the Credential's `vct#integrity` lets the wallet keep the document indefinitely.
3. The `vct` URL is unreachable for the duration of the test.

## Test Scenario

1. Issuer A issues a second `default_credential_E` to the wallet.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
