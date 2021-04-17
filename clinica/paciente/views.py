"""Vistas de la Aplicacion Empleado"""
#Django
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q


#Apps
from .models import Paciente
from .forms import PacienteForm

# Create your views here.
class IndicePaciente(generic.ListView, LoginRequiredMixin):
    """Vista Genèrica de Tabla Pacientes"""
    template_name = 'paciente/paciente_index.html'
    context_object_name = 'lista_paciente'
    model = Paciente
    paginate_by = 5


class DescripcionPaciente(generic.DetailView, LoginRequiredMixin):
    """Muestra una descripcion del Paciente Seleccionado"""
    template_name = 'paciente/paciente_descripcion.html'
    context_object_name = 'descripcion_paciente'
    model = Paciente


class CrearPaciente(generic.ListView, LoginRequiredMixin):
    """Muestra el formulario para crear un nuevo Paciente"""
    model = Paciente
    """form_class = EmpleadoForm"""
    template_name = 'paciente/paciente_editar.html'
    success_url = reverse_lazy('paciente:paciente_index')


class EditarPaciente(LoginRequiredMixin, generic.UpdateView):
    """Actualiza el registro de un Empleado"""
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')


class BusquedaPaciente(generic.ListView, LoginRequiredMixin):
    """Busca un Paciente"""
    model = Paciente
    context_object_name = 'busqueda_paciente'
    template_name = 'paciente/paciente_busqueda.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paciente.objects.filter(
           Q(id_paciente__icontains=query) |
           Q(nombre__icontains=query) |
           Q(apellido__icontains=query)|
           Q(departamento__icontains=query) |
           Q(municipio__icontains=query) |
           Q(id_sexo__icontains=query)|
           Q(id_numero_contacto__icontains=query))
        return object_list
