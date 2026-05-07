# EuPid_DM_IssuingJurisdiction_03

## Objective
This test case verifies that the value of the claim issuing_jurisction contains a valid country subdivion code.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1,"ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.2 (Table 5). ISO 3166-2:2020, 8

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1". claim issuing_jurisdiction is included in a person identification data.

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.  
B. All mandatory data elements within nameSpace  "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested. 
C. EUDI wallet presented the Credential successfully. 
D. The presence of claim nationality in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify that the value of the claim issuing_jurisdiction contains a valid subdivision country code.

## Expected results
1. The value of the claim subdivision coutry code , an alpha-2 code, corresponding to a user assigned country code, that AA, QM to QZ, XA to XZ, and ZZ (ISO 3166-1:2020, 8.3).