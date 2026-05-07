# WS_RP_UC_Presentation_003

## Objective
Verify that a Wallet supporting OAuth 2.0 scope-based Presentation requests processes an Authorization Request using a valid pre-defined scope value, regardless of the response_type used (e.g. vp_token, code, or others).

## References
[OIDF.OID4VP] section 5.5

## Profile applicability
Wallet supports OAuth 2.0

## EUDI-wallet relevancy
EUDI_generic | EUDI_forbidden

## Preconditions


## Test Scenario
1. Engage wallet-verifier interaction (e.g. click link / scan QR code).
2. Wallet receives an Authorization Request using a valid OAuth 2.0 scope value defined in the applicable ETSI profile, with any supported response_type (e.g. vp_token, code).
3. Wallet resolves the scope to its configured Credential mapping and proceeds with the presentation flow.

## Expected results
1. Wallet-verifier interaction is successfully initiated.
2. Wallet successfully parses the Authorization Request.
3. Wallet processes the request using the scope-based credential mapping and proceeds with the presentation flow successfully, independent of the response_type value.

