# WS_RP_IA_MainInteraction_041

## Objective
Test that if "multiple" is false, the vp_token array contains only one presentation.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request where credential query has "multiple" set to false
3. The wallet returns a vp_token parameter in its response

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Verify the vp_token array contains only one presentation.

