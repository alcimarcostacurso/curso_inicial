from django.contrib import admin
from django.contrib.admin import ModelAdmin

from setores.models import Setor


@admin.register(Setor)
class SetorAdmin(ModelAdmin):
    list_display = ('nome', 'telefone', 'sigla', 'gerencia')
