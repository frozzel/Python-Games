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


print(response.json())  # Print the response as JSON
