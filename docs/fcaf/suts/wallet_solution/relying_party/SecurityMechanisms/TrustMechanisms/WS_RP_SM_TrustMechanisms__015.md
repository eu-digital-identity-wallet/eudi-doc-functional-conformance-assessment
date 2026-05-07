# WS_RP_SM_TrustMechanisms_015

## Objective
Test the wallet checks that the trust chain of a matching Credential MUST contain at least one X.509 Certificate that matches one of the entries of the Trusted List or its cascading Trusted Lists.

## References
[OID4VP 6.1.1]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_optional

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. Verifier sends the Wallet a Credential signed by an unrecognised issuer (a certificate that does not appear in the Trusted List or any of its sub-lists).

## Expected results
1. Wallet and Verifier can interact.
2. The Wallet identifies that the issuer is missing from the "Chain of Trust" and rejects the credential (e.g., marks it as "Untrusted" or excludes it from the selection screen).

