# inspect_indeed_actor.py

from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

actor = client.actor("indeed-scraper")

print(actor.get())
