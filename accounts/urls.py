from django.conf import settings
from django.conf.urls import url, include
from .views import registerIndividual, CustomObtainAuthToken, registerBusiness, FacebookLogin, loginWithSocial, GoogleLogin, TwitterLogin, twitter

urlpatterns = [
    url(r'^registerindividual/$', registerIndividual, name='registerindividual'),
    url(r'^registerbusiness/$', registerBusiness, name='registerbusiness'),
    url(r'^api-token-auth/', CustomObtainAuthToken.as_view()),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^login-with-social/$', loginWithSocial, name='loginWithSocial'),
]