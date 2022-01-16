# Importing necessary libraries.

import requests
from datetime import datetime
import smtplib
import time

# Change e-mail address and password accordingly.
def send_email():
    """Sends an e-mail to recipient(s) on their birthday."""
    my_email = "example@email.com"
    password = "my_password"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{my_email}",
            msg=f"Subject:Look Up!\n\n ISS is passing above you!☝️"
        )


def is_iss_overhead():
    """Compares your coordinates against ISS and returns True when ISS is nearby."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5:
        print("is it overhead =True")
        return True
    # Your position is within +5 or -5 degrees of the ISS position.


def is_it_dark():
    """Returns true if the sun has set. and hasn't risen yet."""
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    time_now = datetime.now()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if 0 <= time_now.hour + 3 < sunrise or sunset <= time_now.hour + 3 <= 24:
        print("is it dark =True")
        return True


MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# The loop runs every 60 seconds to check if ISS location is close enough to see it at the sky.
while True:
    time.sleep(60)
    if is_it_dark() and is_iss_overhead():
        send_email()
