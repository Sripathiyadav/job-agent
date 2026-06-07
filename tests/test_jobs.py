from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

print("Connected to Apify")

actors = client.actors().list()

print("Success")
print(f"Found {len(actors.items)} actors")