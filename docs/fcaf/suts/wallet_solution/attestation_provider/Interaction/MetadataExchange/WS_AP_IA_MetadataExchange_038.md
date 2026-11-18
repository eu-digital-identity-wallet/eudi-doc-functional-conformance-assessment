# WS_AP_IA_MetadataExchange_038

## Objective

When the wallet neither retrieves SD-JWT VC Type Metadata from the `vct` URL nor supports an alternative retrieval method, verify that the wallet accepts the SD-JWT VC without retrieving its Type Metadata from the `vct` URL.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02
- [SD-JWT VC] section 6.3.1
- [SD-JWT VC] section 12.1

## Profile applicability

Wallet does not retrieve SD-JWT VC Type Metadata from the URL in the vct claim.
Wallet does not support an alternative method for retrieving SD-JWT VC Type Metadata.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.
2. The `vct` URL of `default_credential_E` is reachable and serves `default_type_metadata_A` for the duration of the test.

## Test Scenario

1. Issuer A issues `default_credential_E` to the wallet.
2. Verify the wallet's Type Metadata requests.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
2. The wallet sent no HTTP request to the `vct` URL.

## Comments

- Retrieving Type Metadata is a MAY in [SD-JWT VC] section 6.3.1, and no EUDI layer requires the Wallet to retrieve it, so a Wallet that does not retrieve Type Metadata is expected to accept the SD-JWT VC.
