import requests


def get_crypto_price(crypto_id):
    crypto_id = crypto_id.strip().lower()
    if not crypto_id:
        return "invalid", None

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "usd"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return "error", None

    price = data.get(crypto_id, {}).get("usd")
    if price is None:
        return "invalid", None

    return "ok", price


def main():
    crypto_id = input("Enter cryptocurrency ID: ")
    status, price = get_crypto_price(crypto_id)

    if status == "error":
        print("Service temporarily unavailable")
    elif status == "invalid":
        print("Invalid cryptocurrency")
    else:
        print(f"Current price of {crypto_id.strip().lower()} in USD: ${price}")


if __name__ == "__main__":
    main()
