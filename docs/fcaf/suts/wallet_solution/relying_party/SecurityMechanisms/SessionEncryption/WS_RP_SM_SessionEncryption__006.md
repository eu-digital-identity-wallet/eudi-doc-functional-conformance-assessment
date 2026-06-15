# WS_RP_SM_SessionEncryption_006

## Objective
Verify that Wallet raises an error if there is no `jwk` within `client_metadata` sent by the Verifier with `alg` value set to ECDH-ES.

## References
[HAIP] section 5 (introduction) 
[OpenID4VP] section 8.3 The alg parameter MUST be present in the JWKs
[RFC 7516] section 4.1.1
[RFC 7518] section 6.2.1.1

## Profile applicability

none

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions

none

## Test Scenario
1. Verify that Wallet raises an error if there is no "jwk" within "client_metadata" sent by the Verifier with "alg" value set to ECDH-ES.

## Expected results
1. Wallet raises an error. 

