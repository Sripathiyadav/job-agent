from database import add_job

from sources.linkedin import search_linkedin
from sources.indeed import search_indeed

# from sources.stepstone import search_stepstone


def search_jobs(query):

    jobs = []

    try:
        jobs.extend(
            search_indeed(query)
        )
    except Exception as e:
        print("Indeed error:", e)

    try:
        jobs.extend(
            search_linkedin(query)
        )
    except Exception as e:
        print("LinkedIn error:", e)

    # Enable later when Stepstone works
    #
    # try:
    #     jobs.extend(
    #         search_stepstone(query)
    #     )
    # except Exception as e:
    #     print("Stepstone error:", e)

    for job in jobs:

        add_job(
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["source"]
        )

    return jobs