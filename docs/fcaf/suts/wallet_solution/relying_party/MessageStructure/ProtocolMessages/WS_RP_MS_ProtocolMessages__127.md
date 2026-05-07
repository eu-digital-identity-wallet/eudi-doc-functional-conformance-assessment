# WS_RP_MS_ProtocolMessages_127

## Objective
Test the Wallet ignores an unrecognized parameter provided by the Verifier in its JSON response, returned from a response_uri.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends an Authorization request, with response_type=vp_token, and parameter response_uri
3. The wallet performs HTTP POST to the response_uri
4. The verifier responds with HTTP 200 and a JSON body (containing an unrecognized parameter)
5. Wallet processes JSON and triggers User agent

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. Verify the Wallet ignores error without displaying issue
5. Wallet opens redirect_uri, shows user success page

