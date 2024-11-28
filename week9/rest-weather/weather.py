import requests

# API documentation: https://openweathermap.org/current

# Your OpenWeatherMap API key (replace with your actual API key)
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Define the query parameters
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        weather_data = response.json()
        print(weather_data)
        return {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_info = get_weather(city)

    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
