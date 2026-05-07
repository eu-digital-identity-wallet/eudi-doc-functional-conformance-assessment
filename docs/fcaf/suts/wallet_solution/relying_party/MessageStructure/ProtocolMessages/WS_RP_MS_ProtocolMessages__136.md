# WS_RP_MS_ProtocolMessages_136

## Objective
Test a wallet that received transaction_data in a request, but cannot support it, MUST return an error.

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends an Authorization request containing a transaction_data object which the wallet cannot support
3. Wallet determines it cannot support this request

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. Wallet does NOT show a credential selection screen to user, it will return an error response.

