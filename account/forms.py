from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'groups'
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha e confirmação de senha devem ser iguais!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'groups'
        )
