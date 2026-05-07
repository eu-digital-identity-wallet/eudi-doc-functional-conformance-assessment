# WS_RP_MS_ProtocolMessages_157

## Objective
Test the wallet returns the invalid_transaction_data error message, when one object in the transaction_data structure is missing required fields for the transaction data type

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
The wallet has a known transaction data type, where specific fields are marked as required.

## Test Scenario
1. The wallet engages with verifier
2. The verifier sends an Authorization request including a transaction_data array where one object uses a known type, but with a missing mandatory field
3. Wallet processes request and the transaction_data structure
4. Test the response returned by the wallet to the verifier

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Wallet identifies missing mandatory field
4. Verify the wallet does NOT proceed to the user consent screen, instead it must return an error response: invalid_transaction_data

