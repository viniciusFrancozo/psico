from django import forms
from django.forms import ModelForm
from .models import Consulta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ('data','horario')
