# Generated by Django 3.2.6 on 2021-08-29 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalventa',
            old_name='id_proveedor',
            new_name='id_cliente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='id_proveedor',
            new_name='id_cliente',
        ),
    ]
