# WS_AP_SM_DeviceBinding_013a

## Objective
Verify that the Wallet uses the nonce from the Nonce Endpoint of the Credential Issuer to include a nonce in the Key Attestation, when the Wallet uses the `attestation` Proof Type.

## References
[CIR 2024/2979 amended] annex Ib
[ETSI TS 119 472-3] section 4.6.1.3
[HAIP] section 4.5.1
[OpenID4VCI] section 7, 8.2, F.3

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
Wallet uses the `attestation` proof type to convey a key attestation in Credential Requests.

## Technology
Credential with Key Binding.

## Preconditions
A. Wallet is set to 'default_configuration_1'
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully obtained Credential Issuer Metadata, including the `nonce_endpoint` of the Credential Issuer.
D. Wallet successfully authenticated to the (Authorization Server of the) Credential Issuer.
E. Wallet successfully obtained an Access Token from the Token Endpoint of the (Authorization Server of the) Credential Issuer.
F. Wallet successfully obtained a value in `c_nonce` in the Nonce Response, by making a Nonce Request to the Nonce Endpoint of the Credential Issuer.
G. Wallet send a valid and trusted signed attestation as Key Attestation, with the Credential Request.
H. Wallet send a syntactically correct `nonce` in the Key Attestation.

## Test Scenario
1. Verify the `nonce` value in the Key Attestation.

## Expected results
1. The value of the `nonce` in the signed attestation that makes the Key Attestation, is equal to the value of the `c_nonce` provided in the Nonce Response from the Nonce Endpoint.
