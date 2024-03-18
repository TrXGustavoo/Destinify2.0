from django.shortcuts import render
from .models import LugarTuristico
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm
from django.db.models import Avg



def destinos(request):
    # Obter parâmetros da requisição
    pais = request.GET.get('pais', '')
    cidade = request.GET.get('cidade', '')
    nome = request.GET.get('nome', '')
    ordenar_por_nota = request.GET.get('ordenar_por_nota', False)

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
        destinos = destinos.order_by('-nota')
    elif request.GET.get('resetar'):
        return render(request, 'destinos.html', {'destinos': destinos})

    return render(request, 'destinos.html', {'destinos': destinos})


from django.shortcuts import render, get_object_or_404

def destino_detalhe(request, destino_id):
    destino = get_object_or_404(LugarTuristico, pk=destino_id)
    comentarios = Comentario.objects.filter(destinoA=destino_id).order_by('-data_criacao')
    
    soma_notas = 0
    for comentario in comentarios:
        soma_notas += comentario.nota
    
    if comentarios.exists():
        media_nota = soma_notas / comentarios.count()
        destino.nota = round(media_nota, 1)
        destino.save()
    

    return render(request, 'destinoDetalhado.html',{'destino': destino, 'comentarios': comentarios})


def destino_comentario_create(request, destino_id):
    destino = get_object_or_404(LugarTuristico, pk=destino_id)
    if request.method == 'POST':
        texto = request.POST.get("comentario_texto")
        nota = request.POST.get("comentario_nota")
        rating = request.POST.get("star-rating")
        print(rating)
        comentario = Comentario(
            texto = texto,
            nota = nota,
            usuario = request.user,
            destinoA = destino_id,
            rating = rating
        )
        comentario.save()
        return redirect('destino_detalhe', destino.id)
    else:
        form = ComentarioForm()
    return render(request, 'destino_comentario_create.html', {'destino': destino, 'form': form})
