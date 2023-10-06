import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.tryterra.co/v2/subscriptions"

#FOR TEST DATA
headers = {
    "accept": "application/json",
    "dev-id": "testingTerra",
    "x-api-key": "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
}

#FOR OUR DATA
headers2 = {
    "accept": "application/json",
    "dev-id": os.environ.get('DEV_ID'),
    "x-api-key": os.environ.get('API_KEY')
}

response = requests.get(url, headers=headers2)

print(response.text)