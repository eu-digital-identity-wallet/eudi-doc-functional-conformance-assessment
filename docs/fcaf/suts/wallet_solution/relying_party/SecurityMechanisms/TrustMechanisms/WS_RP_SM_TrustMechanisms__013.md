# WS_RP_SM_TrustMechanisms_013

## Objective
Verify the Wallet can navigate an ETSI Trusted List (with a List of Lists) to identify and validate a Trust Service Provider’s (TSP) certificate.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_optional

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier provides the Wallet with an ETSI Trusted List that contains a link to another list

## Expected results
1. Wallet and Verifier can interact.
2. Verify the Wallet correctly parses the lists and recognises the Provider as "Trusted" by matching their actual certificate against the one listed in the ETSI entry.

