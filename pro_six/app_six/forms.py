from django import forms
from django.contrib.auth.models import User
from app_six.models import UserProfileInfo

# This class belomgs to the User module
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


# This class belongs to the model class imported from models.py

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")
