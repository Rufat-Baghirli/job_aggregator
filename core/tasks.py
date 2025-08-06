# tasks.py
from celery import shared_task
from .models import Job
from .scraping.djinni import scrape_djinni
from .scraping.linkedin import scrape_linkedin

@shared_task
def scrape_jobs(sources=None):
    print("Task started")
    if sources is None:
        sources = ['djinni']

    source_map = {
        'djinni': scrape_djinni,
        'linkedin': scrape_linkedin,
    }

    for source in sources:
        if source in source_map:
            results = source_map[source]()
            print(f"Data received: {results}")
            for job in results:
                Job.objects.get_or_create(
                    title=job['title'],
                    company=job['company'],
                    link=job['link'],
                    source=source
                )
                print(f"Job added: {job['title']}")
    print("Task finished")
