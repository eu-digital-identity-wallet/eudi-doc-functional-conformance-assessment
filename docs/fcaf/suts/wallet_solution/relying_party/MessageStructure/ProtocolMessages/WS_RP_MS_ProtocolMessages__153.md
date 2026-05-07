# WS_RP_MS_ProtocolMessages_153

## Objective
Test the wallet returns the invalid_transaction_data error message, when one object in the transaction_data structure contains an unsupported transaction data type value

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with verifier
2. The verifier sends an Authorization request including a transaction_data array where one object has an unsupported type
3. Wallet processes request and the transaction_data structure
4. Test the response returned by the wallet to the verifier

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Wallet identifies unsupported type
4. Verify the wallet does NOT proceed to the user consent screen, instead it must return an error response: invalid_transaction_data

