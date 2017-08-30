from django.conf import settings
from django.conf.urls import url, include
from home.views import latestAdv, search

urlpatterns = [
    url(r'^latest/$', latestAdv, name='latest'),
    url(r'^search/$', search, name='search'),
]