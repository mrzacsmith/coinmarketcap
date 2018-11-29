import json
import requests

ticker_specific_url = 'https://api.coinmarketcap.com/v2/ticker/1/'

request = requests.get(ticker_specific_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
