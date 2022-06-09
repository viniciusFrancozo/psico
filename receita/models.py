from django.db import models
from cadastro.models import Pessoa
import datetime
# Create your models here.


class Remedio(models.Model):
    nome = models.CharField(max_length=50, null=False)
    dose = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    remedio = models.ManyToManyField(Remedio)
    paciente = models.ForeignKey(Pessoa, on_delete=models.RESTRICT, blank=True, null=True)
    quantidade = models.CharField(max_length=200, null=False)
    data_expedicao = models.DateTimeField(default=datetime.datetime.now(), null=False)
    data_fim = models.DateField(null=False)
