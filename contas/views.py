from django.shortcuts import render, redirect
from .FormFilme import FormFilme
from .models import Filme
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'contas/home.html')

def listagemFilmes(request):
    data = {}
    data['filmes'] = Filme.objects.all()
    return render(request, 'contas/filme.html', data)

def novoFilme(request):
    data = {}
    form = FormFilme(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagemFilmes')

    data['form'] = form
    return render(request, 'contas/formFilme.html', data)