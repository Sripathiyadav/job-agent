from job_search import search_jobs

jobs = search_jobs("flutter")

for job in jobs:
    print(job["title"], "-", job["location"])
    