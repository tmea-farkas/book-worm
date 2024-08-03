from allauth.account.adapter import DefaultAccountAdapter
from .models import Profile
from django.contrib.auth.models import User


class BookwormAccountAdapter(DefaultAccountAdapter):
    # def confirm_email(self, request, email_address):
    #     user = User.objects.get(emailaddress=email_address)
    #     try:
    #         profile = Profiles.objects.get(user=user)
    #     except:
    #         user_profile = Profile(user=user)
    #         user_profile.save()
    #     return super().confirm_email(request, email_address)

    def is_email_verified(self, request, email_address):
        print('okay')
        user = User.objects.get(email=email_address)
        try:
            profile = Profiles.objects.get(user=user)
        except:
            user_profile = Profile(user=user)
            user_profile.save()
        return True

    def get_login_redirect_url(self, request):
        print('hiya')
        user = request.user
        profile = Profile.objects.get(user=user)
        path = f'profiles/profile/{profile.id}/'
        return path
