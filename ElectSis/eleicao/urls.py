from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name="inicio"),
    path('cadastro/eleicoes/', cad_eleicao, name="cadastro eleicao"),
    path('cadastro/candidato', cad_candidadto, name="cadastro candidato"),
    path('pleitos', pleitos_view, name='pleitos'),
    path('votacao/<int:id>', voto_view, name="votar"),
    path('resultado/<int:id>', resultados_view, name="resultado")

]