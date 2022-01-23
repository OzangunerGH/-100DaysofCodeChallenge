import requests


def create_user():
  sheety_api = "https://api.sheety.co/921c401760af4d4900e7bbef42e3d484/flightDeals/users"
  get_response = requests.get(url=sheety_api)
  result = get_response.json()['users']
  if result == []:
    object_id = 2
  else:
    object_id = result[-1]['id'] +1
  name = input("Please enter your name.").capitalize()
  last_name = input("Please enter your last name.").capitalize()
  email = input("Please enter your email address.")
  email_verification = input("Please enter your email address again to verify.")
  if email == email_verification:
    parameters = {"user":{"firstName": name,
                  "lastName": last_name,
                  "email": email
                  }}
    put_response = requests.put(url=f"{sheety_api}/{object_id}", json=parameters)  
    print(put_response.text)

create_user()
