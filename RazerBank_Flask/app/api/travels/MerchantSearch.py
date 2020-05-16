import requests
from requests.auth import HTTPBasicAuth
import json
from app.api.travels.visaConfig import *

body = {
    "searchAttrList": {
        "merchantName": "STARBUCKS",
        "merchantCity": "SAN FRANCISCO",
        "merchantState": "CA",
        "merchantPostalCode": "94127",
        "merchantCountryCode": "840"
    },
    "responseAttrList": [
        "GNSTANDARD"
    ],
    "searchOptions": {
        "wildCard": [
            "merchantName"
        ],
        "maxRecords": "5",
        "matchIndicators": "true",
        "matchScore": "true",
        "proximity": [
            "merchantName"
        ]
    },
    "header": {
        "requestMessageId": "Request_001",
        "startIndex": "0",
        "messageDateTime": "2020-05-15T18:47:27.903"
    }
}

url = "https://sandbox.api.visa.com/merchantsearch/v1/search"

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

def checkMerchantSearch():
    body = {
        "searchAttrList": {
            "merchantName": "STARBUCKS",
            "merchantCity": "SAN FRANCISCO",
            "merchantState": "CA",
            "merchantPostalCode": "94127",
            "merchantCountryCode": "840"
        },
        "responseAttrList": [
            "GNSTANDARD"
        ],
        "searchOptions": {
            "wildCard": [
                "merchantName"
            ],
            "maxRecords": "5",
            "matchIndicators": "true",
            "matchScore": "true",
            "proximity": [
                "merchantName"
            ]
        },
        "header": {
            "requestMessageId": "Request_001",
            "startIndex": "0",
            "messageDateTime": "2020-05-15T18:47:27.903"
        }
    }
    
    response = requests.request("POST", url, headers=headers, auth=HTTPBasicAuth('VTT095H3IAKYE9IB2QHJ21i2RLnD_iVYx8qwJurINP8bBJzbk', 'ox77y1TivzPgTiHHO3R'), verify=SSLcertfile_path, cert=(certfile_path,key_path), data = json.dumps(body))
    print(response.text.encode('utf8'))
    return response.text.encode('utf8')

checkMerchantSearch()
