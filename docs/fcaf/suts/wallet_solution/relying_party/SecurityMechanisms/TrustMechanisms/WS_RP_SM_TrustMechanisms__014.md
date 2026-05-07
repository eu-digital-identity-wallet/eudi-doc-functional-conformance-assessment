# WS_RP_SM_TrustMechanisms_014

## Objective
Verify the Wallet can navigate an ETSI Trusted List (with a specific entry for a Provider) to identify and validate a Trust Service Provider’s (TSP) certificate.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_optional

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Provide the Wallet with an ETSI Trusted List that contains a specific entry for a Provider and their X.509 certificate.

## Expected results
1. Wallet and Verifier can interact.
2. Verify the Wallet correctly parses the list and recognises the Provider as "Trusted" by matching their actual certificate against the one listed in the ETSI entry.

