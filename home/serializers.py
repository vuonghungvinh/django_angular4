from rest_framework import serializers
from .models import AdName, AdImage, AdFeatures, AdFeaturesPricing, AdPricing
from classified_categories.serializers import CategorySerializer, SubCategorySerialzer
from accounts.serializers import UserSerializer

class AdImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdImage
		fields = ('adname', 'image')

class AdFeaturesPricingSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdFeaturesPricing
		fields = ('ad_features', 'country', 'price', 'currency', 'negotiable', 'delivery_included', 'delivery_comments')

class AdFeaturesSerializer(serializers.ModelSerializer):
	feature_price = AdFeaturesPricingSerializer(many=True, read_only=True)
	class Meta:
		model = AdFeatures
		fields = ('adname', 'condition_of_item', 'period_used', 'warranty', 'position', 'address', 'feature_price')

class AdPricingSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdPricing
		fields = ('adname', 'ad_featured', 'ad_push_to_top', 'ad_premium')

class AdNameSerializer(serializers.ModelSerializer):
	adimages = AdImageSerializer(many = True, read_only = True)
	adname_feature = AdFeaturesSerializer(read_only=True)
	adname_pricing = AdPricingSerializer(read_only=True)
	cat = CategorySerializer(read_only=True)
	sub_cat = SubCategorySerialzer(read_only=True)
	user = UserSerializer(read_only=True)
	created = serializers.DateTimeField(read_only=True)
	class Meta:
		model = AdName
		fields = ('pk', 'user', 'ad_title', 'slug', 'ad_description', 'type', 'ad_type', 'cat', 'sub_cat', 'sub_type', 'ad_complete_status', 'adimages', 'adname_feature', 'adname_pricing', 'created')