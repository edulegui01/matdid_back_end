from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.

class Cliente(BaseModel):
    """Model definition for Cliente."""

    # TODO: Define fields here
    nombre = models.CharField('nombre', max_length=225, null=False, blank=False)
    sector = models.CharField('sector', max_length=225, null=False, blank=False)
    localidad = models.CharField('localidad', max_length=225, null=False, blank=False)
    nombre_encargado = models.CharField('nombre encargado', max_length=225,null=False, blank=False)
    telefono = models.IntegerField()
    direccion = models.CharField('direccion', max_length=225, null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    ruc = models.IntegerField()
    razon_social = models.CharField('razon_social', max_length=225)
    total_comprado = models.IntegerField()
    total_pagado = models.IntegerField()
    deuda_por_pagar = models.IntegerField()
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.nombre

class Cobro(BaseModel):
    """Model definition for Cobro."""

    # TODO: Define fields here
    id_cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    monto = models.IntegerField()
    fecha = models.DateField(auto_now=True, null=True)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Cobro."""

        verbose_name = 'Cobro'
        verbose_name_plural = 'Cobros'

    def __str__(self):
        """Unicode representation of Cobro."""
        return f'{self.id_cliente} {self.monto}'
