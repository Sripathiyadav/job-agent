from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

print("Connected")

for actor in client.actors().list(limit=20).items:
    print(actor.name)