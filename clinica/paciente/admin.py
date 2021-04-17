"""Paciente registers"""
#Django
from django.contrib import admin
#Paciente models
from .models import Sexo
from .models import Religion
from .models import EstadoCivil
from .models import TipoFamiliar
from .models import NumeroContacto
from .models import Paciente
from .models import Familiar
from .models import DatosClinicos

# Register your models here.

admin.site.register(Sexo)
admin.site.register(Religion)
admin.site.register(EstadoCivil)
admin.site.register(TipoFamiliar)
admin.site.register(NumeroContacto)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(DatosClinicos)

