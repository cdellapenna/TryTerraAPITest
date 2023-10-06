import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# API endpoint URL
url = "https://api.tryterra.co/v2/auth/authenticateUser"

# Your Terra developer ID and API key
dev_id = os.environ.get('DEV_ID')
api_key = os.environ.get('API_KEY')

# Other parameters for authentication
resource = "GOOGLE"  # Replace with the resource (provider) to authenticate the user with
reference_id = "MISSBARBARA"  # Replace with an identifier to associate with the user
auth_success_redirect_url = "https://www.google.com/"  # Replace with the URL for redirection upon successful auth
auth_failure_redirect_url = "https://www.youtube.com/"  # Replace with the URL for redirection upon unsuccessful auth

# Headers for the API request
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "dev-id": dev_id,
    "x-api-key": api_key
}

# Body parameters for the API request
body_params = {
    "resource": resource,
    "reference_id": reference_id,
    "auth_success_redirect_url": auth_success_redirect_url,
    "auth_failure_redirect_url": auth_failure_redirect_url
}

# Make the API request
response = requests.post(url, headers=headers, data=json.dumps(body_params))

# Check the response
if response.status_code == 200:
    print("Authentication successful!")
    print("Response JSON: ", response.json())
else:
    print("Authentication failed!")
    print("Status Code: ", response.status_code)
    print("Response Text: ", response.text)