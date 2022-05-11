from django.contrib import admin
from .models import Candidato, Eleicao, Voto

# Register your models here.


admin.site.register(Candidato)
admin.site.register(Eleicao)
admin.site.register(Voto)