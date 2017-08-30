from django.contrib import admin
from .models import City
# Register your models here.
class CityAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','city']
	list_filter = ['created','updated']
	list_display_links = ['__unicode__']
	search_fields =['__unicode__']
	class meta:
		model = City


admin.site.register(City, CityAdmin)
