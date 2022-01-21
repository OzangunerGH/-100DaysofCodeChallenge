import requests
from datetime import date, timedelta
import os

TOKEN = os.environ.get("TOKEN_KEY")

USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "python-graph"
QUANTITY = "60"
today = date.today() - timedelta(2)
today = today.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

register_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}
# Registering for an account at pixela using post request.
response = requests.post(url=pixela_endpoint, json=register_parameters)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Python",
    "unit": "commit",
    "type": "int",
    "color": "momiji"}

# Headers are used to pass in your token securely preventing others from attaining it.

headers = {
    "X-USER-TOKEN": TOKEN
}

# Post request example.
graph = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(graph.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_parameters = {"date": today,
                    "quantity": QUANTITY
                    }
# Post request to change a pixel in graph.
pixel_post = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(pixel_post.text)

pix_update_parameters = {"quantity": QUANTITY
                         }
# Update request example to update an entry in the graph.

update_endpoint = f"{pixel_endpoint}/{today}"
pixel_update = requests.put(url=update_endpoint, json=pix_update_parameters, headers=headers)
print(pixel_update.text)


# delete request example to delete an entry from table.
pixel_delete = requests.delete(url=update_endpoint, json=pix_update_parameters, headers=headers)
print(pixel_delete.text)
