# Generated by Django 5.1 on 2024-08-30 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('localidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.localidad')),
                ('provincia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.provincia')),
            ],
        ),
    ]
