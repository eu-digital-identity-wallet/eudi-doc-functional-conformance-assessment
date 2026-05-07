# WS_RP_SM_TrustMechanisms_016

## Objective
Test that the wallet supports and correctly proccesses the type "openid_federation"

## References
[OID4VP 6.1.1]
[OpenID.Federation] 

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
3b. Check the wallet performs trust-chain lookup and authority validation through the OpenID Federation mechanism.
3c. The wallet checks the provided Entity’s federation_id against its trusted anchors. Wallet presents credential without error.

