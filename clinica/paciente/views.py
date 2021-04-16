"""Vistas de la Aplicacion Empleado"""
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Paciente
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndicePaciente(generic.ListView):
    """Vista Genèrica de Tabla Pacientes"""
    template_name = 'paciente/paciente_index.html'
    context_object_name = 'lista_paciente'
    model = Paciente
    paginate_by = 5

class DescripcionPaciente(generic.DetailView):
    """Muestra una descripcion del Paciente Seleccionado"""
    template_name = 'paciente/paciente_descripcion.html'
    context_object_name = 'descripcion_paciente'
    model = Paciente

class CrearPaciente(generic.ListView):
    #Muestra el formulario para crear un nuevo Paciente
    model = Paciente
    """form_class = EmpleadoForm"""
    template_name = 'paciente/paciente_editar.html'
    success_url = reverse_lazy('paciente:paciente_index')

    """def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('empleado:mensaje_empleado'))
        else:
            return render(request, 'empleado/nuevo_empleado.html',
                          {'form': form, 'error_date': 'Debes ingresar una fecha válida'})"""

"""class EditarEmpleado(LoginRequiredMixin, generic.UpdateView):
    #Actualiza el registro de un Empleado
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')"""

class BusquedaPaciente(generic.ListView):
    """Busca un Paciente"""
    model = Paciente
    context_object_name = 'busqueda_paciente'
    template_name = 'paciente/paciente_busqueda.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paciente.objects.filter(
           Q(id_paciente__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query)| 
           Q(departamento__icontains=query) | Q(municipio__icontains=query) | Q(id_sexo__icontains=query)| 
           Q(id_numero_contacto__icontains=query))
        return object_list





