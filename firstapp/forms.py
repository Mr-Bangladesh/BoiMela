from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#My forms

class AdvertisementForm(forms.ModelForm):
    
    class Meta:
        model = Advertisement
        fields = "__all__"
        #fields = ['Book_Name', 'Authors_Name']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

