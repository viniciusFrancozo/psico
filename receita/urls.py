from django.urls import path
from . import views

urlpatterns = [
    path("receita/", views.receita_view, name="receita"),
    path('remedio/', views.cadastrar_remedio, name='remedio')
]
