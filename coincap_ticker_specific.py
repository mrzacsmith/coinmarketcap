import json
import requests

convert = 'USD'

listings_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listings_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
ticker_url_pairs = {}

for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print(ticker_url_pairs)

# ticker_specific_url = 'https://api.coinmarketcap.com/v2/ticker/1/'

# request = requests.get(ticker_specific_url)
# results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))
