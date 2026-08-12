# WS_AP_IA_MainInteraction_031a

## Objective
Verify that the Wallet handles a correct Credential Response.

## References
[ETSI TS 119 472-3] section 4.1
[HAIP] section 4
[OpenID4VCI] section 8.3

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Profile applicability
None.

## Technology
OpenID4VCI Credential Endpoint response handling.

## Preconditions
A. Wallet is set to 'default_configuration_1'.
B. Wallet started engagement with Credential Issuer.
C. Wallet successfully sent a valid Credential Request to the Credential Issuer.

## Test Scenario
1. Issuer responds with a valid Credential Response, including at least one valid Credential matching the requested Credential Type.

## Expected results
1. The Credential is stored in the wallet and available for the End-user to present to a Verifier. The End-user is informed the Credential is available, if applicable.
