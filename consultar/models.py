from django.db import models
from cadastro.models import Pessoa, Psicologo
# Create your models here.
class Consulta(models.Model):
    data = models.DateField(null=False)
    horario = models.TimeField(null=False)

    psicologo_id = models.ForeignKey(Psicologo, null=True, blank=True, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.CASCADE)

    finalizado = models.BooleanField(default=False)