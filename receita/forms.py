from django import forms
from django.forms import ModelForm
from .models import Remedio, Receita


class RemedioForm(ModelForm):
    class Meta:
        model = Remedio
        fields = ('nome', 'dose')


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ('paciente','remedio','quantidade','data_fim')
