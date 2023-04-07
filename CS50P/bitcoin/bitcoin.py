import requests
import sys

try:
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = float(data.json()['bpi']['USD']['rate_float'])
    if len(sys.argv) == 2:
            print(f'${float(sys.argv[1]) * price:,.4f}')
            sys.exit()
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')