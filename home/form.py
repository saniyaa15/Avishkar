from django import forms
from django.db.models import fields
from .models import *

class ContactUsForm (forms.ModelForm):
    class Meta:
        model=ContactUs
        exclude=['']
        fields = ['name','phone','email','query']

class AddProductForm (forms.ModelForm):
    class Meta:
        model=AddProduct
        exclude=['']
        fields = ['name','price','description','image']