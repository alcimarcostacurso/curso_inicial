from cpf_field.models import CPFField
from django.db import models
from stdimage import StdImageField


class Visitante(models.Model):
    MASCULINO = "M"
    FEMININO = "F"

    SEXO_CHOICES = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino')
    )

    foto = StdImageField(upload_to='fotos_visitantes', variations={
        'avatar': (100, 100, True),
    }, delete_orphans=True, null=True, blank=True, verbose_name='Foto do visitante')
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome')
    cpf = CPFField(verbose_name='CPF', null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=15, null=False, blank=False, verbose_name='Telefone')
    data_nascimento = models.DateField(null=False, blank=False, verbose_name='Data de nascimento')
    sexo = models.CharField(max_length=1, null=False, blank=False, verbose_name='Sexo', choices=SEXO_CHOICES)
    endereco = models.TextField(null=True, blank=True, verbose_name='Endereço')

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cpf)
