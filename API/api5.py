import requests
import os
import sys

# Here we provide a free, default hardcoded api key.
API_KEY = os.environ.get("NEWS_API_KEY", "1054e3a4f230464bbd151ac3b611d21f")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_top_headlines(country="us", category="general", limit=10):
    """Fetches top headlines from NewsAPI."""
    params = {
        "country": country,
        "category": category,
        "pageSize": limit,
        "apiKey": API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return []
            
        return data.get("articles", [])
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to NewsAPI: {e}")
        return []

def main():
    categories = {
        '1': 'general',
        '2': 'business',
        '3': 'technology',
        '4': 'science',
        '5': 'sports',
        '6': 'entertainment',
        '7': 'health'
    }

    while True:
        print("\n=== Top News Headlines Fetcher ===")
        for key, value in categories.items():
            print(f"{key}. {value.title()}")
        print("8. Exit")
        
        choice = input("Select a news category (1-8): ").strip()
        
        if choice == '8':
            print("Exiting...")
            break
        elif choice in categories:
            category = categories[choice]
            print(f"\nFetching top {category} headlines...")
            
            articles = fetch_top_headlines(category=category)
            if not articles:
                continue
                
            print("\n" + "="*80)
            for i, article in enumerate(articles, start=1):
                title = article.get("title", "No Title")
                source = article.get("source", {}).get("name", "Unknown Source")
                author = article.get("author") or "Unknown Author"
                
                print(f"{i}. {title}")
                print(f"   Source: {source} | Author: {author}")
                print(f"   Read more: {article.get('url')}")
                print("-" * 80)
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
