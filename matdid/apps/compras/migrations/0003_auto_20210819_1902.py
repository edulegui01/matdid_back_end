# Generated by Django 3.2.6 on 2021-08-19 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecompra',
            old_name='id_proveedor',
            new_name='id_producto',
        ),
        migrations.RenameField(
            model_name='historicaldetallecompra',
            old_name='id_proveedor',
            new_name='id_producto',
        ),
    ]
