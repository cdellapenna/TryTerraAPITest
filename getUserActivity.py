import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these with your actual credentials and user ID
api_key = os.environ.get('API_KEY')
dev_id = os.environ.get('DEV_ID')
user_id = "7114f2c5-5097-4c67-a646-b44af8ad0cc4"

#api_key = "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
#dev_id = "testingTerra"
#user_id = "c120a9fb-d004-4730-b38d-1526b47c45cd"

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
    "to_webhook": "false",
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