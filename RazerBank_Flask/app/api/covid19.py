import requests
import json

def getCovid19_WorldStats():
  url = 'https://covid19.mathdro.id/api'

  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers)
  # print(response.text.encode('utf8'))
  # reponse = response.json()
  # print(response.json()) # convert to DICT type

  response_JSON = response.json()
  # print('Confirmed: ' +str(response_JSON['confirmed']['value']))
  # print('Deaths: '+ str(response_JSON['deaths']['value']))
  # print('Recovered: '+ str(response_JSON['recovered']['value']))


# print(type(response))