# EuPid_DM_ResidentHouseNumber_02

## Objective
This test case verifies that the claim resident_house_number is a String enconded in UTF-8.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1   
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.2 (Table 7).  
 RFC 7049 section 2.1

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1". claim resident_chouse_number is included in a person identification data.

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.  
B. All mandatory data elements within nameSpace  "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested. 
C. EUDI wallet presented the Credential successfully. 
D. The presence of claim resident_house_number in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify that the claim resident_house_number is a String encoded in UTF-8, supporting the full unicode range.

## Expected results
1. The claim resident_postal_code is a String encoded in UTF-8, supporting the full unicode range.