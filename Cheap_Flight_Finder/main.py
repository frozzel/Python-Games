#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


print("Welcome to the Flight Club!")
print("We find the best flight deals and email them to you.")
data = DataManager()
sheet_data = data.get_flights()
print(sheet_data)