# Generated by Django 3.2.6 on 2021-09-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='encargado',
            field=models.CharField(max_length=225, null=True, verbose_name='encargado'),
        ),
        migrations.AddField(
            model_name='historicalcliente',
            name='encargado',
            field=models.CharField(max_length=225, null=True, verbose_name='encargado'),
        ),
    ]
