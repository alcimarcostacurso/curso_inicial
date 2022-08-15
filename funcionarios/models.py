from cpf_field.models import CPFField
from django.conf import settings
from django.db import models
from stdimage import StdImageField

from gerencias.models import Gerencia
from setores.models import Setor


class Funcionario(models.Model):

    MASCULINO = "M"
    FEMININO = "F"

    SEXO_CHOICES = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino')
    )
    foto = StdImageField(upload_to='fotos_funcionarios', variations={
        'avatar': (100, 100, True),
        'detalhe': (250, 300, True),
        'thumbnail': (400, 600),
    }, delete_orphans=True, blank=True, null=True, verbose_name='Foto do funcionário')
    cpf = CPFField('cpf', null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone')
    matricula = models.CharField(max_length=6, null=True, blank=True, verbose_name='Matrícula')
    sexo = models.CharField(max_length=1, null=True, blank=True, verbose_name='Sexo', choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de nascimento')
    endereco = models.TextField(null=True, blank=True, verbose_name='Endereço')
    gerencia = models.ForeignKey(Gerencia, null=True, blank=True, verbose_name='Gerência', on_delete=models.PROTECT)
    setor = models.ForeignKey(Setor, null=True, blank=True, verbose_name='Setor', on_delete=models.PROTECT)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.user.username
