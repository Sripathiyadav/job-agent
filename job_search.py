from database import add_job

from sources.linkedin import search_linkedin
from sources.stepstone import search_stepstone


def search_jobs(query):

    jobs = []

    try:
        jobs.extend(
            search_stepstone(query)
        )
    except Exception as e:
        print("Stepstone error:", e)

    try:
        jobs.extend(
            search_linkedin(query)
        )
    except Exception as e:
        print("LinkedIn error:", e)

    for job in jobs:

        add_job(
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["source"]
        )

    return jobs
