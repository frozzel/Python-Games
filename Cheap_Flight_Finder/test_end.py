import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Get the client ID and client secret from the environment variables
client_id = os.getenv("AMADEUS_API_KEY")
client_secret = os.getenv("AMADEUS_API_SECRET")

url = "https://test.api.amadeus.com/v1/security/oauth2/token"

response = requests.post(
    url,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    # data = "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
    data={
        "grant_type": "client_credentials",
        "client_id": f"{client_id}",
        "client_secret": f"{client_secret}"
    }
)
access_token = response.json()['access_token']

print(access_token)  # Print the access token

# print(response.json())  # Print the response as JSON

header = {
    "Authorization": f"Bearer {access_token}"
}

response2 = requests.get(url="https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes=BA", headers=header)

print(response2.json())  # Print the response as JSON