from django.db import models

class Productos(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30)
  costo = models.IntegerField()
  precio = models.IntegerField()
  porc_iva = models.DecimalField(max_digits=2,decimal_places=2)
  stock_actual = models.IntegerField()
  stock_minimo = models.IntegerField()
  ultima_compra = models.DateTimeField()


  def __str__(self):
    return self.nombre
