from rest_framework import serializers
from .models import IndividualAccount, BusinessAccount
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation

class IndividualSerializer(serializers.ModelSerializer):
	avatar = serializers.ImageField(required = False)
	profile_img = serializers.ImageField(required = False)
	class Meta:
		model = IndividualAccount
		fields = ('id', 'user', 'type', 'position', 'address', 'country', 'city', 'secondary_contact_no', 'gender', 'dateofbirth', 'contact_no', 'personal_status', 'contact_status', 'profile_img', 'avatar')

class BusinessSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(required=True)
    business_alias = serializers.CharField(required=True)
    hq_city = serializers.CharField(required=True)
    hq_country = serializers.CharField(required=True)
    
    class Meta:
        model = BusinessAccount
        fields = ('id', 'user', 'business_name', 'business_alias', 'type', 'position', 'address', 'country', 'city', 'secondary_contact_no', 'comp_name', 'comp_alias', 'business_type', 'business_sub_category', 'business_address', 'hq_country', 'hq_city', 'hq_address', 'hq_contact_no', 'brief_desc', 'pri_det_status', 'sec_det_status', 'primary_fname', 'primary_lname', 'primary_designation', 'primary_contact_no', 'primary_email', 'secondary_fname', 'secondary_lname', 'secondary_designation', 'secondary_email', 'company_logo')


class UserSerializer(serializers.ModelSerializer):
    business_user = BusinessSerializer(required=False)
    individual_user = IndividualSerializer(required=False)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="Email Address Already exists",)])
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'business_user', 'individual_user')
        # extra_kwargs = {"email":{
        # 	"error_messages":{
        # 		"uniqued": "ffdfsdd"
        # 	}
        # }}
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user