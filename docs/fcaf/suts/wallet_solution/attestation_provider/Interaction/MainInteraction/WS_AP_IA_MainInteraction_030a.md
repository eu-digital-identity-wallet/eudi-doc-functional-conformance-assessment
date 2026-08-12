# WS_AP_IA_MainInteraction_030a

## Objective
Verify that the Wallet sends a Credential Request using a HTTP Request to the Credential Endpoint of the Credential Issuer.

## References
[ETSI TS 119 472-3] section 4.6
[HAIP] section 4
[OpenID4VCI] section 8.2

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None.

## Technology
OpenID4VCI Credential Endpoint requests.

## Preconditions
A. Wallet is set to 'default_configuration_1'.
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully authenticated to the (Authorization Server of the) Credential Issuer.
D. Wallet successfully obtained an Access Token from the Token Endpoint of the (Authorization Server of the) Credential Issuer.
E. Wallet established a connection to the Credential Endpoint of the Credential Issuer, after receiving the Access Token from the Token Endpoint.

## Test Scenario
1. Verify the Credential Request.

## Expected results
1. The Wallet sends a HTTP Request to the Credential Endpoint of the Credential Issuer as listed in the Credential Issuer Metadata. The HTTP Request:
    1. Uses the POST method.
    2. Has the 'hostname', and 'port-number' if applicable, of the `credential_endpoint` in the Credential Issuer's Metadata.
    3. Requests the 'path' and 'query', if applicable, of the `credential_endpoint`, without a fragment part.
