# Generated by Django 3.2.6 on 2021-09-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20210816_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproveedor',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='apellido',
        ),
        migrations.AddField(
            model_name='historicalpago',
            name='fecha',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalpago',
            name='monto',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='historicalproveedor',
            name='nombre_encargado',
            field=models.CharField(max_length=225, null=True, verbose_name='nombre_encargado'),
        ),
        migrations.AddField(
            model_name='pago',
            name='fecha',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='monto',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nombre_encargado',
            field=models.CharField(max_length=225, null=True, verbose_name='nombre_encargado'),
        ),
    ]
