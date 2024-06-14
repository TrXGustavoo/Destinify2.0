from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.messages import constants
from django.contrib import messages, auth
from destinos.models import Comentario
from .models import *
from destinos.models import LugarTuristico
from django.shortcuts import get_object_or_404
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinos'] = LugarTuristico.objects.all()  # Ou filtre os destinos que você quer exibir
        return context


def cadastro(request):
    if request.method == "GET":
    
        return render(request, 'cadastro.html', {'messages': False})
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
        form = [
            first_name,
            last_name,
            username,
            email,
            phone,
            senha,
            confirmar_senha,
            rua,
            estado,
            cidade,
        ]

        if not username:
            messages.add_message(
                request, constants.ERROR, "Nome de usuario nao pode estar vazio"
            )
            return redirect("cadastro")

        if not senha == confirmar_senha or not senha:
            messages.add_message(
                request, constants.ERROR, "Senhas não conferem ou não preenchidas"
            )
            return redirect("cadastro")
        if not email:
            messages.add_message(request, constants.ERROR, "Email nao pode estar vazio")
            return (redirect("cadastro"),)
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, "Usuario já existe")
            return redirect("cadastro")
        try:
            user = User.objects.create_user(
                username=username,
                password=senha,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            endereco = Endereco.objects.create(rua=rua, estado=estado, cidade=cidade)
            profile = Profile.objects.create(
                user=user, telefone=phone, endereco=endereco
            )
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
        Comentario.objects.all()
        .filter(usuario__id=profile.id)
        .order_by("-data_criacao")
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile.profile)
        if form.is_valid():
            form.save()
            return redirect("perfil", username=username)
    else:
        form = ProfileForm(instance=profile.profile)

    fotos_perfil = Profile.objects.filter(user=profile)

    if request.user == profile:
        return render(
            request,
            "perfil.html",
            {
                "comentarios": comentarios,
                "perfil": profile,
                "form": form,
                "fotos_perfil": fotos_perfil,
                "show_form": True,
            },
        )

    else:
        return render(
            request,
            "perfil.html",
            {
                "comentarios": comentarios,
                "perfil": profile,
                "fotos_perfil": fotos_perfil,
                "show_form": False,
            },
        )
        
class SobreView(TemplateView):
    template_name = "sobreNos.html"
