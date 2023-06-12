import requests
from datetime import datetime
import os

auth = {"Authorization": f"Basic {os.environ['AUTH']}"}

today = datetime.now()
formatted_today = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")


API_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
shetty_Endpoint_get = "https://api.sheety.co/dd1e264de0be2c9529211198af2c3696/myWorkout/workouts"
N_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_Endpoint_post = "https://api.sheety.co/dd1e264de0be2c9529211198af2c3696/myWorkout/workouts"

N_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_query_data = {
    "query": input("what exercises you did ?")
}

response = requests.post(N_ENDPOINT, json=exercise_query_data, headers=N_headers)
exercises_data = response.json()['exercises']
for exercise in exercises_data:
    data_to_put = {
        "workout": {
            "date": formatted_today,
            "time": today_time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']

        }
    }

    response_shetty = requests.post(shetty_Endpoint_post, json=data_to_put, headers=auth)
    print(response_shetty.text)

