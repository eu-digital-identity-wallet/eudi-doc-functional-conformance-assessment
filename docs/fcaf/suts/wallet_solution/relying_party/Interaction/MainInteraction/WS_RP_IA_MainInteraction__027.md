# WS_RP_IA_MainInteraction_027

## Objective
Test when the Wallet cannot deliver all claims requested by the Verifier because one of them has a non-matching value, it does NOT return the respective Credential.

## References
[OID4VP 6.4]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The verifier sends a DCQL query with 2 Required claims in a credential
2. Returns 

## Expected results
1. Wallet sees only has 1 of those claims in the credential has a matching value, it cannot return the other
2. Wallet does NOT return credential containing the claim that did match, sends a privacy keeping  response

