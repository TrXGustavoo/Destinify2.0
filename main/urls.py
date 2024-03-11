from django.contrib import admin
from django.urls import path, include
from main import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/cadastro', views.cadastro, name='cadastro'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    # path('perfil/<int:user_id>/', views.perfil, name='perfil'),

]
