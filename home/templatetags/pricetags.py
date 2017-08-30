# from django import template
# from django.db import models
# from price.models import Price
# from classified_categories.models import SubCategoryType,Category,SubCategory
# from accounts.models import IndividualRegister,BusinessRegister
# from cities.models import City
# from home.models import AdImage,AdName,AdFeatures,AdFeaturesPricing
# import datetime, pytz
# import os
# from django.conf import settings
# from PIL import Image
# from business_categories.models import BCategory,BSubCategory
# import re

# register = template.Library()




# @register.filter()
# def another_filter(value_1, value_2):
#     return value_1, value_2

# @register.filter()
# def another_filter1(another_filter_value, value_3):
#     val1,val2 = another_filter_value
#     return val1,val2,value_3

# @register.filter()
# def another_filter2(another_filter_value, value_4):
#     val1,val2,val3 = another_filter_value
#     return val1,val2,val3,value_4


# @register.filter()
# def category1(val1, val2):
#     return val1, val2

# @register.filter()
# def category2(another_filter_value, value_3):
#     val1, val2 = another_filter_value
#     try:
#         get_sub_cat = SubCategoryType.objects.filter(sub_category_id=val1,category_id=val2,cat_type_id=value_3)
#         if get_sub_cat:
#             return 'true_val'
#         else:
#             return 'false_val'
#     except:
#         return 'false_val'

# @register.filter()
# def fetch_ad_image_count(val1):
#     ad_image = AdImage.objects.filter(adname_id=val1).count()
#     return ad_image

# @register.filter()
# def fetch_ad_image(val1):
#     ad_image_count = AdImage.objects.filter(adname_id=val1).count()
#     if ad_image_count:
#         ad_image = AdImage.objects.get(adname_id=val1,counter=1)
#         return ad_image.image.url
#     else:
#         return ""

# @register.filter(name='time_since')
# def time_since(date, default="just now"):
#     now = datetime.datetime.utcnow().replace(tzinfo = pytz.utc)
#     diff = now - date
#     periods = (
#         (diff.days / 365, "year", "years"),
#         (diff.days / 30, "month", "months"),
#         (diff.days / 7, "week", "weeks"),
#         (diff.days, "day", "days"),
#         (diff.seconds / 3600, "hour", "hours"),
#         (diff.seconds / 60, "minute", "minutes"),
#         (diff.seconds, "second", "seconds"),
#     )
#     for period, singular, plural in periods:
#         if period:
#             return "%d %s ago" % (period, singular if period == 1 else plural)
#     return default

# @register.filter()
# def thumbnail(file, size='200x200'):
#     return Image.open(file).resize(size, Image.ANTIALIAS)

# @register.filter(name='age_range') 
# def age_range(number):
#     return range(18,number)

# @register.filter
# def url_replace_all(value,type):
#     if type == "business":
#         return value.replace("type=business","type=")
#     elif type == "classifieds":
#         return value.replace("type=classifieds","type=")
#     else:
#         return value.replace("type=","type=")

# @register.filter
# def url_replace_bus(value,type):
#     if type == "business":
#         return value.replace("type=business","type=business")
#     elif type == "classifieds":
#         return value.replace("type=classifieds","type=business")
#     else:
#         return value.replace("type=","type=business")

# @register.filter
# def url_replace_ind(value,type):
#     if type == "business":
#         return value.replace("type=business","type=classifieds")
#     elif type == "classifieds":
#         return value.replace("type=classifieds","type=classifieds")
#     else:
#         return value.replace("type=","type=classifieds")


# @register.filter
# def cat_count_ad_list_ind(another_filter_value,value_3):
#     value_1, value_2 = another_filter_value
#     if value_2 != "":
#         ind_reg = IndividualRegister.objects.filter(country=value_3,city=value_2)
#     else:
#         ind_reg = IndividualRegister.objects.filter(country=value_3)
#     cat_count_sidebar = AdName.objects.filter(user_id__in=ind_reg.values('id'),cat_id=value_1,usertype="individual").count()
#     if cat_count_sidebar:
#         return cat_count_sidebar
#     else:
#         return 0


# @register.filter
# def subcat_count_ad_list_ind(val):
#     subcat_count_sidebar = AdName.objects.filter(sub_cat_id=val,usertype="individual").count()
#     if subcat_count_sidebar:
#         return subcat_count_sidebar
#     else:
#         return 0


# @register.filter
# def cat_count_ad_list_bus(another_filter_value,value_3):
#     value_1, value_2 = another_filter_value
#     if value_2 != "":
#         bus_reg = BusinessRegister.objects.filter(country=value_3,city=value_2)
#     else:
#         bus_reg = BusinessRegister.objects.filter(country=value_3)
#     cat_count_sidebar = AdName.objects.filter(user_id__in=bus_reg.values('id'),cat_id=value_1,usertype="business").count()
#     if cat_count_sidebar:
#         return cat_count_sidebar
#     else:
#         return 0


# @register.filter
# def subcat_count_ad_list_bus(val):
#     subcat_count_sidebar = AdName.objects.filter(sub_cat_id=val,usertype="business").count()
#     if subcat_count_sidebar:
#         return subcat_count_sidebar
#     else:
#         return 0



# @register.filter
# def fetch_cat_for_adlisting_for_particular_ad(val):
#     fetch_row = AdName.objects.get(id=val)
#     if fetch_row.usertype == "individual":
#         cat = Category.objects.get(id=fetch_row.cat_id)
#     else:
#         cat = BCategory.objects.get(id=fetch_row.cat_id)
#     return cat


# @register.filter
# def fetch_city_id_for_homepage(val1,val2):
#     fetch_city_id = City.objects.get(city=val1,country=val2)
#     if fetch_city_id:
#         return fetch_city_id.id
#     else:
#         return ''

# @register.filter
# def ad_list_pagination(url,page):
#     return url.replace("page=2","page=")


# @register.filter
# def classify_url_change(value):
#     classify_url1 = re.sub("[&,/.']", '-', value)
#     classify_url2 = classify_url1.replace(" ", "-")
#     classify_url3 = classify_url2.replace("--", "-")
#     classify_url4 = classify_url3.replace("--", "-")

#     return classify_url4

# @register.filter
# def classified_subcat_adlist_count(another_filter_value,val4):
#     val1,val2,val3 = another_filter_value
#     if val2 != "":
#         ind_reg = IndividualRegister.objects.filter(country=val3,city=val2)
#     else:
#         ind_reg = IndividualRegister.objects.filter(country=val3)
#     subtype_count_sidebar = AdName.objects.filter(user_id__in=ind_reg.values('id'),sub_cat_id=val1,cat_id=val4,usertype="individual").count()
#     if subtype_count_sidebar:
#         return subtype_count_sidebar
#     else:
#         return 0


# @register.filter
# def classified_subtype_adlist_count(another_filter_value,val5):
#     val1,val2,val3,val4 = another_filter_value
#     if val3 != "":
#         ind_reg = IndividualRegister.objects.filter(country=val4,city=val3)
#     else:
#         ind_reg = IndividualRegister.objects.filter(country=val4)
#     subtype_count_sidebar = AdName.objects.filter(user_id__in=ind_reg.values('id'),sub_cat_id=val1,cat_id=val2,sub_type_id=val5,usertype="individual").count()
#     if subtype_count_sidebar:
#         return subtype_count_sidebar
#     else:
#         return 0

# @register.filter
# def business_cat_adlist_count(val1):
#     cat_count_sidebar = AdName.objects.filter(cat_id=val1,usertype="business").count()
#     if cat_count_sidebar:
#         return cat_count_sidebar
#     else:
#         return 0

# @register.filter
# def business_subcat_adlist_count(another_filter_value,val4):
#     val1,val2,val3 = another_filter_value
#     if val2 != "":
#         bus_reg = BusinessRegister.objects.filter(country=val3,city=val2)
#     else:
#         bus_reg = BusinessRegister.objects.filter(country=val3)
#     subtype_count_sidebar = AdName.objects.filter(user_id__in=bus_reg.values('id'),sub_cat_id=val1,cat_id=val4,usertype="business").count()
#     if subtype_count_sidebar:
#         return subtype_count_sidebar
#     else:
#         return 0


# @register.filter
# def business_subtype_adlist_count(another_filter_value,val5):
#     val1,val2,val3,val4 = another_filter_value
#     if val3 != "":
#         bus_reg = BusinessRegister.objects.filter(country=val4,city=val3)
#     else:
#         bus_reg = BusinessRegister.objects.filter(country=val4)
#     subtype_count_sidebar = AdName.objects.filter(user_id__in=bus_reg.values('id'),sub_cat_id=val1,cat_id=val2,sub_type_id=val5,usertype="business").count()
#     if subtype_count_sidebar:
#         return subtype_count_sidebar
#     else:
#         return 0








    
    



