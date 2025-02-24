from dotenv import load_dotenv
import os, requests
from datetime import datetime as dt

load_dotenv()

nutritionix_api = os.environ.get("NUTRITIONIX_API_KEY")
nutritionix_appid = os.environ.get("NUTRITIONIX_APP_ID")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_header = {
    "x-app-id": nutritionix_appid,
    "x-app-key": nutritionix_api,
}

nutritionix_params = {
    "query": input("What exercise did you do today ? "),
    "weight_kg": 70,
    "height_cm": 172,
    "age": 20
}

try:
    action = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_header)
except Exception as e:
    print(f"Error accessing nutritionix api {e}")
else:
   data = action.json()

sheety_endpoint = "https://api.sheety.co/5499ed2ea52869af395ed000aabbfe81/workouts/sheet1"

for i in range(len(data["exercises"])):
    exercise = data['exercises'][i]['user_input']
    duration = data['exercises'][i]['duration_min']
    calories = data['exercises'][i]['nf_calories']
    time = dt.now().strftime("%H:%M:%S")
    date = dt.now().strftime("%Y-%m-%d")
    met = data['exercises'][i]['met']

    sheety_params = {
        "sheet1": {
            "exercise": exercise,
            "duration": f"{duration} kilometres" if exercise == "ran" else f"{duration} minutes",
            "calories": calories,
            "met Value": met,
            "time": time,
            "date": date,
        }
    }
    try:
        sheety_action = requests.post(sheety_endpoint, json=sheety_params)
        # sheety_action = requests.delete(sheety_endpoint)
        sheety_action.raise_for_status()
    except Exception as e:
        print(f"Error while connecting with Sheety API: {e}")


