from django.db import models
from django.core.urlresolvers import reverse
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Category(models.Model):
	category = models.CharField(max_length=255,null=True,blank=True, unique=True)
	cat_logo = models.ImageField(null=True,blank=True,width_field="width_field_logo",height_field="height_field_logo",verbose_name="Category Logo")
	height_field_logo = models.IntegerField(default=0)
	width_field_logo = models.IntegerField(default=0)
	cat_img = models.ImageField(null=True,blank=True,width_field="width_field_img",height_field="height_field_img",verbose_name="Category Image")
	height_field_img = models.IntegerField(default=0)
	width_field_img = models.IntegerField(default=0)
	background_color = models.CharField(max_length=255,null=True,blank=True, help_text="Ex: #FF0000")
	category_icon = models.CharField(max_length=255,null=True,blank=True, unique=True, help_text="Ex: fa fa-mobile")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.category

	def __str__(self):
		return self.category

	def get_absolute_url(self):
		return reverse("post_ad_sub_cat", kwargs={"type":"classifieds", "id": self.id})


class CategoryType(models.Model):
	category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL)
	cat_type = models.CharField(max_length=255,null=True,blank=True,verbose_name="Category Type")
	cat_order = models.CharField(max_length=255, choices=[('1', 'Left'), ('2', 'Right')],null=True,blank=True,verbose_name="Category Order")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name = "Category Type"
		verbose_name_plural = "Category Types"
		unique_together = ('category', 'cat_type', 'cat_order')

	def __unicode__(self):
		return self.cat_type


class SubCategory(models.Model):
	category = models.ForeignKey(Category, related_name="sub_category", null=True,on_delete=models.SET_NULL)
	#cat_order = models.CharField(max_length=255, choices=[('1', 'Left'), ('2', 'Right')],null=True,blank=True,verbose_name="Category order")
	cat_type = ChainedForeignKey(
        CategoryType,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name="Category Type"
    )
	sub_category = models.CharField(max_length=255,null=True,blank=True,verbose_name="Sub Category")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)
	

	class Meta:
		verbose_name = "Sub Category"
		verbose_name_plural = "Sub Categories"
		unique_together = ('category','sub_category')

	def __unicode__(self):
		return self.sub_category

	def __str__(self):
		return self.sub_category

	
class SubCategoryType(models.Model):
	category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL)
	cat_type = ChainedForeignKey(
        CategoryType,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name="Category Type"
    )
	sub_category = ChainedForeignKey(SubCategory,chained_field="cat_type",chained_model_field="cat_type",show_all=False,auto_choose=True,null=True,verbose_name="Sub Category")
	subcat_type = models.CharField(max_length=255,null=True,blank=True,verbose_name="Sub Category Type")
	created = models.DateTimeField(null=True,blank=True,auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(null=True,blank=True,auto_now_add=False,auto_now=True)
	

	class Meta:
		verbose_name = "Sub Category Type"
		verbose_name_plural = "Sub Category Types"
		unique_together = ('category', 'sub_category','subcat_type')

	def __unicode__(self):
		return self.subcat_type

	def __str__(self):
		return self.subcat_type


