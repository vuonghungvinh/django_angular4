from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from allauth.account.signals import user_signed_up, user_logged_in
from allauth.socialaccount.models import SocialAccount
from accounts.models import IndividualAccount
import hashlib
from allauth.socialaccount.signals import social_account_added

@receiver(user_signed_up)
def social_login_fname_lname_profilepic(sociallogin, user, **kwargs):
    preferred_avatar_size_pixels=256
    picture_url = "http://www.gravatar.com/avatar/{0}?s={1}".format(
        hashlib.md5(user.email.encode('UTF-8')).hexdigest(),
        preferred_avatar_size_pixels
    )
    if sociallogin:
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'twitter':
            name = sociallogin.account.extra_data['name']
            name = sociallogin.account.extra_data['name']
            user.first_name = name.split()[0]
            user.last_name = name.split()[1]
            pic = sociallogin.account.extra_data['profile_image_url_https']
            if pic:
                picture_url = pic

        if sociallogin.account.provider == 'facebook':
            f_name = sociallogin.account.extra_data['first_name']
            l_name = sociallogin.account.extra_data['last_name']
            # email = sociallogin.account.extra_data['email']
            if f_name:
                user.first_name = f_name
            if l_name:
                user.last_name = l_name
            # if email:
                # user.email = email

            #verified = sociallogin.account.extra_data['verified']
            picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                sociallogin.account.uid, preferred_avatar_size_pixels)

        if sociallogin.account.provider == 'google':
            f_name = sociallogin.account.extra_data['given_name']
            l_name = sociallogin.account.extra_data['family_name']
            uname = sociallogin.account.extra_data['name']
            if f_name:
                user.first_name = f_name
            if l_name:
                user.last_name = l_name
            if uname:
                user.username = uname
            #verified = sociallogin.account.extra_data['verified_email']
            picture_url = sociallogin.account.extra_data['picture']
    user.save()
    profile = IndividualAccount(user=user, avatar=picture_url, type=False)
    profile.save()   


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # data = SocialAccount.objects.filter(user=instance, provider='google')
        # print(data)
        Token.objects.create(user=instance)

