from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from destinos import views

urlpatterns = [
    path('', login_required(views.destinos), name='destinos'),
    path('destino/<int:destino_id>/', views.destino_detalhe, name='destino_detalhe'),
    path('destinos/destino/<int:destino_id>/comentario/create/', views.destino_comentario_create, name='destino_comentario_create'),
    path('destinos/destinocreate', views.destino_create, name='destino_create'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)