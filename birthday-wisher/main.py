"""A simple python script that sends birthday messages to loved ones."""
import datetime as dt
import os
import smtplib
import random
import pandas
from dotenv import load_dotenv

load_dotenv()

now = dt.datetime.now()

user_email = os.getenv("USER_EMAIL")
recipient_email = os.getenv("USER_PASSWORD")
password = os.getenv("PASSWD")

birthday_data = pandas.read_csv("birthdays.csv")
data_list = birthday_data.to_dict(orient="records")
for i in range(0, len(data_list)):
    month = data_list[i]['month']
    day = data_list[i]['day']
    email = data_list[i]['email']
    name = data_list[i]['name']
    if month == now.month and day == now.day:
        with open(f"letter_template/letter_{random.randint(1,6)}.txt") as file:
            template = file.read().replace("[NAME]", f"{name}")
            template1 = template.replace("Angela", "Shem")

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user_email, password)
                connection.sendmail(from_addr=user_email,
                                    to_addrs=recipient_email,
                                    msg=f"Subject:Happy Birthday\n\n{template1}")
