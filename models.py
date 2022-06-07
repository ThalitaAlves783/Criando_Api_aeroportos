from django.db import models


class Aeroporto(models.Model):
    nome_aeroporto = models.CharField(max_length=30)
    codigo_iata = models.CharField(max_length=3)
    cidade = models.CharField(max_length=30)
    coodigo_pais_iso = models.CharField(max_length=2)
    latitude = models.FloatField(max_length=13)
    longitude = models.FloatField(max_length=13)
    altidute = models.FloatField(max_length=20)

    def __str__(self):
        return self.nome_aeroporto


