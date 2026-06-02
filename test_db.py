from database import add_job, get_jobs

add_job(
    "Flutter Developer",
    "Example Company",
    "Berlin",
    "https://example.com/job",
    "test"
)

jobs = get_jobs()

for job in jobs:
    print(job)