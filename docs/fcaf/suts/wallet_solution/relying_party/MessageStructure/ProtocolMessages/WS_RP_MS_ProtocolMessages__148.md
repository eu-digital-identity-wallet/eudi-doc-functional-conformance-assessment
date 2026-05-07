# WS_RP_MS_ProtocolMessages_148

## Objective
Test the wallet returns the access_denied error message when the End-User did not give consent to share the requested Credentials with the Verifier.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with verifier.
2. The verifier sends an Authorization request for credentials the wallet does have.
3. Wallet processes request.
4. The User explicitly does NOT give consent to share requested credential.
5. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. The Wallet proceeds to credential selection or user authorization.
4. True.
5. Verify the Wallet does NOT return a vp_token, instead it returns an error response, where the error parameter is exactly access_denied.

