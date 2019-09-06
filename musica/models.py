from django.db import models


# Create your models here.
class Musica(models.Model):
    nomeDaMusica = models.CharField(
        max_length=255,
    )
    artista = models.CharField(
        max_length=255,
    )
    linkDaMusica = models.CharField(
        max_length=255,
    )
    generoMusical = models.CharField(
        max_length=255,
    )