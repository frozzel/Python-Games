#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

# Get the client ID and client secret from the environment variables
client_id = os.getenv("AMADEUS_API_KEY")
client_secret = os.getenv("AMADEUS_API_SECRET")
url = "https://test.api.amadeus.com/v1/security/oauth2/token"


print("Welcome to the Flight Club!")
print("We find the best flight deals and email them to you.")
data = DataManager()
flight_data = data.get_flights()

print(flight_data)

flight_search = FlightSearch(flight_data)
flight_search.search_flights()


# def search_flights():
#      # Get Authorization from Amadeus API token
     
#      token_response = requests.post(
#             url,
#             headers={"Content-Type": "application/x-www-form-urlencoded"},
#             data={
#                 "grant_type": "client_credentials",
#                 "client_id": f"{client_id}",
#                 "client_secret": f"{client_secret}"
#             }
#         )
#      access_token = token_response.json()['access_token']
     
#      # Search for flight deals
#      header = {
#          "Authorization": f"Bearer {access_token}"
#      }
     
#      today = datetime.today()
#      future_date = today + timedelta(weeks=2)
     
#      formatted_date = future_date.strftime("%Y-%m-%d")
#      print(formatted_date)
     
#      for price in sheet_data["prices"]:
#         print(price)
#         parameters = {
#             "originLocationCode": "ATL",
#             "destinationLocationCode": price["iataCode"],
#             "departureDate": formatted_date,
#             "adults": 1,
#             "currencyCode": "USD",
#             "maxPrice": price["lowestPrice"]
#         }
#         print(parameters)
#         response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=header, params=parameters)
#         # response.raise_for_status()
#         data = response.json()
#         if len(data["data"]) > 0:
#             print(data["data"][0]["price"])
#         else: 
#             print("No flights found")

# search_flights()