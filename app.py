from flask import Flask, render_template

import requests
import html
def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return data

app = Flask(__name__)

@app.route('/')
def home():
    data=fetch_weather_data()
    cas=data['hourly']['time']
    return render_template('index.html',cas=cas,hodnota=data['hourly']['temperature_2m'])

if __name__ == '__main__':
    app.run(debug=True)