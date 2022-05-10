from django.shortcuts import render
from .forms import CandidatoForm, EleicaoForm
from .models import Candidato, Eleicao
from django.contrib import messages
from datetime import datetime
from datetime import date

# Create your views here.

def index(request):
    return render(request, "menu.html")

def voto_view(request, id):

    return render(request, "voto.html")

def pleitos_view(request):

    eleicoes = Eleicao.objects.all()

    hoje = date.today()

    cadastradas = []

    finalizadas = []

    em_andamento = []

    for pleito in range(len(eleicoes)):

        if eleicoes[pleito].data_inicial < hoje:

            cadastradas.append(eleicoes[pleito])

        elif eleicoes[pleito].data_final > hoje:

            em_andamento.append(eleicoes[pleito])

        else:

            finalizadas.append(eleicoes[pleito])

    return render(request, "list_pleitos.html", {'cadastradas': cadastradas, 'andamento': em_andamento, 'finalizadas': finalizadas})

def cad_eleicao(request):

    candidatos = Candidato.objects.all()

    if request.method == 'POST':

        if "candidatos" in request.POST:
            qtd = int(request.POST['qtd_candidatos'])
            lis_candidatos = request.POST.getlist('candidatos')
            print(request.POST)

            if len(lis_candidatos) == qtd:

                nome = request.POST['nome']

                if not len(Eleicao.objects.filter(nome=nome)):

                    candidatos_form = candidatos.filter(cpf__in=lis_candidatos)

                    data_final = datetime.strptime(request.POST['data_final'], '%Y-%m-%d').date()
                    data_inicial = datetime.strptime(request.POST['data_inicial'], '%Y-%m-%d').date()

                    if data_inicial > data_final or data_inicial == data_final:

                        messages.error(request, "Selecione um período válido")

                    else:

                        eleicao = Eleicao(nome=nome, data_inicial=data_inicial, data_final=data_final)
                        eleicao.save()
                        for i in range(len(candidatos_form)):
                            eleicao.candidatos.add(candidatos_form[i])

                else:
                    messages.error(request, "Já existe um pleito com esse nome")

            else:
                messages.error(request, "A quantidade de candidatos está incorreta")

        else:
            messages.error(request, "Selecione os candidatos")


        return render(request, "cadastro_eleicao.html", {'candidatos':candidatos})

    else:
        form = EleicaoForm()

        return render(request, "cadastro_eleicao.html", {'form':form, 'candidatos':candidatos   })

def cad_candidadto(request):

    if request.method == "POST":

        forms = CandidatoForm(request.POST)

        if forms.is_valid():
            # ['nome', 'data_nascimento', 'endereco', 'cpf']
            nome = forms.cleaned_data['nome']
            data_nascimento = forms.cleaned_data['data_nascimento']
            endereco = forms.cleaned_data['endereco']
            cpf = forms.cleaned_data['cpf']

            search = Candidato.objects.filter(cpf=cpf)

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