import json
import requests

while True:

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'
    
    limit = 100
    start = 1
    sort = 'rank'
    convert = 'USD'
    
    choice = input("Would you like to customize your parameters?: (y/n) ")
    
    if choice == 'y':
        limit = input("What is the custom limit? ")
        start = input("What is the custom start number? ")
        sort = input("What do you want to sort by? ")  # Sort by rank
        covert = input("What is your local currency? ")
        
    
    ticker_url += '&limit=' + str(limit) + '&start=' + str(start) + '&sort=' + sort + '&convert=' + convert
    
    request = requests.get(ticker_url)
    results = request.json()
    
    # print(json.dumps(results, sort_keys=True, indent=4))
    
    data = results['data']
    
    print
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        
        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])
        
        
        quotes = currency['quotes'][convert]
        market_cap = int(quotes['market_cap'])
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']
        
        volume_string = '{:,}'.format(volume)
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)
        
        print
        print(str(rank) + ': ' + name + ' (' + symbol + ')' )
        print('Market cap: \t\t$' + market_cap_string)
        print('Price: \t\t\t$' + str(price))
        print('24h Volume: \t\t$' + volume_string)
        print('Hour change: \t\t' + str(hour_change) + '%')
        print('Day change: \t\t' + str(day_change) + '%')
        print('Week change: \t\t' + str(week_change) + '%')
        print('Total supply: \t\t' + total_supply_string)
        print('Circulating supply: \t' + circulating_supply_string)
        print('Percentage of coins in circulation: ' + str(float(circulating_supply / total_supply * 100)))
        print
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        
    choice = input('Run again? (y/n) ')

    if choice == 'n':
        break
