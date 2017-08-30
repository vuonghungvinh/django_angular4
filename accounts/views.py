from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, IndividualSerializer, BusinessSerializer
from django.http import HttpResponse
import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.views import LoginView
from rest_auth.registration.serializers import (SocialLoginSerializer, VerifyEmailSerializer)
from allauth.account.adapter import get_adapter
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.shortcuts import redirect
from urllib.request import urlopen
from urllib.parse import urlencode

class SocialLoginView(LoginView):
	serializer_class = SocialLoginSerializer
	def process_login(self):
		get_adapter(self.request).login(self.request, self.user)

class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
	adapter_class = GoogleOAuth2Adapter

class TwitterLogin(LoginView):
	serializer_class = TwitterLoginSerializer
	adapter_class = TwitterOAuthAdapter

@csrf_exempt
def twitter(request):
	oauth_token = request.GET.get("oauth_token", "")
	oauth_verifier = request.GET.get("oauth_verifier", "")
	post_data = {'oauth_token':oauth_token, 'oauth_verifier':oauth_verifier}     # a sequence of two element tuples
	result = urlopen('https://api.twitter.com/oauth/access_token', urlencode(post_data).encode("utf-8"))
	content = result.read()
	return redirect('/twitter?'+content.decode("utf-8"))

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def loginWithSocial(request):
	token = Token.objects.get(user_id=request.user.id)
	user = User.objects.get(id=token.user_id)
	serializer_user = UserSerializer(instance=user)
	return Response({'api_token': token.key, 'user': serializer_user.data})

#login
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer_user = UserSerializer(instance=user)
        return Response({'api_token': token.key, 'user': serializer_user.data})

@csrf_exempt
@api_view(["POST"])
def registerIndividual(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		id = json.loads(json.dumps(serializer.data))['id']
		request.data['user'] = id
		request.data['type'] = False
		serializer_individual = IndividualSerializer(data=request.data)
		if serializer_individual.is_valid():
			serializer_individual.save()
			print (serializer_individual.data)
		else:
			user = User.objects.get(id=id)
			user.delete()
			return Response(serializer_individual.errors, status=404)
			print (serializer_individual.errors)
		return Response(serializer.data)
	return Response(serializer.errors, status=404)

@csrf_exempt
@api_view(["POST"])
def registerBusiness(request):
	request.data['first_name']=""
	request.data['last_name']=""
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		id = json.loads(json.dumps(serializer.data))['id']
		request.data['user'] = id
		request.data['type'] = True
		serializer_business = BusinessSerializer(data=request.data)
		if serializer_business.is_valid():
			serializer_business.save()
			print (serializer_business.data)
		else:
			user = User.objects.get(id=id)
			user.delete()
			return Response(serializer_business.errors, status=404)
		return Response(serializer.data)
	return Response(serializer.errors, status=404)