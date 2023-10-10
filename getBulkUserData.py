import requests
import json

# Define the URL and headers
url = "https://api.tryterra.co/v2/bulkUserInfo"
headers = {
    "accept": "application/json",
    "dev-id": "testingTerra",
    "x-api-key": "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
}

# Array of strings of User IDS
user_ids = ["c120a9fb-d004-4730-b38d-1526b47c45cd","b601bb74-0998-4641-ad55-ae107671fe75"]
body = json.dumps(user_ids)

# Send a POST request to the API endpoint
response = requests.post(url, headers=headers, data=body)

# Print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")