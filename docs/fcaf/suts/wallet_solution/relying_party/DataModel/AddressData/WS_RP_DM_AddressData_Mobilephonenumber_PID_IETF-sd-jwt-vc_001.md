# EuPid_DM_MobilePhoneNumber_01

## Objective
This test case verifies that the claim mobile_phone_number is present in the Credential in IETF SD-JWT VC format if this is indicated in the ICS.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1   
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.2 (Table 2).

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1". claim mobile_phone_number is included in a person identification data.

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.  
B. All mandatory data elements within nameSpace  "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested. 
C. EUDI wallet presented the Credential successfully. 
D. The presence of claim email_address in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify the presence of a claim with identifier mobile_phone_number in the  Credential presented to the Verifier in IETF SD-JWT VC format.

## Expected results
1. One claim with identifier mobile_phone_number is present.