from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class Endereco(models.Model):
    rua = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    # Campos personalizados
    
    foto = models.ImageField(upload_to="geral/img/perfil/", storage=FileSystemStorage(), blank=True, null=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

