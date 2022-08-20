from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=100)
    linha2 = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.linha1

    class Meta:
        verbose_name_plural = "Endereços"
