import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
recipient = os.getenv("RECIPIENT")
set_price = 100

url = "https://www.amazon.com/dp/B075CYMYK6"

def remove_duplicates(string):
    new_string = ""
    first_char = None
    for i in range(0, len(string)):
        if string[i] == first_char:
            continue
        else:
            new_string += string[i]
        first_char = string[i]

    return new_string

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(url=url, headers=headers)
content = BeautifulSoup(response.text, "html.parser")

price_div = content.find(name="span", class_="aok-offscreen")
item_price = float(price_div.get_text().split(" ")[3][1:])

title_div = content.find(name="span", id="productTitle")
title = remove_duplicates(title_div.get_text()).replace("\r\n", " ")
message = f"Subject:Price Update\n\n{title}\nLINK:{url}"
message = message.encode("utf-8")

with smtplib.SMTP("smtp.gmail.com") as connection:
    if item_price < set_price:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=recipient,
                            msg=message)
