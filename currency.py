from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Currency:
    def __init__(self, symbol):
        self.symbol = symbol

    def api_call(self):
        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '10',
            'sort': 'market_cap',
            'sort_dir': 'desc'  # Ordenar por capitalización de mayor a menor
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '3bf88cfe-7d3f-42ac-91c6-270905e29b4f',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data['data']  # Retorna la lista de criptomonedas con mayor capitalización
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return None