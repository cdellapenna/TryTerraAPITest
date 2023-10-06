import datetime
from terra.base_client import Terra
from terra.models.user import User
# ... other necessary imports

# Initialize the Terra client
terra = Terra(api_key="ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG", dev_id="testingTerra", secret="SECRETKEYHERE")

# Assume you have a User object, if not, create or retrieve one
user = User(user_id="b476fcf5-e55e-4d06-9f13-306003329e9b", provider="GOOGLE")

# Define the start and end dates for data retrieval
start_date = datetime.datetime.now() - datetime.timedelta(days=7)  # 7 days ago
end_date = datetime.datetime.now()  # now

# Retrieve activity data
response = terra.get_activity_for_user(user, start_date, end_date, to_webhook=True)

# Handle the response
if response.is_successful():
    print("Data retrieval initiated successfully!")
else:
    print("Error:", response.error_message)