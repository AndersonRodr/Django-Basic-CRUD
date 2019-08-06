from django.shortcuts import render
from .models import Filme
from django.http import HttpResponse

# Create your views here.

def home(request):
    algumaCoisa = {}
    algumaCoisa["listaCoisa"] = ["Coisa 1", "Coisa 2", "Coisa 3", "Coisa 4", "Coisa 5"]

    return render(request, 'contas/home.html', algumaCoisa)


def listagemFilmes(request):
    data = {}
    data['filmes'] = Filme.objects.all()
    return render(request, 'contas/filme.html', data)