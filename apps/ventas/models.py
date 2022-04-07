from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.


class Venta(BaseModel):
    """Model definition for Venta."""

    # TODO: Define fields here
    accion = models.CharField('accion', max_length=225)
    id_empleado = models.ForeignKey('empleados.Empleado', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
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
        """Meta definition for Venta."""

        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        """Unicode representation of Venta."""
        return f'{self.id} {self.accion} {self.id_cliente}'

class DetalleVenta(BaseModel):
    """Model definition for DetalleVenta."""

    # TODO: Define fields here
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField(default=0)
    precio_calculado = models.IntegerField()
    descuento = models.DecimalField('descuento', max_digits=5, decimal_places=2,  null=True, blank=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for DetalleVenta."""

        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'

    def __str__(self):
        """Unicode representation of DetalleVenta."""
        return f'{self.id_venta} {self.id_producto} {self.create_date}'
