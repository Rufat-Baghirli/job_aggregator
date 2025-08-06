from core.scraping.base import JobScraper
from core.scraping.djinni import scrape_djinni
from core.scraping.linkedin import scrape_linkedin
from core.types import Job

class DjinniScraper(JobScraper):
    def scrape(self) -> list[Job]:
        return scrape_djinni()

class LinkedInScraper(JobScraper):
    def scrape(self) -> list[Job]:
        return scrape_linkedin()

def get_all_scrapers() -> list[JobScraper]:
    return [DjinniScraper(), LinkedInScraper()]
