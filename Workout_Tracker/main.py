import requests
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime
from datetime import date

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
    save_data = {
        "workout": {
            "date": date.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data["exercises"][0]["name"],
            "duration": data["exercises"][0]["duration_min"],
            "calories": data["exercises"][0]["nf_calories"]
        }
    }
    header = {
        "Authorization": f"Bearer {os.getenv('SHEETY_API_KEY')}"
    }
    response = requests.post('https://api.sheety.co/4405a332b998aff756b6487fee262faf/myWorkouts/workouts', json=save_data,  headers=header)
    response.raise_for_status()
    data2 = response.json()
    
    print(data2)
    
get_exercise_data()
    
    