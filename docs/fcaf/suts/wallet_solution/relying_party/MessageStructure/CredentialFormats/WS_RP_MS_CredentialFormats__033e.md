# WS_RP_MS_CredentialFormats_033e

## Objective
Verify that the Wallet includes all relevant elements in the `status_list` revocation mechanism in the `status` element in a mdoc presentation, when the issuer included the status information in the credential in Token Status List format.

## References
[CIR 2024/2982 amended] annex II
[ETSI TS 119 472-1] section 6.2.10
[Token Status List] section 6.3

## Profile applicability
None

## Technology
Credential in mdoc format
Credential with revocation status information
Credential with Revocation status information in Token Status List Format

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
A. Wallet is set to 'default_configuration_1'
B. Verifier requested a credential to be presented, using a valid, trusted request for 'default_credential_A' and requesting presentation in mdoc of all data elements.
C. The presentation value of the credential is a syntactically correct presentation of a mdoc.
D. The presentation value of the credential contains a valid signed MSO.
E. The MSO of the presented mdoc contains a correctly formatted `status` element.
F. The `status` element in the MSO of the presented mdoc contains a correctly formatted `status_list` element.

## Test Scenario
1. Verify the `status_list` element in the `status` element in the MSO of the presented mdoc credential.

## Expected results
1. The `status_list` element in the `status` element in the MSO contains a `idx` and a `uri` element.

## Comments
* While the contents of the `status` claim is a responsibility of the issuer, the Wallet must pass the value unmodified.
