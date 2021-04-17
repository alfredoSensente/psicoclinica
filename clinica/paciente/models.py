"""modelos"""
import datetime
from dateutil.relativedelta import relativedelta
from django.db import models

# Create your models here.

class Sexo(models.Model):
    """Sexo"""
    id_sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=45)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table = 'sexo'


class Religion(models.Model):
    """Religión"""
    id_religion = models.AutoField(primary_key=True)
    nombre_religion = models.CharField(max_length=45)
    direccion_congregacion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_religion

    class Meta:
        db_table = 'religion'


class EstadoCivil(models.Model):
    """Estado Civil"""
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table = 'estado_civil'


class TipoFamiliar(models.Model):
    """Tipo Familiar"""
    id_tipo_familiar = models.AutoField(primary_key=True)
    tipo_familiar = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_familiar

    class Meta:
        db_table = 'tipo_familiar'


class NumeroContacto(models.Model):
    """Numero de Contacto"""
    id_numeros_de_contacto = models.AutoField(primary_key=True)
    numero_contacto = models.CharField(max_length=45)
    nombre_contacto = models.CharField(max_length=45)

    def __str__(self):
        return self.numero_contacto

    class Meta:
        db_table = 'numero_contacto'


class Paciente(models.Model):
    """paciente"""
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    departamento = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    id_religion = models.ForeignKey(Religion, on_delete=models.CASCADE,
                                        db_column='id_religion')
    id_estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE,
                                        db_column='id_estado_civil')
    id_numero_contacto = models.ForeignKey('NumeroContacto', on_delete=models.CASCADE,
                                      db_column='id_numero_contacto')
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, db_column='id_sexo')

    def __str__(self):
        return self.nombre + " " + self.apellido

    def menor_edad(self):
        """Devuelve true si la fecha fue antes de hace 18 años"""
        return self.fecha_nacimiento >= datetime.datetime.now().date() - relativedelta(years=18)

    class Meta:
        db_table = 'paciente'
        unique_together = (('id_paciente', 'id_numero_contacto', 'id_religion',
                            'id_estado_civil', 'id_sexo'),)


class Familiar(models.Model):
    """Familiar"""
    id_familiar = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')
    id_tipo_familiar = models.ForeignKey('TipoFamiliar',
                                         on_delete=models.CASCADE, db_column='id_tipo_familiar')
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    trato = models.TextField(max_length=45)
    vives_con_el = models.BooleanField()
    ocupacion = models.CharField(max_length=45, blank=True, null=True)
    responsable = models.BooleanField()

    def __str__(self):
        return self.nombre+ " " + self.apellido

    class Meta:
        db_table = 'familiar'
        unique_together = (('id_familiar', 'id_paciente', 'id_tipo_familiar'),)


class DatosClinicos(models.Model):
    """Datos Clincos"""
    id_datos_clinicos = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')
    enfermedad = models.BooleanField()
    nombre_enfermedad = models.CharField(max_length=45)
    medicamento = models.CharField(max_length=45)
    tratamiento_previo = models.BooleanField()
    por_que_no_tratamiento = models.CharField(max_length=45, blank=True, null=True)
    motivo = models.CharField(max_length=45)
    periodo = models.CharField(max_length=45)
    alta_antes = models.BooleanField()
    alta_por_que_no = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'datos_clinicos'
        unique_together = (('id_datos_clinicos', 'id_paciente'),)
