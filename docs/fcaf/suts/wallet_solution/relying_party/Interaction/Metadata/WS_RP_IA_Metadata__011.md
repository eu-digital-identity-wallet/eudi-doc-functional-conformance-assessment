# WS_RP_IA_Metadata_011

## Objective
Test that the wallet rejects the Authorization Request if aud does NOT match the issuer claim value in the wallet metadata.

## References
[OIDF.OID4VP] section 5.8

## Profile applicability
dynamic discovery

## EUDI-wallet relevancy
EUDI_generic |  EUDI_required

## Preconditions


## Test Scenario
1. The Wallet receives a Request Object (Dynamic Discovery) where the aud claim equals the iss claim value.

## Expected results
1. Wallet accepts and processes the request.

