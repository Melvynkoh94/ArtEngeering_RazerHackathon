import requests
from requests.auth import HTTPBasicAuth
import json
from app.api.config import *

#######################
SSLcertfile_path = 'C:/Users/User/Downloads/DigiCertGlobalRootCA.cer'
certfile_path = 'C:/Users/User/Downloads/cert.pem'
key_path = 'C:/Users/User/Downloads/key_6638c4a9-ca6f-4196-91fb-23e4dd7a5ec2.pem'

body = {
    "destinationCurrencyCode": "156",
    "markUpRate": "1",
    "retrievalReferenceNumber": "201010101031",
    "sourceAmount": "100",
    "sourceCurrencyCode": "702",
    "systemsTraceAuditNumber": "350421"
}
#######################


url = "https://sandbox.api.visa.com/forexrates/v1/foreignexchangerates"

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, auth=HTTPBasicAuth('VTT095H3IAKYE9IB2QHJ21i2RLnD_iVYx8qwJurINP8bBJzbk', 'ox77y1TivzPgTiHHO3R'), verify=SSLcertfile_path, cert=(certfile_path,key_path), data = json.dumps(body))

def checkFXRates():
  response = requests.request("POST", url, headers=headers, auth=HTTPBasicAuth('VTT095H3IAKYE9IB2QHJ21i2RLnD_iVYx8qwJurINP8bBJzbk', 'ox77y1TivzPgTiHHO3R'), verify=SSLcertfile_path, cert=(certfile_path,key_path), data = json.dumps(body))
  print(response.text.encode('utf8'))
  return response.text.encode('utf8')
