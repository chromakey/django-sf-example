from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('leads.urls', namespace='leads')),
]
