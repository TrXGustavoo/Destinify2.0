from django.shortcuts import render
from .models import LugarTuristico
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm, LugarTuristicoForm
from django.db.models import Avg
from django.contrib.auth.models import User
from main.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def destinos(request):
    # Obter parâmetros da requisição
    pais = request.GET.get("pais", "")
    cidade = request.GET.get("cidade", "")
    nome = request.GET.get("nome", "")
    ordenar_por_nota = request.GET.get("ordenar_por_nota", False)

    # Filtrar destinos
    destinos = LugarTuristico.objects.all()
    if pais:
        destinos = destinos.filter(pais__icontains=pais)
    elif cidade:
        destinos = destinos.filter(cidade__icontains=cidade)
    elif nome:
        destinos = destinos.filter(nome__icontains=nome)
    # Ordenar por nota
    elif ordenar_por_nota:
        destinos = destinos.order_by("-nota")
    elif request.GET.get("resetar"):
        return render(request, "destinos.html", {"destinos": destinos})

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
    comentarios = Comentario.objects.filter(destinoA=destino_id).order_by(
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
    print(profile)
    usuario = User
    print(usuario)

    return render(
        request,
        "destinoDetalhado.html",
        {"destino": destino, "comentarios": comentarios, "fotos_perfil": fotos_perfil},
    )

@login_required
def destino_comentario_create(request, destino_id):
    destino = get_object_or_404(LugarTuristico, pk=destino_id)
    if request.method == "POST":
        texto = request.POST.get("comentario_texto")
        rating = request.POST.get("star-rating")
        comentario = Comentario(
            texto=texto, usuario=request.user, destinoA=destino_id, rating=rating
        )
        comentario.save()
        return redirect("destino_detalhe", destino.id)
    else:
        form = ComentarioForm()
    foto_destino = destino

    return render(
        request, "destino_comentario_create.html", {"destino": destino, "form": form}
    )
