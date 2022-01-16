# Importing necessary libraries.
import smtplib
import datetime as dt
import random
import pandas as pd


def send_email():
    """Sends an e-mail to recipient(s) on their birthday."""
    my_email = "python.ozan@gmail.com"
    password = "A123654789b."
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{e_mail_variable}",
            msg=f"Subject:Happy Birthday {name}!\n\n{mail_text}"
        )


def choose_letter():
    """Chooses a random letter from the group of template birthday letters."""
    random_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt") as letter_file:
        final_text = letter_file.read()
        final_text = final_text.replace("[NAME]", name)
    return final_text


# Reading the list of birthdays of people.

birthdays = pd.read_csv("birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")
# Getting Today's date.
today = dt.datetime.now()

# If there is anyone whose birthday is today, e-mail them.
for birthday in birthday_dict:
    if birthday["month"] == today.month and birthday["day"] == today.day:
        e_mail_variable = birthday["email"]
        name = birthday["name"]
        mail_text = choose_letter()
        send_email()
