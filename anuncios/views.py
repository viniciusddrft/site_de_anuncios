from django.shortcuts import render
from django.http import HttpResponse


from .models import Categoria
from .models import Anuncio

def home(request):
    categorias = Categoria.objects.all()

    anuncios = Anuncio.objects.all()

    return render(request, 'home.html', {'categorias': categorias,
                                        'anuncios':anuncios})