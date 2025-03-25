import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime, timedelta
import json


# Get the client ID and client secret from the environment variables
client_id = os.getenv("AMADEUS_API_KEY")
client_secret = os.getenv("AMADEUS_API_SECRET")
url = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        self.data = data
    
    def search_flights(self):
        print("Searching for flights...")
        # Get Authorization from Amadeus API token
        token_response = requests.post(
            url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": f"{client_id}",
                "client_secret": f"{client_secret}"
            }
        )
        
        if token_response.status_code != 200:
            print("Error getting access token:", token_response.json())
            return

        access_token = token_response.json()['access_token']
        
        # Search for flight deals
        header = {
            "Authorization": f"Bearer {access_token}",
            'Content-Type': 'application/json'

        }
        
        today = datetime.today()
        future_date = today + timedelta(weeks=2)
        formatted_date = future_date.strftime("%Y-%m-%d")

        for price in self.data.get("prices", []):
            
            parameters = {
                "currencyCode": "USD",
                "originDestinations": [
                    {
                        "id": "1",
                        "originLocationCode": "ATL",
                        "destinationLocationCode": price["iataCode"],
                        "departureDateTimeRange": {
                            "dateWindow": "P6M",  # 6-month period; adjust as needed
                            "date": formatted_date,
                        }
                    },
 
                ],
                "travelers": [
                    {
                        "id": "1",
                        "travelerType": "ADULT",
   
                    }
                ],
                "sources": [
                    "GDS"
                ],
                "searchCriteria": {
                    "maxFlightOffers": 1,
                    "flightFilters": {
                "maxPrice": price["lowestPrice"]  # Filter by max price
            }
  
                }
            }

            response = requests.post(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=header, data=json.dumps(parameters))
            # response.raise_for_status()
            data = response.json()
            
            print(data)

            # if len(data["data"]) > 0:
            #     print(f"Flights found for {price['city']}:")
            #     print(data["data"][0]["price"])
            # else:
            #     print("No flights found.")