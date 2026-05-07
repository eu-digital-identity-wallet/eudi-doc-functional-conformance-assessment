# WS_RP_SM_TrustMechanisms_002

## Objective
Test that the wallet when proccessing trusted_authorites, the type "aki" is supported

## References
[OID4VP 6.1.1]
Section 4.2.1.1 of [RFC5280]

## Profile applicability
Wallet supports trusted authorities query based on 'aki'

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query with a credential with a "trusted_authorities" property with its type being "aki".
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. No errors returned by the wallet using the KeyIdentifier of the AuthorityKeyIdentifier as defined in Section 4.2.1.1 of [RFC5280], encoded as base64url

