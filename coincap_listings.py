import json
import requests


listings_url = 'https://api.coinmarketcap.com/v2/listings/'
request = requests.get(listings_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))