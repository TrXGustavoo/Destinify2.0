from django.contrib import admin
from django.urls import path, include
from main import views
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/cadastro', views.cadastro, name='cadastro'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('perfil/<username>/', views.perfil, name='perfil'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
