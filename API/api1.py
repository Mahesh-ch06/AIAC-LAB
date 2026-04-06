import requests

def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            return result["latitude"], result["longitude"], result["name"], result.get("country", "")
    return None, None, None, None

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def main():
    city = input("Enter a city name: ")
    lat, lon, name, country = get_coordinates(city)
    
    if lat is None or lon is None:
        print(f"Could not find coordinates for {city}.")
        return

    print(f"\nFound location: {name}, {country} (Lat: {lat}, Lon: {lon})")
    
    weather_data = get_weather(lat, lon)
    if weather_data and "current" in weather_data:
        current = weather_data["current"]
        units = weather_data["current_units"]
        
        temp = current["temperature_2m"]
        temp_unit = units["temperature_2m"]
        
        humidity = current["relative_humidity_2m"]
        humidity_unit = units["relative_humidity_2m"]
        
        wind_speed = current["wind_speed_10m"]
        wind_speed_unit = units["wind_speed_10m"]
        
        print(f"\nCurrent Weather in {name}:")
        print(f"Temperature: {temp} {temp_unit}")
        print(f"Humidity: {humidity}{humidity_unit}")
        print(f"Wind Speed: {wind_speed} {wind_speed_unit}")
    else:
        print("Could not fetch weather data.")

if __name__ == "__main__":
    main()
