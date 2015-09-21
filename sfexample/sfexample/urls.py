from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^', include('leads.urls', namespace='leads')),
]
