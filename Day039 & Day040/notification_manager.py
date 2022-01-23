import os
from twilio.rest import Client
import smtplib


def send_sms(flight):
    """Sends SMS Message using Twilio."""

    account_sid = os.environ.get("TWILIO_ACC_SID")
    auth_token = os.environ.get("TWILIO_ACC_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    header = f"Low price flight for :{flight['cityTo']},for {flight['price']}$ only!\n".encode('utf-8')
    text_message = f"Departure time: {flight['local_departure']}\n" \
                   f"Departure city: {flight['cityFrom']}\n" \
                   f"Departure airport :{flight['flyFrom']}\n" \
                   f"Destination city : {flight['cityTo']}\n" \
                   f"Destination airport : {flight['flyTo']} ".encode('utf-8')

    message = client.messages.create(
        body=f"{header}\n {text_message}",
        from_='+19402672794',
        to='+905309179900'
    )

    print(message.status)


def send_email(flight, user_email):
    """Sends an e-mail to recipient(s) on their birthday."""
    my_email = "python.ozan@gmail.com"
    password = "A123654789b."
    header = f"Low price flight for :{flight['cityTo']},for {flight['price']}$ only!\n".encode('utf-8')
    email_message = f"Departure time: {flight['local_departure']}\n" \
                    f"Departure city: {flight['cityFrom']}\n" \
                    f"Departure airport :{flight['flyFrom']}\n" \
                    f"Destination city : {flight['cityTo']}\n" \
                    f"Destination airport : {flight['flyTo']} ".encode('utf-8')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{user_email}",
            msg=f"Subject:{header}\n {email_message}"
        )

