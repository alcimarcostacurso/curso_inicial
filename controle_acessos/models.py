from django.contrib.auth.models import User
from django.db import models

from setores.models import Setor
from visitantes.models import Visitante


class ControleAcesso(models.Model):
    visitante = models.ForeignKey(Visitante, null=False,
                                  blank=False,
                                  verbose_name='Visitante',
                                  on_delete=models.CASCADE)
    data_entrada = models.DateField(null=False, blank=False,
                                    verbose_name='Data de entrada')
    hora_entrada = models.TimeField(null=False, blank=False,
                                    verbose_name='Hora de entrada')
    data_saida = models.DateField(null=True, blank=True,
                                  verbose_name='Data de saída')
    hora_saida = models.TimeField(null=True, blank=True,
                                  verbose_name='Hora de saída')
    setores = models.ManyToManyField(Setor, verbose_name='Setores', blank=False)
    user = models.ForeignKey(User, null=False, blank=False, verbose_name='Usuáripo',
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.visitante.nome

    class Meta:
        verbose_name = 'Controle de acesso'
        verbose_name_plural = 'Controles de acessos'


