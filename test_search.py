from job_search import search_jobs

jobs = search_jobs("flutter")

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs:

    print(
        f"{job['title']} | "
        f"{job['company']} | "
        f"{job['location']} | "
        f"{job['source']}"
    )

    print(job["url"])

    print("-" * 80)