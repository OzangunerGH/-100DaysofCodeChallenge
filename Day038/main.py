#Importing necessary libraries.

import os
import requests
from datetime import datetime

# Environment variables for authentication to APIs used.
APP_ID = os.environ.get("NUTX_APP_ID")
APP_KEY = os.environ.get("NUTX_APP_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTHORIZATION")

#Endpoints and headers of APIs to access and authenticate.
nutx_headers = {
                "x-app-id": APP_ID,
                "x-app-key": APP_KEY
                }

sheety_headers = {"Authorization": SHEETY_AUTH}



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = f"https://api.sheety.co/921c401760af4d4900e7bbef42e3d484/workoutTracking/workouts"


#Asking user to input the activity/exercise to log it.

exercise_input = input("Put in your exercise details.\n(Example: Ran 3kms, cycled 32kms etc.)")

# Passing in necessary parameters, and some optional ones to more accurately calculate the calories burned.
exercise_params = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 74,
    "height_cm": 175,
    "age": 30
}

# Posting the data entered by user to nutritionx to get data regarding activity.
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=nutx_headers)
response.raise_for_status()
exercise_result = response.json()



# Formatting the data received from Nutritionx in correct format to post it into Google Sheets with Sheety.

today = datetime.today().strftime("%d/%m/%Y")
hour = datetime.now().strftime("%H:%M:%S")

exercise_data = exercise_result["exercises"][0]

duration = round(exercise_data["duration_min"])
exercise = exercise_data["name"].capitalize()
calories = round(exercise_data["nf_calories"])






# Passing the necessary parameters to push the data from Nutritionx to Google Sheets via Sheety.
sheety_parameters = {"workout": {
                          "date": today,
                          "time": hour,
                          "exercise": exercise,
                          "duration": duration,
                          "calories": calories
                          }
              }

#Posting the data to Google Sheets.
post_exercise = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
response.raise_for_status()
