import json
import requests
from bs4 import BeautifulSoup
from core.types import Job

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


def scrape_djinni() -> list[dict]:
    url = "https://djinni.co/jobs/?primary_keyword=Python&location=remote"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find("script", type="application/ld+json")
    if not script_tag:
        print("No JSON-LD found!")
        return []

    data = json.loads(script_tag.string)
    jobs = []

    for job_json in data:
        jobs.append({
            "title": job_json.get("title") or job_json.get("category") or "Python Developer",
            "company": job_json.get("hiringOrganization", {}).get("name", "Unknown"),
            "link": job_json.get("url", url),
        })

    return jobs