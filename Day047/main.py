from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os


def send_email():
    """Sends an e-mail to recipient(s)"""
    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_EMAIL_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=user_email,
            msg=f"Subject:{product_title}is now only{product_price}$! \n\n{message}"
        )


headers = {"accept-Language": "en-US,en;q=0.9",
           "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"
           }
URL = "https://www.amazon.com/Corsair-iCUE-4000X-Mid-Tower-Case/dp/B08C76W2WM/ref=sr_1_4?crid=NX96RFNXNZ5X&keywords=desktop+case&qid=1643587931&sprefix=desktop+c%2Caps%2C220&sr=8-4"
DESIRED_PRICE = float(input("Enter the desired price you would like to buy this product for. Numbers only.\n"))
user_email = input("Please enter your email to receive price notifications. The format should be example@example.com \n")
response = requests.get(url=URL, headers=headers)
result = response.text

soup = BeautifulSoup(result, "lxml")

price = soup.find_all(name="span", class_="a-offscreen")[0]
price_text = price.getText()
product_price = float(price_text.split("$")[1])
item_title = soup.find_all(name="span", class_="a-size-large product-title-word-break")[0]
product_title = item_title.getText()

message = f"The item you were tracking is now {product_price}$ only. Go buy now."
if product_price < DESIRED_PRICE:
    send_email()
