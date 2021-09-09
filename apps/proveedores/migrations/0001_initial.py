# Generated by Django 3.2.6 on 2021-08-15 07:26

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPago',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Pago',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProveedor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('cedula', models.IntegerField(verbose_name='cedula')),
                ('nombre', models.CharField(max_length=225, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=225, verbose_name='apellido')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('direccion', models.CharField(max_length=225, verbose_name='direccion')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='correo electronico')),
                ('ruc', models.CharField(db_index=True, max_length=225, verbose_name='Ruc')),
                ('razon_social', models.CharField(max_length=225, verbose_name='Razon social')),
                ('total_vendido', models.IntegerField(verbose_name='total vendido')),
                ('total_cobrado', models.IntegerField(verbose_name='total cobrado')),
                ('deuda_por_cobrar', models.IntegerField(verbose_name='deuda por cobrar')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Proveedor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('cedula', models.IntegerField(verbose_name='cedula')),
                ('nombre', models.CharField(max_length=225, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=225, verbose_name='apellido')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('direccion', models.CharField(max_length=225, verbose_name='direccion')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='correo electronico')),
                ('ruc', models.CharField(max_length=225, unique=True, verbose_name='Ruc')),
                ('razon_social', models.CharField(max_length=225, verbose_name='Razon social')),
                ('total_vendido', models.IntegerField(verbose_name='total vendido')),
                ('total_cobrado', models.IntegerField(verbose_name='total cobrado')),
                ('deuda_por_cobrar', models.IntegerField(verbose_name='deuda por cobrar')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]
