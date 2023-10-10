from terra.base_client import Terra
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('API_KEY')
DEV_ID = os.environ.get('DEV_ID')
SECRET = os.environ.get('SIGN')

terra = Terra(API_KEY, DEV_ID, SECRET)

widget_response = terra.generate_widget_session(
    reference_id="MISSBARBARA",
    providers=["CRONOMETER", "OURA", "APPLE", "GOOGLE"],
    auth_success_redirect_url="https://www.google.com/",
    auth_failure_redirect_url="https://www.youtube.com/",
    language="en"
).get_parsed_response()

print(widget_response)