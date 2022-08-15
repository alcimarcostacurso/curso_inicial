# Generated by Django 3.2.10 on 2022-02-07 21:20

import cpf_field.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gerencias', '0002_gerencia_ativa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('matricula', models.CharField(blank=True, max_length=6, null=True, verbose_name='Matrícula')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('endereco', models.TextField(blank=True, null=True, verbose_name='Endereço')),
                ('gerencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gerencias.gerencia', verbose_name='Gerência')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='setores.setor', verbose_name='Setor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]