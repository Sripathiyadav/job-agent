from sources.indeed import search_indeed

jobs = search_indeed("flutter")

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs[:5]:
    print(job)