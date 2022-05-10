from django.contrib import admin
from .models import Candidato, Eleicao

# Register your models here.


admin.site.register(Candidato)
admin.site.register(Eleicao)