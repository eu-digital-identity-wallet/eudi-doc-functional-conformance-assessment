# WS_AP_SM_IssuerIntegrity_012

## Objective

When a SD-JWT VC credential is issued, if it does not explicitly specify the digest algorithm for selective disclosures but uses the default SHA-256 hash for selective disclosure hashes, verify the credential is accepted by the wallet and the credential is made available for use.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [RFC9901] section 4.1.1
- [HAIP] section 8

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with selectively disclosable claims, without an `_sd_alg` claim and with digests calculated with SHA-256.

## Expected results

1. The SD-JWT VC is accepted and made available for use.
