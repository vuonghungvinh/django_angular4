from django.db import models
from django_countries.fields import CountryField
from django_countries import Countries
# Create your models here.
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

class City(models.Model):
	country = models.CharField(null=True, blank=True, choices=countries, max_length=255)
	city = models.CharField(max_length=255,null=True,blank=True, verbose_name='City')
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	class Meta:
		app_label = "cities"
		verbose_name = "cities"
		verbose_name_plural = "city list"
		unique_together = ['country','city']

	def __unicode__(self):
		return '%s' % self.country