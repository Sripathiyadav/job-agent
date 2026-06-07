# read_indeed_results.py

from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

dataset_id = "idVKQV2QXsZ0xWYOk"

for item in client.dataset(dataset_id).iterate_items():
    print(item)
    print("-" * 50)