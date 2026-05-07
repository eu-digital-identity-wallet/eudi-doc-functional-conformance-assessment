# WS_RP_MS_ProtocolMessages_101

## Objective
Test that the credential_sets property "required" is correctly supported by the wallet when all credentials exists

## References
[OID4VP 6.2]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query with a "credential_sets" property, including "required" property set as true for a set containing a PID that the wallet is has.
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3a. Wallet identifies that the set containing the PID is marked as required: true.
3b. The wallet confirms the PID exists and satisfies the query. It prepares the PID for presentation.
3c. The wallet presents the PID to the user. Because it is marked as required, the UI should indicate it is mandatory (e.g., no "skip" option for this specific set).
3d. The wallet generates the Verifiable Presentation containing the PID as required by the Verifier

