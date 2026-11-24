# WS_AP_SM_IssuerIntegrity_005

## Objective

When an SD-JWT VC using X509 Certificate Issuer Signature Mechanism is provisioned to a wallet, if the protected header of the Issuer-signed JWT contains the `x5c` parameter with an invalid end-entity certificate and a credential signature created by the end-entity's key, verify the SD-JWT VC is rejected by the wallet and the credential is not made available for use.

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

1. Issuer A issues the SD-JWT VC variant of `default_credential_A` to the wallet with the protected header of the Issuer-signed JWT containing an `x5c` parameter with an invalid end-entity certificate: its signature does not verify with the public key of the CA certificate that issued it. The signature of the Issuer-signed JWT verifies with the public key of the end-entity certificate.

## Expected results

1. The Wallet does not store the Credential and does not make it available for use. The End-user is informed that the Credential was not accepted, if applicable.
