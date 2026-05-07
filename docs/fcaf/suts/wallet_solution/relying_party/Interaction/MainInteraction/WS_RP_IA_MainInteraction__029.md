# WS_RP_IA_MainInteraction_029

## Objective

Test that If credential_sets is provided, the wallet will see this as asking for credentials to be returned, satisfying all of the Credential Set Queries in the credential_sets array, where the required attribute is true or omitted, and optionally, any of the other Credential Set Queries.

## References
[OID4VP 6.4]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
the Wallet only has credential #1

## Test Scenario
Verifier sends credential_sets with two queries:
1. Credential #1 (required: true)
2. Credential #2 (required: false)

## Expected results
The Wallet offers credential #1, and still allows the presentation.

