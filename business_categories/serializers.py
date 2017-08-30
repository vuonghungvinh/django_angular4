from rest_framework import serializers
from .models import BCategory,BSubCategory, BSubCategoryType

class BSubCategoryTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = BSubCategoryType
		fields = ('pk', 'category', 'sub_category', 'subcat_type')

class BSubCategorySerializer(serializers.ModelSerializer):
	bsubcategorytypies = BSubCategoryTypeSerializer(many = True, read_only = True)
	class Meta:
		model = BSubCategory
		fields = ('pk', 'category', 'sub_category', 'bsubcategorytypies')

class BCategorySerializer(serializers.ModelSerializer):
	bsubcategories = BSubCategorySerializer(many = True, read_only = True)
	class Meta:
		model = BCategory
		fields = ('pk', 'category', 'background_color', 'category_icon', 'bsubcategories')