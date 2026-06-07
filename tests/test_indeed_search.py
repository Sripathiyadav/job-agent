# test_indeed_search.py

from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "startUrls": [
        {
            "url": "https://de.indeed.com/jobs?q=flutter&l=Berlin"
        }
    ]
}

run = client.actor(
    "hMvNSpz3JnHgl5jkh"
).call(run_input=run_input)

print(run)