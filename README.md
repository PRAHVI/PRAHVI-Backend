## PRAHVI API Endpoints

|           Endpoint           |        Input (subject to change)       |                 Output                 | HTTP METHOD |                                     Description                                    |
|:----------------------------:|:--------------------------------------:|:--------------------------------------:|:-----------:|:----------------------------------------------------------------------------------:|
| <domain>/api/v1/image/ocr3   | File: Image                            | JSON: { result: string }               | POST        | Prahvi's image to text algorithm using tesseract 3                                 |
| <domain>/api/v1/image/ocr4   | File: Image                            | JSON: { result: string }               | POST        | Prahvi's image to text algorithm using tesseract 3                                 |
| <domain>/api/v1/text/tfidf   | String                                 | JSON: { result: { term: score, ... } } | POST        | Takes in a document string and outputs the scores of all the terms in the document |
| <domain>/api/v1/text/compare | JSON: { text1: string, text2: string } | JSON: { result: int[0, 1] }            | POST        | Returns a score of how similar the documents are.                                  |
