# Cryptocurrency Price Checker

A simple Python script for fetching the current price of a cryptocurrency using the CoinGecko API.

## 📝 Description

This script demonstrates how to retrieve the current price of a cryptocurrency by providing its symbol. It utilizes the CoinGecko API, which offers real-time cryptocurrency data.

## 🚀 Features

- Fetches the current price of a cryptocurrency.
- Supports various cryptocurrency symbols (e.g., BTC, ETH).
- Utilizes the CoinGecko API for accurate and up-to-date data.

## ⚙️ Usage

1. Ensure that you have the `requests` library installed:

    ```bash
    pip install requests
    ```

2. Run the script:

    ```bash
    python crypto_price_checker.py
    ```

3. Enter the cryptocurrency symbol when prompted.

## 📄 Example

```python
# Example usage
crypto_symbol = input("Enter the cryptocurrency symbol (e.g., BTC, ETH): ")
crypto_price = get_crypto_price(crypto_symbol)

if crypto_price is not None:
    print(f"Current price of {crypto_symbol}: ${crypto_price}")
else:
    print(f"Failed to fetch the price of {crypto_symbol}")
```
