from django import forms
from django.forms import ModelForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa, Psicologo
from django.contrib.messages.views import SuccessMessageMixin


class UsuarioForm(SuccessMessageMixin, UserCreationForm):
    cargoChoices = (
        ('PE', 'Cliente'),
        ('PI', 'Psicologo')
    )

    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    cargo = forms.ChoiceField(label='', choices= cargoChoices)
    password1 = forms.CharField(label='', max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='', max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Confirma sua Senha'}))

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'cargo', 'password1', 'password2')
        labels = {
            'email': '',
            'first_name': '',
            'last_name': '',
            'cargo': '',
            'password1': '',
            'password2': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome', 'required': True}),
            'password1': forms.TextInput(attrs={'placeholder': 'Senha'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirme a Senha'}),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.cargo = self.cleaned_data['cargo']

        if commit:
            user.save()
        return user


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ()



class PsicologoForm(ModelForm):
    class Meta:
        model = Psicologo
        fields = ()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    senha = forms.PasswordInput()