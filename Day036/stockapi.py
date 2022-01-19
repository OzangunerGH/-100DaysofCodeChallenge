import requests
from datetime import date, timedelta
import os


def get_day(day):
    """Calculates the nearest day to today that the market was open as yesterday. The closest day before yesterday as
    previous day."""
    while True:
        try:
            a = data[str(day)]
        except KeyError:
            day -= timedelta(1)
        else:
            return day


def calculate_percentage(values: list):
    """Calculates the percentage difference between index item 0 and 1 inside the list."""
    if values[0] > values[1]:
        diff = -1 * (values[0] - values[1]) / values[0]
    else:
        diff = (values[1] - values[0]) / values[0]
    return diff


API_KEY = os.environ.get("STOCK_API_KEY")
FUNCTION = "TIME_SERIES_DAILY"
STOCK = "TSLA"

parameters = {

    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": API_KEY
}

# Getting Stock data from Stockapi.

stock_api = "https://www.alphavantage.co/query"
response = requests.get(stock_api, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Getting Today,Yesterday,previous day values to fetch share's closing values on those days.

today = date.today()

yesterday = today - timedelta(1)
yesterday = get_day(yesterday)

prev_day = yesterday - timedelta(1)
prev_day = get_day(prev_day)

# Gets the yesterday and prev_day close values into a list named close_values.

yesterday = str(yesterday)
prev_day = str(prev_day)
close_values = [float(data[prev_day]["4. close"]), float(data[yesterday]["4. close"])]

percent_diff = int(calculate_percentage(close_values))
