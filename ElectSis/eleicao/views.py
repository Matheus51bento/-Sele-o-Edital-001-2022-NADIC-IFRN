from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "menu.html")

def cad_eleicao(request):
    return render(request, "cadastro_eleicao.html")

def cad_candidadto(request):
    return render(request, "cadastro_candidato.html")