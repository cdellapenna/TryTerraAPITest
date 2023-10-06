import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.tryterra.co/v2/daily"

# User ID and other parameters for the request
user_id = "5e41be1d-5949-4095-b8e7-9749931e8d5f"
start_date = "2022-10-01" 
to_webhook = "true"
with_samples = "true"

# Headers for the API request
headers = {
    "accept": "application/json",
    "dev-id": os.environ.get('DEV_ID'),
    "x-api-key": os.environ.get('API_KEY')
}

# Query parameters for the API request
params = {
    "user_id": user_id,
    "start_date": start_date,
    "to_webhook": to_webhook,
    "with_samples": with_samples
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check the response
if response.status_code == 200:
    print("Request successful!")
    print("Response JSON: ", response.json())
else:
    print("Request failed!")
    print("Status Code: ", response.status_code)
    print("Response Text: ", response.text)