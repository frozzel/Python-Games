import requests
from datetime import datetime
from config import send_email


MY_LAT = 33.952602 # Your latitude
MY_LONG = -84.549934 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5) and (time_now.hour >= sunset or time_now.hour <= sunrise):
    send_email(f"Subject:Look up!\n\n The ISS is close to your current position.")
    
else:
    send_email(f"Subject:Look up!\n\n The ISS is not close to your current position.")
    

