from django.db import models

SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

class Arduino(models.Model):
    serial = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    puerto = models.IntegerField()


class Entrada(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.PROTECT)
    valor = models.FloatField()
    fechaHora = models.DateTimeField(null=True)
    procesado = models.BooleanField()


class Salida(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.PROTECT)
    valor = models.FloatField()
    fechaHora = models.DateTimeField(null=True)
    procesado = models.BooleanField()


class Cliente(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=64)
    foto = models.ImageField(null=True, blank=True)