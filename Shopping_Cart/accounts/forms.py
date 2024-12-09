from django import forms
from django.contrib.auth.models import User
from .models import Vendor

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class VendorRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Vendor
        fields = ['business_name']