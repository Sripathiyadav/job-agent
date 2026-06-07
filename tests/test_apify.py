from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

user = client.user().get()

print("Connected!")
print(user.username)