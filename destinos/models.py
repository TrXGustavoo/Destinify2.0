from django.db import models
from django.contrib.auth.models import User

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, 'QUATOR'),
    (5, 'CINCO'),
    
)

class LugarTuristico(models.Model):
    nome = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    # fotos = models.ManyToManyField('Foto')
    descricao = models.TextField()
    nota = models.DecimalField(max_digits=2, decimal_places=1, null=True, default=0)
    
    comentarios = models.ManyToManyField('Comentario', blank=True)

# class Foto(models.Model):
#     imagem = models.ImageField(upload_to='lugares_turisticos/')
#     legenda = models.CharField(max_length=255)

class Comentario(models.Model):
    texto = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False)
    destinoA = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(default=0,null=True)
    
    def __str__(self):
        return self.texto

