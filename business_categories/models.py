from django.db import models
from django.core.urlresolvers import reverse
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class BCategory(models.Model):
	category = models.CharField(max_length=255,null=True,blank=False, unique=True)
	background_color = models.CharField(max_length=255,null=True,blank=False, help_text="Ex: #FF0000", verbose_name="Background and Title Color")
	category_icon = models.CharField(max_length=255,null=True,blank=False, unique=True, help_text="Ex: fa fa-car")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.category

	def get_absolute_url(self):
		return reverse("post_ad_sub_cat", kwargs={"type":"business", "id": self.id})



class BSubCategory(models.Model):
	category = models.ForeignKey(BCategory, related_name='bsubcategories', null=True,on_delete=models.SET_NULL)
	sub_category = models.CharField(max_length=255,null=True,blank=False,verbose_name="Sub Category")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)
	

	class Meta:
		verbose_name = "Sub Category"
		verbose_name_plural = "Sub Categories"
		unique_together = ('category','sub_category')

	def __unicode__(self):
		return self.sub_category

	
class BSubCategoryType(models.Model):
	category = models.ForeignKey(BCategory, null=True,on_delete=models.SET_NULL)
	sub_category = ChainedForeignKey(
        BSubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        null=True,
        related_name = 'bsubcategorytypies'
    )
	subcat_type = models.CharField(max_length=255,null=True,blank=False,verbose_name="Sub Category Type")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)
	

	class Meta:
		verbose_name = "Sub Category Type"
		verbose_name_plural = "Sub Category Types"
		unique_together = ('category', 'sub_category','subcat_type')

	def __unicode__(self):
		return self.subcat_type


