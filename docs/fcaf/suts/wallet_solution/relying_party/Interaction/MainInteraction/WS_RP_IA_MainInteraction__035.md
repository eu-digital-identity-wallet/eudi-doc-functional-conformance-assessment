# WS_RP_IA_MainInteraction_035

## Objective
Test that the wallet returns the VP token in the Authorization response if the response type value is vp_token

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The Verifier sends a Authorization Request with response type value: vp_token
3. Wallet returns a VP token in its response.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. True

