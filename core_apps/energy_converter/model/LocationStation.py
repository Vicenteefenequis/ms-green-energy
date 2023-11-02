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


# Supondo que você já importou o modelo LocationStation


def getAnyLocation():
    usinas = []

    usina1 = LocationStation(
        nome_usina="Pirapora",
        latitude=-17.3436,
        longitude=-44.9419,
        city="Pirapora",
        average_photovoltaic_irradiation=2300,  # Apenas um valor aproximado
        state="MG"
    )
    usinas.append(usina1)

    usina2 = LocationStation(
        nome_usina="Nova Olinda",
        latitude=-5.5206,
        longitude=-41.3109,
        city="Ribeira do Piauí",
        average_photovoltaic_irradiation=2400,  # Apenas um valor aproximado
        state="PI"
    )
    usinas.append(usina2)

    usina3 = LocationStation(
        nome_usina="Lapa",
        latitude=-12.7111,
        longitude=-45.9031,
        city="Bom Jesus da Lapa",
        average_photovoltaic_irradiation=2200,  # Apenas um valor aproximado
        state="BA"
    )
    usinas.append(usina3)

    usina4 = LocationStation(
        nome_usina="Ituverava",
        latitude=-14.7806,
        longitude=-40.6497,
        city="Tabocas do Brejo Velho",
        average_photovoltaic_irradiation=2300,  # Apenas um valor aproximado
        state="BA"
    )
    usinas.append(usina4)

    usina5 = LocationStation(
        nome_usina="Anápolis",
        latitude=-3.7015,
        longitude=-38.5986,
        city="Tabuleiro do Norte",
        average_photovoltaic_irradiation=2400,  # Apenas um valor aproximado
        state="CE"
    )
    usinas.append(usina5)

    usina6 = LocationStation(
        nome_usina="Murillo Usina",
        latitude=-16.716439325265053,
        longitude=-49.28054809570313,
        city="Goiânia",
        average_photovoltaic_irradiation=10000000,  # Apenas um valor aproximado
        state="GO"
    )
    usinas.append(usina6)
    return usinas
