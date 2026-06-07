from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

run = client.actor(
    "vw0F1amycaxZgyXFq"
).call(
    run_input={}
)

dataset_id = run.default_dataset_id

items = list(
    client.dataset(dataset_id).iterate_items()
)

print(f"\nFound {len(items)} items\n")

for item in items[:5]:
    print(item)
    print("-" * 50)
