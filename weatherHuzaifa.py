import requests

def get_weather(city_name, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city_name,
        'aqi': 'no'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200 or 'error' in data:
            print("Error:", data.get("error", {}).get("message", "Something went wrong."))
            return

        city = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        condition = data['current']['condition']['text']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp_c}°C / {temp_f}°F")
        print(f"Condition: {condition}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("--- WeatherCLI ---")
    city = input("Enter city name: ")
    api_key = input("Enter your WeatherAPI.com API key: ")
    get_weather(city, api_key)
