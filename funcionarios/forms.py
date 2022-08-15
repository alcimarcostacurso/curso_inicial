from django import forms
from django.core.exceptions import ValidationError
from tempus_dominus.widgets import DatePicker

from funcionarios.models import Funcionario
from setores.models import Setor


class FuncionarioForm(forms.ModelForm):
    telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "82 99999-9999"}))
    matricula = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "3001-1"}))
    data_nascimento = forms.DateField(widget=DatePicker())

    class Meta:
        model = Funcionario
        fields = (
            'cpf',
            'telefone',
            'matricula',
            'sexo',
            'data_nascimento',
            'endereco',
            'gerencia',
            'setor',
            'user',
            'foto'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.gerencia:
            self.fields['setor'].queryset = Setor.objects.filter(gerencia=self.instance.gerencia)





