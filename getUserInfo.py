import requests

# API endpoint URL
url = "https://api.tryterra.co/v2/userInfo"

# User ID and (optional) reference ID for the user you want to get information for
user_id = "ccf1bf7e-9530-4d7a-a92d-43070a488a77"  # Replace with the actual user ID
reference_id = "optional_reference_id"  # Replace or omit if not using reference ID

# Headers for the API request
headers = {
    "accept": "application/json",
    "dev-id": "testingTerra",
    "x-api-key": "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
}

# Query parameters for the API request
params = {
    "user_id": user_id,
    "reference_id": reference_id  # Omit this line if not using reference ID
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