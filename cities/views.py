from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import CitySerializer
from .models import City
from django.http import HttpResponse
import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(["POST"])
def get_city(request):
	cities = City.objects.filter(country=request.data['country'])
	serializer = CitySerializer(instance=cities, many=True)
	return Response(serializer.data)