from django.contrib import admin
from .models import Consulta

# Register your models here.

@admin.register(Consulta)
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('id','cliente_id','psicologo_id',)
