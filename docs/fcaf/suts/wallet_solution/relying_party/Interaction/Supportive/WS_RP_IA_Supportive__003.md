# WS_RP_IA_Supportive_003

## Objective
Test the wallet returns the error message: wallet_unavailable when the SE is locked.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
The device SE is locked.

## Test Scenario
1. The wallet engages with verifier.
2. The verifier sends a valid Authorization request.
3. Wallet processes request and attempts to access the Secure Element to sign the response.
4. The Secure Element returns a lockout error to the Wallet application.
5. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request.
3. True: The Wallet proceeds to the point of signing/generation.
4. True: Hardware access is denied.
5. Verify the Wallet does NOT return a credential; instead, it returns an error response where the error parameter is exactly wallet_unavailable.

