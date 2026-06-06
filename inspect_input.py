# inspect_input.py

from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

actor = client.actor("vw0F1amycaxZgyXFq")

data = actor.get()

print("EXAMPLE INPUT:")
print(data.example_run_input)