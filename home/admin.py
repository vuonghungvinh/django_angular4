from django.contrib import admin
from .models import AdName,AdImage,AdFeatures,AdFeaturesPricing,AdPricing, CountryInfo
# Register your models here.

class AdNameAdmin(admin.ModelAdmin):
	list_display = ['id', 'ad_title', 'user']
	list_filter = ['created','updated']
	list_display_links = ['ad_title']
	search_fields =['ad_title']
	class meta:
		model = AdName

class AdImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'adname', 'image']
	list_filter = ['created','updated']
	# list_display_links = ['image']
	search_fields =['adname']
	class meta:
		model = AdImage

class AdFeaturesAdmin(admin.ModelAdmin):
	list_display = ['condition_of_item', 'adname', 'period_used', 'warranty', 'position', 'address']
	list_filter = ['created','updated']
	list_display_links = ['condition_of_item']
	search_fields =['condition_of_item']
	readonly_fields = ['position']
	class meta:
		model = AdFeatures

class AdFeaturesPricingAdmin(admin.ModelAdmin):
	list_display = ['id', 'ad_features', 'currency', 'price']
	list_filter = ['created','updated']
	list_display_links = ['id']
	search_fields =['currency']
	class meta:
		model = AdFeaturesPricing

class AdPricingAdmin(admin.ModelAdmin):
	list_display = ['id', 'adname', 'ad_featured', 'ad_push_to_top', 'ad_premium']
	list_filter = ['created','updated']
	list_display_links = ['id']
	search_fields =['adname']
	class meta:
		model = AdPricing

class CountryInfoAdmin(admin.ModelAdmin):
	list_display = ('country', 'country_name', 'currency')
	list_filter = ('country_name', 'currency')
	search_fields = ('country_name',)
		
admin.site.register(CountryInfo, CountryInfoAdmin)
admin.site.register(AdName, AdNameAdmin)
admin.site.register(AdImage, AdImageAdmin)
admin.site.register(AdFeatures, AdFeaturesAdmin)
admin.site.register(AdFeaturesPricing, AdFeaturesPricingAdmin)
admin.site.register(AdPricing, AdPricingAdmin)
