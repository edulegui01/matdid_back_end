from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.


class Factura(BaseModel):
    """Model definition for Factura."""

    # TODO: Define fields here
    fecha = models.DateField('fecha de la factura', auto_now=True, auto_now_add=False)
    id_venta = models.ForeignKey('ventas.Venta', on_delete=models.CASCADE)
    monto_total = models.IntegerField()
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        """Unicode representation of Factura."""
        pass

