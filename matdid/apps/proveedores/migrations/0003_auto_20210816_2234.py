# Generated by Django 3.2.6 on 2021-08-17 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproveedor',
            name='localidad',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='localidad'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='localidad',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='localidad'),
        ),
    ]
