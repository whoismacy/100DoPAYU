import time
import requests
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("email")
recipient = os.getenv("recipient")
password = os.getenv("password")

MY_LAT = 81.292066
MY_LONG = 96.821945

def is_iss_overhead():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        iss_data = response.json()

        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_longitude = float(iss_data["iss_position"]["longitude"])

        return (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5)
    except(requests.RequestException, ValueError) as e:
        print(f"Error checking iss location: {e}")
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_it_nighttime():
    time_now = dt.datetime.now()
    try:
        action = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        action.raise_for_status()
        data = action.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        return sunset <= time_now <= sunrise
    except(requests.RequestException, ValueError) as e:
        print(f"Error getting Sunrise and Sunset time: {e}")
        return False

while True:
    if is_iss_overhead() and is_it_nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs=recipient,
                                msg="Subject:ISS is Overhead\n\nThe ISS is right above you my guy.")
    time.sleep(60)
