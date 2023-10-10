# Importing the API and instantiating the client using your keys
from terra.base_client import Terra
from terra.models.user import User
import datetime
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


# Hypothetical example, adjust based on actual API client usage
user = User(user_id="9ced657c-2259-4674-a2a0-0b278b154cdb")
start_date = datetime.datetime.strptime("2023-10-01", "%Y-%m-%d")
end_date = None  # or define end_date similarly if needed
parsed_api_response = terra.get_activity_for_user(user, start_date, end_date).get_parsed_response()
print(parsed_api_response)

