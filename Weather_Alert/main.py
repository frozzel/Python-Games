from dotenv import load_dotenv
load_dotenv()
import requests
import smtplib
import os


API_KEY = os.getenv("weather_api_key")
MY_LAT = os.getenv("Latitude")
MY_LONG = os.getenv("Longitude")
URL = "https://api.openweathermap.org/data/2.5/forecast"

my_email = os.getenv("EMAIL")
my_password =  os.getenv("PASSWORD")
send_to_email = os.getenv("CLOUD")

def send_email(quote):
    with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=send_to_email, 
                    msg=f"Subject:Quote of The Day!\n\n{quote}")

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

will_rain = False
for dt in weather_data["list"]:
    if dt["weather"][0]["id"] < 700:
        will_rain = True
        
if not will_rain:
    send_email("Don't Bring an umbrella!")

