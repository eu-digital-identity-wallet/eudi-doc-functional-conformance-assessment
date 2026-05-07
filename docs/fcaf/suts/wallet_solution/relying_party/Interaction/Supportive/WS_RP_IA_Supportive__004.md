# WS_RP_IA_Supportive_004

## Objective
Test the wallet returns the error message: wallet_unavailable when wallet is undergoing critical background updates.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
The Wallet is executing a critical background update and has set its internal state to "Busy/Maintenance."

## Test Scenario
1. The wallet engages with verifier.
2. The verifier sends a valid Authorization request.
3. Wallet processes request and checks internal status.
4. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request.
3. Update in progress.
4. Verify the Wallet does NOT return a credential; instead, it returns an error response where the error parameter is exactly wallet_unavailable.

