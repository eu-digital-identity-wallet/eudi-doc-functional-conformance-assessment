# WS_AP_UC_Provisioning_005

## Objective

When an SD-JWT VC contains a private claim whose value is a hash digest encoded in base64 rather than as a data URI, verify that the wallet accepts the issued SD-JWT VC.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1
- [SD-JWT VC] section 3.2.2.3
- [RFC2397]
- [RFC7519] section 4.3

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with one additional private claim whose value is a hash digest encoded in base64 and not as a data URI.

## Expected results

1. The SD-JWT VC is accepted and is made available for use.
