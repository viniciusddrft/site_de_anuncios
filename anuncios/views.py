from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



from .models import Categoria
from .models import Anuncio

def home(request):
    categorias = Categoria.objects.all()

    ultimos_anuncios_ou_pesquisados = Anuncio.objects.all()[:12]

    search = request.GET.get('search')
    if search:
        ultimos_anuncios_ou_pesquisados = Anuncio.objects.filter(titulo__icontains=search)#isso faz os ultimos anuncios receberem os resultados das pesquisas



    return render(request, 'home.html', {'categorias': categorias,
                                        'anuncios':ultimos_anuncios_ou_pesquisados})


def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    categorias = Categoria.objects.all()
    
    anuncios = Anuncio.objects.filter(categoria=categoria)

    return render(request, 'home.html', {'categorias' : categorias,
                                        'anuncios' : anuncios,
                                        'categoria' : categoria})


def anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, id=anuncio_id)

    categorias = Categoria.objects.all()

    return render(request, 'anuncio.html', {'categorias' : categorias,
                                        'anuncio' : anuncio})