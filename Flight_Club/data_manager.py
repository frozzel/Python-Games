import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/users"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.header = {
            "Authorization": f"Basic {os.getenv('SHEETY_API_KEY')}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.header
            )
            # print(response.text)
    def add_user(self, firstname, lastname, email):
        new_data = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }
        response = requests.post(
            url=SHEETY_USER_ENDPOINT,
            json=new_data,
            headers=self.header
        )
        # print(response.text)
        return response.text
    
    def get_users(self):
        response = requests.get(url=SHEETY_USER_ENDPOINT, headers=self.header)
        data = response.json()
        return data["users"]