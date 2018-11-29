import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'rank'
convert = 'USD'

choice = input("would you like to customize your parameters?: ")

if choice == 'y':
    limit = input("What is the custom limit? ")
    start = input("What is the custom start number? ")
    sort = input("What do you want to sort by? ")  # Sort by rank
    covert = input("What is your local currency? ")
    

ticker_url += '&limit=' + limit + '&start=' + start + '&sort=' + sort + '&convert=' + convert

request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))