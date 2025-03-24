from amadeus import Client, Location, ResponseError
from dotenv import load_dotenv
import os
load_dotenv()



amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET"), 
)
try:
    '''
    What's the airline name for the IATA code BA?
    '''
    response = amadeus.reference_data.airlines.get(airlineCodes='BA')
    print(response.data)

except ValueError as e:
    print("VALUE", e)
except ResponseError as error:
    print("RESPONSE",  error)