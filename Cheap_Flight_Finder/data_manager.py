import requests
from dotenv import load_dotenv
import os
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = {
            "Authorization": f"Basic {os.getenv('SHEETY_API_KEY')}"
        }
        self.data = {}
        
    def get_users(self):
        response = requests.get('https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/users', headers=self.header)
        response.raise_for_status()
        self.data = response.json()
        return self.data
    
    def get_flights(self):
        response = requests.get('https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/prices', headers=self.header)
        response.raise_for_status()
        self.data = response.json()
        return self.data