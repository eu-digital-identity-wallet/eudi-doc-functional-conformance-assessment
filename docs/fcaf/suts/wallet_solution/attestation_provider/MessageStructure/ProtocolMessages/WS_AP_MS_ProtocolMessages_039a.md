# WS_AP_MS_ProtocolMessages_039a

## Objective
Verify that the Wallet sends a syntactically correct Authorization Request to the Authorization Endpoint, when authentication to a Authorization Server for requesting issuance of a Credential.

## References
[ETSI TS 119 472-3] section 4.4
[HAIP] section 4.3
[OpenID4VCI] section 5.1.2, 5.1.3
[RFC9126] section 4
[RFC9101] section 5.2.2
[RFC6749] section 4.1.1

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None.

## Technology
Issuance via Redirects.

## Preconditions
A. Wallet is set to 'default_configuration_1'
B. End-user is engaging with a Credential Issuer using a User-agent.
C. Wallet started engagement with Credential Issuer.
D. Wallet successfully obtained Credential Issuer Metadata.
E. Wallet send a valid and trusted PAR request the Authorization Server's PAR Endpoint.
F. Wallet send a Authorization Request to the Authorization Server's Authorization Endpoint.

## Test Scenario
1. Verify the Authorization Request.

## Expected results
1. The Authorization Request contains the following top-level request parameters:
    1. `request_uri`
    2. `client_id`

