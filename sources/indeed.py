from apify_client import ApifyClient
from config import APIFY_TOKEN


def search_indeed(query, location="Berlin", limit=10):

    client = ApifyClient(APIFY_TOKEN)

    run_input = {
        "position": query,
        "country": "Germany",
        "location": location,
        "maxItems": limit
    }

    run = client.actor(
        "apify/indeed-scraper"
    ).call(run_input=run_input)

    dataset_id = run.default_dataset_id

    jobs = []

    for item in client.dataset(dataset_id).iterate_items():

        jobs.append({
            "title": item.get("positionName"),
            "company": item.get("company"),
            "location": item.get("location"),
            "url": item.get("url"),
            "source": "Indeed"
        })

    return jobs