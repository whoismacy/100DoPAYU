"""formatiing of the api's data isn't fixed and changes from time to time"""
import smtplib
from dotenv import load_dotenv
import os, requests
from datetime import datetime as dt, timedelta

load_dotenv()

# params = function{time series of choice}, apikey, symbol{company_to_track}, outputsize{compact, full}
STOCK = "TSLA"
STOCK_API = os.environ.get("STOCK_PRICES_API_KEY")
NEWS_API = os.environ.get("NEWS_API_KEY")
EMAIL = os.environ.get("USER_EMAIL")
PASSWD = os.environ.get("GOOGLE_APP_PWD")
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API,
}

try:
    stock_action = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
except Exception as e:
    print(f"Error while fetching Stocks API: {e}")
else:
    stock_data = stock_action.json()

# News API
# Url to contain /everything or /top-headlines
# q={keyword/phrases}, searchIn=title/description/phrases, from=ISO 8601 date format, language=en, sortBy=relevancy, popularity, publishedAt

request_from = dt.today() - timedelta(days=29)
news_parameters = {
    "q": STOCK,
    "searchIn": "title",
    "from": request_from,
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": NEWS_API,
    "pageSize": 5,
}

try:
    news_action = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
except Exception as e:
    print(f"Error occurred while fetching the News API: {e}")
else:
    news_data = news_action.json()

print(news_data)

headline = news_data["articles"][0]["title"]
description = news_data["articles"][0]["description"]
content = news_data["articles"][0]["content"]

today = dt.today()
yesterday = today - timedelta(days=1)
day_b4_yday = today - timedelta(days=2)

yesterday = yesterday.strftime("%Y-%m-%d")
day_b4_yday = day_b4_yday.strftime("%Y-%m-%d")

yday_cls_prc = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
dayb4_yday = float(stock_data["Time Series (Daily)"][day_b4_yday]["4. close"])
calculations = ((yday_cls_prc - dayb4_yday) / yday_cls_prc) * 100

message = f"Subject:{STOCK}: {headline}\n\n {description}"

if calculations:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=RECIPIENT,
                            msg=message.encode('utf-8'))


