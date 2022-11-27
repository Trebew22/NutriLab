from django.contrib import admin
from .models import DadosPaciente, Opcao, Pacientes, Refeicao

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Refeicao)
admin.site.register(Opcao)