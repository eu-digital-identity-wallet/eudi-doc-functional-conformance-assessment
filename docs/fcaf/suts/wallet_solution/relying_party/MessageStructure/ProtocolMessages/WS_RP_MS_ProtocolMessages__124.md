# WS_RP_MS_ProtocolMessages_124

## Objective
Test that the Wallet ignores any unrecognized parameters when Response Mode = direct_post.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends a request, with parameter `response_mode=direct_post`plus an additional unknown parameter.
3. The wallet processes the request.
4. The wallet responds with request object

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. Verify the wallet submits the response successfully, ignoring the unknown parameter

