# Generated by Django 5.1 on 2024-09-01 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolocalizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('localidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geolocalizacion.localidad')),
                ('provincia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geolocalizacion.provincia')),
            ],
        ),
    ]
