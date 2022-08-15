from django import forms

from gerencias.models import Gerencia


class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields = '__all__'
