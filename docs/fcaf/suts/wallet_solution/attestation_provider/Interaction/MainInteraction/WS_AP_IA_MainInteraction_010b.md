# WS_AP_IA_MainInteraction_010b

## Objective
Verify that the Wallet sends a reference to a Pushed Authorization Request to the Authorization Server's Authorization Endpoint, when requesting a Credential.

## References
[ETSI TS 119 472-3] section 4.1
[HAIP] section 4
[OpenID4VCI] section 5.1
[RFC9126] section 4
[RFC9101] section 5

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None.

## Technology
Issuance via Redirects.
Credential Issuance using the Authorization Code Flow.

## Preconditions
A. Wallet is set to 'default_configuration_1'.
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully obtained Credential Issuer Metadata.
D. Wallet successfully obtained the Authorization Server Metadata.
E. Wallet successfully pushed an Authentication Request to the Authorization Server's `pushed_authorization_request_endpoint`.
F. Wallet send an Authorization Request to the Authorization Server's `authorization_endpoint`.

## Test Scenario
1. Verify the contents of the Authorization Request.

## Expected results
1. The Authorization Request includes a `request_uri` parameter.
