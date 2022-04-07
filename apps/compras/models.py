from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.db.models.deletion import CASCADE
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.empleados.models import Empleado
from apps.proveedores.models import Proveedor

class Compra(BaseModel):
    """Model definition for Compra."""

    # TODO: Define fields here
    accion = models.CharField('accion', max_length=225)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Fecha = models.DateField('fecha', auto_now=True, auto_now_add=False)
    monto_total = models.IntegerField()
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Compra."""

        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        """Unicode representation of Compra."""
        return f'{self.id}'


class DetalleCompra(BaseModel):
    """Model definition for DetalleCompra."""

    # TODO: Define fields here
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField(default=0)
    precio_calculado = models.IntegerField()
    descuento = models.DecimalField('descuento', max_digits=5, decimal_places=2, null=True, blank=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for DetalleCompra."""

        verbose_name = 'DetalleCompra'
        verbose_name_plural = 'DetalleCompras'

    def __str__(self):
        return f'{self.id}'



