from core.scraping.providers import get_all_scrapers
from core.types import Job

def main() -> None:
    all_jobs: list[Job] = []

    for scraper in get_all_scrapers():
        jobs = scraper.scrape()
        all_jobs.extend(jobs)

    for job in all_jobs:
        print(f"{job['title']} at {job['company']}: {job['link']}")

if __name__ == "__main__":
    main()
