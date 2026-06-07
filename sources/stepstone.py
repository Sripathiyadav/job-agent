from apify_client import ApifyClient
from config import APIFY_TOKEN


def search_stepstone(query):

    client = ApifyClient(APIFY_TOKEN)

    run = client.actor(
        "vw0F1amycaxZgyXFq"
    ).call(
        run_input={}
    )

    dataset_id = run.default_dataset_id

    jobs = []

    for item in client.dataset(dataset_id).iterate_items():

        title = item.get("title", "")

        if query.lower() in title.lower():

            jobs.append({
                "title": title,
                "company": item.get("companyName"),
                "location": item.get("location"),
                "url": item.get("url"),
                "source": "Stepstone"
            })

    return jobs
