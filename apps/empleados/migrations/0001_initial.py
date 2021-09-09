# Generated by Django 3.2.6 on 2021-08-15 07:26

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=225, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=225, verbose_name='apellido')),
                ('fecha_nacimi', models.DateField(verbose_name='fecha nacimiento')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('domicilio', models.CharField(max_length=225, verbose_name='domicilio')),
                ('localidad', models.CharField(max_length=225, verbose_name='localidad')),
                ('email', models.EmailField(blank=True, max_length=225, null=True, verbose_name='email')),
                ('fecha_ingre', models.DateField(blank=True, null=True, verbose_name='fecha de ingreso')),
                ('fecha_sal', models.DateField(blank=True, null=True, verbose_name='fecha de salida')),
                ('rol', models.CharField(max_length=225, verbose_name='rol')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEmpleado',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=225, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=225, verbose_name='apellido')),
                ('fecha_nacimi', models.DateField(verbose_name='fecha nacimiento')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('domicilio', models.CharField(max_length=225, verbose_name='domicilio')),
                ('localidad', models.CharField(max_length=225, verbose_name='localidad')),
                ('email', models.EmailField(blank=True, max_length=225, null=True, verbose_name='email')),
                ('fecha_ingre', models.DateField(blank=True, null=True, verbose_name='fecha de ingreso')),
                ('fecha_sal', models.DateField(blank=True, null=True, verbose_name='fecha de salida')),
                ('rol', models.CharField(max_length=225, verbose_name='rol')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Empleado',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
