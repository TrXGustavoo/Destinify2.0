from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.messages import constants
from django.contrib import messages, auth
from destinos.models import Comentario
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required



class HomeView(TemplateView):
    template_name = "index.html"


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        first_name = request.POST.get("nome")
        last_name = request.POST.get("sobrenome")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("telefone")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")
        rua = request.POST.get("rua")
        estado = request.POST.get("estado")
        cidade = request.POST.get("cidade")

        if not senha == confirmar_senha or not senha:
            messages.add_message(request, constants.ERROR, "Senhas não conferem ou não preenchidas")
            return redirect("cadastro")
        if not username:
            messages.add_message(request, constants.ERROR, "Nome de usuario nao pode estar vazio")
            return redirect("cadastro")
        if not email:
            messages.add_message(request, constants.ERROR, "Email nao pode estar vazio")
            return redirect("cadastro"),
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, "Usuario já existe")
            return redirect("cadastro")
        try:
            user = User.objects.create_user(username=username, password=senha, email=email, first_name=first_name, last_name=last_name)
            endereco = Endereco.objects.create(rua=rua, estado=estado, cidade=cidade)
            profile = Profile.objects.create(user=user, telefone=phone, endereco=endereco)
            auth.login(request, user)
            return redirect("home")
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

@login_required
def perfil(request, username):
    profile = get_object_or_404(User, username=username)
    comentarios = (
        Comentario.objects.all().filter(usuario__id=profile.id).order_by("-data_criacao")
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile.profile)
        if form.is_valid():
            form.save()
            return redirect('perfil', username=username)
    else:
        form = ProfileForm(instance=profile.profile)

    fotos_perfil = Profile.objects.filter(user=profile)
    
    if request.user == profile: 
        return render(request, "perfil.html", {"comentarios": comentarios, "perfil": profile, "form": form, "fotos_perfil": fotos_perfil, "show_form": True}) 
        
    else:
        return render(request, "perfil.html", {"comentarios": comentarios, "perfil": profile, "fotos_perfil": fotos_perfil, "show_form": False})  


class SobreView(TemplateView):
    template_name = "sobreNos.html"