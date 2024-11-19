# Generated by Django 5.1.3 on 2024-11-14 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arduino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
                ('puerto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=64)),
                ('foto', models.ImageField(upload_to='')),
                ('arduino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arduino.arduino')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('fechaHora', models.DateTimeField()),
                ('procesado', models.BooleanField()),
                ('arduino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arduino.arduino')),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('fechaHora', models.DateTimeField()),
                ('procesado', models.BooleanField()),
                ('arduino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arduino.arduino')),
            ],
        ),
    ]