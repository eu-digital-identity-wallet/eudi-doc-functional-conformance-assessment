# WS_RP_MS_ProtocolMessages_144

## Objective

Test the wallet responds with invalid_request if the Client Identifier violates the specific security requirements of its prefix

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier.
2. The verifier sends an Authorization request using client_id prefix https, but the request is sent as plain unsigned URL parameters, instead of a Signed Request Object (JWT).
3. Wallet processes the request and identifies security violation for the prefix
4. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True: The Wallet does NOT proceed to credential selection or user authorization.
4. Verify: The Wallet returns an error response where the error parameter is exactly invalid_request.

