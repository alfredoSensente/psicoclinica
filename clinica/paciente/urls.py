"""urls Paciente"""
from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.IndicePaciente.as_view(), name='paciente_index'),
    path('busqueda_paciente/', views.BusquedaPaciente.as_view(), name='paciente_busqueda'),
    path('nuevo_paciente/', views.CrearPaciente.as_view(), name='paciente_editar'),
    path('<str:pk>/', views.DescripcionPaciente.as_view(), name='paciente_descripcion'),
    path('editar_paciente/<str:pk>/', views.EditarPaciente.as_view(), name='paciente_editar'),
]
