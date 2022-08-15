from django import forms

from setores.models import Setor


class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = '__all__'
