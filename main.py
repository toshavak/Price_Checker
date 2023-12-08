import requests

def get_crypto_price(symbol):
     """
     Gets the current price of a cryptocurrency by its symbol.

     Args:
         symbol (str): Cryptocurrency symbol (e.g. "BTC", "ETH").

     Returns:
         float: Current price of the cryptocurrency.
     """
     base_url = "https://api.coingecko.com/api/v3/simple/price"
     params = {"ids": symbol, "vs_currencies": "usd"}

     response = requests.get(base_url, params=params)

     if response.status_code == 200:
         data = response.json()
         if symbol.lower() in data and "usd" in data[symbol.lower()]:
             return data[symbol.lower()]["usd"]
     else:
         print(f"Failed to fetch data. Status code: {response.status_code}")

     return None

# Usage example
crypto_symbol = "BTC"
crypto_price = get_crypto_price(crypto_symbol)

if crypto_price is not None:
     print(f"Current price of {crypto_symbol}: ${crypto_price}")
else:
     print(f"Failed to fetch the price of {crypto_symbol}")
