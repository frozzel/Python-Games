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

flight_search = FlightSearch(flight_data)
flight_search.search_flights()
