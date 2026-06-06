from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "keyword": "Flutter Developer Berlin",
    "maxItems": 5
}

run = client.actor(
    "hKByXkMQaC5Qt9UMN"
).call(run_input=run_input)

print("RUN FINISHED")
print(run["defaultDatasetId"])