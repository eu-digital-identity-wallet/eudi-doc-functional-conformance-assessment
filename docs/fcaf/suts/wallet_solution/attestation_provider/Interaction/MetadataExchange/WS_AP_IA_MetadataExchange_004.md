# WS_AP_IA_MetadataExchange_004

## Objective

When processing an SD-JWT VC and retrieving its Type Metadata, verify that the wallet retrieves the Type Metadata again for a second SD-JWT VC of the same type when the first response carried `Cache-Control: no-store`.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02, EAA-5.2.1.2-03
- [SD-JWT VC] section 6.3.4

## Profile applicability

Wallet supports retrieval of SD-JWT VC Type Metadata from a local cache.
Wallet retrieves SD-JWT VC Type Metadata from the URL in the vct claim.
Wallet applies the Cache-Control header to cached SD-JWT VC Type Metadata regardless of integrity protection.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_E` to the wallet; the Type Metadata endpoint serves `default_type_metadata_A` with the HTTP header `Cache-Control: no-store`.
2. Issuer A issues a second such Credential to the wallet; the endpoint responds in the same way.
3. Verify the wallet's Type Metadata requests.

## Expected results

1. The first SD-JWT VC is accepted and made available for use.
2. The second SD-JWT VC is accepted and made available for use.
3. The wallet sent an HTTP `GET` request to the `vct` URL for each of the two SD-JWT VCs.
