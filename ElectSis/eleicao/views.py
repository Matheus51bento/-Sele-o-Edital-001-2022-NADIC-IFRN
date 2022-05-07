from django.shortcuts import render
from .forms import CandidatoForm

# Create your views here.

def index(request):
    return render(request, "menu.html")

def cad_eleicao(request):
    return render(request, "cadastro_eleicao.html")

def cad_candidadto(request):

    if request.method == "POST":

        forms = CandidatoForm(request.POST)

        if forms.is_valid():
            print("VALIDOUUUUU")

        return render(request, "cadastro_candidato.html")

    else:

        form = CandidatoForm

        return render(request, "cadastro_candidato.html", {'form': form})