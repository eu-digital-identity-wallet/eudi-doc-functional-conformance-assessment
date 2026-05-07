# WS_RP_IA_MainInteraction_043

## Objective
Test the wallet omits optional DCQL query keys in the presentation when no matching credentials exist.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
Wallet does NOT contain matching credentials for the queries optional credentials

## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request where credential query includes some optional credentials
3. The wallet returns a vp_token parameter in its response

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Verify the vp_token does NOT contain key ids from the optional credentials.

