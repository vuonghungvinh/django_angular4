import json
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django_countries import countries
import pycountry
from price.models import Price
from accounts.models import IndividualRegister,BusinessRegister
from business_categories.models import BSubCategory
from cities.models import City
from django.core import serializers
from django.utils.translation import ugettext as _
from django.utils import translation



def country(request):
    if request.is_ajax() and request.POST:

        select_country = request.POST.get("item", "")
        mycountry = dict(countries)[select_country]
        # print (select_country)
        chose_country = pycountry.countries.get(name=mycountry)
        currency = pycountry.currencies.get(numeric=chose_country.numeric)
        # print (currency)
        data = {'message': currency.alpha_3}
        
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')


# def country(request):
#     if request.is_ajax() and request.POST:
#         select_country = request.POST.get("item", "")
#         mycountry = dict(countries)[select_country]
#         chose_country = pycountry.countries.get(name=mycountry)
#         currency = pycountry.currencies.get(numeric=chose_country.numeric)
#         given_price = request.POST.get("price", "")
#         get_price_country = request.POST.get("get_price_country", "")
#         db_price = Price.objects.get(from_country=get_price_country,to_country=select_country)
#         price = float(db_price.conversion_rate)*float(given_price)
#         data = {'message': currency.letter,'price':price}
        

#         return HttpResponse(json.dumps(data), content_type='application/json')
#     else:
#         return HttpResponseRedirect('/')





def login(request):
  
    user_language = request.session.get('language')

    cities = City.objects.filter(country=request.session['countryName'])

    translation.activate(user_language)

    if request.is_ajax() and request.POST.get('email') and request.POST.get('password'):
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        if '@' in email :
            individual = IndividualRegister.objects.filter(email=email,password=password)
            business = BusinessRegister.objects.filter(primary_email=email,password=password)
            if individual:
                individual1 = IndividualRegister.objects.get(email=email,password=password)
                request.session['username'] = individual1.fname
                request.session['usertype'] = 'individual'
                request.session['userid'] = individual1.id
                if individual1.city:
                    get_city = City.objects.get(id=individual1.city)
                    request.session['city'] = get_city.city
                if individual1.profile_img:
                    request.session['img'] = individual1.profile_img.url
                elif individual1.avartar:
                    request.session['img'] = individual1.avartar
                if individual1.country == 'AE':
                    country = 1
                elif individual1.country == 'EG':
                    country = 2
                elif individual1.country == 'BH':
                    country = 3
                elif individual1.country == 'SA':
                    country = 4
                elif individual1.country == 'LB':
                    country = 5
                elif individual1.country == 'KW':
                    country = 6
                elif individual1.country == 'OM':
                    country = 7
                elif individual1.country == 'QA':
                    country = 8
                else:
                    country = 1
                
                url_login_city = individual1.city 
                url_login_country = country
                url_login_language = request.session.get('language')
            elif business:
                business1 = BusinessRegister.objects.get(primary_email=email,password=password)
                request.session['username'] = business1.comp_name
                request.session['usertype'] = 'business'
                request.session['userid'] = business1.id
                if business1.city:
                    get_city = City.objects.get(id=business1.city)
                    request.session['city'] = get_city.city
                if business1.company_logo:
                    request.session['img'] = business1.company_logo.url
                if business1.country == 'AE':
                    country = 1
                elif business1.country == 'EG':
                    country = 2
                elif business1.country == 'BH':
                    country = 3
                elif business1.country == 'SA':
                    country = 4
                elif business1.country == 'LB':
                    country = 5
                elif business1.country == 'KW':
                    country = 6
                elif business1.country == 'OM':
                    country = 7
                elif business1.country == 'QA':
                    country = 8
                else:
                    country = 1
                url_login_city = business1.city 
                url_login_country = country
                url_login_language = request.session.get('language')
            else :
                error_login = "Login Failed!!!"
        else:
            individual = IndividualRegister.objects.filter(username=email,password=password,login_status=1)
            business = BusinessRegister.objects.filter(username=email,password=password,login_status=1)
            if individual:
                individual1 = IndividualRegister.objects.get(username=email,password=password,login_status=1)
                request.session['username'] = individual1.fname
                request.session['usertype'] = 'individual'
                request.session['userid'] = individual1.id
                if individual1.city:
                    get_city = City.objects.get(id=individual1.city)
                    request.session['city'] = get_city.city
                if individual1.profile_img:
                    request.session['img'] = individual1.profile_img.url
                elif individual1.avartar:
                    request.session['img'] = individual1.avartar
                if individual1.profile_img:
                    request.session['img'] = individual1.profile_img.url
                elif individual1.avartar:
                    request.session['img'] = individual1.avartar
                if individual1.country == 'AE':
                    country = 1
                elif individual1.country == 'EG':
                    country = 2
                elif individual1.country == 'BH':
                    country = 3
                elif individual1.country == 'SA':
                    country = 4
                elif individual1.country == 'LB':
                    country = 5
                elif individual1.country == 'KW':
                    country = 6
                elif individual1.country == 'OM':
                    country = 7
                elif individual1.country == 'QA':
                    country = 8
                else:
                    country = 1
                url_login_city = individual1.city 
                url_login_country = country
                url_login_language = request.session.get('language')
            elif business:
                business1 = BusinessRegister.objects.get(username=email,password=password,login_status=1)
                request.session['username'] = business1.comp_name
                request.session['usertype'] = 'business'
                request.session['userid'] = business1.id
                if business1.city:
                    get_city = City.objects.get(id=business1.city)
                    request.session['city'] = get_city.city
                if business1.company_logo:
                    request.session['img'] = business1.company_logo.url
                if business1.company_logo:
                    request.session['img'] = business1.company_logo.url
                if business1.country == 'AE':
                    country = 1
                elif business1.country == 'EG':
                    country = 2
                elif business1.country == 'BH':
                    country = 3
                elif business1.country == 'SA':
                    country = 4
                elif business1.country == 'LB':
                    country = 5
                elif business1.country == 'KW':
                    country = 6
                elif business1.country == 'OM':
                    country = 7
                elif business1.country == 'QA':
                    country = 8
                else:
                    country = 1
                url_login_city = business1.city 
                url_login_country = country
                url_login_language = request.session.get('language')
            else :
                error_login = "Login Failed!!!"
        data = {'city': url_login_city, 'country' :url_login_country , 'language' : url_login_language }
        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        return HttpResponseRedirect('/')

def city(request):
    if request.is_ajax() and request.POST:
        country = request.POST.get("country", "")
        city = City.objects.filter(country=country)
        data = serializers.serialize("json", city)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def getemail_bus(request):
    if request.is_ajax() and request.POST:
        email = request.POST.get("email", "")
        message = ""
        if email != '':
            if '@' in email :
                queryset = IndividualRegister.objects.filter(email=email)
                queryset1 = BusinessRegister.objects.filter(primary_email=email)
                if queryset or queryset1:
                    message = "Email Address Already exists" 
                else:
                    message = ""
            else :
                message = "Not a Valid Email Address"
        else:
            message = "Kindly enter valid email Address"
        data = {'message': message}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def getemail_bus_sec(request):
    if request.is_ajax() and request.POST:
        email = request.POST.get("email", "")
        message = ""
        if email != '':
            if '@' in email :
                queryset = IndividualRegister.objects.filter(email=email)
                queryset1 = BusinessRegister.objects.filter(primary_email=email)
                if queryset or queryset1:
                    message = "Email Address Already exists" 
                else:
                    message = ""
            else :
                message = "Not a Valid Email Address"
        else:
            message = "Kindly enter valid email Address"
        data = {'message': message}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def get_username_bus(request):
    if request.is_ajax() and request.POST:
        username = request.POST.get("username", "")
        message = ""
        if username != '':
            queryset = IndividualRegister.objects.filter(username=username)
            queryset1 = BusinessRegister.objects.filter(username=username)
            if queryset or queryset1:
                message = "User Name Already exists" 
            else:
                message = ""
        else:
            message = "Kindly enter valid user name"
        data = {'message': message}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def get_pwd_bus(request):
    if request.is_ajax() and request.POST:
        re_pwd = request.POST.get("re_pwd", "")
        data = {'message': re_pwd}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def getemail_ind(request):
    if request.is_ajax() and request.POST:
        email = request.POST.get("email", "")
        message = ""
        if email != '':
            if '@' in email :
                queryset = IndividualRegister.objects.filter(email=email)
                queryset1 = BusinessRegister.objects.filter(primary_email=email)
                if queryset or queryset1:
                    message = "Email Address Already exists" 
                else:
                    message = ""
            else :
                message = "Not a Valid Email Address"
        else:
            message = "Kindly enter valid email Address"
        data = {'message': message}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def get_username_ind(request):
    if request.is_ajax() and request.POST:
        username = request.POST.get("username", "")
        message = ""
        if username != '':
            queryset = IndividualRegister.objects.filter(username=username)
            queryset1 = BusinessRegister.objects.filter(username=username)
            if queryset or queryset1:
                message = "User Name Already exists" 
            else:
                message = ""
        else:
            message = "Kindly enter valid user name"
        data = {'message': message}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def get_pwd_ind(request):
    if request.is_ajax() and request.POST:
        re_pwd = request.POST.get("re_pwd", "")
        data = {'message': re_pwd}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponseRedirect('/')

def subcat(request):
    if request.is_ajax() and request.POST:
        category = request.POST.get("subcat", "")
        subcat = BSubCategory.objects.filter(category_id=category)
        data = serializers.serialize("json", subcat)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseRedirect('/')

