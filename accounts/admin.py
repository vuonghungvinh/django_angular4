from django.contrib import admin
from .models import IndividualAccount,BusinessAccount

# Register your models here.

class IndividualRegisterAdmin(admin.ModelAdmin):
	list_display = ['username', 'email']
	list_display_links = ['username']
	search_fields =['username', 'email']
	class meta:
		model = IndividualAccount

class BusinessRegisterAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'primary_email']
	list_display_links = ['__unicode__']
	search_fields =['__unicode__', 'primary_email']
	class meta:
		model = BusinessAccount

admin.site.register(IndividualAccount, IndividualRegisterAdmin)
admin.site.register(BusinessAccount, BusinessRegisterAdmin)
