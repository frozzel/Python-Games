from dotenv import load_dotenv
load_dotenv()
import requests
import smtplib
import datetime
import os


API_KEY = os.getenv("weather_api_key")
MY_LAT = os.getenv("Latitude")
MY_LONG = os.getenv("Longitude")
URL = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "imperial",
    "cnt": 4,
}

response = requests.get(URL, params=weather_params)

response.raise_for_status()

weather_data = response.json()

for dt in weather_data["list"]:
    print(dt["dt_txt"])
    print(dt["main"]["temp"])
    print(dt["weather"][0]["description"])
    if dt["weather"][0]["id"] < 700:
        print("Bring an umbrella!")
    elif dt["weather"][0]["id"] > 700:
        print("Don't bring an umbrella")
        
    print("------")
    
# print(weather_data)
