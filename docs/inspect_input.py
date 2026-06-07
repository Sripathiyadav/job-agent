# inspect_input.py

from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

actor = client.actor("vw0F1amycaxZgyXFq")

print(actor.get().example_run_input)