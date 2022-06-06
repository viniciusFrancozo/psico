from django.urls import path
from . import views

urlpatterns = [
    path('<int:mes>/<int:ano>/', views.calendario, name='calendario'),
    path('<int:mes>/<int:ano>/<int:dia>', views.calendario_visualizar, name='calendario_visualizar'),
]
