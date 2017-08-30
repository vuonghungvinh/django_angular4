from rest_framework import serializers
from .models import Category, SubCategory

class SubCategorySerialzer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ('category', 'cat_type', 'sub_category')

class CategorySerializer(serializers.ModelSerializer):
	sub_category = SubCategorySerialzer(many=True, read_only=True)
	class Meta:
		model = Category
		fields = ('pk', 'category', 'cat_logo', 'cat_img', 'background_color', 'category_icon', 'sub_category')