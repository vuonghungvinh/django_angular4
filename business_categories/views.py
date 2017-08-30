from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from business_categories.serializers import BCategorySerializer
from business_categories.models import BCategory
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def bcategory(request, format=None):
	if request.method == 'GET':
		bcategory = BCategory.objects.all()
		serializer_class = BCategorySerializer(instance = bcategory, many = True)
		return Response(serializer_class.data)