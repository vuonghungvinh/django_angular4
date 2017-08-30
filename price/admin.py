from django.contrib import admin
from .models import Price
# Register your models here.
class PriceAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','to_country','conversion_rate']
	list_filter = ['created','updated']
	list_display_links = ['__unicode__']
	search_fields =['__unicode__']
	class meta:
		model = Price


admin.site.register(Price, PriceAdmin)
