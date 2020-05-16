import requests
from requests.auth import HTTPBasicAuth
import json

def getLoanProducts():
  url = 'https://razerhackathon.sandbox.mambu.com/api/loanproducts'

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, auth=HTTPBasicAuth('Team50','pass95C660F15'))

  response_JSON = response.json()
  # print(response_JSON)
  # print(len(response_JSON))
  print(response_JSON[0]['productName'])
  print(response_JSON[1]['productName'])

  # print(response.text.encode('utf8'))

