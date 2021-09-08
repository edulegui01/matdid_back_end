from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField, IntegerField
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class Proveedor(BaseModel):
    """Model defin ition for Proveedores."""
    
    # TODO: Define fields here
    cedula = models.IntegerField('cedula', null=False, blank= False)
    nombre = models.CharField('nombre', max_length=225, null=False, blank= False)
    nombre_encargado = models.CharField('nombre_encargado', max_length=225, null=True, blank= False)
    telefono = models.IntegerField('telefono',null=False, blank= False)
    direccion = models.CharField('direccion', max_length=225, null=False, blank= False)
    localidad = models.CharField('localidad', max_length=225, null=True, blank= True)
    email = models.EmailField('correo electronico', max_length=254,blank=True, null=True)
    ruc = models.CharField('Ruc', max_length=225, null=False, blank=False, unique=True)
    razon_social = models.CharField('Razon social', max_length=225, null=False, blank=False)
    total_vendido = models.IntegerField('total vendido',null=False, blank= False)
    total_cobrado = models.IntegerField('total cobrado', null=False, blank=False)
    deuda_por_cobrar = models.IntegerField('deuda por cobrar', null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        """Meta definition for Proveedores."""

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        """Unicode representation of Proveedores."""
        return f"{self.nombre}"   


class Pago(BaseModel):
    """Model definition for Pago."""


    # TODO: Define fields here
    id_proveedor = models.ForeignKey(Proveedor,on_delete=CASCADE)
    fecha = models.DateField(auto_now=True, null=True)
    monto = IntegerField( null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Pago."""

        verbose_name = 'Pago'

        verbose_name_plural = 'Pagos'


    def __str__(self):
        return str({self.id})
