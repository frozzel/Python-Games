import requests
import os
from dotenv import load_dotenv
load_dotenv()

def make_gapi_request():
    api_key = os.getenv("GOLD_API_KEY")
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        print(result.get("price"))
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

make_gapi_request()
