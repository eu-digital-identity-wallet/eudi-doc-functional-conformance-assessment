# WS_AP_MS_ProtocolMessages_050b

## Objective
Verify that the Wallet sends a syntactically correct `credential_configuration_id` parameter in the Credential Request to the Credential Endpoint of the Credential Issuer, when requesting issuance of a Credential with Key Binding.

## References
[ETSI TS 119 472-3] section 4.6
[HAIP] section 4.5
[OpenID4VCI] section 8.2

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None

## Technology
Issuance via Redirects.

## Preconditions
A. Wallet is set to 'default_configuration_1'
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully authenticated to the (Authorization Server of the) Credential Issuer.
D. Wallet obtained an Access Token from a Token Response that did not return `credential_identifiers`.
E. Wallet send a HTTP Request to the Credential Endpoint.
F. Wallet send a Credential Request containing the `credential_configuration_id` parameter to the Credential Endpoint.

## Test Scenario
1. Verify the `credential_configuration_id` parameter in the HTTP Request send to the Credential Endpoint.

## Expected results
1. The `credential_configuration_id` parameter in the HTTP Request is a string.
