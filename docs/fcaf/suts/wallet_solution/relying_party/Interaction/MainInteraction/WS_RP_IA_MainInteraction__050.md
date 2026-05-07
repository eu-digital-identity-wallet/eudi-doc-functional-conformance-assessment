# WS_RP_IA_MainInteraction_050

## Objective
Test all parameters in the HTTP POST request body are encoded using UTF‑8.
Same device DC API

## References
OAuth
[OID4VP Section 8]

## Profile applicability
Same device DC API

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request, with parameter `response_mode=direct_post` and a `response_uri` of the verifier.
3. The wallet processes the request.
4. The wallet responds with request object

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. Verify that all parameters in the HTTP POST request body are encoded using UTF‑8.

