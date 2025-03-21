from amadeus import Client, ResponseError
from dotenv import load_dotenv
import os
load_dotenv()



amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET")
)
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode="JFK",
        destinationLocationCode="LAX",
        departureDate="2025-04-01",
        adults=1
    )
    print(response.data)
except ResponseError as error:
    print("ERROR",error)