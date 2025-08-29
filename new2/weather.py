import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(response.text)  # Add this line to see the raw response
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    CITY = "Pulwama,kashmir"
    get_weather(CITY, API_KEY)