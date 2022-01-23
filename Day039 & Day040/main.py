# Importing necessary libraries
import requests
from datetime import datetime, timedelta
import os
import notification_manager
from pprint import pprint

# CONSTANTS
FLY_FROM = "IST"
DATE_FROM = datetime.today()
DATE_TO = DATE_FROM + timedelta(180)
DATE_FROM = DATE_FROM.strftime("%d/%m/%Y")
DATE_TO = DATE_TO.strftime("%d/%m/%Y")
MAX_STOPOVERS = 0
FLIGHT_PER_CITY = 1
CURRENCY = "USD"

# Endpoints, headers,APIs
kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
KIWI_API = os.environ.get("KIWI_API_KEY")
kiwi_headers = {"apikey": KIWI_API}
kiwi_locations_api = "https://tequila-api.kiwi.com/locations/query"

sheety_header = {"Authorization": "Basic b3phbmd1bmVyOTI6QTEyMzY1NDc4OWIu"}
sheety_endpoint = "https://api.sheety.co/921c401760af4d4900e7bbef42e3d484/flightDeals/prices"
# User sheet endpoint to send e-mails to users.
users_endpoint = "https://api.sheety.co/921c401760af4d4900e7bbef42e3d484/flightDeals/users"

# Getting the data from Google Sheets using Sheety.
response = requests.get(url=sheety_endpoint, headers=sheety_header)
sheet_data = response.json()['prices']

# Checking if iataCode's are empty for cities. Filling them with appropriate codes if they are empty.
for row in sheet_data:
    search_query = {"term": row['city'], "location_types": "city"}
    response = requests.get(url=kiwi_locations_api, params=search_query, headers=kiwi_headers)
    result = response.json()['locations'][0]['code']

    if row['iataCode'] == "":
        row['iataCode'] = result
        new_data = {"price": {"iataCode": result}}
        response = requests.put(url=f"{sheety_endpoint}/{row['id']}", json=new_data, headers=sheety_header)


# Using Kiwi search api to search flights for every city in google sheets.

for city in sheet_data:
    fly_to = city['iataCode']
    lowest_price = city['lowestPrice']
    search_parameters = {"fly_from": FLY_FROM,
                         "fly_to": fly_to,
                         "date_from": DATE_FROM,
                         "date_to": DATE_TO,
                         "max_stopovers": MAX_STOPOVERS,
                         "curr": CURRENCY,
                         "one_for_city": FLIGHT_PER_CITY
                         }

    response = requests.get(url=kiwi_search_endpoint, params=search_parameters, headers=kiwi_headers)
    data = response.json()['data']
    # If there are no flights for a certain city, letting user know there are no flights
    # and preventing the code from error.
    try:
        response.json()['data'][0]
    except IndexError:
        print(f"No direct flights found for origin {FLY_FROM} to {fly_to} between {DATE_FROM} to {DATE_TO}.")
        continue
    else:
        # Sending SMS(to a single person) and e-mails to registered users with flight details if any of the flights
        # that are found is cheaper than the lowest price specified in Google sheets.
        for flight in data:
            if flight['price'] <= lowest_price:
                notification_manager.send_sms(flight)
                response = requests.get(url=users_endpoint)
                user_list = response.json()['users']
                for user in user_list:
                    notification_manager.send_email(flight, user['email'])
