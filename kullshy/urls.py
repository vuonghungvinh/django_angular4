"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from core import views
from accounts.views import twitter

apis = [
    url(r'^products/', include("home.urls")),
    url(r'^business/', include("business_categories.urls")),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^city/', include("cities.urls")),
    url(r'^home/', include("home.urls")),
]

urlpatterns = [
    url(r'accounts/twitter/login/callback/', twitter, name='twitter'),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apis)),
    url(r'^accounts/', include('allauth.urls'),name="allauth"),
    # url(r'^(?![ng/|media/]).*$', views.AngularApp.as_view(), name="angular_app"),
    url(r'^(?!ng/)(?!media/).*$', views.AngularApp.as_view(), name="angular_app"),
] + static(settings.ANGULAR_URL, document_root=settings.ANGULAR_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)