# WS_RP_MS_ProtocolMessages_002

## Objective
Verify that the Wallet can process a plain RFC9700 Authorization Request where parameters are passed directly as URL-encoded parameters (not as a Request Object, not signed).

## References
[RFC 6749]; [RFC 9700]; [OpenID4VP] section 5

## Profile applicability

none

## EUDI-wallet relevancy
EUDI_generic | EUDI_undefined

## Preconditions

none

## Test Scenario
1. Engage wallet-verifier interaction (e.g. click link / scan QR code).
2. Wallet receives a plain RFC9700 Authorization Request where parameters are passed directly as URL-encoded parameters (not as a Request Object, not signed).

## Expected results
1. Wallet-verifier interaction is successfully initiated.
2. Wallet successfully processes the plain RFC9700 Authorization Request and proceeds with the presentation flow.

