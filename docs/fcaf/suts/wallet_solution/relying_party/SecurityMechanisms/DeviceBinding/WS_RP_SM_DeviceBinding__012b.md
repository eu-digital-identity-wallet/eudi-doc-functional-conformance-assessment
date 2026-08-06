# WS_RP_SM_DeviceBinding_012b

## Objective
Verify that the Wallet includes a valid signed key binding JWT cryptographically bound to the credential, if a presented credential in SD-JWT VC format is key bound.

## References
[HAIP] section 6.1
[OpenID4VP] section 8, B.3.6
[SD-JWT VC] section 3.4
[RFC9901] section 4.1.2, 7.3
[RFC7515]

## Profile applicability
None.

## Technology
Credential in SD-JWT VC format
Credential with key-binding
Issuer uses compact serialization of SD-JWT and SD-JWT VC

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
A. Wallet is set to 'default_configuration_1'.
B. Verifier requested a credential to be presented, using a valid, trusted request for 'default_credential_A', which is key bound, and requesting presentation in SD-JWT VC format.
C. The Wallet transmitted a syntactically correct presentation in the `vp_token` of the Authorization Response.
D. The presentation value of the credential is a syntactically correct serialization in compact serialization format of an SD-JWT VC.
E. The presentation value of the credential contains a valid signed SD-JWT.
F. The SD-JWT has a top-level `cnf` claim.
G. The presentation value of the credential contains a correctly serialized KB-JWT.
H. The KB-JWT uses an acceptable signature algorithm.

## Test Scenario
1. Verify the KB-JWT signature using the public key identified by the `cnf` claim in the presented SD-JWT.

## Expected results
1. The signature is valid.
