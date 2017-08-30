from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from business_categories.serializers import BCategorySerializer
from business_categories.models import BCategory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdNameSerializer
from .models import AdName
from django.conf import settings

@api_view(['GET'])
def latestAdv(request, format=None):
	if request.method == 'GET':
		adname = AdName.objects.all().order_by('-created')
		serializer_class = AdNameSerializer(instance = adname, many = True)
		return Response(serializer_class.data)

@api_view(['POST'])
def search(request, format=None):
	items_per_page = settings.ITEMS_PER_PAGE
	data = request.data
	cur = 1
	total_page = 1
	cur = int(data['cur'])
	if data['type'] == 'marketplace':
		adname = AdName.objects.filter(ad_title__icontains=data['key']).order_by('-created')
		total_page = int(len(adname)/items_per_page)
		if len(adname)%items_per_page > 0:
			total_page = total_page+1
		if cur>total_page:
			cur=1
		print(cur)
		try:
			adname = adname[(cur-1)*items_per_page: cur*items_per_page]
		except :
			adname = []
		serializer_class = AdNameSerializer(instance = adname, many = True)
		return Response({'data':serializer_class.data, 'current': cur, 'total': total_page, 'key': data['key']})
	if data['type'] == 'store':
		return Response({"store": "error"}, status=404)
	if data['type'] == 'user':
		return Response({'user': "error"}, status=404)
	return Response({'unknow': "error"}, status=404)