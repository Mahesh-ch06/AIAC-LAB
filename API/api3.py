import requests

def get_supported_currencies():
    """Fetches the list of supported fiat currencies."""
    url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except:
        # Fallback list if API fails
        return ["usd", "inr", "eur", "gbp", "jpy", "cad", "aud"]

def get_top_cryptos(limit=10, currency="usd"):
    """
    Fetches the top N cryptocurrencies by market cap using the CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            print("Rate limit exceeded. Please wait a moment and try again.")
        else:
            print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to CoinGecko API: {e}")
        return None

def get_crypto_price(crypto_id, currency):
    """Fetches the price of a specific cryptocurrency."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_id.lower(),
        "vs_currencies": currency.lower()
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if crypto_id.lower() in data:
            return data[crypto_id.lower()][currency.lower()]
        return None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def display_prices(coins, currency):
    """
    Formats and prints the cryptocurrency data.
    """
    if not coins:
        return
        
    print("\n" + "="*70)
    print(f"{'Rank':<5} | {'Name':<20} | {'Symbol':<8} | {'Price ('+currency.upper()+')':>20}")
    print("="*70)
    
    for coin in coins:
        rank = coin.get('market_cap_rank', 'N/A')
        name = coin.get('name', 'Unknown')
        symbol = coin.get('symbol', '').upper()
        price = coin.get('current_price', 0.0)
        
        # Print formatted row
        print(f"{rank:<5} | {name:<20} | {symbol:<8} | {price:>20,.6f}")
    print("="*70 + "\n")

def main():
    supported_currencies = get_supported_currencies()
    
    while True:
        print("\n--- Cryptocurrency & Fiat Converter ---")
        print("1. View Top 10 Cryptocurrencies in a specific fiat")
        print("2. View Top 50 Cryptocurrencies in a specific fiat")
        print("3. Convert Crypto to Fiat (e.g., Bitcoin to INR)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice in ['1', '2']:
            limit = 10 if choice == '1' else 50
            fiat = input(f"Enter target currency (e.g., usd, inr, eur): ").lower()
            if fiat not in supported_currencies:
                print(f"Warning: '{fiat}' might not be supported. Using 'usd' as fallback.")
                fiat = "usd"
            
            print(f"\nFetching current prices in {fiat.upper()}...")
            coins = get_top_cryptos(limit, currency=fiat)
            display_prices(coins, fiat)
            
        elif choice == '3':
            crypto = input("Enter cryptocurrency ID (e.g., bitcoin, ethereum, dogecoin): ").lower()
            fiat = input("Enter target fiat currency (e.g., usd, inr, eur): ").lower()
            amount_str = input(f"Enter amount of {crypto.title()}: ")
            
            try:
                amount = float(amount_str)
                price = get_crypto_price(crypto, fiat)
                if price is not None:
                    total = amount * price
                    print(f"\n✅ {amount} {crypto.title()} = {total:,.2f} {fiat.upper()}")
                    print(f"   (Current rate: 1 {crypto.title()} = {price:,.6f} {fiat.upper()})")
                else:
                    print(f"\n❌ Could not find data for '{crypto}' or currency '{fiat}'. Make sure the ID is correct (e.g., 'bitcoin' not 'btc').")
            except ValueError:
                print("\n❌ Invalid amount entered. Please enter a number.")
                
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
