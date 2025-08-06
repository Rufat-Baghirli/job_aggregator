import requests
from bs4 import BeautifulSoup
from core.types import Job

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


def scrape_djinni() -> list[Job]:
    url = "https://djinni.co/jobs/?primary_keyword=Python&location=remote"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_listings = soup.select("li.list-jobs__item")

    for job in job_listings[:10]:
        title_tag = job.select_one("div.list-jobs__title > a")
        company_tag = job.select_one("div.list-jobs__details__info > a")

        if title_tag and company_tag:
            jobs.append({
                "title": title_tag.get_text(strip=True),
                "company": company_tag.get_text(strip=True),
                "link": f"https://djinni.co{title_tag['href']}",
            })

    return jobs
