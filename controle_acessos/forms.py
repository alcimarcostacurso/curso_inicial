from datetime import date

from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker

from controle_acessos.models import ControleAcesso


class ControleAcessoForm(forms.ModelForm):
    data_entrada = forms.DateField(widget=DatePicker())
    hora_entrada = forms.TimeField(widget=TimePicker())

    class Meta:
        model = ControleAcesso
        fields = (
            'visitante',
            'data_entrada',
            'hora_entrada',
            'setores'
        )

    def clean_visitante(self):
        visitante = self.cleaned_data.get('visitante')
        acessos = ControleAcesso.objects.filter(visitante__id=visitante.id)
        acessos_em_aberto = []
        if acessos:
            for acesso in acessos:
                if not acesso.data_saida:
                    acessos_em_aberto.append(acesso)
        if len(acessos_em_aberto) >= 1:
            raise forms.ValidationError(f'Não é possível cadastrar o acesso do {visitante.nome}, '
                                        f'pois ainda existe a pendência de saída em outro acesso.')
        return visitante

    def clean_data_entrada(self):
        data_atual = date.today()
        data_entrada = self.cleaned_data.get('data_entrada')

        if data_entrada > data_atual:
            raise forms.ValidationError('Data de entrada não pode ser no futuro!')
        if data_entrada < data_atual:
            raise forms.ValidationError('Data de entrada não pode ser no passado!')
        return data_entrada



class ControleAcessoEditForm(forms.ModelForm):
    data_entrada = forms.DateField(widget=DatePicker())
    hora_entrada = forms.TimeField(widget=TimePicker())
    data_saida = forms.DateField(required=False, widget=DatePicker())
    hora_saida = forms.TimeField(required=False, widget=TimePicker())

    class Meta:
        model = ControleAcesso
        fields = (
            'visitante',
            'data_entrada',
            'data_saida',
            'hora_entrada',
            'hora_saida',
            'setores'
        )