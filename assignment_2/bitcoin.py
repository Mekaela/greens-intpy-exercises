'''Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy.
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.'''

# expects two command line arguments, e.g. python bitcoin.py 1.5
import requests
import sys

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    try:
        data = fetch_bitcoin_price()
        usd_rate = data.get('bpi')['USD']['rate_float']
        user_input = get_user_amount()
        print('${:,.4f}'.format(calculate_value(user_input, usd_rate)))
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except ValueError:
        print('Input not a valid float value')
        sys.exit(1)
    except IndexError:
        print('Missing required argument: Please provide an amount to convert')
        sys.exit(1)

def fetch_bitcoin_price():
    response = requests.get(API_URL)
    return response.json()

def get_user_amount():
    user_input = sys.argv[1]
    return float(user_input)

def calculate_value(amount, price):
    return amount * price

main()