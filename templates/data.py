import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return data

def present_temperature(data):
    current_temp = data.get('current', {}).get('temperature_2m', 'No data')
    hourly_temps = data.get('hourly', {}).get('temperature_2m', 'No data')
    
    print(f"Current Temperature: {current_temp}")
    print("Hourly Temperatures:")
    for temp in hourly_temps:
        print(temp)

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    present_temperature(weather_data)