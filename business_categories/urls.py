from django.conf import settings
from django.conf.urls import url, include
from .views import bcategory

urlpatterns = [
    url(r'^category/$', bcategory, name='bcategory'),
]