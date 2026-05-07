# WS_RP_SM_TrustMechanisms_018

## Objective
Test that the wallet correctly proccesses the type "openid_federation" when Entity has a expired/revoked federation_id

## References
[OID4VP 6.1.1]

## Profile applicability
Wallet supports trusted authorities query based on OpenID Federation.

## EUDI-wallet relevancy
EUDI_generic | EUDI_undefined

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query requesting a credential with a "trusted_authorities" property with its type being "openid_federation".
3. The Wallet evaluates the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3a. Confirm the wallet recognises type: "openid_federation" without errors.
3b. The wallet performs trust-chain lookup and authority validation through the OpenID Federation mechanism then decides it must not use the credential in question.
3c. The wallet checks the provided Entity’s federation_id against its trusted anchors.
3d. The wallet returns a generic response to the Verifier to ensure the existence of the credential/PID is not disclosed.

