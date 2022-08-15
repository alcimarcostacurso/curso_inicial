from django.db import models

from gerencias.models import Gerencia


class Setor(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    telefone = models.CharField(max_length=14, null=False, blank=False, verbose_name='Telefone')
    sigla = models.CharField(max_length=10, null=False, blank=False, verbose_name='Sigla')
    gerencia = models.ForeignKey(Gerencia, null=False, blank=False, verbose_name='Gerência',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome
