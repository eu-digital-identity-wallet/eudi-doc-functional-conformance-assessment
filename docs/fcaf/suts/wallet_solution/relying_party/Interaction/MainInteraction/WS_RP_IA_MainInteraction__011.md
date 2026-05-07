# WS_RP_IA_MainInteraction_011

## Objective
Test that the wallet can, if supported, use claim value matching for issuer selection

## References
[OID4VP 6.1.1]

## Profile applicability
wallet supports claim iss value matching in request

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The Wallet engages with the Verifier
2. The Verifier sends an Authorization Request containing a dcql_query with a credentials constraint with a valid trusted_authorities with a specific value.
3. The Wallet processes the request.

## Expected results
1. Wallet and Verifier can interact.
2. Wallet receives the request.
3. The Wallet identifies and presents only the credential(s) issued by the matching entity, logically excluding all other valid credentials from non-matching issuers.

