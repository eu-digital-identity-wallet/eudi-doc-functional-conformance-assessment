# WS_RP_SM_TrustMechanisms_020

## Objective
Test the wallet ensures the path leads to the specific anchor requested.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_undefined

## Preconditions


## Test Scenario
1. Verifier requests openid_federation with Value Anchor_A. The Wallet has a credential that is perfectly valid but belongs to Anchor_B.

## Expected results
1. Wallet treats the credential as non-matching (does not present it), even though it is technically "trusted" in its own separate ecosystem.

