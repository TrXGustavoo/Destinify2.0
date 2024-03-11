from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.messages import constants
from django.contrib import messages, auth
from destinos.models import Comentario


class HomeView(TemplateView):
    template_name = "index.html"


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "Senhas não conferem")
            return redirect("cadastro")
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, "Usuario já existe")
            return redirect("cadastro")
        try:
            User.objects.create_user(username=username, password=senha, email=email)
            return redirect("login")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do servidor")
            return redirect("cadastro")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, "Logado!")
            return redirect("home")
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou Senha invalidos")
            return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect("home")


def perfil(request, user_id):
    comentarios = (
        Comentario.objects.all().filter(usuario__id=user_id).order_by("-data_criacao")
    )
    print('comentarios')
    return render(request, "perfil.html", {"comentarios": comentarios})
