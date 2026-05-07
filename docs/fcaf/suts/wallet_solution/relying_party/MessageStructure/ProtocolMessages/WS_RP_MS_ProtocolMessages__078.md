# WS_RP_MS_ProtocolMessages_078

## Objective
Test the Wallet rejects a DCQL-query with the credential property "trusted_authorities" in an incorrect format (i.e. not an array).

## References
[OID4VP 6.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The Verifier sends a Authorization Request with a DCQL-query with a credential with a non-empty, non-array type "trusted_authorities" property.
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. Wallet rejects the request by either:
a. answering with an error with details (`invalid_request`), 
b. answering with an error without providing details or,
c. discontinuing the interaction.

