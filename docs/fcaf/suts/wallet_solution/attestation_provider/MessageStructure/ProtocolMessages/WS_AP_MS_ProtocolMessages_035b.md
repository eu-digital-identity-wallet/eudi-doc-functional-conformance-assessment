# WS_AP_MS_ProtocolMessages_035b

## Objective
Verify that the Wallet sends a HTTP Request that contains a syntactically correct `OAuth-Client-Attestation` HTTP header when sending a Pushed Authorization Request, when using Pushed Authorization Requests for issuance.

## References
[CIR 2024/2979 amended] annex Ib
[ETSI TS 119 472-3] section 4.4
[HAIP] section 4.3
[OpenID4VCI] section 5.1.4
[RFC9126] section 2.1
[IETF draft-attestation-based-client-auth] section 5.1, 6.1

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None.

## Technology
Issuance via Redirects.

## Preconditions
A. End-user is engaging with a Credential Issuer using a User-agent.
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully obtained Credential Issuer Metadata.
D. The Wallet sends an HTTP POST Request to the selected Authorization Server's PAR endpoint.
E. The HTTP Request to the selected Authorization Server's PAR endpoint contains an `OAuth-Client-Attestation` HTTP header.

## Test Scenario
1. Verify the `OAuth-Client-Attestation` HTTP-Header of the received HTTP Request.

## Expected results
1. The value of the `OAuth-Client-Attestation` HTTP Header of the HTTP Request has the structure of a signed JWT in compact serialization, that is three Base64url-encoded parts separated by exactly two period (`.`) characters.
