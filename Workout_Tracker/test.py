import requests
from dotenv import load_dotenv
import os
load_dotenv()

header = {
    "Authorization": f"Bearer {os.getenv('SHEETY_API_KEY')}"
}
data = {
    "workout": {
        "date": "Monday",
        "time": "08:00:00",
        "exercise": "Push-ups",
        "duration": "20",
        "calories": "100"
    }
}
response = requests.post('https://api.sheety.co/4405a332b998aff756b6487fee262faf/myWorkouts/workouts', json=data,  headers=header)

response.raise_for_status()

data = response.json()

print(data)