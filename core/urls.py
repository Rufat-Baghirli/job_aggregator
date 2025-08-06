from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, trigger_scrape

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('', include(router.urls)),
    path('scrape/', trigger_scrape, name='trigger_scrape'),
]
