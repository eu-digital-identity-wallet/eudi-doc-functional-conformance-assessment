# WS_RP_SM_TrustMechanisms_019

## Objective
Test that the wallet can check a valid path, by detecting invalid signatures in the middle of the path.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_undefined

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Provide a credential with a path to the correct Trust Anchor, but intentionally corrupt the signature of an intermediate entity.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet rejects the credential because a valid cryptographic path cannot be finished.

