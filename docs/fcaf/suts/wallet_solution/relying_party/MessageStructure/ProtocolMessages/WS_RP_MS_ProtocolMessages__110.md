# WS_RP_MS_ProtocolMessages_110

## Objective
Test the wallet checks that within a particular claims array, the same id MUST NOT be present more than once.

## References
[OID4VP 6.3]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The verifier sends an Authorisation request containing a "credentials" object which itself contains "claims" with the same "id" occuring twice in the claims array.
3. Wallet handles Query

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. The wallet detects duplicate claims "id" values in the claims array and returns an "invalid request" error

