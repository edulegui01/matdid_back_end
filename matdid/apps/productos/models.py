from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords


class Producto(BaseModel):
  nombre = models.CharField(max_length=225)
  descripcion = models.CharField(max_length=225, null=True)
  autor = models.CharField(max_length=225, null=True)
  costo = models.IntegerField()
  precio = models.IntegerField()
  stock_actual = models.IntegerField()
  stock_minimo = models.IntegerField()
  historical = HistoricalRecords()

  @property
  def _history_user(self):
    return self.changed_by

  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value


  def __str__(self):
    return f'{self.nombre}'
