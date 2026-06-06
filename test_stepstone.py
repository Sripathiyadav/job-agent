from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "urls": [
        "https://www.stepstone.de/jobs/flutter"
    ]
}

run = client.actor(
    "vw0F1amycaxZgyXFq"
).call(run_input=run_input)

dataset_id = run["defaultDatasetId"]

items = list(
    client.dataset(dataset_id).iterate_items()
)

print(f"Found {len(items)} jobs")

for item in items[:5]:
    print(item)
    print("-" * 50)