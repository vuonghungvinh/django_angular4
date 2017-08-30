from rest_framework import serializers
from .models import City
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth import password_validation

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('id', 'country', 'city')