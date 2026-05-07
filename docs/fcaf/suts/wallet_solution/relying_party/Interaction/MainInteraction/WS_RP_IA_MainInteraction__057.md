# WS_RP_IA_MainInteraction_057

## Objective
Test that Wallet accepts an HTTP 200 response with Content-Type: application/json after sending the Authorization Response to the response_uri.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request, with parameter `response_mode=direct_post'
3. The wallet processes the request.
4. The wallet responds with request object
5. Verifier sends a HTTP status code of 200 + a JSON body

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. True
5. Wallet does NOT return an error, returns user to URL provided.

