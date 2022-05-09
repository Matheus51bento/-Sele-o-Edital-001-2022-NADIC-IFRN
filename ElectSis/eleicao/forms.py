from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from django.db.models.base import Model
from django.forms.models import ALL_FIELDS, ModelForm
from .models import *
from django import forms


class CandidatoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder': ('Digite o nome completo'), 'class': ('form-control')})
        self.fields['data_nascimento'].widget.attrs.update({'placeholder': "Data de Nascimento",'class': ('form-control')})
        self.fields['endereco'].widget.attrs.update({'placeholder': ('Digite o endereço'), 'class': ('form-control')})
        self.fields['cpf'].widget.attrs.update({'placeholder': ('Digite o CPF'), 'class': ('form-control')})

    class Meta:
        model = Candidato
        fields = ['nome', 'data_nascimento', 'endereco', 'cpf']
        widgets = {
            'data_nascimento': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento',
                                                    'type': 'date'}),}
class EleicaoForm(ModelForm):

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':('Digite o nome do Pleito'), 'class':('form-control')})
        self.fields['data_inicial'].widget.attrs.update(
            {'placeholder': "Data de inicio", 'class': ('form-control')})
        self.fields['data_final'].widget.attrs.update(
            {'placeholder': "Data de finalização", 'class': ('form-control')})

    class Meta:
        model = Eleicao
        fields = ["nome", "data_inicial", "data_final"]
        widgets = {
            'data_inicial': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Data de inicio',
                                                    'type': 'date'}),
            'data_final': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Data de fim',
                                                    'type': 'date'}
                                                                )}

