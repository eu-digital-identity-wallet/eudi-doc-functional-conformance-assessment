# WS_RP_DM_Credentialmetadata_Issuingcountry_PID_IETF-sd-jwt-vc_002

## Objective
This test case verifies that the claim `issuing_country` is a String encoded in UTF-8. Note that `issuing_country` is the Attribute Identifier in IETF SD-JWT VC for the Data Identifier `issuing_country`. 

## References
- [PID rulebook] Annex 3.01, Section 4.2 (Table 8)
- [RFC7049] Section 2.1

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1".

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.

B. All mandatory data elements within namespace "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested.

C. EUDI wallet presented the Credential successfully.

D. The presence of claim `issuing_country` in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify that the claim `issuing_country` is a String encoded in UTF-8, supporting the full Unicode range

## Expected results
1. The claim `issuing_country` is a String encoded in UTF-8, supporting the full Unicode range.