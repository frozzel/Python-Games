import requests
from dotenv import load_dotenv
import os
load_dotenv()

APP_ID = os.getenv("NUTRITION_IX_APP_ID")
API_KEY = os.getenv("NUTRITION_IX_APP_KEY")
NUT_DOMAIN = os.getenv("NUTRITION_ENDPOINT")

def get_exercise_data():
    
    exercise_endpoint = f"{NUT_DOMAIN}/v2/natural/exercise"
    
    exercise_text = input("Tell me which exercises you did: ")
    
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    
    exercise_params = {
        "query": exercise_text,
    }
    
    response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
    # response.raise_for_status()
    data = response.json()
    print(data)
    
get_exercise_data()
    
    