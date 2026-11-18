# WS_AP_IA_MetadataExchange_008

## Objective

When processing an SD-JWT VC whose Type Metadata extends a type that itself extends a third type, verify that the wallet retrieves the Type Metadata of both extended types referenced through the `extends` properties before accepting the SD-JWT VC.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02
- [SD-JWT VC] section 6.3.1
- [SD-JWT VC] section 6.4

## Profile applicability

Wallet retrieves SD-JWT VC Type Metadata from the URL in the vct claim.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues to the wallet a `default_credential_E` whose `vct` is the URL of `default_type_metadata_C` and whose `vct#integrity` matches that document.
2. Verify the wallet's Type Metadata requests.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
2. Before accepting the SD-JWT VC, the wallet sent three HTTP `GET` requests, in this order:
    1. to the `vct` URL, receiving `default_type_metadata_C`;
    2. to the URL in the `extends` property of `default_type_metadata_C`, receiving `default_type_metadata_B`;
    3. to the URL in the `extends` property of `default_type_metadata_B`, receiving `default_type_metadata_A`.
