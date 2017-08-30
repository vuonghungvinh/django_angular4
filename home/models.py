from django.db import models
from geoposition.fields import GeopositionField
from django_countries.fields import CountryField
from django_countries import Countries
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_resized import ResizedImageField
from business_categories.models import BCategory, BSubCategory, BSubCategoryType
from classified_categories.models import Category, SubCategory, SubCategoryType
from PIL import Image as Img
# from io import StringIO
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import sys
import re
from datetime import datetime

from smart_selects.db_fields import ChainedForeignKey

Country = (
    (1, u'UAE'),
    (2, u'Egypt'),
    (3, u'Bahrain'),
    (4, u'KSA'),
    (5, u'Lebanon'),
    (6, u'Kuwait'),
    (7, u'Oman'),
    (8, u'Qatar'),
)

ChoiceCondition = [('','Condition of Items'), ('Brand New Still in Packing', 'Brand New Still in Packing',), 
		('New without original packing', 'New without original packing',), ('Sparingly used', 'Sparingly used',), ('Used', 'Used',), ('Canadians', 'Canadians',), 
		('In good condition', 'In good condition',), ('Used with a few notable damage','Used with a few notable damage'),('Needs Repair','Needs Repair')]

ChoicePeriodUser = [('','Period Used'), ('Not Used', 'Not Used',), 
		('Few Days', 'Few Days',), ('1 Month', '1 Month',), ('2-6 months', '2-6 months',),
		('6-12 months','6-12 months'),('above 12 months','above 12 months'),
		('1 to 2 years used','1 to 2 years used'),('used above 2 years','used above 2 years')]

ChoiceWarranty = [('','Warranty'), ('Full Warranty Available', 'Full Warranty Available',), ('No Warranty', 'No Warranty',), ('Does not Apply', 'Does not Apply',)]

class G8Countries(Countries):
    only = ['AE', 'EG', 'BH', 'SA', 'LB', 'KW', 'OM','QA']


def get_upload_img_adname(instance, filename):
    name = re.sub(r'[^a-zA-Z0-9._\-()]', '', str(filename))
    name1 = re.sub(r'[^a-zA-Z0-9]', '', str(datetime.today()))
    name = str(name1)+str(name)
    return os.path.join("Adimage/"+str(instance.adname.pk), name)

# Create your models here.
class AdName(models.Model):
	user = models.ForeignKey('auth.User', related_name="adname_user", null=True, blank=True, on_delete=models.SET_NULL)
	ad_title = models.CharField(max_length=255,null=True,blank=True)
	slug = models.SlugField(max_length=255,null=True,blank=True)
	ad_description = models.TextField(max_length=255,null=True,blank=True)
	ad_type = models.BooleanField(choices = (
            (False, u"Products"),
            (True, u"Services"),
        ), default=False)
	type = models.BooleanField(choices = (
            (False, u"Classified"),
            (True, u"Business"),
        ), default=False)
	cat = models.ForeignKey(Category, related_name="adname_category", null=True, blank=True, on_delete=models.SET_NULL)
	sub_cat = models.ForeignKey(SubCategory, related_name="adname_subcategory", null=True, blank=True, on_delete=models.SET_NULL)
	sub_type = models.ForeignKey(SubCategoryType, related_name="adname_scategorytype", null=True, blank=True, on_delete=models.SET_NULL)
	ad_complete_status = models.BooleanField(default=False)
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.ad_title)
		super(AdName, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.ad_title
	def __str__(self):
		return self.ad_title

# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.ad_title)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs = AdName.objects.filter(slug=slug).order_by('-id')
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, sender=AdName)


class AdImage(models.Model):
	adname = models.ForeignKey(AdName, related_name='adimages', blank=True, null=True,on_delete=models.SET_NULL)
	# image = models.ImageField(null=True,blank=True)
	image = ResizedImageField(upload_to=get_upload_img_adname, size=[1024, 768], null=True, blank=True)
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.image

	def save(self, *args, **kwargs):
		try:
			this = AdImage.objects.get(id=self.id)
			if this.image != self.image:
				this.image.delete(save=False)
		except: pass
		if self.image:
			# image = Img.open(io.StringIO(self.image.read()))
			image = Img.open(io.BytesIO(self.image.read()))
			image.thumbnail((1024,768), Img.ANTIALIAS)
			output = io.BytesIO()
			image.save(output, format='JPEG', quality=75)
			output.seek(0)
			# self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name, 'image/jpeg', output.len, None)
			self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name, 'image/jpeg', output.getbuffer().nbytes, None)
		super(AdImage, self).save(*args, **kwargs)

class AdFeatures(models.Model):
	adname = models.OneToOneField(AdName, related_name="adname_feature", blank=True, null=True)
	condition_of_item = models.CharField(max_length=255, choices=ChoiceCondition,null=True,blank=True)
	period_used = models.CharField(max_length=255,choices=ChoicePeriodUser ,null=True,blank=True)
	warranty = models.CharField(max_length=255,choices=ChoiceWarranty,null=True,blank=True)
	position = GeopositionField(null=True, blank=True)
	address = models.CharField(max_length=255,null=True, blank=True)
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.condition_of_item

	def __str__(self):
		if self.adname:
			return '('+str(self.id)+')-'+self.adname.ad_title
		else:
			return '('+str(self.id)+')'


class AdFeaturesPricing(models.Model):
	ad_features = models.ForeignKey(AdFeatures, related_name="feature_price",null=True,blank=True)
	country =CountryField(null=True, blank=True,countries=G8Countries)
	price = models.IntegerField(default=0)
	currency = models.CharField(max_length=255,null=True,blank=True)
	negotiable = models.BooleanField(default=False)
	delivery_included = models.BooleanField(default=False)
	delivery_comments = models.TextField(max_length=255,null=True,blank=True)
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.currency


class AdPricing(models.Model):
	adname = models.OneToOneField(AdName, on_delete=models.CASCADE,  related_name="adname_pricing", blank=True, null=True)
	ad_featured = models.BooleanField(default=False)
	ad_push_to_top = models.BooleanField(default=False)
	ad_premium = models.BooleanField(default=False)
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

class CountryInfo(models.Model):
	country = models.IntegerField(default=0, choices=Country)
	country_name = models.CharField(max_length=255,null=True,blank=True)
	currency = models.CharField(max_length=255,null=True,blank=True)