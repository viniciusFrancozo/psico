from django.db import models

# Create your models here.
class Consulta(models.Model):
    data = models.DateField(null=False)
    horario = models.TimeField(null=False)
