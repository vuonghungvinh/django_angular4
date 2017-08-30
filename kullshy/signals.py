# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.conf import settings
# from allauth.account.signals import user_signed_up, user_logged_in
# from accounts.models import IndividualAccount

# @receiver(user_signed_up)
# def social_login_fname_lname_profilepic(sociallogin, user):
#     preferred_avatar_size_pixels=256
#     print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
#     picture_url = "http://www.gravatar.com/avatar/{0}?s={1}".format(
#         hashlib.md5(user.email.encode('UTF-8')).hexdigest(),
#         preferred_avatar_size_pixels
#     )

#     if sociallogin:
#         # Extract first / last names from social nets and store on User record
#         if sociallogin.account.provider == 'twitter':
#             name = sociallogin.account.extra_data['name']
#             user.first_name = name.split()[0]
#             user.last_name = name.split()[1]

#         if sociallogin.account.provider == 'facebook':
#             f_name = sociallogin.account.extra_data['first_name']
#             l_name = sociallogin.account.extra_data['last_name']
#             email = sociallogin.account.extra_data['email']
#             if f_name:
#                 user.first_name = f_name
#             if l_name:
#                 user.last_name = l_name
# 			if email:
# 				user.email = email

#             #verified = sociallogin.account.extra_data['verified']
#             picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
#                 sociallogin.account.uid, preferred_avatar_size_pixels)

#         if sociallogin.account.provider == 'google':
#             f_name = sociallogin.account.extra_data['given_name']
#             l_name = sociallogin.account.extra_data['family_name']
#             if f_name:
#                 user.first_name = f_name
#             if l_name:
#                 user.last_name = l_name
#             #verified = sociallogin.account.extra_data['verified_email']
#             picture_url = sociallogin.account.extra_data['picture']

#     user.save()
#     profile = IndividualAccount(user=user, avatar__url=picture_url)
#     profile.save()   

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
# 	print("1111111111111111111111111111111111111111111111111111111111111111111111111111")
#     if created:
#         Token.objects.create(user=instance)

