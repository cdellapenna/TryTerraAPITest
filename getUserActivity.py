import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these with your actual credentials and user ID
api_key = os.environ.get('API_KEY')
dev_id = os.environ.get('DEV_ID')
user_id = "5e41be1d-5949-4095-b8e7-9749931e8d5f"

# Define the start and end dates for data retrieval
# Note: Ensure these dates have data for the user
start_date = "2022-10-01"

# URL for the API endpoint
url = f"https://api.tryterra.co/v2/activity"

# Headers for the API request
headers = {
    "accept": "application/json",
    "x-api-key": api_key,
    "dev-id": dev_id
}

# Parameters for the API request
params = {
    "user_id": user_id,
    "start_date": start_date,
    "to_webhook": "true",
    "with_samples": "true"
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Handle the API response
if response.status_code == 200:
    print("Data retrieval initiated successfully!")
    print("Response Data:", response.json())
else:
    print("Error:", response.status_code)
    print("Response Data:", response.text)