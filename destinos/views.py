
from .models import LugarTuristico, Comentario
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LugarTuristicoForm, ComentarioForm
from django.contrib.auth.models import User
from main.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def destinos(request):
    filters = {}
    for field in ["pais", "cidade", "nome"]:
        value = request.GET.get(field)
        if value:
            filters[f"{field}__icontains"] = value

    if request.GET.get("ordenar_por_nota"):
        destinos = LugarTuristico.objects.filter(**filters).order_by("-nota")
    else:
        destinos = LugarTuristico.objects.filter(**filters)

    return render(request, "destinos.html", {"destinos": destinos})



@user_passes_test(lambda u: u.is_superuser)
def destino_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = LugarTuristicoForm(request.POST, request.FILES)
            if form.is_valid():
                lugar_turistico = form.save()
                return redirect('destinos')
        else:
            form = LugarTuristicoForm()

        return render(request, "destino_create.html", {"form": form})
    return redirect('home')


@login_required
def destino_detalhe(request, destino_id):
    destino = get_object_or_404(LugarTuristico, pk=destino_id)
    comentarios = Comentario.objects.filter(destino=destino_id).order_by(
        "-data_criacao"
    )

    media_nota = 0
    for comentario in comentarios:
        media_nota += comentario.rating

    if comentarios.exists():
        media_nota = media_nota / comentarios.count()
    destino.nota = round(media_nota, 1)
    destino.save()

    profile = get_object_or_404(User, username=request.user.username)
    fotos_perfil = Profile.objects.filter(user=profile)

    return render(
        request,
        "destinoDetalhado.html",
        {"destino": destino, "comentarios": comentarios, "fotos_perfil": fotos_perfil},
    )


@login_required
def destino_comentario_create(request, destino_id):
    destino = get_object_or_404(LugarTuristico, pk=destino_id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.destino = destino
            comentario.save()
            return redirect("destino_detalhe", destino.id)
    else:
        form = ComentarioForm()

    return render(request, "destino_comentario_create.html", {"destino": destino, "form": form})
