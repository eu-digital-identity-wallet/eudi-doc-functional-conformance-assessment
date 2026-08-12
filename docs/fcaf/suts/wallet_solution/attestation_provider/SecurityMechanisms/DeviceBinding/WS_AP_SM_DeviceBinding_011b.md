# WS_AP_SM_DeviceBinding_011b

## Objective
Verify that the Wallet Provider signs the Key Attestation with a valid signature value, when the Wallet uses the `jwt` Proof Type.

## References
[CIR 2024/2979 amended] annex Ib
[ETSI TS 119 472-3] section 4.6.1.2
[HAIP] section 4.5.1
[OpenID4VCI] section F.1

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
Wallet uses the `jwt` proof type to convey a key attestation in Credential Requests.

## Technology
Credential with Key Binding.

## Preconditions
A. Wallet is set to 'default_configuration_1'
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully authenticated to the (Authorization Server of the) Credential Issuer.
D. Wallet successfully obtained an Access Token from the Token Endpoint of the (Authorization Server of the) Credential Issuer.
E. Wallet send a syntactically correct Credential Request to the Credential Endpoint of the Credential Issuer.
F. Wallet send a syntactically correct `proofs` parameter in the Credential Request.
G. Wallet send a valid signed JWT as value of the  `jwt` property in the `proofs` parameter of the Credential Request.
H. The Key Attestation in the `jwt` proof type is signed using an acceptable signature algorithm.

## Test Scenario
1. Verify the signature value of the Key Attestation, using the public key in the `x5c` JOSE header.

## Expected results
1. The signature is valid.
