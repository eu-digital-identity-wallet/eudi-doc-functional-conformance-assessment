# EuPid_DM_ResidentPostalCode_01

## Objective
This test case verifies that the data element resident_postal_code is present in the mdoc data if this is indicated in the ICS.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.1    
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.1 (Table 2).

## EUDI-wallet relevancy
EUDI_specific | EUDI_optional

## Profile applicability
The EUDI wallet contains a Credential in ISO-mdoc format with DocType = “eu.europa.ec.eudi.pid.1” Data element resident_postal_code is present in the mdoc data.

## Preconditions
A. A device retrieval mdoc request was sent to the EUDI wallet, to retrieve the document with DocType = "eu.europa.ec.eudi.pid.1". 
B. All mandatory data elements within nameSpace "eu.europa.ec.eudi.pid.1" and all data elements indicated as present in the ICS were requested. 
C. The device retrieval mdoc response was retrieved.

## Test Scenario
1. Verify the presence of a data element with identifier resident_postal_code in the device retrieval mdoc response. 2. Verify the presence of an ErrorItem for data element resident_postal_code.

## Expected results
1. One data element with identifier resident_postal_code is present. 2. There is no ErrorItem for data element resident_postal_code.