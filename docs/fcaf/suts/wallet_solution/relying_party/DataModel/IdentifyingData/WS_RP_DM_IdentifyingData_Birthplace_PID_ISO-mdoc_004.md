# EuPid_DM_BirthPlace_04

## Objective
This test case verifies that the value of each data element present inbirth_place is a well-formed CBOR text string.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.5    
“ANNEXES to the COMMISSION IMPLEMENTING REGULATION amending Implementing Regulation (EU) 2024/2977, (EU) 2024/2979, (EU) 2024/2980 and (EU) 2024/2982 as regards applicable standards and specifications and correcting Implementing Regulation (EU) 2024/2980" section 4.1 (Table 6).  
 RFC 7049 section 2.1

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
The EUDI wallet contains a document with DocType = "eu.europa.ec.eudi.pid.1".

## Preconditions
A. A device retrieval mdoc request was sent to the EUDI wallet, to retrieve the document with DocType = "eu.europa.ec.eudi.pid.1". 
B. All mandatory data elements within nameSpace "eu.europa.ec.eudi.pid.1" and all data elements indicated as present in the ICS were requested. 
C. The device retrieval mdoc response was retrieved. 
D. The presence of data element birth_place in the device retrieval mdoc response was verified.

## Test Scenario
For each data item present, perform the following check for the value of the key/value pair: 1. Verify the encoding of the data item value.

## Expected results
1. The major type value is equal to 3.