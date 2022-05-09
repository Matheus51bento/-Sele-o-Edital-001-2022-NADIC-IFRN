from django.db import models

# Create your models here.

from django.db import models
from cpf_field.models import CPFField


class Candidato(models.Model):

    cpf = CPFField('cpf', default='000.000.000-00', unique=True)
    nome = models.CharField(verbose_name='Nome Completo', max_length=255, null=False)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.CharField(verbose_name="Endereço", max_length=255, null=False)

class Eleicao(models.Model):

    nome = models.CharField(verbose_name="Nome da Eleição", max_length=80)
    data_inicial = models.DateField(verbose_name="Data Inicial")
    data_final = models.DateField(verbose_name="Data Final")
    candidatos = models.ManyToManyField(Candidato, blank=True)
    _total_candidatos = None

    def __str__(self):
        return '{}'.format(self.nome)
