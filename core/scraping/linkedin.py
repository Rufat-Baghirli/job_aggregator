import requests
from bs4 import BeautifulSoup
from core.types import Job

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_linkedin() -> list[Job]:
    url = "https://www.linkedin.com/jobs/search/?keywords=python&location=Remote"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_cards = soup.select("ul.jobs-search__results-list li")

    for job in job_cards[:10]:
        title_tag = job.select_one("h3.base-search-card__title")
        company_tag = job.select_one("h4.base-search-card__subtitle")
        link_tag = job.select_one("a.base-card__full-link")

        if title_tag and company_tag and link_tag:
            jobs.append({
                "title": title_tag.get_text(strip=True),
                "company": company_tag.get_text(strip=True),
                "link": link_tag['href'].split("?")[0],
            })

    return jobs
