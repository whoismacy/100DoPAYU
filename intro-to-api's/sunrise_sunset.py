import requests
import datetime as dt
from dotenv import load_dotenv

lat = 21.292066
long = 86.821945

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
position = (data['iss_position']['longitude'], data['iss_position']['latitude'])
print(position)

parameters = {
    "lat": lat,
    "lng": long,
    "formatted": 0,
}

action = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
action.raise_for_status()
data = action.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

now = dt.datetime.now()
print(sunrise, sunset)
