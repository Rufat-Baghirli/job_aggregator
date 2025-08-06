from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(unique=True)
    source = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

