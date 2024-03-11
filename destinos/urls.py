from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.decorators import login_required
from destinos import views

urlpatterns = [
    path('destinos/', login_required(views.destinos), name='destinos'),
    path('destino/<int:destino_id>/', views.destino_detalhe, name='destino_detalhe'),
    path('destinos/destino/<int:destino_id>/comentario/create/', views.destino_comentario_create, name='destino_comentario_create'),

]
