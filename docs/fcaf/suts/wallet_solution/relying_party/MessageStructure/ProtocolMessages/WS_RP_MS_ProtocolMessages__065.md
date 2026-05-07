# WS_RP_MS_ProtocolMessages_065

## Objective
Test the wallet rejects DCQL-query credential object property "id" when it consists of invalid charafcters (i.e. other than alphanumeric, underscore (_), or hyphen (-)).

## References
[OID4VP 6.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The Verifier sends a Authorization Request with a DCQL-query with a credential with "id" property containing a character other than alphanumeric, underscore (_), or hyphen (-).
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. Wallet rejects the request by either:
a. answering with an error with details (`invalid_request`), 
b. answering with an error without providing details or,
c. discontinuing the interaction.

