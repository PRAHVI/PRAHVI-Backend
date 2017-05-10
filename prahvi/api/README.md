## PRAHVI API Endpoints

|           Endpoint           |        Input (subject to change)       |                 Output                 | HTTP METHOD |                                     Description                                    |
|:----------------------------:|:--------------------------------------:|:--------------------------------------:|:-----------:|:----------------------------------------------------------------------------------:|
| <domain>/api/v1/image/ocr3   | File: Image                            | JSON: { result: string }               | POST        | Prahvi's image to text algorithm using tesseract 3                                 |
| <domain>/api/v1/image/ocr4   | File: Image                            | JSON: { result: string }               | POST        | Prahvi's image to text algorithm using tesseract 4                                 |
| <domain>/api/v1/text/tfidf   | JSON: { text: string }                 | JSON: { result: { term: score, ... } } | POST        | Takes in a document string and outputs the scores of all the terms in the document |
| <domain>/api/v1/text/compare | JSON: { text1: string, text2: string } | JSON: { result: int[0, 1] }            | POST        | Returns a score of how similar the documents are.                                  |


## Sample Curl Queries

### OCR
```
curl -F image=@<path/to/image> http://174.62.109.150/api/v1/image/ocr3/
```

```
curl -F image=@<path/to/image> http://174.62.109.150/api/v1/image/ocr4/
```



### TFIDF
```
curl -H "Content-Type: application/json" -X POST -d '{"text":"This is a sample sentence"}' http://174.62.109.150/api/v1/text/tfidf/
```

### Text Comparison
```
curl -H "Content-Type: application/json" -X POST -d '{"text1":"This is a sample sentence", "text2": "Also a test sentence"}' http://174.62.109.150/api/v1/text/compare/
```

