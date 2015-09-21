from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^leads/create/$', views.create_lead, name='create_lead'),
    url(r'^leads/(?P<lead_id>[a-zA-Z0-9_.-]+)/delete/$', views.delete_lead, name='delete_lead'),
    url(r'^leads/(?P<lead_id>[a-zA-Z0-9_.-]+)/edit/$', views.edit_lead, name='edit_lead'),
    url(r'^leads/(?P<lead_id>[a-zA-Z0-9_.-]+)/$', views.lead_detail, name='lead_detail'),
]
