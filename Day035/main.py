import requests
from twilio.rest import Client
import time
import os

API_KEY = os.environ.get("OWM_API_KEY") # Change to your openweathermap API key.
CITY_NAME = "San Francisco" # Change the city and lat-long values if you choose.
parameters = {
    "lat": 37.774929,
    "lon": -122.419418,
    "exclude": "current,daily,minutely,alerts",
    "appid": API_KEY,

}

OWM_Endpoint = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
OWM_Endpoint.raise_for_status()

weather_data = OWM_Endpoint.json()["hourly"]
weather_codes = []
weather_slice = weather_data[:12]
for hourly_data in weather_slice:
    weather_codes.append(hourly_data["weather"][0]["id"])

rain = False
for code in weather_codes:
    if 500 <= code <= 630:
        rain = True

if rain:
    account_sid = os.environ.get("TWILIO_ACC_SID") # Change to your account sid
    auth_token = os.environ.get("TWILIO_ACC_AUTH") # Change to your auth token
    client = Client(account_sid, auth_token)

    message = client.messages.create\
        (
            body="Test message.",
            from_='+12345678', #Change to sender phone number. ( Your twilio phone number in console page.)
            to='12345678' #Change to recipient phone number ( Add the number as a verified caller ID in Twilio.
        )

    print(message.status)
    time.sleep(10)
    latest_message = client.messages(message.sid).fetch()
    print(latest_message.status)
