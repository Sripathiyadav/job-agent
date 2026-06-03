from database import add_job
from sources.linkedin import search_linkedin
from sources.stepstone import search_stepstone


def search_jobs(query):

    jobs = []

    jobs.extend(
        search_linkedin(query)
    )

    jobs.extend(
        search_stepstone(query)
    )

    for job in jobs:
        add_job(
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["source"]
        )

    return jobs