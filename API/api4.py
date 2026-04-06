'''Display the Geo details with the given IP address. ip-api.com API'''
import requests

def get_geo_details(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching geo details for {ip_address}: {e}")
        return None

def main():
    ip_address = input("Enter IP address: ")
    geo_details = get_geo_details(ip_address)
    if geo_details:
        print("Geo Details:")
        for key, value in geo_details.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()