from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.

class Empleado(BaseModel):
    cedula = models.IntegerField()
    nombre = models.CharField('nombre', max_length=225,null=False,blank=False)
    apellido = models.CharField('apellido', max_length=225,null=False,blank=False)
    fecha_nacimi = models.DateField('fecha nacimiento',auto_now=False, auto_now_add=False)
    telefono = models.IntegerField('telefono')
    domicilio = models.CharField('domicilio', max_length=225,null=False,blank=False)
    localidad = models.CharField('localidad', max_length=225, null=False, blank=False)
    email = models.EmailField('email', max_length=225, null=True, blank=True)
    rol = models.CharField('rol', max_length=225,null=False,blank=False)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        """Meta definition for Empleados."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleados."""
        return f"{self.nombre} {self.apellido}"   
