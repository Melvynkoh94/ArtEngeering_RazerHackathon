import requests
from requests.auth import HTTPBasicAuth
import json


loanProducts = {
  "Term Loan (Small)" : """In Singapore, short term loans are taken by people who need fast cash for various reasons. These are unsecured loans and to qualify for them, you need to have a regular income from sources such as a job or a business. You also need to be a citizen of Singapore, or a foreigner who has the authority to live in Singapore and work as well.

Additionally, the law stipulates that you should be above the age of 21 before you can take a short term loan.""",

"Term Loan (Large)" : """A long-term personal loan is a loan used for big purchases such as a car, boat, complicated surgery or a huge wedding. This guide covers what you need to know before taking up a long term loan in Singapore, including how it works and how to choose the best one for your financial situation.

Borrowers will have a choice between fixed and variable rates with their long-term personal loan. Fixed-rate loans mean steady repayments, but variable rate loans give you more flexibility with your repayments, including being able to make additional repayments and pay back the loan early.""",

"Endowment Plan" : """Unlike investments like shares or deposits, which require only a lump sum payment at the start, endowment plans require you to
continue paying premiums throughout the lifespan of your plan.
These premiums are generally of a fixed amount each time you pay, although you might have the opportunity to increase or reduce your premiums if you make changes to your plan. You may be required to pay every month, quarter, 6 months or year."""
}

def getLoanProducts():
  url = 'https://razerhackathon.sandbox.mambu.com/api/loanproducts'

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, auth=HTTPBasicAuth('Team50','pass95C660F15'))

  response_JSON = response.json()
  for i in range(len(response_JSON)):
    # print(response_JSON[0]['productName'])
    if(response_JSON[i]['productName'] in loanProducts):
      print(response_JSON[i]['productName'])
      print(response_JSON[i]['productName'])

      

  # print(response_JSON[0]['productName'])
  # print(response_JSON[1]['productName'])

  # print(response.text.encode('utf8'))

# smallTermLoan_info = """In Singapore, short term loans are taken by people who need fast cash for various reasons. These are unsecured loans and to qualify for them, you need to have a regular income from sources such as a job or a business. You also need to be a citizen of Singapore, or a foreigner who has the authority to live in Singapore and work as well.

# Additionally, the law stipulates that you should be above the age of 21 before you can take a short term loan."""

# longTermLoan_info = """A long-term personal loan is a loan used for big purchases such as a car, boat, complicated surgery or a huge wedding. This guide covers what you need to know before taking up a long term loan in Singapore, including how it works and how to choose the best one for your financial situation.

# Borrowers will have a choice between fixed and variable rates with their long-term personal loan. Fixed-rate loans mean steady repayments, but variable rate loans give you more flexibility with your repayments, including being able to make additional repayments and pay back the loan early."""

# endowmentPlan_info = """Unlike investments like shares or deposits, which require only a lump sum payment at the start, endowment plans require you to
# continue paying premiums throughout the lifespan of your plan.
# These premiums are generally of a fixed amount each time you pay, although you might have the opportunity to increase or reduce your premiums if you make changes to your plan. You may be required to pay every month, quarter, 6 months or year."""


getLoanProducts()
