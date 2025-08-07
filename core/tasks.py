# tasks.py
from celery import shared_task
from .models import Job
from .scraping.djinni import scrape_djinni
from .scraping.linkedin import scrape_linkedin

@shared_task
def scrape_jobs(sources=None):
    print("Task started")
    if sources is None:
        sources = ['djinni', 'linkedin']

    source_map = {
        'djinni': scrape_djinni,
        'linkedin': scrape_linkedin,
    }

    for source in sources:
        if source in source_map:
            results = source_map[source]()
            print(f"Data received from {source}: {len(results)} jobs")
            for job in results:
                obj, created = Job.objects.get_or_create(
                    title=job.get('title', ''),
                    company=job.get('company', ''),
                    url=job.get('link', ''),
                    source=source,
                    defaults={
                        "description": job.get('description', ''),
                        "location": job.get('location', ''),
                    }
                )
                if created:
                    print(f"Job added: {job['title']} from {source}")
                else:
                    print(f"Job already exists: {job['title']} from {source}")
    print("Task finished")