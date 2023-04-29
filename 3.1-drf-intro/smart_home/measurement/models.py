from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    descriprion = models.CharField(max_length=200, verbose_name='Описание')


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateField(auto_now_add=True)
