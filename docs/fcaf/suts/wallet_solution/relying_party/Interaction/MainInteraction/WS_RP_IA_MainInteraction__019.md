# WS_RP_IA_MainInteraction_019

## Objective
Test that when a claim_sets is present, the Wallet allows the selection of only one specific combination from claim_sets, preventing disclosure of multuiple sets.

## References
[OID4VP 6.4]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends a DCQL query with a claim_sets holding 3 "claim_sets objects"
3. Wallet does not try to send both claim_sets objects

## Expected results
1. Wallet and Verifier can interact.
2. Wallet identifies two sets it can satisfy based on its credentials.
3. Once a valid set has been presented to user, the remaining claim_sets object will not be used.

