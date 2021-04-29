import requests
from datetime import date, timedelta

"""Get the previous few days' datetime"""
today = date.today().strftime('%Y-%m-%d')
yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
day_before = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "60min",    
    "apikey": "0I9TRC6RIK0LK6US",
}

news_params = {
    "q": "TSLA",
    "apiKey": "0d60b23561254d3fb2a2a25a8ff6ba7f",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()

"""Plug the dates in to retrieve the final stock prices"""
yesterday_end_price = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
print(f"Yesterday's closing price: {yesterday_end_price}")
day_before_end_price = float(data["Time Series (Daily)"][str(day_before)]["4. close"])
print(f"The day before's closing price: {day_before_end_price}")

"""Calculate the price fluctuation"""
price_change = abs(yesterday_end_price - day_before_end_price)
print(f"Difference: {round(price_change, 3)}")
percent_change = (price_change / yesterday_end_price) * 100
print(f"Percentage change: {round(percent_change, 3)}%")      # format to 3 decimal points

"""Retrieve news headlines if fluctuations are > 5%"""
if percent_change >= 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news = news_response.json()
    for _ in range(3):
        title = news["articles"][_]["title"]
        desc = news["articles"][_]["description"]
        print(f"{(_ +1)}: {title}")
        print(f"\nDesciption: {desc}\n")
else:
    print("Minor fluctuations, don't be greedy...")
