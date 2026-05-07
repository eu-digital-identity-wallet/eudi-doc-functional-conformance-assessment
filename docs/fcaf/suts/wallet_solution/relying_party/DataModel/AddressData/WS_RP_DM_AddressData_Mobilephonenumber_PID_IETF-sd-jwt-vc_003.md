# EuPid_DM_MobilePhoneNumber_03

## Objective
This test case verifies that the value of the claim  mobile_phone_number is a formatted as an international phone number.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1   
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.2 (Table 2).  
 RFC 5322 Section 3.4

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
The EUDI wallet contains a Credential in IETF SD-JWT VC format. `vct` claim includes base type of person identification "urn:eudi:pid:1". claim mobile_phone_number is included in a person identification data.

## Preconditions
A. A presentation request was sent to the EUDI wallet, to retrieve a PID Credential in IETF SD-JWT VC format.  
B. All mandatory data elements within nameSpace  "urn:eudi:pid:" and all data elements indicated as present in the ICS were requested. 
C. EUDI wallet presented the Credential successfully. 
D. The presence of claim mobile_phone_number in the IETF SD-JWT VC Credential presented was verified.

## Test Scenario
1. Verify the length of the claim mobile_phone_number. 2. Verify the value of the Mobile Phone Number. 3. Check that the following numbers after the '+'.

## Expected results
1. The length of the claim mobile_phone_number is at least 8 UTF-8 characters. 2. Mobile telephone number of the User to whom the person identification data relates, starting with the '+' symbol as the international code prefix and the country code, followed by numbers only. 3. Check that the following numbers after the '+' are a country code for phone following ITU-T E.164.