import requests
from requests.auth import HTTPBasicAuth
import json
from app.api.travels.visaConfig import *

url = 'https://sandbox.api.visa.com/travelnotificationservice/v1/travelnotification/itinerary'


def addItinerary(userId, countryCode, state, cardAccountNumber):
  body = {
    "addTravelItineraryResponse": {
        "travelItinerary": {
            "partnerBid": "10074101",
            "travelItineraryId": "118202",
            "userId": "melvyn",
            "primaryAccountNumbers": [
                {
                    "cardAccountNumber": "4121254490072441"
                },
                {
                    "cardAccountNumber": "4121254490072442"
                }
            ],
            "destinations": [
                {
                    "country": "840",
                    "state": "CA"
                }
            ],
            "departureDate": "2020-05-21",
            "returnDate": "2020-06-28",
            "source": "Cardholder Self-Reported",
            "lastUpdatedBy": "melvyn",
            "lastUpdateTime": "2020-05-16T08:31:46Z"
        },
        "responseCode": "0",
        "responseMessage": "Success Transaction"
    }
  }


def updateItinerary():
  pass

def deleteItinerary():
  pass

def retrieveItinerary():
  pass