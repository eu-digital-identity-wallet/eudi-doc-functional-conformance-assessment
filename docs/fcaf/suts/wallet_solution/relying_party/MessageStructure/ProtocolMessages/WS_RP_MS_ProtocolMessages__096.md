# WS_RP_MS_ProtocolMessages_096

## Objective
Test that the credential_sets "options" property is REQUIRED and correctly processed by the Wallet.

## References
[OID4VP 6.2]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query with a "credential_sets" property, but where it is missing its "options" property
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. The wallet detects a missing crendential_sets "options" property and returns an "invalid request" error

