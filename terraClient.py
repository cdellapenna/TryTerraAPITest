# Importing the API and instantiating the client using your keys
from terra.base_client import Terra
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('API_KEY')
DEV_ID = os.environ.get('DEV_ID')
SECRET = os.environ.get('SIGN')


terra = Terra(API_KEY, DEV_ID, SECRET)

parsed_api_response = terra.list_providers().get_parsed_response()
print(parsed_api_response)

parsed_api_response = terra.list_users().get_parsed_response()
print(parsed_api_response)

