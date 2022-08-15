from django import forms
from tempus_dominus.widgets import DatePicker

from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=DatePicker)

    class Meta:
        model = Visitante
        fields = (
            'foto',
            'nome',
            'cpf',
            'telefone',
            'data_nascimento',
            'sexo',
            'endereco'
        )