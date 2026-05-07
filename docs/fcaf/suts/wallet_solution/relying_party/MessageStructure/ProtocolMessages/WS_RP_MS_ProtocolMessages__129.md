# WS_RP_MS_ProtocolMessages_129

## Objective
Test that when the JWK has kid parameter, the Wallet MUST include that same kid value, in the kid JWE header of the response.

## References
Section 4.1.6
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends an Authorization request to the wallet, with response mode=direct_post.jwt, and a client_metadata object containing a JWK with kid parameter
3. Wallet processes request

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Verify the wallet returns a response, without an error, and that it includes that same kid value, in the kid JWE header of its response.

