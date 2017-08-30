from django.db import models
from geoposition.fields import GeopositionField
from django_countries.fields import CountryField
from django_countries import Countries
from business_categories.models import BCategory, BSubCategory
from django_resized import ResizedImageField
from datetime import datetime
import os
import sys
import re

from PIL import Image as Img
from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def get_upload_img_individual(instance, filename):
    name = re.sub(r'[^a-zA-Z0-9._\-()]', '', str(filename))
    name1 = re.sub(r'[^a-zA-Z0-9]', '', str(datetime.today()))
    name = str(name1)+str(name)
    return os.path.join("individual_account", name)

def get_upload_img_business(instance, filename):
    name = re.sub(r'[^a-zA-Z0-9._\-()]', '', str(filename))
    name1 = re.sub(r'[^a-zA-Z0-9]', '', str(datetime.today()))
    name = str(name1)+str(name)
    return os.path.join("business_account", name)

class G8Countries(Countries):
    only = ['AE', 'EG', 'BH', 'SA', 'LB', 'KW', 'OM','QA']

countries = (
	("BH", "Bahrain"),
	("EG", "Egypt"),
	("KW", "Kuwait"),
	("LB", "Lebanon"),
	("OM", "Oman"),
	("QA", "Qatar"),
	("SA", "Saudi Arabia"),
	("AE", "United Arab Emirates")
)

class IndividualAccount(models.Model):
	user = models.OneToOneField("auth.User", on_delete=models.CASCADE,  related_name="individual_user")
	type = models.BooleanField(choices = (
            (False, u"Individual"),
            (True, u"Business"),
        ), default=False)
	position = GeopositionField(null=True, blank=True)
	address = models.CharField(max_length=255,null=True, blank=True)
	# country = CountryField(null=True, blank=True,countries=G8Countries)
	country = models.CharField(null=True, blank=True, choices=countries, max_length=255)
	city = models.CharField(max_length=255,null=True, blank=True)
	secondary_contact_no = models.CharField(max_length=255,null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True, blank=True)
	# fname = models.CharField(max_length=255, null=True, blank=True)
	# lname = models.CharField(max_length=255,null=True, blank=True)
	# password = models.CharField(max_length=255,null=True, blank=True)
	# repassword = models.CharField(max_length=255,null=True, blank=True)
	gender = models.BooleanField(choices = (
            (False, u"Male"),
            (True, u"Female"),
        ), default=False)
	# dateofbirth = models.CharField(max_length=100,null=True, blank=True)
	dateofbirth = models.DateField(null=True, blank=True)
	contact_no = models.CharField(max_length=255,null=True, blank=True)
	# secondary_contact_no = models.CharField(max_length=255,null=True, blank=True)
	# username = models.CharField(max_length=255,null=True, blank=True)
	# email = models.CharField(max_length=255,null=True, blank=True)
	personal_status = models.IntegerField(default=0, verbose_name="Hide Personal Details", null=True, blank=True)
	contact_status = models.IntegerField(default=0, verbose_name="Hide Contact Details", null=True, blank=True)
	# login_status = models.IntegerField(default=0)
	profile_img = ResizedImageField(upload_to=get_upload_img_individual, size=[1024, 768], null=True, blank=True)
	# timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True, blank=True)
	avatar = ResizedImageField(upload_to=get_upload_img_individual, size=[640, 480], null=True, blank=True)

	def username(self):
		return self.user.username
	def email(self):
		return self.user.email

	class Meta:
		verbose_name = "Individual Users"
		verbose_name_plural = "Individual Users"

	def __unicode__(self):
		return self.username

class BusinessAccount(models.Model):
	user = models.OneToOneField("auth.User", on_delete=models.CASCADE,  related_name="business_user")
	type = models.BooleanField(choices = (
            (False, u"Individual"),
            (True, u"Business"),
        ), default=True)
	position = GeopositionField(null=True, blank=True)
	address = models.CharField(max_length=255,null=True, blank=True)
	country = models.CharField(null=True, blank=True, choices=countries, max_length=255)
	city = models.CharField(max_length=255,null=True, blank=True)
	secondary_contact_no = models.CharField(max_length=255,null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True, blank=True)
	business_name = models.CharField(max_length=255, blank=True, null=True)
	business_alias = models.CharField(max_length=255, blank=True, null=True)

	comp_name = models.CharField(max_length=255,null=True, blank=True)
	comp_alias = models.CharField(max_length=255,null=True, blank=True)
	# position = GeopositionField(null=True, blank=True)
	# address = models.CharField(max_length=255,null=True, blank=True)
	# business_type = models.CharField(max_length=255,null=True, blank=True)
	business_type = models.OneToOneField(BCategory, on_delete=models.CASCADE, related_name="business_bcategory")
	# business_sub_category = models.CharField(max_length=255,null=True, blank=True)
	business_sub_category = models.OneToOneField(BSubCategory, on_delete=models.CASCADE, related_name="business_bsubcategory", blank=True, null=True)
	business_address = models.TextField(max_length=255,null=True, blank=True)
	# country =CountryField(null=True, blank=True,countries=G8Countries, blank_label='-- Choose Country --')
	# city = models.CharField(max_length=255,null=True, blank=True)
	hq_country = models.CharField(max_length=255,null=True,blank=True)
	hq_city = models.CharField(max_length=255,null=True,blank=True)
	hq_address = models.CharField(max_length=255,null=True,blank=True)
	hq_contact_no = models.CharField(max_length=255,null=True,blank=True)
	brief_desc = models.TextField(max_length=255,null=True,blank=True)
	pri_det_status = models.IntegerField(default=0)
	sec_det_status = models.IntegerField(default=0)
	primary_fname = models.CharField(max_length=255,null=True, blank=True)
	primary_lname = models.CharField(max_length=255,null=True, blank=True)
	primary_designation = models.CharField(max_length=255,null=True,blank=True)
	primary_contact_no = models.CharField(max_length=255,null=True, blank=True)
	primary_email = models.CharField(max_length=255,null=True, blank=True)
	secondary_fname = models.CharField(max_length=255,null=True, blank=True)
	secondary_lname = models.CharField(max_length=255,null=True, blank=True)
	secondary_designation = models.CharField(max_length=255,null=True,blank=True)
	# secondary_contact_no = models.CharField(max_length=255,null=True, blank=True)
	secondary_email = models.CharField(max_length=255,null=True, blank=True)
	company_logo = ResizedImageField(upload_to=get_upload_img_business, size=[640, 480], null=True, blank=True)

	def username(self, x):
		return x.user.username
	def email(self, x):
		return x.user.email

	class Meta:
		verbose_name = "Business Users"
		verbose_name_plural = "Business Users"

	def __unicode__(self):
		return self.comp_name
