# WS_AP_MS_Metadata_026

## Objective

When processing an issued SD-JWT VC whose `vct` claim is a URL using the HTTPS scheme, verify that the wallet retrieves the Type Metadata from that URL.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-01, EAA-5.2.1.2-02
- [SD-JWT VC] section 6.3.1

## Profile applicability

Wallet retrieves SD-JWT VC Type Metadata from the URL in the vct claim.

## EUDI-wallet relevancy

EUDI_generic | EUDI_optional

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues `default_credential_E` to the wallet.
2. Verify the wallet's Type Metadata requests.

## Expected results

1. The wallet sent an HTTP `GET` request for the Type Metadata to the `vct` URL.
2. The wallet accepts the SD-JWT VC and makes it available for use.
