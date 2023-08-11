# forms.py

# forms.py
from django import forms
from .models import AndroidApp,Admin
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomAndroidAppForm(forms.ModelForm):
    class Meta:
        model = AndroidApp
        fields = ['name', 'points','image','link','category','subcategory']



class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['admin_name','email','password','confirm_password']

class AdminLoginForm(forms.Form):
    admin_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')