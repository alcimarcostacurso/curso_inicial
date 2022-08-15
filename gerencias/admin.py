from django.contrib import admin
from django.contrib.admin import ModelAdmin

from gerencias.models import Gerencia


@admin.register(Gerencia)
class GerenciaAdmin(ModelAdmin):
    list_display = ('nome', 'sigla', 'ativa')
    search_fields = ('nome',)
    list_editable = ['ativa']
    list_filter = ('ativa',)
