# WS_AP_SM_IssuerIntegrity_013

## Objective

When a SD-JWT VC credential is issued using the X.509 Certificate Issuer Signature Mechanism, if the signing X.509 certificate in `x5c` is self-signed, verify that the wallet rejects the credential.

## References

- [CIR 2024/2982 amended] Article 4(3)(d)
- [CIR 2024/2979 amended] Article 8, Annex II
- [ETSI TS 119 472-1] clause 5.1 EAA-5.1-01
- [SD-JWT VC] section 3.5
- [RFC7515] section 4.1.6
- [HAIP] section 6.1.1

## Profile applicability

None

## EUDI-wallet relevancy

EUDI_generic | EUDI_required

## Technology

Credential in SD-JWT VC format

## Preconditions

1. Wallet is set to `default_configuration_1`.

## Test Scenario

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with an `x5c` header that contains one self-signed certificate, which is not a trust anchor of the wallet, and with a signature of the Issuer-signed JWT that verifies with the public key of that certificate.

## Expected results

1. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
