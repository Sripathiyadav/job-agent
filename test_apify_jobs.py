from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

me = client.user().get()

print("Connected")
print(me.username)