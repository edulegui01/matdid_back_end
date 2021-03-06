# Generated by Django 3.2.6 on 2021-08-15 07:26

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProducto',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=30)),
                ('costo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('porc_iva', models.DecimalField(decimal_places=2, max_digits=2)),
                ('stock_actual', models.IntegerField()),
                ('stock_minimo', models.IntegerField()),
                ('ultima_compra', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=30)),
                ('costo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('porc_iva', models.DecimalField(decimal_places=2, max_digits=2)),
                ('stock_actual', models.IntegerField()),
                ('stock_minimo', models.IntegerField()),
                ('ultima_compra', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
    ]
