from django import forms
from .models import Endereco, Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto'] 
        