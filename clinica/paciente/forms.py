'''Formularios de Paciente'''
from datetime import date
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    """Formulario para agregar un nuevo Paciente"""
    class Meta:
        """Especificaciones"""
        model = Paciente

        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'departamento',
            'municipio',
            'direccion',
            'id_religion',
            'id_estado_civil',
            'id_numero_contacto',
            'id_sexo',
        ]

        labels = {
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'departamento':'Departamento',
            'municipio':'Municipio',
            'direccion':'Direccion',
            'id_religion':'Religion',
            'id_estado_civil':'Estado Civil',
            'id_numero_contacto':'Contacto',
            'id_sexo':'Sexo',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Nombres',
                                            'name':'nombre',
                                            'id':'nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control',
                                              'type':'text',
                                              'placeholder':'Apellidos',
                                              'name':'apellido',
                                              'id':'apellido'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control',
                                                      'type':'date',
                                                      'placeholder':'Fecha',
                                                      'name':'fecha_nacimiento'}),
            'departamento':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Departamento',
                                            'name':'departamento',
                                            'id':'departamento'}),
            'municipio':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Municipio',
                                            'name':'municipio',
                                            'id':'municipio'}),
            'direccion':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Direccion',
                                            'name':'direccion',
                                            'id':'direccion'}),
            'id_religion':forms.TextInput(attrs={'class':'custom-select',
                                            'name':'religion',}),
            'id_estado_civil':forms.TextInput(attrs={'class':'custom-select',
                                            'name':'estado_civil'}),
            'id_numero_contacto':forms.TextInput(attrs={'class':'custom-select',
                                            'name':'estado_civil'}),
            'id_sexo':forms.Select(attrs={'class':'custom-select',
                                          'name':'sexo'}),
        }

    def clean_fecha_nacimiento(self):
        """Comprueba que el campo de fecha sea mayor o igual a 18 años de edad"""
        cleaned_data = super().clean()
        dob = cleaned_data.get("fecha_nacimiento")
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Must be at least 18 years old to register')
        return dob
       