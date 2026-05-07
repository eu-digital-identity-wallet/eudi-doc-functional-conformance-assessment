# WS_RP_IA_MainInteraction_049

## Objective
Test when using response mode "direct_post" the Wallet encodes the Authorization Response, in the HTTP POST request body, using format defined by application/x‑www‑form‑urlencoded.
Same device custom URL.

## References
[OID4VP Section 8]

## Profile applicability
Same device custom URL

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
4. Verify the wallet submits the response including the Authorization Response encoded using format defined by application/x‑www‑form‑urlencoded.

