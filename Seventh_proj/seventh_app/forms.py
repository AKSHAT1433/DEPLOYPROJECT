from django import forms
from django.contrib.auth.models import User
from seventh_app.models import UserInfo
from django.forms import ModelForm
class UserForms(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields = ('username', 'email', 'password')



class UserInfoForms(ModelForm):
    class Meta:
        model=UserInfo
        fields=('portfolio','profile_pic')

