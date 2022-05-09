from django.shortcuts import render
from .forms import CandidatoForm
from .models import Candidato
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "menu.html")

def cad_eleicao(request):
    return render(request, "cadastro_eleicao.html")

def cad_candidadto(request):

    if request.method == "POST":

        forms = CandidatoForm(request.POST)

        if forms.is_valid():
            # ['nome', 'data_nascimento', 'endereco', 'cpf']
            nome = forms.cleaned_data['nome']
            data_nascimento = forms.cleaned_data['data_nascimento']
            endereco = forms.cleaned_data['endereco']
            cpf = forms.cleaned_data['cpf']

            search = Candidato.objects.get(cpf=cpf)

            if not search:

                Candidato.objects.create(nome=nome, data_nascimento=data_nascimento, endereco=endereco, cpf=cpf)
                messages.success(request, 'Candidato cadastrado')

            else:
                messages.error(request, "Candidato já existe")

        else:
            messages.warning(request, 'Formulário inválido')

        return render(request, "cadastro_candidato.html")

    else:

        form = CandidatoForm

        return render(request, "cadastro_candidato.html", {'form': form})