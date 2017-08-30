from django.db import models
from django_countries.fields import CountryField
from django_countries import Countries
# Create your models here.
class G8Countries(Countries):
    only = ['AE', 'EG', 'BH', 'SA', 'LB', 'KW', 'OM','QA']
    
class Price(models.Model):
	from_country = CountryField(blank_label='Select Country',null=True, blank=True,countries=G8Countries)
	to_country = CountryField(blank_label='Select Country',null=True, blank=True,countries=G8Countries)
	conversion_rate = models.FloatField(max_length=255,null=True,blank=True, verbose_name='Conversion Rate')
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	class Meta:
		app_label = "price"
		verbose_name = "price"
		verbose_name_plural = "price list"
		unique_together = ['from_country','to_country','conversion_rate']

	def __unicode__(self):
		return '%s' % self.from_country

