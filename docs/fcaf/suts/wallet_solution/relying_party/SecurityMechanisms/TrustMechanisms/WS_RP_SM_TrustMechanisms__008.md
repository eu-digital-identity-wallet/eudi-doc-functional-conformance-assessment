# WS_RP_SM_TrustMechanisms_008

## Objective
Test that the wallet behaves correctly when AKI match NOT successful.

## References
[OID4VP 6.1.1]

## Profile applicability
Wallet supports trusted authorities query based on 'aki'

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query requesting a credential which will not match to any in wallet.
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3a. The wallet identifies a mismatch. 
 
3b. The credential is excluded.
3c. The wallet does not present the mismatched credential to the user.
3d. The wallet returns a privacy keeping (generic error) to verifier, NOT specific "AKI wrong".

