from django.db import models

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default=True)
    create_date = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)
    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

    def __str__(self):
        """Unicode representation of BaseModel."""
        pass

