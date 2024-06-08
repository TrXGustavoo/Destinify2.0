from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

class LugarTuristico(models.Model):
    nome = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    estado = models.CharField(max_length=255,  blank=True, null=True, default='')
    cidade = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="lugares/", blank=True, null=True)
    descricao = models.TextField()
    nota = models.DecimalField(max_digits=2, decimal_places=1, null=True, default=0)
    
    comentarios = models.ManyToManyField('Comentario', blank=True)
    
    def __str__(self):
        return self.nome


class Comentario(models.Model):
    texto = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False)
    destino = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE, related_name='comentarios_destinos', blank=True, null=True) 

    
    rating = models.IntegerField(default=0,null=True)
    
    def __str__(self):
        return self.texto
