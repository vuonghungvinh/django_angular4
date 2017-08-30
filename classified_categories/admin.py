from django.contrib import admin
from .models import Category,CategoryType,SubCategory,SubCategoryType

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['created','updated']
	list_display_links = ['__unicode__']
	search_fields =['__unicode__']
	class meta:
		model = Category

class CategoryTypeAdmin(admin.ModelAdmin):
	list_display = ['category','__unicode__','cat_order']
	list_filter = ['created','updated']
	list_display_links = ['category']
	search_fields =['category','cat_type','cat_order']
	class Meta:
		model = CategoryType

class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ['sub_category','category','cat_type']
	list_filter = ['created','updated']
	list_display_links = ['sub_category']
	search_fields =['category','cat_order']
	class Meta:
		model = SubCategory

class SubCategoryTypeAdmin(admin.ModelAdmin):
	list_display = ['subcat_type','sub_category','cat_type','category']
	list_filter = ['created','updated']
	list_display_links = ['subcat_type']
	search_fields =['category','cat_type']
	class Meta:
		model = SubCategoryType


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SubCategoryType, SubCategoryTypeAdmin)
