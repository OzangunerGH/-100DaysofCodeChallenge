import requests
# Getting questions with Open Trivia Database API.
QUESTION_AMOUNT = 10
QUESTION_TYPE = "boolean"
parameters = {"amount": QUESTION_AMOUNT,
              "type": QUESTION_TYPE}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]


