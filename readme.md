# Job Aggregator

A Python-based **Job Aggregator** built with Django REST Framework that scrapes job listings from **Djinni** and **LinkedIn**.  
The project uses **Celery** + **Redis** for asynchronous scraping and provides a REST API to access collected jobs.

## Features
- Scrapes job listings from Djinni & LinkedIn.
- Stores results in a PostgreSQL (or SQLite) database.
- Asynchronous scraping with Celery and Redis.
- REST API endpoints for job listings.
- Easily extendable to new job sources.

## Tech Stack
- Python 3.10+
- Django 5.x
- Django REST Framework
- Celery
- Redis
- BeautifulSoup4

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/Rufat-Baghirli/job_aggregator.git
   cd job_aggregator
