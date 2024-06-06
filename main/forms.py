from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto']  # Adicione 'foto' aos campos do formulário
