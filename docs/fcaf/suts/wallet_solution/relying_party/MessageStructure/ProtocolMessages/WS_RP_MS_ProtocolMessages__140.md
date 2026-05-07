# WS_RP_MS_ProtocolMessages_140

## Objective
Test that the wallet will not leave the verifier hanging after an error response, it must terminate the session.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier.
2. The verifier sends an Authorization request with a scope value that is intentionally empty (e.g. missing any value)
3. Wallet processes the request and identifies the scope as invalid.
4. Test the response returned by the wallet to the Verifier.
5. Test the wallet terminates the session.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True: The Wallet does NOT proceed to credential selection or user authorization.
4. Verify: The Wallet returns an error response where the error parameter is exactly invalid_scope.
5. True

