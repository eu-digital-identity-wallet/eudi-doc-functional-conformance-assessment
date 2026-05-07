# WS_RP_IA_MainInteraction_037

## Objective
Test that the vp_token parameter returned by the wallet, contains key id(s), aligning with the id value of the credential query.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request
3. The wallet returns a vp_token parameter in its response

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Verify the vp_token keys align with the requests credential query id values.

