from django.db import models


class Gerencia(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    sigla = models.CharField(max_length=10, null=False, blank=False, verbose_name='Sigla')
    ativa = models.BooleanField(null=False, blank=False, verbose_name='Ativa', default=True)

    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'

    def __str__(self):
        return self.nome
