from django.contrib import admin
from .models import BCategory,BSubCategory,BSubCategoryType

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['created','updated']
	list_display_links = ['__unicode__']
	search_fields =['__unicode__']
	class meta:
		model = BCategory

class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ['sub_category','category']
	list_filter = ['created','updated']
	list_display_links = ['sub_category']
	search_fields =['category','sub_category']
	class Meta:
		model = BSubCategory

class SubCategoryTypeAdmin(admin.ModelAdmin):
	list_display = ['subcat_type','sub_category','category']
	list_filter = ['created','updated']
	list_display_links = ['subcat_type']
	search_fields =['category','sub_category','subcat_type']
	class Meta:
		model = BSubCategoryType


admin.site.register(BCategory, CategoryAdmin)
admin.site.register(BSubCategory, SubCategoryAdmin)
admin.site.register(BSubCategoryType, SubCategoryTypeAdmin)
