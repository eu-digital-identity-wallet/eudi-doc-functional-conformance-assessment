# EuPid_DM_DocumentNumber_02

## Objective
This test case verifies that the value of the document_number is a String.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1 The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1".  
 RFC 7049 section 2.1

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.2 (Table 8).

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.  
B. All mandatory data elements within nameSpace  "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested. 
C. EUDI wallet presented the Credential successfully.

## Test Scenario
1. The claim expiry_date is a String encoded in UTF-8, supporting the full unicode range.

## Expected results
1. The major type value is equal to 3. 2. All bytes in the data item value are UTF-8 encoded characters.