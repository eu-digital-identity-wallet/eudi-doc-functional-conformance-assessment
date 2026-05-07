# WS_RP_IA_MainInteraction_056

## Objective
The response_uri value MUST be a value that the client would be permitted to use as redirect_uri when following the rules defined in Section 5.9.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request, with parameter `response_mode=direct_post` and an invalid `redirect_uri` (not following rules in section 5.9)
3. The wallet processes the request.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Wallet returns an error.

