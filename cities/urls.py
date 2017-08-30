from django.conf import settings
from django.conf.urls import url, include
from .views import get_city

urlpatterns = [
    url(r'^list/$', get_city, name='get_city'),
]