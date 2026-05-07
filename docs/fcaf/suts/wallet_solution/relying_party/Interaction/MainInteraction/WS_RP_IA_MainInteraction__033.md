# WS_RP_IA_MainInteraction_033

## Objective
Checking the wallet is correctly performing logic on range of value constrainsts

## References
[OID4VP 6.4]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
Credentials in wallet are numerical edge cases, string and format edge cases, logical edge cases, array edge cases, DTS edge cases
Verifier sends a DCQL query with "credentials" just MISSING these edge cases.

## Test Scenario
1. Verifier sends in multiple "credentials" each with a unique case as follows: 
age >= 18, 
expiry <= 2025, (also <, >)
kg == 10 (integer vs float) , 
country == "spain" (lowercase)
name == "Smith " (space included)
city = "München" (special characters)
"" (missing claims)
name == "" (null vs "")
[] (empty lists)
["FR"] (single element arrays
2. Wallet processes DCQL

## Expected results
1. Wallet successfully reads and processes "credentials"
2. Credentials do not match, and are not returned.

