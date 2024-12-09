from django import forms
from .models import Membership, Product


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['user', 'duration']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['vendor', 'name', 'price', 'image']