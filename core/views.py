# views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from .tasks import scrape_jobs

class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer

@api_view(['POST'])
def trigger_scrape(request):
    allowed_sources = ['djinni', 'linkedin']
    sources = request.data.get('sources', allowed_sources)
    sources = [s for s in sources if s in allowed_sources]

    task = scrape_jobs.delay(sources)
    return Response({'status': 'scraping started', 'sources': sources, 'task_id': task.id})
