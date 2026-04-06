import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import urlopen

try:
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False

REST_COUNTRIES_API = "https://restcountries.com/v3.1"

def fetch_all_country_names() -> list[str]:
    """Fetch all country names to use for autocompletion."""
    url = f"{REST_COUNTRIES_API}/all?fields=name"
    try:
        with urlopen(url, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
            names = []
            for country in data:
                common = country.get("name", {}).get("common")
                if common:
                    names.append(common)
            return sorted(names)
    except Exception:
        return []

def fetch_country_info(country_name: str, exact_match: bool = True) -> list:
    """Fetch country information from the REST Countries API.
    Uses exact match by default parameter using `?fullText=true`.
    """
    encoded_name = quote(country_name)
    url = f"{REST_COUNTRIES_API}/name/{encoded_name}"
    
    if exact_match:
        url += "?fullText=true"
        
    try:
        with urlopen(url, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        if exc.code == 404:
            raise ValueError(f"Country '{country_name}' not found.")
        raise RuntimeError(f"HTTP error {exc.code} for URL: {url}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError("Failed to parse JSON response") from exc

def main() -> None:
    if len(sys.argv) > 1:
        country_name = " ".join(sys.argv[1:])
    else:
        if PROMPT_TOOLKIT_AVAILABLE:
            print("Fetching country list for suggestions...")
            country_names = fetch_all_country_names()
            if country_names:
                country_completer = WordCompleter(country_names, ignore_case=True, match_middle=True)
                print("Start typing to search for a country (Use Tab/Arrows to select):")
                country_name = prompt("> ", completer=country_completer).strip()
            else:
                country_name = input("Enter country name: ").strip()
        else:
            country_name = input("Enter country name: ").strip()

    if not country_name:
        print("No input provided. Exiting.")
        return

    try:
        # Using exact match api flag
        results = fetch_country_info(country_name, exact_match=True)
        country_data = results[0]
        
        # Parse output data
        name = country_data.get("name", {}).get("common", "N/A")
        official_name = country_data.get("name", {}).get("official", "N/A")
        capitals = ", ".join(country_data.get("capital", ["N/A"]))
        region = country_data.get("region", "N/A")
        subregion = country_data.get("subregion", "N/A")
        
        population = country_data.get("population", "N/A")
        if isinstance(population, (int, float)):
            population = f"{population:,}"
            
        area = country_data.get("area", "N/A")
        if isinstance(area, (int, float)):
            area = f"{area:,} km²"
            
        languages_dict = country_data.get("languages", {})
        languages = ", ".join(languages_dict.values()) if languages_dict else "N/A"
        
        currencies_dict = country_data.get("currencies", {})
        currencies = ", ".join(
            [f"{c.get('name', '')} ({c.get('symbol', '')})" 
            for c in currencies_dict.values()]
        ) if currencies_dict else "N/A"

        print(f"\nCountry Information for: {name}")
        print("-" * 40)
        print(f"Official Name: {official_name}")
        print(f"Capital:       {capitals}")
        print(f"Region:        {region} ({subregion})")
        print(f"Population:    {population}")
        print(f"Area:          {area}")
        print(f"Languages:     {languages}")
        print(f"Currencies:    {currencies}")
        
    except Exception as exc:
        print(f"\nError: {exc}")

if __name__ == "__main__":
    main()
    