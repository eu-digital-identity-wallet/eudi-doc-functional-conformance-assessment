# WS_AP_MS_Metadata_009

## Objective

When processing an issued SD-JWT VC, verify that the wallet accepts an SD-JWT VC with a `typ` header value of `dc+sd-jwt`.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] section 3.2.1

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with a `typ` header value of `dc+sd-jwt`.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
