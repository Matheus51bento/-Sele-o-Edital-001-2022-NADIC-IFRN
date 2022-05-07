from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name="inicio"),
    path('cadastro/eleicoes/', cad_eleicao, name="cadastro eleicao"),
    path('cadastro/candidato', cad_candidadto, name="cadastro candidato")

]