import requests
import os
from dotenv import load_dotenv
load_dotenv()

header = {
    "Authorization": f"Bearer {os.getenv('AMADEUS_ACCESS_TOKEN')}"
}

response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes=BA", headers=header)

print(response.json())  # Print the response as JSON