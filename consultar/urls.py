from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.consultar, name='consultar'),
]
