from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro')
    # path('cadastro-idoso/', views.elder_cadastro, name='elder_cadastro'),
    # path('cadastro-voluntario/', views.voluntario_cadastro, name='voluntario_cadastro'),
]