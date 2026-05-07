# WS_RP_MS_ProtocolMessages_054

## Objective
Test that if DCQL does not contain a property "credentials", the Wallet rejects the request.

## References
[OID4VP 6]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The Verifier sends a Authorization Request with a DCQL-query with a missing "credentials"
3. The wallet evaluates the request

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. The Wallet rejects the request by either:
a. answering with an error with details (`invalid_request`), 
b. answering with an error without providing details or,
c. discontinuing the interaction.

