from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

coinmarketcap_api = os.getenv('COINMARKETCAP_API')
class Crypto:

    def get_top_5(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':'5',
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          #'X-CMC_PRO_API_KEY': 'enter-your-api-key-here',
          'X-CMC_PRO_API_KEY': coinmarketcap_api,
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']

    def get_top_10(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':'10',
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          #'X-CMC_PRO_API_KEY': 'enter-your-api-key-here',
          'X-CMC_PRO_API_KEY': coinmarketcap_api,
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']

