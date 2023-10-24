from django.db import models


class LocationStation(models.Model):
    nome_usina = models.CharField(max_length=255, verbose_name="Nome da Usina")
    latitude = models.FloatField(verbose_name="Latitude", default=0.0)
    longitude = models.FloatField(verbose_name="Longitude", default=0.0)
    city = models.CharField(max_length=255, verbose_name="Cidade")
    average_photovoltaic_irradiation = models.FloatField(verbose_name="Media por ano KhW", default=0.0)
    state = models.CharField(max_length=255, verbose_name="Estado")

    def __str__(self):
        return self.nome_usina

    class Meta:
        verbose_name = "Localização"
