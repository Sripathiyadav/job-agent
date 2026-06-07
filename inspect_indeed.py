from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

actors = client.actors().list()

for actor in actors.items:
    print(actor.name)
    