# EuPid_DM_BirthPlace_06

## Objective
This test case verifies that the region item of data element birth_place has only UTF-8 characters, and maximal length of 150 characters.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.5,    
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.1 (Table 6).  
 ISO/IEC 3166-1

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
The mdoc contains a document with DocType = "eu.europa.ec.eudi.pid.1".

## Preconditions
A. A device retrieval mdoc request was sent to the EUDI wallet, to retrieve the document with DocType = "eu.europa.ec.eudi.pid.1". 
B. All mandatory data elements within nameSpace "eu.europa.ec.eudi.pid.1" and all data elements indicated as present in the ICS were requested. 
C. The device retrieval mdoc response was retrieved. 
D. The presence of the item `region` in data element birth_place in the device retrieval mdoc response was verified.

## Test Scenario
1. Verify that the value of the data element `region` in map place_of_birth 2. Check the length of the  `region` value in map place_of_birth.

## Expected results
1. Values includes only UTF-8 characters. 2. Length is equal or smaller tjam 150 characters.