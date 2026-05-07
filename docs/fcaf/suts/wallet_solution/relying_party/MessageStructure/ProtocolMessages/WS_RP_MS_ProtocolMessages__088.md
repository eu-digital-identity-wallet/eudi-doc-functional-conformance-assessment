# WS_RP_MS_ProtocolMessages_088

## Objective
Test the wallet Rejects a DCQL-query with a constraint on "trusted_autorities" with an unspecified type.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query with a credential constraint with a trusted_authorities "type" that is not defined in [OID4VP 6.1]
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. Wallet rejects the request by either:
a. answering with an error with details (`invalid_request`), 
b. answering with an error without providing details or,
c. discontinuing the interaction.

