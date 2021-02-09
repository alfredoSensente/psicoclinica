from django.db import models
from paciente.models import Paciente

# Create your models here. 
class MotivoConsulta(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    motivo_consulta = models.CharField(max_length=45)
    descripcion_problema = models.CharField(max_length=45)
    paso_algo_antes = models.BooleanField()
    que_paso = models.CharField(max_length=45)
    fecha_consulta = models.DateField()
    alta_consulta = models.BooleanField()
    archivo_consulta = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'motivo_consulta'
        
    def __str__(self):
        return str(self.id_motivo)



class TipoPrueba(models.Model):
    id_tipo_prueba = models.AutoField(primary_key=True)
    nombre_prueba = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_prueba'

    def __str__(self):
        return str(self.nombre_prueba)



class EvaluacionesAdministradas(models.Model):
    id_prueba = models.AutoField(primary_key=True)
    fecha_administracion = models.DateField()
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    id_tipo_prueba = models.ForeignKey(TipoPrueba, on_delete=models.CASCADE, db_column='id_tipo_prueba')
    id_motivo = models.ForeignKey(MotivoConsulta, on_delete=models.CASCADE, db_column='id_motivo')

    class Meta:
        managed = True
        db_table = 'evaluaciones_administradas'
        unique_together = (('id_prueba', 'id_tipo_prueba','id_motivo'),)

    def __str__(self):
        return str(self.id_prueba)



class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    fecha_diagnostico = models.DateField()
    motivo_consulta = models.ForeignKey(MotivoConsulta, on_delete=models.CASCADE, db_column='motivo_consulta')

    class Meta:
        managed = True
        db_table = 'diagnostico'

    def __str__(self):
        return str(self.id_diagnostico)



class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha_cita = models.DateField()
    realizada = models.BooleanField()
    descripcion = models.CharField(max_length=45)
    otros_indicacodres = models.CharField(max_length=45)
    sugerencias = models.CharField(max_length=45)
    motivo_consulta = models.CharField(max_length=45)
    tareas_proxima_cita = models.CharField(max_length=45)
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, db_column='id_diagnostico')
    id_motivo = models.ForeignKey(MotivoConsulta, on_delete=models.CASCADE, db_column='id_motivo')

    class Meta:
        managed = True
        db_table = 'cita'
        unique_together = (('id_cita', 'id_diagnostico','id_motivo'),)

    def __str__(self):
        return str(self.id_cita)

    
class RegistroXMotivo(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_paciente')
    id_motivo = models.ForeignKey(MotivoConsulta, on_delete=models.CASCADE, db_column='id_motivo')

    class Meta:
        managed = True
        db_table = 'registro_x_motivo'

