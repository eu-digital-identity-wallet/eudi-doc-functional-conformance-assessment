# WS_RP_DM_Credentialmetadata_Domestic_PID_IETF-sd-jwt-vc_002

## Objective
This test case verifies domestic claims are located in a valid domestic namespace, if these have been indicated in the ICS.

## References
- [PID rulebook] Annex 3.01, Section 4.2

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1", which contains data elements in a domestic namespace.

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.

B. All mandatory data elements within namespace "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested.

C. EUDI wallet presented the Credential successfully.

D. The presence of claim from domestic namespace in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify that the domestic namespace complies with a valid the domestic namespace identifier.

## Expected results
1. Domestic namespace complies with a valid the domestic namespace identifier.