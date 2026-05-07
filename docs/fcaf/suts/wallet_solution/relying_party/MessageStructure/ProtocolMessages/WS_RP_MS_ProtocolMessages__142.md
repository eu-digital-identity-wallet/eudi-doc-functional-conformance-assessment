# WS_RP_MS_ProtocolMessages_142

## Objective

Test the wallet responds with invalid_request when the request asks for a vp_token, but does not include instructions on what data to put in token.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier.
2. The verifier sends an Authorization request with response_type=vp_token, but omitting both the dcql_query & any scope values referencing a credential
3. Wallet processes the request and identifies no data requirements provided
4. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True: The Wallet does NOT proceed to credential selection or user authorization.
4. Verify: The Wallet returns an error response where the error parameter is exactly invalid_request.

