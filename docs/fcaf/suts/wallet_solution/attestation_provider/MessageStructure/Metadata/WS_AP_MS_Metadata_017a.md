# WS_AP_MS_Metadata_017a

## Objective

When processing an issued SD-JWT VC, verify that the wallet rejects an SD-JWT VC in which the `vct#integrity` claim is included in the Disclosures.

## References

- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.2.1.2 EAA-5.2.1.2-03
- [SD-JWT VC] sections 3.2.2.2 and 3.4
- [RFC9901] sections 7.1 and 7.2

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with its `vct#integrity` claim conveyed in a Disclosure instead of in the Issuer-signed JWT payload.

## Expected results

1. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
