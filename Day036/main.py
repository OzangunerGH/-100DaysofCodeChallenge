from stockapi import percent_diff
from newsapi import message_text
from twilio.rest import Client
import time
import os


def send_sms():
    """Sends SMS Message using Twilio."""
    account_sid = os.environ.get("TWILIO_ACC_SID")
    auth_token = os.environ.get("TWILIO_ACC_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{header} Check out the articles below to find out why.{message_text}",
        from_='+11234568',
        to='+91234567'
    )

    print(message.status)
    time.sleep(10)
    latest_message = client.messages(message.sid).fetch()
    print(latest_message.status)

# Also update STOCK variable in stockapi.py.
STOCK = "TSLA"

# Send an SMS if the difference between yesterday and previous day is higher than negative/positive %5 percent.

if percent_diff <= -5:
    header = f"{STOCK} is down by {percent_diff} percent.\n"
    send_sms()

elif percent_diff >= 5:
    header = f"{STOCK} is up by {percent_diff} percent!\n"
    send_sms()
