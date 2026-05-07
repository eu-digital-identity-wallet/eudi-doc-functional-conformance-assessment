# WS_RP_MS_ProtocolMessages_125

## Objective
Test that Wallet returns an error after an HTTP 200 response not of form json

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
5. Verifier sends a HTTP status code of 200 + a plain text body

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. True
5. Wallet returns an error

