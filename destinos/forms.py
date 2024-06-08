from django.forms import ModelForm
from .models import Comentario, LugarTuristico
from django import forms

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'rating']
        
        
class LugarTuristicoForm(forms.ModelForm):
    class Meta:
        model = LugarTuristico
        fields = ['nome','pais','estado','cidade','foto','descricao']
    