from database import add_job

def search_jobs(query):
    jobs = [
        {
            "title": "Flutter Developer",
            "company": "Tech GmbH",
            "location": "Berlin",
            "url": "https://example.com/job1",
            "source": "demo"
        },
        {
            "title": "Werkstudent Mobile Development",
            "company": "Startup AG",
            "location": "Leipzig",
            "url": "https://example.com/job2",
            "source": "demo"
        }
    ]

    for job in jobs:
        add_job(
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["source"]
        )

    return jobs